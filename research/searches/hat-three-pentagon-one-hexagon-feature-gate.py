#!/usr/bin/env python3
"""Exact changed hat cut: convex feature first, then finite side-inventory gate."""
import argparse, importlib.util, itertools, json
from pathlib import Path
from sage.all import AA, QQ, PolynomialRing
sp=importlib.util.spec_from_file_location('geometry',Path('research/reviews/check_hat_eight_kite_convex_clusters.py'))
g=importlib.util.module_from_spec(sp);sp.loader.exec_module(g)
K,r=g.K,g.r
R=PolynomialRing(K,'b,u,v');b,u,v=R.gens()
H=[(0,0),(-r*b/2,-b/2),(-r*b/2+QQ(1)/2,-b/2-r/2),(-r*b/2+QQ(5)/2,-b/2-r/2),(-r*b/2+3,-b/2),(3,-b),(r*b/2+3,-b/2),(r*b/2+QQ(5)/2,-b/2+r/2),(r*b/2+QQ(3)/2,-b/2+r/2),(r*b/2+QQ(3)/2,b/2+r/2),(QQ(3)/2,b+r/2),(1,b),(0,b)]
H=[tuple(map(R,p)) for p in H];V=(u,v)
P={'P6':[H[i] for i in (0,1,2,3,4)],'P9':[H[0],H[4],V,H[11],H[12]],'P48':[H[i] for i in (4,5,6,7,8)]+[V],'P192':[V]+[H[i] for i in (8,9,10,11)]}
def sub(a,z):return tuple(x-y for x,y in zip(a,z))
def cross(a,z):return a[0]*z[1]-a[1]*z[0]
def dist(a,z):return sum(t*t for t in sub(a,z))
def convex(A):
 return all(cross(sub(A[(i+1)%len(A)],A[i]),sub(z,A[i]))>0 for i in range(len(A)) for j,z in enumerate(A) if j not in(i,(i+1)%len(A)))
def evaluate(A,bb,uu,vv):return [tuple(AA(x(bb,uu,vv)) for x in p) for p in A]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
 # Strict supporting inequalities, rather than local turns alone.
 support={name:[str(cross(sub(A[(i+1)%len(A)],A[i]),sub(z,A[i]))) for i in range(len(A)) for j,z in enumerate(A) if j not in(i,(i+1)%len(A))] for name,A in P.items()}
 sample={name:[tuple(K(x(r,2,-r/10)) for x in p) for p in A] for name,A in P.items()}
 assert all(convex(A) for A in sample.values())
 assert all(g.area2(g.clip(A,B))==0 for A,B in itertools.combinations(sample.values(),2))
 source=[tuple(K(x(r,2,-r/10)) for x in p) for p in H]
 assert g.same(g.boundary(list(sample.values())),g.simplify(source))
 # P6 has squared lengths b²,1,4,1,L². P192 contains b² twice.
 # Hence b=1,2 or sqrt3 (L²=b² requires b=sqrt3).
 # P9 contains the L,1,b sides, so its two variable sides must be 1,2.
 rows=[];survivors=[]
 S=PolynomialRing(K,'x,y');x,y=S.gens()
 for bb in (K(1),K(2),r):
  h4=tuple(K(t(bb,0,0)) for t in H[4]);h11=(K(1),bb)
  for l4,l11 in ((1,4),(4,1)):
   I=S.ideal([(x-h4[0])**2+(y-h4[1])**2-l4,(x-h11[0])**2+(y-h11[1])**2-l11])
   assert I.dimension()<=0
   sols=I.variety(AA) if I.dimension()==0 else []
   row={'b':str(bb),'squared_Vh4':l4,'squared_Vh11':l11,'real_points':[]}
   for sol in sols:
    uu,vv=sol[x],sol[y];polys={n:evaluate(A,bb,uu,vv) for n,A in P.items()}
    strict=all(convex(A) for A in polys.values())
    congruent=g.congruent(polys['P6'],polys['P9']) and g.congruent(polys['P6'],polys['P192'])
    failures=[]
    for name,A in polys.items():
     for i in range(len(A)):
      for j,z in enumerate(A):
       if j in(i,(i+1)%len(A)):continue
       value=cross(sub(A[(i+1)%len(A)],A[i]),sub(z,A[i]))
       if value<=0:failures.append({'polygon':name,'edge_start':i,'other_vertex':j,'support':str(value),'minpoly':str(value.minpoly())})
    assert failures # Even these weaker common side-inventory conditions fail.
    rec={'u':str(uu),'v':str(vv),'u_minpoly':str(uu.minpoly()),'v_minpoly':str(vv.minpoly()),'all_strict_convex':strict,'all_pentagons_congruent':congruent,'failed_supports':failures}
    row['real_points'].append(rec)
    if strict and congruent:survivors.append({'b':str(bb),**rec})
   rows.append(row)
 out={'scope':'Changed four-piece hat cut, three strictly convex pentagons and one strictly convex hexagon. Two shape classes require all three pentagons congruent. No arbitrary source cut or unrestricted tiling recognition theorem.','polygons':{n:[[str(z) for z in p] for p in A] for n,A in P.items()},'strict_support_inequalities':support,'strict_partition_sample':['sqrt3','2','-sqrt3/10'],'sample_polygons':{n:[[str(z) for z in p] for p in A] for n,A in sample.items()},'sample_partition_checked':True,'necessary_b_values':['1','2','sqrt3'],'circle_cases':rows,'strict_two_class_survivors':survivors}
 Path(args.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'strict_partition_sample':True,'circle_cases':len(rows),'real_points':sum(len(z['real_points']) for z in rows),'survivors':survivors}))
if __name__=='__main__':main()
