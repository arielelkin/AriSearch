"""Complete9-plane arrangement for centerpp/pureqq binary two-run hexagons.
Actual metric phase is separate. Exact UNSAT requires retained strong rational dual.
Normal replay read-only; explicit --output writes. No timeout is UNSAT.
"""
from pathlib import Path
from collections import Counter
from itertools import combinations,combinations_with_replacement,permutations,product
from fractions import Fraction
from math import gcd
from functools import reduce
from sage.all import QQ,matrix,vector
import z3,argparse,json
labels=[['p','q']*3,['p']*3+['q']*3]
angle_names=['H','L']*3+['u','alpha','beta','v','chi','psi']
angle_dict={'H':(120,1,0,0),'L':(120,-1,0,0),'u':(300,0,-1,-1),'alpha':(120,0,0,0),'beta':(120,0,0,0),'v':(60,0,0,1),'chi':(120,0,0,0),'psi':(0,0,1,0)}
angles=[angle_dict[n] for n in angle_names]
def canon(v):
 g=reduce(gcd,map(abs,v));w=tuple(int(x/g) for x in v) if g else tuple(v)
 if next((x for x in w if x),1)<0:w=tuple(-x for x in w)
 return w

def inventory():
 raw=[];classes={};ident=[]
 def add(tri):
  v=[sum(angle_dict[c][j] for c in tri) for j in range(4)];v[0]-=360
  c=canon(v);entry={'slots':tri,'sum_minus360':v,'canonical':c};raw.append(entry)
  if any(c):classes.setdefault(c,[]).append(tri)
  else:ident.append(tri)
 for pair in combinations_with_replacement(['H','L','u','v'],2):
  for h in ['alpha','beta','chi','psi']:add(pair+(h,))
 for hs in [('alpha','beta'),('chi','psi')]:
  for tri in combinations_with_replacement(hs,3):add(tri)
 assert len(raw)==48 and len(ident)==9 and len(classes)==11
 removed={(0,1,0,0):'delta0 excluded',(120,0,-1,0):'psi120 gives p=q excluded'}
 planes=sorted(k for k in classes if k not in removed);assert len(planes)==9
 return {'raw48':raw,'permanent_identities':ident,'nonidentity11':[{'coefficients':k,'types':ts} for k,ts in sorted(classes.items())],
         'removed_planes':[{'coefficients':k,'reason':v} for k,v in removed.items()],'exception_planes9':planes}

def cyc(t):return min(tuple(t[j:]+t[:j]) for j in range(3))
def frac(e,m):
 a=m.eval(e,model_completion=True);return str(Fraction(a.numerator_as_long(),a.denominator_as_long()))
