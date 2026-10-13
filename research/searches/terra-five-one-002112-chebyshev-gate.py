#!/usr/bin/env python3
"""Finite domain: all203 Bell6 partitions, nonH1, admitting one of64 AAA stars.
Outcomes: empty positive A closure excludes stratum; negative B closure excludes
mixed saturated field; surviving A/B closure requires exact BB endpoint gate.
No extension/aperiodicity conclusion follows from a positive result.
"""
from sage.all import QQ,AA,RIF,PolynomialRing,matrix
from itertools import product
from collections import Counter
from pathlib import Path
import json
R=PolynomialRing(QQ,"t");t=R.gen()
P=16*t**5-20*t**3+5*t;Q=16*t**4-12*t**2+1
cols=[(1,0),(t,1),(-P,-Q),(-1,0),(-P,Q),(t,-1)]
L=(AA(2)-AA(2).sqrt()).sqrt()/2
H=(AA(10)-2*AA(5).sqrt()).sqrt()/4
reqs=[]
for corners in product((0,1),(3,4),(2,5)):
 for signs in product((1,-1),repeat=3):
  pa=list(range(6))
  def find(i):
   while pa[i]!=i:i=pa[i]
   return i
  arms=[((i-1)%6,i)[::s] for i,s in zip(corners,signs)]
  for j in range(3):pa[find(arms[j][1])]=find(arms[(j+1)%3][0])
  seen={};p=tuple(seen.setdefault(find(i),len(seen)) for i in range(6))
  reqs.append(p)
def partitions(prefix=(0,)):
 if len(prefix)==6:yield prefix;return
 for i in range(max(prefix)+2):yield from partitions(prefix+(i,))
def refines(a,b):return all(a[i]!=a[j] or b[i]==b[j] for i in range(6) for j in range(i))
def gcds(polys):
 ps=[R(p) for p in polys if p]
 if not ps:return R(0)
 g=ps[0]
 for p in ps[1:]:g=g.gcd(p)
 return g.monic()
def roots(p):return [v for v,m in p.roots(AA) if L<v<H and v!=AA(1)/2] if p else []
def exact_number(x):
 x=AA(x)
 interval=x.interval(RIF)
 return dict(minpoly=str(x.minpoly()),rational_interval=[str(interval.lower().exact_rational()),str(interval.upper().exact_rational())])
def rational_between(a,b):
 n=2
 while True:
  q=QQ((a*n).floor()+1)/n
  if a<q<b:return q
  n*=2
