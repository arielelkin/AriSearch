"""Finite native incidence relaxation; scipy proposes, Fraction verifies."""
import itertools,json
from fractions import Fraction as F
import numpy as np
from scipy.optimize import linprog
WORDS=['ABBCCBC','ABBCCCB','ABCBBCC','ACBBBCC']
def run(w):
 slots=[0,2,4,6]
 opts=[(s,r) for s in slots for r in range(2)]
 def ends(o):
  s,r=o; a,b=w[s],w[(s+1)%7]
  return (a,b) if r else (b,a)
 types=[]
 for k in range(3):
  for pp in itertools.combinations(range(5),k):
   if any((i+1)%5 in pp for i in pp):continue
   pq=[i for i in range(5) if i not in pp]
   for vals in itertools.product(opts,repeat=len(pq)):
    t=dict(zip(pq,vals)); valid=True
    for v in range(5):
     left=(v-1)%5;right=v
     if left in pp or right in pp:
      o=t[right] if left in pp else t[left]
      a=ends(o)[0 if left in pp else 1]
      if a!='A':valid=False;break
     elif set((ends(t[left])[1],ends(t[right])[0]))!={'B','C'}:
      valid=False;break
    if valid:types.append((pp,t))
 # Rows: Q unit-side uses by parity; PP oriented descriptor conservation.
 descriptors=set()
 def desc(pp,t,i):return (t[(i-1)%5],t[(i+1)%5])
 def mate(d):return tuple((6-s,r) for s,r in d[::-1])
 for pp,t in types:
  for i in pp:descriptors.add(desc(pp,t,i))
 keys=sorted(descriptors|{mate(d) for d in descriptors})
 rows=[('pq',s,r) for s,r in opts]+[('pp',d) for d in keys]+[('norm',)]
 cols=[]
 for pp,t in types:
  c={}
  for s,r in t.values():c[('pq',s,r)]=c.get(('pq',s,r),0)+1
  for i in pp:
   d=desc(pp,t,i);c[('pp',d)]=c.get(('pp',d),0)+1;c[('pp',mate(d))]=c.get(('pp',mate(d)),0)-1
  cols.append(c)
 for r in range(2):cols.append({**{('pq',s,r):-1 for s in slots},('norm',):1})
 A=np.array([[c.get(row,0) for c in cols] for row in rows],dtype=int)
 b=np.array([int(row==('norm',)) for row in rows])
 objective=np.array([-int(len(pp)!=1) for pp,t in types]+[0,0])
 res=linprog(objective,A_eq=A,b_eq=b,bounds=(0,None),method='highs')
 assert res.success,res.message
 x=[F(float(v)).limit_denominator(1000000) for v in res.x]
 assert all(sum(F(int(A[i,j]))*x[j] for j in range(len(x)))==int(b[i]) for i in range(len(b)))
 assert all(v>=0 for v in x)
 n=[sum(x[j] for j,(pp,t) in enumerate(types) if len(pp)==k) for k in range(3)]
 # Complete QQ endpoint-compatible seam domain, both reflection parities.
 # No metric or global realization is asserted.
 qq=[]
 for e in (1,3,5):
  for f in (1,3,5):
   for r in range(2):
    for u in range(2):
     a=[w[e],w[(e+1)%7]];bb=[w[f],w[(f+1)%7]]
     if r==u:bb=bb[::-1]
     if all({a[i],bb[i]}=={'B','C'} for i in range(2)):qq.append([e,r,f,u])
 qqflow=[]
 for r,q in enumerate(x[-2:]):
  bb=next(e for e in (1,3,5) if w[e]+w[e+1]=="BB")
  cc=next(e for e in (1,3,5) if w[e]+w[e+1]=="CC")
  bc=next(e for e in (1,3,5) if e not in (bb,cc))
  for e,f,v in [(bb,cc,q),(bc,bc,q/2)]:
   assert [e,r,f,r] in qq
   qqflow.append({"seam":[e,r,f,r],"weight":str(v)})
  for e in (1,3,5):
   assert sum(F(a["weight"])*(int(a["seam"][0]==e)+int(a["seam"][2]==e)) for a in qqflow if a["seam"][1]==r)==q
 support=[]
 for j,v in enumerate(x[:-2]):
  if v:
   pp,t=types[j];support.append({'weight':str(v),'PP':list(pp),'PQ':{str(i):list(o) for i,o in t.items()}})
 assert n[0]+n[2]==0
 assert all(len(pp)<=1 for pp,t in types)
 for pp,t in types:
  charge=sum(F(1-2*(int(w[s]=="A")+int(w[(s+1)%7]=="A")),5) for s,r in t.values())
  assert charge==1-len(pp) and charge>=0
 assert sum(F(1-2*(int(w[s]=="A")+int(w[(s+1)%7]=="A")),5) for s in slots)==0
 return {'word':w,'P_type_count':len(types),'PP_descriptor_count':len(keys),'Q_parities':[str(v) for v in x[-2:]],'n':[str(v) for v in n],'P_support':support,'QQ_domain':qq,'QQ_flow':qqflow,'exact_residual':'zero','dual_PQ_weights':{'0':'-1/5','2':'1/5','4':'1/5','6':'-1/5'},'dual_defect_bound':'n0+n2=0'}
if __name__=='__main__':
 data=[run(w) for w in WORDS]
 out=__file__.replace('.py','.json')
 with open(out,'w') as f:json.dump(data,f,indent=2)
 for d in data:print(d['word'],d['P_type_count'],d['n'])
