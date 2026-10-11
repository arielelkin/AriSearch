# Fresh hostile review of the affine mirror hexagon escape

**Reviewer:** pending_reviews, 2026-10-10. The reviewer did not develop the
construction, source proof, certificate, or original verifier.

**Verdict: valid**, with the explicitly imported current primary monohedral
hexagon theorem as a dependency. The exact pair admits a doubly periodic
whole-plane tiling, has exactly two non-equilateral congruence classes, has
irrational area ratio, and neither prototile tiles monohedrally. These are
properties of this fixed example, rather than a classification of arbitrary
repeated-length hexagon pairs or a solution of the main problem.

## Claims and assumptions audited

The reviewed [proof](../lemmas/hexagon-affine-mirror-periodic-escape.md) gives
a fixed pair in Q(sqrt(3),sqrt(5)), its three-copy motif, a rank-two lattice,
and source parameter sin(a)=1/4, cos(a)=sqrt(15)/4. The
[certificate](../certificates/hexagon-affine-mirror-escape.json) and
[original verifier](verify_hexagon_affine_mirror_escape.py) were read and the
original check replayed successfully. Reflections are permitted by the main
problem, and the displayed reflected A motif therefore introduces no new
prototile or placement restriction.

The independent checker reconstructs coordinates separately from the displayed
formulas, checks them against the certificate, proves strict convexity using
all supporting-side inequalities, verifies all eighteen source sides occur
exactly once in nine seams, and checks their endpoint translations. It also
checks D*S=S*D and the exact source/reflected A identity. The positive-definite
D sends translations to translations. The independent global witness check
below makes no assumption that an arbitrary affine deformation would preserve
a Euclidean tile-class count.

## Whole-plane witness and exact arithmetic

The retained [independent checker](verify_hexagon_affine_mirror_independent.py)
uses Sage real and complex algebraic arithmetic, without importing or calling
the original checker. It reduces possible overlaps using bounding boxes in
**lattice coordinates**, rather than the author's physical x/y parity bounds.
It checks all 24 resulting ordered nonidentity comparisons by exact polygon
clipping, rather than the author's separating-axis projections. Every clipped
intersection has area zero. Every omitted translate has disjoint lattice-coordinate
bounding boxes, so there is no uncontrolled period or shift cutoff.

The sum of three motif areas equals the lattice covolume. Periodization of
area in a fundamental cell therefore gives full coverage almost everywhere.
A finite motif repeated by a lattice is locally finite and closed; any
uncovered point would have an uncovered open neighborhood of positive area.
Consequently it covers the entire plane. This independently checks the global
coverage step and does not infer existence from a finite patch or local stars.

Five distinct side lengths in A versus three in B preclude congruence even
under reversal or rotation. Both counts exceed one, so both are
non-equilateral. The exact area ratio sqrt(15)/2-1 is irrational. The proof of
at least one irrational B angle is also valid: rational native angles would
make the indicated direction ratio a root of unity, whose rational trace
118/61 would have to be an integer. It is not. No numerical angle estimate
is used.

## Monohedral exclusion: unrestricted primary source checked

On 2026-10-10 the reviewer opened
[Zhu--Wang--Yan, *Hexagonal Tiling of the Plane*, arXiv:2508.01404v2](https://arxiv.org/html/2508.01404v2),
Sections 1 and 2. Its Main Theorem assumes at least three tiles meet at every
vertex; convex hexagons satisfy this. The text explicitly includes half
vertices and does not impose edge-to-edge contacts. The distinct-edge strip
theorem later in the introduction has an edge-to-edge hypothesis and is **not**
the theorem imported here. The unrestricted Main Theorem is the correct
necessary classification for excluding monochromatic tilings.

The independent checker encodes H1, H2, and H3 for all twelve dihedral
labelings of each polygon, including their angle requirements. Angle sums
are decided by exact products of unit exterior-turn complex numbers: three
strict convex exterior turns lie in (0,3pi), so their product is -1 exactly
when their sum is pi. The corresponding interior-angle sum is then 2pi.
The H3 120-degree conditions use exact interior cosines. Both polygons fail
every system. This checks all cyclic and reflected labelings and does not
substitute an edge-to-edge or a local-patch classification for the required
unrestricted theorem.

The shorter argument in the author proof is independently sound as well:
A has no equal opposite pair; B's only equal opposite pair is not parallel;
H1 forces that pair to be parallel. Neither has the necessary H2 repetition
pattern or H3 adjacent-pair partition. No pentagon classification is invoked.
The classification theorem itself remains an explicit external mathematical
dependency; this review checks its stated scope and this application rather
than re-proving the entire source paper.

## Attacks, defects, repairs, and replay

The reviewer attempted failures through an extra affine tile class, accidental
congruence of A and B, a missed lattice shift, positive-area overlap, a hole
of zero area in an incomplete covering, an irrational-angle inference from
numerical values, and a hidden unrestricted/edge-to-edge classification switch.
All are excluded by the exact checks and arguments above. No defect was found
in the author claim, proof, certificate, or original checker. The reviewer's
first checker execution used an unsupported denominator method on an algebraic
real; coercing the proven rational trace to QQ fixed that implementation issue.
It did not change any mathematical decision.

```text
conda run --no-capture-output -n arisearch python3 research/reviews/verify_hexagon_affine_mirror_independent.py
```

The finite check completes and prints:

```text
PASS: separate exact coordinates, all 24 dihedral labelings fail full Reinhardt systems, 24 lattice-coordinate clipping comparisons, motif-area=covolume, two classes, irrational area ratio and direction.
```

No timeout, memory bound, randomized search, or denominator cutoff is used.
No remaining uncertainty was found within the exact fixed-example claim.
The unrestricted two-convex-tile aperiodicity target remains unresolved.
