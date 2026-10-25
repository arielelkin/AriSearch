"""Static, portable SVG gallery for a bounded discovery screen."""
from __future__ import annotations

from html import escape
from pathlib import Path
import math


def polygon_svg(polygon, label="", *, width=220, height=170):
    points = [(float(x), float(y)*math.sqrt(3)) for x, y in polygon]
    low_x = min(x for x, _ in points)
    low_y = min(y for _, y in points)
    span_x = max(x for x, _ in points)-low_x
    span_y = max(y for _, y in points)-low_y
    margin = 18
    scale = min((width-2*margin)/max(span_x, 1),
                (height-2*margin)/max(span_y, 1))
    coordinates = " ".join(f"{margin+(x-low_x)*scale:.5f},{height-margin-(y-low_y)*scale:.5f}"
                           for x, y in points)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
            f'role="img" aria-label="{escape(label)}"><polygon points="{coordinates}" '
            'fill="#b9dcd4" stroke="#163d39" stroke-width="2"/></svg>')


def write_gallery(result: dict, path: Path):
    singleton = {record["tile"]: record for record in result["singletons"]}
    tiles = result["catalogue"]
    survivor_ids = {tile["id"] for tile in tiles
                    if singleton[tile["id"]]["status"] not in
                    ("MONOHEDRAL_THEOREM", "PERIODIC_WITNESS")}
    cards = []
    for tile in tiles:
        record = singleton[tile["id"]]
        label = tile["id"]
        status = record["status"]
        survivor = label in survivor_ids
        cards.append('<article class="'+('survivor' if survivor else 'omitted')+'">'
                     + polygon_svg(tile["polygon"], label)
                     + f'<h2>{escape(label)}</h2><p>{len(tile["cells"])} kites · '
                     + f'{len(tile["polygon"])} sides</p><p>{escape(status)}</p>'
                     + (f'<p>{escape(record["reason"])}</p>' if "reason" in record else '')
                     + '<details><summary>Exact polygon</summary><pre>'
                     + escape(str(tile["polygon"]))+'</pre></details></article>')
    pair_rows = ''.join('<tr><td>'+escape(' + '.join(pair["tiles"]))+'</td><td>'
                        +escape(pair["status"])+'</td></tr>' for pair in result["pairs"])
    funnel = ', '.join(f'{key}: {value}' for key, value in result["funnel"].items())
    content = '''<!doctype html><html lang="en"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Polykite discovery pilot</title><style>
body{font:16px system-ui,sans-serif;max-width:1280px;margin:2rem auto;padding:0 1rem;color:#17322f;background:#f7faf9}
h1{font-size:2rem}.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:1rem}
article{background:white;border:1px solid #c7d6d2;border-radius:8px;padding:1rem;overflow-wrap:anywhere}
article.survivor{border:3px solid #b46a1b}svg{width:100%;height:170px}h2{margin:.2rem 0}p{font-size:.9rem}
pre{white-space:pre-wrap;font-size:.75rem}table{border-collapse:collapse}td,th{padding:.5rem;border:1px solid #c7d6d2;text-align:left}
</style><h1>Polykite discovery pilot</h1>'''
    content += '<p>'+escape(result["scope"])+ '</p><p>'+escape(funnel)+'</p>'
    content += '<p>Orange borders mark unresolved singleton shapes. All catalogue shapes appear below; omitted shapes have positive monohedral evidence. Exact coordinates use (x, y√3).</p>'
    content += '<p>Catalogue SHA-256: <code>'+escape(result["catalogue_sha256"])+'</code></p>'
    content += '<div class="grid">'+''.join(cards)+'</div>'
    content += '<h2>Remaining unordered pairs</h2>'
    content += ('<table><tr><th>Pair</th><th>Bounded result</th></tr>'+pair_rows+'</table>'
                if pair_rows else '<p>No pairs remain after the positive singleton omissions.</p>')
    content += '<p>Machine-readable placements, budgets, versions, hashes, and every attempted HNF domain are in <a href="screen.json">screen.json</a>.</p></html>'
    Path(path).write_text(content)

