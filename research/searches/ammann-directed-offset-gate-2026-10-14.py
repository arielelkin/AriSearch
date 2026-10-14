"""Exact local geometry and bounded NLSAT gate for directed-offset surgery."""
import argparse
import hashlib
import json
import time
import sympy as S

aX,aY,hX,hY,c,s=S.symbols('aX aY hX hY c s', real=True)
V=(S.Matrix([0,0]),S.Matrix([1,0]),S.Matrix([1+c,s]),S.Matrix([c,s]))
TYPES={
 'thin': ((0,1,'X'),(2,1,'X'),(2,3,'Y'),(0,3,'Y')),
 'thick':((0,1,'X'),(1,2,'Y'),(3,2,'Y'),(0,3,'X')),
}
P={'X':(aX,hX),'Y':(aY,hY)}

def cross(u,v): return S.expand(u[0]*v[1]-u[1]*v[0])
def signed_area(poly): return S.factor(sum(cross(poly[i],poly[(i+1)%len(poly)]) for i in range(len(poly)))/2)
def d2(u,v):
 d=u-v
 return S.expand(d.dot(d)).subs(s*s,1-c*c).factor()
def apex(edge, arrows, interior):
 i=edge; j=(i+1)%4
 tail,head,Z=arrows[i]; a,h=P[Z]
 edgevec=V[j]-V[i]; n=S.Matrix([-edgevec[1],edgevec[0]])
 b=a if tail==i else 1-a
 return S.simplify(V[i]+b*edgevec+(1 if interior else -1)*h*n)

def outputs():
 out=[]
 for name,arrows in TYPES.items():
  for donor_parity in (0,1):
   donor=(donor_parity,(donor_parity+2)%4)
   nodes={i:apex(i,arrows,True) for i in donor}
   for recv in ((donor_parity+1)%4,(donor_parity+3)%4):
    i=recv; j=(i+1)%4
    poly=[V[i],apex(i,arrows,False),V[j],nodes[(i+1)%4],nodes[(i-1)%4]]
    out.append((name,donor_parity,i,arrows[i][2],poly))
 return out

def norm(expr):
 return S.factor(S.expand(expr).subs(s*s,1-c*c))

def turns(poly):
 return [cross(poly[(i+1)%len(poly)]-poly[i],poly[(i+2)%len(poly)]-poly[(i+1)%len(poly)]) for i in range(len(poly))]

def support_exprs(poly):
 """Strict full-support tests for a counterclockwise convex polygon."""
 n=len(poly)
 return [cross(poly[(i+1)%n]-poly[i],poly[j]-poly[i])
         for i in range(n) for j in range(n) if j not in (i,(i+1)%n)]

def sectors(kind,role):
 """Four source sectors in cyclic order, before cross-edge triangle exchange."""
 arrows=TYPES[kind]
 donor={role,(role+2)%4}
 nodes={i:apex(i,arrows,True) for i in donor}
 result=[]
 for i in range(4):
  j=(i+1)%4
  if i in donor:result.append([V[i],V[j],nodes[i]])
  else:result.append([V[i],V[j],nodes[(i+1)%4],nodes[(i-1)%4]])
 return result

def separating_options(p,q):
 """SAT axes for disjoint interiors of two strictly convex sectors."""
 options=[]
 for x,y in ((p,q),(q,p)):
  for i in range(len(x)):
   options.append([cross(x[(i+1)%len(x)]-x[i],v-x[i]) for v in y])
 return options

def congruence_equations(p,q,shift,reverse):
 idx=lambda j:(shift+(-j if reverse else j))%5
 return [norm(d2(p[i],p[j])-d2(q[idx(i)],q[idx(j)])) for i in range(5) for j in range(i+1,5)]

def partitions4():
 # Unlabeled two-class partitions: the class containing index 0 is canonical.
 for mask in range(8):
  left=[0]+[i for i in range(1,4) if mask&(1<<(i-1))]
  if len(left)==4: continue
  right=[i for i in range(4) if i not in left]
  yield left,right

def substitute_source(expr,kind):
 phi,t=S.symbols('phi t', real=True)
 cc=phi/2 if kind=='thin' else (phi-1)/2
 ss=t if kind=='thin' else phi*t
 return S.expand(expr.subs({c:cc,s:ss}))

