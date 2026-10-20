"""Exact six-template closure gate for the 2026-10-20 Astra proposal.

All arithmetic uses the real algebraic field AA. The script deliberately tests
only the six prescribed Q-corner templates, with P4 and Q0,Q7 normalized to 1.
"""
from sage.all import *
from scipy.optimize import linprog
from itertools import product
import z3
import json
from pathlib import Path
import importlib.util

PANG = (100,110,100,120,110)
QANG = (150,130,140,130,140,120,140,130)
Z = QQbar.zeta(36)
def cs(deg):
    w = Z ** (deg//10)
    return vector(AA, (w.real(),w.imag()))
def directions(angles):
    d=0; out=[]
    for i in range(len(angles)):
        out.append(cs(d));d+=180-angles[(i+1)%len(angles)]
    return out
PD,QD=directions(PANG),directions(QANG)
assert sum(PANG)==540 and sum(QANG)==1080
assert [(PANG[0]+PANG[4],PANG[1]+PANG[3])]==[(210,230)]
assert [i for i,a in enumerate(QANG) if a==130]==[1,3,7]

def lin_solve(cols, known, pair):
    """Solve two closure lengths at pair, all other coordinates known."""
    rhs=-sum((known[i]*cols[i] for i in known),vector(AA,(0,0)))
    a,b=cols[pair[0]],cols[pair[1]]
    det=a[0]*b[1]-a[1]*b[0]
    assert det!=0
    return ( (rhs[0]*b[1]-rhs[1]*b[0])/det,
            (a[0]*rhs[1]-a[1]*rhs[0])/det )

def make_p(t):
    vals={0:AA(t),3:AA(t),4:AA(1)}
    vals[1],vals[2]=lin_solve(PD,vals,(1,2))
    return [vals[i] for i in range(5)]

def q_known(p,k,rev):
    vals={0:AA(1),7:AA(1)}
    # Q side k-1 and k pair with P sides 1 and 2 in either order.
    assignments={(k-1)%8:p[2] if rev else p[1], k:p[1] if rev else p[2]}
    for j,v in assignments.items():
        if j in vals:
            assert vals[j]==v, (k,rev,j,vals[j],v)
        vals[j]=v
    return vals

def feasibility(p,k,rev):
    known=q_known(p,k,rev)
    # Exact 2D convex-hull feasibility: positive unknown lengths can balance
    # the fixed closure vector iff LP margin >0. LP is candidate discovery;
    # exact AA certificates below verify the selected outcomes.
    eq=[[float(v[j]) for v in QD] for j in (0,1)]
    fixed=[[1 if i==j else 0 for i in range(8)] for j in known]
    A=eq+fixed
    b=[0,0]+[float(v) for v in known.values()]
    res=linprog([0]*8+[-1],A_eq=[row+[0] for row in A],b_eq=b,
                A_ub=[[-int(i==j) for i in range(8)]+[1] for j in range(8)],
                b_ub=[0]*8,bounds=[(0,None)]*8+[(0,None)],method='highs')
    return bool(res.success and res.x[-1]>1e-8), (res.x[-1] if res.success else None)

def make_q(p,k,rev,freevals):
    known=q_known(p,k,rev)
    free=[i for i in range(8) if i not in known and i not in (4,5)]
    assert len(free)==3 if k in (1,7) else len(free)==2
    for i,v in zip(free,freevals):known[i]=AA(v)
    assert len(known)==6 and 4 not in known and 5 not in known
    known[4],known[5]=lin_solve(QD,known,(4,5))
    return [known[i] for i in range(8)]

def vertices(lengths, dirs):
    v=[vector(AA,(0,0))]
    for l,d in zip(lengths,dirs):v.append(v[-1]+l*d)
    assert v[-1]==v[0]
    return v[:-1]

def orient(a,b,c):
    u=b-a;v=c-a
    return u[0]*v[1]-u[1]*v[0]

def strict_convex(v):
    n=len(v)
    return all(orient(v[i],v[(i+1)%n],v[(i+2)%n])>0 for i in range(n))

def overlap_int(a,b):
    # Strict separating axis test for convex polygons; touching is allowed.
    for poly in (a,b):
        for i in range(len(poly)):
            edge=poly[(i+1)%len(poly)]-poly[i]
            axis=vector(AA,(-edge[1],edge[0]))
            aa=[axis.dot_product(x) for x in a]
            bb=[axis.dot_product(x) for x in b]
            if max(aa)<=min(bb) or max(bb)<=min(aa):return False
    return True

def reflected(v):return [vector(AA,(x[0],-x[1])) for x in v]
def place_on_edge(poly,idx,dst,dstnext):
    # Isometry taking two native vertices to prescribed target vertices.
    n=len(poly);u=poly[idx];w=poly[(idx+1)%n]
    su=w-u;du=dstnext-dst
    if su.dot_product(su)!=du.dot_product(du):return None
    # Rotation or reflection determined by source and target edge.
    cross=su[0]*du[1]-su[1]*du[0]
    dot=su.dot_product(du);norm=su.dot_product(su)
    rot=matrix(AA,2,2,[dot,-cross,cross,dot])/norm
    return [dst+rot*(x-u) for x in poly]

records=[]
for k in (1,3,7):
 for rev in (False,True):
  if k==3:
   candidate_t=[AA(QQ(1)/2)]
  else:
   # A Q side at this corner coincides with Q0 or Q7; solve the
   # resulting P1=1 or P2=1 equation exactly before closure LP.
   j = (1 if (k==1 and not rev) or (k==7 and rev) else 2)
   p0,p1=make_p(AA(0)),make_p(AA(1))
   candidate_t=[(AA(1)-p0[j])/(p1[j]-p0[j])]
  trials=[]
  for t in candidate_t:
   p=make_p(t)
   if min(p)<=0:continue
   ok,margin=feasibility(p,k,rev)
   trials.append((str(t),ok,margin,[str(x) for x in p]))
  records.append(dict(corner=int(k),reverse=rev,trials=trials))
print(json.dumps(records,indent=2))

# Exact representative for each feasible Q3 radial order. The two Q copies at
# seam endpoints are inspected numerically/with exact convex tests separately.
p=make_p(QQ(1)/2)
assert min(p)>0
print('P',[str(x) for x in p])
assert strict_convex(vertices(p,PD))

def endpoint_placements(qv,k,V,left,right):
    out=[]
    for flip in (False,True):
        source=reflected(qv) if flip else qv
        for target,target_name in ((left,'left'),(right,'right')):
            for side in ((k-1)%8,k):
                if side==k:
                    cand=place_on_edge(source,side,V,target)
                else:
                    cand=place_on_edge(source,side,target,V)
                if cand is None:continue
                if cand[k]!=V:continue
                other=cand[(k-1)%8] if side==k else cand[(k+1)%8]
                expected=(right if target_name=='left' else left)
                if other!=expected:continue
                out.append((flip,target_name,side,cand))
    return out

def patch_status(p,q,k):
    av=vertices(p,PD)
    bv=place_on_edge(av,3,av[1],av[0])
    assert bv[4]==av[0] and bv[3]==av[1] and not overlap_int(av,bv)
    qv=vertices(q,QD)
    top=endpoint_placements(qv,0,av[0],av[4],bv[0])
    bot=endpoint_placements(qv,k,av[1],av[2],bv[2])
    if k==3 and not bot:
      V,left,right=av[1],av[2],bv[2]
      print('DEBUG ANGLE',float((left-V).dot_product(right-V)),float((left-V).norm()),float((right-V).norm()))
      print('DEBUG TARGETS',tuple(map(float,left)),tuple(map(float,right)))
      for flip in (False,True):
       source=reflected(qv) if flip else qv
       cand=place_on_edge(source,2,left,V)
       if cand is not None:print('DEBUG OTHER',flip,tuple(map(float,cand[4])),tuple(map(float,cand[4]-right)))
    good=[]
    for a in top:
      for b in bot:
       polys=(av,bv,a[3],b[3])
       if all(not overlap_int(polys[i],polys[j]) for i in range(4) for j in range(i+1,4)):
        good.append(dict(top=(a[0],a[1],a[2]),bottom=(b[0],b[1],b[2])))
    return dict(top_count=len(top),bottom_count=len(bot),nonoverlap=good)

spec=importlib.util.spec_from_file_location('rao_filter',Path('research/searches/convex-substitution-shapes.py').resolve())
rao_mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(rao_mod)
def rao_hits(p):
    out=[]
    for typ,(angle_eqs,length_eqs) in rao_mod.RAO.items():
      for sign in (1,-1):
       for off in range(5):
        amap=[(off+sign*i)%5 for i in range(5)]
        rotated=[PANG[j] for j in amap]
        if not all(sum(a*b for a,b in zip(row,rotated))==target*36 for row,target in angle_eqs):continue
        smap=([(off+i)%5 for i in range(5)] if sign==1 else [(off-i-1)%5 for i in range(5)])
        if all(sum((AA(c)*p[j] for c,j in zip(row,smap)),AA(0))==0 for row in length_eqs):
         out.append((typ,sign,off))
    return out

R=(QQ(1)/5,QQ(1)/2,QQ(1),QQ(3)/2,QQ(2))
for rec in records:
 k,rev=rec['corner'],rec['reverse']
 t=AA(rec['trials'][0][0].replace('?','')) if False else None
 if k==3:t=AA(QQ(1)/2)
 else:
  j=(1 if (k==1 and not rev) or (k==7 and rev) else 2)
  p0,p1=make_p(AA(0)),make_p(AA(1))
  t=(AA(1)-p0[j])/(p1[j]-p0[j])
 p=make_p(t)
 free=[i for i in range(8) if i not in q_known(p,k,rev) and i not in (4,5)]
 candidates=[]
 for vals in product(R,repeat=len(free)):
  q=make_q(p,k,rev,vals)
  if min(q)>0:
   candidates.append((vals,q))
   break
 if not candidates:
  print('NO POSITIVE RATIONAL FREE CHOICE',k,rev)
  continue
 vals,q=candidates[0]
 assert all(x>0 for x in q)
 assert strict_convex(vertices(p,PD)) and strict_convex(vertices(q,QD))
 status=patch_status(p,q,k)
 print('TEMPLATE',k,rev,'t',str(t),'free',list(map(str,vals)),'q',list(map(str,q)),'patch',status,'rao',rao_hits(p))
 rec['metric']=(p,q)

def torus_2p1q(p,q):
  outcomes=[]
  for flips in product((0,1),repeat=2):
    angles=[];labels=[];rho=[];faces=[];native=[]
    for f,(A,L,flip) in enumerate(zip((PANG,PANG,QANG),(p,p,q),(0,*flips))):
      n=len(A);off=len(angles)
      for i in range(n):
        j=(-i)%n if flip else i
        angles.append(int(A[j]));labels.append(L[(j-1)%n] if flip else L[j])
        rho.append(int(off+(i+1)%n));faces.append(f);native.append(j)
    n=len(angles);s=z3.Solver();s.set(timeout=int(8000),random_seed=int(0))
    alpha=[z3.Int('a%d'%i) for i in range(n)]
    def elem(xs,k):
      ar=z3.K(z3.IntSort(),int(0))
      for j,val in enumerate(xs):ar=z3.Store(ar,int(j),int(val) if not isinstance(val,z3.ExprRef) else val)
      return z3.Select(ar,k)
    for i in range(n):
      s.add(z3.Or([alpha[i]==j for j in range(n) if j!=i and labels[i]==labels[j]]))
      s.add(elem(alpha,alpha[i])==i)
    v=[elem(rho,alpha[i]) for i in range(n)]
    for i in range(n):
      v2=elem(v,v[i]);v3=elem(v,v2)
      s.add(v3==i,v[i]!=i,v2!=i,
            angles[i]+elem(angles,v[i])+elem(angles,v2)==360)
    sat=s.check();record=dict(flips=flips,status=str(sat))
    if sat==z3.sat:
      model=s.model();aa=[model.eval(x).as_long() for x in alpha]
      seen={0}
      while True:
        new=seen|{rho[i] for i in seen}|{aa[i] for i in seen}
        if new==seen:break
        seen=new
      record.update(alpha=aa,connected=len(seen)==n,
                    pairings=[(i,aa[i]) for i in range(n) if i<aa[i]])
    if sat==z3.unknown:record['reason']=s.reason_unknown()
    outcomes.append(record)
  return outcomes

for rec in records:
 p,q=rec['metric']
 print('TORUS_2P1Q',rec['corner'],rec['reverse'],torus_2p1q(p,q),flush=True)

def seam_orbit(p):
  source=vertices(p,PD)
  tiles=[source]
  for j in range(12):
    cur=tiles[-1]
    tiles.append(place_on_edge(source,3,cur[1],cur[0]))
  intersections=[(i,j) for i in range(12) for j in range(i+1,12)
                 if overlap_int(tiles[i],tiles[j])]
  return dict(closed=tiles[12]==tiles[0],intersections=intersections,
              centers=[tuple(float(x) for x in v[0]) for v in tiles[:12]])
for rec in records:
 p,q=rec['metric']
 print('SEAM_ORBIT',rec['corner'],rec['reverse'],seam_orbit(p),flush=True)

for rec in records:
 if (rec['corner'],rec['reverse']) not in ((1,True),(3,False),(3,True),(7,False)):continue
 p,q=rec['metric'];pv=vertices(p,PD);qv=vertices(q,QD)
 ring=[pv]
 for _ in range(11):ring.append(place_on_edge(pv,3,ring[-1][1],ring[-1][0]))
 first=ring[0];prev=ring[1]
 top=endpoint_placements(qv,0,first[0],first[4],prev[0])
 for flip,target,side,cand in top:
  conflicts=[i for i,tile in enumerate(ring) if overlap_int(cand,tile)]
  seam_hits=[(i,e) for i,tile in enumerate(ring) for e in (0,1) if cand[3]==tile[e]]
  print('Q150_RING',rec['reverse'],(flip,target,side),'Q3',tuple(map(float,cand[3])),
        'P_conflicts',conflicts,'seam_hits',seam_hits,flush=True)

for rec in records:
 if (rec['corner'],rec['reverse']) not in ((1,True),(3,False),(3,True),(7,False)):continue
 p,q=rec['metric'];pv=vertices(p,PD);qv=vertices(q,QD)
 ring=[pv]
 for _ in range(11):ring.append(place_on_edge(pv,3,ring[-1][1],ring[-1][0]))
 options=[]
 for i in range(12):
  cur,nxt=ring[i],ring[(i+1)%12]
  unique=[]
  for _,_,_,cand in endpoint_placements(qv,0,cur[0],cur[4],nxt[0]):
   if cand not in unique and all(not overlap_int(cand,tile) for tile in ring):unique.append(cand)
  options.append(unique)
 conflict={}
 for i in range(12):
  for a in range(len(options[i])):
   for j in range(i+1,12):
    for b in range(len(options[j])):
     if overlap_int(options[i][a],options[j][b]):conflict[i,a,j,b]=True
 assignments=[]
 def backtrack(chosen):
  i=len(chosen)
  if i==12:
   assignments.append(tuple(chosen));return
  for a in range(len(options[i])):
   if all((j,chosen[j],i,a) not in conflict for j in range(i)):
    backtrack(chosen+[a])
 backtrack([])
 print('INNER_Q_RING',rec['corner'],rec['reverse'],'options',[len(x) for x in options],
       'conflict_edges',len(conflict),'assignments',len(assignments),
       'example',assignments[:1],flush=True)

def seam_endpoint_atlas(p,q):
  # All native full-edge P/P pairings on the two t sides, including reflected
  # copies. Each endpoint receives one trivalent third corner if possible.
  result=[]
  for a,b in product((0,3),repeat=2):
   for reflected in (False,True):
    endpoint_corners=[((a,b) if reflected else (a,(b+1)%5)),
                      (((a+1)%5,(b+1)%5) if reflected else ((a+1)%5,b))]
    completions=[]
    for ca,cb in endpoint_corners:
      need=360-PANG[ca]-PANG[cb]
      la=p[(ca-1)%5] if ca==a else p[ca]
      lb=p[(cb-1)%5] if cb==b else p[cb]
      hits=[]
      for species,A,L in (('P',PANG,p),('Q',QANG,q)):
       for h,ang in enumerate(A):
        if ang==need and {L[(h-1)%len(A)],L[h]}=={la,lb}:
         hits.append((species,h))
      completions.append(hits)
    if all(completions):
     result.append(dict(sides=(a,b),reflected=reflected,
                        corners=endpoint_corners,completions=completions))
  return result
for rec in records:
 p,q=rec['metric']
 print('P_SEAM_ENDPOINT_ATLAS',rec['corner'],rec['reverse'],
       seam_endpoint_atlas(p,q),flush=True)
