"""Write index.html from assets/layers/manifest.json (run once after extract_layers.py; then edit index.html by hand).

usage: python build/make_index.py   (from the project folder)
Every layer becomes an <img> at its poster position inside #poster (1080x1920 poster coordinates).
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
M = json.loads((HERE / "assets/layers/manifest.json").read_text())


def img(name, cls="", extra=""):
    b = M[name]
    return (f'<img id="{name.replace("_", "-")}" class="ly {cls}" src="assets/layers/{name}.png" alt="" '
            f'style="left:{b["x"]}px; top:{b["y"]}px; width:{b["w"]}px; height:{b["h"]}px"{extra} />')


def piece(key):
    b = M[f"pz_{key}_photo"]
    box = f'left:{b["x"]}px; top:{b["y"]}px; width:{b["w"]}px; height:{b["h"]}px'
    return (f'<div id="pz-{key}" class="pz" style="{box}" data-layout-allow-overflow data-layout-allow-overlap>\n'
            f'          <div class="pzm" style="-webkit-mask-image:url(assets/layers/pz_{key}_mask.png); mask-image:url(assets/layers/pz_{key}_mask.png)">'
            f'<img class="pzp" src="assets/layers/pz_{key}_photo.png" alt="" /></div>\n'
            f'          <img class="pzf" src="assets/layers/pz_{key}_frame.png" alt="" />\n        </div>')


letters = sorted([k for k in M if k.startswith("h_admissions")], key=lambda k: int(k.rsplit("_", 1)[1])) + \
          sorted([k for k in M if k.startswith("h_open")], key=lambda k: int(k.rsplit("_", 1)[1]))
tags = sorted([k for k in M if k.startswith("tag_")], key=lambda k: int(k.split("_")[1]))
L = "\n        ".join

body = f"""
        <!-- headline: yellow brush + letters (cut from the poster) -->
        {img("head_brush", "wipe")}
        {L(img(k, "hl adm") for k in letters if "admissions" in k)}
        <div id="open-line" class="grp">
        {L(img(k, "hl opn") for k in letters if "open" in k)}
        </div>
        {img("tk_head_l", "tk tkl")}
        {img("tk_head_r", "tk tkr")}
        <!-- everything below the headline moves down by LINE_GAP + HEAD_MARGIN -->
        <div id="below" class="grp">
        <!-- year ribbon -->
        {img("ribbon")}
        {img("year")}
        {img("tk_year_l", "tk tkl")}
        {img("tk_year_r", "tk tkr")}
        <!-- puzzle: photo masked to the piece, white frame on top -->
        <div id="puzzle">
        {piece("tl")}
        {piece("tr")}
        {piece("bl")}
        {piece("br")}
        </div>
        <!-- date -->
        {img("date_brush", "wipe")}
        {img("d_21st")}
        {img("d_november")}
        {img("date_line", "wipe")}
        {img("tk_date_l", "tk tkl")}
        {img("tk_date_r", "tk tkr")}
        <!-- tagline, one image per word, and the url as live text (2026-11-17: no pill, green bold) -->
        {L(img(k, "tw") for k in tags)}
        <div id="url" class="ly">greenlawns.org</div>
        </div>
        <!-- school crest (client file) -->
        <img id="logo" class="ly" src="assets/greenlawns-crest.png" alt="Greenlawns crest" style="left:46px; top:52px; width:133px; height:132px" />"""

tpl = (HERE / "build/index.tpl.html").read_text()
(HERE / "index.html").write_text(tpl.replace("<!--LAYERS-->", body.strip("\n")))
print("index.html written")
