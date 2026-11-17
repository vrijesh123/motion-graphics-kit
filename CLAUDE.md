# 3D motion graphics kit (branch `3d-graphics`)

A workspace for making short 3D motion graphics videos (explainers, promos, brand films) with Claude Code and
HyperFrames (HTML, Three.js/WebGL and GSAP rendered to MP4). It was split off the 2D kit on `main`; the 2D
references, skills and project template were removed from this branch and are still on `main`.
Human guide: `docs/GUIDE.md`. Media not in git: `docs/MEDIA.md`.

**Status (2026-11-17): the 3D pipeline is not set up yet.** There is no 3D project template, no 3D project skill
and no 3D reference yet. Until they exist, build from the HyperFrames skills directly (see "Skills"), and record
what worked in the project's `script.md` so it can become the template and skills later.

## Folders
- `clients/wolfx/` the WOLFx client pack, brought over from the `wolfx` branch. Read its `README.md` first.
  `clients/_template/` is the blank pack.
- `projects/<client>-<slug>/` one folder per video: `index.html`, `cues.json`, `script.md`, `assets/`.
- `refrences/` analysed 3D references, text only (the folder name is spelled this way on purpose; keep it).
  Empty for now. One folder per reference with `analysis.md` and the small JSON files from `tools/prep_reference.py`.
- `tools/` shared scripts (see below). `outputs/` finished renders (git-ignored). `docs/` guide + media manifest.

## Branches and clients
- `main` is the 2D kit. `wolfx` is WOLFx's 2D branch; WOLFx's first video, the 2D "Clarity first" promo, and the
  decisions behind it (approved copy, no voice-over, open questions) are in `projects/wolfx-clarity-promo/script.md`
  on that branch (`git show wolfx:projects/wolfx-clarity-promo/script.md`).
- `3d-graphics` (this branch) is the 3D kit and also carries the WOLFx pack. Because it holds client material,
  never merge it into `main` or into another client's branch. Bring kit fixes from `main` with
  `git cherry-pick <commit>` rather than `git merge main`: a merge also brings in any 2D files added on `main`
  later, and conflicts on 2D files `main` edits that this branch deleted.
- For WOLFx work, read `clients/wolfx/README.md` before any brief, script or build. Its palette, fonts, logo, voice
  and end card replace the defaults; ask only for what it does not answer.
- Every fact in a pack cites its source in `sources.md`. Numbers, client names, testimonials and contact
  details stay marked "confirm" until the client approves them, and are not put on screen before that.
- Keep client facts in the pack, not in Claude's memory (memory is shared across branches).
- Pushing this branch to a public remote publishes the WOLFx pack: ask first.

## Skills
- HyperFrames skills (installed per machine with `npx hyperframes skills`): read `/hyperframes` before writing or
  changing any composition. For 3D also read its `references/types/3d.md`, `references/runtimes.md` (Three.js seek
  protocol: draw from `hf-seek` time, no `requestAnimationFrame` loop, seeded randomness) and
  `references/path-tracing.md`. `/hyperframes-cli` for check/snapshot/render, `/hyperframes-registry` before
  hand-building a named visual (it has 3D blocks), `/media-use` for voice-over, music, images and cut-outs.
  If they are missing, tell the user to install them; do not install them yourself.
- No project skills on this branch yet (`.claude/skills/` is empty). The 2D ones (`motion-graphics-2d`,
  `analyze-motion-reference`, `make-motion-video`) are on `main`: `git show main:.claude/skills/<name>/SKILL.md`.
  Their pipeline steps (script approval, VO timing, `cues.json`, check, snapshot, versioned render) still apply.

## Rules
- Never modify or delete reference videos or anything the user supplies (voice-overs, logos, footage, 3D models).
  Write results to `outputs/`.
- Never commit or push unless the user explicitly asks. `.gitignore` keeps renders, reference videos and project
  audio/video out of git, but logos, scripts and `index.html` are tracked. Ask before committing anything
  client-specific.
- **References are analysed as text only.** Look at frames while analysing, then delete `frames/` and `sheets/`;
  keep only `analysis.md` and the small JSON files. Never copy a reference's artwork, models, logo or copy: borrow
  its structure, pacing, camera and motion grammar.
- **Voice-over scripts sound like a person talking:** conversational full sentences, no AI-style fragments
  ("Fast. Simple. Done."), but lean: about 50-60 words per 25 s (2.2-2.6 words/s). Show the draft and wait for
  approval before building. Write scripts to `projects/<name>/script.md` with a shot table.
- **Timing comes from the voice-over, never from guesses.** Transcribe the VO with `tools/transcribe.py --json`,
  place it at `vo_offset` (default 0.2 s) and use word start + offset as cue times. Scene changes sit in the pauses
  between phrases. Whisper mishears brand names: fix them by ear.
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
Node 22+ required (`node -v`; with nvm, `nvm use 22`). The `npm run audio/check/render` scripts came from the
2D template's `package.json`; until a 3D template exists, start a project's from
`git show main:projects/_template/package.json`. In a project: `npm run check`,
`npx hyperframes snapshot --at 1,3,5`, `npx hyperframes preview --background` (Studio),
`npm run render -- -o ../../outputs/<file>.mp4`. Pin the HyperFrames version in each project's `package.json`
(the 2D kit used `hyperframes@0.9.19`); upgrading is `npx hyperframes@latest upgrade --project .`.
WebGL renders on the machine's GPU; without a working one Chrome draws in software, which is much slower
(timeouts and settings in `/hyperframes` `references/path-tracing.md`).
On Windows, `python` must be on PATH for `npm run audio`; run commands from Git Bash or PowerShell.
