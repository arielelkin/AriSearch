# Independent QQbar checker; no import of candidate search.
from itertools import combinations
from collections import Counter
import json
z=QQbar.zeta(20)
def det(a,b): return a.real()*b.imag()-a.imag()*b.real()
def canonical(w): return min(v[k:]+v[:k] for v in (w,w[::-1]) for k in range(8))
def polygon(w,edges):
 d=[QQbar(1)]
 for k in range(1,8): d.append(d[-1]*z**(2 if w[k]=='A' else 3))
 s=sum(d[k] for k in range(8) if k not in edges)
 u,v=[d[k] for k in edges]; D=det(u,v)
 if D==0:
  assert s==0 and v==-u
  return None
 x,y=-det(s,v)/D,-det(u,s)/D
 assert x>0 and y>0 and x==y and x==z+z.conjugate()
 length=[x if k in edges else 1 for k in range(8)]
 p=[QQbar(0)]
 for k in range(8): p.append(p[-1]+length[k]*d[k])
 assert p.pop()==0
 assert all(det(p[(k+1)%8]-p[k],p[j]-p[k])>0 for k in range(8) for j in range(8) if j not in (k,(k+1)%8))
 return p
def pent(a,b):
 p=[a]; step=b-a
 for k in range(4): p.append(p[-1]+step); step*=z**(-4)
 assert p[-1]+step==a
 return p
def interior_hit(p,q):
 for r in (p,q):
  for a,b in zip(r,r[1:]+r[:1]):
   n=b-a
   pi=[det(n,t) for t in p]; qi=[det(n,t) for t in q]
   if max(pi)<=min(qi) or max(qi)<=min(pi): return False
 return True
def in_open_edge(t,a,b):
 return det(b-a,t-a)==0 and 0<((t-a)/(b-a)).real()<1
def audit_pair(p,q):
 if set(p)==set(q): return 'identical'
 assert not interior_hit(p,q)
 # Unintended partial edges / T junctions would defeat unrestricted-contact claims.
 assert not any(in_open_edge(t,a,b) for r,s in ((p,q),(q,p)) for t in r for a,b in zip(s,s[1:]+s[:1]))
 common=set(p)&set(q)
 assert len(common)<=2
 if len(common)==2:
  assert any(set((a,b))==common for a,b in zip(p,p[1:]+p[:1]))
  assert any(set((a,b))==common for a,b in zip(q,q[1:]+q[:1]))
 return 'edge' if len(common)==2 else ('vertex' if common else 'disjoint')
raw=[]; representatives=set()
for bs in combinations(range(8),4):
 w=''.join('B' if k in bs else 'A' for k in range(8))
 for ee in combinations(range(8),2):
  covered=[k for e in ee for k in (e,(e+1)%8)]
  if len(set(covered))!=4 or set(covered)!=set(bs): continue
  raw.append((w,ee)); polygon(w,ee)
  if canonical(w)==w: representatives.add((w,ee))
assert representatives=={('AABBAABB',(2,6)),('AAABBABB',(3,6)),('AAAABBBB',(4,6))}
result={'labeled_word_matching_pairs':len(raw),'representatives':[],'arithmetic':'QQbar with certified real algebraic comparisons'}
for w,ee in sorted(representatives):
 p=polygon(w,ee)
 if p is None: continue
 ns={k:pent(p[k],p[(k+1)%8]) for k in range(8) if k not in ee}
 base=[p]+list(ns.values())
 base_counts=Counter(audit_pair(a,b) for a,b in combinations(base,2))
 for k in range(8):
  if w[k]=='A':
   common=set(ns[(k-1)%8])&set(ns[k]); assert len(common)==2
   a,b=list(common); assert abs(a-b)==1
 joins=[]
 for target in ee:
  a,b=p[target],p[(target+1)%8]
  for source in ee:
   c,d=p[source],p[(source+1)%8]
   for reflected in (False,True):
    if reflected:
     multiplier=(b-a)/(d-c).conjugate()
     moved=[[a+multiplier*(t-c).conjugate() for t in r] for r in base]
    else:
     multiplier=(a-b)/(d-c)
     moved=[[b+multiplier*(t-c) for t in r] for r in base]
    assert abs(multiplier)==1
    counts=Counter(audit_pair(r,s) for r in base for s in moved)
    joins.append({'target':target,'source':source,'reflected':reflected,'cross_patch_pair_counts':dict(counts)})
 result['representatives'].append({'word':w,'base_pair_counts':dict(base_counts),'joins':joins})
print(json.dumps(result,indent=2))
