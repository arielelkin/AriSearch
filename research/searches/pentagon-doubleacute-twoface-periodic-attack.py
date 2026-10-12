#!/usr/bin/env python3
"""Authorized two-face weak-hex periodic escape attempt; positive witness gate.
Domain25splitchoices x3index-twoHNF tori x144full placements. Flat corners
are retained in the Euclidean gluing; no strict-six-corner theorem imported.
"""
import argparse,itertools,json,time
from pathlib import Path
from sage.all import QuadraticField,PolynomialRing,AA,QQbar,QQ,matrix,Polyhedron,vector
import z3
K=QuadraticField(3,'r',embedding=AA(3).sqrt());r=K.gen();R=PolynomialRing(K,'cA,dA,eA,cB,dB,eB,hA,hB');X=R.gens()
ROOT=z3.simplify(z3.Sqrt(z3.RealVal(3)));Y=[z3.Real(str(v)) for v in X]
D=((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1));PLACEMENTS=[(a,s) for s in (1,-1) for a in range(6)]
ANGLE=(60,60,150,120,150)
def source(i):
 c,d,e=X[3*i:3*i+3];return (e+(c+2*d)/r,e+(d-c)/r,c,d,e)
L=[source(0),source(1)]
def coefficient(a):
 aa,bb=K(a).list();return z3.RealVal(str(aa))+z3.RealVal(str(bb))*ROOT

def convert(p):
 out=z3.RealVal(0)
 for powers,a in R(p).dict().items():
  term=coefficient(a)
  for y,n in zip(Y,powers):
   if n:term*=y**int(n)
  out+=term
 return out

def template(i,j):
 angles=list(ANGLE);angles.insert(j+1,180)
 lengths=list(L[i]);lengths[j:j+1]=[X[6+i],L[i][j]-X[6+i]]
 return angles,lengths

def decode(value):
 if z3.is_rational_value(value):
  v=QQ(value.numerator_as_long())/value.denominator_as_long();return QQbar(v),{'rational':str(v)}
 assert z3.is_algebraic_value(value)
 coefficients=[QQ(str(c)) for c in value.poly()];P=PolynomialRing(QQ,'t');poly=P(coefficients);roots=sorted([a for a,n in poly.roots(QQbar) if a.imag()==0],key=lambda a:AA(a.real()));index=value.index();v=roots[index-1]
 return v,{'polynomial_coefficients':list(map(str,coefficients)),'real_root_index':index,'sexpr':value.sexpr()}

def encode_real(v):
 v=AA(v)
 try:return {'rational':str(QQ(v))}
 except (TypeError,ValueError):
  poly=v.minpoly();roots=sorted([a for a,n in poly.roots(AA)]);index=roots.index(v)+1
  return {'polynomial_coefficients':list(map(str,poly.list())),'real_root_index':index}

