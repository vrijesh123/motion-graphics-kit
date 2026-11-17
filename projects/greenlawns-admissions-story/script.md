# Greenlawns: "Admissions open 2027-2028" Instagram story

## Decisions and feedback (newest last)
- 2026-11-17: user chose **option A, "Pieces find their place"**, from three proposals (A: puzzle assembles; B: zoom-out
  reveal; C: whole poster with light motion). Greenlawns is its own client: branch `greenlawns`, pack `clients/greenlawns/`.
- 2026-11-17: the Canva link (canva.link/lvwpaqd5pq98p6y) opens the editor and needs the user's Canva login, so it
  could not be read. v1 is built entirely from the flat poster JPEG plus the crest PNG the user supplied.
- 2026-11-17: copy, capitals and colours are the poster's own (client artwork), not the kit's sentence-case /
  one-accent defaults. No voice-over; music bed + SFX only.
- 2026-11-17: the whole poster is shown at 0.82 scale (`POSTER_SCALE`, `POSTER_Y` in `index.html`) so the crest sits
  below Instagram's profile bar (top at y≈215) and the url above the reply bar (bottom at y≈1694). Wave and grid stay
  full-frame. **Needs the school's OK**; `POSTER_SCALE = 1, POSTER_Y = 0` restores the original layout.
- 2026-11-17: v1 rendered: `outputs/greenlawns-admissions-story-v1-12s.mp4`.

## Format
1080x1920, 30 fps, 12 s, one scene. Message on screen by ~1.3 s (stories get tapped through); the complete poster
holds from 6.4 s to 12 s.

## Shot table (no VO, times are the animation's own)
| Time | On screen | Motion | Sound |
|---|---|---|---|
| 0.0-0.6 | Cream grid, green wave | Wave rises from the bottom | |
| 0.05 | Crest | Pops in with a small turn | pop |
| 0.1-0.95 | Yellow brush, "ADMISSIONS OPEN" | Brush paints on left to right; letters warp in one by one | whoosh |
| 0.72 | Green tick marks | Burst outwards | |
| 0.85-1.35 | Ribbon "2027-2028", red ticks | Ribbon opens from the centre, year rises in, ticks burst | whoosh, pop |
| 1.55-3.25 | Four puzzle photos | Fly in from the sides (TL, TR, BL, BR, 0.4 s apart) with a lift shadow, click into place | whoosh + tick per piece |
| 3.3 | Complete puzzle | Small settle pulse | chime |
| 3.85-4.9 | "21st November", underline, ticks | Green brush paints on, "21st" pops, "November" slides in, underline draws | whoosh, pop |
| 5.0-5.95 | "Every child finds their place to grow." | Word by word | |
| 6.05 | greenlawns.org pill | Pops in | pop, chime |
| 6.4-12.0 | Full poster | Slow push-in inside each photo (aimed at faces, away from the garbled shirt crests), gentle camera push, tick pulses at 7.2 / 9.2 / 11.0, wave breathes, crest sways | music thins |

## How it is built
- `build/extract_layers.py` cuts the poster (`clients/greenlawns/assets/source/admissions-2027-poster.jpeg`, never
  modified) into 48 PNG layers in `assets/layers/` with `manifest.json` (boxes in poster px). Text is keyed by colour,
  brushes/ticks/pill/wave against the cream, puzzle pieces along their white gutters (photo + mask + white frame, photo
  padded outwards so push-ins never show an edge).
- `build/make_index.py` + `build/index.tpl.html` wrote `index.html`. **Edit `build/index.tpl.html` and re-run
  `make_index.py`** (it overwrites `index.html`), or edit `index.html` directly and stop using the generator.
- Soundtrack: `cues.json` → `npm run audio`. There are no scene cuts, so there are no `cut` cues.

## Open
- Canva layers: if the user exports elements as transparent PNGs (or shares view access), replace the matching
  layers in `assets/layers/` and keep the manifest boxes.
- Instagram link sticker to greenlawns.org: added in the Instagram app when posting; it can sit on the wave strip.
- School to approve the 0.82 safe-zone scaling, and confirm what "21st November" is (copy is used verbatim).
