"""Build a project's soundtrack: synthesized music bed + SFX on cue + voice-over, ducked and loudness-normalised.

usage: python tools/make_audio.py <project_dir>
Reads <project_dir>/cues.json and writes <project_dir>/assets/audio.wav (git-ignored, re-run after any timing change).
Needs ffmpeg on PATH and pip install numpy. Everything is generated from code, so there are no music rights issues.

cues.json (all times are absolute video seconds and MUST match the scene/cue times in index.html):
{
  "duration": 12.5,                   # video length in seconds
  "vo": "assets/vo.mp3",              # voice-over file relative to the project, or null for no voice
  "vo_offset": 0.2,                   # where the VO starts in the video (Whisper times are file times: add this)
  "music": {"bpm": 120, "key": 0,     # key = semitones up from C major (e.g. 2 = D); "music": false = no bed
            "gain": 0.55, "end_card": 9.4},   # from end_card on the bed thins out to pad + sparse arp
  "sfx": [                            # one entry per sound; gain (default 1) and pan (-1 left .. 1 right) optional
    {"t": 3.1, "type": "cut"},        # cut = short whoosh into a tick, use on every scene change
    {"t": 4.2, "type": "pop"},        # pop = something appears (icon, sticker, badge)
    {"t": 5.0, "type": "whoosh", "dur": 0.4},
    {"t": 6.0, "type": "tick"},       # tick = small UI hit (check marks, counters); "type" = keyboard click
    {"t": 9.4, "type": "riser", "dur": 1.4},  # riser PEAKS at t (it starts dur seconds earlier)
    {"t": 9.4, "type": "impact"},     # impact = low boom for the end card / big reveal
    {"t": 9.5, "type": "chime", "note": 72}, # chime = bell, MIDI note (72 = C5)
    {"t": 2.0, "type": "kick"}
  ]
}
"""
import json
import os
import pathlib
import subprocess
import sys
import wave

import numpy as np

FF = os.environ.get("FFMPEG", "ffmpeg")
SR = 48000
proj = pathlib.Path(sys.argv[1]).resolve()
cfg = json.loads((proj / "cues.json").read_text(encoding="utf-8"))
DUR = float(cfg["duration"])
N = int(SR * DUR)
rng = np.random.default_rng(7)  # fixed seed: the same cues always give the same file
L = np.zeros(N)
R = np.zeros(N)


def hz(m):
    return 440.0 * 2 ** ((m - 69) / 12)


def tt(d):
    return np.arange(int(SR * d)) / SR


def add(sig, t, g=1.0, pan=0.0):
    i = int(round(t * SR))
    if i >= N:
        return
    if i < 0:
        sig, i = sig[-i:], 0
    sig = sig[: N - i] * g
    L[i:i + len(sig)] += sig * np.sqrt((1 - pan) / 2)
    R[i:i + len(sig)] += sig * np.sqrt((1 + pan) / 2)


def hp(x):
    return x - np.concatenate([[0], x[:-1]])


def lp(x, k):
    if k <= 1:
        return x
    c = np.cumsum(np.concatenate([[0], x]))
    y = (c[k:] - c[:-k]) / k
    return np.concatenate([y, np.zeros(k - 1)])


# ---------- instruments (soft) ----------
def pad(notes, d):
    t = tt(d)
    x = sum(np.sin(2 * np.pi * hz(m) * t) + 0.5 * np.sin(2 * np.pi * hz(m) * 1.003 * t)
            + 0.25 * np.sin(2 * np.pi * hz(m) * 2 * t) for m in notes)
    e = np.minimum(1, t / 0.6) * np.minimum(1, (d - t) / 0.6)
    return x * e * 0.03


def pluck(m, d=0.22):
    t = tt(0.5)
    f = hz(m)
    x = np.sin(2 * np.pi * f * t) + 0.3 * np.sin(2 * np.pi * 2 * f * t)
    return x * np.exp(-t / d) * 0.05


def softkick():
    t = tt(0.3)
    f = 50 + 70 * np.exp(-t / 0.025)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.12) * 0.35


def shaker():
    t = tt(0.06)
    return hp(rng.uniform(-1, 1, len(t))) * np.exp(-t / 0.018) * 0.035


def bass(m, d=0.9):
    t = tt(d)
    e = np.minimum(1, t / 0.02) * np.exp(-t / 0.6)
    return np.sin(2 * np.pi * hz(m) * t) * e * 0.16


# ---------- sfx ----------
def whoosh(d=0.3, g=1.0):
    t = tt(d)
    x = rng.uniform(-1, 1, len(t))
    x = lp(x, 3) - lp(x, 30)
    return x * np.sin(np.pi * np.clip(t / d, 0, 1)) ** 2 * 0.22 * g


def tick(g=1.0):
    t = tt(0.05)
    return (np.sin(2 * np.pi * 2400 * t) * 0.5 + hp(rng.uniform(-1, 1, len(t))) * 0.5) * np.exp(-t / 0.007) * 0.14 * g


def type_click():
    t = tt(0.04)
    return (hp(rng.uniform(-1, 1, len(t))) * 0.6 + np.sin(2 * np.pi * 1500 * t)) * np.exp(-t / 0.005) * 0.09


def pop(g=1.0):
    t = tt(0.14)
    f = 1100 * np.exp(-t / 0.025) + 380
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.045) * 0.16 * g


