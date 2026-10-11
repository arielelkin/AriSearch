# The complete pi/5 pentagon angle reduction

**Status:** adversarially reviewed as valid in the
[fresh audit](../reviews/pentagrid-pentagon-angular-reduction-review.md).
This is a restricted necessary-condition theorem and an
exhaustive angular relaxation. It is not an aperiodic tile construction.

## Statement

Let P,Q be genuine convex pentagons with every interior angle an integer
multiple of pi/5. Side lengths are arbitrary positive real numbers, all
isometries including reflections are permitted, contacts are unrestricted,
and a tiling may omit either shape. If {P,Q} is aperiodic in the sense of
[the problem](../../research-problem.md), then the cyclic angle words of
P,Q, in pi/5 units and up to rotation and reversal, form one of exactly
the following five unordered pairs:

| Name | Cyclic angle word |
| --- | --- |
| U | (1,3,4,4,3) |
| V | (2,2,4,3,4) |
| W | (3,3,3,3,3) |

The five pairs are U/U, U/V, U/W, V/V, and V/W. Equal angle words do not
mean congruent polygons: the two shapes must still be distinct congruence
classes, as required by the original problem.

Every one of these five pairs passes the complete native-angle incidence
relaxation, with both shape counts positive. U and V individually also
pass this relaxation. Consequently, angle sums and the aggregate corner
counts alone do not establish that either U or V fails to tile alone.
The claim does not infer plane tilability from a feasible incidence vector.

There is an additional metric-independent count restriction. In a plane
tiling by U- and W-angle pentagons, let N_U(R),N_W(R) count tiles whose
chosen reference points lie in a square of side R. Then

    N_W(R) <= N_U(R) + O(R).

The corresponding inequality holds with V replacing U. The constants
depend on the fixed polygons and reference points. This covers all
partial-side contacts. It is sharp for the angular incidence relaxation,
but no equality-case geometric tiling is asserted.

## Exact finite angle domain

A genuine convex pentagon has five angles strictly between 0 and pi,
whose sum is 3pi. Its integer angle word therefore belongs to

    { (m0,...,m4) in {1,2,3,4}^5 : m0+...+m4=15 }.

There are 101 ordered words. Rotation and reversal give thirteen dihedral
classes. A direct complete list is:

| Word | Has an adjacent pair summing to 5? |
| --- | --- |
| (1,2,4,4,4) | yes |
| (1,3,3,4,4) | yes |
| (1,3,4,3,4) | yes |
| (1,3,4,4,3) | no: U |
| (1,4,2,4,4) | yes |
| (1,4,3,3,4) | yes |
| (2,2,3,4,4) | yes |
| (2,2,4,3,4) | no: V |
| (2,3,2,4,4) | yes |
| (2,3,3,3,4) | yes |
| (2,3,3,4,3) | yes |
| (2,3,4,2,4) | yes |
| (3,3,3,3,3) | no: W |

The five sorted angle multisets are

    (1,2,4,4,4), (1,3,3,4,4), (2,2,3,4,4),
    (2,3,3,3,4), (3,3,3,3,3).

The [producer](../searches/pentagrid_pentagon_angles.py) enumerates the
1024 raw ordered words; the [separate verifier](../reviews/verify_pentagrid_pentagon_angles.py)
instead generates integer partitions of 15 and their distinct permutations.
Both retain all reflections. Their common exact output is the
[certificate](../certificates/pentagrid_pentagon_angles.json).

## The adjacent supplementary escape

If a genuine convex pentagon has consecutive corner angles whose sum is
pi, join it to its half-turn about the midpoint of the side connecting
these corners. The copies have disjoint interiors because that side is a
supporting segment and their interiors lie in opposite open half-planes.
The two seam endpoints become straight boundary points; each of the
other six boundary corners remains strictly convex. The union is a
genuine convex centrally symmetric hexagon.

The elementary centrally symmetric hexagon lattice tiling in
[the reviewed equilateral obstruction](new-angle-equilateral-rational-obstruction.md)
gives a periodic monohedral tiling of the original pentagon, by retaining
the two copies inside each translated hexagon. The construction does not
require any special side-length equality. Thus each of the ten "yes"
words supplies a periodic tiling using one member of the pair alone and
cannot occur in an aperiodic pair.

For W/W every native corner has angle 3pi/5. A nonempty sum of these
angles can equal neither pi nor 2pi, because neither 5 nor10 is divisible
by3. No plane tiling exists. This also proves that a single W-angle
pentagon cannot tile alone. It does not eliminate W partnered with U or
V: the full star (3,3,4), for example, contains W corners and is legal.

There were 91 unordered pairs with repetition of the thirteen words.
The supplementary escape removes 85 of them, leaving six. The W/W
exclusion leaves exactly the five pairs in the statement.

## Native stars with unrestricted contacts

Fixed convex prototiles have a positive minimum area and bounded maximum
diameter. Interior disjointness therefore makes every bounded region meet
only finitely many tiles. At a point which is a native tile corner, each
incident tile contributes either a genuine corner sector or a straight
sector. If no straight sector is present, the genuine sectors sum to2pi.
If a straight sector is present, it is unique and the genuine sectors on
its other side sum to pi. Two straight sectors would leave no angle for
a genuine corner. This dichotomy includes T-junctions and partial-side
contacts without imposing edge-to-edge tiling.

