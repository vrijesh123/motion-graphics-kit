# Quantiphi: "Own your AI" (vertical promo)

## Decisions and feedback (newest last)
- 2026-11-18:
  - User asked for a Quantiphi script on the theme and structure of reference `ig-Dbc1KrKh2wV`.
  - Draft 1 written. Not yet approved.
  - Assumed: about 29 s, 1080x1920, 30 fps, call to action = quantiphi.com.
- 2026-11-18: user asked to build Draft 1 as a video.
  - Theme colours given by the user: navy `#223D80` and green `#3C823F`. These replace the pack's `#48DD84`.
  - On navy, small green text uses the tint `#6CC46F`; large words use `#3C823F`.
  - Dark-world background: the client's image `assets/industries_bg.png` (from https://cdn.quantiphi.com/2025/08/Component-1industries_bg.webp). Measured gradient: `#041030` at the left to `#0A2265` at the right, with faint wave lines.
  - The two-world flip (light and dark) is kept, as in the reference.
  - VO to come from the user, so all timings are still estimates.
  - Rendered `outputs/quantiphi-own-your-ai-v1-29s.mp4` (silent VO; music and SFX only).
  - Next step: when the VO arrives, transcribe it, retime `data-t`, the scene starts and `cues.json`, re-run audio and render v2.
- 2026-11-18, feedback on v1: "rushing towards the end; without voice-over no one can read this; slow down the text transitions and the overall video."
  - **Diagnosis:** in v1, "We help you own your intelligence." held only 0.2 s before the wipe and "We don't rent you AI." about 0.8 s. "Most companies" showed about 0.5 s and "We help you own it." about 0.9 s. The camera-tracked "and the bill keeps growing" never showed the whole sentence at once.
  - **v2 changes:**
    - Every line holds at least 0.5 s + 0.3 s per word after it is complete.
    - Typing slowed to 15–16 characters/s.
    - Word blur-ins take 0.4 s (was 0.28).
    - Pans and whips take 0.45 / 0.3 s (were 0.34 / 0.2).
    - One beat per pill.
    - "and the bill keeps growing." is now typed as two centred lines that stay above the cost card.
    - The end card holds 2.3 s.
  - **Result:** the video is 28.8 s → 45 s. Rendered `outputs/quantiphi-own-your-ai-v2-45s.mp4`.
  - When the VO arrives, its timing replaces these holds. Ask the voice talent to read slowly with pauses, or the video will shrink back toward about 30 s.

## Brief
| | |
|---|---|
| Client | Quantiphi (pack: `clients/quantiphi/`, not yet confirmed by the client) |
| Audience | Enterprise and transformation leaders who already pay for AI tools and services |
| The one message | **Own your AI instead of renting it.** (Their line: "Own your enterprise intelligence.") |
| Call to action | quantiphi.com on the end card |
| Length | About 29 s: 25.5 s of VO plus a 3 s end card |
| Format | 1080x1920, 30 fps |
| Reference | `refrences/2d-motion-graphics/ig-Dbc1KrKh2wV` (Indi Creative, "Most agencies sell you ads") |
| Tone | Confident, calm, outcome-led; spoken like a person, not slogans |

**How the reference maps to Quantiphi:**

| Reference beat | Quantiphi beat |
|---|---|
| "Most agencies sell you ads." | "Most companies rent their AI." |
| "We build the system behind the growth." | "We help you own it." |
| A pill track of four connected services | A pill track of what Quantiphi builds (platform, data, agents, your cloud) |
| "Connected" | "Works together" |
| Real proof assets | Proof drum of industries plus a project count |
| "Growth isn't left to chance" | "AI you own starts to compound" |
| Brand sting | Brand sting |
| "We don't run your marketing. We build your empire." | "We don't rent you AI. We help you own your intelligence." |

---

## Draft 1

### Voice-over (63 words, about 25.5 s, 2.5 words/s)
> Most companies rent their AI, and the bill keeps growing.
> We help you own it.
> We build your platform, data and agents inside your cloud, and every piece works together.
> This isn't theory. It comes from thousands of real projects.
> AI you own stops being a cost and starts to compound.
> Quantiphi.
> We don't rent you AI. We help you own your intelligence.

Read with the sound off, the on-screen words alone carry: rent → own → built inside your cloud → works together →
not theory → starts to compound → own your intelligence.

### Shot table
Times are **estimates**: 3 words/s inside a phrase, 0.5 s pauses, VO starting at 0.2 s. Real times come from the
recorded VO.