def z3gate(total_cap):
 import z3
 from fractions import Fraction
 out=outputs()
 reps=[out[i] for i in (0,1,4,5)]
 zv={str(v):z3.Real(str(v)) for v in (aX,aY,hX,hY)}
 zv.update({'phi':z3.Real('phi'),'t':z3.Real('t')})
 def cv(expr):
  if expr.is_Integer: return z3.RealVal(str(expr))
  if expr.is_Rational: return z3.RealVal(f'{expr.p}/{expr.q}')
  if expr.is_Symbol: return zv[str(expr)]
  if expr.is_Add: return z3.Sum(*[cv(x) for x in expr.args])
  if expr.is_Mul:
   v=z3.RealVal(1)
   for x in expr.args:v=v*cv(x)
   return v
  if expr.is_Pow and expr.exp.is_Integer and expr.exp>=0:return cv(expr.base)**int(expr.exp)
  raise TypeError(expr)
 phi=zv['phi'];t=zv['t']
 base=[phi*phi==phi+1,phi>z3.RealVal('8/5'),phi<z3.RealVal('17/10'),
       4*t*t==3-phi,t>z3.RealVal('58/100'),t<z3.RealVal('59/100'),
       zv['aX']>0,zv['aX']<1,zv['aY']>0,zv['aY']<1,zv['hX']>0,zv['hY']>0,
       z3.Or(zv['aX']!=z3.RealVal('1/2'),zv['aY']!=z3.RealVal('1/2'),zv['hX']!=zv['hY'])]
 # Source sector and pentagon support constraints for all eight cases.
 for kind,role,edge,mark,poly in out:
  for expr in support_exprs(poly):base.append(cv(substitute_source(expr,kind))>0)
 for kind in TYPES:
  for role in (0,1):
   local=sectors(kind,role)
   for sector in local:
    for expr in support_exprs(sector):base.append(cv(substitute_source(expr,kind))>0)
   for donor in (role,(role+2)%4):
    node=apex(donor,TYPES[kind],True)
    for i in range(4):
     base.append(cv(substitute_source(cross(V[(i+1)%4]-V[i],node-V[i]),kind))>0)
   for i in range(4):
    for j in range(i+1,4):
     base.append(z3.Or(*[z3.And(*[cv(substitute_source(e,kind))<=0 for e in option])
                        for option in separating_options(local[i],local[j])]))
 # Symmetric edge-distance equations also precede the dihedral match.
 congr={}
 for i in range(4):
  for j in range(i+1,4):
   kindi=reps[i][0];kindj=reps[j][0]
   if kindi!=kindj:
    # Build each polygon with its own source-angle substitutions.
    p=[S.Matrix([substitute_source(v[k],kindi) for k in range(2)]) for v in reps[i][4]]
    q=[S.Matrix([substitute_source(v[k],kindj) for k in range(2)]) for v in reps[j][4]]
    eqs=lambda sh,rev:[S.expand(d2(p[u],p[v])-d2(q[(sh+(-u if rev else u))%5],q[(sh+(-v if rev else v))%5])) for u in range(5) for v in range(u+1,5)]
   else:
    eqs=lambda sh,rev:[substitute_source(e,kindi) for e in congruence_equations(reps[i][4],reps[j][4],sh,rev)]
   options=[]
   for sh in range(5):
    for rev in (False,True):options.append(z3.And(*[cv(e)==0 for e in eqs(sh,rev)]))
   congr[i,j]=z3.Or(*options)
 start=time.monotonic();results=[]
 for left,right in partitions4():
  remain=max(0,total_cap-(time.monotonic()-start))
  if remain<1:break
  sol=z3.SolverFor('QF_NRA');sol.set('timeout',min(30000,int(remain*1000)))
  sol.add(*base)
  for group in (left,right):
   for j in group[1:]:sol.add(congr[min(group[0],j),max(group[0],j)])
  status=sol.check();entry={'left':left,'right':right,'status':str(status),'wall_seconds':round(time.monotonic()-start,3)}
  if status==z3.sat:entry['model']=str(sol.model())
  if status==z3.unknown:entry['reason']=sol.reason_unknown()
  results.append(entry);print(json.dumps(entry),flush=True)
  if status==z3.unknown:break
 print(json.dumps({'total_solver_wall_cap_seconds':total_cap,'results':results,'complete':len(results)==7}),flush=True)

def check_algebra():
 """Read-only exact geometry audit; no solver calls or enumeration."""
 out=outputs()
 checks=[]
 for i in range(0,8,2):
  kind=out[i][0]
  total=signed_area(out[i][4])+signed_area(out[i+1][4])
  checks.append(S.simplify(S.expand(total-s).subs(s*s,1-c*c))==0)
 for kind in TYPES:
  for role in (0,1):
   local=sectors(kind,role)
   total=sum(signed_area(p) for p in local)
   checks.append(S.simplify(S.expand(total-s).subs(s*s,1-c*c))==0)
 if not all(checks):raise AssertionError(checks)
 support_count=sum(len(support_exprs(row[4])) for row in out)
 sector_support_count=sum(len(support_exprs(p)) for kind in TYPES for role in (0,1) for p in sectors(kind,role))
 node_support_count=4*2*4
 separations=4*6
 raw='\n'.join(S.srepr(v) for row in out for point in row[4] for v in point)
 digest=hashlib.sha256(raw.encode()).hexdigest()
 print(json.dumps({'status':'exact algebra checks pass','output_polygons':8,
   'role_cases':4,'area_identities':len(checks),'pentagon_support_inequalities':support_count,
   'sector_support_inequalities':sector_support_count,
   'node_support_inequalities':node_support_count,
   'sector_pair_separation_disjunctions':separations,
   'four_representative_partitions':len(list(partitions4())),
   'ordered_distance_correspondences_per_pair':10,
   'squared_distances_per_correspondence':10,
   'ordered_coordinate_sha256':digest},sort_keys=True))

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--z3',action='store_true');parser.add_argument('--check',action='store_true');parser.add_argument('--cap',type=int,default=180);args=parser.parse_args()
 if args.check:
  check_algebra()
  raise SystemExit
 if args.z3:
  z3gate(args.cap)
  raise SystemExit
 out=outputs()
 for name,role,edge,mark,poly in out:
  print(name,role,edge,mark,'area=',signed_area(poly))
 print('PAIR DIFFERENCES')
 for i in range(0,8,2):
  d=S.factor(signed_area(out[i][4])-signed_area(out[i+1][4]))
  d=S.factor(S.rem(d,S.Poly(c*c+s*s-1,c),c)) if False else S.factor(d.subs(s*s,1-c*c))
  print(out[i][:2],d)
 print('EDGE SUM DIFFERENCES')
 for i in (0,4):
  F=lambda poly:S.expand(sum(d2(poly[j],poly[(j+1)%5]) for j in range(5)))
  print(out[i][:2],S.factor((F(out[i][4])-F(out[i+1][4])).subs(s*s,1-c*c)))
 print('EDGE SUMS')
 for i in (0,1,4,5):
  print(out[i][:3],S.factor(F(out[i][4]).subs(s*s,1-c*c)))
