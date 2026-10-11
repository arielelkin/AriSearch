# Independent hostile review: angle coverage without whole-tile balance

**Date:** 2026-10-10. **Independence:** root authored the counterexample,
search, producer and certificate. This reviewer did not develop them and
wrote a separate verifier importing neither the producer nor Z3.

**Verdict: valid** for the exact finite angle-only classification and the
concrete unrestricted untileability family. No substantive repair was
required. These are not tileable aperiodic shapes or a resolution of the
main problem.

## Exact claims, assumptions and artifacts

The claim refuted is that, for two convex hexagons, angle eligibility of
every native corner in some numerical three-corner360-degree star implies
nonnegative whole-tile angle-frequency balance. Eligibility is only an
angle test, not an assertion of whole-side length matches or extendible
local patches.

The concrete multisets are A=(100,100,100,140,140,140) and
B=(100,100,110,130,140,140). Every present angle appears in a legal
angle star, but the normalized nonnegative count system is infeasible.
Every pair of genuine convex hexagons with these multisets is untileable,
for arbitrary actual side lengths, reflected copies, partial contacts,
and omission of either species. Exact tangent-line coordinates demonstrate
that the multisets are realized by two distinct genuine convex shapes.

The finite comparison domain comprises all sorted six-element multisets
from {100,110,120,130,140,150,160,170} with total720 degrees, and all
unordered pairs with repetition. It makes no cyclic-order, side-length,
placement, or polygon-congruence classification claim.

Reviewed:
[counterexample](../counterexamples/angle-cover-without-frequency-balance.md),
[search record](../searches/angle-frequency-cover-counterexample.md),
[producer](../searches/angle-frequency-cover-counterexample.py), and
[retained certificate](../certificates/angle-frequency-cover-counterexample.json).

## Fresh reconstruction and certificate verification

The new independent verifier is
[verify_angle_frequency_cover_independent.py](verify_angle_frequency_cover_independent.py).
It reconstructs the domain by recursively enumerating integer angle
multiplicity vectors with total multiplicity6 and weighted angle sum720.
This yields46 multisets and1081 unordered pairs. The same method with
multiplicity3 and angle sum360 reconstructs seven global angle stars.
For each pair, it keeps exactly the stars whose numerical angles are
present and tests whether their union covers all present angles.
Exactly692 pairs pass coverage.

The retained entries are required to be a disjoint exact partition of
those692 covered pairs, with no duplicates, missing pairs, out-of-domain
pairs, omitted stars or altered numerical angles. All681 feasible entries
have exact rational fa,fb>=0 with fa+fb=1, nonnegative star variables,
and every angle's exact marginal equation satisfied. All11 rejected
entries have rational weights on precisely the present angles, nonnegative
sum on every legal star and sum at most-1 on each tile multiset. Taking
the weighted sum of the equations would give a nonnegative left side
and a right side at most-1 under the normalization. Thus each rejection
is proved independently of any solver result. Feasible certificates are
linear-system witnesses, not tiling witnesses.

The exhibited A/B pair occurs in the checked rejection list. Its only
angle stars are (100,130,130) and (110,110,140), as independently enumerated
by sorted triples over its four present angles. They cover all present
angles. The displayed weights (2,-1,-1,2) have sum0 on both stars and
positive tile charges12 and6. This is an explicit contradiction to the
proposed local sufficiency implication, rather than a failure to find
frequencies in a bounded search.

Sorting is legitimate for this angle-marginal comparison only: all
constraints depend on numerical multiplicities. The finite result does
not assert that every angle-covered system has compatible side matches,
that cyclic words with the same multiset are congruent, or that a
frequency-feasible pair tiles.

## Exact geometry attacks and checks

The polynomial z^12-z^6+1 is Phi_36 and has degree12. The verifier checks
its twelve primitive roots in exact complex algebraic arithmetic. Exactly
one lies in the supplied rational real/imaginary rectangle, and that root
is the embedding z=exp(2pi i/36). This checks uniqueness as well as
membership; an arbitrary conjugate cannot silently change the geometry.

Every retained coordinate is reconstructed from its rational coefficients
in the basis1,z,...,z^11 and embedded exactly. Both coordinates of every
vertex are real. The normals are independently built from the root's
real and imaginary parts; each is a unit vector. The claimed accumulated
normal angles are recomputed from the ordered corner lists.

