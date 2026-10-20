# Exact one-saturated-P gate; SageMath, no numerical predicates.
import itertools,json
from pathlib import Path
K=CyclotomicField(20);z=K.gen();I=z**5
from functools import lru_cache
@lru_cache(None)
def sgn(x):return QQbar(x).real().sign()
def cross(a,b):return (a.conjugate()*b-a*b.conjugate())/(2*I)
def overlap(p,q):
 for poly,other in ((p,q),(q,p)):
  orientation=sgn(sum(cross(a,b) for a,b in zip(poly,poly[1:]+poly[:1])))
  for a,b in zip(poly,poly[1:]+poly[:1]):
   v=[orientation*cross(b-a,x-a) for x in other]
   if all(sgn(x)<=0 for x in v):return False
 return True
def bad_contact(p,q):
 # A boundary vertex in an open edge is forbidden by reviewed no-T lemma.
 for poly,other in ((p,q),(q,p)):
  for a,b in zip(poly,poly[1:]+poly[:1]):
   for v in other:
    if cross(b-a,v-a)==0:
     t=(v-a)/(b-a)
     if t==t.conjugate() and sgn(t)>0 and sgn(1-t)>0:return True
 return False
def attach(poly,si,a,b,reflect):
 c,d=poly[si],poly[(si+1)%len(poly)]
 if reflect:
  f=lambda v:a+(b-a)/(d-c).conjugate()*(v-c).conjugate()
 else:
  f=lambda v:b+(a-b)/(d-c)*(v-c)
 return [f(v) for v in poly]
P=[K(0)];d=K(1)
for j in range(4):P.append(P[-1]+d);d*=z**4
assert P[-1]+d==0
word='AAABBABB';L=2*z-z**3+z**5-z**7
Q=[K(0)];d=K(1)
for i in range(7):
 Q.append(Q[-1]+(L if i in (3,6) else 1)*d)
 d*=z**(2 if word[i+1]=='A' else 3)
assert Q[-1]+d==0
PP=[attach(P,0,P[i],P[(i+1)%5],False) for i in (0,2)]
roles={1:'AA',3:'AB',4:'BA'};options={}
for i,role in roles.items():
 options[i]=[]
 for e in (0,1,2,4,5,7):
  for ref in (False,True):
   # reflection maps source start to target start; rotation reverses it.
   pair=word[e]+word[(e+1)%8]
   if (pair if ref else pair[::-1])!=role:continue
   poly=attach(Q,e,P[i],P[(i+1)%5],ref)
   options[i].append((e,ref,poly))
records=[]
for choices in itertools.product(*(options[i] for i in (1,3,4))):
 tiles=[P]+PP+[c[2] for c in choices]
 names=['P','PP0','PP2','Q1','Q3','Q4'];bad=[];coincident=[];contacts=[]
 for i,j in itertools.combinations(range(6),2):
  p,q=tiles[i],tiles[j]
  if set(p)==set(q):coincident.append([names[i],names[j]]);continue
  if overlap(p,q):bad.append([names[i],names[j],'interior overlap'])
  elif bad_contact(p,q):bad.append([names[i],names[j],'partial contact'])
  common=set(p)&set(q)
  if common:contacts.append([names[i],names[j],len(common)])
 # Exact required whole edges: all five vertex stars around P.
 stars=[]
 for v in range(5):
  incident=[k for k,t in enumerate(tiles) if P[v] in t]
  stars.append([names[k] for k in incident])
  if len(incident)!=3:bad.append(['vertex',v,'wrong corner multiplicity'])
 # adjacent external neighbors share the required full edge at each root vertex
 ring=[1,3,2,4,5] # neighbor across root sides 0..4
 for v in range(5):
  a,b=tiles[ring[(v-1)%5]],tiles[ring[v]]
  common=set(a)&set(b)
  if len(common)!=2:bad.append(['vertex',v,'missing full neighbor edge'])
 records.append(dict(choices=[[c[0],bool(c[1])] for c in choices],bad=bad,coincident=coincident,contacts=contacts,stars=stars))
out=dict(field='CyclotomicField(20), distinguished z=exp(2pi*i/20)',pp_sides=[0,2],pq_sides=[1,3,4],options={str(k):[[e,bool(r)] for e,r,p in v] for k,v in options.items()},total=len(records),survivors=[r for r in records if not r['bad']],branches=records,sage_version=version())
path=Path('research/searches/regular-pentagon-octagon-saturated-p-star-sol-2026-10-19.json');path.write_text(json.dumps(out,indent=2,default=int)+'\n')
print('options',out['options'],'total',out['total'],'survivors',len(out['survivors']))
for r in out['survivors']:print(r['choices'],r['coincident'])
