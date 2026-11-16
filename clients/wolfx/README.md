# WOLFx Digital Agency: client pack

Everything needed to make on-brand WOLFx videos on this branch. Read this file first, then `brand.md` (look,
type, logo, voice) and `profile.md` (facts for scripts). Every fact is cited in `sources.md`.
Researched 2026-11-16 from wolfx.io and public listings. **Not yet confirmed by WOLFx.**

## At a glance
| | |
|---|---|
| Name | **WOLFx** (capital WOLF, lower-case x). Legal name WOLFx Digital Agency LLP |
| What they do | A Mumbai technology company that designs and builds websites, apps, e-commerce, AI, cloud and blockchain products, and runs digital marketing. They sell as a long-term tech partner |
| Their line | "A Creative Technology Company. Everything Technology is our Playground." |
| Where | Mumbai, India; on-site and remote; clients in India and the Middle East |
| Founded | 2019, by Ruchit Kharwa and Vrijesh Rathod; team of 10-49 |
| Website | wolfx.io |
| Look | White, near-black `#121212`, one red accent `#FF2B2B`; Poppins; tall condensed wordmark; faint grid, hairlines, grey contour lines; square corners |
| Default end card | Wordmark, "Let's make something great together.", `wolfx.io` |
| Best-fit references | MotionDesigners (punchy promos), InsiderForce (calm explainers); see `brand.md` |

## Confirm with WOLFx before the first video
1. **Logo as SVG** (wordmark and "Wx" monogram). Only a 213×110 web PNG exists. The 699 px black/white versions
   here are extracted from their social banner as a stopgap.
2. **Which numbers to show.** The Work page says 100+ projects and 50+ clients; TechBehemoths says 50+ projects
   in 6+ years.
3. **Naming clients on screen:** Cross, Quick SO, Weekend Fables, Interiors and More, Mahindra Armored, Indian
   Navy. Can we name them and quote their results and testimonials? For the Indian Navy, what may be said at all?
4. **Contact line for end cards.** The site shows none, and listings give two different phone numbers (see
   `sources.md`).
5. **Captions:** sentence case (kit default) or Title Case (their site headings)?
6. **Voice-over:** how to say "WOLFx" (we assume "Wolf-ex"), which voice and accent, and who records it.
7. **Wordmark typeface name**, if they want condensed headlines to echo it.

## Files
- `brand.md`: palette as the template's `:root` tokens, Poppins `@font-face` block, logo rules, motifs, motion
  direction, voice and wording, end card.
- `profile.md`: positioning, services, engagement models, process, values, case studies with verified numbers,
  testimonials, Cerberus, audience, video angles.
- `sources.md`: 14 sources with URLs, plus what was found but not verified and what was left out.
- `assets/logo/`: interim black and white wordmarks, the site's own logo file and the "Wx" monogram.
- `assets/fonts/`: Poppins 400-800 (SIL OFL 1.1).
- `assets/reference/`: WOLFx's social banner and a homepage screenshot, for look only.

## Starting a WOLFx video
```bash
cp -r projects/_template projects/wolfx-<video>
cp clients/wolfx/assets/fonts/* projects/wolfx-<video>/assets/fonts/
cp clients/wolfx/assets/logo/wolfx-wordmark-*-interim.png projects/wolfx-<video>/assets/
```
In the project's `index.html`:
1. Replace the `:root` line and the two template `@font-face` lines with the blocks from `brand.md`.
2. Set `#root` to Poppins.
3. Drop the italic-serif `.key` style. If it stays, `npm run check` fails with "font family used without
   @font-face".
4. On the end card, replace the `LOGO` tile and the `.brand` text with the wordmark `<img>`. Also delete
   `"#end .brand"` from the script's `splitChars` list and its `warp(...)` line, or the page throws an error.

These steps were tested on 2026-11-16: the template with this pack passed `npm run check` with 0 errors.

Then follow `make-motion-video`: the script comes first, for approval.

## Decisions and feedback (newest last)
- 2026-11-16: pack created from public sources; waiting on the confirmations above.
