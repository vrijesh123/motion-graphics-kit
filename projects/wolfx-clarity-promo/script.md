# WOLFx: "Clarity first" promo, 25 s, 1080×1920

## Decisions and feedback (newest last)
- 2026-11-16: Draft 1 written. Defaults assumed; change any of them:
  - **One message:** WOLFx gets clear on your problem before writing code. This is their own stated difference
    (`clients/wolfx/profile.md` [S7]).
  - **Audience:** founders and growing businesses that need software built.
  - **Call to action:** "Let's make something great together." (the CTA on every page of wolfx.io) and `wolfx.io`.
    No phone or email until WOLFx confirms one.
  - **Format:** 1080×1920, 30 fps, about 25 s including a held end card.
  - **Style:** sentence-case captions (open question for WOLFx) and the interim wordmark (no SVG yet).
  - **On screen:** no numbers, client names or testimonials, since none are confirmed yet.
  - **Reference:** MotionDesigners (`pin-933230354043913635`) for the motion grammar: light/black flip, red key
    word, blur-in words, black iris reveal, slow push-in. It runs at the kit's calmer pace (about 2.5 words/s,
    2-4 s scenes, not the reel's 1.3 s). WOLFx's own motifs replace the reel's emoji, glow and road band.
- 2026-11-16: **Draft 1 approved by the user, with one change: no voice-over.** The video is graphics, text
  transitions and a music bed only.
  - The approved VO text becomes the on-screen copy, word for word, including hook A.
  - With no VO, the kit's "timing comes from the voice-over" rule doesn't apply. Timing comes from the music's
    beat grid (120 bpm: a beat is 0.5 s, a bar 2 s) and from reading time (at least 0.3 s per word, with longer
    holds on key lines). See Draft 2.
  - The pronunciation and voice questions are dropped.
- 2026-11-16: **Build is waiting on the HyperFrames skills** (the user's choice: install them first, then build in
  a new session). Project folder is ready (template copied, ids renamed, WOLFx fonts and logos in `assets/`);
  `index.html` and `cues.json` are still the template's. Next: build Draft 2 below.
