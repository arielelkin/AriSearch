# One exact symmetric pentagon / two-private octagon periodic carrier

Date:2026-10-13. Status: SUPERSEDED by the all-metric symbolic carrier at
[contact-symmetric-two-private-distance-three-periodic-carrier.md](contact-symmetric-two-private-distance-three-periodic-carrier.md).
The canonical producer is research/searches/contact-symmetric-two-private-symbolic-carrier.py;
this fixed-point extraction is retained only as construction history, not a
separate result or replay registration.
Scope: one explicitly fixed pair, outside the completed nonsymmetric family.

Let r=sqrt2,u=1,w=5/4 and b=(3-r)/8. The pentagon P has cyclic vertices
(0,-w),(b,-5/8-r/2),(b+r/2,-5/8),(b,-5/8+r/2),(0,0).
It has one90 and four112.5 corners, reflection symmetry, and native lengths
(x,1,1,x,5/4). The octagon Q starts at0 and has successive native directions
0,45,...315 degrees and length word(H,1,1,H,1,5/4,5/4,1), H=(5+r)/4.
Exactly its slots0,3 are private relative to P. P and Q are distinct genuine
convex shapes (five versus eight sides). All copies below are ordinary allowed
isometries; no adjacency rule is imposed on other admitted tilings.

The exact certificate is
research/searches/contact-symmetric-two-private-periodic-carrier.py.
It explicitly lists six CCW representatives: Q, its halfturn across side0,
and four P copies F1,F2,F4,F7. It gives lattice vectors

    V=(1+5r/8,9/4+13r/8), U=(-13/8-9r/8,5/8+r/2).

The retained table has eighteen pairs of directed native edges. Each second
edge translated by its specified integer combination of V,U is the exact
reverse of the first. Every one of the36 edges occurs exactly once. The
producer checks all72 endpoint-coordinate identities in Q(sqrt2), all strict
support inequalities, native angle identities, full pairwise-distance
congruence to P/Q, and the exact two-private mask. It also verifies

    area(P)=39/64+7r/64,
    area(Q)=49/16+45r/16,
    det(V,U)=137/16+97r/16=4area(P)+2area(Q)>0.

These finite exact checks imply actual entire-plane covering, beyond the
previous four-ring necessary local census. Translate the six bounded closed
polygons by the discrete rank-two lattice. The periodic integer multiplicity
N is locally integrable. Every polygon-indicator distributional gradient is
an edge-normal measure; the eighteen reversed-edge pairings cancel all these
measures, so gradN=0. Connectedness gives N constant almost everywhere. Its
mean is the total representative area divided by positive covolume, exactly1.
Thus interiors do not overlap: an interior overlap would be an open positive
area set with N>=2. The union is closed by local finiteness, so an uncovered
point would lie in an open positive area gap with N=0. Both contradict N=1.
Consequently the indicated periodic family covers the whole plane legally.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch sage research/searches/contact-symmetric-two-private-periodic-carrier.py

This supplies a periodic escape for this pair only. It neither proves that
all its admitted fillings are periodic nor yet classifies symmetric metrics.
