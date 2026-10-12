#!/usr/bin/env python3
"""Independent complex-coordinate audit of the tiny Ammann H gate."""
import json,time,hashlib
from pathlib import Path
from sage.all import CyclotomicField,QuadraticField,AA,PolynomialRing
import z3
ROOT=Path(__file__).resolve().parents[2];start=time.monotonic()
K=CyclotomicField(10);w=K.gen();F=QuadraticField(5,'sqrt5',embedding=AA(5).sqrt());phi=(1+F.gen())/2
R=PolynomialRing(F,['s','t','a','b','r','c']);s,t,a,b,r,c=R.gens();S=PolynomialRing(K,['s','t']);ss,tt=S.gens();J=ss+w*tt
Jp=1+w**4*(J-1);Jpp=w+w**6*(J-w);J2=1+w+w**2-J
KK=w**2+w**6*(J-1);LL=1+w**7*(J-1-w)
polys=[[S(0),Jp,S(1),J,S(w),Jpp],[S(0),Jp,S(1),LL,KK],[KK,LL,S(1+w**2),J2,S(w**2)]]
def conjugate(P):return S({mon:coef.conjugate() for mon,coef in S(P).dict().items()})
def real_to_R(P):
 out=R(0)
 for mon,coef in S(P).dict().items():
  # Fixed field Q(sqrt5) directly reconstructed as A+B*sqrt5.
  assert coef==coef.conjugate()
  v=list(coef.vector());ff=F(v[0]-v[2])-phi*v[3];assert K(ff[0])+K(ff[1])*(2*(w+w**-1)-1)==coef
  out+=ff*s**int(mon[0])*t**int(mon[1])
 return out
def norm(P):return real_to_R(S(P)*conjugate(P))
def area(P):
 summand=sum(conjugate(P[i])*P[(i+1)%len(P)] for i in range(len(P)))
 return real_to_R((summand-conjugate(summand))/(w-w**-1))
areas=[area(P) for P in polys];norms=[norm(J-1-w),norm(J-1),norm(J-w),norm(KK-LL)]
for P,word in zip(polys,['abbrra','abaca','crrab']):
 assert [norm(P[(i+1)%len(P)]-P[i]) for i in range(len(P))]==[norms['abrc'.index(q)] for q in word]
assert areas[0]==2 and areas[1]+areas[2]==1+F.gen()
record=json.loads((ROOT/'research/certificates/boundary-attachment-ammann-h-gate.json').read_text())
assert [R(record['side_norms'][q]) for q in 'abrc']==norms
assert [R(record['scaled_areas'][q]) for q in ('H','P1','P2')]==areas
base=[q*q-n for q,n in zip((a,b,r,c),norms)]
cases=[('P1+P2','b',areas[0]-areas[1]-areas[2],b-a-c),('P1+P2','r',areas[0]-areas[1]-areas[2],r-a-c),
 ('2P1','a',areas[0]-2*areas[1],a+c-r),('2P1','b',areas[0]-2*areas[1],2*a+c-r-b),('2P1','c',areas[0]-2*areas[1],2*a-r),
 ('2P2','a',areas[0]-2*areas[2],r+c-a),('2P2','b',areas[0]-2*areas[2],r+c-b)]
cases += [('2P1 negative orientation','a',areas[0]+2*areas[1],a+c-r),('2P1 negative orientation','b',areas[0]+2*areas[1],2*a+c-r-b),('2P1 negative orientation','c',areas[0]+2*areas[1],2*a-r),
 ('2P2 negative orientation','a',areas[0]+2*areas[2],r+c-a),('2P2 negative orientation','b',areas[0]+2*areas[2],r+c-b)]
assert len(record['rows'])==len(cases)==12
assert F.gen()>1  # Positive real embedding: unsigned mixed area obstruction.
results=[]
for case,row in zip(cases,record['rows']):
 fam,side,ae,pe=case;assert (fam,side)==(row['family'],row['shared_side']) and ae==R(row['area_equation']) and pe==R(row['perimeter_equation'])
 I=R.ideal(base+[ae,pe]);G=tuple(I.groebner_basis());assert G==tuple(R(g) for g in row['groebner_basis']);dim=int(I.dimension());assert dim==row['ideal_dimension']
 powers={}
 for g in G:
  exp=g.lm().exponents()[0];nz=[i for i,k in enumerate(exp) if k]
  if len(nz)==1:powers[str(R.gen(nz[0]))]=int(exp[nz[0]])
 if dim==0:assert len(powers)==6 and powers==row['pure_power_leading_monomials']
 else:assert dim==-1 and G==(R(1),)
 results.append({'family':fam,'side':side,'dimension':dim,'pure_powers':powers})
