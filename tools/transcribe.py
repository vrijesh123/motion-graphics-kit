"""Word-timestamped Whisper transcript of any audio or video file.

Use it on a voice-over to get the cue times every caption and scene change is built on, or on a reference reel.
usage:
    python tools/transcribe.py <media>                       # print segments with word@time
    python tools/transcribe.py <media> --json vo_words.json  # also write [{"w", "s", "e"}, ...] (seconds, file time)
Options: --model small|medium (default small), --lang en (default: auto-detect).
Needs: ffmpeg on PATH, pip install numpy faster-whisper. Runs on CPU; the model downloads on first use.
Whisper often mishears brand names: check them by ear and fix the JSON by hand if needed.
"""
import argparse
import json
import subprocess
import sys

import numpy as np
from faster_whisper import WhisperModel

sys.stdout.reconfigure(encoding="utf-8")
ap = argparse.ArgumentParser()
ap.add_argument("media")
ap.add_argument("--json", help="write word list here")
ap.add_argument("--model", default="small")
ap.add_argument("--lang", default=None)
a = ap.parse_args()

x = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", a.media, "-ac", "1", "-ar", "16000", "-f", "f32le", "-"],
                                 capture_output=True, check=True).stdout, np.float32)
m = WhisperModel(a.model, device="cpu", compute_type="int8")
segs, info = m.transcribe(x, word_timestamps=True, beam_size=5, language=a.lang)
print("lang", info.language, round(info.language_probability, 2))
words = []
for s in segs:
    print(f"{s.start:.2f}-{s.end:.2f} nsp={s.no_speech_prob:.2f} :: " + " ".join(f"{w.word.strip()}@{w.start:.2f}" for w in s.words))
    words += [{"w": w.word.strip(), "s": round(w.start, 2), "e": round(w.end, 2)} for w in s.words]
if a.json:
    with open(a.json, "w", encoding="utf-8") as f:
        json.dump(words, f, indent=1, ensure_ascii=False)
    print(f"wrote {a.json} ({len(words)} words)")
