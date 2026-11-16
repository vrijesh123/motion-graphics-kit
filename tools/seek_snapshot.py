"""Screenshot a HyperFrames index.html at given times WITHOUT the HyperFrames CLI (headless Chrome + a seek harness).

Prefer `npx hyperframes snapshot --at 1,3,5` inside the project. Use this only when Node 22 / the CLI is not available.
usage: python tools/seek_snapshot.py <project_dir> <out_dir> t1 t2 ...
It hides clips outside their data-start/data-duration window and calls __timelines.main.seek(t).
JS onUpdate counters may not refresh. Set CHROME=<path> if Chrome/Chromium is not found automatically.
"""
import os
import pathlib
import shutil
import subprocess
import sys


def find_chrome():
    if os.environ.get("CHROME"):
        return os.environ["CHROME"]
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome"):
        if shutil.which(name):
            return shutil.which(name)
    for p in (r"C:\Program Files\Google\Chrome\Application\chrome.exe",
              r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
              os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
              "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"):
        if os.path.exists(p):
            return p
    sys.exit("Chrome not found: set CHROME=<path to chrome>")


proj = pathlib.Path(sys.argv[1]).resolve()
out = pathlib.Path(sys.argv[2]).resolve()
out.mkdir(parents=True, exist_ok=True)
times = sys.argv[3:]
chrome = find_chrome()
src = (proj / "index.html").read_text(encoding="utf-8")
base = '<base href="' + proj.as_uri() + '/">'
for t in times:
    hook = """<script>
document.fonts.ready.then(() => { const t = %s;
  document.querySelectorAll('.clip[data-start]').forEach(el => { const s = +el.dataset.start, d = +el.dataset.duration;
    el.style.visibility = (t >= s && t < s + d) ? 'visible' : 'hidden'; });
  window.__timelines.main.seek(t); });
</script>""" % t
    html = src.replace("<head>", "<head>" + base, 1).replace("</body>", hook + "</body>")
    h = out / f"h_{t}.html"
    h.write_text(html, encoding="utf-8")
    png = out / f"s_{t}.png"
    subprocess.run([chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--allow-file-access-from-files",
                    "--window-size=1080,1920", "--virtual-time-budget=6000", f"--screenshot={png}", h.as_uri()],
                   capture_output=True, timeout=90)
    h.unlink()
    print(t, png if png.exists() else "FAILED")
