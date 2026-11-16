---
name: make-motion-video
description: End-to-end pipeline for a vertical 2D motion graphics video in this kit, from brief to script, voice-over timing, HyperFrames composition, soundtrack and rendered MP4. Use when the user asks to make, build, produce, animate or revise a motion graphics video, reel, explainer or promo, or to write its script.
---

# Make a 2D motion graphics video

Read `/hyperframes` (HyperFrames skill) before writing any composition code, and `motion-graphics-2d` for craft.
Work in `projects/<client>-<slug>/`, copied from `projects/_template/`.
After copying, set `name`/`id` in `package.json` and `meta.json` to the new slug, and delete the copied
`assets/audio.wav` if there is one.

## 1. Brief (ask only for what is missing)
Client/brand, audience, the ONE message, call to action, length (15-30 s typical), format (default 1080x1920, 30 fps),
brand assets (logo SVG/PNG, colours, fonts, contact line), tone, and which reference(s) to follow.
If the user gives a reference link that is not in `refrences/2d-motion-graphics/`, run `analyze-motion-reference` first.
Read `refrences/2d-motion-graphics/SUMMARY.md` and the chosen `analysis.md` files.

## 2. Script (stop for approval)
Write `projects/<name>/script.md`:
- VO text: conversational full sentences, no AI-style fragments, about 2.2-2.6 words/s (50-60 words per 25 s).
- Shot table: `scene | VO line | on-screen words (lead-in / key word) | visual metaphor | transition out | approx time`.
- Which reference each scene borrows from, palette, fonts.
- Claims the client must confirm (numbers, warranties, prices).
Show it to the user and wait. Expect several rounds; keep each draft in the file (Draft 1, Draft 2 ...).

## 3. Voice-over
- The user supplies the VO file (recorded, or generated in their own TTS tool), or uses `/media-use` if a voice
  service is connected. Copy it into `assets/` (never edit the original).
- `python tools/transcribe.py assets/vo.mp3 --json assets/vo_words.json`; fix misheard names by hand.
- `python tools/caption_spans.py assets/vo_words.json --offset 0.2` gives the caption spans and phrase times.
  Scene changes go in the pauses between phrases. Without a VO yet, build on estimated times and say so.

## 4. Build `index.html`
- Set the palette in `:root`, fonts in `assets/fonts/` (`@font-face`), root `data-duration` = VO end + ~3 s end card.
- One `<section class="clip">` per scene with `data-start`/`data-duration` (overlap neighbours by ~0.1 s for transitions).
- Captions: lead-in line + key line, each word a `<span class="w" data-t>`; `.mk` + `.hl` for a highlighter bar.
- One visual metaphor per scene, drawn as inline SVG (or a cut-out PNG); a different short transition per scene
  (push, zoom-through, iris, blur, slide), a bigger set-piece only at section changes. Keep the plate (grid, stars,
  small logo) alive across scenes, and something moving during every hold.
- Search `/hyperframes-registry` before hand-building a named effect (kinetic type, transitions, charts).
- Deterministic only: no `Math.random()`/`Date.now()`; one paused root timeline registered as `window.__timelines["main"]`.

## 5. Soundtrack
Edit `cues.json`: `duration`, `vo`, `vo_offset`, music `bpm`/`key`/`end_card`, and SFX cues (a `cut` at every scene
change, `pop` for things appearing, `riser` + `impact` into the end card). Then `npm run audio`
(= `python ../../tools/make_audio.py .`). Re-run after every timing change.

## 6. Check, look, render
```bash
npm run check                                   # must be 0 errors; review warnings
npx hyperframes snapshot --at 1,3,5,8,12        # one time per scene + transitions; READ the frames
npm run render -- -o ../../outputs/<client>-<slug>-v1-<len>s.mp4
```
Run the checklist in `motion-graphics-2d` section 8. Report: output path, length, what each scene shows, and anything
left open (claims to confirm, missing assets).

## 7. Revisions
Write the user's feedback and the decisions at the top of `script.md` (dated), change only what was asked, re-run
audio if timings moved, check + snapshot again, and render the next version number. Never overwrite a version the
user has already seen.
