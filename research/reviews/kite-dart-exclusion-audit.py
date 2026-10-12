#!/usr/bin/env python3
"""Independent P2 rejection-witness and necessary-convexity audit.

Does not import producer modules. Reads recorded abstract embeddings and
rebuilds every dead local component, its boundary and exact straightness.
Uses its own real-coordinate / SMT encoder. Not a formal UNSAT certificate.
"""
import argparse, collections, itertools, json, time, hashlib
from pathlib import Path
from sage.all import CyclotomicField, QuadraticField, PolynomialRing, QQbar, AA
import z3
ROOT=Path(__file__).resolve().parents[2]
C=ROOT/'research/certificates'
K=CyclotomicField(10);w=K.gen();kp=w+w**-1
F=QuadraticField(5,'sqrt5',embedding=AA(5).sqrt());phi=(1+F.gen())/2
embed=K.hom([QQbar.zeta(10)])
def sign(q):
 a=AA(embed(q));return int(a>0)-int(a<0)
def split(q):
 a=list(K(q).vector());return F(a[0]-a[2])-phi*a[3],F(a[1])+phi*(a[2]+a[3])
def source(level):
 p=json.loads((C/f'penrose-kite-dart-patch{level}.json').read_text())
 V=[K(v) for v in p['verts']];owners=collections.defaultdict(list);stars=collections.defaultdict(list)
 for ri,(kind,gv,a) in enumerate(p['tiles']):
  for j,v in enumerate(gv):
   stars[v].append((ri,j));owners[frozenset((v,gv[(j+1)%4]))].append((ri,j))
 return p,V,owners,stars
T=json.loads((C/'penrose-kite-dart-recomposition-patch3.types.json').read_text())
p,V,owners,stars=source(3)
slots=[];segments=[]
for typ in T:
 sl={};sg=[]
 for pi,face in enumerate(typ['pieces']):
  local=[]
  for a,b in face:
   if a in '0123' and b in '0123' and (int(a)+1)%4==int(b):sl[int(a)]=pi
   else:local.append((a,b))
  sg.append(local)
 assert set(sl)==set(range(4));slots.append(sl);segments.append(sg)
def node(ri,s):
 return ('v',p['tiles'][ri][1][int(s)]) if s in '0123' else ('p',ri,s)
def point(nd):
 v=[K(0)]*5
 if nd[0]=='v':v[4]=V[nd[1]]
 else:
  _,ri,s=nd;kind,gv,a=p['tiles'][ri];v[4]=V[gv[0]]
  v[(0 if kind=='kite' else 2)+(s=='Q')]=w**a
 return tuple(v)
def diff(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a.conjugate()*b-a*b.conjugate())/(w-w.conjugate())
def simplified(cycle):
 forms=[point(nd) for nd in cycle]
 changed=True
 while changed:
  changed=False
  for j in range(len(forms)):
   A=diff(forms[j],forms[j-1]);B=diff(forms[(j+1)%len(forms)],forms[j])
   assert any(A) and any(B)
   k=next(i for i,q in enumerate(A) if q);ratio=B[k]/A[k]
   if ratio==ratio.conjugate() and all(y==ratio*x for x,y in zip(A,B)):
    assert sign(ratio)>0,'Identically backward spike'
    forms.pop(j);changed=True;break
 return forms

