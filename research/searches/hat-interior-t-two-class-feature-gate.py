#!/usr/bin/env python3
"""Four convex source pieces with a genuine interior T contact; exact cheap gate."""
import argparse,itertools,json,runpy
from pathlib import Path
from sage.all import AA
d=runpy.run_path('research/searches/hat-three-pentagon-one-hexagon-feature-gate.py')
K,r,R,b,u,v,H,g=d['K'],d['r'],d['R'],d['b'],d['u'],d['v'],d['H'],d['g']
V=(u,v);W=tuple((H[4][j]+V[j])/2 for j in(0,1))
P={'P0':H[:5]+[W],'P1':H[4:9]+[V],'P2':[V]+H[8:12],'P3':[H[0],W,V,H[11],H[12]]}
L=d['dist'](H[4],V);G=d['dist'](H[8],V);F=d['dist'](H[0],W)
def polygons(vals):return {n:[tuple(AA(z(*vals)) for z in p) for p in A] for n,A in P.items()}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
 sample={n:[tuple(K(z(1,K(9)/5,0)) for z in p) for p in A] for n,A in P.items()}
 assert all(d['convex'](A) for A in sample.values())
 assert all(g.area2(g.clip(A,B))==0 for A,B in itertools.combinations(sample.values(),2))
 h=[tuple(K(z(1,K(9)/5,0)) for z in p) for p in H]
 assert g.same(g.boundary(list(sample.values())),g.simplify(h))
 rows=[];survivors=[]
 for name,equations in [('A',[b-1,L-4,F-G]),('B',[L-4,G-1,F-b*b])]:
  I=R.ideal(equations);assert I.dimension()==0
  row={'branch':name,'groebner_basis':[str(z) for z in I.groebner_basis()],'real_points':[]}
  for sol in I.variety(AA):
   vals=tuple(sol[z] for z in(b,u,v));polys=polygons(vals)
   strict=vals[0]>0 and all(d['convex'](A) for A in polys.values())
   congruent=g.congruent(polys['P0'],polys['P1']) and g.congruent(polys['P2'],polys['P3'])
   failures=[]
   for n,A in polys.items():
    for i in range(len(A)):
     for j,z in enumerate(A):
      if j in(i,(i+1)%len(A)):continue
      val=d['cross'](d['sub'](A[(i+1)%len(A)],A[i]),d['sub'](z,A[i]))
      if val<=0:failures.append({'polygon':n,'edge_start':i,'other_vertex':j,'value':str(val),'minpoly':str(val.minpoly())})
   rec={'b_u_v':[str(z) for z in vals],'minpolys':[str(z.minpoly()) for z in vals],'b_positive':vals[0]>0,'strict_convex':strict,'both_congruences':congruent,'failed_supports':failures}
   row['real_points'].append(rec)
   if strict and congruent:survivors.append(rec)
  rows.append(row)
 out={'scope':'Specific four-piece hat cut with W strictly between h4 and V; W is a genuine flat interior contact on P1. Side-inventory necessity forces W midpoint before this exact gate. No arbitrary compiler or unrestricted recognition claim.','sample_b_u_v':['1','9/5','0'],'sample_partition_verified':True,'sample_polygons':{n:[[str(z) for z in p] for p in A] for n,A in sample.items()},'polygons_at_forced_midpoint':{n:[[str(z) for z in p] for p in A] for n,A in P.items()},'necessary_reduction':'s=1/2, L=2 and [(b=1,F=G) or (G=1,F=b)] where L,F,G are actual lengths','branches':rows,'strict_two_class_survivors':survivors}
 Path(args.output).write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({'sample_partition':True,'branch_points':[len(z['real_points']) for z in rows],'strict_points':[sum(z['strict_convex'] for z in q['real_points']) for q in rows],'survivors':survivors}))
if __name__=='__main__':main()
