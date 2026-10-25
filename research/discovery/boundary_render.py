"""Portable static gallery of the native boundary-word screening experiment."""
from html import escape
import json
import math
from pathlib import Path


def polygons_svg(placements, width=500, height=360, period_vectors=None):
    points = [(x, y*math.sqrt(3)) for placement in placements for x, y in placement["polygon"]]
    if not points:
        return ""
    xmin, xmax = min(p[0] for p in points), max(p[0] for p in points)
    ymin, ymax = min(p[1] for p in points), max(p[1] for p in points)
    scale = min((width-24)/max(xmax-xmin, 1), (height-24)/max(ymax-ymin, 1))
    ids = sorted({p["tile"] for p in placements})
    colors = ["#bcded4", "#edc08a", "#a7bcdf"]
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-label="Exact developed tile patch">']
    for placement in placements:
        coordinates = " ".join(f'{12+(x-xmin)*scale:.5f},{height-12-(y*math.sqrt(3)-ymin)*scale:.5f}'
                               for x, y in placement["polygon"])
        color = colors[ids.index(placement["tile"]) % len(colors)]
        parts.append(f'<polygon points="{coordinates}" fill="{color}" stroke="#183b36" stroke-width="1"/>')
    if period_vectors is not None:
        u, v = period_vectors
        cell = [(0, 0), u, (u[0]+v[0], u[1]+v[1]), v]
        coordinates = " ".join(f'{12+(x-xmin)*scale:.5f},{height-12-(y*math.sqrt(3)-ymin)*scale:.5f}' for x, y in cell)
        parts.append(f'<polygon points="{coordinates}" fill="none" stroke="#8c2446" stroke-width="2.5" stroke-dasharray="7 4"/>')
    return ''.join(parts)+'</svg>'


def periodic_svg(witness):
    u, v = witness["period_vectors"]
    copies = []
    for m in (-1, 0, 1):
        for n in (-1, 0, 1):
            for placement in witness["placements"]:
                copies.append({"tile": placement["tile"],
                               "polygon": [(x+m*u[0]+n*v[0], y+m*u[1]+n*v[1])
                                           for x, y in placement["polygon"]]})
    return polygons_svg(copies, period_vectors=witness["period_vectors"])


def write_gallery(result, path):
    content = '''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Native hexagon screening</title><style>
body{font:16px system-ui,sans-serif;color:#17332e;background:#f6faf8;max-width:1320px;padding:1.5rem;margin:auto}h1{font-size:2rem}svg{width:100%;max-height:360px}article{background:white;border:1px solid #bed0c9;border-radius:8px;padding:1rem;overflow-wrap:anywhere}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:1rem}pre{white-space:pre-wrap;font-size:.75rem}table{border-collapse:collapse;width:100%}td,th{border:1px solid #bdcfc8;padding:.4rem;text-align:left}summary{cursor:pointer}a{color:#225e50}</style><h1>Native boundary-length hexagon experiment</h1>'''
    content += '<p>'+escape(result["scope"])+'</p>'
    content += '<p>All six angles are 120°. This family overlaps earlier repository experiments; no novelty claim is made. Every native length uses one shared scale.</p>'
    content += '<p>Screen bounds: HNF index ≤ '+str(result["budgets"]["max_index"])+', symbolic disk radii '+escape(str(result["budgets"]["radii"]))+'.</p>'
    content += '<pre>'+escape(str(result["funnel"]))+'</pre>'
    survivors = [pair for pair in result["pairs"] if pair["status"] in ("SURVIVES_BOUNDED_SCREENS", "UNKNOWN")]
    content += f'<h2>Strongest retained patches · {len(survivors)} unresolved pairs</h2><div class="grid">'
    for pair in survivors:
        title = ' + '.join(pair["tiles"])
        content += '<article><h3>'+escape(title)+'</h3><p>'+escape(pair["status"])+'</p>'
        witnesses = [record for record in pair.get("growth", []) if "witness" in record]
        for record in witnesses:
            content += f'<p>Seed {escape(record["seed_tile"])} · symbolic radius {record["symbolic_radius"]}</p>'
            content += polygons_svg(record["witness"]["placements"])
        content += '<p>These finite patches do not establish infinite tileability or aperiodicity.</p></article>'
    content += '</div>'
    periodic = [pair for pair in result["pairs"] if pair["status"] == "PERIODIC_WITNESS"]
    content += '<h2>Periodic witnesses</h2><details'+(' open' if len(periodic) <= 4 else '')+'><summary>'+str(len(periodic))+' positive periodic constructions</summary><p>Each picture repeats the exact representative tiles over nine period cells. The dashed red outline is one period parallelogram. Every tile in a picture uses the same coordinate scale.</p><div class="grid">'
    for pair in periodic:
        witness = pair["periodic"]["witness"]
        content += '<article><h3>'+escape(' + '.join(pair["tiles"]))+'</h3><p>HNF '+escape(str(witness["domain_hnf"]))+' · exact periods '+escape(str(witness["period_vectors"]))+'</p>'
        content += periodic_svg(witness)
        content += '<details><summary>Exact representative placements</summary><pre>'+escape(json.dumps(witness["placements"], sort_keys=True, indent=2))+'</pre></details></article>'
    content += '</div></details><h2>Pair status table</h2><details><summary>All bounded pair outcomes</summary><table><tr><th>Pair</th><th>Status</th></tr>'
    content += ''.join('<tr><td>'+escape(' + '.join(pair["tiles"]))+'</td><td>'+escape(pair["status"])+'</td></tr>' for pair in result["pairs"])
    content += '</table></details><h2>Noncentral shape library</h2><div class="grid">'
    for tile in result["catalogue"]:
        if not tile["centrally_symmetric"]:
            content += '<article><h3>'+escape(tile["id"])+'</h3>'
            content += polygons_svg([{"tile": tile["id"], "polygon": tile["polygon"]}], 320, 190)
            content += '<p>Native word '+escape(str(tile["word"]))+'</p></article>'
    content += '</div><p>Exact polygons, full attempts, source hashes, deterministic budgets, and retained witnesses: <a href="boundary-screen.json">boundary-screen.json</a>.</p>'
    content += '<p>Result SHA-256: <code>'+escape(result["result_sha256"])+'</code></p></html>'
    Path(path).write_text(content)
