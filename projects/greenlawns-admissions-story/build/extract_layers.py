"""Cut the flat Greenlawns poster into animatable layers.

usage: python build/extract_layers.py   (run from the project folder)
Reads  ../../clients/greenlawns/assets/source/admissions-2027-poster.jpeg (3240x5760, never modified)
Writes assets/layers/*.png (2x of the 1080 frame) and assets/layers/manifest.json (boxes in 1080 px).

Why: the client supplied only a flattened JPEG, so every element is keyed out of it: text by colour,
brush strokes / ticks / pill / wave against the cream background, puzzle pieces along their white gutters.
If the layered Canva exports arrive, replace the matching PNGs and keep the manifest boxes.
"""
import json
import pathlib

import numpy as np
from PIL import Image, ImageDraw

HERE = pathlib.Path(__file__).resolve().parent.parent
SRC = HERE / "../../clients/greenlawns/assets/source/admissions-2027-poster.jpeg"
OUT = HERE / "assets/layers"
OUT.mkdir(parents=True, exist_ok=True)

A = np.asarray(Image.open(SRC).convert("RGB")).astype(np.float32)
CREAM = np.array([253, 245, 236], np.float32)
YELLOW = np.array([252, 211, 17], np.float32)
S = 3.0          # source px per 1080-frame px
OUT_SCALE = 2.0  # exported px per 1080-frame px
manifest = {}


# ---------- helpers ----------
def box_blur(x, r):
    """Separable box blur of a 2D float array (radius r, edge-clamped)."""
    if r < 1:
        return x
    for ax in (0, 1):
        pad = [(0, 0), (0, 0)]
        pad[ax] = (r + 1, r)
        p = np.pad(x, pad, mode="edge")
        c = np.cumsum(p, axis=ax)
        x = (np.take(c, range(2 * r + 1, c.shape[ax]), axis=ax) - np.take(c, range(0, c.shape[ax] - 2 * r - 1), axis=ax)) / (2 * r + 1)
    return x


def gauss(x, s):
    r = max(1, int(round(s * 0.93)))   # three box passes ~ gaussian of sigma s
    for _ in range(3):
        x = box_blur(x, r)
    return x


def dilate(mask, dist):
    """Rounded dilation by ~dist px."""
    return gauss(mask.astype(np.float32), dist / 2.05) > 0.02


def ramp(x, lo, hi):
    return np.clip((x - lo) / (hi - lo), 0, 1)


def lum(c):
    return c[..., 0] * 0.299 + c[..., 1] * 0.587 + c[..., 2] * 0.114


def fill_holes(mask):
    """Fill regions of ~mask that are not connected to the crop border."""
    h, w = mask.shape
    im = Image.fromarray(np.pad(np.where(mask, 0, 255).astype(np.uint8), 1, constant_values=255)).copy()  # copy: a numpy-backed image ignores floodfill
    ImageDraw.floodfill(im, (0, 0), 128)
    outside = np.asarray(im)[1:-1, 1:-1] == 128
    return ~outside


def save(name, rgb, alpha, x0, y0, trim=True):
    """Save a layer cut from source box at (x0, y0); trims empty borders; records its 1080 box."""
    if trim:
        ys, xs = np.where(alpha > 0.004)
        if len(xs) == 0:
            raise SystemExit(f"{name}: empty")
        t, b, l, r = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
        # snap to multiples of 3 so 1080 boxes are whole numbers at OUT_SCALE
        l, t = l - l % 3, t - t % 3
        r, b = r + (-r) % 3, b + (-b) % 3
        rgb, alpha = rgb[t:b, l:r], alpha[t:b, l:r]
        x0, y0 = x0 + l, y0 + t
    h, w = alpha.shape
    rgba = np.dstack([np.clip(rgb, 0, 255), np.clip(alpha, 0, 1) * 255]).astype(np.uint8)
    im = Image.fromarray(rgba, "RGBA")
    ow, oh = int(round(w / S * OUT_SCALE)), int(round(h / S * OUT_SCALE))
    im = im.resize((ow, oh), Image.LANCZOS)
    im.save(OUT / f"{name}.png", optimize=True)
    manifest[name] = {"x": round(x0 / S, 2), "y": round(y0 / S, 2), "w": round(w / S, 2), "h": round(h / S, 2)}
    return manifest[name]


def crop(x0, y0, x1, y1):
    return A[y0:y1, x0:x1].copy()


def cream_alpha(c, lo=26, hi=95):
    d = np.abs(c - CREAM).sum(2)
    return ramp(d, lo, hi)


