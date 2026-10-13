#!/usr/bin/env python3
"""One exact retained-boundary H6 cut; no global source enumeration.
Changed hypothesis: fractional H pieces, source boundary retained, degree3 cut ends.
"""
import json,importlib.util
from pathlib import Path
from sage.all import CyclotomicField,QQ,QQbar,AA
K=CyclotomicField(10);w=K.gen();emb=K.hom([QQbar.zeta(10)])
def encode(z):return [str(c) for c in K(z).vector()]
def cross(a,b):return (a.conjugate()*b-a*b.conjugate())/(w-w.conjugate())
def sign(z):return int(AA(emb(z)).sign())
def area(P):return sum(cross(P[i],P[(i+1)%len(P)]) for i in range(len(P)))/2
J=QQ(1)/2+QQ(4)/5*w;Jp=1+w**4*(J-1);Jpp=w+w**6*(J-w)
H=[K(0),Jp,K(1),J,w,Jpp];q=(H[0]+H[1])/2;r=(H[3]+H[4])/2
P=[q,H[1],H[2],H[3],r];Q=[r,H[4],H[5],H[0],q]
for tile in (H,P,Q):
 assert all(sign(cross(tile[(i+1)%len(tile)]-tile[i],tile[j]-tile[i]))>0 for i in range(len(tile)) for j in range(len(tile)) if j not in(i,(i+1)%len(tile)))
assert sign(area(P))>0 and sign(area(Q))>0 and area(P)+area(Q)==area(H)
for e,end,other in ((0,q,r),(3,r,q)):
 assert end==(H[e]+H[(e+1)%6])/2
 assert cross(H[(e+1)%6]-H[e],other-end)!=0
 assert (H[e]-end)==-(H[(e+1)%6]-end)
 # The cut lies in source interior on its entire open segment by convexity.
 midpoint=(end+other)/2
 assert all(sign(cross(H[(i+1)%6]-H[i],midpoint-H[i]))>0 for i in range(6))
spec=importlib.util.spec_from_file_location('families',Path(__file__).with_name('pentagrid_monohedral_family_filter.py'))
families=importlib.util.module_from_spec(spec);spec.loader.exec_module(families)
records=[]
for name,tile in (('P',P),('Q',Q)):
 angles=[]
 for i in range(5):
  z=emb((tile[i-1]-tile[i])/(tile[(i+1)%5]-tile[i]));angles.append(z/(z*z.conjugate()).real().sqrt())
 lengths=[AA(emb((tile[(i+1)%5]-tile[i])*(tile[(i+1)%5]-tile[i]).conjugate())).sqrt() for i in range(5)]
 tests=[]
 for typ,(ae,le) in families.FAMILIES.items():
  for epsilon in(1,-1):
   for h in range(5):
    amap=[(h+epsilon*i)%5 for i in range(5)];smap=[(h+i)%5 if epsilon==1 else(h-i-1)%5 for i in range(5)]
    angleok=all(__import__('functools').reduce(lambda a,b:a*b,(angles[i]**c for c,i in zip(row,amap)),QQbar(1))==QQbar(1 if target==10 else-1) for row,target in ae)
    lengthok=all(sum(c*lengths[i] for c,i in zip(row,smap))==0 for row in le)
    tests.append({'type':typ,'epsilon':epsilon,'offset':h,'angle_equations_pass':angleok,'length_equations_pass':lengthok})
 records.append({'tile':name,'boundary_word':['q','H1','H2','H3','r'] if name=='P' else['r','H4','H5','H0','q'],
                 'vertices':[encode(z) for z in tile],'strict_convexity':True,'normalized_area':encode(area(tile)),
                 'family_tests':tests,'compatible_families':[t for t in tests if t['angle_equations_pass'] and t['length_equations_pass']]})
out={'domain':'one reviewed source H6 sample J=1/2+4/5w; one chord between native-side0/3 midpoints; exactly2 five-corner pieces and300 known-family relabelings',
     'source':[encode(z) for z in H],'cut_endpoints':[encode(q),encode(r)],'source_boundary_retained':True,
     'endpoint_distinct_ray_degree':3,'strict_source_cut_containment':True,'area_partition':True,'tiles':records,
     'scope':'local two-boundary-word module only; sourceP1/P2 resection and plane covering/globaltwo-class congruence/forcing absent'}
print(json.dumps(out,indent=2))
