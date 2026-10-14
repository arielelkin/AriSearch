"""Independent exact checker for the midpoint thin four-P periodic escape.
Replay: mise exec -- conda run --no-capture-output -n arisearch sage research/reviews/current-exact-convex-source-six-hostile-check.py
Scope: one algebraic thin P, both parent parities, fan triangles, lattice.
The global plane argument is the separately reviewed PL homotopy proof.
"""
from sage.all import AA, QQ, vector

def det(x,y): return x[0]*y[1]-x[1]*y[0]
def turn(x): return vector(AA,[-x[1],x[0]])
def reflect(x): return vector(AA,[x[0],-x[1]])
def signed_area(p):
    return sum(det(p[i],p[(i+1)%len(p)]) for i in range(len(p)))/2
root=AA(5).sqrt()
cos18=(10+2*root).sqrt()/4
sin18=(root-1)/4
first=vector(AA,[cos18,-sin18])
second=vector(AA,[cos18,sin18])
zero=vector(AA,[0,0])
old=[zero,first,first+second,second]
epsilon=QQ(1)/100
bend=[]
for i in range(4):
    side=old[(i+1)%4]-old[i]
    bend.append((old[i]+old[(i+1)%4])/2+(-1 if i%2==0 else 1)*epsilon*turn(side))
centre=(first+second)/2
assert bend[2]==2*centre-bend[0]
assert bend[3]==2*centre-bend[1]
p=[old[0],bend[0],old[1],bend[1],bend[3]]
for i in range(5):
    for j in range(5):
        if j not in (i,(i+1)%5):
            assert det(p[(i+1)%5]-p[i],p[j]-p[i])>0
assert signed_area(p)==det(first,second)/2
def angle_cosine(index):
    v=p[(index-1)%5]-p[index]
    w=p[(index+1)%5]-p[index]
    return v.dot_product(w)/(v.norm()*w.norm())
assert angle_cosine(0)==-angle_cosine(2)
reflected_bends=[reflect(bend[(3-i)%4]) for i in range(4)]
assert bend[1]==reflected_bends[3]+first
assert bend[2]==reflected_bends[0]+second
assert bend[3]==reflected_bends[1]-first
assert bend[0]==reflected_bends[2]-second
for images in (bend,reflected_bends):
    for i in range(4):
        midpoint=(old[i]+old[(i+1)%4])/2
        for point in (midpoint,images[i]):
            assert det(point-old[i],centre-old[i])>0
            assert det(old[(i+1)%4]-point,centre-point)>0
assert epsilon<sin18/(2*cos18)
assert abs(det(first+second,first-second))==4*signed_area(p)
# Figure-1 Type2 uses a=EA,b=AB,c=BC,d=CD,e=DE.
# Reindex old P vertices D,E,A,B,C: a,d,c,e are four profile edges.
new=[p[3],p[4],p[0],p[1],p[2]]
lengths=[(new[(i+1)%5]-new[i]).norm()**2 for i in range(5)]
assert lengths[4]==lengths[2] and lengths[1]==lengths[3]
print("Independent thin-P convexity, checkerboard adjacency, homotopy endpoint determinants and four-P lattice passed")
