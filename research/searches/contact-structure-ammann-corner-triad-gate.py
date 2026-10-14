from sage.all import QQbar
import json
z=QQbar.zeta(10);J=QQbar(1)/2+QQbar(4)/5*z
jp=1+z**4*(J-1);jpp=z+z**6*(J-z)
K=z**2+z**6*(J-1);L=1+z**7*(J-1-z);J2=1+z+z**2-J
H=[QQbar(0),jp,QQbar(1),J,z,jpp]
P1=[QQbar(0),jp,QQbar(1),L,K];P2=[K,L,1+z**2,J2,z**2]
rot=z**(-2);A=[rot*q for q in P1];B=[rot*q for q in P2]
assert A[4]==B[0]==H[1] and B[4]==H[2] and A[0]==H[0]
assert A[3]==B[1]
faces=[H,A,B]
def cross(a,b):return (a.conjugate()*b).imag()
for F in faces:
 assert all(cross(F[(i+1)%len(F)]-p,q-p)>0 for i,p in enumerate(F) for j,q in enumerate(F) if j not in (i,(i+1)%len(F)))
for i,F in enumerate(faces):
 for G in faces[i+1:]:
  assert any(all(cross(F[(k+1)%len(F)]-p,q-p)<=0 for q in G) for k,p in enumerate(F))
edges=[(p,F[(i+1)%len(F)]) for F in faces for i,p in enumerate(F)]
outer=[e for e in edges if (e[1],e[0]) not in edges]
assert len(outer)==10
word=[outer[0][0]]
while len(word)<10:
 nxt=[q for p,q in outer if p==word[-1]];assert len(nxt)==1;word.append(nxt[0])
assert (word[-1],word[0]) in outer and len(set(word))==10
turns=[cross(word[i]-word[i-1],word[(i+1)%10]-word[i]) for i in range(10)]
assert all(t!=0 for t in turns)
reflex=[i for i,t in enumerate(turns) if t<0]
assert len(reflex)==2 and set(word[i] for i in reflex)=={H[2],A[3]}
d=(reflex[1]-reflex[0])%10;assert d in (3,7)
print(json.dumps(dict(scope="Exact J0 Ammann H-Jprime/P1-K/P2-K full-native-corner triad only",outer_sides=10,reflex_indices=reflex,reflex_boundary_distances=[d,10-d],forced_binary_piece_sides=[4,8],vertices=[[str(q.real()),str(q.imag())] for q in word]),indent=2))
