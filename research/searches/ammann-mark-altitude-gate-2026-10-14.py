"""Exact four-case X/Y altitude interface test; no contact catalogue."""
import json,itertools,argparse
from pathlib import Path
import sympy as S
phi=(1+S.sqrt(5))/2;z=(3-phi)/4
hx=S.Rational(1,10);hy=S.Rational(1,20)
h={"X":hx,"Y":hy}
def sm(x):return S.simplify(S.expand(x))
def add(a,b):return tuple(sm(x+y) for x,y in zip(a,b))
def sub(a,b):return tuple(sm(x-y) for x,y in zip(a,b))
def mid(a,b):return tuple(sm((S.sympify(x)+S.sympify(y))/2) for x,y in zip(a,b))
def normal(e,k):return (-z*k*e[1],k*e[0])
def cross(a,b):return sm(a[0]*b[1]-a[1]*b[0])
def area(p):return sm(sum(cross(p[i],p[(i+1)%len(p)]) for i in range(len(p)))/2)
def support(p):
 for i in range(len(p)):
  for j in range(len(p)):
   if j not in (i,(i+1)%len(p)):assert cross(sub(p[(i+1)%len(p)],p[i]),sub(p[j],p[i])).is_positive is True

def sep(p,q):
 for r in (p,q):
  for i in range(len(r)):
   a,b=r[i],r[(i+1)%len(r)];e=sub(b,a)
   x=[cross(e,sub(v,a)) for v in p];y=[cross(e,sub(v,a)) for v in q]
   if (all(t.is_nonnegative is True for t in x) and all(t.is_nonpositive is True for t in y)) or (all(t.is_nonpositive is True for t in x) and all(t.is_nonnegative is True for t in y)):return True
 return False
rows=[]
for typ,c,s,marks in (("thin",phi/2,S.Integer(1),["X","X","Y","Y"]),("thick",(phi-1)/2,phi,["X","Y","Y","X"])):
 base=[(0,0),(1,0),(1+c,s),(c,s)]
 target={sm(s/2+(c+(S.Rational(1,2) if typ=="thin" else -S.Rational(1,2)))*(hx-hy)/2),sm(s/2-(c+(S.Rational(1,2) if typ=="thin" else -S.Rational(1,2)))*(hx-hy)/2)}
 for k in (0,1):
  R=base[k:]+base[:k];m=marks[k:]+marks[:k];A,B,C,D=R
  N=add(mid(A,B),normal(sub(B,A),h[m[0]]));M=add(mid(C,D),normal(sub(D,C),h[m[2]]))
  sectors=[[A,B,N],[B,C,M,N],[C,D,M],[D,A,N,M]]
  for poly in sectors:
   support(poly)
   for v in poly:
    for i in range(4):assert cross(sub(R[(i+1)%4],R[i]),sub(v,R[i])).is_nonnegative is True
  for v in (N,M):
   for i in range(4):assert cross(sub(R[(i+1)%4],R[i]),sub(v,R[i])).is_positive is True
  for p,q in itertools.combinations(sectors,2):assert sep(p,q)
  assert sm(sum(map(area,sectors))-s)==0
  out=[]
  for quad,mark in ((sectors[1],m[1]),(sectors[3],m[3])):
   U,V,*other=quad;t=sub(mid(U,V),normal(sub(V,U),h[mark]));pent=[U,t,V,*other]
   support(pent);assert sep(quad,[U,t,V]);assert sm(area(pent)-area(quad)-h[mark]/2)==0, (typ,k,mark,area(pent),area(quad),sm(area(pent)-area(quad)-h[mark]/2))
   out.append(pent)
  assert set(map(area,out))==target
  rows.append({"type":typ,"triangle_edge_choice":k,"native_cyclic_marks":marks,"triangle_marks":[m[0],m[2]],"receiving_marks":[m[1],m[3]],"output_areas":[str(area(p)) for p in out],"pentagons":[[[str(x),str(y)] for x,y in p] for p in out]})
# Independent symbolic shoelace expansion with generic physical coordinates.
cg,sg,xg,yg=S.symbols("c s hX hY",real=True)
quad_generic=[(1,0),(1+cg,sg),(S.Rational(1,2)+cg,sg-yg),(S.Rational(1,2),xg)]
assert sm(area(quad_generic)-(sg/2-(xg+yg)/4+cg*(xg-yg)/2))==0
allareas={sm(a) for row in rows for a in row["output_areas"]}
assert len(allareas)==4
# Parametric pair offsets are nonzero multiples of hx-hy and pair means unequal.
thin_coeff=sm((phi/2+S.Rational(1,2))/2);thick_coeff=sm(((phi-1)/2-S.Rational(1,2))/2)
assert thin_coeff.is_positive is True and thick_coeff.is_negative is True
assert sm(phi/2-S.Rational(1,2)).is_positive is True
result={"status":"GENUINE_GLOBAL_FRACTIONAL_PENTAGON_RULE; NONZERO_XY_HEIGHT_DIFFERENCE_REQUIRES_AT_LEAST_THREE_CLASSES", "coordinate_scale":"x+i*sin(pi/5)*y","height_X_normalized":str(hx),"height_Y_normalized":str(hy),"rows":rows,"fixture_distinct_area_count":len(allareas),"all_parameter_gate":"If delta !=0, each rhomb yields two distinct areas; two total area values would make both pairs equal and force identical means, contrary to thin/thick sine difference.","offset_coefficients_normalized":[str(thin_coeff),str(thick_coeff)],"equal_height_branch":"previous globally compatible two-class rule with periodic omission"}
ap=argparse.ArgumentParser();ap.add_argument("--output");a=ap.parse_args()
if a.output:Path(a.output).write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
