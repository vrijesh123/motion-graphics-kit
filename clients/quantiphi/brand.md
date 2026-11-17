# Quantiphi: brand for motion graphics

How Quantiphi looks and sounds, translated into this kit's template. Colours come from the site's own code
[S8] and logo files [S9], and were checked against a screenshot of the live homepage
(`assets/reference/quantiphi-site-hero.png`) [S1]. Anything we suggest rather than Quantiphi stating it is marked
"suggested". None of it has been confirmed by Quantiphi yet.

## Look in one line
Dark and premium: a deep navy night-sky gradient with white Poppins headlines and one bright green line. Green
growth curves run through dotted nodes. Glassy blue cube icons sit in an "A + B + C = result" equation. The logo is
a 3×3 grid of navy, green and white squares.

## Palette
The homepage is **dark-first** [S1, S8], so the default video palette is dark. The site also has a light mode
(toggle in the header) and light sections; use the light set below for a white video.

**Default (dark):**

| Token | Hex | Source | Use in video |
|---|---|---|---|
| `--bg` | `#02051F` | Outer stop of the hero's radial gradient `#0B1868 → #050F45 → #02051F` [S8]; measured `#02051E` in the screenshot | Background. Add the radial glow (below) behind the main subject |
| `--ink` | `#FFFFFF` | Hero headline line 1 [S1, S8] | All main type |
| `--soft` | `#223D80` | Logo navy (`#223E80` in the logo file) and the site's most-used navy [S8, S9] | Highlighter bars behind white words, grid lines, card fills, ghost words |
| `--accent` | `#48DD84` | Hero headline line 2, "Compound Your Edge." (in the hero HTML; measured `#48DD84`) [S1, S8] | One key word per scene, the growth curve, node dots |
| `--mute` | `#CBD5E1` | The site's stat-label text colour (Tailwind slate-300) [S8] | Secondary text, small labels |

```css
:root { --bg: #02051F; --ink: #FFFFFF; --soft: #223D80; --accent: #48DD84; --mute: #CBD5E1; }
/* hero glow, from the site [S8]: put on #root or a full-frame layer */
#root { background: radial-gradient(ellipse 90% 65% at 50% 58%, #0B1868 0%, #050F45 40%, #02051F 75%, #04061C 100%); }
```

**Light alternative:**

| Token | Hex | Source |
|---|---|---|
| `--bg` | `#FFFFFF` (or `#F7F8F8` for panels) | Site light sections [S8] |
| `--ink` | `#333333` | Wordmark grey in the dark-on-light logo [S9] and the site's body text [S8] |
| `--soft` | `#E4FFEF` | Pale mint panel fill on the site [S8] |
| `--accent` | `#00874C` | Primary button green [S1, S8]. The brighter site green `#12A04E` fails as small text on white |
| `--mute` | `#223D80` | Logo navy [S9] |

```css
:root { --bg: #FFFFFF; --ink: #333333; --soft: #E4FFEF; --accent: #00874C; --mute: #223D80; }
```

**Contrast (WCAG):**
- **Dark set:**
  - White on `#02051F` is 20.1:1.
  - Green `#48DD84` on `#02051F` is 11.4:1, and 8.9:1 on the glow centre `#0B1868`.
  - Slate `#CBD5E1` is 13.5:1.
  - Navy `#223D80` on `#02051F` is only 2.0:1. It works as a fill or shape, never as text.
- **Light set:**
  - `#333333` on white is 12.6:1.
  - Button green `#00874C` is 4.6:1, fine for key words.
  - Site green `#12A04E` is 3.4:1, so big text only (100 px and up).
  - Logo green `#23B082` is 2.8:1, so shapes only.
  - White on `#00874C` is 4.6:1 (the button style).

**Other greens on the site:**
- `#12A04E`: links and section labels, the site's most-used colour [S8].
- `#00874C`: buttons [S1].
- `#23B082`: logo [S9].
- `#48DD84`: hero headline [S8].

Treat them as one accent. On dark use `#48DD84`; on light use `#00874C`. Never put two greens in one scene.

## Type
- **Poppins for everything.** The site's CSS loads Poppins 400, 500, 600, 700 and 900 [S8]. The hero headline is
  Poppins Bold with tight tracking, in Title Case ("Own Your Enterprise Intelligence.") [S1].
- **Files:** `assets/fonts/`, static TTFs 400-800 under the SIL OFL 1.1 licence (see `assets/fonts/FONTS.md`).
  There is one `@font-face` per weight:

```css
@font-face { font-family: "Poppins"; src: url("assets/fonts/Poppins-Regular.ttf") format("truetype"); font-weight: 400; font-display: block; }
@font-face { font-family: "Poppins"; src: url("assets/fonts/Poppins-Medium.ttf") format("truetype"); font-weight: 500; font-display: block; }
@font-face { font-family: "Poppins"; src: url("assets/fonts/Poppins-SemiBold.ttf") format("truetype"); font-weight: 600; font-display: block; }
@font-face { font-family: "Poppins"; src: url("assets/fonts/Poppins-Bold.ttf") format("truetype"); font-weight: 700; font-display: block; }
@font-face { font-family: "Poppins"; src: url("assets/fonts/Poppins-ExtraBold.ttf") format("truetype"); font-weight: 800; font-display: block; }
```

- **Mapping to the template:**
  - `#root` font-family becomes `"Poppins", sans-serif`.
  - `.lead` (lead-in line): Poppins 500, white, as in the site's sub-lines.
  - `.keyb` (big key word): Poppins 700, in `--accent` or white, as in the hero headline.
  - Drop the template's italic serif `.key`. Quantiphi has no serif; emphasise with colour (white to green), as the hero
    does.
- **Size:** Poppins sets wider than the template's Figtree. Expect to shrink the template's big key-word sizes by
  roughly 10-15% and re-check every line for wrapping.
- **Casing:** Site headings use Title Case. The kit's caption default is sentence case. Suggested: sentence case
  for captions and VO text, Title Case only for product names and the "Own Your Enterprise Intelligence." campaign
  line. Confirm (open question in `README.md`).
- **The name:**
  - In text it is always **Quantiphi**, with a capital Q [S1, S6].
  - The wordmark is lower-case "quantiphi" [S9]. That is artwork; never type the name in lower case in captions.
- **Product names** (exact casing):
  - **baioniq**: always lower-case [S1, S10].
  - **Codeaira** [S11].
  - **Dociphi** [S12].
  - **Qollective.CX**: the product page writes ".CX" [S13], while the navigation writes "Qollective.cx" [S1]. Use
    ".CX" and confirm.

## Logo
| File | What | Use |
|---|---|---|
| `quantiphi-logo-on-dark.svg` | Full logo: grid symbol, white "quantiphi" wordmark, tagline "Solving What Matters". The client's `Qlogo-Light.svg`, unaltered [S9] | Dark scenes and the default end card |
| `quantiphi-logo-on-light.svg` | Same, with a `#333` wordmark and tagline. The client's `Qlogo-Dark.svg`, unaltered [S9] | White scenes |
| `quantiphi-logo-white-tagline.svg` | All-white version, with the symbol drawn as white squares [S9] | Over photos or busy colour, or when the coloured squares clash |
| `quantiphi-mark-grid.svg` | The 3×3 symbol alone: nine squares cut from `Qlogo-Light.svg` with their geometry and colours unchanged. Each square has an id (`r00` to `r22`, row then column) for animation | Small persistent badge, logo-build animation, grid-wipe transitions |

**How to use it:**
- **The grid:**
  - Left column and bottom row: navy `#223E80`.
  - Top-middle, top-right and middle-right: green `#23B082`.
  - Centre: white (empty on the light logo).
  - Keep that pattern exactly. Don't recolour squares, add squares or rotate the grid.
- **No tagline-free version yet.** All supplied full logos include "Solving What Matters". At small sizes (under
  about 400 px wide) the tagline gets thin, so use the grid symbol alone there and ask Quantiphi for a wordmark
  without the tagline.
- **Navy on navy.** On `#02051F` the navy squares are only 2.0:1. Place the logo over the lighter glow (`#0B1868`)
  or accept that the navy squares read as a quieter base. Never put the logo on green.
- **Clear space (suggested):** at least one grid square's width on every side.
- Ask Quantiphi for brand guidelines; none are public.

## Graphic language
All from the live homepage and campaign pages [S1, S4]:
- **The equation:** "( pillar + pillar + pillar + pillar + pillar ) = Compounded Edge". Five glass-cube icons
  joined by "+" signs inside big round brackets, then "=" and a result cube. It is their signature diagram.
- **Growth curve:** a thick green line rising from bottom left to an arrowhead, with ring-and-dot nodes connected
  by dashed vertical lines to labels above.