| Scene | VO line | On-screen words (lead-in / key word) | Visual | Transition out | Approx time | Borrows from (ref `ig-Dbc1KrKh2wV`) |
|---|---|---|---|---|---|---|
| 1 Hook | "Most companies rent their AI," | "Most companies" / "rent [tile] their AI." | **Light world.** "Most companies" blurs in word by word. "rent [icon tile] their AI." follows with the black rounded tile (white cloud with a small price tag) popping inline | A caret "\|" appears; whip left with motion blur | 0.2–1.9 | Scenes 1–3 (blur-in words, inline icon tile, caret whip) |
| 2 Cost | "…and the bill keeps growing." | Typed close-up "the bill keeps growing\|" | A dark usage card slides in ("AI usage cost", a line climbing steeply, bars growing). It is illustrative only, with **no figures or currency**, just an upward arrow | Hard cut to dark | 1.9–3.6 | Scene 4 (count-up dashboard card), inverted: the line rising is the problem |
| 3 Turn | "We help you own it." | "We help you" / **"own it."** (green) | **Dark world** (navy glow). Typewriter close-up "own\|" huge in white with glow, then a zoom-out whip to the small full line, "own" in `#48DD84` | Camera pans right into the pill track | 3.9–5.6 | Scene 15 (zoomed typewriter, then whip zoom-out) |
| 4 What we build | "We build your platform, data and agents inside your cloud," | One pill per noun: "AI platform", "Your data", "Agents\|" (search bar, typed), "Your cloud" | Glass pills on one baseline; the camera pans one pill per spoken noun. "Agents" is the search-bar pill with a **green fill wipe**. Faint 3×3 grid squares drift in the navy glow behind | Zoom out to the full row | 6.1–9.5 | Scenes 5–8 (pill track, search-bar wipe) |
| 5 Connected | "…and every piece works together." | "Every piece" / **"works together."** | The camera pulls back. The four pills now sit in one row, joined by a thin green line with ring-and-dot nodes (Quantiphi's growth-curve node style). A **flash band** carries us into the light world, where "Works together" blooms in a white pill with a green rim | Cut | 9.5–11.2 | Scenes 9–10 (zoom-out reveal, flash band, "Connected" pill) |
| 6 Proof | "This isn't theory. It comes from thousands of real projects." | "This *isn't* **theory**" (italic lock-up), then **"4,500+ data and AI projects"** (confirm) | **Dark world.** A drum of rolling strips, one industry per strip: Banking, Healthcare, Insurance, Public sector, Retail, Telecom, Manufacturing, Life sciences (their own industry list, **no client names**). The centre strip is bright, the rest dim. A push-in, then the counter rolls 0 → 4,500+ under a thin green rule | Vertical whip up | 11.7–15.4 | Scene 14 (Ads Manager result drum, "This isn't theory" header) |
| 7 Thesis | "AI you own stops being a cost and starts to compound." | "AI you own stops being a cost" / **"and starts to compound."** | Quantiphi's own hero graphic, rebuilt: the green growth curve draws left to right through ring-and-dot nodes. The flat grey "cost" line beneath it fades out, and the arrowhead lands on "compound". Typewriter close-up on "compound\|", then a zoom-out to the full line | Grey dissolve to light | 15.9–19.9 | Scene 15 (typed thesis on dark, light streak); curve from quantiphi.com (`brand.md` "Graphic language") |
| 8 Logo sting | "Quantiphi." | (logo) | **Light world.** The 3×3 grid **builds square by square** (navy, then green, then the white centre, stagger 0.06 s) instead of the reference's bouncing letters. The wordmark and "Solving What Matters" fade up | Blur fade | 20.4–21.2 | Scene 16 (logo sting) |
| 9 Sign-off 1 | "We don't rent you AI." | "We don't rent you AI." | Light world, small centred line (about 60 px). Words blur in from pale green to ink, one per VO word | Blur out | 21.5–23.2 | Scene 17 |
| 10 Sign-off 2 | "We help you own your intelligence." | "We help you **own** your intelligence.\|" | Typewriter with a blinking caret, "own" in `#00874C` | **Grid wipe** (3×3 navy squares flip) to the end card | 23.6–25.6 | Scene 18, plus Quantiphi's grid as the set-piece |
| 11 End card | (none; music resolves) | "Own your enterprise **intelligence.**" + quantiphi.com | **Dark world**, the default end card from the pack: `quantiphi-logo-on-dark.svg` about 600 px wide over the glow, the line in white Poppins 600 with "intelligence." in green, quantiphi.com in slate. Held **3 s** (the reference's abrupt ending is not copied) | End | 25.8–28.8 | `clients/quantiphi/brand.md` "End card" |

### Look
The reference's two worlds are kept, translated to Quantiphi's palette (`clients/quantiphi/brand.md`):

- **Dark world** (pack default):
  - `--bg #02051F` with the hero radial glow `#0B1868 → #050F45 → #02051F`.
  - White Poppins type with a soft glow.
  - Accent `#48DD84`.
  - A faint green light streak replaces the reference's amber streak.
- **Light world** (pack's light set):
  - White, with soft mint corners in place of the reference's yellow ones. The mint is `#B9E3C9` (the site's secondary green) and `#E4FFEF` through the middle.
  - Ink `#333333`, with an optional subtle gradient fill to navy `#223D80` (suggested, the counterpart of the reference's black-to-ochre).
  - Accent `#00874C`.
- **One accent per scene:** green only, the lighter green on dark and the deeper green on light.
- **Type:** Poppins (400/500 for lines, 700 for key words). Poppins has no light italic, so the italic lock-up in scene 6 uses Poppins Italic 400 and Bold Italic 700. Those two files still need adding from Google Fonts at build time.
- **Logo:**
  - The grid build in scene 8 uses `quantiphi-mark-grid.svg`.
  - The end card uses `quantiphi-logo-on-dark.svg`.
  - Square-by-square animation of the grid needs Quantiphi's OK.
- **Motion** (from the reference):
  - blur-in words;
  - zoomed typewriter with caret;
  - glass pills on a panning track;
  - motion-blur whips (faked with directional blur);
  - a flash band and a grid wipe as the two set-pieces.

### Claims and assets Quantiphi must confirm before this goes on screen
1. **"4,500+ data and AI projects"** (scene 6). From their Gemini for Healthcare release [S18]. The VO only says
   "thousands of real projects"; confirm both.
2. **The cost chart in scene 2** is illustrative, with no figures. Confirm they're comfortable implying that rented AI
   costs keep rising (their own framing: "unpredictable economics", "consumption-dependent" [S4]).
3. **"Stops being a cost and starts to compound"** paraphrases their "expense to asset" and "compound your edge"
   lines [S3, S4]. Confirm the wording.
4. **Industry names on the drum** (scene 6) come from their site's industry list [S1], with no client names or logos.
5. **Animating the logo grid** square by square (scene 8).
6. **VO:** voice, accent, and pronunciation of "Quantiphi" ("kwon-TIF-ee" is unverified).

### Open questions for you
- Is about 29 s right, or do you want a 15 s cut-down as well (scenes 1, 3, 4, 7, 10, 11)?
- Keep the two-world flip (light and dark, like the reference), or stay dark throughout, like Quantiphi's homepage?
- Who provides the voice-over (your own recording or TTS file), so timings can come from it?
- 2026-11-18, VO received: `assets/voiceover/ElevenLabs_2026-11-17T20_37_18_Emma_pvc_s50_sim75_v4.mp3` (the user's file, untouched).
  - **Working copy:** `assets/vo.mp3`. The read is 26.1 s; ElevenLabs mostly ignored the break tags.
  - **Pacing decision:** keep the readable v2 pacing rather than shrink the video to the raw read (about 29 s).
    - The read was cut at its own silences into 9 phrases, with no words cut.
    - Each phrase is placed at the start of its scene in `assets/vo_placed.wav` (offsets: 0.18 / 2.89 / 6.68 / 9.62 / 17.59 / 23.12 / 28.33 / 30.00 / 32.46 s).
    - Word times come from `assets/vo_words.json` (transcript of the placed file). `cues.json` uses `vo: assets/vo_placed.wav` with `vo_offset: 0`.
  - **Visuals:** everything was retimed to the spoken words.
    - The opening is now two stacked lines ("Most companies / rent [icon] their AI.").
    - "Every piece" now sits above the "Works together" pill.
    - Typing follows the speech.
  - **Length:** 40 s. Speech ends at 34.4 s; the end card holds from 37.3 s.
  - **Sync check:** the rendered audio was re-transcribed, and key words land within 0.1 s of their on-screen cues.
  - **Rendered** `outputs/quantiphi-own-your-ai-v3-40s.mp4`.
  - **Note:** Whisper hears the brand as "Quantity"/"Quantifi". Listen and check that the TTS says "Quantiphi" the way the client wants (unconfirmed: kwon-TIF-ee).

---

## Voice-over read for recording / TTS (matches v2 pacing, 2026-11-18)
- **Target:** about 41 s of speech, ending before the end card at 41.7 s. The last 3 s is music only.
- **Read:** calm, confident and unhurried, with a pause at each `/` (short, about 0.6 s) or `//` (long, about 1.2–1.5 s).
- **Format:** mp3 or wav, starting at 0.2 s.

| Cue (v2) | Line |
|---|---|
| 0.3 s | Most companies / rent their AI, / and the bill keeps growing. // |
| 8.8 s | We help you own it. // |
| 12.5 s | We build your platform, / your data / and your agents, / inside your own cloud, / and every piece works together. // |
| 21.1 s | This isn't theory. / It comes from thousands of real projects. // |
| 26.1 s | AI you own stops being a cost, / and starts to compound. // |
| 32.2 s | Quantiphi. // |
| 33.9 s | We don't rent you AI. / We help you own your intelligence. |

- **Pronunciation:** "Quantiphi" = kwon-TIF-ee (unverified; confirm with the client). In TTS, spell it "Kwon-tiffy" if the voice mispronounces it.
- **Change from Draft 1:** "platform, data and agents inside your cloud" became "your platform, your data and your agents, inside your own cloud" so each pill gets its own spoken beat.
