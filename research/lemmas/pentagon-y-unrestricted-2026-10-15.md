# The rational Y-pair admits no unrestricted plane tiling

Date: 2026-10-15. Status: independently hostile-reviewed VALID; see
[review](../reviews/y-unrestricted-and-family-hostile-2026-10-15.md).

## Statement and dependencies

Let

    P=((0,0),(2,0),(3,2),(2,3),(0,2)),
    Q=((2,3),(1,4),(-1,4),(-2,3),(0,2)).

**Theorem.** There is no tiling of the Euclidean plane by isometric copies
of P and Q, including reflections and unrestricted partial contacts.
This excludes this specific candidate and does not prove the original
universal impossibility target for arbitrary pairs of convex polygons.

The proof uses the reviewed theorem that each native P BB side has one
full equal-length native mate, proved in
[pentagon-y-one-breakpoint-bb-obstruction-2026-10-14.md](pentagon-y-one-breakpoint-bb-obstruction-2026-10-14.md).
It also uses the exact geometry and irrationality of theta/pi from
[the Y interface source](../searches/pentagon-y-interface-2026-10-14.md).
No finite quotient, bounded patch search, or whole-edge assumption occurs.

## Local geometry

Write theta=atan(2). The native angle labels and words are

    r=pi/2, a=pi-theta, b=pi/4+theta,
    c=3pi/4-theta, g=3pi/4, d=2theta;
    P=r,a,b,b,a; Q=c,g,g,c,d.

The native sides, with their actual endpoint types, are

    P RA: length 2 (two occurrences),
    P AB: length sqrt(5) (two occurrences),
    P BB: length sqrt(2),
    Q CG: length sqrt(2) (two occurrences),
    Q GG: length 2,
    Q CD: length sqrt(5) (two occurrences).

All angles exceed pi/3, and c is the minimum angle. The seven native
angle-star multisets are aad,abg,rgg,rrrr,rrbc,rccd,bbcc. The complete
flat-star palette is rr or bc. These are angle-only facts, so they remain
applicable when native sides do not match in full. In particular the
unique native star containing r+g is rgg; the unique star containing
any of a+g or a+b is abg.

The angles a,d,g cannot occur with a flat sector: their complements to pi
are theta,pi-2theta,pi/4 respectively, each strictly smaller than c.
Call this the **no-flat property**. Consequently, a native A,D,or G
cannot lie strictly inside another tile's native side.

Local finiteness holds without a hypothesis: each prototile contains a
disk of positive radius, their diameters are bounded, and the disjoint
interior disks of tiles meeting a fixed compact set lie in another bounded
set. This permits a finite interval decomposition along any native side.

## Lemma 1: every GG side has a full native mate

Consider any Q GG side, of length 2. At both endpoints the opposite-side
tiles must have native corners: an opposite flat sector is forbidden by
the host G's no-flat property. At an interior transition between guests,
the two guests also have native corners, since a flat sector on that side
would consume the full opposite half-plane.

Thus every consecutive interval of contact on GG is an entire native
side of its guest. If there were two or more such intervals, their total
length would be at least 2sqrt(2)>2. Hence there is exactly one interval,
and it is one entire native side of length 2. Its tile is either Q, using
GG, or P, using RA. In particular longer containing sides are impossible:
they would put at least one host G against a flat sector.

## Lemma 2: a G cannot use its CG arm along a P RA ray from R

Suppose a P R corner and Q G corner are adjacent across a ray along P's
RA side, and the Q uses its CG arm on that ray. At distance sqrt(2) from
R, its C endpoint lies strictly inside the P RA side of length 2. The P
contributes a flat sector there. The unique complementary corner is B,
by the complete flat-star palette bc.

One native side of that new B tile follows the remaining P RA segment
toward A. It has length at least sqrt(2), while the distance to A is
2-sqrt(2)<sqrt(2). Therefore the original A lies strictly inside that
B tile's native side. This violates A's no-flat property. The argument
holds on either arm, for either reflected orientation.

## Lemma 3: GG cannot have a Q GG mate

If two Q GG sides mate, at each endpoint the two G corners must belong
to an rgg star. The remaining R corner is a P corner. Each incident ray
of that R is a P RA side. Both Q G corners have already used their GG
arms along the common GG side, so their arms along the two P RA rays
are CG. This contradicts Lemma 2. Therefore Lemma 1's full mate is always
P RA.

## Propagation on one actual P tile

If a Q occurs, Lemma 3 gives a P whose RA side is fully matched by that
Q's GG. At its R endpoint the star is rgg. Both sides of this particular
P incident to R are RA. Across each stands a G. Lemma 2 excludes CG
on either ray; hence each G uses its GG side, length 2, and fully matches
the corresponding RA side. Both actual A corners of this one P therefore
meet G corners. Their stars are abg.

At each A, the neighbor across P's AB side is consequently a B corner.
If that neighboring B used BB along the ray, the reviewed full-BB-mate
theorem would require its complete sqrt(2) BB side to have a full native
mate. But its opposite is the original P AB side of length sqrt(5),
which continues strictly beyond it. This is impossible. Thus the B uses
its BA arm, length sqrt(5), and fully matches the original AB side.

At the far endpoint, each of the original P's two actual B corners now
meets an A corner, and so lies in an abg star. Since A is across the AB
arm, G must be across the BB arm. Apply the full-BB-mate theorem to the
original P's BB side. Its full native mate would need length sqrt(2)
and a G corner at each endpoint. There is no such native GG side:
the only length-sqrt(2) sides are BB and CG. This contradiction excludes
every Q from any hypothetical tiling.

A P-only tiling is also impossible. At any A corner no flat sector can
occur, and neither native star containing a, namely aad or abg, uses
P corners alone. Thus a hypothetical plane tiling cannot omit Q either.
This completes the unrestricted untileability proof.

## Scope, review and exact replay

The result upgrades the older whole-edge obstruction for this exact pair.
The argument deliberately uses only the seven angle stars, not the
five-star full-edge length atlas. It does not infer any infinite tiling
from locally legal patches. All uses of a full mate are supplied by the
reviewed BB theorem or by Lemmas 1-3 above.

The accompanying exact checker reconstructs native geometry, the seven
angle stars and both flat stars, endpoint-type side records, all metric
inequalities, and the finite symbolic propagation implications:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/pentagon-y-unrestricted-2026-10-15.py

This computation is a deterministic finite arithmetic verification, not a
search for plane tilings. The unbounded implication is the proof above.
Independent hostile review is VALID, with a separate coordinate and
interval reconstruction. A stronger parameter-family version is proved in
[y-pentagon-parameter-family-2026-10-15.md](y-pentagon-parameter-family-2026-10-15.md).