def full_model(flat,index,timeout):
 space=flat.row_space();ori=[]
 for s in(0,1):
  for i in range(6):
   cid=6*s+i;out,prev=labels[s][i],labels[s][i-1]
   ori.extend([(cid,0,out,prev,(s,i),(s,(i-1)%6),0,1),(cid,1,prev,out,(s,(i-1)%6),(s,i),1,0)])
 legal=[]
 for tri in combinations_with_replacement(range(12),3):
  v=[sum(angles[c][j] for c in tri) for j in range(4)];v[0]-=360
  if vector(QQ,v) in space:legal.append(tri)
 stars=set()
 for tri in legal:
  for order in set(permutations(tri)):
   for flips in product((0,1),repeat=3):
    st=[2*c+f for c,f in zip(order,flips)]
    if all(ori[st[i]][3]==ori[st[(i+1)%3]][2] for i in range(3)):stars.add(cyc(st))
 stars=sorted(stars);C=[];S=[];keys=set()
 for st in stars:
  cc=Counter();ss=Counter()
  for j,o in enumerate(st):
   a=ori[o];b=ori[st[(j+1)%3]];cc[a[0]]+=1;x,y=a[5],b[4];px,py=a[7],b[6]
   if x==y and px!=py:continue
   if x<=y:key=(x,y,px^py);sign=1 if px==0 else -1
   else:key=(y,x,px^py);sign=1 if py==0 else -1
   ss[key]+=sign
  C.append(cc);S.append(ss);keys.update(ss)
 keys=sorted(keys);f=z3.Reals('FA FB');X=[z3.Real('X'+str(i)) for i in range(len(stars))]
 solver=z3.Solver();solver.set(timeout=timeout);solver.add(*(v>=0 for v in list(f)+X),sum(f)==1)
 for c in range(12):solver.add(sum(X[i]*cc[c] for i,cc in enumerate(C) if cc[c])==f[c//6])
 for k in keys:solver.add(sum(X[i]*ss[k] for i,ss in enumerate(S) if ss[k])==0)
 status=solver.check();r={'index':index,'status':str(status),'oriented_stars':stars,'star_corner_counts':[dict(c) for c in C],'seam_keys':keys,'star_seam_counts':[[s[k] for k in keys] for s in S]}
 if status==z3.sat:
  solver.push();solver.add(f[0]>0,f[1]>0);mix=solver.check();r['mixed_status']=str(mix)
  if mix!=z3.sat:solver.pop();assert solver.check()==z3.sat
  m=solver.model();r['species_frequencies']=[frac(v,m) for v in f];r['star_frequencies']=[frac(v,m) for v in X]
  ff=list(map(Fraction,r['species_frequencies']));xx=list(map(Fraction,r['star_frequencies']));assert sum(ff)==1 and min(ff+xx)>=0
  assert all(sum(xx[i]*cc[c] for i,cc in enumerate(C))==ff[c//6] for c in range(12))
  assert all(sum(xx[i]*ss[k] for i,ss in enumerate(S))==0 for k in keys)
 elif status==z3.unsat:
  W=[z3.Real('W'+str(i)) for i in range(12)];Y=[z3.Real('Y'+str(i)) for i in range(len(keys))];dual=z3.Solver();dual.set(timeout=timeout)
  for cc,ss in zip(C,S):dual.add(sum(W[c]*v for c,v in cc.items())+sum(Y[j]*ss[k] for j,k in enumerate(keys) if ss[k])>=0)
  for s in(0,1):dual.add(sum(W[c] for c in range(6*s,6*s+6))<=-1)
  ds=dual.check();r['dual_status']=str(ds)
  if ds==z3.sat:
   m=dual.model();r['corner_dual']=[frac(v,m) for v in W];r['seam_dual']=[frac(v,m) for v in Y]
   ww=list(map(Fraction,r['corner_dual']));yy=dict(zip(keys,map(Fraction,r['seam_dual'])))
   assert all(sum(ww[c]*v for c,v in cc.items())+sum(yy[k]*v for k,v in ss.items())>=0 for cc,ss in zip(C,S))
   assert all(sum(ww[c] for c in range(6*s,6*s+6))<=-1 for s in(0,1))
  else:r['status']='unknown';r['reason']='strongdual not retained:'+str(ds)
 else:r['reason']=solver.reason_unknown()
 print('flat',index,r['status'],'stars',len(stars),'seams',len(keys),'f',r.get('species_frequencies'),flush=True)
 return r

def run(output=None,timeout=10000):
 inv=inventory();planes=inv['exception_planes9'];flats={};ngen=0
 for k in range(4):
  for subset in combinations(range(9),k):
   ngen+=1;A=matrix(QQ,[planes[j] for j in subset]) if subset else matrix(QQ,0,4)
   if A.nrows() and A[:,1:].rank()!=A.rank():continue
   A=A.row_space().basis_matrix();key=tuple(tuple(str(t) for t in row) for row in A.rows())
   flats.setdefault(key,{'flat':A,'generating_subsets':[]})['generating_subsets'].append(subset)
 assert ngen==130
 records=[];rejected=[]
 for key,entry in sorted(flats.items()):
  A=entry['flat'];D,T,P=z3.Reals('DELTA PSI RHO');vars=[z3.RealVal(1),D,T,P]
  active=[j for j,row in enumerate(planes) if vector(QQ,row) in A.row_space()]
  linear=z3.Solver();linear.add(D>0,D<30,T>0,T<180,T!=120,P>0,P<90,P+T>120)
  for row in A.rows():linear.add(sum(z3.RealVal(str(c))*v for c,v in zip(row,vars))==0)
  for j,row in enumerate(planes):
   if j not in active:linear.add(sum(z3.RealVal(str(c))*v for c,v in zip(row,vars))!=0)
  status=linear.check()
  if status==z3.unsat:rejected.append({'flat_basis':key,'generating_subsets':entry['generating_subsets'],'active_exception_planes':active});continue
  assert status==z3.sat;m=linear.model();sample=[frac(v,m) for v in[D,T,P]]
  r=full_model(A,len(records),timeout);r.update({'flat_basis':key,'generating_subsets':entry['generating_subsets'],'active_exception_planes':active,'strict_linear_sample':sample,'sample_not_actual_metric_geometry':True});records.append(r)
 out={'schema':'centerpp-pureqq-complete-slot-arrangement-v1','inventory':inv,'pre_stated_domain':'all130 subsets of9exception planes,size0..3;allconsistent affineflats; exact active-complement linear strata0delta30,0psi180,psi!=120,0rho90,rho+psi120',
 'actual_metric_requirement_separate':'rho=arg(1+exp(i60)+exp(i(240-psi)));p=|P|/2;actualstrictdomain60<psi180,psi!=120',
 'generator_subset_count':ngen,'consistent_flat_count':len(flats),'linear_infeasible_flats':rejected,'records':records,'counts':dict(Counter(r['status'] for r in records)),
 'scope':'Every exactdual excludes all admittedactual geometries in its precise active stratum via reviewedETE limit and signedside invariant. SATnecessaryonly. No missing timeout treatedasUNSAT; speciesfrequenciesfree.'}
 if output:Path(output).write_text(json.dumps(out,indent=2)+'\n')
 print('COMPLETE',len(flats),'flats;',len(records),'envelopes;',out['counts'],flush=True);return out
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output');ap.add_argument('--timeout-ms',type=int,default=10000);args=ap.parse_args();run(args.output,args.timeout_ms)
