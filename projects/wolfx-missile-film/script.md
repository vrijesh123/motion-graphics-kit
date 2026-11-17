# WOLFx: "Lykos Wx-1" missile launch film, about 70 s, 1080×1920, text only

## Decisions and feedback (newest last)
- 2026-11-17: Draft 1 written (narrated, missile as a metaphor for WOLFx's services). Built on chunk 1 of the
  Oreshnik reference (`refrences/oreshnik-hypersonic-missile/analysis.md`, Part 01), themed on wolfx.io.
- 2026-11-17: **User's answers to Draft 1:**
  - **Name: Lykos Wx-1.**
  - **Text only.** Narration would need ElevenLabs or another outside source, so there is no voice-over; timing
    comes from the music's beat grid and reading time.
  - **Standalone, with the end card.**
  - **Title Case for all on-screen text.**
  - Draft 2 turned the lines into on-screen copy (superseded below).
- 2026-11-17: **User: "the script must be like WOLFx is launching its new missile Lykos, just like the reference
  chunk."**
  - Draft 3 drops the metaphor: a straight launch reveal of WOLFx's new missile, beat for beat like the
    reference's first 68 s.
  - The previous decisions (text only, Title Case, standalone end card) still stand.
  - **Fiction, stated as fact on screen:** every spec below is invented for the film (see "Specs"). No real
    weapon, country, defence system or target is named or shown.
  - **"Payloads", not "warheads":** keeps the brand film clear of weapon-of-war wording; swap if the user wants
    it closer to the reference.
  - **Original wording:** the beats follow the reference, but none of its sentences are reused (kit rule).
  - **One message:** Lykos Wx-1, engineered by WOLFx. It is a showcase of WOLFx's 3D and engineering craft;
    WOLFx's homepage lists defence and WebGL work among its industries [S1].
  - **On screen:** no client names, testimonials or contact details beyond `wolfx.io`. The only numbers are the
    fictional specs.
- 2026-11-17: **User: "go ahead and build it." Built v1** (`outputs/wolfx-missile-film-v1-70s.mp4`).
  - Three.js r147 is vendored in `assets/lib/`.
  - The film is one `index.html` (kit convention), driven by one GSAP clock.
  - Notes are in `SPEC.md` and `REVIEW.md`.
  - Changes from the shot table, all for vertical framing and legibility:
    - the floor label is two lines ("8×8 Mobile / Launcher") and faces the camera;
    - in shot 8 the payload words sit above the nose, and the lead line is 620 px wide and leaves at 55.6 s;
    - the shot 9 lead line is 620 px wide, with the missile on the right third;
    - the diagram's paths start drawing at 38.5 s.
    - in shot 8 the launch tube lifts off the missile (instead of the missile sliding out);
    - the Solid Fuel tag shows from 50.0 to 51.3 s, and the camera holds on stage 1 until 51.45 s.
- 2026-11-17: **User asked for a voice-over script for ElevenLabs.**
  - VO Draft 4 is below; the paste-ready text with pause tags is `vo-elevenlabs.txt`.
  - The user generates the voice; Claude does not call ElevenLabs.
  - The lines are timed to v1's shots. When the MP3 arrives as `assets/vo.mp3`: transcribe it
    (`tools/transcribe.py`), set `"vo"` in `cues.json`, align cuts and lines to the words, and render v2.
  - Still unconfirmed: "WOLFx" said as "Wolf-ex", and "Lykos" as "LEE-kos".
- 2026-11-17: **User added the voice-over (`assets/voiceover/v1.mp3`, ElevenLabs "Atlas", 46.8 s) and asked for a
  bolder, war-ready look. Built v2** (`outputs/wolfx-missile-film-v2-53s.mp4`, 52.8 s).
  - **Pauses:** ElevenLabs did not apply the pause tags; the read has about 0.5 s between lines.
  - **Re-timing:** the film was re-timed to the voice (kit rule), not the other way round.
    - `assets/vo_paced.wav` is a copy of the voice-over with two longer pauses: +0.8 s after line 1, and +3.2 s
      before "The nose holds", so the stages can be read. The user's file is untouched.
    - Word times on the film timeline are in `assets/vo_words_film.json`; brand names were fixed by ear.
    - Each cut sits about 0.2 s before its line. Key moments are pinned to words: nose opens on "opens",
      the fuel tag on "solid", the nose opens again on "nose", the payload words on "seven".
    - The 3D world still runs on the 70 s design grid through a time map (`MAP` in `index.html`).
  - **On-screen copy:** the Draft 3 lead lines stay as titles, each landing with its spoken line.
    Word-for-word captions of the voice-over remain an option.
  - **Look:** WOLFx's dark flip, made bolder.
    - Night ground #0B0B0B, grid #242424, contours #5E5E5E.
    - Gunmetal hardware with white stencils, hard warm key light and strong cool rim light.
    - Orange flame and grey smoke.
    - Bold white type (700, 66 px) and white button tags.
    - Dark studio and diagram; white wordmark on the end card.

## VO Draft 4 (for ElevenLabs, timed to v1)
Spoken style (kit rule), 131 words in about 65 s.
- **Paste:** `vo-elevenlabs.txt` is the paste-ready version, with names spelled the way they should sound and
  `<break>` pauses so each line starts near its shot.
- **Times:** they assume about 2.5 words/s; the real voice will drift, and we re-align after transcribing.

| Shot | Starts near | Line |
|---|---|---|
| 1 | 0.3 | This is Lykos Wx-1, the newest missile from WOLFx. |
| 2 | 6.2 | It rides an eight-by-eight launcher, so it can launch from almost anywhere. |
| 3 | 12.3 | Three solid-fuel stages carry it up into orbit in just a few minutes. |
| 4 | 18.3 | Once it's up there, it turns over and dives back down at hypersonic speed. |
| 4 | 24.2 | Then the nose opens, and out come seven payloads. |
| 5 | 28.3 | Each one steers itself toward its own target. |
| 6 | 32.6 | Small thrusters at the base let it change course on the way down. |
| 7 | 38.5 | That weaving path is what makes it so hard for an interceptor to catch. |
| 8 | 46.6 | Open it up, and you'll find three stages, with solid fuel packed into the first. |
| 8 | 55.5 | The nose holds seven payloads, each with its own engine. |
| 9 | 60.4 | Lykos Wx-1, engineered by WOLFx. |
| End | 64.3 | Let's make something great together. Find us at wolfx.io. |

## Specs (fictional; change freely)
| Spec | Value | Where it shows |
|---|---|---|
| Name | Lykos Wx-1 | shots 1 and 9 |
| Launcher | 8×8 mobile launcher | shot 2 |
| Stages | three, solid fuel | shots 3 and 8 |
| Flight | climbs to orbit in minutes, then dives at hypersonic speed | shots 3 and 4 |
| Payloads | seven, independently steered, each with its own engine and thrusters | shots 4-8 |
| Defence | a weaving path built to slip past interceptors | shot 7 |

Seven payloads, not the reference's six: a quiet nod to WOLFx's seven services, and not a copy of the
reference's numbers.

## Draft 3: on-screen copy and timing
**Music:** 120 bpm, so a beat is 0.5 s and a bar is 2 s.
- Every cut sits on a bar downbeat (an even second).
- Lead lines step in word by word, about 0.2 s apart, like the words on wolfx.io.
- Each key word or tag lands on a beat with a soft tick.
- Every line stays readable for at least 0.3 s per word plus a hold, and the final line holds 4.6 s.

**Title Case:** Chicago style. Articles, coordinating conjunctions and short prepositions stay lower case unless
they come first. Always "WOLFx"; the domain stays `wolfx.io`.

**The copy:**
- **Lead lines** (Poppins SemiBold, 64 px or more, upper third), 76 words:
  1. Introducing the New Missile from WOLFx
  2. Built to Launch from Anywhere
  3. Three Stages Carry It to Orbit in Minutes
  4. Then It Turns and Dives at Hypersonic Speed / The Nose Opens on Seven Payloads
  5. Each One Steers to Its Own Target
  6. Small Thrusters Let It Change Course as It Falls
  7. Its Weaving Path Is Built to Slip Past Interceptors
  8. Open It Up: Three Stages and Seven Payloads
  9. Lykos Wx-1, Engineered by WOLFx
  10. *(end card)* Let's Make Something Great Together.
- **3D words, tags and pills in the scene:**
  - "Lykos" and "Wx-1"
  - label "8×8 Mobile Launcher"
  - tag "7 Independent Payloads"
  - "Thrusters"
  - labels "Interceptor" and "Lykos Payload"
  - "Stage 1", "Solid Fuel", "Stage 2" and "Stage 3"
  - "7 Payloads, Each with Its Own Engine"
  - spec pills "3 Stages", "Solid Fuel", "Hypersonic" and "7 Payloads"

## Shot table
"Mirrors" is the reference beat (Part 01) whose structure we borrow. Red is the shot's one red element: brand rule,
one per scene, only on large words or lines.

| # | Time | Mirrors | On-screen text (timing) | Picture | Camera | Red | Sound |
|---|---|---|---|---|---|---|---|
| 1 | 0-6 | hero missile hovering, title standing in the scene (0-4 s) | 3D "Lykos" lands 0.5 and "Wx-1" 1.0; lead line 1 steps in 1.4-2.6; hold to 5.6 | **The page as a world:** white floor and sky, faint grid, grey contour lines drawing across the floor. Lykos hovers on its side and turns slowly: matte ink body, square-cut fins, hairline panel lines, a small white "Wx" monogram decal | slow push in with a 15° orbit | thin rule under "Lykos" | tick 0.5, low pad |
| 2 | 6-12 | launcher appears as X-ray wireframe around the missile, turns solid, label in perspective (4-7 s) | lead line 2 steps in 6.6-7.6; "8×8 Mobile Launcher" types onto the floor in perspective 9.0-9.8; hold to 11.6 | an 8×8 launcher truck assembles around the missile as grey hairline wireframe, so Lykos stays visible inside, then turns solid matte ink (7.5-8.1) | static, slight drift | none | tick 9.0 |
| 3 | 12-18 | launcher raises the missile, launch (7-13 s) | lead line 3 steps in 12.6-14.0; hold to 17.6 | the launcher arm raises Lykos upright (12.0-13.5); ignition at 14.0, white smoke rolls over the floor and the contour lines ripple outwards like a topographic wave; lift-off 15.0. At 17.0-18.0 Lykos climbs into its own smoke, which fills the frame white, and the cut to the dark scene happens under it | low angle, tilting up with the missile | none | low swell 14-16, whoosh 17.2 |
| 4 | 18-28 | space flight, stage burn, fairing opens, payload callout (13-29 s) | first half of line 4 steps in 18.6-20.0; second half 24.0-25.2; tag "7 Independent Payloads" (bar wipes in, then the text) 25.5; hold to 27.6 | **Dark flip** (the site's black footer and buttons): ink space with a faint dark grid, no stars or planet. Stage burn; stage 1 falls away (19.0); Lykos pitches over into a dive with speed streaks (21-23); the nose splits like a clamshell (24.0) on seven pods, six around one | tracking alongside, then a slow orbit as the nose opens | the tag's outline | whoosh 19.0, chime 24.0, tick 25.5 |
| 5 | 28-32 | payloads streaking down through the sky (29-33 s) | lead line 5 steps in 28.4-29.6; hold to 31.6 | flip back to white: seven ink trails streak down across the white sky at a steep angle, spreading apart | wide, static | none | soft whooshes 28.2, 28.7, 29.2 |
| 6 | 32-38 | close-up on the thrusters, big word (33-38 s) | 3D "Thrusters" builds 33.0 (letter fragments, 0.35 s); lead line 6 steps in 34.0-35.6; hold to 37.6 | one payload in close-up over white: small thruster puffs fire at its base (34.5, 36.0) and short arrows show the push | slow push in | the thrust arrows | tick 33.0, puffs |
| 7 | 38-46 | flat diagram, weaving paths, bracket labels (38-45 s) | lead line 7 steps in 38.6-40.2; "Interceptor" 41.0; "Lykos Payload" 43.0; hold to 45.6 | a flat white card with the site's thin vertical rule on the left. A grey interceptor path rises from below while the payload's path draws on and weaves past it (40.0-45.0); the two never meet | slow tilt down along the paths | the Lykos path | ticks 41.0 and 43.0 |
| 8 | 46-60 | exploded view in the studio (45-68 s) | lead line 8 steps in 46.6-48.0; "Stage 1" 49.0; "Solid Fuel" 50.0; "Stage 2" 52.0; "Stage 3" 54.0; "7 Payloads, Each with Its Own Engine" 57.0; hold to 59.6 | white studio (white centre, light grey edges, floor grid). Lykos slides out of its launch tube and stands upright, then its stages slide apart vertically (0.6 s each, on 49, 52 and 54), each word beside its stage. A cut-away of stage 1 shows the solid fuel. The nose opens on the seven pods (56.0), then closes, and a grey hairline grid scans down the nose (58.0-59.0) | booms up the stack (a tall stack fills the vertical frame) | "7 Payloads" | whoosh per stage, chime 57.0 |
| 9 | 60-64 | *(our addition: sign-off before the end card)* | lead line 9 steps in 60.4-61.4; spec pills land on the half-beats 62.0-63.5; hold to 63.6 | stages slide back together (60.0-60.6). The camera pulls back as Lykos lifts away off the top of the frame, leaving a thin ink path. Four red-outlined spec pills (the banner's style) line up under the sign-off | pull back | pill outlines | swell 60.0, a tick per pill |
| End | 64-70 | *(standalone)* | wordmark lands 64.0; line 10 builds 64.6-65.4; `wolfx.io →` button 66.0; hold to 70.0 | kit end card on the white page with faint grid and contour lines: WOLFx wordmark (black interim PNG), the closing line, and `wolfx.io` in a square black button with a thin → | static | none (the logo never sits on red) | music resolves from 64.0, tick 66.0 |

## Look: wolfx.io as a 3D world
- **World:** the site's white page with depth. A pure white floor and sky, a faint `#ECECEC` grid, and grey
  `#909090` contour lines as the only terrain. The site's thin vertical rule and hairlines are set pieces. It
  replaces the reference's forest.
- **Dark flip:** `#121212` with a faint grid and white type, like the site's footer and buttons. It replaces the
  reference's space; no stars, planets or nebulae.
- **Lykos:** matte `#121212` with chamfered square-cut details (the site has square corners), hairline panel lines
  in `#909090` and a small white "Wx" monogram decal from `assets/logo/wolfx-monogram-wx.png`. It has no red of
  its own, so each shot can keep its one red.
- **Type:** Poppins throughout, in Title Case.
  - Lead lines: SemiBold, 64 px or more, up to three lines, in the upper third.
  - Big 3D words: ExtraBold ink with tight tracking (about -0.02em), 120 px cap height or more.
  - Tags and labels: SemiBold, 32 px or more. Pills: Bold, 40 px or more. All sizes at 1080 wide.
  - Red text only at 100 px or more (contrast).
- **Label kinds:**
  - big 3D words in the scene;
  - WOLFx button tags (square black box, white text, thin →) on a hairline leader ending in a small square dot;
  - thin bracket labels on the diagram;
  - red-outlined pills for the closing specs.
- **Light:** soft and clean, per `/hyperframes` `references/types/3d.md`: warm key, cool rim, a soft environment
  and a contact shadow under the object.
- **Motion:** strong ease-out, no bounce. Lines draw on (contours, hairlines, pill outlines, paths).
- **Sound:** music bed and SFX from `tools/make_audio.py` (`cues.json`, `"vo": null`, `"bpm": 120`,
  `"end_card": 64.0`). No explosions.

## Borrowed from the reference, and left behind
- **Borrowed (structure only):** the cold open's eight beats in the same order:
  1. hero and title;
  2. X-ray launcher;
  3. launch;
  4. stage drop and nose reveal;
  5. streaks;
  6. thrusters;
  7. weaving-path diagram;
  8. exploded view.

  Also its pass-through transition and its tags on leaders.
- **Left behind:**
  - its sentences, models, teal/amber/lemon palette and watermark;
  - the forest, photoreal space and plasma (also simpler to build: there is no 3D template yet, and WebGL on this
    machine is untested);
  - real weapons, countries and defence systems;
  - explosions;
  - an extruded 3D wordmark: the logo exists only as PNG, so it is used flat on the end card.

## Superseded: Draft 2 lead lines (metaphor version, text only)
If WOLFx Built a Missile, It Would Launch Products · Every Launch Starts with a Clear Picture of Your Problem ·
We Get That Right First / So It Knows Where It's Going · Inside Are Seven Payloads, One for Every Service · Each
One Lands Where Your Business Needs It · When Plans Change, We Change with Them · That's How It Gets Past What
Sinks Most Projects · Three Stages, All Fuelled by Clarity · From Idea to Delivery and Beyond · Let's Make
Something Great Together.