- 2026-11-16: **Built v1 from Draft 2** (`outputs/wolfx-clarity-promo-v1-25s.mp4`, 25 s, 1080×1920, 30 fps).
  `npm run check`: 0 errors. The 12 warnings left are structural: the kit template keeps every scene in one
  `index.html`, while HyperFrames prefers sub-compositions. Changes from Draft 2:
  - **Frame 0** already shows "Most tech projects" and the code window, so the thumbnail isn't empty. "don't
    fail" lands at 1.0.
  - **Pills** land on the beats 17.5 / 18.0 / 18.5, not 17.75 / 18.25 / 18.75, with their pops at the same
    times. The first pill's animation starts at 17.42, so it is already visible on the 17.5 hard cut; with the
    old times that cut landed on an empty frame.
  - **Scene 3 sound:** three short, quiet whooshes (4.3, 5.3, 6.3) replace the single 3.3 s one. The kit's
    `whoosh` is high-pass noise, and at that length it read as hiss over the bed. Measured, not listened to.
  - **Wordmark** lands at full opacity, large and blurred, at 20.0, so the impact frame isn't blank.
  - **Red**, one element per scene:
    - S2: the strike-through. "bad code." stays ink.
    - S3: "the problem."
    - S4: "clarity."
    - S6: the pin. "business needs," stays ink.
    - S8: the pill outlines.
    - End card: the rule.
    - S1, S5 and S7 have no red.
  - **Two key lines wrap** to two lines rather than shrinking: "business / needs," and "design and / build it,".
  - **No grain overlay**, so WOLFx's white stays clean.
  - **The "Wx" badge** flips to white on black in scene 3 (black/white only, per the logo rules).
  - **wolfx.io** sits in a square black button with an arrow, in WOLFx's own button style.
  - **Final times:**
    - Cuts at 2, 4, 8, 10.5, 12.5, 15, 17.5 and 20 (each scene's `data-start` equals its `cut` cue).
    - Key lines land at 1.0, 2.5 (strike at 3.0), 6.0, 9.5, 11.5, 13.5 and 16.0.
    - The knot pulls straight from 7.45 to 8.0. The white iris opens from the full stop at (930, 583) from
      8.0 to 8.45.
    - The end line builds from 20.55 to 21.25, wolfx.io comes in at 21.6, and both hold to 25.0.
  - **Weakest spots, for the next pass:**
    - S2's caption sits over the faded code bars.
    - S4's ruler ticks are faint.
    - The zoom-through at 12.5 passes through a nearly empty frame, on purpose.
  - **Still open with WOLFx:**
    - hook A;
    - "AI" in a general promo;
    - sentence case or Title Case;
    - the interim PNG wordmark (we need an SVG);
    - wolfx.io as the only contact.
- 2026-11-17: **The user asked for an ElevenLabs voice-over script** (below) and will generate the MP3 themselves.
  When it arrives:
  - Copy it to `assets/vo.mp3` and transcribe it with `tools/transcribe.py`. Fix "WOLFx" in the transcript.
  - Move the word `data-t` times and the cuts to the voice's pauses.
  - Set `"vo"` in `cues.json` and re-run `npm run audio`.
  - Render as v2; v1 stays.
- 2026-11-17: **User feedback on v1:** they added the voice-over (`voiceovers/ElevenLabs_…Bella…v4.mp3`, 19.96 s)
  and asked for it to be synced. They also reported "broken" text in S7 (screenshot at about 16.3 s) and asked for
  v1 to be checked for other mistakes.
  - **What was wrong in v1:**
    1. **S7 placeholders.** Each grey dashed box had a snap pulse written as a `fromTo` from scale 1.05. GSAP
       applies a `fromTo`'s start values when the timeline is built, and these scaled from the top-left corner, so
       every box was 5% too big before its snap and spilled past the browser and phone frames.
    2. **Key-line word spacing.** Poppins 800 with −0.04em tracking left only about 0.11em between words, so lines
       read as "designand", "buildit,", "don’tfail" and "theproblem.".
  - **Fixes:**
    - The pulse is now a keyframed `to()`, so the boxes rest at scale 1.
    - Key lines get `word-spacing: 0.15em` (about 0.26em between words) and `line-height: 1.02`. The end line gets
      `word-spacing: 0.06em`.
    - The iris origin moved to (940, 584) to follow the full stop.
  - **v2 timing comes from the voice-over:**
    - The voice-over is copied to `assets/vo.mp3` and placed at +0.2 s (measured in the final mix: +0.200).
    - Whisper word times are in `assets/vo_words.json`, with "WolfX" corrected to WOLFx. Each word's `data-t` is
      its start + 0.2.
    - Cuts sit in the voice's pauses: 2.0, 3.62, 6.6, 9.3, 10.95, 12.8, 15.35 and 18.0. The video is 23 s long
      (voice ends 20.16 s, plus the end-card hold).
    - The S1→S2 cut is mid-sentence ("don’t fail | because"), because the voice doesn't pause there.
    - The pills land on their spoken words (16.44, 17.22). "Websites" starts at 15.3, so it is on screen at the
      15.35 cut, ahead of the spoken word at 15.62.
    - The S8 → end-card set-piece runs from 17.66 to 18.0, in the 17.7–18.3 pause.
    - The closing line builds from 18.24 to 19.4 and holds to 23.0; the wolfx.io button comes in at 19.95.
    - Sound effects are quieter under the voice, with three short knot swells. The music bed ducks under the voice.
  - **Voice clarity (measured by fitting the voice against the mix, not listened to):**
    - The first v2 mix had the closing line only 3.6 dB above the impact, chime and riser.
    - The impact (0.4), chime (0.3, 1.2 s) and riser (0.5, 0.6 s) were lowered, along with the cut and strike at
      2.0–2.95. The closing line now sits 10.4 dB above the rest; the other phrases 11–17 dB.
    - "because of bad code." is 8.8 dB above the music's bass and kick, which all sit below 1 kHz. In 1–4 kHz the
      rest is 22–30 dB down, so the voice stays clear.
  - **S2:** the code rows behind "because of / bad code." fade out, so the caption sits on white.
  - **Render:** `outputs/wolfx-clarity-promo-v2-23s.mp4`. `npm run check`: 0 errors; craft and layout show no
    findings.
  - **Still tight, if a v3 is wanted:** the voice moves on quickly.
    - "don’t fail" is fully on screen only from 1.72 to 1.82 s before the push into the code window.
    - "with you," and "business needs," hold for about 0.25–0.6 s.
    - That's fine with sound, short with the sound off.
  - **On purpose:** "Most tech projects" is on screen from frame 0 for the thumbnail, slightly ahead of the voice
    (spoken 0.2–1.2 s).
  - **Repo note:** `voiceovers/` is not git-ignored (only `projects/*/assets/*.mp3` is), so committing would add
    the original MP3. The fix belongs in `.gitignore` on `main`.

---

## Voice-over for ElevenLabs (2026-11-17)
Approved Draft 1 text, 53 words, with WOLFx spelled phonetically. The pauses sit at the scene changes: the
turn into scene 4, and the beat before the end card. Commas carry the rest. Aim for a read of about 22 s
(2.4–2.5 words/s), so the closing line holds for about 2.5 s on the end card.

```text
Most tech projects don't fail because of bad code. <break time="0.5s" />
They fail because nobody was clear on the problem. <break time="0.8s" />
At Wolf-ex, we start with clarity. <break time="0.4s" />
We sit down with you, map out what your business needs, and only then design and build it, from websites and apps to A.I. <break time="0.6s" />
Let's make something great together.
```

Plain version, for models that don't support break tags (the line breaks and full stops carry the pauses):

```text
Most tech projects don't fail because of bad code.

They fail because nobody was clear on the problem.

At Wolf-ex, we start with clarity.

We sit down with you, map out what your business needs, and only then design and build it, from websites and apps to A.I.

Let's make something great together.
```

- **Delivery:** warm and confident, like a founder talking, not an announcer. Keep the voice settings neutral:
  middle stability, low style exaggeration, speed 1.0.
- **Voice:** WOLFx still has to choose. Indian English suits a Mumbai company with clients in India and the
  Middle East; a neutral international voice also works.
- **If the read runs past about 23 s,** switch to hook B ("Good software doesn't begin with code. It begins with
  understanding the problem.") rather than speeding the voice up.

## Draft 2 (approved copy, text-only timing)
Same copy and visuals as Draft 1. The words build on the music instead of a voice: lead-in words arrive about
0.2 s apart, the key line lands on a beat with a sound hit, then the line holds to be read. Cuts sit on beats, and
the two set-pieces sit on bar downbeats (8.0 s and 20.0 s).

| # | Time | On screen (lead / **key**) | Words | Hold after the key lands | Transition out (on the beat) |
|---|---|---|---|---|---|
| 1 | 0.0-2.0 | Most tech projects / **don't fail** | 5 | about 0.9 s | Push in on the code window |
| 2 | 2.0-4.0 | because of / **bad code.** + red strike-through at 3.0 | 4 | about 1.0 s after the strike | Hard cut with a flip to black |
| 3 | 4.0-8.0 | They fail because nobody was clear on / **the problem.** | 9 | about 1.6 s | **Set-piece** at 8.0: the knot pulls straight and a white iris opens |
| 4 | 8.0-10.5 | At WOLFx, we start with / **clarity.** | 6 | about 1.3 s | Slide left |
| 5 | 10.5-12.5 | We sit down / **with you,** | 5 | about 1.0 s | Zoom through |
| 6 | 12.5-15.0 | map out what your / **business needs,** | 6 | about 1.2 s | Push up |
| 7 | 15.0-17.5 | and only then / **design and build it,** | 7 | about 1.1 s | Hard cut |
| 8 | 17.5-20.0 | **Websites · Apps · AI** (pills on beats 17.75, 18.25, 18.75) | 3 | about 1.2 s | **Set-piece** at 20.0: pills fly to centre, riser and impact, wordmark lands |
| End | 20.0-25.0 | Wordmark · red rule · **Let's make something great together.** · wolfx.io | 7 | the full line holds about 3.5 s | Hold to the end; music thins out from 20.0 |

**Soundtrack** (`cues.json`, generated by `tools/make_audio.py`):
- `"vo": null`, a music bed at 120 bpm, and `end_card` at 20.0.
- A `cut` cue at every scene change.
- `tick`s as code lines and wireframe blocks appear, and a `pop` for each pill.
- A low whoosh under the knot.
- A `chime` when the line pulls straight (8.0).
- A `riser` peaking at 20.0 plus an `impact`.

---

## Draft 1

### Voice-over (53 words, about 22-23 s read; video about 25 s)
> Most tech projects don't fail because of bad code. They fail because nobody was clear on the problem.
> At WOLFx, we start with clarity. We sit down with you, map out what your business needs, and only then design
> and build it, from websites and apps to AI. Let's make something great together.

**Alternate hook (B), softer and shorter (47 words in total).** Use it if WOLFx won't stand behind the first two
sentences, or if the recorded read runs long:
> Good software doesn't begin with code. It begins with understanding the problem.

Delivery: warm and confident, about 2.5 words/s, like a founder talking, not an announcer. A small pause before
"At WOLFx" (the turn) and before the closing line.

Length check: at 2.5 words/s the video lands at about 25 s. A slow read (2.2 words/s) pushes it to about 28 s.
If that happens, switch to hook B (about 25 s even at a slow read) rather than speeding up the voice.

### Shot table
Times are **estimates** at about 2.5 words/s, with the VO starting at 0.2 s. Real times come from the recorded VO
(Whisper), and cuts move to its pauses. "Lead / **key**" is the two-tier caption: a small lead-in line over a big key
line. Every word builds in on the VO.

| # | Time (est.) | VO line | On screen (lead / **key**) | Visual metaphor | Transition out |
|---|---|---|---|---|---|
| 1 | 0.0-2.2 | Most tech projects don't fail | Most tech projects / **don't fail** | White grid. A hairline browser window slides up into frame; neat grey code lines type in, one per word | Push in on the code window |
| 2 | 2.2-4.0 | because of bad code. | because of / **bad code.** | The code window fills the background, all lines clean. On "code" a **red line strikes through "bad code."**: the code isn't the problem | Hard cut with a flip to black (one dark blink) |
| 3 | 4.0-7.9 | They fail because nobody was clear on the problem. | They fail because nobody was clear on / **the problem.** (red on black) | Black. One white hairline tries to cross the frame and keeps looping back into a growing **tangled knot** (WOLFx's contour line, gone wrong) | **Set-piece:** the knot pulls taut into one straight line, while a white iris opens from the full stop after "problem" |
| 4 | 7.9-10.6 | At WOLFx, we start with clarity. | At WOLFx, we start with / **clarity.** (red) | White. The straight line runs across the frame like a horizon, calm; the grid settles back in behind it | Slide left (the line carries on into scene 5) |
| 5 | 10.6-12.8 | We sit down with you, | We sit down / **with you,** | Two square-cornered speech bubbles (hairline, WOLFx button style) take turns on either side of the line; typing dots in each | Zoom through the gap between the bubbles |
| 6 | 12.8-15.3 | map out what your business needs, | map out what your / **business needs,** | **Topographic map** (WOLFx's contour lines). A dashed route draws itself across the contours and lands on a **red pin** | Push up |
| 7 | 15.3-18.2 | and only then design and build it, | and only then / **design and build it,** | A hairline phone and browser wireframe; grey placeholder boxes snap into solid ink UI blocks one by one. The last block is a square black button with "→" | Hard cut |
| 8 | 18.2-20.8 | from websites and apps to AI. | **Websites · Apps · AI** as three red-outlined pills (WOLFx's service-pill style), one per spoken word | The pills pop in on their words on the grid, with a slow push-in | **Set-piece:** the pills fly to centre and the wordmark lands (riser + impact) |
| End | 20.8-25.0 | Let's make something great together. | WOLFx wordmark · red hairline rule · **Let's make something great together.** · wolfx.io | White. The wordmark sits over a faint grid; contour lines drift slowly in the bottom corner. The closing line builds on the VO and holds at least 2 s after the last word | Hold to the end |

**Sound-off read** (captions only): "Most tech projects don't fail because of ~~bad code.~~ They fail because nobody
was clear on the problem. At WOLFx, we start with clarity. We sit down with you, map out what your business needs,
and only then design and build it. Websites · Apps · AI. Let's make something great together. wolfx.io". It tells
the whole story without the voice.

### Look (from `clients/wolfx/brand.md`)
- **Palette:** white `#FFFFFF` and ink `#121212`, with one accent, red `#FF2B2B`, used once per scene at most (the
  strike-through, "the problem.", "clarity.", the pin, the pills, the end-card rule). `--soft #ECECEC` grid,
  `--mute #909090` contour lines.
  - Scene 3 is the only black scene, with white type and a red key word.
- **Type:** Poppins only. Lead lines 500-600; key lines 800 at roughly 130-150 px (about 10-15% smaller than the
  template, because Poppins sets wide). Sentence case. No serif.
- **Persistent plate:** a faint grid, a slow contour-line drift in one corner, and the small "Wx" monogram badge at
  the top centre.
  - In scene 3 the grid stays faintly visible on black.
  - The end card uses the full interim wordmark.
- **Motion:**
  - Words blur in (blur 8 px → 0, y +10 → 0, 0.14 s, hard ease-out) on their spoken beat.
  - Every shot pushes in 3-5% over its length. Lines draw on rather than pop. No bounce.
  - Each cut uses a different transition, with set-pieces only at the turn (3 → 4) and into the end card.
- **Sound:**
  - A light music bed at about 110-118 bpm, ducked under the VO.
  - A `cut` cue at every scene change; `tick`s for the typing code and wireframe blocks; a `pop` per pill.
  - A low "tangle" whoosh in scene 3 and a clean chime when the line pulls straight.
  - A riser and impact into the end card.

### Claims WOLFx must confirm
1. **The hook:** "Most tech projects don't fail because of bad code. They fail because nobody was clear on the
   problem." This is a broad claim we wrote. WOLFx's own copy only says they get clear before coding. Approve it,
   or use hook B.
2. **"From websites and apps to AI":** listed as services on wolfx.io (fine), but check WOLFx wants AI in a
   general promo.
3. **End card contact:** `wolfx.io` only, unless they give a phone number or email.

### Needed before the voice-over
- **How to say "WOLFx":** we assume "Wolf-ex". This decides the VO and how Whisper's transcript gets corrected.
- **Who voices it:** a WOLFx founder or team member (most authentic), or a generated voice. We could generate it
  with the ElevenLabs account connected to this workspace, which uses your credits, or you supply an MP3.
- **Voice:** male or female, and accent (Indian English suits a Mumbai company talking to Indian and Middle East
  clients; neutral international also works).
