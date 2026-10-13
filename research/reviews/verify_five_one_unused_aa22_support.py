#!/usr/bin/env python3
"""Independent unused-AA22 native fibre audit; no producer imports.
The sparse-limit, support and global-lift arguments need the accompanying review.
"""
import json
from itertools import product, combinations_with_replacement
from pathlib import Path
import sympy as sp

J=json.loads(Path('research/certificates/five-one-all-mask-no-cross-binary-lift.json').read_text())
assert J['scope']=='actualunusedAA22support;derivednoAAA/allcurvedlimit;allmetricaliasesallowed'
# Independently reconstruct the star palette from exact affine angle pairs.
angles=((1,0),(-5,720),(4,-360),(-2,360),(10,-1080))
triples=[t for t in combinations_with_replacement(range(5),3)
         if tuple(sum(angles[i][k] for i in t) for k in (0,1))==(0,360)]
assert triples==[(0,0,3),(0,1,2),(1,1,4),(2,3,3)]
steps=((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))
poses=list(product(range(6),(-1,1)))

def native_edge(pose,slot):
    start,direction=pose
    return (start+direction*slot-(direction==-1))%6

def native_corner(pose,slot):
    return (pose[0]+pose[1]*slot)%6

n_cells=0
for rec in J['records']:
    word=tuple(map(int,rec['A_word']))
    assert word in ((0,0,1,1,2,2),(0,1,0,1,2,2))
    q=(0,rec['initial_row_phase'],1,1-rec['initial_row_phase'])
    assert tuple(rec['row_phases'])==q
    def species(i,j):return 'AB'[(i+q[j%4])%2]
    for row in rec['cells']:
        n_cells+=1
        i,j=row['cell'];own=species(i,j)
        neighbours=[species(i+dx,j+dy) for dx,dy in steps]
        count=[sum(t=='A' for t in (own,neighbours[k],neighbours[(k+1)%6])) for k in range(6)]
        assert set(count)=={1,2}
        stars=['AAB' if n==2 else 'ABB' for n in count]
        assert row['species']==own and row['stars']==stars
        zedge=[k for k in range(6) if stars[k]==stars[(k+1)%6]=='ABB' and neighbours[(k+1)%6]!=own]
        oedge=[k for k in range(6) if stars[k]==stars[(k+1)%6]=='AAB' and neighbours[(k+1)%6]!=own]
        assert len(zedge)==len(oedge)==1 and (zedge[0]-oedge[0])%6==3
        zedge,oedge=zedge[0],oedge[0]
        assert (row['AB22_global'],row['AB01_global'])==(zedge,oedge)
        if own=='A':
            allowed=[p for p in poses if all((word[native_corner(p,k)]==2)==(count[k]==1) for k in range(6))]
            assert len(allowed)==2
            assert sorted(allowed)==sorted(map(tuple,row['allowed_poses']))
            for p in allowed:
                actual_AA={native_edge(p,k) for k in range(6) if neighbours[(k+1)%6]=='A'}
                assert actual_AA=={0,2}
                assert (native_edge(p,zedge),native_edge(p,oedge))==(4,1)
        else:
            allowed=[p for p in poses if all(native_corner(p,k)!=0 for k in range(6) if count[k]==1)]
            assert len(allowed)==4
            assert sorted(allowed)==sorted(map(tuple,row['allowed_poses']))
            branches={}
            for p in allowed:
                bb={native_edge(p,k) for k in range(6) if neighbours[(k+1)%6]=='B'}
                assert bb in ({1,3},{2,4})
                pair=(native_edge(p,zedge),native_edge(p,oedge))
                branches.setdefault(pair,[]).append(p)
            assert set(branches)=={(2,5),(3,0)}
            assert all(len(v)==2 for v in branches.values())
            assert {str(k):sorted(v) for k,v in branches.items()}=={k:sorted(map(tuple,v)) for k,v in row['metric_branches'].items()}
            # Independent profile quotient with literal symbolic length names.
            lens=('m','p','n','n','p','m')
            profiles={}
            for p in allowed:
                profile=(tuple(native_corner(p,k)==0 for k in range(6)),tuple(lens[native_edge(p,k)] for k in range(6)))
                profiles.setdefault(profile,[]).append(p)
            assert sorted(map(len,profiles.values()))==[2,2]
assert len(J['records'])==4 and n_cells==32
E,m,n,p,q=sp.symbols('E m n p q',nonzero=True)
f=m+p*E+n*E**2+n*E**3+q*E**4+m*E**5
assert sp.expand(E**5*f.subs(E,1/E)-f)==sp.expand((q-p)*(E-E**4))
# R=2x-180 lies strictly in (36,72); E^3=1 has no solution there.
assert 0<3*36<3*72<360
print('PASS independent 35-triple palette, 32 cells, all full native fibres, branches, aliases, reflection quotient and B closure identity')