For both shapes the verifier checks six distinct vertices, all36
vertex/halfplane incidences with equality precisely on the two incident
lines and strict inequality on the other four, strictly positive consecutive
edge determinants, and positive polygon area. Every side contains its two
consecutive certified vertices and every other vertex is strictly on its
interior side. The normals traverse the circle with gaps strictly between
0 and180 degrees, so their intersection is bounded; the origin satisfies
every inequality strictly and the unit disk is contained in all six
halfplanes. Thus the coordinate lists are genuine compact strictly convex
hexagons with nonempty interiors and six genuine native sides.

The independent angle check uses actual incident vertex-to-vertex rays:
its exact normalized dot product is compared with the algebraic cosine
of the specified corner angle. Both ray lengths are positive, the turn
is strictly convex, and the angle lies in (0,180), making cosine injective
on the allowed interval. This verifies the actual polygon angles without
relying only on the producer's dot products of normal vectors. Distinct
corner-angle multisets rule out congruence, including reflected congruence.

No decimal approximation, floating-point threshold or numerical sign test
is used. The real-algebraic field performs exact support and angle decisions.

## Infinite-plane and unrestricted-contact attacks

**A corner could lie in a side, or a high-valence exceptional star could
escape the trivalent angle test.** In any tiling by these fixed polygons,
positive minimum tile area and bounded diameter imply local finiteness,
so a native star has finitely many sectors. Each genuine corner angle
is strictly greater than90 and strictly less than180. A straight180
sector leaves180 degrees, which cannot be filled by two genuine corners
or one genuine corner. Two straight sectors leave no room for a native
corner. Thus there are no native corner-to-side contacts. Genuine convex
polygon contacts are consequently whole-side contacts. Four corners
would exceed360 and two would fall short; exactly three occur at every
native vertex. Reflections preserve every relevant angle and weight.

**Arbitrary local stars might be declared globally realized.** They are
not. Including every numerically permitted star only enlarges the local
language. Any actual star would be one of the two enumerated triples.
Both have zero charge. Therefore the obstruction is valid even if some
or all of the angle-legal stars cannot match actual side lengths. The
existence of local whole-tile configurations is unnecessary to refute
the stated angle-only implication.

**The infinite proof could assume frequencies, periodicity, or positive
density of both species.** It does none of these. Fix any proposed tiling
of one actual pair of shapes, with maximum diameter D, maximum area M,
and minimum area a>0. Select precisely the tiles whose interiors meet
int Q_R. They cover Q_R and number N>=4R^2/M. Their summed tile charge
is at least6N regardless of which species occur.

At every native vertex whose incident tiles are all selected, the charge
sum is zero. If a selected native corner has an unselected incident tile,
that point cannot lie in int Q_R: an unselected sector near it would
have interior points in int Q_R and would have been selected. A selected
tile incident at such a point has both an interior point of Q_R and a
point outside int Q_R, and hence meets partial Q_R. It lies in the
D-neighborhood of that boundary. Its disjoint interior area is at least a,
so only O(R) such boundary tiles exist. The constants depend on this
fixed pair and not on R or tile orientations.

There are at most six corners per boundary tile and each absolute weight
is at most2. Consequently the entire incomplete-star charge, even allowing
signed cancellation or several disconnected boundary components, has
absolute value at most O(R). Grouping the finite patch's corner charges
by native vertices now gives6N<=O(R), contradicting quadratic coverage.
Holes and pinch points need no Euler argument here: the charge grouping
and boundary localization work for arbitrary selected unions.

This proves untileability for any side metrics realizing the two angle
multisets. It also excludes either monohedral tiling; the proof never
assumes both fA and fB are strictly positive. The displayed frequency
identity6fA+3fB=0 is a harmless positive rescaling of the charge equation;
the direct boundary proof is the independently verified infinite argument.

## Execution, defects and remaining uncertainty

Successfully run:

    conda run --no-capture-output -n arisearch python research/reviews/verify_angle_frequency_cover_independent.py

Output certifies46 multisets,1081 pairs,692 covered pairs, all681 rational
primals, all11 rational duals, the unique cyclotomic root, both exact convex
polygons, all actual native angles, and the charges12,6. The verifier is
read-only by default and can take an alternate certificate path. It
contains no producer import, Z3 import, solver call or generated witness.

No substantive defect was found and no repair of existing artifacts was
made. Independent review status applies to the exact assertions above.
Remaining uncertainty concerns other angle domains, side matching of
frequency-feasible pairs, actual tilability or periodic witnesses for
such pairs, and novelty beyond this elementary counterexample. None is
an obligation needed for the counterexample or its untileability theorem.

**Final verdict:** valid. Local angle coverage alone is demonstrably weaker
than nonnegative whole-tile frequency balance; the two explicit shapes
cannot satisfy the main task's existence gate.