def witness(row):
 choices=[row['kite'],row['dart']];M={tuple(q) for q in row['witness']['pieces']};adj=collections.defaultdict(set);darts=[]
 for ri,pi in M:
  kind,gv,a=p['tiles'][ri];ti=choices[kind=='dart']
  assert 0<=pi<len(T[ti]['pieces'])
  for j,facepi in slots[ti].items():
   if facepi!=pi:continue
   os=owners[frozenset((gv[j],gv[(j+1)%4]))];assert len(os)==2,'Witness touches patch boundary'
   r2,s2=next((r,s) for r,s in os if r!=ri);k2=p['tiles'][r2][0];other=(r2,slots[choices[k2=='dart']][s2])
   assert other in M,'Witness is not a full dual component';adj[ri,pi].add(other)
  darts.extend((node(ri,a),node(ri,b)) for a,b in segments[ti][pi])
 seen=set();todo=[next(iter(M))]
 while todo:
  v=todo.pop()
  if v in seen:continue
  seen.add(v);todo.extend(adj[v]-seen)
 assert seen==M,'Witness component disconnected'
 status=row['dead'];ds=set(darts);assert len(ds)==len(darts)
 if status=='slit':assert any((b,a) in ds for a,b in darts);return
 assert not any((b,a) in ds for a,b in darts)
 out=collections.defaultdict(list)
 for a,b in darts:out[a].append(b)
 if status=='pinched-face':assert any(len(bs)>1 for bs in out.values());return
 assert all(len(bs)==1 for bs in out.values())
 start=darts[0][0];cyc=[start];cur=out[start][0]
 while cur!=start:
  assert cur not in cyc;cyc.append(cur);cur=out[cur][0]
 if status=='multiple-boundary-cycles':assert len(cyc)<len(darts);return
 assert len(cyc)==len(darts)
 forms=simplified(cyc)
 if status=='triangle-or-quadrilateral-escape':assert 3<=len(forms)<=4;return
 assert status=='fixed-reflex-corner'
 bad=False
 for j in range(len(forms)):
  A=diff(forms[j],forms[j-1]);B=diff(forms[(j+1)%len(forms)],forms[j])
  if not any(A[:4]) and not any(B[:4]) and sign(cross(A[4],B[4]))<0:bad=True
 assert bad

def validate_retained_faces(row):
 # Rebuild ALL dual components of an un-rejected recipe. Check that every
 # recorded class is the exact normalized metric of a genuine bounded face,
 # and that the class/count census contains every such face.
 choices=[row['kite'],row['dart']];adj=collections.defaultdict(set);boundary=set();allnodes=set()
 for ri,(kind,gv,orientation) in enumerate(p['tiles']):
  typ=choices[kind=='dart']
  for pi in range(len(T[typ]['pieces'])):allnodes.add((ri,pi))
 for edge,os in owners.items():
  nodes=[(ri,slots[choices[p['tiles'][ri][0]=='dart']][side]) for ri,side in os]
  if len(nodes)==1:boundary.add(nodes[0])
  else:
   A,B=nodes;adj[A].add(B);adj[B].add(A)
 R=PolynomialRing(F,[f'{prefix}{j}' for j in range(4) for prefix in ('s','t')]);X=R.gens()
 def metric(forms):
  points=[]
  for f in forms:
   aa,bb=split(f[4]);A=R(aa);B=R(bb)
   for j,q in enumerate(f[:4]):
    ca,cb=split(q);ss,tt=X[2*j],X[2*j+1]
    A+=ca*ss-cb*tt;B+=cb*ss+(ca+phi*cb)*tt
   points.append((A,B))
  D=[]
  for A,B in points:
   ds=[]
   for C,Dd in points:
    da,db=A-C,B-Dd;ds.append(da*da+phi*da*db+db*db)
   D.append(ds)
  n=len(forms)
  keys=[]
  for start in range(n):
   for o in (1,-1):
    perm=[(start+o*i)%n for i in range(n)]
    # Polynomial dictionaries are canonicalized without their display order.
    keys.append(tuple(tuple(sorted((tuple(mon),tuple(F(c).vector())) for mon,c in D[perm[i]][perm[j]].dict().items())) for i in range(n) for j in range(i+1,n)))
  return n,min(keys)
 measured=collections.Counter();unseen=set(allnodes);bounded=0
 while unseen:
  start=next(iter(unseen));component=set();todo=[start]
  while todo:
   v=todo.pop()
   if v in component:continue
   component.add(v);todo.extend(adj[v]-component)
  unseen-=component
  if component&boundary:continue
  darts=[]
  for ri,pi in component:
   typ=choices[p['tiles'][ri][0]=='dart'];darts.extend((node(ri,a),node(ri,b)) for a,b in segments[typ][pi])
  nxt=dict(darts);assert len(nxt)==len(darts)
  start=darts[0][0];cycle=[start];cur=nxt[start]
  while cur!=start:
   assert cur not in cycle;cycle.append(cur);cur=nxt[cur]
  assert len(cycle)==len(darts)
  measured[metric(simplified(cycle))]+=1;bounded+=1
 recorded=collections.Counter()
 for c in row['classes']:
  forms=[]
  for f in c['forms']:
   coeff=[K(0)]*5
   for key,vec in f.items():coeff[4 if key=='c' else int(key)]=K(vec)
   forms.append(tuple(coeff))
  recorded[metric(forms)]+=c['count']
 assert recorded==measured
 assert bounded==row['interior_faces']
 return bounded