def riser(d):
    t = tt(d)
    x = rng.uniform(-1, 1, len(t))
    x = hp(x) * 0.4 + lp(x, 10)
    sweep = np.sin(2 * np.pi * np.cumsum(300 + 1500 * (t / d) ** 2) / SR) * 0.2
    return (x * 0.4 + sweep) * (t / d) ** 2.4 * 0.22


def impact(d=2.2):
    t = tt(d)
    f = 38 + 70 * np.exp(-t / 0.06)
    boom = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.6)
    air = lp(hp(rng.uniform(-1, 1, len(t))), 4) * np.exp(-t / 0.35) * 0.3
    return (boom * 0.55 + air) * 0.7


def chime(m, d=1.6):
    t = tt(d)
    x = sum(np.sin(2 * np.pi * hz(m) * k * t) / k ** 1.5 for k in (1, 2, 3, 4.2))
    return x * np.exp(-t / 0.5) * 0.06


# ---------- music bed: Imaj7 vi7 IVmaj7 V, light ----------
music = cfg.get("music") or False
MUSIC_G = 0.0
if music:
    k = int(music.get("key", 0))
    beat = 60.0 / float(music.get("bpm", 120))
    BAR = 4 * beat
    END = float(music.get("end_card", DUR))
    MUSIC_G = float(music.get("gain", 0.55))
    CH = [[60, 64, 67, 71], [57, 60, 64, 67], [53, 57, 60, 64], [55, 59, 62, 67]]
    RT = [36, 33, 29, 31]
    ARP = [[72, 76, 79, 83], [69, 72, 76, 79], [65, 69, 72, 76], [67, 71, 74, 79]]
    for b in range(int(DUR / BAR) + 1):
        bt = b * BAR
        ci = b % 4
        add(pad([m + k for m in CH[ci]], BAR + 0.5), bt)
        add(bass(RT[ci] + k, BAR * 0.8), bt)
        for s in range(8):  # eighth notes
            st = bt + s * beat / 2
            if st >= DUR:
                break
            if st < END:
                if s % 2 == 0:
                    add(softkick(), st, 0.55 if st > 2 * beat * 2 else 0.0)  # kick enters after the first 4 beats
                add(shaker(), st, 1.0 if s % 2 else 0.5, 0.3)
                add(pluck(ARP[ci][s % 4] + k), st, 0.8, -0.35 if s % 2 else 0.35)
            elif s % 2 == 0:  # end card: pad + sparse high arp only
                add(pluck(ARP[ci][s % 4] + k + 12, 0.35), st, 0.6, -0.3 if s % 4 else 0.3)
music_L, music_R = L.copy(), R.copy()
L[:] = 0
R[:] = 0

# ---------- sfx cues ----------
for c in cfg.get("sfx", []):
    t, g, pan, ty = float(c["t"]), float(c.get("gain", 1.0)), float(c.get("pan", 0.0)), c["type"]
    d = c.get("dur")
    if ty == "cut":
        add(whoosh(0.3, 0.9), t - 0.15, g, pan - 0.2)
        add(tick(), t, g, pan)
    elif ty == "whoosh":
        add(whoosh(d or 0.3), t, g, pan)
    elif ty == "tick":
        add(tick(), t, g, pan)
    elif ty == "type":
        add(type_click(), t, g, pan)
    elif ty == "pop":
        add(pop(), t, g, pan)
    elif ty == "riser":
        add(riser(d or 1.0), t - (d or 1.0), g, pan)
    elif ty == "impact":
        add(impact(), t, g, pan)
    elif ty == "chime":
        add(chime(int(c.get("note", 72)), d or 1.6), t, g, pan)
    elif ty == "kick":
        add(softkick(), t, g, pan)
    else:
        sys.exit(f"unknown sfx type {ty!r} at {t}")
sfx_L, sfx_R = L.copy(), R.copy()

# ---------- voiceover + ducking ----------
vo = np.zeros(N)
if cfg.get("vo"):
    raw = subprocess.run([FF, "-v", "error", "-i", str(proj / cfg["vo"]), "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    src = np.frombuffer(raw, np.float32).astype(np.float64)
    i0 = int(float(cfg.get("vo_offset", 0.2)) * SR)
    seg = src[: max(0, N - i0)]
    vo[i0:i0 + len(seg)] = seg
env = np.sqrt(lp(vo ** 2, int(0.05 * SR)))
env = env / (env.max() + 1e-9)
duck = 1.0 - 0.55 * lp(np.clip(env * 12, 0, 1), int(0.25 * SR))  # music drops to ~45% under the voice

out_L = music_L * duck * MUSIC_G + sfx_L * 0.8 + vo
out_R = music_R * duck * MUSIC_G + sfx_R * 0.8 + vo
mix = np.stack([out_L, out_R], 1)
fade = np.ones(N)
fade[: int(0.02 * SR)] = np.linspace(0, 1, int(0.02 * SR))
fo = min(N, int(1.8 * SR))
fade[-fo:] = np.linspace(1, 0, fo) ** 1.5
mix *= fade[:, None]
peak = np.abs(mix).max()
if peak > 0:
    mix *= 0.89 / peak

out = proj / "assets" / "audio.wav"
out.parent.mkdir(exist_ok=True)
tmp = out.with_suffix(".tmp.wav")
with wave.open(str(tmp), "wb") as w:
    w.setnchannels(2)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes((mix * 32767).astype("<i2").tobytes())
subprocess.run([FF, "-v", "error", "-y", "-i", str(tmp), "-af", "loudnorm=I=-15:TP=-1.5:LRA=11", "-ar", str(SR),
                "-c:a", "pcm_s16le", str(out)], check=True)
tmp.unlink()
print("wrote", out)
