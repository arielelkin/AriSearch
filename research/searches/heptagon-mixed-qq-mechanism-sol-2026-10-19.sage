# Exact Laurent-polynomial identity checks; t formally represents exp(i*d).
K = CyclotomicField(20)
w = K.gen()
R = LaurentPolynomialRing(K, 't')
t = R.gen()
i = w**5

def bar(f):
    return R({-int(k): K(v).conjugate() for k,v in R(f).dict().items()})
def cross(u,v):
    return (bar(u)*v-u*bar(v))/(2*i)
def e(c,k=0):
    assert c % 18 == 0
    return w**(c//18)*t**k
cos18=(w+w**(-1))/2
cos54=(w**3+w**(-3))/2
sin_d=(t-t**(-1))/(2*i)
cos_d=(t+t**(-1))/2
U=e(162,1)
V=e(54,1)+e(270,1)
S=e(0)+e(108,2)+e(216,2)+e(324)
assert cross(U,V)==0
assert cross(U,S)==2*(cos18+cos54)*sin_d
assert cross(U,e(162,1))==0
assert cross(U,e(162,3))==2*sin_d*cos_d
# Hence z*2*sin(d)*cos(d)=-2*(cos18+cos54)*sin(d).
print('PASS: exact formal all-parameter closure obstructions for ABBCBCC and ABBBCCC')
