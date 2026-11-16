# WOLFx: brand for motion graphics

How WOLFx looks and sounds, translated into this kit's template. Colours were measured from WOLFx's own social
banner (`assets/reference/wolfx-social-banner.png`) and site CSS [S1, S11]. Anything we suggest rather than WOLFx
stating it is marked "suggested". None of it has been confirmed by WOLFx yet.

## Look in one line
Engineering-clean monochrome: a white page, near-black type and one red accent used sparingly. Headlines are bold
Poppins and the wordmark is a tall condensed face. Faint grid, thin hairline rules and grey topographic contour
lines. Corners are square.

## Palette
| Token | Hex | Source | Use in video |
|---|---|---|---|
| `--bg` | `#FFFFFF` | Site background, banner background [S1, S11] | Default background (pure white, not the template's cream) |
| `--ink` | `#121212` | Wordmark and pill text in the banner, measured. The site uses `#090909` text and `#000` buttons | Type, logo, dark "flip" scenes |
| `--soft` | `#ECECEC` | Suggested. The banner grid is `#F9F9F9`, too faint to survive video compression | Grid lines, highlighter bars, ghost words |
| `--accent` | `#FF2B2B` | Red pill outlines in the banner (measured) and `#ff2b2b` in the site CSS | One key word or one outline per scene |
| `--mute` | `#909090` | Contour lines in the banner (measured); the site's borders are `#888888` | Contour lines, hairlines, decoration |

```css
:root { --bg: #FFFFFF; --ink: #121212; --soft: #ECECEC; --accent: #FF2B2B; --mute: #909090; }
```

Contrast (WCAG):
- **Ink:** `#121212` on white is 18.7:1.
- **Red:** `#FF2B2B` on white is 3.7:1, so use it for big key words (100 px and up) or outlines, never for
  small text. On `#121212` it is 5.0:1.
- **Grey:** `#909090` on white is 3.2:1, so keep it for decoration. Secondary text on white needs `#6E6E6E`
  (5.1:1).

The red is a signal, not a fill. WOLFx uses it as a thin outline around black text (service pills), never as a
background. Dark scenes are a black/white flip: `--ink` background with white type, like the site's footer and
buttons.

## Type
- **Poppins for all text.** The site's CSS sets every heading and body style in Poppins [S11]. The homepage hero
  "A Creative Technology Company" is Poppins Bold/ExtraBold with tight tracking (about -0.02em); the subline
  "Everything Technology is our Playground" is Poppins Regular.
- **The files are static, one per weight** (`assets/fonts/`, SIL OFL 1.1). Each weight needs its own
  `@font-face`, unlike the template's single variable-font line:

```css
@font-face { font-family: "Poppins"; src: url("assets/fonts/Poppins-Regular.ttf") format("truetype"); font-weight: 400; font-display: block; }
@font-face { font-family: "Poppins"; src: url("assets/fonts/Poppins-Medium.ttf") format("truetype"); font-weight: 500; font-display: block; }
@font-face { font-family: "Poppins"; src: url("assets/fonts/Poppins-SemiBold.ttf") format("truetype"); font-weight: 600; font-display: block; }
@font-face { font-family: "Poppins"; src: url("assets/fonts/Poppins-Bold.ttf") format("truetype"); font-weight: 700; font-display: block; }
@font-face { font-family: "Poppins"; src: url("assets/fonts/Poppins-ExtraBold.ttf") format("truetype"); font-weight: 800; font-display: block; }
```

- **Mapping to the template:**
  - `#root` font-family becomes `"Poppins", sans-serif`.
  - Lead line `.lead`: Poppins 500-600.
  - Key word `.keyb`: Poppins 800, ink or red.
  - The template's italic serif key word (`.key`, Instrument Serif) is not part of WOLFx's look. Emphasise with
    weight, size and the red accent instead, and drop the serif from the project.
- **Poppins sets wider than the template's Figtree.** In a test build of the template (2026-11-16), the 176 px
  "in seconds." line nearly filled the 1080 px frame, and a 64 px end-card line wrapped to two lines. Expect to
  shrink the template's big key-word sizes by roughly 10-15%, and re-check layout after any copy change.
- **The wordmark is not Poppins.** It is a tall condensed face, and we have not identified it. Treat it as
  artwork: wherever the logo appears (plate badge, end card), use the logo file and never imitate it with a font.
  In running captions and VO text, the name is ordinary Poppins text spelled `WOLFx`, so each caption word can be
  timed like any other. Ask WOLFx for the typeface before using condensed headlines.
- **Casing:** WOLFx's site headings use Title Case ("Our Featured Work"). The kit's default for captions is
  sentence case. Confirm which WOLFx wants (open question in `README.md`).

## Logo
| File | What | Use |
|---|---|---|
| `wolfx-wordmark-black-interim.png` | 699×437, `#121212` on transparent, extracted from WOLFx's social banner | Light scenes and end card, up to about 700 px wide. Interim until WOLFx sends an SVG |
| `wolfx-wordmark-white-interim.png` | Same, white | Dark scenes |
| `wolfx-wordmark-white-web-213.png` | 213×110, the site's own header logo file, untouched | Small marks only (under 200 px wide) |
| `wolfx-monogram-wx.png` | 420×400 "Wx" monogram, the site favicon, untouched | Small persistent badge, app-icon style tiles |

- Write the name exactly **WOLFx**: capital WOLF, lower-case x. Some client testimonials write "WolfX" or
  "Wolfx"; captions must not.
- The banner also shows the wordmark inside a thin black rectangle, used as a small corner tag. That suits the
  template's small persistent logo tile at the top of the frame.
- Never recolour the logo other than black or white. Never stretch it, outline it or put it on red.

## Graphic language (from WOLFx's site and social banner)
- **Faint grid** across the page: the template's grid plate, solid hairlines in `--soft` instead of dashes.
- **Topographic contour lines:** thin grey (`--mute`) flowing strokes entering from a corner. Draw our own
  SVG paths in that style; a slow `stroke-dashoffset` draw-on keeps holds alive.
- **Outlined pills:** black bold text in a rounded pill with a red outline (about 4 px at 1080 wide). WOLFx
  uses them to list services, and they work for any list.
- **Hairline rules:** thin grey lines under headlines and a vertical rule along the left edge of the site.
  Editorial and precise.
- **Square-cornered black buttons** with a thin right arrow ("Contact Us →"), plus a circled arrow icon on
  links.
- **The site moves:** GSAP with scroll-triggered reveals and smooth scrolling ("scroll to experience the
  journey"). The words "from idea to delivery and beyond" step in one at a time [S1], already kinetic type.

## Motion direction (suggested)
- **Punchy promos:** follow the MotionDesigners reference (`pin-933230354043913635`). Its light/black flip, red key
  word and black iris reveal map almost one-to-one onto WOLFx's white, black and red.
- **Calm explainers** (process, case studies): follow the InsiderForce reference (`pin-901986631645535447`).
  Grey-to-black word builds on one light background suit Poppins and the editorial site.
- **Easing:** strong ease-out, no bounce. Precise rather than playful.
- **Lines** draw on (hairlines, contours, pill outlines) rather than popping in.
- **Red:** one red element per scene at most, saved for the word that matters.

## Voice and wording
- **Tone:** confident, plain and partner-like. Their core values start with "Clear, Concise and Confident
  communication" [S2]. They speak as "we", to a business owner.
- **Their own lines, usable in scripts:**
  - "A creative technology company." / "Everything technology is our playground." [S1]
  - "We are your technology partners." [S1]
  - "Allow us to handle the complexities of technology, so you can stay focused on driving your vision forward." [S1]
  - "From idea to delivery and beyond." [S1]
  - "Let's make something great together." (the closing CTA on every page) [S1]
  - "Designs that work, not just look good." [S5]
  - "Instead of jumping straight into code, we first work with business owners and tech teams to create clarity
    around the problem." (their stated difference, from their TechBehemoths profile) [S7]
- **Avoid:** "best digital agency" superlatives (they appear in WOLFx's search metadata, not its own copy),
  long technology lists read aloud, and slogan fragments (kit rule).
- **Pronunciation:** we assume "Wolf-ex"; confirm. Whisper will hear "Wolf X", "WolfX" or "Wolfie". Fix it to
  "WOLFx" in `vo_words.json`.

## End card
The WOLFx wordmark (black on white), the line "Let's make something great together." and `wolfx.io`. Add a phone
number or email only once WOLFx confirms one: the listings disagree (see `sources.md`).
