# 2D motion graphics references: summary

These are four vertical, voice-over-driven explainer and promo reels, each saved from Pinterest. Every reel has its own folder `pin-<id>/` holding `analysis.md` (the full beat-by-beat breakdown), `vo_words.json` (Whisper word timestamps) and small data JSONs. The videos are git-ignored. At the user's request, no frames or contact sheets are kept.

Four older, shorter references (`ref-*.mp4`, kinetic-type reels) are summarised together in `older-refs-style-profile.md`. They have no per-reel folder.

| Folder | Reel | Length | Scenes (avg) | Look | Signature move |
|---|---|---|---|---|---|
| pin-924363892282992611 | Web Rank Studio, "Power of motion design" | 19.3 s | 12 (1.6 s) | Purple #751AA8 / white flip, italic didone pairs, 3D cut-out metaphors | A different short transition every scene (zoom-out, push, circle wipe from an object) |
| pin-933230354043913635 | MotionDesigners.Pro, Instagram growth pitch | 17.9 s | 14 (1.3 s) | Cream #FDF6EF / black #030303 flip, tight grotesk, red #F5060E key word, glow on black | Black iris reveal growing from the key word; word-by-word blur build |
| pin-1061653312177886416 | Solution Wagon, "Most agencies compete on output" | 35.8 s | 15 (2.4 s) | Off-white #FDFBF7 + vignette, Montserrat black/grey, greyscale photo collage | Everything is blur: blur-in words, defocus dissolves, zoom-through, light-orb wipe |
| pin-901986631645535447 | InsiderForce, "3 Claude Code skills" | 60.7 s | 15 (4 s) | Off-white #F6F6F6 / #222, Inter, product mock-ups | Grey→black word-by-word caption build; objects enter from frame edges |

## What all four share
- **The voice-over drives everything.** Each reel is built on a Whisper-able narration (2.1–3.2 words/s; it sounds like TTS or a tightly edited voice) with a quiet music bed under it. Scenes change in the pauses between phrases, and words appear in sync with the voice or up to about 0.4 s ahead of it. In long sentences the key word can land up to 1 s early.
- **One visual metaphor per line:** a background-removed cut-out (a 3D render or greyscale photo) with a soft drop shadow, often big and cropped by the frame edge.
- **Two-tier type lock-up:** a small regular lead-in sits over one big bold key word (2–3× larger). The key word stands out by colour (purple, red or grey) or by style (italic, caps, bold).
- **Minimal palette:** one background colour plus one dark colour, with at most one accent colour. Faint grid backgrounds appear in all four.
- **Short transitions (0.1–0.35 s) with strong ease-out and no bounce.** A big set-piece transition (circle or iris wipe, light orb, whip, zoom-through) is saved for section changes.
- **Constant small life during holds:** a slow push-in, rotating corner ornaments, footage playing inside cards, eyeballs moving.
- **Persistent anchors** carry across scenes: a logo top-centre or a watermark, and in some reels discs, a pin or a road band.

## Where they differ (pick one per project)
- **Pace:** fast punch (1.3–1.6 s scenes, a colour flip every scene: the Web Rank and MotionDesigners reels) or calm explainer (2.4–4 s scenes on one constant background: the Solution Wagon and InsiderForce reels).
- **Transition grammar:** a different transition every cut (Web Rank), one consistent family (Solution Wagon: blur), or mostly hard cuts and slides (InsiderForce).
- **Text entrance:** whole-word pops ahead of the VO (Web Rank), blur-fade per word on the VO (MotionDesigners, Solution Wagon), or grey→black slide per word (InsiderForce).

## Adapting a reference to your brand
Copy the structure, pacing and motion grammar of a reference, never its artwork, logo or copy.
- Map the reference's accent colour to the brand's accent (or, for a monochrome brand, to black plus an italic serif accent word).
- Map its fonts to the brand fonts: keep the two-tier contrast (small regular lead-in, big bold or italic key word).
- Keep the brand's casing rules even when the reference shouts in caps; use size and weight for emphasis instead.
- Replace the reference's watermark or logo slot with the client's logo, and its end card with the client's end card.
- Each reel's `analysis.md` ends with "Recreate-it notes (HyperFrames)": the concrete CSS/GSAP values to start from.

## Getting the videos back
The videos are git-ignored (third-party content, public repo). Each folder's `meta.json` holds the source URL;
re-download with `yt-dlp -o "refrences/2d-motion-graphics/pin-<id>/video.mp4" <webpage_url>` if you need to watch one.
