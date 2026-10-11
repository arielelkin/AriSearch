"""Fresh reduced-coordinate native notch audit, without producer imports."""
import json
from itertools import product
from sage.all import QuadraticField, AA, matrix, vector
K=QuadraticField(3,'w',embedding=AA(3).sqrt());w=K.gen()
# Free physical coordinates s,b,c,A,C; solve both native closure equations.
z=[vector(K,[int(i==j) for j in range(5)]) for i in range(5)]
s,b,c,A,C=z
d=s+(b-c)/w;B=C+w*(s-A)
physical=[s,b,c,d,A,B,C,s]
physical += [w*c+d-2*s,w*C+s-2*A]
perp=(1,0,3,2,5,4,7,6)
rawcorners=((0,8),(1,2),(3,8),(4,9),(5,6),(7,9))
D=json.load(open('research/certificates/partial-contact-cairo-one-shared-event-flats.json'))
for fid,host,notch,filler in ((223,0,2,0),(638,0,2,0),(259,1,3,5),(366,1,3,5)):
 r=next(t for t in D['records'] if t['flat_id']==fid)
 constraints=[sum((K(v)*physical[j] for j,v in enumerate(row)),vector(K,5)) for row in r['constraint_rows']]
 kernel=matrix(K,constraints).right_kernel().basis()
 assert len(kernel)==2
 vals=[tuple(f.dot_product(t) for t in kernel) for f in physical]
 add=lambda i,j:tuple(x+y for x,y in zip(vals[i],vals[j]))
 events=[(i,j,add(i,j)) for i,j in product(range(8),repeat=2) if vals[perp[i]]==vals[perp[j]]]
 # All generic private-core event exclusions follow as identities of forms.
 core=(2,3) if host==0 else (4,5)
 for bank in core:
  target=tuple(2*x for x in vals[bank])
  assert target!=add(1,6) and target!=vals[8] and target!=vals[9]
 assert vals[8+host]==tuple(2*x for x in vals[0])
 totals=[{T for i,j,T in events if i==a or j==a} for a in range(8)]
 def matches(i,j):
  if i<8 and j<8:return vals[i]==vals[j] or bool(totals[i]&totals[j])
  if i>=8 and j>=8:return vals[i]==vals[j]
  if i>=8:i,j=j,i
  return vals[j] in totals[i]
 # Ordered triples with fixed notch copies; no author's unordered inventory.
 candidates=set()
 for f in range(6):
  for order in ((notch,notch,f),(notch,f,notch),(f,notch,notch)):
   for bits in product((0,1),repeat=3):
    sectors=[rawcorners[k][::(-1 if flip else 1)] for k,flip in zip(order,bits)]
    if all(matches(sectors[j][1],sectors[(j+1)%3][0]) for j in range(3)):candidates.add(f)
 assert candidates=={filler},(fid,candidates)
 # Private perpendicular bank at the only filler has precisely its own slot.
 perpendicular=1 if host==0 else 6
 assert [i for i in range(8) if vals[i]==vals[perpendicular]]==[perpendicular]
 print('PASS',fid,'forced native core, sole notch filler',filler,'private whole perpendicular mate')
print('PASS four relative-open strata; geometry uses independently reviewed full-interval original-pentagon overlap, not a macro assumption about the other species')
