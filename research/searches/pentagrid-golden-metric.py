#!/usr/bin/env python3
"""Exact closed pentagons in a fixed golden-power alphabet."""
from itertools import product
import json
from pathlib import Path
from sage.all import AA, QQ, QQbar, CyclotomicField

K = CyclotomicField(10)
z = K.gen()
phi = z + 1/z
WORDS = {"U": (1,3,4,4,3), "V": (2,2,4,3,4), "W": (3,3,3,3,3)}

def coefficients(value):
    return [str(QQ(value[j])) for j in range(4)]

def real_sign(value):
    q = QQbar(value)
    assert q.imag() == 0
    return AA(q.real()) > 0

def make_polygon(word, exponents):
    directions = [K(1)]
    for a in word[:-1]:
        directions.append(directions[-1]*z**(5-a))
    vertices = [K(0)]
    for e, d in zip(exponents,directions):
        vertices.append(vertices[-1]+phi**e*d)
    if vertices[-1] != 0:
        return None
    for i in range(5):
        a,b = vertices[i],vertices[i+1]
        for j in range(5):
            if j in (i,(i+1)%5):
                continue
            cross = ((b-a).conjugate()*(vertices[j]-a)-(b-a)*(vertices[j]-a).conjugate())/(z-z.conjugate())
            assert real_sign(cross)
    for i in range(5):
        e0 = vertices[i+1]-vertices[i]
        e1 = vertices[(i+2)%5]-vertices[i+1]
        assert e1/e0/(phi**exponents[(i+1)%5]/phi**exponents[i]) == z**(5-word[i])
    return {"side_exponents": list(exponents), "vertices": [coefficients(v) for v in vertices[:-1]]}

def certificate():
    records=[]
    for name,word in WORDS.items():
        closed=[]
        for exponents in product(range(4),repeat=5):
            if min(exponents)!=0:
                continue
            p=make_polygon(word,exponents)
            if p is not None:
                closed.append(p)
        records.append({"name":name,"angles_after_sides_in_pi_over_5":list(word),"normalized_exponent_vectors_tested":4**5-3**5,"closed":closed})
    return {"field":{"polynomial":"x^4-x^3+x^2-x+1","embedding":"z=exp(pi*i/5), Im(z)>0, 4/5<Re(z)<81/100","phi":"z+z^(-1)"},"domain":"Each of U,V,W, e in {0,1,2,3}^5, min(e)=0; no geometric congruence reduction of length vectors","records":records}

if __name__ == "__main__":
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument("--output")
    args=parser.parse_args()
    out=certificate()
    payload=json.dumps(out,indent=2)+"\n"
    if args.output: Path(args.output).write_text(payload)
    else: print(payload,end="")
