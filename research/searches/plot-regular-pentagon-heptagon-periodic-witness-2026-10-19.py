"""Render the exact retained four-face periodic certificate as a diagnostic SVG."""
import json
from pathlib import Path

from sympy import I, exp, pi, sympify

ROOT = Path('research/searches/regular-pentagon-heptagon-minimal-torus-sol-2026-10-19.json')
OUT = Path('research/figures/regular-pentagon-heptagon-periodic-witness-2026-10-19.svg')
data = json.loads(ROOT.read_text())['verification']
w = exp(I*pi/10)

def point(expr):
    z = complex(sympify(expr, locals={'zeta20': w}).evalf(20))
    return z.real, z.imag

base = [[point(v) for v in poly] for poly in data['polygons']]
l1, l2 = [point(x) for x in data['lattice']]
faces = []
for a in range(-1, 2):
    for b in range(-1, 2):
        for kind, poly in enumerate(base):
            faces.append((kind, [(x+a*l1[0]+b*l2[0], y+a*l1[1]+b*l2[1]) for x,y in poly]))
xs = [x for _,p in faces for x,_ in p]
ys = [y for _,p in faces for _,y in p]
pad = 0.35
xmin,xmax = min(xs)-pad,max(xs)+pad
ymin,ymax = min(ys)-pad,max(ys)+pad
scale = 65
width,height = scale*(xmax-xmin),scale*(ymax-ymin)
def loc(z):
    return f'{scale*(z[0]-xmin):.3f},{scale*(ymax-z[1]):.3f}'
colors = ['#e7b44e','#f2d186','#4d9eaa','#80bbc2']
parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width:.0f}" height="{height:.0f}" viewBox="0 0 {width:.3f} {height:.3f}">',
         '<rect width="100%" height="100%" fill="#faf8f1"/>']
for kind, poly in faces:
    parts.append(f'<polygon points="{" ".join(map(loc,poly))}" fill="{colors[kind]}" stroke="#25323a" stroke-width="1.25"/>')
par = [(0,0),l1,(l1[0]+l2[0],l1[1]+l2[1]),l2]
parts.append(f'<polygon points="{" ".join(map(loc,par))}" fill="none" stroke="#b9443a" stroke-width="2.4" stroke-dasharray="6 4"/>')
parts.append('</svg>')
OUT.parent.mkdir(parents=True,exist_ok=True)
OUT.write_text('\n'.join(parts)+'\n')
print(OUT)

from matplotlib import pyplot as plt
from matplotlib.patches import Polygon
fig, ax = plt.subplots(figsize=(10, 7))
for kind, poly in faces:
    ax.add_patch(Polygon(poly, closed=True, facecolor=colors[kind], edgecolor='#25323a', linewidth=0.7))
ax.add_patch(Polygon(par, closed=True, fill=False, edgecolor='#b9443a', linewidth=1.5, linestyle='--'))
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)
ax.set_aspect('equal')
ax.axis('off')
fig.savefig(OUT.with_suffix('.png'), dpi=160, bbox_inches='tight', pad_inches=0.03)
plt.close(fig)
