# An exact two-dimer successor obstruction for flat591 and its native reflected partner484

**Status:** complete proof and exact supporting witness; fresh hostile review
pending. This is an independent geometric mechanism for these two ratio
families. It does not assume validity of the optional seam-balance LP.

Let w=sqrt3 and normalize the reviewed sole-cross flat591 by Pa=Qd=1:

    P=(1,u,(-3w/2-7/2)u+3w/2+3/2,
       (3w/2+3/2)u-w/2-1/2,(-2w-3)u+w+2),
    Q=((-w-3/2)u+w/2+1,(-w/2-1)u+w+1/2,
       (-2w-4)u+w+2,1,(-2w-3)u+w+2).

Here1/3<u<1/2, excluding(4+w)/13 and(w-1)/2, exactly the undeclared
native-arm equality points. Write P=(1,b,c,d,e),Q=(A,B,C,1,f). Their
identities are e=f=b+C=2A. Every native side is strictly positive, the
sole cross arm is Pa=Qd, and each species has four distinct arms.

P has a forced fourfold private c,d core: neither b+C,e nor f equals2c
or2d on these exact strata. The reviewed core proof therefore applies to
P alone. Q's B arm is globally private, its self-event2B has no collision
with other event bank multisets, and neither e nor f equals2B. Thus every
Q B side whole-matches the same slot with endpoints preserved. Reflection
across that seam pairs each Q uniquely into a canonical two-Q dimer.
The dimer has a reflex240 corner at its two coinciding native(B,C) corners.

## Every Q dimer has a Q successor and two forced P neighbors

At the dimer's reflex corner the only allowed native120 filler is Q(a,f),
using the reviewed actual star inventory(3,4,4). All orientations reduce
to two choices exchanged by reflection in the dimer's intrinsic B-seam
axis. Each filler Q also has its canonical B mate and hence forms a
successor Q dimer. No extension choice can omit this successor.

In one orientation the filler f ray faces one host C arm. Since f=b+C>C,
that C arm's90 endpoint is a T in f. Its perpendicular arm is Qd=1. The
other bank must be Pb=b: the alternative Qc=C would give2C=f=2A, forcing
A=C, a removed privacy equality. Thus Qd whole-matches Pa, uniquely placing
a P on its opposite halfplane.

On the other ray the filler A arm faces the other host C arm. A and C
are unequal in the exact stratum. The two-T invariant applies whichever
arm is shorter. At the90 endpoint of C, the bank event is necessarily
C+b=2A, because2C differs from2A. Its perpendicular Qd seam therefore
again whole-matches Pa and forces a P. This accounts for either ordering
of A,C and every intervening T; no arm equality or whole-side assumption
has been silently imposed on this ray. Both P neighbors complete to their
canonical fourfold cores. The resulting P positions depend on the host
Q dimer, not the chirality of its successor.

Apply this same fact to the successor dimer. Its own compulsory successor
forces its two P neighbors, even before any further tiling is specified.
Thus two linked Q dimers force four P cores, and the following two actual
P constituents already have strictly overlapping interiors.

## Raw exact placements and a uniform strict witness

For a native word(a,b,c,d,e), let its raw polygon vertices be

    0,(a,0),(a,b),(a-wc/2,b+c/2),(-e/2,we/2).

Call the raw Q vertices q0..q4. The initial dimer consists of q and its
reflection across x=A. Choose the successor filler q2+R30*q, with Rθ
the usual exact rotationθ. The P across the initial q native Qd seam has
vertices

    p_i=q4+R60*P_i.

This maps Pa's120 endpoint to q4 and90 endpoint to q3, with its interior
on the opposite side of Qd. Its private core center is O=p3. The successor
pose is x↦q2+R30*x, so its corresponding private P core center is
O1=q2+R30*O. Within that successor core, reflect the displayed P through
the line through O at300 degrees, using

    F300=[[-1/2,-w/2],[-w/2,1/2]].

A second forced original P has vertices

    p'_i=q2+R30*(O+F300*(p_i-O)).

Define the exact point

    W=((2w+22/5)u-3w/2-59/30, 3(w+1)(1-u)/4).

All five oriented supporting determinants for p and all five for p' are
strictly positive throughout1/3<u<1/2. The producer computes them from
these raw vertices, factors each completely over Q(w), verifies its sign
at2/5 and that none of its roots lies in the interval. Completeness of the
root list is checked against each polynomial's degree. This is a direct
strict original-tile intersection witness, not an inference from a picture
or finite sample. The vertical difference(O1-O)y is strictly positive on
the same interval, so the centers and tiles are distinct.

The opposite successor choice is obtained by reflecting the entire forced
configuration across the initial dimer axis. It swaps its two P neighbors
and carries the same strict overlap to their reflected counterparts. Thus
both admitted choices contradict disjoint original tile interiors. Since
Q cannot be omitted (P alone is a four-distinct nonmonotile), flat591 is
untileable under all original isometries and partial contacts.

Native reflection(a,b,c,d,e)↦(d,c,b,a,e), followed by species exchange,
transports flat591 to flat484. Its event identities are b+C=e=f=2d,
and the same geometric obstruction applies. This correspondence can also
be checked from the retained exact flat rows; no unrelated family is
included. Therefore flat484 is untileable as well.

[Exact raw checker](../searches/partial-contact-cairo-flat591-successor-obstruction.py),
[record](../searches/partial-contact-cairo-flat591-successor-obstruction.md).
The prerequisite full event-flat reduction is independently reviewed; this
new successor forcing and strict geometry require their own fresh review.
