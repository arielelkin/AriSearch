#!/usr/bin/env python3
"""No-cross all-mask finite obligation:2words*2bases*8cells, all12poses.
Verify2A states,2B states per metric branch, and2 combined B profiles when
both branches occur and closure forces reflection symmetry. No polygonsearch.
"""
import argparse,json
from itertools import product
from pathlib import Path
import sympy as sy
D=((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))
P=list(product(range(6),(1,-1)));B=(3,4,4,4,4,4);BM=(0,1,2,2,1,0)
def corner(W,p,k):return W[(p[0]+p[1]*k)%6]
def side(p,k):
 ends={(p[0]+p[1]*k)%6,(p[0]+p[1]*(k+1))%6}
 return next(j for j in range(6) if {j,(j+1)%6}==ends)
records=[]
for word in ('001122','010122'):
 A=tuple(map(int,word))
 for initial in (0,1):
  q=(0,initial,1,1-initial)
  def species(i,j):return 'A' if (i+q[j%4])%2==0 else 'B'
  cells=[]
  for j,i in product(range(4),range(2)):
   own=species(i,j);ns=[species(i+dx,j+dy) for dx,dy in D]
   assert all(not(own==ns[k]==ns[(k+1)%6]) for k in range(6))
   stars=['AAB' if [own,ns[k],ns[(k+1)%6]].count('A')==2 else 'ABB' for k in range(6)]
   same_sides=[k for k in range(6) if ns[(k+1)%6]==own]
   assert len(same_sides)==2 and (same_sides[1]-same_sides[0])%6 not in (1,3,5)
   special22=[k for k in range(6) if ns[(k+1)%6]!=own and stars[k]==stars[(k+1)%6]=='ABB']
   special01=[k for k in range(6) if ns[(k+1)%6]!=own and stars[k]==stars[(k+1)%6]=='AAB']
   assert len(special22)==len(special01)==1 and (special22[0]-special01[0])%6==3
   zedge,oedge=special22[0],special01[0]
   if own=='A':
    allowed=[p for p in P if all((corner(A,p,k)==2)==(stars[k]=='ABB') for k in range(6))]
    assert len(allowed)==2
    for p in allowed:
     assert {side(p,k) for k in same_sides}=={0,2}
     assert side(p,zedge)==4 and side(p,oedge)==1
    cells.append(dict(cell=[i,j],species=own,stars=stars,AA_native=[0,2],AB22_global=zedge,AB01_global=oedge,allowed_poses=allowed))
   else:
    allowed=[p for p in P if all(corner(B,p,k)==4 for k in range(6) if stars[k]=='ABB')]
    assert len(allowed)==4
    branches={}
    for p in allowed:
     assert {side(p,k) for k in same_sides} in ({1,3},{2,4})
     pair=(side(p,zedge),side(p,oedge));assert pair in ((2,5),(3,0))
     branches.setdefault(str(pair),[]).append(p)
    assert set(map(len,branches.values()))=={2} and len(branches)==2
    profiles={}
    for p in allowed:
     profile=(tuple(corner(B,p,k) for k in range(6)),tuple(BM[side(p,k)] for k in range(6)))
     profiles.setdefault(str(profile),[]).append(p)
    assert len(profiles)==2 and set(map(len,profiles.values()))=={2}
    cells.append(dict(cell=[i,j],species=own,stars=stars,AB22_global=zedge,AB01_global=oedge,allowed_poses=allowed,metric_branches=branches,symmetric_combined_profiles=profiles))
  records.append(dict(A_word=word,initial_row_phase=initial,row_phases=q,cells=cells))
E=sy.symbols('E',nonzero=True);m,n,p,t=sy.symbols('m n p t',real=True)
f=m+p*E+n*E**2+n*E**3+t*E**4+m*E**5
assert sy.cancel(f-E**5*f.subs(E,1/E)-(p-t)*(E-E**4))==0
out=dict(domain='2Awords*2speciesbases*8cells;12indexedposes each;allgeometryconditionalactualfield',records=records,B_closure_reversal_identity='f(E)-E^5 f(E^-1)=(p-q)(E-E^4)',angle_constraints='everyAAB is equality of twoAcolourmaps and Bcorner map r->0,s->1;ABBautomatic',scope='actualunusedAA22support;derivednoAAA/allcurvedlimit;allmetricaliasesallowed')
a=argparse.ArgumentParser();a.add_argument('--output',type=Path);a.add_argument('--check',type=Path);args=a.parse_args()
if args.check:
 assert json.loads(args.check.read_text())==json.loads(json.dumps(out))
 print('PASS2words/2bases/32cells:2A states,2B states per branch,2 Breflectionprofiles;exactclosureidentity')
elif args.output:args.output.write_text(json.dumps(out,indent=2)+'\n')
else:print(json.dumps(out,indent=2))
