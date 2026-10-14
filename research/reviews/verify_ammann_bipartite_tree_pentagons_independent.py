"""Independent SymPy support-axis audit of two-node Ammann surgery."""
import itertools
import sympy as S
phi=(1+S.sqrt(5))/2
z=(3-phi)/4
h=S.Rational(1,10)
def simp(x):return S.simplify(S.expand(x))
def sub(a,b):return tuple(simp(x-y) for x,y in zip(a,b))
def det(a,b):return simp(a[0]*b[1]-a[1]*b[0])
def ar(p):return simp(sum(det(p[i],p[(i+1)%len(p)]) for i in range(len(p)))/2)
def positive(x):assert simp(x).is_positive is True, x
def support(p):
 for i in range(len(p)):
  e=sub(p[(i+1)%len(p)],p[i])
  for j in range(len(p)):
   if j not in (i,(i+1)%len(p)):positive(det(e,sub(p[j],p[i])))
def inside(p,v):
 for a,b in zip(p,p[1:]+p[:1]):assert simp(det(sub(b,a),sub(v,a))).is_nonnegative is True

def separated(p,q):
 # One complete supporting axis separates interiors. Exact interval comparison.
 for r in (p,q):
  for a,b in zip(r,r[1:]+r[:1]):
   edge=sub(b,a)
   vp=[det(edge,sub(v,a)) for v in p]
   vq=[det(edge,sub(v,a)) for v in q]
   if (all(x.is_nonnegative is True for x in vp) and all(x.is_nonpositive is True for x in vq)) or (all(x.is_nonpositive is True for x in vp) and all(x.is_nonnegative is True for x in vq)):return True
 return False
for c,s in ((phi/2,S.Integer(1)),((phi-1)/2,phi)):
 A=(0,0);B=(1,0);C=(1+c,s);D=(c,s);R=[A,B,C,D]
 N=(S.Rational(1,2),h);M=(S.Rational(1,2)+c,s-h)
 cells=[[A,B,N],[B,C,M,N],[C,D,M],[D,A,N,M]]
 support(R)
 for cell in cells:
  support(cell)
  for v in cell:inside(R,v)
 for x,y in itertools.combinations(cells,2):assert separated(x,y)
 assert simp(sum(ar(x) for x in cells)-ar(R))==0
 # Reflection fixes A and C and exchanges B,D; metric uses y physical scale sqrt(z).
 def refl(v):return (simp(c*v[0]+z*s*v[1]),simp(s*v[0]-c*v[1]))
 assert refl(B)==D and refl(D)==B and refl(C)==C
 assert simp(c*c+z*s*s-1)==0
 def halfturn(v):return (simp(C[0]-v[0]),simp(C[1]-v[1]))
 assert set(map(halfturn,cells[0]))==set(cells[2])
 assert set(map(halfturn,cells[1]))==set(cells[3])
 # Outside apex on BC, reconstructed from physical unit normal.
 T=(simp(1+c/2+h*z*s),simp(s/2-h*c))
 poly=[B,T,C,M,N]
 support(poly)
 assert separated(cells[1],[B,T,C])
 assert simp(ar(poly)-ar(cells[1])-ar([B,T,C]))==0
 assert simp(ar(poly)-s/2)==0
 # Both triangles have unit physical base and common physical altitude.
 def norm2(v):return simp(v[0]**2+z*v[1]**2)
 assert norm2(sub(C,B))==1
 assert simp(det(sub(C,B),sub(T,B)))==-h
 # Alternate coloring: reflected original sectors exchange edge roles exactly.
 for cell in cells:support(list(reversed([refl(v) for v in cell])))
 positive(s/2-h*(1+c));positive(s/2-h*(1-c))
 print('PASS support, exact partition, glued strict pentagon, reflection, carrier:',c,s)
print('PASS independent two-row audit; global bipartition and decoder proof require accompanying argument')
