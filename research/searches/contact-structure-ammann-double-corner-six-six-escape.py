import runpy,io,json
from contextlib import redirect_stdout
with redirect_stdout(io.StringIO()):d=runpy.run_path("research/searches/contact-structure-ammann-double-corner-gate.py")
patch=d["patches"]["P1","P2"]
W=patch["word"];cross=d["cross"];i,j=patch["reflex"]
assert (len(W),i,j)==(10,2,7)
P=W[i:j+1];Q=W[j:]+W[:i+1]
for F in [P,Q]:assert len(F)==6 and all(cross(F[(i+1)%6]-p,q-p)>0 for i,p in enumerate(F) for j,q in enumerate(F) if j not in (i,(i+1)%6))
def area(H):return sum(cross(p,H[(i+1)%len(H)])for i,p in enumerate(H))/2
assert area(P)+area(Q)==sum(area(H)for H in patch["faces"])
assert Q[1]-Q[0]==-(Q[4]-Q[3])
# Rotate the native indices so the reviewed general theorem applies as e2=-e5.
F=Q[4:]+Q[:4];origin=F[0];F=[p-origin for p in F]
assert F[3]==F[2]+F[5]
a=F[2];b=F[3]+F[4]-F[1];T=F[1];G=[T-p for p in F]
assert cross(a,b)==2*area(F)>0
pairs=[(0,0,1,0,0,0),(0,1,1,1,1,0),(0,2,0,5,1,0),(0,3,1,3,0,1),(0,4,1,4,-1,1),(1,2,1,5,-1,0)]
reps=[F,G]
for f,i,g,j,m,n in pairs:
 shift=m*a+n*b
 assert reps[f][i]==reps[g][(j+1)%6]+shift
 assert reps[f][(i+1)%6]==reps[g][j]+shift
# Exact retained coefficients in the canonical tenth-cyclotomic field.
from sage.all import PolynomialRing,QQ,NumberField,QQbar
Z=PolynomialRing(QQ,"z");z=Z.gen();K=NumberField(z**4-z**3+z**2-z+1,"zeta",embedding=QQbar.zeta(10))
encode=lambda v:[str(K(p))for p in v]
print(json.dumps(dict(scope="P1/P2 exterior double-corner fixture produces two convex hexagons; SECOND has exact Q-only rank-two periodic omission",field="zeta^4-zeta^3+zeta^2-zeta+1=0; zeta=exp(i*pi/5)",hexagon1=encode(P),hexagon2=encode(Q),normalized_reps=[encode(F),encode(G)],periods=encode([a,b]),pairs=pairs,area=str(area(F))),indent=2))
