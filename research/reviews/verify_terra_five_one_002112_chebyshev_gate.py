#!/usr/bin/env python3
"""No producer imports. Native directions rebuilt with Chebyshev recurrences;
all Bell6 coarsenings, algebraic cuts, signs and BB endpoints reconstructed.
"""
from sage.all import QQ,AA,PolynomialRing
from itertools import product
from pathlib import Path
from collections import Counter
import json
J=json.loads(Path('research/certificates/terra-five-one-002112-chebyshev-gate.json').read_text())
R=PolynomialRing(QQ,'t');t=R.gen()
def T(n,x):
 a,b=R(1),x
 if n==0:return a
 for _ in range(1,n):a,b=b,2*x*b-a
 return b
def U(n,x):
 a,b=R(1),2*x
 if n==0:return a
 for _ in range(1,n):a,b=b,2*x*b-a
 return b
def unit(n):
 return (T(abs(n),t), (1 if n>0 else -1)*U(abs(n)-1,t) if n else R(0))
A=[tuple(s*x for x in unit(n)) for n,s in zip((0,1,5,0,-5,-1),(1,1,-1,-1,-1,1))]
C=1-2*t*t
B=[(T(j,C),2*t*U(j-1,C) if j else R(0)) for j in range(6)]
def det(x,y):return x[0]*y[1]-x[1]*y[0]
D=det(B[1],B[4])
L=(AA(2)-AA(2).sqrt()).sqrt()/2;H=(AA(10)-2*AA(5).sqrt()).sqrt()/4

def decode(e):
 p=R(e['minpoly'].replace('x','t'));lo,hi=map(QQ,e['rational_interval'])
 rr=[x for x,m in p.roots(AA) if lo<=x<=hi]
 assert len(rr)==1
 return rr[0]
def parts(prefix=(0,)):
 if len(prefix)==6:yield prefix;return
 for v in range(max(prefix)+2):yield from parts(prefix+(v,))
# Ray equalities as graph connectivity; independent of producer DSU convention.
required=[]
for cc in product((0,1),(3,4),(2,5)):
 for reflect in product((False,True),repeat=3):
  rays=[(c,(c-1)%6) if rev else ((c-1)%6,c) for c,rev in zip(cc,reflect)]
  ed=[(rays[j][1],rays[(j+1)%3][0]) for j in range(3)]
  required.append(ed)
def eligible(p):return p[0]!=p[3] and any(all(p[a]==p[b] for a,b in ed) for ed in required)
assert len(required)==64
expected={p for p in parts() if eligible(p)}
assert expected=={tuple(r['partition']) for r in J['rows']}
def gcd(polys):
 g=R(0)
 for p in polys:g=g.gcd(p)
 return g.monic() if g else g

def roots(p):return [x for x,m in p.roots(AA) if L<x<H and x!=AA(1)/2] if p else []
def between(a,b):
 n=2
 while True:
  z=QQ((a*n).floor()+1)/n
  if a<z<b:return z
  n*=2
Cword=(0,0,2,1,1,2)
def other(j):
 c=j if Cword[j]==2 else (j+1)%6
 return (j-1)%6 if c==j else (j+1)%6
hist=Counter();counts=Counter();survpart=[]
for row in J['rows']:
 p=tuple(row['partition']);k=max(p)+1
 G=[tuple(sum(A[j][i] for j in range(6) if p[j]==c) for i in range(2)) for c in range(k)]
 minors=[det(G[i],G[j]) for i in range(k) for j in range(i+1,k)]
 assert any(minors)
 hist[k,2,k-2]+=1
 rankg=gcd(minors)
 assert rankg==R(row['rank_drop_polynomial']) and not roots(rankg)
 assert [[str(x)for x in c] for c in G]==row['grouped_columns']
 if k!=3:continue
 V=[det(G[1],G[2]),det(G[2],G[0]),det(G[0],G[1])];vg=gcd(V);V=[v//vg for v in V]
 assert V==list(map(R,row['kernel']))
 polys=V+[V[i]-V[j] for i in range(3) for j in range(i)]+[rankg]
 fans=[]
 for ch in product((2,4),(1,5),(1,5),(2,4)):
  native=[None]*6
  for j,a in zip((0,2,3,5),ch):native[j]=V[p[a]]
  rhs=tuple(-sum(native[j]*B[j][i] for j in (0,2,3,5)) for i in range(2))
  bn=(det(rhs,B[4]),det(B[1],rhs))
  fans.append((ch,bn));polys.extend([*bn,bn[0]-bn[1]])
 cuts=sorted(set([L,H,AA(1)/2]+[z for f in polys for z in roots(f)]))
 assert cuts==[decode(e)for e in row['exact_critical_cuts']]
 tests=[(str(cuts[i]),str(cuts[i+1]),between(cuts[i],cuts[i+1]))for i in range(len(cuts)-1)]
 tests.extend((str(z),str(z),z)for z in cuts if L<z<H and z!=AA(1)/2)
 actual=[]
 for lo,hi,z in tests:
  vals=[v(z)for v in V];sg=1 if min(vals)>0 else -1 if max(vals)<0 else 0
  if not sg or len(set(vals))!=3 or rankg(z)==0:continue
  live=[ch for ch,bn in fans if all(sg*f(z)/D(z)>0 for f in bn)]
  bb=[]
  for ch,bn in fans:
   if ch not in live:continue
   options=[(q,qn) for q,qn in fans if any(all(p[a]==p[b] for a,b in zip(q,form)) for form in (ch,ch[::-1]))]
   edgeok=[]
   for e,slots in enumerate(((0,1),(2,3))):
    ok=[]
    for q,qn in options:
     for f,partner in enumerate(((0,1),(2,3))):
      if bn[e](z)!=qn[f](z):continue
      for flip in (False,True):
       target=partner[::-1] if flip else partner
       if all(q[b]==other(ch[a]) or (p[1]==p[5] and p[2]==p[4] and q[b]==(-other(ch[a]))%6) for a,b in zip(slots,target)):
        ok.append(dict(partner_native_choices=list(q),partner_BB_side=(1,4)[f],reverse_endpoints=flip))
    edgeok.append(ok)
   if all(edgeok):bb.append(dict(native_choices=list(ch),links=edgeok))
  counts['A_cells']+=1;counts['AB_cells']+=bool(live);counts['ABB_cells']+=bool(bb)
  actual.append((lo,hi,z,[list(ch)for ch in live],bb))
 assert len(actual)==len(row['positive_cells'])
 for x,c in zip(actual,row['positive_cells']):
  assert x[0]==c['lower'] and x[1]==c['upper'] and x[2]==decode(c['sample_exact'])
  assert x[3]==c['B_positive_fans'] and x[4]==c['BB_endpoint_survivors']
 if any(x[4]for x in actual):survpart.append(p)
assert dict(counts)==J['rank2_k3_counts']
assert hist==Counter({(2,2,0):12,(3,2,1):26,(4,2,2):4})
print('PASS42 partitions; no allowed rankdrops; exact counts',dict(counts),'ABB-positive partitions',len(survpart))
