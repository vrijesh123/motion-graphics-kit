"""Turn a Whisper word list into caption <span>s with data-t cue times, ready to paste into index.html.

usage: python tools/caption_spans.py <vo_words.json> [--offset 0.2] [--gap 0.35]
  --offset  where the voice-over starts in the video (same as "vo_offset" in cues.json); added to every time
  --gap     a pause longer than this starts a new phrase (new line in the output); so does a sentence end
  --max-words  start a new phrase after this many words (default 12) when the voice never pauses
Each phrase prints with its start/end time, so you can also read off where scene changes belong
(scene changes go in the pauses between phrases). Split each phrase into a lead-in line and a key line by hand.
"""
import argparse
import html
import json

ap = argparse.ArgumentParser()
ap.add_argument("words")
ap.add_argument("--offset", type=float, default=0.2)
ap.add_argument("--gap", type=float, default=0.35)
ap.add_argument("--max-words", type=int, default=12)
a = ap.parse_args()

words = json.load(open(a.words, encoding="utf-8"))
if isinstance(words, dict):  # older files: {"model": ..., "words": [{"w", "start", "end"}]}
    words = words["words"]
words = [{"w": w["w"], "s": w.get("s", w.get("start")), "e": w.get("e", w.get("end"))} for w in words]
phrases, cur = [], []
for i, w in enumerate(words):
    if cur and (w["s"] - words[i - 1]["e"] > a.gap or words[i - 1]["w"].endswith((".", "?", "!")) or len(cur) >= a.max_words):
        phrases.append(cur)
        cur = []
    cur.append(w)
if cur:
    phrases.append(cur)

for p in phrases:
    s, e = p[0]["s"] + a.offset, p[-1]["e"] + a.offset
    print(f"<!-- {s:.2f}-{e:.2f}  \"{' '.join(w['w'] for w in p)}\" -->")
    spans = []
    for j, w in enumerate(p):
        txt = html.escape(w["w"], quote=False) + (" " if j < len(p) - 1 else "")
        spans.append(f'<span class="w" data-t="{w["s"] + a.offset:.2f}">{txt}</span>')
    print("".join(spans))
    print()
