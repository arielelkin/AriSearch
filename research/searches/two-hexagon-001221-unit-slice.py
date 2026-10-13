#!/usr/bin/env python3
"""Falsification slice: U=exp(67deg i), B001221; all algebraic V roots.
Only unit acute-turn roots allowed. Actual polygon/support and omission gates
are checked before any global extension search. No tiling is asserted.
"""
import json,argparse
from itertools import combinations_with_replacement
from pathlib import Path
import sympy as s
from sage.all import CyclotomicField,QQbar,AA,PolynomialRing
U,V=s.symbols('U V',nonzero=True)
d=json.loads(Path('research/certificates/two-hexagon-001122-symbolic-b-closure.json').read_text())
row=next(r for r in d['rows'] if r['word']==[0,0,1,2,2,1])
p=s.Poly(s.sympify(row['numerator'],locals={'U':U,'V':V}),U,V)
parser=argparse.ArgumentParser();parser.add_argument('--rational-unit',action='store_true');args=parser.parse_args()
z=QQbar.zeta(360);u=(QQbar(3)+4*QQbar.zeta(4))/5 if args.rational_unit else z**67
R=PolynomialRing(QQbar,'v');v=R.gen()
poly=sum(int(c)*u**a*v**b for (a,b),c in p.terms())
roots=poly.roots();records=[]
print('algebraic roots',len(roots),flush=True)
def det(a,b):return AA((a.conjugate()*b).imag())
def supports(P):return all(det(P[(i+1)%6]-P[i],P[j]-P[i])>0 for i in range(6) for j in range(6) if j not in(i,(i+1)%6))
def mono(angles,lens):
    result=[]
    for k in range(6):
      for sg in (1,-1):
        ac=lambda i:angles[(k+sg*i)%6]
        ll=lambda i:lens[(k+i)%6] if sg==1 else lens[(k-i-1)%6]
        h1=ac(0)*ac(1)*ac(2)==1 and ll(2)==ll(5)
        h2=ac(0)*ac(1)*ac(3)==1 and ll(1)==ll(3) and ll(2)==ll(5)
        h3=all(ac(i)==QQbar.zeta(3) for i in (0,2,4)) and ll(0)==ll(1) and ll(2)==ll(3) and ll(4)==ll(5)
        if h1 or h2 or h3:result.append((k,sg,h1,h2,h3))
    return result
for vv,m in roots:
    if vv==0:continue
    ww=-1/(u*vv)
    allowed=all(t.real()>0 and t.imag()>0 and t*t.conjugate()==1 for t in(u,vv,ww))
    if not allowed:continue
    S=(1+u,u*vv*(1+vv),-vv*(1+ww))
    weights=(det(S[1],S[2]),det(S[2],S[0]),det(S[0],S[1]))
    lens=tuple(QQbar(q/weights[0]) for q in weights)
    assert all(l.real()>0 and l.imag()==0 for l in lens)
    assert sum(a*b for a,b in zip(S,lens))==0
    Aang=(-1/u,-1/vv,-1/ww);Bang=(u*u,vv*vv,ww*ww)
    allang=Aang+Bang
    triples=[list(t) for t in combinations_with_replacement(range(6),3) if allang[t[0]]*allang[t[1]]*allang[t[2]]==1]
    exactstars=triples==[[0,0,3],[0,1,2],[1,1,4],[2,2,5],[3,4,5]]
    Ae=(1,u,u*vv,u*vv*vv,-vv,-vv*ww)
    Alen=(lens[0],lens[0],lens[1],lens[1],lens[2],lens[2]);Aa=(Aang[0],Aang[0],Aang[1],Aang[1],Aang[2],Aang[2])
    AP=[QQbar(0)]
    for le,e in zip(Alen,Ae):AP.append(AP[-1]+le*e)
    assert AP[-1]==0
    Be=[QQbar(1)]
    for col in row['word'][1:]:Be.append(Be[-1]*(-1/(u,vv,ww)[col]**2))
    Blen=tuple(lens[k] for k in row['side_classes']);Ba=tuple(Bang[k] for k in row['word']);BP=[QQbar(0)]
    for le,e in zip(Blen,Be):BP.append(BP[-1]+le*e)
    assert BP[-1]==0
    ar=mono(Aa,Alen);br=mono(Ba,Blen)
    record={'V_minpoly':str(vv.minpoly()),'V_real_approx':str(vv.real().n(digits=20)),'V_imag_approx':str(vv.imag().n(digits=20)),
            'A_strictly_convex':supports(AP[:-1]),'B_strictly_convex':supports(BP[:-1]),
            'exact_generic_star_language':exactstars,'actual_triples':triples,
            'A_monohedral_classes':ar,'B_monohedral_classes':br,
            'lengths_approx':[str(l.real().n(digits=15)) for l in lens]}
    records.append(record);print(record,flush=True)
out={'finite_domain':('U=(3+4i)/5' if args.rational_unit else 'U=zeta360^67')+' fixed; all roots V of full B001221 closure numerator; exact QQbar embedding',
     'root_count':len(roots),'retained_unit_acute_roots':records,
     'scope':'Exact geometric feasibility and monohedral escape tests only; infinite mixed covering and nonperiodicity not proved'}
Path('research/certificates/two-hexagon-001221-'+('rational-unit-slice' if args.rational_unit else 'unit-slice')+'.json').write_text(json.dumps(out,indent=2)+'\n')