Write s=(s1,s2,s3,s4) for the numbers of native sectors of angles
pi/5,2pi/5,3pi/5,4pi/5 at such a point. All possibilities obey

    s_i >= 0 integers;   s1+2s2+3s3+4s4 is 5 or10.

The minimum corner angle is pi/5, so a full star contains at most ten
native corners and a half star at most five. The domain {0,...,10}^4
therefore overincludes every possibility, irrespective of side geometry.
It gives exactly 29 native-star vectors. A pair may use only stars whose
nonzero entries refer to one of its available angle values.

This finite domain does not bound edge subdivisions, polygon placements,
orientations, or the number of tiles in a patch. It exhausts only the
native-angle sums.

## Exact incidence relaxation and its witnesses

For a word T, write C_T=(c1,c2,c3,c4) for its corner-count vector. The
necessary incidence relaxation asks for nonnegative rational or real
weights x_s and nonnegative shape counts n_P,n_Q, not both zero, satisfying

    sum_s x_s*s = n_P*C_P+n_Q*C_Q.

Its necessity for plane tilings follows by applying the corner-count
identity in square windows, allowing O(R) boundary error and then taking
a subsequential normalized limit. Finite prototile areas make the tile
count Theta(R^2). The weights need not correspond to vertices of an
actual geometric patch. A feasible vector only shows that this relaxation
cannot exclude the pair.

For compact notation, e.g. "334" means a full star with native angles
3pi/5,3pi/5,4pi/5. The following exact rational sums give monohedral
incidence witnesses for all four non-W multisets:

| Sorted multiset | Native-star decomposition of its corner counts |
| --- | --- |
| (1,2,4,4,4) | 244 + (1/2)1144 |
| (1,3,3,4,4) | 334 + (1/2)1144 |
| (2,2,3,4,4) | (1/2)(244 + 334 + 2224) |
| (2,3,3,3,4) | 334 + (1/2)2233 |

Combining any two such witnesses gives positive counts for both members
of the corresponding pair. For partners of W, exact sharp witnesses are

    C_(1,2,4,4,4) + 2 C_W = 3*334 + 1333 + (1/2)2233,
    C_U + C_W = 2*334 + 1333,
    C_V + C_W = 2*334 + 2233.

In particular the five surviving word pairs all admit incidence witnesses
with positive counts for both shapes, using full stars only. The fourth
multiset, (2,3,3,3,4), can be paired with W in the relaxation only if the
W count is zero, as established below. W/W has no feasible incidence
vector. These statements classify all fifteen multiset pairs exactly.

## A nonnegative star functional

Define

    F(s)=3s1+s2-s3+2s4.

For native stars this is always nonnegative. One can check all29 vectors
with integers; there is also a short direct proof. If v=sum s_i and
t=s1+2s2+3s3+4s4, then

    F(s)=5v-2t+5s4.

For a full star t=10, a negative value would require v+s4<=3.
If v>=4 this is impossible. If v=3, it would require s4=0, in which case
t<=9; if v<=2, then t<=8. Thus F>=0. For a half star t=5, a negative
value would require v+s4<=1, but one genuine convex corner has at most
four units. Again F>=0.

The tile values for the five sorted multisets are respectively

    10, 5, 5, 0, -5.

Thus a partner of W with tile value 5 admits at most one W per partner in
the exact incidence relaxation; value10 admits at most two; value0
forces the W count to be zero. The explicit witnesses above attain each
bound, so the count restrictions are sharp for this relaxation.

To obtain the asserted window inequality, sum F over complete native
stars based in a square. Its sum is nonnegative. Replacing the collected
corner counts by the exact corner counts of tiles whose reference points
lie in the square costs O(R): only tiles in a fixed-width boundary strip
contribute to the difference, and their number is O(R) by bounded diameter
and minimum area. For a U/W pair the resulting sum is

    5N_U(R)-5N_W(R)+O(R) >= 0.

This proves the claimed inequality, and the V/W proof is identical.
Nothing requires the two tile densities to exist. An asymptotic equality
does not imply that every individual star has F=0; isolated or sparse
positive-F stars may have zero density. No global equality-case rigidity
is claimed.

## Scope, dependencies, and exact remaining work

The theorem derives all angular filtering locally and by boundary counts.
Its only imported geometric ingredient is the previously reviewed
half-turn/lattice escape, whose construction is recalled above. It uses
neither the classification of monohedral convex pentagons nor a
restriction on lengths, partial contacts, chirality, or absolute
orientations. A candidate whose lengths are in golden-ratio proportions
still needs exact closure, strict convexity, a proof of plane existence,
and a proof excluding every periodic tiling admitted by the two shapes.

The five word signatures remain candidates for a metric construction;
their feasibility in this relaxation is not evidence of such a
construction. In particular no integer-independence argument involving
1 and the golden ratio has been used to rule out a lattice period.

Replay the enumeration and independent exact certificate check as listed
in [the search record](../searches/pentagrid-pentagon-angular-search.md).