U7=128*t**7-192*t**5+80*t**3-8*t
S1=2*t;S2=4*t-8*t**3;D=32*t**5-32*t**3+6*t
rows=[];hist=Counter();positive=Counter()
for part in partitions():
 if part[0]==part[3] or not any(refines(a,part) for a in reqs):continue
 k=max(part)+1
 cs=[tuple(sum(R(cols[j][i]) for j in range(6) if part[j]==c) for i in range(2)) for c in range(k)]
 minors=[cs[i][0]*cs[j][1]-cs[i][1]*cs[j][0] for i in range(k) for j in range(i+1,k)]
 rank=2 if any(minors) else 1 if any(x for c in cs for x in c) else 0
 hist[k,rank,k-rank]+=1
 g=gcds(minors if rank==2 else [x for c in cs for x in c])
 row=dict(partition=part,k=k,generic_rank=rank,kernel_dimension=k-rank,grouped_columns=[[str(x) for x in c] for c in cs],rank_drop_polynomial=str(g),rank_drop_roots=[str(x) for x in roots(g)])
 if rank==2 and k==3:
  def det(a,b):return a[0]*b[1]-a[1]*b[0]
  v=[det(cs[1],cs[2]),det(cs[2],cs[0]),det(cs[0],cs[1])]
  vg=gcds(v);v=[x//vg for x in v]
  pols=v+[v[i]-v[j] for i in range(3) for j in range(i)]+[g]
  fans=[]
  for choice in product((2,4),(1,5),(1,5),(2,4)):
   m0,m2,m3,m5=[v[part[j]] for j in choice]
   pn=m0*U7-m2*S2-m3*S1+m5*S1
   qn=m0*S1-m2*S1-m3*S2+m5*U7
   fans.append((choice,pn,qn));pols.extend([pn,qn,pn-qn])
  rr=sorted(set([L,H,AA(1)/2]+[r for p in pols for r in roots(p)]))
  def exposed(j):return {2:1,4:5,1:2,5:4}[j]
  def bb_gate(choice,pn,qn,sample):
   # Same polygon B in canonical order; alternative A indices may realize
   # identical B side lengths when actual A classes merge.
   partners=[(ch,p,q) for ch,p,q in fans if any(all(part[a]==part[b] for a,b in zip(ch,pattern)) for pattern in (choice,choice[::-1]))]
   slots=((0,1),(2,3));bb=(pn,qn)
   links=[]
   for edge in range(2):
    live=[]
    for ch,pp,qq in partners:
     for pe in range(2):
      if (bb[edge]-(pp,qq)[pe])(sample)!=0:continue
      for flip in (False,True):
       target=slots[pe][::-1] if flip else slots[pe]
       if all((ch[j]==exposed(choice[i]) or (part[1]==part[5] and part[2]==part[4] and ch[j]==(-exposed(choice[i]))%6)) for i,j in zip(slots[edge],target)):
        live.append(dict(partner_native_choices=list(ch),partner_BB_side=(1,4)[pe],reverse_endpoints=flip))
    links.append(live)
   return links
  cells=[]
  # Include algebraic critical points: A classes may remain distinct at B zeros
  tests=[(str(rr[i]),str(rr[i+1]),rational_between(rr[i],rr[i+1])) for i in range(len(rr)-1)]
  tests += [(str(x),str(x),x) for x in rr if L<x<H and x!=AA(1)/2]
  for lo,hi,s in tests:
   vals=[x(s) for x in v]
   sign=1 if min(vals)>0 else -1 if max(vals)<0 else 0
   if not sign or len(set(vals))!=3 or g(s)==0:continue
   live=[list(ch) for ch,pn,qn in fans if sign*pn(s)/D(s)>0 and sign*qn(s)/D(s)>0]
   bb_live=[]
   for ch,pn,qn in fans:
    if list(ch) not in live:continue
    links=bb_gate(ch,pn,qn,s)
    if all(links):bb_live.append(dict(native_choices=list(ch),links=links))
   cells.append(dict(lower=lo,upper=hi,sample=str(s),sample_exact=exact_number(s),A_positive=True,B_positive_fans=live,BB_endpoint_survivors=bb_live))
   positive['ABB_cells']+=bool(bb_live)
   positive['A_cells']+=1;positive['AB_cells']+=bool(live)
  row.update(kernel=[str(x) for x in v],exact_critical_cuts=[exact_number(x) for x in rr],positive_cells=cells)
 rows.append(row)
out=dict(scope=__doc__,formal_nonH1_required_partition_count=len(set(p for p in reqs if p[0]!=p[3])),actual_partition_count=len(rows),group_counts=[dict(k=k,rank=r,kernel_dimension=d,count=n) for (k,r,d),n in sorted(hist.items())],rank2_k3_counts=dict(positive),rows=rows)
Path('research/certificates/terra-five-one-002112-chebyshev-gate.json').write_text(json.dumps(out,indent=2)+'\n')
print('partition counts',out['group_counts'],'total',len(rows),flush=True)
print('rank2 k3 counts',dict(positive),flush=True)
for row in rows:
 if row.get('rank_drop_roots'):print('RANKDROP',row['partition'],row['rank_drop_roots'])
 for cell in row.get('positive_cells',[]):
  if cell['BB_endpoint_survivors']:pass
