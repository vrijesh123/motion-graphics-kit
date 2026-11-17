# Quantiphi: client pack

Everything needed to make on-brand videos for Quantiphi on this branch. Read this file first, then
`brand.md` (look, type, logo, voice) and `profile.md` (facts to write scripts from). Every fact is cited in
`sources.md`. Pack researched 2026-11-17; not yet confirmed by the client.

## At a glance
| | |
|---|---|
| Name | **Quantiphi** (capital Q in all text; the lower-case "quantiphi" wordmark is artwork only) |
| What they do | AI-native services company that builds enterprise AI platforms inside the client's own cloud, so the client owns its data, models and IP |
| Where | HQ Marlborough, Massachusetts; offices in the US, Canada and India, plus London, Amsterdam and Singapore; founded 2013 |
| Website | quantiphi.com |
| Look | Deep navy radial-gradient night background, white Poppins headline with one bright green line (`#48DD84`), green growth curves, glass cubes, and a 3×3 navy/green/white grid logo |
| Campaign line | "Own Your Enterprise Intelligence. Compound Your Edge." |
| Default end card | Logo with "Solving What Matters", the line "Own your enterprise intelligence.", and quantiphi.com. Contact details only once confirmed |

## Confirm with the client before the first video
1. **Brand guidelines.** None are public. Ask for:
   - the official palette;
   - a wordmark without the "Solving What Matters" tagline;
   - permission to animate the 3×3 grid square by square (`brand.md`, "Logo");
   - whether "Solving What Matters" is still the current tagline.
2. **Numbers we would put on screen.** All are from their own site but need approval and the current figure:
   - up to 55% lower operational costs, up to 70% time freed, up to 3.5x faster retrieval;
   - 60-80% lower AI operating cost, 3-month delivery, 40-50% automation;
   - 4,500+ projects, 21 Google Cloud Partner of the Year awards, 86 patents filed.
   - Headcount: third-party figures conflict (about 1,500 to 4,500) and Quantiphi publishes none. Ask for the
     number they want used.
3. **Description.** Is it "AI-native services partner" (2026 pages) or "AI-first digital engineering company"
   (older releases)?
4. **Permissions:**
   - naming customers and using testimonials (only one is public in full);
   - showing partner and analyst logos (Google Cloud, AWS, NVIDIA, Gartner, ISG...).
5. **Casing.** Their headlines are Title Case; the kit default is sentence case for captions.
6. **Voice-over.** Who records it, which voice and accent, and the pronunciation of "Quantiphi" ("kwon-TIF-ee" is
   unverified), "baioniq", "Dociphi", "Codeaira" and "Qollective.CX".
7. **End-card contact line.** info@quantiphi.com and +1 508-661-9050 are public, but confirm before use.
8. **Dark or light.** Which is the default for social videos? The pack assumes dark, matching the homepage.

## Files
- `brand.md`:
  - palette as the template's `:root` tokens (dark default and light alternative), with the hero gradient;
  - Poppins `@font-face` block;
  - logo rules;
  - graphic motifs (equation, growth curve, glass cubes, grid);
  - motion direction;
  - voice and wording, Whisper fixes, end card.
- `profile.md`:
  - positioning and services (AI, data, cloud and four products);
  - the 5-pillar approach and proof points (all **confirm**);
  - industries, people, video angles, presence.
- `sources.md`:
  - 29 sources with URLs, retrieved 2026-11-17;
  - conflicts and unverified items;
  - what was left out.
- `assets/logo/`:
  - `quantiphi-logo-on-dark.svg`, `quantiphi-logo-on-light.svg` and `quantiphi-logo-white-tagline.svg`, the client's
    own files, unaltered;
  - `quantiphi-mark-grid.svg`, the 3×3 symbol alone, cut from the logo file, with ids per square.
- `assets/fonts/`: Poppins 400-800 (TTF) with `OFL.txt` and `FONTS.md`.
- `assets/reference/quantiphi-site-hero.png`: their homepage hero (2026-11-17). For look only; never used in a video.

## Starting a video for this client
```bash
cp -r projects/_template projects/quantiphi-<video>
cp clients/quantiphi/assets/fonts/*.ttf projects/quantiphi-<video>/assets/fonts/
cp clients/quantiphi/assets/logo/quantiphi-logo-on-dark.svg clients/quantiphi/assets/logo/quantiphi-mark-grid.svg projects/quantiphi-<video>/assets/
```
Then:
1. Paste the `:root` palette, the hero gradient and the `@font-face` block from `brand.md` into the project's
   `index.html`.
2. Drop the template's serif `.key` style.
3. Follow the `make-motion-video` skill.

## Decisions and feedback (newest last)
- 2026-11-17: pack created from public sources (quantiphi.com, press releases, product sites and third-party listings). Dark palette chosen as default to match the live homepage; not yet reviewed by Quantiphi.
