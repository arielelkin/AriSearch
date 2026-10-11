# Fresh hostile review of the pi/5 pentagon angular reduction

**Reviewer:** pending_reviews, 2026-10-10. The reviewer did not develop the
lemma, producer, certificate, or partition-based verifier.

**Verdict: valid** within its explicitly restricted angular scope. No defect
or author repair was required. The five signatures are necessary for an
aperiodic pair, not sufficient for geometric realization or aperiodicity.

## Exact claim and finite completeness

The [lemma](../lemmas/pentagrid-pentagon-angular-reduction.md) concerns genuine
convex pentagons whose native interior angles are integer multiples of pi/5,
with arbitrary positive side lengths, reflections, unrestricted contacts,
and permission to omit either shape. The angle units must belong to
{1,2,3,4} and sum to15. These restrictions follow from genuine convexity
and the pentagon angle sum; no numerical or denominator bound was added.

The reviewer read the [producer](../searches/pentagrid_pentagon_angles.py),
[certificate](../certificates/pentagrid_pentagon_angles.json), and
[separate verifier](verify_pentagrid_pentagon_angles.py). Fresh producer output
matches the retained certificate exactly. The separate verifier, which imports
none of the producer, reconstructs integer partitions and their permutations
and passes. All101 ordered words,13 dihedral classes, and5 angle multisets are
covered. The dihedral reduction includes both cyclic shifts and reversals.
The listed supplementary seams were checked in every class. Of91 unordered
pairs with repetition,85 have a supplementary member; removing W/W leaves
exactly U/U, U/V, U/W, V/V, and V/W. Repeated angle words do not incorrectly
identify two distinct congruence classes of polygons.

## Geometric escape and unrestricted native stars

For adjacent supplementary corners, the half-turn about the intervening
side midpoint places the copies on opposite sides of a supporting line.
Their interiors are disjoint. The seam endpoints have straight combined
boundary angle; the remaining six boundary corners remain strictly convex.
The boundary is simple, and deleting the two straight points gives a genuine
convex centrally symmetric hexagon. The recalled elementary lattice tiling
of that hexagon gives a periodic tiling by the original pentagon copies.
This is a valid monohedral escape even if a proposed pair would usually use
both types. No side-length equality is required.

A bounded region meets finitely many tiles because their diameters are
uniformly bounded and areas uniformly bounded below. At a native corner,
no incident tile can contain the point in its interior. The incident sectors
fill the full disk. There are either no straight sectors, with native angles
summing to2pi, or one straight sector, with native angles summing to pi.
Two straight sectors would leave no space for the distinguished native
corner. This includes every T-junction or subdivided side permitted by the
problem. The minimum native angle pi/5 bounds native-sector counts by10
or5. The weighted-sum5/10 enumeration exhausts all29 vectors. It does not
assert that every vector is metrically realizable. For W alone neither5
nor10 is a multiple of3, so no native corner can occur in a tiling.

## Incidence witnesses and the window inequality

The reviewer checked all displayed rational decompositions directly. They
reproduce the four non-W monohedral corner-count vectors, the three mixed
W witnesses, and all positive-count witnesses required for the five surviving
word pairs. The verifier also checks availability of every used angle, positive
rational weights, duplicate stars, and all15 multiset-pair records. These
identities certify the stated relaxation only; they do not prove geometric
closure, global extendability, or monohedral tilability of U or V.

The functional is exactly F(s)=3s1+s2-s3+2s4=5v-2t+5s4. For full stars
t=10, negative F would force v+s4<=3, incompatible with weighted sum10
and corner units at most4. For half stars t=5, it would force v+s4<=1,
also impossible. Thus all full and half stars have nonnegative F. Its
five tile values are10,5,5,0,-5. The sharp incidence caps2,1,1,0 are dual
inequalities attained by the explicit witnesses; the zero-value partner
cannot have positive W count in the relaxation.

For an actual tiling, summing complete stars at native points in the square
is nonnegative. Comparing the resulting corner sum with tiles whose fixed
reference points lie in the square changes only contributions from a fixed
boundary strip. Every such tile lies in a fixed thicker strip, whose area
is O(R); interior disjointness and the minimum area bound give O(R) tiles.
Each has five corners, so the discrepancy in F is O(R), including corners
in half stars. This proves 5N_U-5N_W+O(R)>=0, and likewise for V/W.
The argument requires neither density limits nor positive densities of both
types. Constants may depend on the fixed reference points and polygons.

The exact zero-F stars are full334, full2233, full1333, and half23. In U/W
only full334 and full1333 are available; V/W also permits half23. This is
consistent with the unrestricted-contact claim. Equal asymptotic counts
would not itself remove isolated or sparse positive-F stars. The author
explicitly avoids that invalid equality-case rigidity inference.

## Attacks, uncertainty, and replay

Attacks checked included omitted reflected words, omission of one tile type,
a half-turn cluster losing strict convexity, multiple straight sectors,
unbounded native valence, accidental use of an edge-to-edge assumption,
a nonpositive incidence witness, counting errors at reference-point windows,
and confusing necessary incidence feasibility with plane tilability. None
invalidates the stated result. The reviewed lattice escape dependency is
used with its actual hypotheses and does not import a pentagon classification.
No remaining uncertainty was found within this angular theorem. Exact metric
candidates and their existence/periodicity proofs remain separate obligations.

```text
conda run --no-capture-output -n arisearch python3 research/searches/pentagrid_pentagon_angles.py
conda run --no-capture-output -n arisearch python3 research/reviews/verify_pentagrid_pentagon_angles.py
```

The independent verifier completes and reports101 ordered words,13 dihedral
words,29 full/half stars,15 complete incidence cases, and five surviving pairs.
No timeout, stochastic seed, solver answer, or floating-point decision is used.