def unmix(c, alpha, bg=CREAM):
    """Foreground colour of a pixel that is alpha*F + (1-alpha)*bg."""
    a = np.maximum(alpha, 1e-3)[..., None]
    return (c - (1 - a) * bg) / a


def split_columns(alpha, min_gap):
    """Column ranges holding content, split where at least min_gap empty columns sit between them."""
    on = alpha.max(0) > 0.5
    runs, start, gap = [], None, 0
    for i, v in enumerate(on):
        if v:
            if start is None:
                start = i
            gap = 0
            end = i
        elif start is not None:
            gap += 1
            if gap >= min_gap:
                runs.append((start, end + 1)); start = None
    if start is not None:
        runs.append((start, end + 1))
    return runs


def components(binary, min_px=2000):
    """Connected blobs of a boolean mask, largest first skipped below min_px. Returns a list of masks."""
    work = Image.fromarray(np.where(binary, 255, 0).astype(np.uint8)).copy()
    out = []
    while True:
        arr = np.asarray(work)
        ys, xs = np.nonzero(arr == 255)
        if len(xs) == 0:
            return out
        ImageDraw.floodfill(work, (int(xs[0]), int(ys[0])), 128, thresh=0)
        arr = np.asarray(work).copy()
        comp = arr == 128
        arr[comp] = 0
        work = Image.fromarray(arr).copy()
        if comp.sum() >= min_px:
            out.append(comp)


def split_rows(alpha, min_gap):
    return split_columns(alpha.T, min_gap)


# ---------- 1. headline: yellow brush + dark green letters ----------
x0, y0, x1, y1 = 330, 270, 2975, 1320
c = crop(x0, y0, x1, y1)
L = lum(c)
yel = (c[..., 0] > 200) & (c[..., 2] < 120)
yel[: 560 - y0, : 560 - x0] = False           # the logo's flame is yellow too
yhull = fill_holes(dilate(yel, 3))
near = dilate(yhull, 150)                     # letters may overhang the brush (the last S does)
for bx0, by0, bx1, by1 in [(0, 0, 560, 560), (170, 730, 390, 1090), (2570, 945, 2820, 1240), (0, 1262, 3240, 1400)]:
    near[max(by0 - y0, 0):max(by1 - y0, 0), max(bx0 - x0, 0):max(bx1 - x0, 0)] = False   # logo, ticks, ribbon
txt = ramp(185 - L, 0, 120) * near            # dark green ink (lum ~55) vs yellow (~195) and cream (~245)
brush_a = cream_alpha(c) * dilate(yhull, 6)
brush_a = np.maximum(brush_a, yhull * 1.0)
brush_rgb = unmix(c, np.maximum(brush_a, 1e-3))
brush_rgb = brush_rgb * (1 - txt[..., None]) + YELLOW * txt[..., None]
brush_rgb[brush_a < 0.95] = YELLOW               # soft dry-brush edges: flat yellow, no unmix fringes
save("head_brush", brush_rgb, brush_a * yhull + brush_a * (1 - yhull) * (1 - txt), x0, y0)
ink = np.median(c[txt > 0.98], axis=0)
rgb_ink = np.broadcast_to(ink, c.shape)
letters = components(txt > 0.5)
cents = [(np.nonzero(m)[1].mean(), np.nonzero(m)[0].mean(), m) for m in letters]
cy = np.array([q[1] for q in cents])
split = (cy.min() + cy.max()) / 2
counts = {"admissions": 0, "open": 0}
for cx_, cy_, m in sorted(cents, key=lambda q: q[0]):
    word = "admissions" if cy_ < split else "open"
    a = txt * dilate(m, 5)
    save(f"h_{word}_{counts[word]}", rgb_ink, a, x0, y0)
    counts[word] += 1
print("headline letters", counts)
assert counts == {"admissions": 10, "open": 4}, counts

# ---------- 2. year ribbon: green banner + white digits ----------
x0, y0, x1, y1 = 760, 1262, 2480, 1665
c = crop(x0, y0, x1, y1)
ra = cream_alpha(c)
ra = ra * (1 - dilate((c[..., 0] > 170) & (c[..., 2] < 150) & (c[..., 1] > 140), 4))   # bottom of the yellow brush is in this crop
hull = fill_holes(ra > 0.5)
inner = ~dilate(~hull, 14)
white = ramp(lum(c), 120, 235) * inner
rib_rgb = unmix(c, np.maximum(ra, 1e-3))
green = np.median(c[hull & (white < 0.02) & (ra > 0.99)], axis=0)
rib_rgb = rib_rgb * (1 - white[..., None]) + green * white[..., None]
rib_a = np.maximum(ra, hull * 1.0)
save("ribbon", rib_rgb, rib_a, x0, y0)
save("year", np.full_like(c, 255), white, x0, y0)

