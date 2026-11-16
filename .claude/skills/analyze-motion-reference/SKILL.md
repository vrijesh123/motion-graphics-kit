---
name: analyze-motion-reference
description: Add a reference video (Pinterest, Instagram, YouTube, TikTok link or a local video file) to the 2D motion graphics reference library and write its scene-by-scene analysis. Use when the user shares a reference, inspiration or "make it like this" video, or asks to study, break down or analyse a motion graphics reel.
---

# Analyse a motion graphics reference

Goal: a text-only, reusable breakdown that a later session can build from without watching the video again.
Output per reference: `refrences/2d-motion-graphics/<folder>/` with `analysis.md`, `meta.json`, `probe.json`,
`cuts.json`, `audio.json`, `vo_words.json`. The video stays local and git-ignored. No frames are kept.

## 1. Download
Folder name: `pin-<id>` for Pinterest, `ig-<shortcode>`, `yt-<id>`, `tt-<id>`, or a short slug for a local file.
```bash
yt-dlp -f "bv*+ba/b" --merge-output-format mp4 --write-info-json \
  -o "refrences/2d-motion-graphics/<folder>/video.%(ext)s" "<url>"
```
- Local file from the user: copy it to `<folder>/video.mp4` (copy, never move or edit the original).
- Instagram/TikTok may need cookies: `--cookies-from-browser chrome`. If the download fails, ask the user for the file.
- Several references at once: download each into its own folder, then run step 2 once on the library folder.

## 2. Prepare
```bash
python tools/prep_reference.py refrences/2d-motion-graphics/<folder>
```
Writes the JSON files plus temporary `frames/` (1 fps + one frame per cut) and `sheets/` (contact sheets).
Scene detection misses blur/dissolve/push transitions: treat `cuts.json` as a starting point and check by eye.

## 3. Look
- Read the contact sheets, then the cut frames, then 1 fps frames around every transition.
- For a transition or text animation you can't read from 1 fps, grab a short burst into the scratchpad:
  `ffmpeg -ss <t> -t 0.6 -i video.mp4 -vf fps=30,scale=360:-2 <scratch>/burst_%02d.jpg`.
- Measure colours from frames (don't guess hex values), and compare caption timing with `vo_words.json`.
- For several references, analyse them in parallel subagents (one per reference) and spot-check one claim per
  reference yourself.

## 4. Write `analysis.md` (same sections as the existing ones, so references stay comparable)
1. Title line: `# 2D motion graphics ref — <creator>, "<hook line>" (<platform> <id>)` + source URL, length, size, fps.
2. **Overview:** what it sells, the full VO script (from Whisper), words per second, voice character, music bed.
3. **Look:** palette with hex values, type system (fonts or nearest free match, sizes, weights, the lead-in/key-word
   lock-up), imagery style, background, persistent elements.
4. **Scene-by-scene table:** `# | time | VO words (times) | background | what's on screen | entrance / motion | exit / transition`.
5. **Motion language:** easing, durations, how text enters, transition vocabulary, what keeps the frame alive during holds.
6. **Recreate-it notes (HyperFrames):** concrete CSS/GSAP values (durations, eases, blur amounts, clip-path shapes,
   sizes at 1080x1920) a builder can copy.
Note what you could not verify (for example "audio not listened to; SFX inferred from levels").

## 5. Clean up and index
- Delete `frames/` and `sheets/` and any scratch bursts (house rule: written context only).
- Add a row to the table in `refrences/2d-motion-graphics/SUMMARY.md` and update "What all share" / "Where they differ"
  if the new reference changes the picture.
- Run `python tools/media_manifest.py` so `docs/MEDIA.md` lists the new (git-ignored) video.
- Tell the user in a few lines: what the reference does best, its pace, and which kind of video it suits.
