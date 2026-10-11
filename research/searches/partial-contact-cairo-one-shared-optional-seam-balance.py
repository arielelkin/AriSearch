"""Necessary finite optional-subdivision seam LP on reviewed sole-Pa/Qd flats.
Normal replay is read-only. All whole sides remain optional. Residual pieces
without a120 endpoint deliberately ignore length, a safe overapproximation.
SAT means only local balance. Numeric discovery is accepted ONLY after exact
rational reconstruction of every primal equality or dual inequality.
"""
import argparse,json
from pathlib import Path
from itertools import product
from collections import Counter,defaultdict
from fractions import Fraction
from sage.all import QuadraticField,AA
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix
K=QuadraticField(3,'w',embedding=AA(3).sqrt());w=K.gen()
SOURCE=Path('research/certificates/partial-contact-cairo-one-shared-event-flats.json')
PERP=(1,0,3,2,5,4,7,6)

def canonical(x):return min(tuple(x[i:]+x[:i]) for i in range(len(x)))
def model(record,chamber,order_free=False):
 forms=[tuple(map(K,t)) for t in record['arm_forms']+record['e_forms']]
 add=lambda i,j:tuple(a+b for a,b in zip(forms[i],forms[j]))
 sample=K(chamber['sample_parameter']);value=lambda f:f[0]+f[1]*sample
 assert order_free or all(value(f)>0 for f in forms)
 events=[(i,j,add(i,j)) for i,j in product(range(8),repeat=2) if forms[PERP[i]]==forms[PERP[j]]]
 sums=[{T for i,j,T in events if i==k or j==k} for k in range(8)]
 choices=[]
 for i in range(8):
  shorter=sorted({forms[j] for j in range(8) if forms[j]!=forms[i] and (order_free or value(forms[j])<value(forms[i])) and sums[i]&sums[j]})
  choices.append([None]+shorter)
 echoices=[]
 for H in (8,9):
  echoices.append([None]+sorted({(forms[i],forms[j]) for i,j,T in events if T==forms[H]}))
 edges=[];edgeid={};corners=[];cornerid={};variants=[];rawvariants=[]
 # Each edge signature records its native side, its complete partition, and
 # its piece. Other cuts on the same occurrence do not alter that signature.
 def edge(species,native,parts,j,angles):
  key=(species,native,tuple(parts),j)
  if key not in edgeid:
   k=len(edges);edgeid[key]=k
   count=int(angles[j]==120)+int(angles[j+1]==120)
   colour=(count,parts[j] if count else ())
   edges.append((key,colour))
  return edgeid[key]
 for species in (0,1):
  for cuts in product(*choices[4*species:4*species+4],echoices[species]):
   nativeangles=(120,90,120,90,120)
   es=[];angs=[]
   for i,cut in enumerate(cuts):
    length=forms[4*species+i] if i<4 else forms[8+species]
    if cut is None:parts=(length,)
    elif i==4:parts=cut
    else:
     residual=tuple(a-b for a,b in zip(length,cut))
     assert order_free or value(residual)>0
     parts=(cut,residual) if i in (0,2) else(residual,cut)
    aa=(nativeangles[i],)+((180,) if len(parts)==2 else())+(nativeangles[(i+1)%5],)
    for j in range(len(parts)):
     es.append(edge(species,i,parts,j,aa));angs.append(aa[j])
   cs=[]
   for i,ang in enumerate(angs):
    key=(ang,es[i-1],es[i])
    if key not in cornerid:cornerid[key]=len(corners);corners.append(key)
    cs.append(cornerid[key])
   variants.append(Counter(cs));rawvariants.append((species,tuple(cuts),cs))
 oriented=[];first=defaultdict(list)
 for c,(angle,prev,nxt) in enumerate(corners):
  for flip in (0,1):
   # sector first and last rays, together with native endpoints of edges.
   outgoing,incoming=(nxt,prev) if not flip else(prev,nxt)
   op,ip=(0,1) if not flip else(1,0)
   oid=len(oriented);oriented.append((c,flip,angle,outgoing,incoming,op,ip))
   first[edges[outgoing][1]].append(oid)
 stars=set()
 def extend(chain,total):
  a=oriented[chain[-1]]
  if total==360:
   b=oriented[chain[0]]
   if len(chain) not in (3,4) or edges[a[4]][1]!=edges[b[3]][1]:return
   if a[2]==b[2]==90 and edges[a[4]][1][0]!=1:return
   stars.add(canonical(chain));return
  if total>360 or len(chain)>=4:return
  for j in first[edges[a[4]][1]]:
   b=oriented[j]
   if j<chain[0]:continue
   if a[2]==b[2]==90 and edges[a[4]][1][0]!=1:continue
   # Native Cairo angular partitions have exactly these compositions.
   if (a[2]==120)!=(b[2]==120):continue
   extend(chain+[j],total+b[2])
 for start,a in enumerate(oriented):extend([start],a[2])
 stars=sorted(stars);counts=[];seams=[];keys=set()
 for star in stars:
  cc=Counter();ss=Counter()
  for j,i in enumerate(star):
   a=oriented[i];b=oriented[star[(j+1)%len(star)]];cc[a[0]]+=1
   x,y=a[4],b[3];px,py=a[6],b[5]
   if x>y:x,y,px,py=y,x,py,px
   if x==y and px!=py:continue
   key=(x,y,px^py);ss[key]+=1 if px==0 else -1
  counts.append(cc);seams.append(ss);keys.update(k for k,v in ss.items() if v)
 return rawvariants,edges,corners,oriented,stars,counts,seams,sorted(keys),variants

