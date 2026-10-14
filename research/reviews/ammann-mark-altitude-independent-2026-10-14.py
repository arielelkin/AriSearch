#!/usr/bin/env python3
"""Independent symbolic mark-table area derivation and exact convexity check.

Does not import the author's script. Heights remain symbolic for the area gate.
"""
from sage.all import AA, NumberField, PolynomialRing, QQ

t = PolynomialRing(QQ,'t').gen()
field = NumberField(t*t-t-1,'phi',embedding=(AA(1)+AA(5).sqrt())/2)
phi = field.gen()
ring = PolynomialRing(field,['hX','hY'])
hX,hY = ring.gens()
z = (3-phi)/4
heights = {'X':hX,'Y':hY}
fixture = (field(1)/10,field(1)/20)

def vector_sub(a,b):
    return tuple(x-y for x,y in zip(a,b))

def cross(a,b):
    return a[0]*b[1]-a[1]*b[0]

def signed_area(poly):
    return sum(cross(a,b) for a,b in zip(poly,poly[1:]+poly[:1]))/2

def apex(a,b,height,inside=True):
    dx,dy = vector_sub(b,a)
    assert dx*dx+z*dy*dy == 1
    direction = 1 if inside else -1
    return ((a[0]+b[0])/2-direction*z*height*dy,
            (a[1]+b[1])/2+direction*height*dx)

def check_strict_support(poly):
    values = [tuple(ring(q)(*fixture) for q in vertex) for vertex in poly]
    for i,a in enumerate(values):
        b = values[(i+1)%len(values)]
        for j,p in enumerate(values):
            if j not in (i,(i+1)%len(values)):
                assert AA(cross(vector_sub(b,a),vector_sub(p,a))) > 0

rows = 0
for typ,c,s,marks in [('thin',phi/2,field(1),'XXYY'),
                      ('thick',(phi-1)/2,phi,'XYYX')]:
    vertices = [(ring(0),ring(0)),(ring(1),ring(0)),(ring(1+c),ring(s)),(ring(c),ring(s))]
    coefficient = (1+2*c)/4 if typ=='thin' else (2*c-1)/4
    predicted = {ring(s/2)+coefficient*(hX-hY),ring(s/2)-coefficient*(hX-hY)}
    assert coefficient != 0
    for choice in (0,1):
        selected = (choice,(choice+2)%4)
        nodes = {j:apex(vertices[j],vertices[(j+1)%4],heights[marks[j]]) for j in selected}
        sectors=[]
        outputs=[]
        for j in range(4):
            a,b = vertices[j],vertices[(j+1)%4]
            if j in selected:
                triangle=[a,b,nodes[j]]
                sectors.append(triangle)
                assert signed_area(triangle)==heights[marks[j]]/2
            else:
                quad=[a,b,nodes[(j+1)%4],nodes[(j-1)%4]]
                sectors.append(quad)
                receiving=apex(a,b,heights[marks[j]],inside=False)
                pentagon=[a,receiving,b,*quad[2:]]
                assert len(pentagon)==5
                assert signed_area(pentagon)==signed_area(quad)+heights[marks[j]]/2
                check_strict_support(pentagon)
                outputs.append(signed_area(pentagon))
                rows += 1
        for sector in sectors:
            check_strict_support(sector)
        assert sum(map(signed_area,sectors))==s
        assert set(outputs)==predicted
        assert sum(outputs)==s
        assert outputs[0] != outputs[1]

assert rows==8
assert phi/2 != field(1)/2
assert (1+phi)/4 != 0 and (phi-2)/4 != 0
print('PASS: symbolic native-mark areas for both tree roles; eight exact strict pentagons; unequal pair means')
