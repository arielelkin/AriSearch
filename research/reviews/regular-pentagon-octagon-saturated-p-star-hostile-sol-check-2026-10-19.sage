# Independent QQbar reconstruction; source search is never imported.
from itertools import product, combinations
from collections import Counter
import json
exec(open('research/reviews/regular-pentagon-octagon-144-126-hostile-sol-check-2026-10-19.sage').read().split('raw=[]')[0])
from functools import lru_cache
raw_audit_pair=audit_pair
@lru_cache(None)
def cached_pair(p,q): return raw_audit_pair(list(p),list(q))
def audit_pair(p,q): return cached_pair(tuple(p),tuple(q))
P=[QQbar(0)]; step=QQbar(1)
for k in range(4):
 P.append(P[-1]+step); step*=z**4
assert P[-1]+step==0
Q=polygon('AAABBABB',(3,6)); word='AAABBABB'
def place(poly,e,a,b,flip):
 c,d=poly[e],poly[(e+1)%len(poly)]
 endpoints=(a,b) if flip else (b,a)
 origin,target=endpoints
 transform=(lambda x:x.conjugate()) if flip else (lambda x:x)
 multiplier=(target-origin)/transform(d-c)
 assert abs(multiplier)==1
 return [origin+multiplier*transform(v-c) for v in poly]
# Derive roles from root-side status rather than hard-code them.
pp={0,2}
roles={i:('A' if (i-1)%5 in pp else 'B')+('A' if (i+1)%5 in pp else 'B') for i in range(5) if i not in pp}
assert roles=={1:'AA',3:'AB',4:'BA'}
opts={}
for i,role in roles.items():
 opts[i]=[]
 for e in range(8):
  if e in (3,6):continue
  for flip in (False,True):
   ends=word[e]+word[(e+1)%8]
   if (ends if flip else ends[::-1])==role:
    opts[i].append((e,flip,place(Q,e,P[i],P[(i+1)%5],flip)))
assert all(len(v)==4 for v in opts.values())
fixed=[pent(P[i],P[(i+1)%5]) for i in (0,2)]
certificate=json.load(open('research/searches/regular-pentagon-octagon-saturated-p-star-sol-2026-10-19.json'))
seen=set(); counts=Counter()
for choices in product(*(opts[i] for i in (1,3,4))):
 key=tuple((int(c[0]),bool(c[1])) for c in choices); seen.add(key)
 tiles=[P]+fixed+[c[2] for c in choices]
 paircounts=Counter(audit_pair(a,b) for a,b in combinations(tiles,2))
 assert paircounts['identical']==0
 counts[tuple(sorted(paircounts.items()))]+=1
 ring=[1,3,2,4,5]
 for v in range(5):
  assert sum(P[v] in t for t in tiles)==3
  a,b=tiles[ring[(v-1)%5]],tiles[ring[v]]
  assert audit_pair(a,b)=='edge' and P[v] in set(a)&set(b)
  ends=list(set(a)&set(b)); length=abs(ends[0]-ends[1])
  assert length==(z+z.conjugate() if v==4 else 1)
recordkeys={tuple((int(e),bool(f)) for e,f in r['choices']) for r in certificate['branches']}
assert seen==recordkeys and len(seen)==len(certificate['branches'])==64
assert len(certificate['survivors'])==64 and all(not r['bad'] and not r['coincident'] for r in certificate['branches'])
print('Independent QQbar audit: 64/64 legal stars; certificate domain identical.')
print('Pair inventories:',counts)
