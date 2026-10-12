#!/usr/bin/env python3
"""Exact cheap compiler gate: convex subsets and partitions of8fixed hatkites.

No new source-decoration enumeration. Coordinates from retained exact
reference-hat producer, checked in Q(sqrt3). No forcing inherited merely
from selecting a partition.
"""
import importlib.util,itertools,json,sys
from pathlib import Path
from sage.all import QuadraticField,AA,QQ

K=QuadraticField(3,'r',embedding=AA(3).sqrt());r=K.gen()
def sign(x):return AA(x)
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def sub(a,b):return (a[0]-b[0],a[1]-b[1])
def hull(points):
    points=sorted(set(points),key=lambda p:(AA(p[0]),AA(p[1])))
    def chain(points):
        out=[]
        for p in points:
            while len(out)>=2 and sign(cross(sub(out[-1],out[-2]),sub(p,out[-1])))<=0:out.pop()
            out.append(p)
        return out
    return chain(points)[:-1]+chain(list(reversed(points)))[:-1]
def area2(P):return sum(cross(P[i],P[(i+1)%len(P)]) for i in range(len(P)))
def norm2(a):return a[0]**2+a[1]**2
def congruent(P,Q):
    if len(P)!=len(Q):return False
    n=len(P)
    return any(all(norm2(sub(P[i],P[j]))==norm2(sub(Q[(s+d*i)%n],Q[(s+d*j)%n]))
                   for i,j in itertools.combinations(range(n),2)) for s in range(n) for d in (1,-1))
def encoded(P):return [[[str(K(x)[0]),str(K(x)[1])] for x in p] for p in P]

spec=importlib.util.spec_from_file_location('hat',Path('research/searches/source-decoration-hat-patch.py'))
hat=importlib.util.module_from_spec(spec);spec.loader.exec_module(hat)
kites=[[(K(p[0].a)+K(p[0].b)*r,K(p[1].a)+K(p[1].b)*r) for p in kite] for kite in hat.ref_kites()]
outline=[(K(p[0].a)+K(p[0].b)*r,K(p[1].a)+K(p[1].b)*r) for p in hat.hat_outline]
assert len(kites)==8 and sum(area2(kite) for kite in kites)==area2(outline)
convex=[];polys={}
for mask in range(1,256):
    indices=[i for i in range(8) if mask>>i&1]
    P=hull([p for i in indices for p in kites[i]])
    A=sum(area2(kites[i]) for i in indices)
    if area2(P)!=A:continue
    polys[mask]=P
    convex.append({'mask':mask,'kite_indices':indices,'corners':len(P),'hull':encoded(P),
                   'centrally_symmetric':len(P)%2==0 and all(tuple(P[i][j]+P[(i+len(P)//2)%len(P)][j] for j in (0,1))==tuple(P[0][j]+P[len(P)//2][j] for j in (0,1)) for i in range(len(P)//2))})
eligible=[row['mask'] for row in convex if row['corners']>=5]
partitions=[]
def partition(remaining,chosen):
    if not remaining:
        reps=[]
        for mask in chosen:
            if not any(congruent(polys[mask],P) for P in reps):reps.append(polys[mask])
        partitions.append({'masks':chosen,'congruence_classes':len(reps),'corner_counts':[len(P) for P in reps]});return
    first=(remaining&-remaining).bit_length()-1
    for mask in eligible:
        if mask>>first&1 and mask&remaining==mask:partition(remaining^mask,chosen+[mask])
partition(255,[])
out={'scope':'All255nonempty subsets ofthe fixed8kite decomposition ofTile(1,sqrt3); convex unions with>=5intrinsiccorners; allwhole-kitepartitions ofthe referencehat into suchunions.',
     'field':'Q(r),r^2=3,r>0','source_primary':'https://arxiv.org/html/2303.10798v3',
     'kites':[encoded(k) for k in kites],'hat_outline':encoded(outline),
     'convex_subsets':convex,'eligible_masks':eligible,'partitions':partitions,
     'at_most_two_class_partitions':[p for p in partitions if p['congruence_classes']<=2]}
Path(sys.argv[1]).write_text(json.dumps(out,indent=2)+'\n')
print('convex subsets',len(convex),'eligible>=5',len(eligible),'partitions',partitions,flush=True)
print('convex corner-counts',[(row['mask'],row['corners']) for row in convex],flush=True)
