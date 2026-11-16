# 2D motion graphics kit

A workspace for making short vertical 2D motion graphics videos (explainers, promos, kinetic type) with Claude Code
and HyperFrames (HTML + GSAP rendered to MP4). Human guide: `docs/GUIDE.md`. Media not in git: `docs/MEDIA.md`.

## Folders
- `refrences/2d-motion-graphics/` analysed style references. Start with `SUMMARY.md`; each `pin-<id>/analysis.md` is a
  scene-by-scene breakdown with "Recreate-it notes (HyperFrames)". Videos are git-ignored; `meta.json` has the source URL.
  (The folder name `refrences` is spelled this way on purpose; keep it.)
- `projects/_template/` starter HyperFrames project in the house style. Copy it for every new video: `projects/<client>-<slug>/`.
- `projects/<name>/` one folder per video: `index.html`, `cues.json`, `script.md`, `assets/`.
- `tools/` shared scripts (see below). `outputs/` finished renders (git-ignored). `docs/` guide + media manifest.

## Skills
- Project skills in `.claude/skills/` (load automatically): `motion-graphics-2d` (craft, formats, principles, checklist),
  `analyze-motion-reference` (add a reference video to the library), `make-motion-video` (brief to rendered MP4).
- HyperFrames skills (installed per machine with `npx hyperframes skills`): read `/hyperframes` before writing or changing
  any composition, `/hyperframes-cli` for check/snapshot/render, `/hyperframes-registry` before hand-building a named
  visual, `/media-use` for voice-over, music, images and cut-outs. If they are missing, tell the user to install them;
  do not install them yourself.

## Rules
- Never modify or delete reference videos or anything the user supplies (voice-overs, logos, footage). Write results to `outputs/`.
- Never commit or push unless the user explicitly asks. `.gitignore` keeps renders, reference videos and project
  audio/video out of git, but logos, scripts and `index.html` are tracked: if the repo is public, client work belongs
  in a private copy. Ask before committing anything client-specific.
- **References are analysed as text only.** Look at frames while analysing, then delete `frames/` and `sheets/`;
  keep only `analysis.md` and the small JSON files. Never copy a reference's artwork, logo or copy: borrow its
  structure, pacing and motion grammar.
- **Voice-over scripts sound like a person talking:** conversational full sentences, no AI-style fragments
  ("Fast. Simple. Done."), but lean: about 50-60 words per 25 s (2.2-2.6 words/s). Show the draft and wait for approval
  before building. Write scripts to `projects/<name>/script.md` with a shot table.
- **Timing comes from the voice-over, never from guesses.** Transcribe the VO with `tools/transcribe.py --json`,
  place it at `vo_offset` (default 0.2 s) and use word start + offset as `data-t` cue times. Scene changes sit in
  the pauses between phrases. Whisper mishears brand names: fix them by ear.
- **`cues.json` must match `index.html`.** Every scene change in `index.html` has a `cut` cue at the same second;
  after any timing change re-run `python tools/make_audio.py projects/<name>` (it writes `assets/audio.wav`).
- One message per video, readable with the sound off, sentence case unless the brand says otherwise, one accent
  colour at most, text never below 28 px at 1080 wide, final line on screen at least 2 s.
- After every edit: `npm run check` in the project (0 errors), then `npx hyperframes snapshot --at <times>` and look
  at the frames before reporting. Render only after that.
- Version renders: `outputs/<client>-<slug>-v1-<length>s.mp4`, `-v2-...`; never overwrite a version the user has seen.
- Record per-project decisions and user feedback at the top of that project's `script.md` (newest last), so the next
  session can continue.

## Tools (Python 3.10+, ffmpeg on PATH, `pip install numpy faster-whisper yt-dlp`)
- `tools/transcribe.py <audio> --json assets/vo_words.json` Whisper word timestamps.
- `tools/caption_spans.py assets/vo_words.json --offset 0.2` caption `<span data-t>` markup, one block per phrase.
- `tools/make_audio.py <project_dir>` synth music bed + SFX + VO from `cues.json` (format in its docstring).
- `tools/prep_reference.py <folder>` probe, cuts, audio stats, words, meta and temporary frames for a reference.
- `tools/seek_snapshot.py` frame grabs without the HyperFrames CLI (fallback only).
- `tools/media_manifest.py` rewrites `docs/MEDIA.md` (inventory of git-ignored media). Re-run after adding media.

## HyperFrames
Node 22+ required (`node -v`). In a project: `npm run check`, `npx hyperframes snapshot --at 1,3,5`,
`npx hyperframes preview --background` (Studio), `npm run render -- -o ../../outputs/<file>.mp4`.
Projects pin `hyperframes@0.9.19` in `package.json`; upgrading is `npx hyperframes@latest upgrade --project .`.
On Windows, `python` must be on PATH for `npm run audio`; run commands from Git Bash or PowerShell.