def closed_stars(level):
 pp,VV,oo,ss=source(level);matches=[]
 def direction(z):
  for a in range(10):
   q=z/w**a
   if q==q.conjugate() and sign(q)>0:return a
  raise AssertionError('Not a decagonal direction')
 for vertex,inc in ss.items():
  signature=sorted((pp['tiles'][ri][0],j) for ri,j in inc)
  if signature!=[('dart',2),('kite',1),('kite',3)]:continue
  sectors=[]
  for ri,j in inc:
   kind,gv,a=pp['tiles'][ri];lo=direction(VV[gv[(j+1)%4]]-VV[vertex]);hi=direction(VV[gv[j-1]]-VV[vertex])
   sector=[(lo+k)%10 for k in range((hi-lo)%10)]
   assert len(sector)==(6 if kind=='dart' else 2)
   sectors.extend(sector)
   assert all(len(oo[frozenset((vertex,gv[k]))])==2 for k in ((j+1)%4,(j-1)%4))
  assert sorted(sectors)==list(range(10));matches.append({'vertex':vertex,'incident':inc})
 assert matches
 for td in (54,1,3):
  degree=sum(str(2) in e for e in T[td]['edges'])
  assert degree==1
 assert not T[0]['edges']
 return {'deflations':level,'exact_closed_star_count':len(matches),'example':matches[0],
  'signature':[['dart',2],['kite',1],['kite',3]],'angle_units_pi_over_5':[6,2,2],
  'pairs_excluded':[[0,0],[0,54],[0,1],[0,3]],'nonempty_pairs_boundary_degree_at_witness':1}

def coordinates(row):
 active=sorted({int(k) for c in row['classes'] for f in c['forms'] for k in f if k!='c'})
 R=PolynomialRing(F,[f'{prefix}{p}' for p in active for prefix in ('s','t')]);X=R.gens()
 P=[]
 for c in row['classes']:
  seq=[]
  for f in c['forms']:
   a=b=R(0)
   for key,vec in f.items():
    ca,cb=split(K(vec))
    if key=='c':a+=ca;b+=cb
    else:
     i=active.index(int(key));s,t=X[2*i:2*i+2]
     # (ca+cb*w)*(s+t*w), w^2=phi*w-1.
     a+=ca*s-cb*t;b+=cb*s+(ca+phi*cb)*t
   seq.append((a,b))
  P.append(seq)
 return R,active,P

