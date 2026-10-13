from sage.all import *
# Independent reconstruction of author fixture using support-line linear algebra.
r=AA(5).sqrt();c=(1+r)/4;s=(10-2*r).sqrt()/4
rot=matrix(AA,[[c,-s],[s,c]])
normals=[rot**k*vector(AA,[1,0]) for k in [0,2,4,5,6,7,8,9]]
vertices=[]
for i in range(8):
    mat=matrix(AA,[normals[i],normals[(i+1)%8]])
    vertices.append(mat.solve_right(vector(AA,[1,1])))
assert all(all(n*v<=1 for n in normals) for v in vertices)
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
assert all(cross(vertices[(i+1)%8]-vertices[i],vertices[(i+2)%8]-vertices[(i+1)%8])>0 for i in range(8))
lengths=[(vertices[i]-vertices[(i-1)%8]).norm() for i in range(8)]
t=s/c;u=(1-c)/s
assert lengths==[t+u,2*t,t+u,2*u,2*u,2*u,2*u,2*u]
assert 0<u<t and 2*u != 2*t
assert sum(ell==2*u for ell in lengths)==5
P=[(u/s)*(rot**(2*j)*vector(AA,[1,0])) for j in range(5)]
assert all((P[(j+1)%5]-P[j]).norm()==2*u for j in range(5))
# Half-angle tangent support construction gives required angle cosines.
cos108=(1-r)/4;cos144=-(1+r)/4
corner_cos=[]
for i in range(8):
    a=vertices[(i-1)%8]-vertices[i];b=vertices[(i+1)%8]-vertices[i]
    corner_cos.append(a.dot_product(b)/(a.norm()*b.norm()))
assert corner_cos==[cos108,cos108,cos144,cos144,cos144,cos144,cos144,cos144]
print('PASS: eight strict support vertices, exact angle word, unique alpha-alpha length, repeated others')