def field_primal(equations,ja,jb,basis):
 space=basis.row_space()
 def coefficients(p):return vector(K,[R(p).monomial_coefficient(x) for x in X])
 positive=list(X[:6])+[L[0][1],L[1][1],X[6],X[7],L[0][ja]-X[6],L[1][jb]-X[7]]
 forbidden=[X[0]-X[2],L[0][1]-X[1],X[3]-X[5],L[1][1]-X[4]]
 for p in positive:
  if coefficients(p) in space:return None,{'reason':'FORCED_ZERO_POSITIVE_FORM','form':str(p)}
 for p in forbidden:
  if coefficients(p) in space:return None,{'reason':'FORCED_MONOHEDRAL_LOCUS','form':str(p)}
 def row(p,epsilon=0):return [AA(K(R(p).constant_coefficient()))]+list(map(AA,coefficients(p)))+[AA(epsilon)]
 equalities=[row(p) for p in equations]+[row(X[2]-1)]
 base=[row(p,-1) for p in positive]+[[AA(1)]+[AA(0)]*8+[AA(-1)]]
 for signs in itertools.product((1,-1),repeat=4):
  inequalities=base+[row(sign*p,-1) for sign,p in zip(signs,forbidden)]
  poly=Polyhedron(ieqs=inequalities,eqns=equalities,base_ring=AA,backend='field')
  # All six shape parameters and both cuts are lower-bounded, so the
  # feasible polyhedron has no lineality. epsilon<=1 bounds its objective.
  vertices=[v for v in poly.vertices() if v[-1]>0]
  if vertices:return list(map(QQbar,vertices[0][:-1])),{'reason':'EXACT_ORDERED_FIELD_VERTEX','nonmonohedral_signs':signs,'positive_margin':str(vertices[0][-1])}
 return None,{'reason':'ALL_16_EXACT_SIGN_CONES_EMPTY_OR_ZERO_MARGIN'}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--mode',choices=('sample','module','family'),default='sample');ap.add_argument('--output',required=True);ap.add_argument('--timeout-ms',type=int,default=5000);ap.add_argument('--backend',choices=('nra','field'),default='nra');args=ap.parse_args()
 stats={'angle_cases':0,'length_queries':0,'unsat':0,'unknown':0};count=0;cache=set();witness=None;case_records=[];t0=time.monotonic()
 for ja,jb in itertools.product(range(5),repeat=2):
  templates=[template(0,ja),template(1,jb)]
  for lat in ((1,0,2),(2,0,1),(2,1,1)):
   n,s,m=lat;cells=[(x,y) for x in range(n) for y in range(m)];assert len(cells)==2
   def wrap(z):
    q=z[1]//m;return ((z[0]-s*q)%n,z[1]-m*q)
   for pa,pb in itertools.product(PLACEMENTS,repeat=2):
    count+=1;lab={cells[0]:(0,pa),cells[1]:(1,pb)}
    def corner(z,k):
     i,(a,sign)=lab[z];return templates[i][0][(a+sign*k)%6]
    def side(z,k):
     i,(a,sign)=lab[z];j=(a+k)%6 if sign==1 else (a-k-1)%6;return templates[i][1][j]
    vertices=[]
    for z in cells:
     for k in (0,1):
      b=wrap((z[0]+D[k][0],z[1]+D[k][1]));c=wrap((z[0]+D[k+1][0],z[1]+D[k+1][1]));vertices.append((corner(z,k),corner(b,k+2),corner(c,k+4)))
    if any(sum(v)!=360 for v in vertices):continue
    stats['angle_cases']+=1;equations=set()
    for z in cells:
     for k in range(6):
      w=wrap((z[0]+D[(k+1)%6][0],z[1]+D[(k+1)%6][1]));p=side(z,k)-side(w,(k+3)%6)
      if p:equations.add(p/p.leading_coefficient())
    if args.mode=='module':equations|={L[0][0]-X[1]-X[5],X[0]-L[1][0]}
    M=matrix(K,[[p.monomial_coefficient(x) for x in X] for p in equations]);basis=M.row_space().basis_matrix();key=(ja,jb,tuple(tuple(row) for row in basis))
    if key in cache:continue
    cache.add(key);stats['length_queries']+=1
    case={'split_sides':[ja,jb],'lattice':lat,'A_placement':pa,'B_placement':pb,'side_equations':[str(p) for p in equations]};case_records.append(case)
    if args.backend=='field':
     assert args.mode!='sample','Sample was already exactly screened with NRA; field mode for affine module/family only'
     exact,explanation=field_primal(equations,ja,jb,basis);case.update(explanation)
     if exact is None:stats['unsat']+=1;case['status']='UNSAT_EXACT_FIELD';continue
     encoded=[encode_real(v) for v in exact];model_text={str(x):str(v) for x,v in zip(X,exact)};case['status']='SAT_EXACT_FIELD'
    else:
     solver=z3.SolverFor('QF_NRA');solver.set(timeout=args.timeout_ms);solver.add(*[convert(p)==0 for p in equations])
     for i,j in ((0,ja),(1,jb)):
      solver.add(*[convert(v)>0 for v in X[3*i:3*i+3]],convert(L[i][1])>0,convert(X[6+i])>0,convert(L[i][j]-X[6+i])>0)
      solver.add(convert(X[3*i]-X[3*i+2])!=0,convert(L[i][1]-X[3*i+1])!=0)
     if args.mode=='sample':
      sample=(K(4),K(3),K(1),2*r-K(10)/3,2*r-K(10)/3,10/r-2)
      solver.add(*[Y[i]==coefficient(v) for i,v in enumerate(sample)])
     else:solver.add(Y[2]==1)
     answer=solver.check()
     if answer==z3.unknown:stats['unknown']+=1;continue
     if answer==z3.unsat:stats['unsat']+=1;continue
     model=solver.model();exact=[];encoded=[]
     for y in Y:
      v,code=decode(model.eval(y,model_completion=True));exact.append(v);encoded.append(code)
     model_text={str(y):model.eval(y,model_completion=True).sexpr() for y in Y}
     case['status']='SAT'
    def evaluate(p):return QQbar(R(p)(*exact))
    assert all(evaluate(p)==0 for p in equations)
    for i,j in ((0,ja),(1,jb)):
     assert all(AA(exact[k])>0 for k in range(3*i,3*i+3)) and AA(evaluate(L[i][1]))>0
     assert AA(exact[6+i])>0 and AA(evaluate(L[i][j]-X[6+i]))>0
     assert evaluate(X[3*i]-X[3*i+2])!=0 and evaluate(L[i][1]-X[3*i+1])!=0
    witness={'split_sides':[ja,jb],'lattice':lat,'placements':[[i,*lab[z][1]] for z,i in zip(cells,(0,1))],'parameters':encoded,'vertex_angle_triples':vertices,'side_equations':[str(p) for p in equations],'model':model_text}
    break
   if witness:break
  if witness:break
 result={'status':'EXACT_POSITIVE_WEAK_TORUS' if witness else ('UNKNOWN_CASES' if stats['unknown'] else 'NO_POSITIVE_TWOFACE_MODEL'),'mode':args.mode,'backend':args.backend,'case_records':case_records,'bounded_domain':'25splitchoices x3index2HNF x144rotated/reflectedlabelpairs;exactsideandcutconstraints','cases_visited':count,'full_cases':10800,'enumeration_complete':not witness,'complete':not witness and not stats['unknown'],'stats':stats,'witness':witness,'seconds':round(time.monotonic()-t0,3),'proof_scope':'Finite two-face weak-hex model only; negative not global. Positive requires independent flat-development/geometry witness review.'}
 Path(args.output).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
if __name__=='__main__':main()