# ---------- 3. tick bursts (each group one layer) ----------
ticks = {
    "tk_head_l": (170, 730, 390, 1090), "tk_head_r": (2570, 945, 2820, 1240),
    "tk_year_l": (525, 1310, 750, 1645), "tk_year_r": (2490, 1310, 2710, 1640),
    "tk_date_l": (145, 4712, 372, 5055), "tk_date_r": (2890, 4628, 3100, 4972),
}
for name, (x0, y0, x1, y1) in ticks.items():
    c = crop(x0, y0, x1, y1)
    a = cream_alpha(c)
    save(name, unmix(c, a), a, x0, y0)

# ---------- 4. date: dark green brush + yellow words + yellow underline ----------
x0, y0, x1, y1 = 355, 4510, 2880, 5165
c = crop(x0, y0, x1, y1)
da = cream_alpha(c)
uline = np.zeros(da.shape, bool)
uline[5008 - y0:] = (c[5008 - y0:, :, 2] < 150) & (c[5008 - y0:, :, 1] > 150)   # the yellow underline below the brush
da = da * (1 - dilate(uline, 3))
dgreen = np.array([24, 111, 60], np.float32)
v = YELLOW - dgreen
t = np.clip(((c - dgreen) * v).sum(2) / (v * v).sum(), 0, 1)
hull = fill_holes(da > 0.5)
t = ramp(t, 0.5, 0.9) * hull * ramp(200 - c[..., 2], 0, 80)
t[5008 - y0:] = 0   # yellow has almost no blue; cream bristle gaps do
# brush keeps its own texture; text pixels are replaced by the brush green
d_rgb = unmix(c, np.maximum(da, 1e-3))
d_rgb = d_rgb * (1 - t[..., None]) + dgreen * t[..., None]
yellowish = (c[..., 0] > 150) & (c[..., 2] < 130) & (c[..., 0] - c[..., 1] < 90)
d_rgb[yellowish | (t > 0) | (da < 0.95)] = dgreen   # text edge and soft brush-edge pixels: flat brush green
save("date_brush", d_rgb, np.maximum(da, hull * 1.0), x0, y0)
ytxt = np.median(c[t > 0.98], axis=0)
rgb_y = np.broadcast_to(ytxt, c.shape)
words = split_columns(t, 8)
names = ["d_21st", "d_november"]
# the widest gap separates "21st" from "November"
gaps = [(words[i + 1][0] - words[i][1], i) for i in range(len(words) - 1)]
cut = max(gaps)[1]
print("date runs", words, "cut after", cut)
groups = [(words[0][0], words[cut][1]), (words[cut + 1][0], words[-1][1])]
for name, (k0, k1) in zip(names, groups):
    a = np.zeros_like(t); a[:, k0:k1] = t[:, k0:k1]
    save(name, rgb_y, a, x0, y0)

x0, y0, x1, y1 = 880, 5008, 2440, 5160
c = crop(x0, y0, x1, y1)
a = cream_alpha(c) * (c[..., 2] < 150)    # yellow only, no grid or green
save("date_line", unmix(c, np.maximum(a, 1e-3)), a, x0, y0)

# ---------- 5. tagline words ----------
x0, y0, x1, y1 = 420, 5200, 2790, 5375
c = crop(x0, y0, x1, y1)
a = cream_alpha(c, 40, 160)
rgb = unmix(c, np.maximum(a, 1e-3))
words = split_columns(a, 22)
assert len(words) == 7, words
for i, (k0, k1) in enumerate(words):
    aw = np.zeros_like(a); aw[:, k0:k1] = a[:, k0:k1]
    save(f"tag_{i}", rgb, aw, x0, y0)

# ---------- 6. url pill ----------
x0, y0, x1, y1 = 1130, 5392, 2026, 5582
c = crop(x0, y0, x1, y1)
pa = cream_alpha(c)
hull = fill_holes(pa > 0.5)
save("url", c, np.maximum(pa, hull * 1.0), x0, y0)

# ---------- 7. bottom wave (pill area removed) ----------
x0, y0, x1, y1 = 0, 5370, 3240, 5760      # starts below the tagline descenders
c = crop(x0, y0, x1, y1)
wa = cream_alpha(c)
py0, py1, px0, px1 = 5392 - y0, 5582 - y0, 1130, 2026
pill = np.zeros_like(wa, bool); pill[py0:py1, px0:px1] = hull
wa = np.where(dilate(pill, 6), 0, wa)
save("wave", unmix(c, np.maximum(wa, 1e-3)), wa, x0, y0, trim=False)

