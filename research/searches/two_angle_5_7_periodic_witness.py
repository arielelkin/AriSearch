"""Construct an exact periodic witness in the new two-angle (5,7) family."""
from sage.all import NumberField, PolynomialRing, QQ, QQbar
import json
R = PolynomialRing(QQ, 'x'); x = R.gen()
K = NumberField(x**12-x**10+x**8-x**6+x**4-x**2+1, 'w')
w = K.gen(); ii = w**7; z = w**4
C = lambda t: (t+t**(-1))/2
S = lambda t: (t-t**(-1))/(2*ii)
s1,s2,s3 = S(w**2),S(w**4),S(w**6)
lengths = [K(1)] * 7
lengths[5] = (2*s2-s1+s3)/(2*s3)
lengths[3] = 1+(s3/s1)*(lengths[5]-1)
lengths[0] = -sum(lengths[i]*C(z**i) for i in range(1,7))
add = lambda a,b: (a[0]+b[0],a[1]+b[1])
sub = lambda a,b: (a[0]-b[0],a[1]-b[1])
H = [(K(0),K(0))]
for i in range(7):
    H.append(add(H[-1], (lengths[i]*C(z**i), lengths[i]*S(z**i))))
assert H[-1] == (0,0)
H.pop()
d = {i: add(H[i],H[(i+1)%7]) for i in (0,2,4)}
u,v = sub(d[2],d[0]),sub(d[4],d[0])
c = add(sub(d[0],d[2]),d[4])
P = [H[6],H[0],sub(d[0],H[2]),add(sub(d[0],d[2]),H[4]),sub(c,H[6])]
H2 = [sub(d[0],p) for p in H]
P2 = [sub(c,p) for p in P]
enc = lambda t: [str(q) for q in K(t).list()]
point = lambda p: [enc(p[0]),enc(p[1])]
cert = {"field": {"polynomial_coefficients": [str(q) for q in K.polynomial().list()],
    "root_real_interval": ["97/100","98/100"], "root_imag_interval": ["22/100","23/100"]},
    "lengths": [enc(t) for t in lengths],
    "lattice": [point(u),point(v)],
    "tiles": [{"name":name,"type":kind,"vertices":[point(t) for t in poly]}
        for name,kind,poly in [("H0","H",H),("H1","H",H2),("P0","P",P),("P1","P",P2)]],
    "intended_angles": {"H": ["5/7"]*7, "P": ["5/7","4/7","4/7","4/7","4/7"]},
    "scope": "one doubly-periodic (5,7) tiling; does not kill all angle-family parameters"}
print(json.dumps(cert,indent=2,sort_keys=True))
