#!/usr/bin/env python3
"""Reconstruct the directed matrix from actual Lang--Hayes child coordinates.
No cluster census. Replay with the repository mise/conda command wrapper.
"""
import importlib.util, json
from pathlib import Path
from sage.all import matrix, ZZ
root=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('source',root/'research/searches/penrose-kite-dart-patch.py')
src=importlib.util.module_from_spec(spec); spec.loader.exec_module(src)
K,w,phi=src.K,src.w,src.phi
# Canonical reference triples have negative signed orientation; reflection
# gives the opposite chirality before the script's explicit normalization.
A=('a1',K(1),K(0),w)
O=('o1',K(0),w/phi,K(1))
labels=[('a1',1),('a1',-1),('o1',1),('o1',-1)]
S=matrix(ZZ,4,4)
boundary_checks=[]
imbalances=[]
def directional(q):
    q=list(q)
    if src.sign(src.area(q))<0: q.reverse()
    d=[K(0)]*5
    for a,b in zip(q,q[1:]+q[:1]):
        v=b-a
        matches=[]
        for j in range(10):
            length=v/w**j
            if length==length.conjugate() and src.sign(length)>0:
                matches.append((j,length))
        assert len(matches)==1
        j,length=matches[0]; d[j%5]+=length if j<5 else -length
    return d
for j,(typ,hand) in enumerate(labels):
    ref=A if typ=='a1' else O
    pts=list(ref[1:])
    if src.sign(src.area(pts))!=hand: pts=[z.conjugate() for z in pts]
    imbalances.append(directional(pts))
    children=src.step(src.step([(typ,*pts)]))
    for t,x,y,z in children:
        S[labels.index((t,src.sign(src.area([x,y,z])))),j]+=1
    # Exact oriented edge-vector closure: use CCW boundaries irrespective of
    # ordered atom chirality. Full positional seam cancellation requires
    # splitting at every child endpoint, which is done below.
    segments=[]
    for _,x,y,z in children:
        q=[x,y,z]
        if src.sign(src.area(q))<0: q.reverse()
        segments.extend(zip(q,q[1:]+q[:1]))
    parent=pts[:]
    if src.sign(src.area(parent))<0: parent.reverse()
    parentseg=list(zip(parent,parent[1:]+parent[:1]))
    vertices=set(v for e in segments+parentseg for v in e)
    def split(seg):
        counts={}
        for a,b in seg:
            v=b-a
            on=[]
            for z in vertices:
                t=(z-a)/v
                if t==t.conjugate() and src.sign(t)>=0 and src.sign(1-t)>=0:
                    on.append((src.AA(src.emb(t)),z))
            on.sort(key=lambda item:item[0])
            for (_,u),(_,v) in zip(on,on[1:]):
                counts[(u,v)]=counts.get((u,v),0)+1
                counts[(v,u)]=counts.get((v,u),0)-1
        return {e:n for e,n in counts.items() if n}
    assert split(segments)==split(parentseg)
    boundary_checks.append(True)
expected=matrix(ZZ,[[1,1,0,1],[1,1,1,0],[1,0,1,0],[0,1,0,1]])
assert S==expected
C=matrix(ZZ,[[1,0],[1,0],[0,1],[0,1]])
M=matrix(ZZ,[[2,1],[1,1]])
assert S*C==C*M
assert S.charpoly().list()==[1,-4,5,-4,1]
# Antisymmetric chirality coordinates transform by R, an order-six map.
D=matrix(ZZ,[[1,-1,0,0],[0,0,1,-1]])
R=matrix(ZZ,[[0,-1],[1,1]])
assert D*S==R*D and R**3==-matrix.identity(ZZ,2)
result={'source':'research/searches/penrose-kite-dart-patch.py step(), applied twice',
 'atom_order':['A+','A-','O+','O-'],'S':[[int(v) for v in r] for r in S.rows()],
 'charpoly':'(x^2-3*x+1)*(x^2-x+1)',
 'C':[[int(v) for v in r] for r in C.rows()],'M':[[int(v) for v in r] for r in M.rows()],
 'directed_positional_boundary_checks':boundary_checks,
 'atom_directional_imbalances':[[str(v) for v in row] for row in imbalances],
 'balanced_A_mirror_pair_imbalance':[str(v) for v in directional([K(0),w.conjugate(),K(1),w])],
 'geometric_partition_certified':False,
 'status':'inventory necessary condition only; no candidate output polygons'}
out=root/'research/certificates/penrose-directed-triangle-inventory.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,sort_keys=True))
