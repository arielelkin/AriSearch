"""Exact binary square-lattice power-cell first gate; no solver dependencies."""
from fractions import Fraction as F
from collections import Counter
import json

def cell(mask):
    b=lambda x,y:(mask>>((y+1)*3+x+1))&1
    p=[(F(-1),F(-1)),(F(1),F(-1)),(F(1),F(1)),(F(-1),F(1))]
    for a,c in ((1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,1),(-1,-1),(1,-1)):
        h=F(a*a+c*c,2)+F(b(0,0)-b(a,c),10)
        q=[]
        for s,t in zip(p,p[1:]+p[:1]):
            ds=a*s[0]+c*s[1]-h; dt=a*t[0]+c*t[1]-h
            if ds<=0:q.append(s)
            if (ds<0<dt) or (dt<0<ds):
                z=ds/(ds-dt); q.append(tuple(s[i]+z*(t[i]-s[i]) for i in (0,1)))
        p=q
    # Delete collinear vertices, including boundary coincidences.
    p=list(dict.fromkeys(p))
    while True:
        q=[v for i,v in enumerate(p) if (v[0]-p[i-1][0])*(p[(i+1)%len(p)][1]-v[1]) != (v[1]-p[i-1][1])*(p[(i+1)%len(p)][0]-v[0])]
        if len(q)==len(p):break
        p=q
    return p

def signature(p):
    n=len(p)
    # Full cyclic distance matrix is an intrinsic congruence invariant and complete.
    return min(tuple(sum((p[(s+d*i)%n][k]-p[(s+d*j)%n][k])**2 for k in (0,1)) for i in range(n) for j in range(n)) for s in range(n) for d in (-1,1))

cells=[cell(m) for m in range(512)]
sigs=[signature(p) for p in cells]
def local(bits,x,y):
    return sum(((bits>>(((y+v)%4)*4+(x+u)%4))&1)<<((v+1)*3+u+1) for v in (-1,0,1) for u in (-1,0,1))

counts=Counter(); witnesses={}
for bits in range(1<<16):
    masks=[local(bits,x,y) for y in range(4) for x in range(4)]
    if min(len(cells[m]) for m in masks)<5:continue
    classes={sigs[m] for m in masks}
    key=(len(classes),tuple(sorted({len(cells[m]) for m in masks})))
    counts[str(key)]+=1
    if len(classes)==2:
        witnesses.setdefault(str(key),bits)

out={'domain':'all 65536 labelled binary 4x4 tori; weight contrast 1/5', 'counts':dict(counts),'two_class_witnesses':{}}
for key,bits in witnesses.items():
    reps={}
    for y in range(4):
        for x in range(4):
            m=local(bits,x,y); reps.setdefault(sigs[m],m)
    out['two_class_witnesses'][key]={'bits':bits,'rows':[''.join(str((bits>>(4*y+x))&1) for x in range(4)) for y in range(4)],'polygons':[[[str(x),str(y)] for x,y in cells[m]] for m in reps.values()]}
print(json.dumps(out,indent=2))
