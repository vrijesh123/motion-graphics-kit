# Clients: one branch each

`main` holds the kit only: tools, skills, the project template and the reference library. Every client gets
its own git branch, cut from `main` and named after the client's slug (lower case, no spaces): `wolfx`, `acme`...

On a client branch:

| Path | What |
|---|---|
| `clients/<slug>/` | The client pack: who they are, how they look and sound, and their logo and fonts. Read `README.md` first. |
| `projects/<slug>-<video>/` | One folder per video, copied from `projects/_template/` (as everywhere in the kit). |
| `outputs/<slug>-<video>-v1-<len>s.mp4` | Renders (git-ignored, as everywhere in the kit). |

`clients/_template/` is the blank pack. `main` has no filled-in pack: client facts never land on `main`.

## Start a new client
```bash
git switch main && git pull                   # start from the latest kit
git switch -c <slug>                          # the client's branch
cp -r clients/_template clients/<slug>
```
Then ask Claude: "Research <client> (<website>) and fill in `clients/<slug>/`." It fills the pack from the
website and public listings, cites every fact in `sources.md`, and lists what the client must confirm.

## Keep the branches clean
- **On a client branch, change only `clients/<slug>/` and `projects/<slug>-*/`.** Then merging the kit in is
  always conflict-free.
- **Kit changes go to `main`** (tools, skills, `projects/_template/`, references, docs). Bring them into a client
  branch with `git switch <slug> && git merge main`.
- If you fix something in the kit while working on a client branch, commit that fix on its own and
  `git cherry-pick` it onto `main`.
- **Never merge a client branch into `main` or into another client's branch.** That would mix client
  material into the kit, or one client's material into another's.
- **This repository is public.** Pushing a client branch to it publishes that client's pack and scripts.
  Keep client branches local, or push them to a private remote (`git remote add private <url>`,
  `git push private <slug>`), unless the client agrees to it being public.