- **Glass cubes:** translucent blue cubes with white line icons (cube/chip, database, robot arm, head with heart,
  institution). The result is a Rubik-style cube in navy, green and white, echoing the logo grid.
- **Numbered cards:** "01", "02", "03", "04" problem cards ("Point Solution Sprawl", "Unpredictable Economics",
  "Ecosystem Lock-In", "Reinvention Fatigue").
- **Big stat blocks:** for example "60-80%", "3 Months", "100%" with a short label under each.
- **Partner and analyst logo strips:** Google Cloud, AWS, NVIDIA, Snowflake and others. Third-party logos need
  permission before going in a video.
- **Corners:** rounded (7-12 px on buttons and inputs [S1]); cards are soft-cornered.

## Motion direction (suggested)
- **Pace:** calm enterprise explainer, not fast punch. Scenes of 2.4-4 s on one constant dark background. This fits
  `pin-901986631645535447` (InsiderForce: word-by-word caption build, objects entering from the frame edges) and
  `pin-1061653312177886416` (Solution Wagon: blur-in words, defocus dissolves). Use their structure and timing,
  never their look.
- **Text entrance:** word by word on the VO. Each word slides up 20 px and fades from `--mute` to white. The key
  word lands in green, like the hero's two-line headline (white line, then green line).
- **Signature moves to build from Quantiphi's own graphics:**
  1. **Logo build:** the nine grid squares drop in one by one (stagger 0.05 s, ease-out, no bounce), then the
     wordmark fades up. This is for the opening and the end card.
  2. **Grid wipe:** the frame divides into a 3×3 grid of navy squares that flip to reveal the next scene. Use it at
     section changes only.
  3. **Equation build:** terms pop in with "+" between them, the brackets close and "=" lands the result. Use it for
     any "X + Y = outcome" line.
  4. **Growth curve draw:** the green line draws left to right (stroke-dashoffset), nodes pop as it passes, and the
     arrowhead lands on the payoff word.
  5. **Counter roll:** stats count up (55%, 3.5x) under a thin green rule.
- **Easing:** `power3.out` or `expo.out` for entrances and 0.2-0.35 s transitions. The site's hover easing is a
  slight overshoot (`cubic-bezier(0.34, 1.15, 0.64, 1)`) [S8]. Use that overshoot only for small icon pops, never for
  type.
- **Life during holds:** slow drift of the radial glow, a faint grid of navy lines at 6-8% opacity, and a gentle
  float on the glass cubes.

## Voice and wording
- **Tone:** confident, enterprise and outcome-led. The site speaks to C-level buyers about control, ownership and
  P&L, not to developers about features [S1, S2, S4].
- **Their phrases, to reuse:**
  - "Own your enterprise intelligence."
  - "Compound your edge."
  - "Solve what matters" ("Ready to Solve What Matters?")
  - "AI-native"
  - "sovereign AI"
  - "lasting AI capability"
  - "from expense to asset"
  - "without reinvention"
  - "Agentic Wild West"
- **Their framing:** the question isn't whether enterprises can adopt AI but whether they can build AI they
  control [S4].
- **Words to handle with care:**
  - Jargon such as "Inner Loop", "Outer Loop", "Knowledge Vault", "Decision Graph" and "FinOps-optimized LLM routing"
    is fine on a web page, too dense for a 30 s VO. Say "your own AI platform, inside your cloud" instead.
  - Don't use "Quantifi" (a different company) [S29].
- **Pronunciation for VO:** "kwon-TIF-ee" (stress on the second syllable). This comes from user-submitted audio, not
  the company [S28]; confirm by ear from a Quantiphi video before recording.
- **Whisper fixes:** Whisper is likely to write:
  - "Quantify", "Quantiphy" or "Quantifi" for **Quantiphi**
  - "bionic" for **baioniq**
  - "collective" for **Qollective.CX**
  - "Docify" for **Dociphi**
  - "Code Ira" for **Codeaira**

  Fix these by ear.

## End card
Default (suggested, needs approval):
- `quantiphi-logo-on-dark.svg` centred on the glow, about 600 px wide.
- Below it the line "Own your enterprise intelligence." in white Poppins 600, with "intelligence." in green.
- Then `quantiphi.com` in `--mute`.
- Hold for at least 2 s.
- Add contact details (info@quantiphi.com, +1 508-661-9050, both public on the site [S5]) only once Quantiphi
  approves.
