#!/usr/bin/env python3
"""Independent Q(zeta720) closure of11 forced B bracelets; no author imports."""
from pathlib import Path
from itertools import permutations,product
import json
from sage.all import CyclotomicField,QQbar,AA
K=CyclotomicField(720);r=K.gen();z=r**2;j=r**180
h=K.hom([QQbar.zeta(720)],QQbar)
cr=lambda x,y:(x.conjugate()*y-x*y.conjugate())/(2*j)
S=(1+z**67,z**126+z**185,z**239+z**293)
k=(cr(S[1],S[2]),cr(S[2],S[0]),cr(S[0],S[1]))
length=tuple(q/k[0] for q in k)
assert len(set(length))==3 and all(AA(h(q).real())>0 for q in length)
angles=(134,118,108)
cols=(0,0,1,1,2,2)
classes=(0,0,1,1,2,2)
root=Path(__file__).resolve().parents[2]
c=json.loads((root/"research/certificates/terra-001122-b-neighbourhood.json").read_text())
palette={}
for i in range(6):
    pair=tuple(sorted((cols[i],cols[(i+1)%6])))
    assert pair not in palette or palette[pair]==classes[i]
    palette[pair]=classes[i]
assert palette=={tuple(p["endpoint_pair"]):p["side_class"] for p in c["palette"]}
fan=[set() for _ in range(3)]
for i,si,k,sk in product(range(6),range(2),range(6),range(2)):
    if cols[i]!=cols[k]:continue
    ai=(classes[(i-1)%6],classes[i]);ak=(classes[(k-1)%6],classes[k])
    if ai[si]==ak[sk]:fan[cols[i]].add((ai[1-si],ak[1-sk]))
assert fan==[{tuple(p) for p in row["ordered_pairs"]} for row in c["fans"]]
def canonical(w):return min(q[k:]+q[:k] for q in (w,w[::-1]) for k in range(6))
words=sorted({canonical(w) for w in permutations(cols)})
assert len(words)==11 and words==[tuple(q["B_word"]) for q in c["B_rows"]]
survive=[]
for w,row in zip(words,c["B_rows"]):
    a=tuple(palette[tuple(sorted((w[i],w[(i+1)%6])))] for i in range(6))
    assert list(a)==row["forced_side_classes"]
    assert all((a[i-1],a[i]) in fan[w[i]] for i in range(6))
    d=[0]
    for colour in w[1:]:d.append(d[-1]+180-angles[colour])
    assert d==row["directions"]
    v=[K(0)]
    for q,b in zip(a,d):v.append(v[-1]+length[q]*z**b)
    assert (v[-1]==0)==row["closes"]
    if v[-1]!=0:continue
    survive.append(w)
    assert w[:3]==w[3:] and a[:3]==a[3:]
    assert all(AA(h(cr(v[i+1]-v[i],v[k]-v[i])).real())>0
               for i in range(6) for k in range(6) if k not in (i,(i+1)%6))
    assert row["strictly_convex"] and row["centrally_symmetric"]
assert survive==[(0,1,2,0,1,2)]
print("PASS: independent exact forced AB palettes, reflected AAB fans,11 B bracelets; only opposite-equal012012 closes with strict supports")
