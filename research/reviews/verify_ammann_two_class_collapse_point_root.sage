K.<w> = CyclotomicField(10)
def cj(z): return z.galois_conjugate() if hasattr(z,'galois_conjugate') else K(z).complex_conjugate()
cj = lambda z: K(z).polynomial()(w^-1)        # complex conjugation: w -> w^-1
n2 = lambda z: cj(z)*z                         # |z|^2 (lies in real subfield)
r5 = 2*(w^2+w^8)+1; assert r5^2 == 5
s = (5+r5)/10; J = s + s*w
B,C,D = K(1),1+w,w
print("J is circumcentre of BCD:", n2(J-B)==n2(J-C)==n2(J-D))
Kp = w^2 + w^6*(J-1); Lp = 1 + w^7*(J-1-w)
J1 = 1 + w^4*(J-1); J2 = w + w^6*(J-w); J3 = 1+w+w^2-J
T = {'H6':[K(0),J1,K(1),J,w,J2],'P1':[K(0),J1,K(1),Lp,Kp],'P2':[Kp,Lp,1+w^2,J3,w^2]}
H = T['H6']; E=[H[(i+1)%6]-H[i] for i in range(6)]
print("H6 centrally symmetric (E_i + E_{i+3} = 0):", all(E[i]+E[i+3]==0 for i in range(3)))
def sig(P):
    n=len(P); return [(n2(P[(i+1)%n]-P[i]), (P[(i-1)%n]-P[i])*cj(P[(i+1)%n]-P[i]) + cj(P[(i-1)%n]-P[i])*(P[(i+1)%n]-P[i])) for i in range(n)]
def cross(u,v): return (cj(u)*v - u*cj(v))  # = 2i * cross product
CCe = [e for e in K.complex_embeddings() if abs(e(w)-CC(exp(I*pi/5)))<1e-9][0]
for k,P in T.items():
    n=len(P)
    turns=[(CCe(cross(P[i]-P[i-1],P[(i+1)%n]-P[i]))/(2*CC(0,1))).real() for i in range(n)]
    print(k,"convex(all left turns):",all(t>0 for t in turns), "sides^2:",[CCe(n2(P[(i+1)%n]-P[i])).real().n(15) for i in range(n)])
s1,s2=sig(T['P1']),sig(T['P2']); rots=lambda L:[L[i:]+L[:i] for i in range(len(L))]
print("P1 congruent to P2 (direct or mirror):", any(r==s1 for r in rots(s2)) or any(r==s1 for r in rots(s2[::-1])))
