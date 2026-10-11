# Independent hostile review: fixed-B chirality collapse

Date2026-10-10. Reviewer partial_contacts, independent of construction.

**Final verdict: VALID for all stated branch-collapse, monohedral-witness
and conditional fixed-B transport claims.** No substantive repair required.

## Exact claim and quantifiers

Reviewed
[branching-hexagon-new-chirality-collapse.md](../lemmas/branching-hexagon-new-chirality-collapse.md),
producer/search record/certificate. The branch premise requires both A mate
orientation signs, full trivalent endpoint stars at both ends, and the same
given B with word(r,p,q,q,q,q). It does not quantify over arbitrary hexagon
pairs or infer extension of a finite patch. All three numerical lengths
are distinct, A's alternating angles differ, and all reflections are allowed.

## General forcing and periodicity checks

The preserving mate exchanges alternating A angles, requiring120 qq fillers.
The reflected mate requires120±2delta. A has no qq corner; B has exactly3.
These required values are distinct and exhaust those3 corners, so their sum
is360. Strict convexity forces delta<30. The direction turn from B2 to B5
is180 and their equal q lengths give exact negative vectors. The implication
uses both seam endpoints; one-ended compatibility alone would not suffice.

The two-face monohedral construction's6 reversed endpoint identities follow
from V5=V3-V2. Its actual4 links are circular3-corner stars with sum360,
using both beta3+4+5=360 and the complementary beta0+1+2 sum. The quotient
is a connected closed orientable flat torus, whose complete simply connected
cover is Euclidean. det(u,v)=2area(B)>0 provides2 independent translations.
Thus the monohedral B escape is an infinite tiling with unrestricted valid
contacts, not an imposed marked or selected-substitution witness.

All further nonresonant r/p/q5 transport cases were checked at both endpoint
corner-length labels. Reflected r and p cases require pp or rr absent.
B2 at an r endpoint, a half-turn B/B p neighbor, or the pq B corner at q5
would force the excluded beta0+1+2 sum. A qq mate at q5 requires two B0
sectors at an r seam and violates its fixed orientation. The other mate
case requires rr. These exhaust actual q incident B corner classes.
The conclusions correctly stop at the unclassified q2/3/4 continuation.

## Independent exact computation

[verify_branching_hexagon_new_chirality_collapse_independent.py](verify_branching_hexagon_new_chirality_collapse_independent.py)
uses raw algebraic definitions, no author imports or producer execution.
It checks the exact field isolating interval, closed edge lists, all support
inequalities, A135/105 alternating angles, B qq150/120/90, squared lengths,
10 branch contacts,12 whole-patch separations,6 monohedral seams,4 actual
circular links with zero translation holonomy, area/covolume, and all16
nonidentity lattice comparisons in the complete exact bounding ranges.
It compares retained coordinates, periods, links and comparison list.

Replay passed:

    conda run --no-capture-output -n arisearch python research/reviews/verify_branching_hexagon_new_chirality_collapse_independent.py

AA comparisons here are exact real algebraic comparisons, not floating-point
approximations. Neither certificate nor author file is mutated.

No defect or unresolved gap remains in the stated theorem. No novelty claim
or universal repeated-hexagon classification follows. The other private-chain
result has its own separate review and repaired-step re-review requirement.
