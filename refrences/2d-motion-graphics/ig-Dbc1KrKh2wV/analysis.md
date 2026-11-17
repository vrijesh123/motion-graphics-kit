# 2D motion graphics ref — Arpit Kaushik for Indi Creative, "Most agencies sell you ads" (Instagram Dbc1KrKh2wV)
https://www.instagram.com/p/Dbc1KrKh2wV/ · uploader "Arpit kaushik" (@arpit_clipsyk), posted 2026-07-31 as "Recent work for @indicreativeagency" · 24.77 s · 1076x1914 (9:16), 30 fps, VP9 about 940 kb/s + AAC 48 kHz stereo

Files here: `video.mp4` (git-ignored), `probe.json`, `cuts.json`, `audio.json`, `meta.json`, `vo_words.json` (Whisper word timestamps, 57 words), `video.info.json`.
- **How it was analysed:** built with `tools/prep_reference.py`, then checked by eye on 8 fps timestamped contact sheets covering the whole video and on full-resolution crops.
- **Colours:** sampled from decoded RGB pixels.
- **Not kept:** per the house rule, no frames are kept.

## Overview
- **What it is:** a VO-driven agency promo for a growth-marketing agency (Indi Creative). It sells "systems, not ads".
  - **Built from:** kinetic type plus real proof assets (ad creatives, the agency's website, case-study cards, Meta Ads Manager result rows), dropped into a slick two-world look.
  - **The two worlds:** a sunny yellow/cream gradient world and a black world with an amber floor glow.
  - **Payoff:** it alternates between the two and ends on a short logo sting plus a two-line typed sign-off.
- **Script (VO, Whisper, 57 words):** "Most agencies sell you ads. We build the system behind the growth. Ads, funnels, websites, follow-up. Every piece connected. Built to work as one. Nothing runs in isolation. Nothing left to guesswork. This isn't theory. This is what happens when growth isn't left to chance. Indie creative. We don't run your marketing. We build your empire." The brand is spelled "Indi Creative" on screen.
- **Voice:** one narrator at **2.35 words/s** (57 words in 24.3 s).
  - Short declarative sentences, with gaps of 0.5–0.65 s between them.
  - Speech covers 73% of the runtime.
  - The copy is deliberately punchy fragments ("Every piece connected.", "Built to work as one."). The kit's own scripts should stay conversational; borrow the visuals, not this copy style.
- **Structure:**

  | Part | Time |
  |---|---|
  | Hook / contrast | 0–4.2 s |
  | List of the four pieces (dark) | 4.25–8.75 s |
  | "Connected / built to work as one" (light) | 8.85–11.25 s |
  | Proof: website and case studies (light) | 11.25–15.6 s |
  | Proof: Ads Manager results (dark) | 15.7–18.3 s |
  | Thesis line (dark) | 18.4–20.0 s |
  | Logo sting (light) | 20.25–21.5 s |
  | Sign-off, two typed lines (light) | 21.6–24.77 s |

  - The detector found 6 shots (cuts at 4.30, 8.83, 15.57, 17.60, 20.10). By eye there are about **20 layouts, roughly 1.2 s each**, joined by whips, pushes and blur dissolves the detector misses.
- **Audio (inferred from levels only; I did not listen):**
  - Integrated −14.2 LUFS.
  - Gaps between phrases sit at −23 to −28 dB mean while speech sits around −15 dB. A **music bed about 10 dB under the VO** runs throughout.
  - The no-speech window during the logo sting (20.9–21.5 s) is the loudest gap: −18 dB mean, −3.3 dB peak. That is most likely a logo hit or whoosh.
  - The tempo estimate (156 BPM, confidence 0.09) is unreliable.
  - The video ends abruptly at 24.77 s, about 0.85 s after the last word starts.

## Look
- **Palette (measured):**
  - **Light world:** an animated two-corner gradient.
    - Saturated yellow **#FDCC00** in the top-left and bottom-right corners.
    - Near-white **#FFFFF8** in the other two corners.
    - Cream **#FDF3C8 / #FDF1C0** through the middle.
    - The gradient blobs drift slowly. Faint white swoosh curves (light-leak ribbons) cross it in some scenes.
  - **Dark world:** pure **#000000** top and middle (#120E02–#190C00 just above the glow), with a blurred amber floor glow at the bottom.
    - Glow colour **#A66900 → #D39301**, roughly the bottom 25% of the frame.
    - A thin yellow light streak (a curved swoosh) sweeps across the upper right in the thesis scene.
  - **Text on light:** a **vertical gradient fill**, near-black **#0E0D08** at the top of the letters to ochre **≈#9A7000–#B08400** at the baseline. It reads as black with a golden glint.
  - **Text on dark:** white, with a soft white outer glow on big words.
  - **Brand yellow:** the logo's "CREATIVE" is **#F8D410 / #FCD410**.
  - **UI cards:** black **#0B0B0B**, 28–32 px corner radius, with yellow (#F5C400-ish) data accents.
- **Type:**
  - **Main face:** a tight neo-grotesk, Helvetica Neue / Neue Haas style, set with very tight tracking (about −0.04 to −0.05em).
    - Free match: **Inter Tight** (Regular/Medium) or Inter with negative tracking.
    - Mostly **Regular weight, sentence case**.
  - **Two-weight italic lock-up** for emphasis lines, in the same family's italics:
    - "*Nothing* **runs**": Nothing in bold italic, runs in light italic, gradient fill.
    - "*in* ***isolation.***"
    - "This *isn't* ***theory***": regular, then light italic, then bold italic.
  - **Wordmark:** "INDI" (white, nearly invisible on its white pill) plus "CREATIVE" in **bold caps**, a geometric grotesk (Montserrat Bold-like), yellow.
  - **Sizes at 1080 wide (estimated from frames):**

    | Use | Size |
    |---|---|
    | Hook lines ("Most Agencies", "Sell you … Ads.") | about 95–110 px |
    | Typed whip line "We build the" | about 200 px (camera zoomed in) |
    | Pill labels ("Ads", "Funnels", "Follow-up") | about 85–100 px |
    | "Connected" | about 150 px |
    | "Growth" typed close-up | about 230 px |
    | Payoff sentences: "Build to work as one.", "Growth isn't left to chance.", "We don't run your marketing.", "We build your empire" | **small, about 52–60 px**, centred |
    | Italic headers ("This isn't theory", "Nothing runs") | about 70–80 px |
  - **The signature contrast:** words arrive big, then the full sentence settles small and quiet in the middle of a lot of empty gradient.
- **Imagery and props:**
  - **Glassy 3D yellow icons** (soft, translucent, slightly frosted):
    - chat bubbles with three dots (hook);
    - play/rewind triangles (dashboard);
    - a magnifying glass (website);
    - a ring;
    - a row of white "••••" dots in a frosted pill.
  - **A black rounded app-icon tile** with a yellow megaphone, used as an inline word ("Sell you [icon] Ads.").
  - **Glass/chrome pills** (thick white rim, dark translucent fill, inner highlight; chromatic rainbow fringing during motion) and a **search-bar pill** (cream field, typed text with caret, black circular button with a yellow magnifier).
  - **Real proof assets:**
    - a dark analytics card ("Conversion Rate 27% ▲12.8%", yellow area-line chart, yellow mini bar chart, a "Track" yellow pill button);
    - real ad creatives in a 3D fan;
    - a website screenshot in a card;
    - case-study photo cards with bold result captions;
    - Meta Ads Manager result rows.
- **Persistent elements:** none (no logo bug, no watermark). Continuity comes from the two background worlds and the yellow accent.

## Scene-by-scene (times from 8 fps sheets; VO word times from vo_words.json)

| # | Time | VO words (times) | Background | What's on screen | Entrance / motion | Exit / transition |
|---|---|---|---|---|---|---|
| 1 | 0.00–0.70 | Most 0.00, agencies 0.28 | Light gradient | "Most Agencies" centred (about 100 px, gradient fill); glassy yellow chat bubbles drifting at the left edge and bottom right | Per word: blur 12→0 px plus opacity 0→1, about 0.25 s; "Agencies" 0.25 s after "Most". Slow drift; bubbles slide in from the edges | Line pushes left, then cut |
| 2 | 0.75–1.75 | sell 0.52, you 1.00, ads 1.14 | Light | "Sell you [megaphone tile] Ads." | "Sell you" enters from the right with horizontal motion blur (0.75), sharp by 0.875. The icon tile pops at 1.125 (scale about 0.6→1, grey→black). "Ads." blurs in at 1.125–1.25. The whole line drifts left about 15% over the hold | A text caret "\|" appears at the right edge (1.75) |
| 3 | 1.75–2.5 | We 1.94, build 2.00, the 2.28 | Light | Typed line "We build the\|" at about 200 px, larger than the frame | Fast whip left: the old line and the new typed text slide left with heavy horizontal motion blur, and the camera tracks along the typing (cropped "build t", "d the\|") | The dashboard card slides in from the right and pushes the text out (2.5) |
| 4 | 2.5–4.2 | system 2.44, behind 2.82, growth 3.38 | Light, with large glassy yellow triangles at the bottom right | Black analytics card: "Conversion Rate" count-up 0→27%, ▲12.8%, yellow area chart, yellow bar mini chart, "Track" pill | Card slides in from the right (about 0.4 s, ease-out). The counter rolls 2→5→7→11→15→19→22→25→27% from 2.6 to 3.75 (about 0.13 s per step). The card scales up about 1.5× and pans left (3.25–3.75). "Track" highlights at 4.0. The VO words are **not** captioned; the card illustrates them | Hard cut to black (4.25) |
| 5 | 4.25–5.0 | Ads 4.26 | Dark plus amber floor glow | Glass pill "Ads" (about 90 px white) with real ad creatives fanning out from behind it in 3D | Pill and cards emerge from a glow blur (4.375). Cards fly up and left in a tilted stack, rotating slightly; the pill rim gets a rainbow fringe | The camera pans right along an invisible line |
| 6 | 5.0–6.0 | funnels 4.98 | Dark | "Ads" pill exits left; "Funnels" glass pill centred; creatives keep drifting up and left | Horizontal track: pills sit on one baseline, spaced about 1 pill apart, and the camera slides right about 600 px per word, ease-in-out with motion blur | Continue pan |
| 7 | 6.0–6.7 | websites 5.86 | Dark | Search-bar pill "Websites\|" (cream field, black round button, yellow magnifier) | Text types in letter by letter; a **yellow fill wipes left→right** across the field (6.125–6.4), then fades back to cream | Continue pan; an empty glass pill arrives first (6.875) |
| 8 | 6.75–7.75 | follow 6.76, up 7.16 | Dark, faint curved light streak | "Follow-up" glass pill | Text fades and sharpens into the already-placed pill (7.0) | Zoom out (7.875) |
| 9 | 7.875–8.75 | Every 7.90, piece 8.14, connected 8.52 | Dark | All four pills small in one row (Ads, Funnels, Websites, Follow-up), with creatives stacked at the left | Camera pull-back about 2.5× in 0.15 s, then a slow drift. This is the "connected" reveal without captions | **Flash**: grey wash (8.75), then a bright white band (8.875), then the light world |
| 10 | 8.875–9.7 | (connected, held) | Light with white swoosh ribbons | "Connected" in a white pill with a yellow rim, about 150 px gradient text | A blurred white blob (9.0) blooms to the pill (9.125, small) and overshoots to full size (9.25), settling about 5% smaller by 9.5 | Cut |
| 11 | 9.75–11.25 | Built 9.92, to 10.14, work 10.38, as 10.60, one 10.82 | Light | "Build" (the on-screen spelling, not "Built") starts big (about 110 px), shrinks to about 55 px by 10.0, then "to / work / as / one." append word by word, line centred | Each new word blurs in about 0.15 s **before** its VO time. The line re-centres as it grows (it is not left-anchored). Brief double-image glitch on "Build to" at 10.375 | The line slides left with motion blur while the website card enters from the right (11.25) |
| 12 | 11.25–13.75 | Nothing 11.68, runs 12.00, in 12.38, isolation 12.56 | Light, glassy yellow ring top right, frosted "••••" pill bottom right | Website screenshot card (about 900 px wide, dark site) with a 3D yellow magnifier at its bottom-left corner; "*Nothing* runs" above the card's left edge, "in ***isolation.***" below its right edge | Card slides in from the right; the page inside **scrolls down** slowly (12.0–13.6). Header words fade up on their VO times; "in isolation." blurs in | Swing: the card rotates away in 3D with motion blur (13.75) |
| 13 | 13.875–15.55 | Nothing 13.70, left 14.08, to 14.46, guesswork 14.68 | Light | **3D card carousel** of case-study photo cards (thick black rim, result caption e.g. "OVER 150K OF QUOTES IN 2 WEEKS", "OVER 200 ADDITIONAL LEADS A MONTH / 200% INCREASE IN ROI…"). One VO word sits above each card | Cards swing in from the right on a cylinder (Y-rotation about 35°→0, heavy motion blur), one card per word, about 0.35 s each. Each word is pinned to its card and travels with it. "guesswork." holds 15.0–15.5 | Darken: frame dims to grey and the card scales and rises (15.625), then black |
| 14 | 15.75–18.1 | This 15.72, isn't 15.94, theory 16.26, This 17.16, is 17.30, what 17.42, happens 17.60, when 18.06 | Dark plus a faint yellow swoosh | **Drum of Ads Manager result rows** (Results / Cost per result / Budget / Amount spent): 6–7 strips stacked in perspective, the centre strip bright white and scaled up, the others greyer and smaller toward top and bottom. Header "This *isn't* ***theory***" about 75 px white | Rows **roll upward like a slot-machine drum** (the centre highlight passes from row to row about every 0.5 s). Header words blur up one per VO word while the header rises about 100 px (15.75→16.4). Push-in about 1.15× (17.6–17.9); "*Happens* when" in white italic fades in behind the bottom rows (17.75) | **Vertical whip**: everything slides up out of frame with motion blur (18.125–18.375) |
| 15 | 18.375–20.0 | growth 18.30, isn't 18.62, left 19.18, to 19.34, chance 19.50 | Dark, yellow light streak top right | Typed "G\|" → "Gro\|" → "Growth" at about 230 px white with soft glow; then the whole sentence "Growth isn't left to chance.\|" at about 55 px centred | Close-up typewriter with the camera tracking right (18.5–19.0). **Whip zoom-out** with horizontal blur (19.125–19.5) into the small full sentence; caret blinks | Grey dissolve to light (20.0–20.25) |
| 16 | 20.25–21.5 | Indie 20.36, creative 20.70 | Light | Logo: a frosted white pill with faint "INDI" and yellow bold caps "CREATIVE" | Pill blooms from blur (20.25–20.375). "CREATIVE" letters **drop in one by one with rotation and bounce** (C, CRE, CREAT… 20.5–21.0), the last letters landing tilted (about ±10°) and settling. Likely a sound hit here | Blur-fade out (21.5) |
| 17 | 21.625–23.1 | We 21.64, don't 21.80, run 22.06, your 22.24, marketing 22.36 | Light, white swoosh ribbon | "We dont run your marketing." (apostrophe missing on screen) about 55 px centred | Per word: blur-in that starts pale yellow and darkens to the gradient fill (about 0.3 s), timed to the VO. The line tightens slightly (tracking and scale) through the hold | Blur-out (23.25) |
| 18 | 23.375–24.77 | We 23.36, build 23.44, your 23.74, empire 23.92 | Light | Typed "W\|" → "We build\|" → "We build your" → "We build your em\|" → "We build your empire\|", about 55 px centred | Typewriter with caret, about 12 characters/s; a brief letter-doubling glitch at 23.5. The caret blinks on the end. **No end card**; the video stops 0.85 s after "empire" | End of file |

## Motion language
- **Two worlds, flipped for meaning:**
  - Light yellow is the brand/promise world: hook, "connected", thesis payoffs, logo, sign-off.
  - Black with amber glow is the machinery/proof world: the four services, the Ads Manager results, the thesis.
  - Flips happen on hard cuts (4.25), flash/white-band wipes (8.75), dim-to-black (15.6) or grey dissolves (20.1).
- **Three text engines, used for different jobs:**
  1. **Blur-in per word** on the VO (12→0 px blur, opacity 0→1, about 0.2–0.3 s, words 0–0.15 s ahead of speech). Used for calm statements.
  2. **Typewriter with a blinking caret "\|"**, about 12–15 characters per second, often with the camera zoomed in and tracking the typing. Used for thesis lines and the sign-off; it reads as "being written now".
  3. **Words as objects:** pills, search bars and inline icon tiles that carry one word each and move as physical things (pan, fan, carousel).
- **Big-to-small rhythm:** a word lands huge (150–230 px), then the full sentence resolves small (about 55 px) in a calm centre. Emphasis comes from scale change over time, not from colour.
- **Camera grammar:** horizontal whips and pans with strong motion blur (directional blur about 40–80 px during 0.12–0.2 s moves), quick zoom-outs to reveal a whole set, and a push-in before a whip. Moves are ease-in-out with very short peaks; nothing bounces except the logo letters and the "Connected" overshoot.
- **Proof grammar:** real numbers, counted up or rolling (the 0→27% counter, the Ads Manager drum, scrolling website, case-study captions). The VO speaks abstractly and the visuals carry the evidence; the VO is **not** fully captioned in proof scenes.
- **Glass and glow:** frosted 3D props, glass pills with a rainbow fringe in motion, soft outer glow on white type, amber floor glow, light-streak swooshes, white flash bands as transitions.
- **Life during holds:** the gradient blobs drift, props float (chat bubbles, triangles, ring), the website scrolls, the drum rolls, the caret blinks and cards slowly scale or pan. Nothing is ever fully static for more than about 0.3 s.
- **Average layout length about 1.2 s.** It is fast, but each idea gets one clear focal object.

## Recreate-it notes (HyperFrames)
- **Frame:** 1080x1920, 30 fps. Two background layers you can cross-fade:
  - **Light:** `#root.light { background: radial-gradient(60% 45% at 0% 0%, #FDCC00 0%, transparent 70%), radial-gradient(60% 45% at 100% 100%, #FDCC00 0%, transparent 70%), radial-gradient(80% 60% at 100% 0%, #FFFFF8 0%, transparent 70%), #FDF3C8; }`
    - Animate the gradient centres ±8% over 6–10 s, `sine.inOut`, yoyo, so it breathes.
    - Optional white ribbon: an SVG path, `stroke: rgba(255,255,255,.6)`, `filter: blur(6px)`, drifting.
  - **Dark:** `background: #000;` plus a floor glow div `bottom:-10%; height:35%; background: radial-gradient(70% 60% at 50% 100%, #D39301 0%, #A66900 35%, transparent 75%); filter: blur(40px)`.
    - Optional streak: a curved SVG path, `stroke:#F5C400; stroke-width:6; filter: blur(8px) drop-shadow(0 0 20px #F5C400); opacity:.6`.
- **Gradient text on light:** `background: linear-gradient(180deg, #0E0D08 35%, #A67A00 100%); -webkit-background-clip: text; color: transparent;`
  - Font: Inter Tight 400/500, `letter-spacing: -0.045em`.
  - Italic lock-up: Inter Tight Italic 300 plus Bold Italic 700.
  - White text on dark: `color:#fff; text-shadow: 0 0 24px rgba(255,255,255,.35)`.
- **Blur-in word:** at `t = wordStart − 0.1`, `fromTo(word, {opacity:0, filter:'blur(12px)', y:12}, {opacity:1, filter:'blur(0px)', y:0, duration:0.25, ease:'power2.out'})`.
  - Variant used in the sign-off: start `color` at `#F2C94C` and tween to the gradient by fading a gradient-filled duplicate in over 0.3 s.
- **Typewriter with caret:** reveal characters with a stepped tween, `gsap.to(el, {duration: chars/13, text: full, ease:'none'})`. Without the TextPlugin, animate a `clip-path: inset(0 X% 0 0)` with `steps(n)`.
  - Caret: a `::after` "\|" 0.06em wide, `opacity` toggled every 0.5 s with `repeat:-1`.
  - **Zoomed typing:** wrap the line in a group at `scale(3.5)` and tween its `x` so the caret stays about 70% across the frame, then `scale 3.5→1` over 0.35 s with `expo.inOut` and `filter: blur(0→10px→0)`.
- **Whip / pan with motion blur:** HyperFrames has no native motion blur. Fake it during the 0.15–0.2 s move:
  - stack 3–4 copies at 25–35% opacity offset along the move, or apply an SVG `feGaussianBlur stdDeviation="40 0"` (horizontal only) ramped 0→40→0;
  - `x` tween `power3.inOut`.
  - Vertical whip: same with `stdDeviation="0 40"`.
- **Pill track:** pills absolutely placed on one baseline, about 640 px apart.
  - The camera is a parent group: `to(track, {x: -640*i, duration: 0.35, ease:'power3.inOut'})` per VO word.
  - Glass pill: `border: 6px solid rgba(255,255,255,.85); background: rgba(30,30,30,.55); backdrop-filter: blur(8px); box-shadow: inset 0 2px 8px rgba(255,255,255,.4), 0 10px 40px rgba(0,0,0,.6); border-radius: 999px; padding: 18px 54px`.
  - Rainbow fringe: two offset copies tinted red and cyan at 30%, only during moves.
  - Final reveal: `to(track, {scale: 0.4, x: center, duration: 0.15, ease:'expo.out'})`.
- **Search-bar fill wipe:** inside the field, a `#FDCC00` div with `scaleX 0→1` (`transform-origin: left`) over 0.25 s, then `opacity 1→0` over 0.3 s.
- **Counter card:** a number tween with `snap: 1`, 1.2 s `power1.out`. The SVG area path draws with `stroke-dashoffset`, its fill fades in, and mini bars grow `scaleY 0→1` with a 0.04 s stagger. The card enters `x: 700→0`, 0.4 s `power3.out`, then a slow `scale 1→1.5` push.
- **3D carousel:** cards on a parent with `perspective: 1400px`. Each card enters `rotateY: 35, x: 500, filter: blur(10px)` → `rotateY: 0, x: 0, blur(0)` in 0.35 s, while the previous card goes to `rotateY: -35, x: -500`. The caption word is a child of the card.
- **Results drum:** 7 strips in a column on a parent with `perspective: 1200px`. Per strip, `rotateX = (i − active) × 18°`, `scale = 1 − |i − active| × 0.06`, `filter: brightness(1 − |i − active| × 0.18)`. Step `active` every 0.5 s with a 0.3 s `power2.inOut` tween.
- **Transitions:**
  - **Flash band:** a full-width white div 300 px tall, `filter: blur(30px)`, sweeping `y` across the frame over 0.15 s while the scene swaps under it.
  - **Dim-to-black:** `brightness 1→0.3` plus `scale 1→1.1` over 0.15 s, then cut.
  - **Grey dissolve:** cross-fade 0.2 s through `filter: saturate(0) brightness(.7)`.
- **Logo sting:** the wordmark pill blooms `scale .6→1, blur 20→0` in 0.15 s. The letters of the bold word drop from `y:-80, rotate: random(-25,25)` to `y:0, rotate: 0` with `back.out(2)`, stagger 0.06 s, but leave the last two letters landing at ±8° for character. Add a hit SFX on the first letter.
- **Kit rules when borrowing this:**
  - End on a held final line of at least 2 s plus a real end card (this reel cuts off 0.85 s after its last word).
  - Write conversational VO instead of fragments.
  - Never reuse the agency's assets, wordmark or copy. Borrow the two-world structure, the type engines and the camera grammar.
