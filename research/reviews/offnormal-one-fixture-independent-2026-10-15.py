"""Independent exact check of ONE off-normal SAT-angle/coordinate fixture.
No producer imports or solver. Fraction angle checks; exact QQbar complex geometry.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import ast,json
from sage.all import QQbar,AA,QQ
ROOT=Path(__file__).resolve().parents[1]
angle=json.loads((ROOT/'certificates/offnormal-cap-h-angle-gate-2026-10-15.json').read_text())
geom=json.loads((ROOT/'certificates/offnormal-one-fixture-geometry-2026-10-15.json').read_text())
assert angle['status']=='sat'
H=tuple(map(F,angle['H']))
assert H==(36,156,144,156,72,156) and sum(H)==720
base={ast.literal_eval(k):F(v) for k,v in angle['base'].items()}
theta={ast.literal_eval(k):F(v) for k,v in angle['theta'].items()}
external={ast.literal_eval(k):F(v) for k,v in angle['external'].items()}
for mark in ('X','Y'):
 assert (base[mark,'tail'],base[mark,'head'])==(6,42)
 assert (theta[mark,'tail'],theta[mark,'head'])==(120,12)
 assert theta[mark,'tail']+theta[mark,'head']==180-base[mark,'tail']-base[mark,'head']
 for role in ('tail','head'):
  pair=tuple(external[mark,role,k] for k in (0,1))
  assert pair==((156,144) if role=='tail' else (156,36))
  assert sum(pair)==180+theta[mark,role]
  assert all(theta[mark,role]<value<180 for value in pair)
ARROWS={
 'thin':((0,1,'X'),(2,1,'X'),(2,3,'Y'),(0,3,'Y')),
 'thick':((0,1,'X'),(1,2,'Y'),(3,2,'Y'),(0,3,'X')),
}
contexts={}
for species,arrows in ARROWS.items():
 for parity in (0,1):
  for edge in range(4):
   if edge%2==parity:continue
   tail,head,mark=arrows[edge]
   for vertex in (edge,(edge+1)%4):
    outgoing=(vertex-1)%4 if vertex==edge else vertex
    ot,oh,om=arrows[outgoing]
    role='tail' if vertex==tail else 'head'
    otherrole='tail' if vertex==ot else 'head'
    source=(36,144)[vertex%2] if species=='thin' else (72,108)[vertex%2]
    alpha=source+base[mark,role]-base[om,otherrole]
    contexts[species,parity,edge,vertex]=(alpha,mark,role)
assert len(contexts)==16
seen=set()
for record in angle['aliases']:
 key=tuple(record[k] for k in ('species','parity','receiver','endpoint'))
 assert key in contexts and key not in seen
 seen.add(key)
 alpha,mark,role=contexts[key]
 start,bit=divmod(record['alias'],2)
 assert 0<=start<6
 step=1 if bit else -1
 word=tuple(H[(start+step*k)%6] for k in range(6))
 assert word[:3]==(alpha,external[mark,role,0],external[mark,role,1])
 assert word[3]==156 and F(record['alpha'])==alpha
 inner=360-alpha-theta[mark,role]-word[3]
 assert 0<inner<180 and all(inner<a<180 for a in word[4:])
 assert sum(word[4:])==180+inner
assert seen==set(contexts)

# Independent complex-coordinate reconstruction. z is exactly exp(pi*i/30).
z=QQbar.zeta(60);I=QQbar.gen()
assert I*I==-1
cs=lambda n:AA((z**n).real())
sn=lambda n:AA((z**n).imag())
cot=lambda n:cs(n)/sn(n)
h=1/(cot(1)+cot(7));u=h*cot(1);m=u+h*cot(9)
assert 0<u<m<1 and h>0
cross=lambda a,b:AA((a.conjugate()*b).imag())
dot=lambda a,b:AA((a.conjugate()*b).real())
def turn(a,b,c):return cross(b-a,c-b)
def strict(poly):
 vals=[cross(poly[(i+1)%len(poly)]-p,q-p) for i,p in enumerate(poly) for j,q in enumerate(poly) if j not in (i,(i+1)%len(poly))]
 return all(v>0 for v in vals) or all(v<0 for v in vals)
def cot_at(poly,k):
 a=poly[k-1]-poly[k];b=poly[(k+1)%len(poly)]-poly[k]
 den=abs(cross(a,b));assert den>0
 return dot(a,b)/den
T=QQbar(0);foot=QQbar(m);apex=QQbar(u)+I*h
assert cot_at((T,apex,foot),0)==cot(1)
assert cot_at((T,apex,foot),1)==cot(20)
assert cot_at((apex,QQbar(1),foot),0)==cot(2)

def area(poly):return abs(sum(cross(poly[i],poly[(i+1)%len(poly)]) for i in range(len(poly)))/2)
def apart(P,Q):
 for poly in (P,Q):
  for i,p in enumerate(poly):
   normal=I*(poly[(i+1)%len(poly)]-p)
   a=[dot(v,normal) for v in P];b=[dot(v,normal) for v in Q]
   if max(a)<=min(b) or max(b)<=min(a):return True
 return False
actual={};source_ok={}
for species,power in (('thin',6),('thick',12)):
 w=z**power
 vertices=(QQbar(0),QQbar(1),1+w,w)
 for parity in (0,1):
  donors={}
  for edge in range(4):
   if edge%2!=parity:continue
   tail,head,_=ARROWS[species][edge]
   along=vertices[(edge+1)%4]-vertices[edge]
   donors[edge]=vertices[tail]+u*(vertices[head]-vertices[tail])+I*h*along
  cells=[(vertices[e],vertices[(e+1)%4],p) for e,p in donors.items()]
  cells += [(vertices[e],vertices[(e+1)%4],donors[(e+1)%4],donors[(e-1)%4]) for e in range(4) if e%2!=parity]
  assert all(strict(P) for P in cells)
  assert all(apart(P,Q) for P,Q in combinations(cells,2))
  assert sum(area(P) for P in cells)==sn(power)
  assert all(cross(vertices[(e+1)%4]-vertices[e],v-vertices[e])>=0 for P in cells for v in P for e in range(4))
  source_ok[species,parity]=True
  for edge in range(4):
   if edge%2==parity:continue
   tail,head,mark=ARROWS[species][edge]
   along=vertices[(edge+1)%4]-vertices[edge]
   ext=vertices[tail]+u*(vertices[head]-vertices[tail])-I*h*along
   split=vertices[tail]+m*(vertices[head]-vertices[tail])
   p,q=donors[(edge-1)%4],donors[(edge+1)%4]
   assert strict((split,q,p))
   for endpoint,node in ((edge,p),((edge+1)%4,q)):
    poly=(vertices[endpoint],ext,split,node)
    valid=strict(poly)
    signs=[1 if turn(poly[k],poly[(k+1)%4],poly[(k+2)%4])>0 else -1 for k in range(4)]
    cotM=cot_at(poly,2)
    angleM=next((6*k for k in range(1,30) if cotM==cot(k)),None)
    alpha,Z,role=contexts[species,parity,edge,endpoint]
    required=360-alpha-theta[Z,role]-156
    actual[species,parity,edge,endpoint]=dict(strict_convex=valid,consecutive_turn_signs=signs,minor_M_ray_angle_matches_156=(cotM==cot(26)),minor_M_ray_angle_exact_six_degree_grid=angleM,required_internal_angle=int(required),actual_internal_matches_required=(cot_at(poly,3)==cot(int(required)//6)) if valid else None)
    if (species,parity,edge,endpoint)==('thin',0,1,1):
     delta=turn(poly[1],poly[2],poly[3])
     assert signs==[1,-1,1,1]
     assert cross(poly[1]-poly[0],poly[2]-poly[1])==h*(1-m)>0
     formula=h*(1-m)*(1+cs(6))+sn(6)*((u-m)*(1-u)-h*h)
     assert delta==formula and QQ(-3254)/10**6<delta<QQ(-3253)/10**6<0
assert len(actual)==16
assert sum(r['strict_convex'] for r in actual.values())==8
assert all(not r['minor_M_ray_angle_matches_156'] for r in actual.values() if r['strict_convex'])
assert actual['thick',0,3,0]['strict_convex']
assert actual['thick',0,3,0]['minor_M_ray_angle_exact_six_degree_grid']==108
assert len(geom['records'])==16
geometry_seen=set()
for r in geom['records']:
 key=tuple(r[k] for k in ('species','parity','receiver','endpoint'))
 assert key in actual and key not in geometry_seen
 geometry_seen.add(key)
 for k,v in actual[key].items():assert r[k]==v,(key,k,r[k],v)
assert geometry_seen==set(actual)
assert len(geom['source_partitions'])==4
assert {(r['species'],r['parity']) for r in geom['source_partitions']}==set(source_ok)
for r in geom['source_partitions']:assert r['strict_cells_disjoint_cover']==source_ok[r['species'],r['parity']]
assert geom['status']=='FAIL_THIS_ONE_ANGLE_WITNESS'
print('PASS:16 relaxed Fraction angle contexts;4 exact valid source partitions;8 strict and8 nonconvex receiving quads; explicit negative turn interval; strict M=108 mismatch. ONE fixture only.')