def balance(r,ch,order_free=False):
 raw,edges,corners,oriented,stars,counts,seams,keys,variants=model(r,ch,order_free)
 nw=len(corners);kid={k:i for i,k in enumerate(keys)};rr=[];cc=[];vv=[]
 # primal matrix: corner conservation and opposite seam endpoint balance.
 for j,(C,S) in enumerate(zip(counts,seams)):
  for c,v in C.items():rr.append(c);cc.append(j);vv.append(v)
  for key,v in S.items():
   if v:rr.append(nw+kid[key]);cc.append(j);vv.append(v)
 for j,C in enumerate(variants):
  for c,v in C.items():rr.append(c);cc.append(len(stars)+j);vv.append(-v)
  rr.append(nw+len(keys));cc.append(len(stars)+j);vv.append(1)
 nrow=nw+len(keys)+1;ncol=len(stars)+len(variants)
 mat=coo_matrix((vv,(rr,cc)),shape=(nrow,ncol)).tocsr();rhs=np.zeros(nrow);rhs[-1]=1
 proposal=linprog(np.zeros(ncol),A_eq=mat,b_eq=rhs,bounds=(0,None),method='highs')
 rec={'flat_id':r['flat_id'],'order_free':order_free,'interval':ch['interval'],'sample_parameter':ch['sample_parameter'],
      'variant_count':len(variants),'corner_count':nw,'edge_count':len(edges),'star_count':len(stars),'seam_count':len(keys),'numeric_status':int(proposal.status)}
 frac=lambda x:Fraction(float(x)).limit_denominator(1000000)
 if proposal.success:
  vals=list(map(frac,proposal.x))
  valid=all(v>=0 for v in vals) and sum(vals[len(stars):])==1
  for c in range(nw):
   valid &= sum(vals[j]*C.get(c,0) for j,C in enumerate(counts))==sum(vals[len(stars)+j]*C.get(c,0) for j,C in enumerate(variants))
  for k in keys:valid &= sum(vals[j]*S.get(k,0) for j,S in enumerate(seams))==0
  if valid:
   rec['result']='exact-necessary-primal';rec['star_frequencies']={str(i):str(v) for i,v in enumerate(vals[:len(stars)]) if v};rec['variant_frequencies']={str(i):str(v) for i,v in enumerate(vals[len(stars):]) if v}
  else:rec['result']='numeric-primal-unreconstructed'
 elif proposal.status==2:
  rr=[];cc=[];vv=[]
  for j,(C,S) in enumerate(zip(counts,seams)):
   for c,v in C.items():rr.append(j);cc.append(c);vv.append(-v)
   for k,v in S.items():
    if v:rr.append(j);cc.append(nw+kid[k]);vv.append(-v)
  for j,C in enumerate(variants):
   for c,v in C.items():rr.append(len(stars)+j);cc.append(c);vv.append(v)
  dm=coo_matrix((vv,(rr,cc)),shape=(len(stars)+len(variants),nw+len(keys))).tocsr();dr=np.zeros(len(stars)+len(variants));dr[len(stars):]=-1
  dual=linprog(np.zeros(nw+len(keys)),A_ub=dm,b_ub=dr,bounds=(None,None),method='highs')
  if dual.success:
   d=list(map(frac,dual.x));W=d[:nw];Y=d[nw:]
   valid=all(sum(W[c]*v for c,v in C.items())+sum(Y[kid[k]]*v for k,v in S.items())>=0 for C,S in zip(counts,seams)) and all(sum(W[c]*v for c,v in C.items())<=-1 for C in variants)
   if valid:rec['result']='exact-necessary-dual';rec['corner_dual']=list(map(str,W));rec['seam_dual']=list(map(str,Y))
   else:rec['result']='numeric-dual-unreconstructed'
  else:rec['result']='numeric-infeasible-no-dual'
 else:rec['result']='numeric-failure'
 print(r['flat_id'],ch['interval'],rec['result'],'variants',len(variants),'corners',nw,'stars',len(stars),'seams',len(keys),flush=True)
 return rec

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--flat',type=int,action='append');p.add_argument('--chamber',type=int);p.add_argument('--output');p.add_argument('--order-free',action='store_true');a=p.parse_args()
 D=json.loads(SOURCE.read_text());out=[]
 for r in D['records']:
  if r['status']!='generic-local-survivor' or(a.flat and r['flat_id'] not in a.flat):continue
  for j,ch in enumerate(r['generic_arm_order_chambers'][:1] if a.order_free else r['generic_arm_order_chambers']):
   if a.chamber is not None and j!=a.chamber:continue
   out.append(balance(r,ch,a.order_free))
 if a.output:Path(a.output).write_text(json.dumps({'scope':'necessary optional native-subdivision corner/seam balance; length-free residual overapproximation; no existence inferred','source':str(SOURCE),'records':out},indent=2)+'\n')
