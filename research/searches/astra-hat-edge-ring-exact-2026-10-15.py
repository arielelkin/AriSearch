#!/usr/bin/env python3
"""Exact convex precursor only; seven pieces are NOT asserted two congruence classes."""
import importlib.util,json,sys
from collections import Counter
from sage.all import QuadraticField,AA,vector
K=QuadraticField(3,'r',embedding=AA(3).sqrt());r=K.gen()
sp=importlib.util.spec_from_file_location('hat','research/searches/source-decoration-hat-patch.py')
hat=importlib.util.module_from_spec(sp);sp.loader.exec_module(hat)
old=[vector(K,[K(x.a)+K(x.b)*r for x in p]) for p in hat.hat_outline]
H=[vector(K,[0,0])]
for i in range(13):
 d=old[(i+1)%13]-old[i];n=d.dot_product(d)
 H.append(H[-1]+d*(2/r if n==3 else 1))
assert H[-1]==H[0];H.pop()
W=(H[1]+H[2])/2;U=(H[5]+H[6])/2
arcs=[[H[0],H[1],W],[W,H[2],H[3],H[4]],[H[4],H[5],U],[U,H[6],H[7],H[8]],[H[8],H[9],H[10],H[11]],[H[11],H[12],H[0]]]
Z=[vector(K,[K(a)/1000,K(b)/1000]) for a,b in [(764,271),(637,-161),(1228,-479),(3095,-985),(2838,-429),(1655,973)]]
split='--split-center' in sys.argv
center=[Z]
if split:
 R=(Z[0]+Z[1])/2;S=(Z[3]+Z[4])/2
 center=[[R,Z[1],Z[2],Z[3],S],[S,Z[4],Z[5],Z[0],R]]
polys=center+[arcs[i]+[Z[(i+1)%6],Z[i]] for i in range(6)]
def det(v,w):return v[0]*w[1]-v[1]*w[0]
def area2(P):return sum(det(P[i],P[(i+1)%len(P)]) for i in range(len(P)))
mins=[]
for P in polys:
 vals=[det(P[(i+1)%len(P)]-P[i],P[j]-P[i]) for i in range(len(P)) for j in range(len(P)) if j not in (i,(i+1)%len(P))]
 assert all(x>0 for x in vals)
 mins.append(min(vals))
# Exact separating supporting lines for each of the21 convex pairs.
for i,P in enumerate(polys):
 for Q in polys[i+1:]:
  assert any(all(det(A[(j+1)%len(A)]-A[j],v-A[j])<=0 for v in B) for A,B in ((P,Q),(Q,P)) for j in range(len(A)))
# Oriented chain cancellation proves equality of winding functions, hence coverage.
chain=Counter()
vertices={tuple(v) for P in polys for v in P}
for P in polys:
 for a,b in zip(P,P[1:]+P[:1]):
  d=b-a;cuts=[]
  for vv in vertices:
   v=vector(K,vv);t=(v-a).dot_product(d)/d.dot_product(d)
   if det(d,v-a)==0 and 0<=t<=1:cuts.append((t,vv))
  cuts.sort()
  for (_,x),(_,y) in zip(cuts,cuts[1:]):chain[x,y]+=1
for a,b in list(chain):
 n=min(chain[a,b],chain[b,a]);chain[a,b]-=n;chain[b,a]-=n
chain=+chain
source=[H[0],H[1],W,*H[2:6],U,*H[6:]]
expected=Counter((tuple(a),tuple(b)) for a,b in zip(source,source[1:]+source[:1]))
assert chain==expected
assert sum(area2(P) for P in polys)==area2(H)
assert [len(P) for P in polys]==([5,5,5,6,5,6,6,5] if split else [6,5,6,5,6,6,5])
print(json.dumps({'status':'EXACT_PRECURSOR_INTERNAL_CHECK_NOT_TWO_CLASS','field':'Q(sqrt3),positive embedding','source_ratio_b':2,'ring_vertices':[[str(x) for x in p] for p in Z],'corner_counts':[len(P) for P in polys],'minimum_support_determinants':[str(x) for x in mins],'minimum_support_approx':[float(x) for x in mins],'pairwise_separation_checks':len(polys)*(len(polys)-1)//2,'split_center':split,'boundary_chain_and_area':'PASS'},indent=2))
