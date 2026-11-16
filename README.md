# 2D motion graphics kit

Make short vertical 2D motion graphics videos (explainers, promos, kinetic type) with Claude Code and
[HyperFrames](https://hyperframes.heygen.com): brief → script → voice-over timing → animated HTML → MP4.

**Start with [docs/GUIDE.md](docs/GUIDE.md)**: setup, which skills to install, how to give references, how to make
and revise a video.

Inside:
- `refrences/2d-motion-graphics/` four analysed reference reels (start with `SUMMARY.md`); videos are not in git.
- `projects/_template/` a working 12.5 s starter project in the house style (render it to test your setup).
- `clients/` one branch per client: `main` is the kit, each client branch adds its brand pack in
  `clients/<slug>/` (see `clients/README.md`).
- `.claude/skills/` project skills Claude Code loads automatically.
- `tools/` Whisper transcripts, caption markup, soundtrack generator, reference prep.
