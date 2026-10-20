"""Exact local escape gates for Astra's offset P5/H6 fixture.

Run from repository root under the arisearch environment.  This is not a
complete tiling search.
"""
from sage.all import AA, CyclotomicField
from importlib.util import spec_from_file_location, module_from_spec

K = CyclotomicField(36)
z = K.gen()
I = z**9
def u(d):
    assert d % 10 == 0
    return z**(d//10)
def re(v): return (v + v.conjugate())/2
def im(v): return (v - v.conjugate())/(2*I)
def cross(v,w): return re(v)*im(w) - im(v)*re(w)

w = -u(50) - K(3)/2*u(200) - K(1)/2*u(280)
p = cross(w,u(150))/cross(u(0),u(150))
q = cross(u(0),w)/cross(u(0),u(150))
L = p+q
w = -L*u(0)-u(50)-u(100)-u(230)/2
c = cross(w,u(280))/cross(u(180),u(280))
e = cross(u(180),w)/cross(u(180),u(280))
P = (p,K(1),q,K(3)/2,K(1)/2)
H = (L,K(1),K(1),c,K(1)/2,e)
assert sum((a*u(d) for a,d in zip(P,(0,50,150,200,280))),K(0)) == 0
assert sum((a*u(d) for a,d in zip(H,(0,50,100,180,230,280))),K(0)) == 0
assert all(AA(x)>0 for x in P+H)
assert AA(q)<AA(K(1)/2)<AA(K(1))<AA(p)<AA(K(3)/2)<AA(L)
assert AA(K(1))<AA(e)<AA(L)<AA(c)
assert AA(p)<AA(e)<AA(K(3)/2)
assert all(AA(x)<AA(L) for x in P)
assert all(AA(x)<AA(L) for x in H[1:] if x != c)

# At vertex 1 of a reflected H0/H0 seam, the two H1 rays each have
# length 1 and end in 130-degree corners.  The remaining angle is 100,
# which can only be filled by the four native 100-degree corners below.
# Each listed corner has an incident side longer than 1.  That side must
# align with one of the two H1 rays.  At its far endpoint the H corner is
# 130 degrees while the longer tile edge is straight: residual = 50 degrees.
corners_100 = {
    'P vertex 0': (P[4],P[0]),
    'P vertex 4': (P[3],P[4]),
    'H vertex 0': (H[5],H[0]),
    'H vertex 3': (H[2],H[3]),
}
assert all(any(AA(s)>1 for s in sides) for sides in corners_100.values())
assert min((80,100,130)) > 50
print('H0/H0 mirrored whole-side mate: impossible in any P/H plane tiling')
print('100-degree corner incident lengths:',
      {name:tuple(AA(x) for x in sides) for name,sides in corners_100.items()})

# There is a second opposite-interior whole-side placement: a half-turn,
# which swaps the H0 endpoints.  At either endpoint H100+H130 leaves one
# 130-degree cap between outward H1 (length 1) and H5 (length e) rays.
# If a cap side overruns one of those rays, its 130-degree far endpoint
# lies inside a straight cap side, leaving 50 degrees.  A shorter cap
# side may terminate inside a ray only if its far angle is <=100.
angle_words = {'P':(100,130,80,130,100),'H':(100,130,130,100,130,130)}
length_words = {'P':P,'H':H}
halfturn_caps=[]
for species in ('P','H'):
    angles=angle_words[species]; lengths=length_words[species]; n=len(angles)
    for v in range(n):
        if angles[v]!=130: continue
        incident=((v-1)%n,v)
        for along_one,along_e in (incident,incident[::-1]):
            def far(s): return (v-1)%n if s==(v-1)%n else (v+1)%n
            a,b=lengths[along_one],lengths[along_e]
            if AA(a)>1 or AA(b)>AA(e): continue
            if AA(a)<1 and angles[far(along_one)]>100: continue
            if AA(b)<AA(e) and angles[far(along_e)]>100: continue
            halfturn_caps.append((species,v,along_one,along_e))
assert halfturn_caps == [('P',1,1,0),('H',2,1,2)]
assert AA(e-p)>0 and AA(e-p)<AA(q)
assert AA(e-1)>0 and AA(e-1)<AA(q)
print('H0/H0 half-turn endpoint cap germs:',halfturn_caps)
print('H0/H0 half-turn mate: impossible in any P/H plane tiling')
print('Both opposite-interior H0/H0 whole-side placements excluded')

# Independent next-vertex gate for the constructor's named P0+P2 split.
# The P4 edge of length 1/2 ends at the midpoint E of the other P1 edge
# (length 1).  At E: flat P edge 180 + P vertex 4 angle 100, hence the
# only cap is P vertex 2 of angle 80.  Its side following the remaining
# half of P1 is either P2=q or P1=1.  Both possibilities fail at the next
# vertex, even before checking overlap with any other cap:
#  q<1/2: cap P3 (130 degrees) ends inside flat original P1;
#  1>1/2: original P1 (130 degrees) ends inside flat cap P1.
# Each leaves a 50-degree gap, below the minimum native angle 80.
assert (180+100+80)==360
assert AA(q)<AA(K(1)/2)<AA(K(1))
assert angle_words['P'][1]==angle_words['P'][3]==130
assert 180+130+50==360 and min(angle_words['P']+angle_words['H'])==80
print('Named P0+P2 H0 split: both P80 short-cap continuations fail at next T')

# H3 is longer than H0 and is the sole other possible single-side cover
# of H0.  If it covers H0, H0 vertex 1 cannot lie in H3's interior:
# 180+130 leaves only 50 degrees.  Hence it aligns with an H3 endpoint,
# while H0 vertex 0 lies in H3's interior.  There 180+100 leaves one
# P80 corner, namely P vertex 2.  One of its incident sides (P1=1 or
# P2=q) follows the outward H5 ray of length e.  Both are shorter than
# e; their far endpoints are P130 corners inside H5, leaving 50 degrees.
assert AA(c)>AA(L)
assert AA(e)>AA(P[1]) and AA(e)>AA(P[2])
assert (180+130+50)==360 and (180+100+80)==360
print('H3 single-side cover of H0: impossible in any P/H plane tiling')

# H0 vertex 1 has angle 130; its exterior 230 must split as 100+130.
# An H0-side guest shorter than L must end inside H0, where the flat
# host angle requires the guest endpoint angle at most 100.  Enumerate
# all 100- and 130-degree corners with their incident side endpoint.
short_options=[]
cover_options=[]
for species in ('P','H'):
    angles=angle_words[species]; lengths=length_words[species]; n=len(angles)
    for v in range(n):
        if angles[v] not in (100,130): continue
        for s,other in (((v-1)%n,(v-1)%n),(v,(v+1)%n)):
            if AA(lengths[s])<AA(L) and angles[other]<=100:
                short_options.append((species,v,s,angles[v],angles[other]))
            if AA(lengths[s])>=AA(L):
                cover_options.append((species,v,s,angles[v]))
assert short_options == [
    ('P',0,4,100,100),('P',1,0,130,100),('P',1,1,130,80),
    ('P',3,2,130,80),('P',3,3,130,100),('P',4,4,100,100),
    ('H',2,2,130,100),('H',5,5,130,100)]
assert sorted(cover_options) == sorted([
    ('H',0,0,100),('H',1,0,130),('H',3,3,100),('H',4,3,130)])
print('H0 vertex-1 short-side options:',short_options)

# H-only contacts cannot have T vertices: 180 + min(H angle)=280, and
# the remaining 80 degrees cannot accommodate a second H corner.
# Thus a H-only tiling is edge-to-edge.  At H vertex 0 the 100-degree
# corner needs two 130-degree corners linking its incident lengths e,L.
corners_130 = tuple((H[(i-1)%6],H[i]) for i in (1,2,4,5))
bridges = []
for a,b in corners_130:
    for left,mid in ((a,b),(b,a)):
        for cc,dd in corners_130:
            for mid2,right in ((cc,dd),(dd,cc)):
                if left == e and mid == mid2 and right == L:
                    bridges.append(((left,mid),(mid2,right)))
assert bridges == []
print('H-only edge-to-edge corner bridge: impossible')

# The standard complete convex-pentagon monohedral classification is
# imported as a conditional omission filter, not reproved here.
spec=spec_from_file_location('rao','research/searches/convex-substitution-shapes.py')
mod=module_from_spec(spec); spec.loader.exec_module(mod)
angles=(100,130,80,130,100)
hits=[]
for typ,(aeqs,leqs) in mod.RAO.items():
    for sign in (1,-1):
        for off in range(5):
            aa=[angles[(off+sign*i)%5] for i in range(5)]
            if not all(sum(co*x for co,x in zip(row,aa))==36*target for row,target in aeqs):
                continue
            smap=[(off+i)%5 if sign==1 else (off-i-1)%5 for i in range(5)]
            if all(sum((co*P[i] for co,i in zip(row,smap)),K(0))==0 for row in leqs):
                hits.append((typ,sign,off))
assert hits == []
print('P-only Rao type hits: none (conditional on imported classification)')
print('metric p,q,L,c,e:',*[AA(x) for x in (p,q,L,c,e)])
