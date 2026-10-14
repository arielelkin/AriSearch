import runpy,io,json
from contextlib import redirect_stdout
with redirect_stdout(io.StringIO()):d=runpy.run_path("research/searches/contact-structure-ammann-corner-triad-gate.py")
z=d["z"];cross=d["cross"];H=d["H"];A=[1+z-z*p for p in d["P1"]];B=[1+z+z**2-p for p in d["P2"]]
assert A[1]==B[3]==H[3]
assert A[2]==H[2] and B[2]==H[4] and A[0]==B[4]
faces=[H,A,B]
for i,F in enumerate(faces):
 for G in faces[i+1:]:assert any(all(cross(F[(k+1)%len(F)]-p,q-p)<=0 for q in G) for k,p in enumerate(F))
edges=[(p,F[(i+1)%len(F)]) for F in faces for i,p in enumerate(F)]
outer=[e for e in edges if (e[1],e[0]) not in edges]
assert len(outer)==10
word=[outer[0][0]]
while len(word)<len(outer):
 nxt=[q for p,q in outer if p==word[-1]];assert len(nxt)==1;word.append(nxt[0])
assert (word[-1],word[0]) in outer and len(set(word))==len(word)
turns=[cross(word[i]-word[i-1],word[(i+1)%len(word)]-word[i]) for i in range(len(word))]
refs=[i for i,t in enumerate(turns) if t<0]
assert all(t!=0 for t in turns)
assert refs==[2,8] and {word[i] for i in refs}=={H[2],H[4]}
print(json.dumps(dict(outer_sides=len(word),flat=[i for i,t in enumerate(turns) if t==0],reflex=refs,vertices=[[str(q.real()),str(q.imag())]for q in word]),indent=2))

F=[z,H[5],H[0],H[1],H[2]]
G=[H[2],A[3],A[4],1+z,B[0],B[1],z]
assert F==word[8:]+word[:3] and G==word[2:9]
assert len(F)==5 and len(G)==7
for C in [F,G]:assert all(cross(C[(i+1)%len(C)]-p,q-p)>0 for i,p in enumerate(C) for j,q in enumerate(C) if j not in (i,(i+1)%len(C)))
def area(C):return sum(cross(p,C[(i+1)%len(C)]) for i,p in enumerate(C))/2
assert area(F)+area(G)==sum(area(C)for C in faces)
from sage.all import PolynomialRing,QQ,NumberField,QQbar
Z=PolynomialRing(QQ,"z");zz=Z.gen();K=NumberField(zz**4-zz**3+zz**2-zz+1,"zeta",embedding=QQbar.zeta(10))
print(json.dumps(dict(field="zeta=exp(i*pi/5)",P5=[str(K(p))for p in F],Q7=[str(K(p))for p in G],scope="Exact LOCAL convex two-class replacement only; global source partition and reverse forcing unproved"),indent=2))
