#!/usr/bin/env python3
"""Render retained exact finite U/V source clusters; floats only for SVG."""
import importlib.util
import json
from pathlib import Path
from sage.all import QQ,QQbar
spec=importlib.util.spec_from_file_location("geo",Path(__file__).with_name("pentagrid-golden-metric-robinson-partitions.py"))
geo=importlib.util.module_from_spec(spec);spec.loader.exec_module(geo)
K,z,phi=geo.K,geo.z,geo.phi
root=Path(__file__).parents[1]
cert=json.loads((root/"certificates"/"pentagrid-robinson-residual-rhombs.json").read_text())
svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="550" viewBox="0 0 1000 550">',
     '<rect width="1000" height="550" fill="white"/>',
     '<text x="500" y="27" text-anchor="middle" font-family="sans-serif" font-size="19">Exact finite unit rhomb source geometry</text>',
     '<text x="500" y="51" text-anchor="middle" font-family="sans-serif" font-size="13">Penrose arrows, infinite source membership and global repartition remain unproved</text>']
for panel,name in enumerate(("U","V")):
    witness=cert["fixtures"][name]["first_witness"];assert witness is not None
    whole=[[K([QQ(x) for x in p]) for p in r] for r in witness["whole_rhombs"]]
    parent=([K(0),phi**3,z+z**2+z**3,z**2+z**3,z**3] if name=="U" else
            [K(0),K(1),1+(1+3*phi)*z**3,2*phi**2*z**3,2*phi*z**4])
    dirs=[0,4,6,7,8] if name=="U" else [0,3,6,7,9]
    half=[];outer=[]
    for i,(word,k) in enumerate(zip(witness["side_words"],dirs)):
        x=parent[i]
        for symbol in word:
            y=x+{"u":K(1),"l":phi,"s":phi-1}[symbol]*z**k
            if symbol!="u":
                a=x+z**(k+(1 if symbol=="l" else 2))
                half.append(([x,y,a],symbol));outer.append([x,x+y-a,y,a])
            x=y
    def xy(p):
        q=QQbar(p);return float(q.real()),float(q.imag())
    vertices=[xy(p) for poly in whole+outer for p in poly]
    lo=[min(p[i] for p in vertices) for i in (0,1)];hi=[max(p[i] for p in vertices) for i in (0,1)]
    scale=min(440/(hi[0]-lo[0]),390/(hi[1]-lo[1]));cx=panel*500+250;cy=300
    def pixel(p):
        x,y=xy(p);return (cx+scale*(x-(lo[0]+hi[0])/2),cy-scale*(y-(lo[1]+hi[1])/2))
    def polygon(poly,fill,stroke,width=1,dash=None):
        points=" ".join('%.4f,%.4f'%pixel(p) for p in poly)
        extra='' if dash is None else ' stroke-dasharray="%s"'%dash
        svg.append('<polygon points="%s" fill="%s" stroke="%s" stroke-width="%s"%s/>'%(points,fill,stroke,width,extra))
    for poly in outer:polygon(poly,'#f3f3f3','#9b9b9b',1,'5,4')
    for i,poly in enumerate(whole):
        thin=any((poly[j]-poly[(j+2)%4])*(poly[j]-poly[(j+2)%4]).conjugate()==phi**(-2) for j in (0,1))
        polygon(poly,'#ffd78c' if thin else '#acd5ed','#46505c',1.3)
        target=phi**(-2) if thin else phi**2
        for j in (0,1):
            if (poly[j]-poly[j+2])*(poly[j]-poly[j+2]).conjugate()==target:
                a,b=pixel(poly[j]),pixel(poly[j+2]);svg.append('<path d="M %.4f %.4f L %.4f %.4f" stroke="#7c8991" stroke-width="0.8" fill="none"/>'%(*a,*b))
        x,y=pixel(sum(poly)/4);svg.append('<text x="%.4f" y="%.4f" text-anchor="middle" font-family="sans-serif" font-size="12">%d</text>'%(x,y,i+1))
    for poly,symbol in half:polygon(poly,'#ffd78c' if symbol=='s' else '#acd5ed','#46505c',1.3)
    polygon(parent,'none','#151922',2.5)
    svg.append('<text x="%d" y="91" text-anchor="middle" font-family="sans-serif" font-size="16">%s: %d whole rhombs + %d boundary halves</text>'%(panel*500+250,name,len(whole),len(half)))
svg.append('<text x="500" y="531" text-anchor="middle" font-family="sans-serif" font-size="12">Grey dashed rhombs complete boundary halves outside each pentagon; exact coordinates are retained in the certificate.</text>')
svg.append('</svg>')
Path(__file__).with_name("pentagrid-robinson-source-clusters.svg").write_text(chr(10).join(svg)+chr(10))
print('Rendered retained exact first source-cluster witnesses to research/searches/pentagrid-robinson-source-clusters.svg')