# Check whether strict positive orientation of H alone forces positive
# orientations of the two listed pentagons, so signed area equations are
# indeed necessary throughout the geometric strict-H domain.
root=z3.Real('positive_sqrt_five');xs,xt=z3.Reals('s t')
def cv(P):
 out=z3.RealVal(0)
 for mon,coef in R(P).dict().items():
  aa,bb=F(coef).vector();term=z3.RealVal(str(aa))+z3.RealVal(str(bb))*root
  for x,k in zip((xs,xt),mon[:2]):
   if k:term*=x**int(k)
  assert not any(mon[2:]);out+=term
 return out
turns=[]
for P in polys:
 seq=[]
 for i in range(len(P)):
  A=P[i]-P[i-1];B=P[(i+1)%len(P)]-P[i]
  seq.append(real_to_R((conjugate(A)*B-A*conjugate(B))/(w-w**-1)))
 turns.append(seq)
orientation=[]
for ci in (1,2):
 solver=z3.SolverFor('QF_NRA');solver.set(timeout=10000);solver.add(root*root==5,root>2,root<3)
 solver.add(*[cv(q)>0 for q in turns[0]],cv(areas[ci])<=0)
 answer=solver.check();orientation.append({'pentagon':ci,'H_positive_turns_and_nonpositive_pentagon_area':str(answer)})
 if answer==z3.sat:orientation[-1]['model']={str(x):solver.model().eval(x).sexpr() for x in (xs,xt)}
 path=ROOT/f'research/certificates/boundary-attachment-ammann-h-gate-review-orientation-{ci}.smt2';path.write_text(solver.sexpr()+'\n(check-sat)\n')
# The prescribed uncut shape family really has varying normalized angles.
# Two exact points in its strict convex domain give different cos^2 at
# P1's vertex 1; this is stronger than merely counting free coordinates.
angle_samples=[];P=polys[1];u=P[1]-P[2];v=P[3]-P[2]
dot=real_to_R((conjugate(u)*v+u*conjugate(v))/2);du,dv=norm(u),norm(v)
for sr,tr in ((F(1)/2,F(4)/5),(F(1)/2,F(3)/4)):
 vals=(sr,tr,F(0),F(0),F(0),F(0))
 for poly in polys:
  for i in range(len(poly)):
   edge=poly[(i+1)%len(poly)]-poly[i]
   for j in range(len(poly)):
    if j in (i,(i+1)%len(poly)):continue
    off=poly[j]-poly[i]
    determinant=real_to_R((conjugate(edge)*off-edge*conjugate(off))/(w-w**-1))
    assert determinant(*vals)>0
 ratio=dot(*vals)**2/(du(*vals)*dv(*vals));angle_samples.append({'s':str(sr),'t':str(tr),'P1_vertex_1_cosine_squared':str(ratio)})
assert angle_samples[0]['P1_vertex_1_cosine_squared']!=angle_samples[1]['P1_vertex_1_cosine_squared']
result={'side_words_independently_verified':True,'areas_independently_derived':[str(q) for q in areas],'mixed_area_difference':str(areas[0]-areas[1]-areas[2]),
 'twelve_ideal_bases_recomputed':results,'orientation_necessity_checks':orientation,'seconds':round(time.monotonic()-start,3),
 'mixed_unsigned_obstruction':'|A1|+|A2| >= |A1+A2| = 1+sqrt5 > 2 = |AH|',
 'uncut_shape_angle_variation_exact_samples':angle_samples,
 'producer_hash_matches':record['script_sha256']==hashlib.sha256((ROOT/'research/searches/boundary-attachment-ammann-h-gate.py').read_bytes()).hexdigest()}
(ROOT/'research/certificates/boundary-attachment-ammann-h-gate-review.json').write_text(json.dumps(result,indent=1)+'\n');print(json.dumps(result),flush=True)
