# Independent reconstruction from supporting lines, not producer cot helper.
zeta = QQbar.zeta(36)
def normal(deg):
    z = zeta**(deg//10)
    return vector(AA,[z.real(),z.imag()])
def polygon(degrees):
    ns = [normal(t) for t in degrees]
    vs = [matrix(AA,[ns[i-1],ns[i]]).solve_right(vector(AA,[1,1])) for i in range(len(ns))]
    lens = [(vs[(i+1)%len(ns)]-vs[i]).norm() for i in range(len(ns))]
    angs = [180-((degrees[i]-degrees[i-1])%360) for i in range(len(ns))]
    return angs,lens
pa,pl=polygon([0,90,160,230,300])
qa,ql=polygon([0,80,160,200,240,280,320])
assert pa==[120,90,110,110,110]
assert qa==[140,100,100,140,140,140,140]
h,a,b,b2,c=pl
d,f,d2,e,e2,e3,e4=ql
assert b==b2 and d==d2 and e==e2==e3==e4
assert 0<c<b<a and c<b<h and 0<e<d<f
r=b/e
assert r*e==b and c<r*e<h
print('PASS independent exact support-line vertices, native lengths, unique scale and fatal inequality')