# ---------- 8. puzzle pieces ----------
x0, y0, x1, y1 = 170, 1665, 3060, 4440
c = crop(x0, y0, x1, y1)
h, w = c.shape[:2]
white = (c.min(2) > 234) & (c[..., 0] - c[..., 2] < 9)   # pure white; the cream has ~17 less blue than red
im = Image.fromarray(np.where(white, 255, 0).astype(np.uint8)).copy()
assert white[1688 - y0, 900 - x0], "gutter seed must be white"
ImageDraw.floodfill(im, (900 - x0, 1688 - y0), 128, thresh=0)    # the gutter network, seeded on the top border
gutter = np.asarray(im) == 128
# white paper touching the gutter joins the flood; the real gutter is <45 px wide, so anything that survives a
# 30 px erosion is paper. Grow it back by only 20 px so a thin band of gutter still separates the pieces.
paper = dilate(~dilate(~gutter, 30), 20) & gutter
gutter &= ~paper
# paper with colour dots is too broken up for the erosion test: mark it by hand (source px, clear of real gutters,
# which sit at x 1591-1627, y 3012-3053 and on the outer border)
for zx0, zy0, zx1, zy1 in [(1200, 2770, 1584, 3004),     # drawing sheet, bottom of the top-left piece
                           (1700, 4240, 2990, 4398)]:    # notebook, bottom of the bottom-right piece
    gutter[zy0 - y0:zy1 - y0, zx0 - x0:zx1 - x0] = False
print("paper px", int(paper.sum()))
outside = ~fill_holes(gutter | ~(cream_alpha(c) < 0.5) | white)
free = ~gutter & ~outside
print("gutter px", int(gutter.sum()), "outside px", int(outside.sum()), "of", gutter.size)
seeds = {"tl": (700, 2300), "tr": (2400, 2300), "bl": (700, 3800), "br": (2400, 3800)}
HALF = 19     # half the 37 px inner gutter; the outer border is ~21 px
PAD = 72      # extra photo around each piece so push-ins never show an edge
claimed = np.zeros((h, w), bool)
for key, (sx, sy) in seeds.items():
    assert free[sy - y0, sx - x0], key
    im = Image.fromarray(np.where(free, 255, 0).astype(np.uint8)).copy()
    ImageDraw.floodfill(im, (sx - x0, sy - y0), 128, thresh=0)
    m = np.asarray(im) == 128
    assert not (m & claimed).any(), key
    claimed |= m
    m = fill_holes(m)
    m = gauss(m.astype(np.float32), 1.2) > 0.5            # smooth the stair-steps
    inner = np.clip(gauss(m.astype(np.float32), 0.8), 0, 1)
    outer = np.clip(gauss(dilate(m, HALF).astype(np.float32), 0.8), 0, 1)
    ys, xs = np.where(outer > 0.004)
    t, b, l, r = ys.min() - PAD, ys.max() + 1 + PAD, xs.min() - PAD, xs.max() + 1 + PAD
    t, l = max(t - t % 3, 0), max(l - l % 3, 0)
    b, r = min(b + (-b) % 3, h), min(r + (-r) % 3, w)
    # photo with its colours pushed outwards (push-pull fill) beyond the piece edge
    known = (gauss(m.astype(np.float32), 1.0) > 0.98).astype(np.float32)
    photo = c * known[..., None]
    acc_c, acc_k = photo.copy(), known.copy()
    filled = c.copy()
    have = known > 0.5
    for s in (3, 6, 12, 24, 48, 96):
        bc = np.dstack([gauss(acc_c[..., i], s) for i in range(3)])
        bk = gauss(acc_k, s)
        est = bc / np.maximum(bk, 1e-4)[..., None]
        newly = (~have) & (bk > 0.02)
        filled[newly] = est[newly]
        have |= newly
    filled[known > 0.5] = c[known > 0.5]
    sl = (slice(t, b), slice(l, r))
    save(f"pz_{key}_photo", filled[sl], np.ones_like(inner[sl]), x0 + l, y0 + t, trim=False)
    save(f"pz_{key}_mask", np.full_like(c[sl], 255), inner[sl], x0 + l, y0 + t, trim=False)
    save(f"pz_{key}_frame", np.full_like(c[sl], 255), np.clip(outer[sl] - inner[sl] * 0.0, 0, 1) * (1 - np.clip(inner[sl] * 1.6 - 0.6, 0, 1)), x0 + l, y0 + t, trim=False)
    print(key, "piece px", int(m.sum()), "box", manifest[f"pz_{key}_photo"])

(OUT / "manifest.json").write_text(json.dumps(manifest, indent=1))
print(len(manifest), "layers ->", OUT)
