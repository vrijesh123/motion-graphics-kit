# Guide: the 3D motion graphics kit (branch `3d-graphics`)

This branch is for 3D motion graphics videos made by **Claude Code** with **HyperFrames**: Claude writes the script,
builds the 3D scenes as an HTML page (Three.js/WebGL, animated with GSAP), makes the soundtrack and renders the MP4.
You give it references, the brief and feedback.

It was split off the 2D kit on `main`. **The 3D starter project, the 3D project skills and the 3D reference library
are not set up yet.** Until they are, Claude builds from the HyperFrames skills directly. The 2D versions are still on
`main` if you want to look at them (`git show main:docs/GUIDE.md`).

---

## 1. One-time setup

| Install | Why | Check it works |
|---|---|---|
| [Claude Code](https://claude.com/claude-code) (terminal or the VS Code extension) | Does the work | `claude --version` |
| **Node.js 22 or newer** | HyperFrames needs it | `node -v` shows v22+ |
| **FFmpeg** (ffmpeg + ffprobe) | Audio, probing, frame grabs | `ffmpeg -version` |
| **Python 3.10+** | The scripts in `tools/` | `python --version` |
| Python packages | Whisper transcripts, downloads | `pip install numpy faster-whisper yt-dlp` |
| Git | Get the kit and keep versions | `git --version` |
| A working GPU driver | WebGL renders on the GPU; in software it is much slower | Chrome's `chrome://gpu` shows hardware acceleration |

Per operating system:
- **Windows:** install Node 22 LTS from nodejs.org and Python from python.org (tick "Add to PATH"). For FFmpeg,
  download a build from gyan.dev or BtbN, unzip it, and add its `bin` folder to PATH. Use Git Bash or PowerShell.
- **macOS:** `brew install node@22 ffmpeg python`.
- **Linux:** `sudo apt install ffmpeg python3-pip`, and Node 22 via nvm (`nvm install 22 && nvm use 22`).

Get the kit:
```bash
git clone <repo-url> motion-graphics
cd motion-graphics
git switch 3d-graphics
```

---

## 2. Skills

Skills are instruction packs Claude Code loads when a task needs them.

### a) HyperFrames skills (install once per computer, required)
```bash
npx hyperframes skills
```
This copies them into `~/.claude/skills/`. Start a **new** Claude Code session afterwards. Update later with
`npx hyperframes skills update`.

| Skill | What it gives Claude |
|---|---|
| `hyperframes` | The rules for writing compositions that render correctly. For 3D: `references/types/3d.md` (camera, light, materials), `references/runtimes.md` (how Three.js is driven frame by frame) and `references/path-tracing.md` (photoreal light, slow). |
| `hyperframes-cli` | Check, snapshot, preview, render, and how to recover from render errors. |
| `hyperframes-registry` | About 450 ready-made blocks, including 3D ones: 3D transitions, 3D UI reveals, extruded 3D code, phone and laptop models. |
| `media-use` | Voice-over, music, SFX, images, cut-outs, colour grades, audio mixing. |
| `remotion-to-hyperframes` | Bring in existing Three.js code or renders from Blender and check them frame by frame. |
| `style-sampling` | Includes a "3D Brand Explainer" style (HyperFrames Pro). |

### b) Project skills
None on this branch yet. The 2D ones are on `main`.

### c) Optional connectors (your own accounts)
- **Voice-over:** any TTS service you have (ElevenLabs, HeyGen and others). Connect one in Claude Code (`/mcp`, or
  claude.ai connectors), or generate the voice yourself and give Claude the MP3. Use only voices you have the
  rights to.
- **3D assets:** a generator or modelling tool connected the same way, if a video needs a model that code can't
  build. Generated assets cost credits; check the licence before using them in client work.

---

## 3. References

Analysed references go in `refrences/<id>/` as text: `analysis.md` plus small JSON files from
`tools/prep_reference.py`. The videos stay on your machine (git-ignored) because they belong to other people.
Borrow structure, pacing, camera moves and motion, never the artwork, models, logos or copy.

---

## 4. Clients

This branch carries one client pack, **WOLFx** (`clients/wolfx/`, brought over from the `wolfx` branch): what the
company does, its palette, fonts, logo, tone of voice, proof points and what still needs WOLFx's approval, with a
source for every fact. Claude reads it before writing anything for WOLFx. WOLFx's first video (a 2D promo) and
its approved copy are on the `wolfx` branch.

Because this branch holds client material, never merge it into `main`. If the repository is public, pushing this
branch publishes the WOLFx pack: keep it local or on a private remote unless WOLFx agrees.

---

## 5. Making and revising a video

The flow carries over from the 2D kit: brief, then a script for your approval, then voice-over timing, build,
check and snapshot, and finally a versioned render in `outputs/<client>-<slug>-v1-<length>s.mp4`. The 3D build
step has no template yet, so expect the first video to set it up (its `package.json` scripts can start from
`git show main:projects/_template/package.json`).

Give feedback in plain words and be specific about time and scene:
> v1 feedback: the camera dive at 0:04 is too fast; drop the second object in scene 3;
> make the end card hold 1 s longer. Render v2.

Claude writes the feedback into `script.md`, changes only what you asked, regenerates the audio if timings moved,
checks and renders **v2** next to v1. Earlier versions are never overwritten.

**Preview it yourself while it's being built:** in the project folder, run `npx hyperframes preview` and open the
link.

---

## 6. Troubleshooting

| Problem | Fix |
|---|---|
| `hyperframes` errors about the Node version | `node -v` must be 22+. Switch with nvm (`nvm use 22`) or install Node 22. |
| `ffmpeg: not found` | FFmpeg isn't on PATH in this terminal. Add its `bin` folder and open a new terminal. |
| 3D renders are very slow, or `check` times out | Chrome is drawing WebGL in software. Fix the GPU driver, or raise the timeouts (see `/hyperframes` `references/path-tracing.md`). |
| Video has no sound | `assets/audio.wav` is missing (it's git-ignored). Run `npm run audio`. |
| Captions out of sync | The VO offset differs from `vo_offset` in `cues.json`, or the VO changed. Re-transcribe and re-run audio. |
| Whisper writes the brand name wrong | Normal. Correct it in `assets/vo_words.json`; only the times matter for the build. |
| Claude doesn't use the HyperFrames skills | Run `npx hyperframes skills`, then start a new Claude Code session. |

---

## Where things are

```
CLAUDE.md            rules Claude follows in this folder
docs/GUIDE.md        this guide
docs/MEDIA.md        list of git-ignored media (re-run: python tools/media_manifest.py)
clients/wolfx/       the WOLFx client pack (README.md first)
clients/_template/   blank client pack
projects/            one folder per video
refrences/           analysed 3D references (text only)
tools/               transcribe, caption_spans, make_audio, prep_reference, seek_snapshot, media_manifest
outputs/             finished MP4s (not in git)
```
