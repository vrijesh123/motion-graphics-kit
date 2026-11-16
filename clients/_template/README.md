# <Client name>: client pack

Everything needed to make on-brand videos for <Client name> on this branch. Read this file first, then
`brand.md` (look, type, logo, voice) and `profile.md` (facts to write scripts from). Every fact is cited in
`sources.md`. Pack researched <YYYY-MM-DD>; <confirmed by the client on ... / not yet confirmed by the client>.

## At a glance
| | |
|---|---|
| Name | <exact spelling and casing, e.g. how captions must write it> |
| What they do | <one sentence> |
| Where | <city, country; markets served> |
| Website | <domain> |
| Look | <one line: background, ink, accent, type, signature motif> |
| Default end card | <logo, closing line, website; contact only once confirmed> |

## Confirm with the client before the first video
1. <logo as SVG, if missing>
2. <numbers you would put on screen, with the conflicting sources>
3. <permission to name their clients or show their work>
4. <contact line for the end card>
5. <voice-over: voice, accent, who records it>

## Files
- `brand.md`: palette (as the template's `:root` tokens), fonts (`@font-face` block), logo rules, graphic motifs,
  motion direction, voice and wording.
- `profile.md`: positioning, services, process, proof points, audience, video angles.
- `sources.md`: every source with its URL and retrieval date, plus what was found but not verified.
- `assets/logo/`, `assets/fonts/` (with licence), `assets/reference/` (the client's own brand images, for look only).

## Starting a video for this client
```bash
cp -r projects/_template projects/<slug>-<video>
cp clients/<slug>/assets/fonts/* projects/<slug>-<video>/assets/fonts/
cp clients/<slug>/assets/logo/<logo file> projects/<slug>-<video>/assets/
```
Then paste the `:root` palette and the `@font-face` block from `brand.md` into the project's `index.html`, and
follow the `make-motion-video` skill.

## Decisions and feedback (newest last)
- <YYYY-MM-DD>: pack created from public sources.
