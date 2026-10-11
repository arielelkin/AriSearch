"""Independent certificate audit using vertex-link graphs, not union-find."""
from pathlib import Path
from itertools import combinations_with_replacement as multisets
from fractions import Fraction as F
from collections import Counter
import json
root=Path(__file__).resolve().parents[2]
c=json.loads((root/'research/certificates/new-angle-two-equilateral-hexagons-certificate.json').read_text())
assert c['status']=='PASS'
coefs=[(1,0),(-1,0),(0,1),(0,-1)]
rows=[]
for t in multisets(range(4),3):
    a=sum(coefs[i][0] for i in t);b=sum(coefs[i][1] for i in t)
    ratio=F(-a,b) if b else None
    if ratio is not None and ratio<=0:ratio=None
    rows.append({'corners':list(t),'a_coefficient':a,'b_coefficient':b,'positive_b_over_a':str(ratio) if ratio else None})
assert rows==c['triangle_symbolic_rows']
assert sorted({r['positive_b_over_a'] for r in rows if r['positive_b_over_a']})==c['positive_triangle_parameter_ratios']==['1/2','2']
symbols=[(120,1),(120,-1),(60,0),(108,0),(168,0)];starrows=[]
for t in multisets(range(5),3):
    if 4 not in t:continue
    base=sum(symbols[i][0] for i in t);slope=sum(symbols[i][1] for i in t)
    if slope:
        a=F(360-base,slope)
        if 0<a<60:starrows.append({'a':str(a),'corners':list(t)})
assert sorted(starrows,key=lambda t:(F(t['a']),t['corners']))==c['sporadic_168_parameter_rows']
assert [q['a'] for q in c['sporadic_cases']]==[12,24,36]
for q in c['sporadic_cases']:
    a=q['a'];angles=[120+a,120-a,60,108,168]
    legal=[list(t) for t in multisets(range(5),3) if sum(angles[i] for i in t)==360]
    assert angles==q['angles'] and legal==q['legal_triples']
    covered={i for t in legal for i in t};missing=[i for i in (2,3,4) if i not in covered]
    assert missing==q['uncovered_sporadic_categories'] and missing
assert not any(sum((60,108,168)[i] for i in t)==360 for t in multisets(range(3),3))
# Endpoint graph each native corner is a link edge. Endpoint identifications
# connect the two ends of these link edges; degree2 components must be cycles.
links={(f,j):[] for f in range(3) for j in range(6)};used=[];seams=[]
assert len(c['torus_pairings'])==9 and c['reference_reflections']==[False]*3
for (f,i),(g,j) in c['torus_pairings']:
    used.extend(((f,i),(g,j)))
    for u,v in [((f,i),(g,(j+1)%6)),((f,(i+1)%6),(g,j))]:
        links[u].append(v);links[v].append(u);seams.append([list(u),list(v)])
assert sorted(used)==list(links) and seams==c['torus_seam_endpoint_pairs']
assert all(len(v)==2 for v in links.values())
left=set(links);components=[]
while left:
    start=min(left);stack=[start];seen={start}
    while stack:
        for v in links[stack.pop()]:
            if v not in seen:seen.add(v);stack.append(v)
    left-=seen;components.append(sorted(seen))
assert len(components)==6 and all(len(v)==3 for v in components)
assert components==[list(map(tuple,q['corners'])) for q in c['torus_flat_vertices']]
for corners in components:
    assert {f for f,j in corners}=={0,1,2}
    coef=sum((1 if j%2==0 else -1) if f<2 else (-2 if j%2==0 else 2) for f,j in corners)
    assert coef==0
assert len(components)-9+3==0
print('PASS: independent 20 angular rows, all sporadic branches, 9 seams and 6 circular flat vertex links.')
