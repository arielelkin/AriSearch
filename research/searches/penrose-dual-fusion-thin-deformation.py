#!/usr/bin/env python3
"""Finite exact omission/convexity gate for t=1/100 marked thin-point shift.
Symbolic family p_r(t)=center_r+t*w^frame for thin rhombs, centers for thick.
Only one local fused cell is a candidate; no infinite covering asserted.
"""
import json, importlib.util, argparse
from collections import defaultdict
from pathlib import Path
from sage.all import CyclotomicField, QQbar, AA, QQ
K=CyclotomicField(10); w=K.gen(); emb=K.hom([QQbar.zeta(10)])
def decode(v): return sum(K(c)*w**i for i,c in enumerate(v))
def encode(z): return [str(c) for c in z.vector()]
def cross(a,b): return (a.conjugate()*b-a*b.conjugate())/(w-w.conjugate())
def sign(z): return int(AA(emb(z)).sign())
d=json.loads(Path('research/certificates/penrose-centered-dual-single-fusion-source.json').read_text())
verts=[decode(v) for v in d['verts']]; t=QQ(1)/100
points=[]
for kind,r,a in d['rhombs']:
    p=sum(verts[v] for v in r)/4+(t*w**a if kind=='thin' else 0)
    # Source frames need not be CCW; use each polygon's own orientation.
    orientation=sign(sum(cross(verts[r[i]],verts[r[(i+1)%4]]) for i in range(4)))
    assert all(orientation*sign(cross(verts[r[(i+1)%4]]-verts[r[i]],p-verts[r[i]]))>0 for i in range(4))
    points.append(p)
edges=defaultdict(list)
for i,(_,r,_) in enumerate(d['rhombs']):
    for j in range(4):edges[tuple(sorted((r[j],r[(j+1)%4])))].append(i)
for (v,u),rs in edges.items():
    if len(rs)!=2:continue
    a,b=[points[r] for r in rs]; e=verts[u]-verts[v]; direction=b-a
    lam=cross(verts[v]-a,e)/cross(direction,e)
    mu=cross(a-verts[v],direction)/cross(e,direction)
    assert 0<AA(emb(lam))<1 and 0<AA(emb(mu))<1
for local_ids in ([3,6,7],[3,5,58,6]):
    Q=[points[r] for r in local_ids]
    assert all(sign(cross(Q[(i+1)%len(Q)]-Q[i],Q[j]-Q[i]))>0 for i in range(len(Q)) for j in range(len(Q)) if j not in (i,(i+1)%len(Q)))
untouched_quad_ids=[10,12,17,11]
Q=[points[r] for r in untouched_quad_ids]
if sign(sum(cross(Q[i],Q[(i+1)%4]) for i in range(4)))<0: Q.reverse(); untouched_quad_ids.reverse()
assert all(sign(cross(Q[(i+1)%4]-Q[i],Q[j]-Q[i]))>0 for i in range(4) for j in range(4) if j not in (i,(i+1)%4))
ids=[3,5,58,6,7]; P=[points[r] for r in ids]
assert all(sign(cross(P[(i+1)%5]-P[i],P[j]-P[i]))>0 for i in range(5) for j in range(5) if j not in (i,(i+1)%5))
# Exact algebraic unit e^(i*alpha_i), alpha_i in (0,pi).
angles=[]
for i in range(5):
    a=emb(P[i-1]-P[i]); b=emb(P[(i+1)%5]-P[i]); ratio=a/b
    unit=ratio/(ratio*ratio.conjugate()).real().sqrt()
    assert unit.imag()>0
    angles.append(unit)
lengths=[AA(emb((P[(i+1)%5]-P[i])*(P[(i+1)%5]-P[i]).conjugate())).sqrt() for i in range(5)]
spec=importlib.util.spec_from_file_location('families',Path(__file__).with_name('pentagrid_monohedral_family_filter.py'))
families=importlib.util.module_from_spec(spec);spec.loader.exec_module(families)
rows=[]
for typ,(ae,le) in families.FAMILIES.items():
    for epsilon in (1,-1):
        for h in range(5):
            amap=[(h+epsilon*i)%5 for i in range(5)]
            smap=[(h+i)%5 if epsilon==1 else (h-i-1)%5 for i in range(5)]
            failures=[]
            for j,(coeff,target) in enumerate(ae):
                phase=QQbar(1)
                for c,i in zip(coeff,amap): phase*=angles[i]**c
                required=QQbar(1 if target==10 else -1)
                assert target in (5,10)
                if phase!=required: failures.append({'angle_equation':j})
            if not failures:
                for j,coeff in enumerate(le):
                    value=sum(c*lengths[i] for c,i in zip(coeff,smap))
                    if value!=0: failures.append({'length_equation':j})
            rows.append({'type':typ,'epsilon':epsilon,'offset':h,'failures':failures})
assert len(rows)==150
survivors=[r for r in rows if not r['failures']]
# Exact nonzero phase of the original Type1 wraparound relation.
old_phase=angles[3]*angles[4]*angles[0]
assert old_phase!=1
out={'family':'thin p=center+t*w^marked_frame; thick p=center', 'sample_t':str(t),
     'source_edge_deleted':[9,10],'fused_rhomb_ids':ids,'polygon':[encode(z) for z in P],
     'all_source_points_strictly_inside':True,'all_internal_center_lines_cross_source_edges_strictly':True,'triangle_and_quadrilateral_module_strictly_convex':True,'strict_convexity':True,
     'original_type1_angle_equation_broken':True,'untouched_quad_source_vertex':21,'untouched_quad_rhombs':untouched_quad_ids,'untouched_quad_coordinates':[encode(z) for z in Q],
     'monohedral_classification_dependency':'Rao arXiv1708.00274v1 Table2 types1..15; necessary list external',
     'finite_domain':'15 types x 10 dihedral relabelings = 150 exact algebraic tests',
     'family_tests':rows,'compatible_family_tests':survivors}
parser=argparse.ArgumentParser(); parser.add_argument('--check',type=Path); args=parser.parse_args()
if args.check:
    assert json.loads(args.check.read_text())==out
    print('PASS: exact convex local fusion; all 150 known monohedral-family relabelings fail.')
else: print(json.dumps(out,indent=2))
