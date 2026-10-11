"""Reconstruct native notch inventories for four exact single-core flats."""
import json
from itertools import combinations_with_replacement,product
from sage.all import QuadraticField,matrix,vector
K=QuadraticField(3,"w");w=K.gen();u=[vector(K,[int(i==j) for j in range(8)]) for i in range(8)]
other=(1,0,3,2,5,4,7,6);corners=((0,8),(1,2),(3,8),(4,9),(5,6),(7,9))
E=-2*u[0]+w*u[2]+u[3];F=-2*u[4]+w*u[6]+u[7];cross=u[1]+u[6]
cert=json.load(open("research/certificates/partial-contact-cairo-one-shared-event-flats.json"))
for number,H in((223,0),(638,0),(259,1),(366,1)):
 r=next(x for x in cert["records"] if x["flat_id"]==number)
 ns=matrix(K,[[K(t) for t in row] for row in r["constraint_rows"]]).right_kernel().basis();q=lambda v:tuple(v.dot_product(z) for z in ns)
 arms=[q(z) for z in u];es=[q(E),q(F)];core=(2,3) if H==0 else(4,5)
 assert all(any(q(L-2*u[i])) for L in(cross,E,F) for i in core)
 assert es[H]==q(2*u[0])
 sums=[{q(u[i]+u[j]) for j in range(8) if arms[other[i]]==arms[other[j]]} for i in range(8)]
 compat={(i,j) for i,j in product(range(8),repeat=2) if arms[i]==arms[j] or sums[i]&sums[j]}
 for h,g in enumerate(es):
  for i in range(8):
   if g in sums[i]:compat.add((8+h,i));compat.add((i,8+h))
  for k,f in enumerate(es):
   if f==g:compat.add((8+h,8+k))
 notch=2 if H==0 else 3;expected=0 if H==0 else 5;fillers=[]
 for i in range(6):
  trip=(notch,notch,i)
  if any(all((banks[j][1],banks[(j+1)%3][0]) in compat for j in range(3)) for signs in product((0,1),repeat=3) for banks in[[corners[t] if not flip else corners[t][::-1] for t,flip in zip(trip,signs)]]):fillers.append(i)
 assert fillers==[expected]
 print("PASS",number,"forced core",core,"only notch filler",expected)
