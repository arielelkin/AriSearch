# Exact geometry and complete local-star obstruction; no numerical decisions.
K = CyclotomicField(18)
z = K.gen()
i = QQbar.zeta(4)
def normal(k):
    w = QQbar(z^k)
    return vector(AA, [w.real(), w.imag()])
def det(u,v):
    return u[0]*v[1]-u[1]*v[0]
for indices in [(0,4,8,12,16), (0,4,8,12,14,16)]:
    normals = [normal(k) for k in indices]
    vertices=[]
    for j,n in enumerate(normals):
        q=normals[(j+1)%len(normals)]
        d=det(n,q)
        assert d>0
        v=vector(AA,[(q[1]-n[1])/d,(n[0]-q[0])/d])
        assert n.dot_product(v)==1 and q.dot_product(v)==1
        assert all(t.dot_product(v)<=1 for t in normals)
        vertices.append(v)
    for j,v in enumerate(vertices):
        u=vertices[(j+1)%len(vertices)]-v
        w=vertices[(j+2)%len(vertices)]-vertices[(j+1)%len(vertices)]
        assert u.dot_product(u)>0 and det(u,w)>0
    gaps=[(indices[(j+1)%len(indices)]-indices[j])%18 for j in range(len(indices))]
    assert sum(gaps)==18 and all(g in [2,4] for g in gaps)
    print('verified exact convex polygon:',len(vertices),'angles',[180-20*g for g in gaps])
# Complete domain: every corner contributes at least 5, every straight sector 9.
solutions=[(a,b,c) for a in range(4) for b in range(3) for c in range(3)
           if a+b>=1 and 5*a+7*b+9*c==18]
assert solutions==[]
print('complete local star domain has no solution')