def weak_check(row,timeout):
 R,active,P=coordinates(row);X=R.gens()
 root=z3.Real('sqrt_five');Y=[z3.Real(str(x)) for x in X]
 def cv(q):
  total=z3.RealVal(0)
  for mon,coeff in R(q).dict().items():
   aa,bb=F(coeff).vector();term=z3.RealVal(str(aa))+z3.RealVal(str(bb))*root
   for y,k in zip(Y,mon):
    if k:term*=y**int(k)
   total+=term
  return total
 solver=z3.SolverFor('QF_NRA');solver.set(timeout=timeout);solver.add(root**2==5,root>2,root<3)
 def det(A,B,C):return (B[0]-A[0])*(C[1]-A[1])-(B[1]-A[1])*(C[0]-A[0])
 def norm(A,B):
  a,b=A[0]-B[0],A[1]-B[1];return a*a+phi*a*b+b*b
 for seq in P:
  turns=[cv(det(seq[i-1],seq[i],seq[(i+1)%len(seq)])) for i in range(len(seq))]
  solver.add(*[q>=0 for q in turns],z3.Sum([z3.If(q>0,1,0) for q in turns])>=5)
  solver.add(cv(sum(det((R(0),R(0)),seq[i],seq[(i+1)%len(seq)]) for i in range(len(seq))))>0)
  solver.add(*[cv(norm(seq[i],seq[(i+1)%len(seq)]))>0 for i in range(len(seq))])
 for i,k in enumerate(active):
  A=(X[2*i],X[2*i+1]);ref=[(R(0),R(0)),(R(1),R(0)),(R(0),R(1 if k<2 else 1/phi)),(R(-1),R(phi))]
  if k<2:solver.add(*[cv(det(ref[j],ref[(j+1)%4],A))>0 for j in range(4)])
  else:
   o,b,c,d=ref
   solver.add(z3.Or(z3.And(cv(det(o,b,A))>0,cv(det(b,c,A))>0,cv(det(c,o,A))>=0),
    z3.And(cv(det(o,c,A))>=0,cv(det(c,d,A))>0,cv(det(d,o,A))>0)))
 for a,b in ((0,1),(2,3)):
  if a in active and b in active:
   i,j=active.index(a),active.index(b);solver.add(cv(norm((X[2*i],X[2*i+1]),(X[2*j],X[2*j+1])))>0)
 start=time.monotonic();ans=solver.check();result={'pair':[row['kite'],row['dart']],'status':str(ans),'seconds':round(time.monotonic()-start,3)}
 if ans==z3.unknown:result['reason_unknown']=solver.reason_unknown()
 return result,solver.sexpr()

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);ap.add_argument('--timeout-ms',type=int,default=15000);args=ap.parse_args();start=time.monotonic()
 rows=[json.loads(x) for x in (C/'penrose-kite-dart-recomposition-patch3.jsonl').read_text().splitlines()]
 assert len(rows)==9604 and {(r['kite'],r['dart']) for r in rows}==set(itertools.product(range(98),repeat=2))
 checked=0
 for r in rows:
  if r['dead'] is not None:witness(r);checked+=1
 print(json.dumps({'dead_witnesses_independently_validated':checked}),flush=True)
 retained_checked=sum(validate_retained_faces(r) for r in rows if r['dead'] is None)
 print(json.dumps({'retained_bounded_faces_and_classes_independently_verified':retained_checked}),flush=True)
 result={'retained_bounded_faces_and_classes_independently_verified':retained_checked,'dead_witnesses_independently_validated':checked,'rejection_counts':dict(collections.Counter(r['dead'] or 'retained' for r in rows)),
 'four_template_local_witnesses':[closed_stars(3),closed_stars(4)],'weak_convexity_independent_encoder':[],
 'scope':'Recorded embedding domain; source languages containing the exact witnessed patch/star. Solver replay is not a formally checked UNSAT proof.'}
 out=Path(args.output)
 for r in rows:
  if r['dead'] is None and r['interior_faces']:
   answer,smt=weak_check(r,args.timeout_ms);result['weak_convexity_independent_encoder'].append(answer)
   out.with_suffix(f'.{r["kite"]}-{r["dart"]}.smt2').write_text(smt+'\n(check-sat)\n')
   out.write_text(json.dumps(result,indent=1)+'\n');print(json.dumps(answer),flush=True)
 result['elapsed_seconds']=round(time.monotonic()-start,3);out.write_text(json.dumps(result,indent=1)+'\n')
if __name__=='__main__':main()
