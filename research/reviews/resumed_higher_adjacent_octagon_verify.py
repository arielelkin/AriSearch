from sage.all import AA, vector, ceil, floor
# Independent verifier: direct trig vertex construction and separating axes.
# No producer import; no clipping; exact AA arithmetic throughout.
rt=AA(5).sqrt();ph=(1+rt)/2
cc=ph/2;ss=(10-2*rt).sqrt()/4
# Derive directions via algebraic complex multiplication, no matrix powers.
vectors=[vector(AA,[1,0])]
for k in range(1,10):
 xx,yy=vectors[-1];vectors.append(vector(AA,[cc*xx-ss*yy,ss*xx+cc*yy]))
a=ph+2;d=AA(1);b=c=AA(1)
Q=[vector(AA,[0,0])]
for size,k in zip([d,a,b,c,d,c,b,a],[0,2,3,4,5,6,7,8]):Q.append(Q[-1]+size*vectors[k])
assert Q[-1]==Q[0];Q=Q[:-1]
T=Q[5];D=Q[3];X=D+2*ph**2*vectors[1];Y=X+vectors[3];Z=Y-a*vectors[0]
P=[Q[4],D,X,Y,Z];L=D+X
S=vector(AA,[2*(L[0]-1),0]);assert T[0]==0 and T[1]>0 and S[0]>0
mate=[L-v for v in P]
def mirror(poly):return [vector(AA,[1-v[0],v[1]])+S for v in poly[::-1]]
polys=[Q,[L-v for v in Q],P,mate,mirror(P),mirror(mate)]
def cr(v,w):return v[0]*w[1]-v[1]*w[0]
def ar(p):return sum(cr(v,w)for v,w in zip(p,p[1:]+p[:1]))/2
for p in polys:assert all(cr(p[(i+1)%len(p)]-p[i],p[(i+2)%len(p)]-p[(i+1)%len(p)])>0 for i in range(len(p)))
assert sum(map(ar,polys))==S[0]*T[1]
# Interior-disjoint convex sets have a separating supporting edge of one
# polygon; exact weak separation accepts shared sides or vertices.
def separated(A,B):
 for p,q in [(A,B),(B,A)]:
  for i,v in enumerate(p):
   e=p[(i+1)%len(p)]-v
   if all(cr(e,w-v)<=0 for w in q):return True
 return False
checked=0
for i,A in enumerate(polys):
 for j,B in enumerate(polys):
  minx=min(v[0]for v in A);maxx=max(v[0]for v in A)
  miny=min(v[1]for v in A);maxy=max(v[1]for v in A)
  lowm=ceil((minx-max(v[0]for v in B))/S[0]);highm=floor((maxx-min(v[0]for v in B))/S[0])
  lown=ceil((miny-max(v[1]for v in B))/T[1]);highn=floor((maxy-min(v[1]for v in B))/T[1])
  for m in range(lowm,highm+1):
   for n in range(lown,highn+1):
    if i==j and m==n==0:continue
    shifted=[v+m*S+n*T for v in B]
    assert separated(A,shifted),(i,j,m,n)
    checked+=1
assert checked==44
# Angles and length classes verified from actual coordinates.
for p,cosines in [(P,[(1-rt)/4]*5),(Q,[(1-rt)/4]*2+[-(1+rt)/4]*6)]:
 for i,v in enumerate(p):
  x=p[i-1]-v;y=p[(i+1)%len(p)]-v
  assert x.dot_product(y)/(x.norm()*y.norm())==cosines[i]
assert (Q[1]-Q[0]).norm()==(Q[5]-Q[4]).norm()==1
assert len(P)==5 and len(Q)==8
print('PASS: independent exact six-face covering, 44 separating-axis tests, full translate domain, two classes, alpha-alpha/beta-beta equality')
