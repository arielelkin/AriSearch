# Hostile review: exact A-only periodic escape

Date: 2026-10-19. Verdict: **valid**.

## Claim and scope

Reviewed `research/counterexamples/hexagon-five-four-angle-fixture-periodic-2026-10-19.md`
and `research/searches/hexagon-five-four-periodic-attack-2026-10-19.py`.
The exact displayed A tiles periodically by the two representatives A and
Q=-A+(2,2), translated by L=Zh+Zt, where
h=(2+2sqrt(3),0) and t=(-3sqrt(3)/2,7/2).
Consequently the particular pair {A,B} is not aperiodic under the governing
omission-permitted definition. No other angle cone, mixed tiling, corona,
or full family classification is reviewed or implied.

## Independent reconstruction

Write r=sqrt(3)>0. Starting at zero, the six successive A edge vectors are

    (1,0), (0,2), (-3r/2,3/2), (-1,0), (-r/2,-3/2), (2r,-2).

Their partial sums give exactly

    (0,0), (1,0), (1,2), (1-3r/2,7/2), (-3r/2,7/2), (-2r,2).

Their squared lengths are (1,4,9,1,3,16); their directions are respectively
0,90,150,180,240,330 degrees. Exterior turns are 90,60,30,60,90,30,
so the stated end-of-side interior angles are correct. The script's strict
left-half-plane tests include all 24 nonincident vertex/side pairs; those
imply both simplicity and strict convexity rather than merely positive local
turns. The shoelace sum is 7+7r, giving area(A)=(7+7r)/2.
Directly det(h,t)=(2+2r)(7/2)=7+7r>0.

Independent B edge reconstruction gives

    (1,0), (r,1), (0,2), (-1,0), (-3r/2,-3/2), (r/2,-3/2).

Its squared lengths are (1,4,4,1,9,3), and area(B)=3+5r/2.
Thus A and B are distinct congruence classes (their areas already differ),
so this really is a pair in the original problem's class. B's geometry is
not an assumption needed by the A-only tiling.

## Exact edge matches and orientation attack

With side i directed from vertex i to i+1, independent substitution of both
endpoints verifies the following table. Offsets are lattice vectors.

| A side | Matching side | Offset |
| --- | --- | --- |
| 0 | A side 3 | -t |
| 1 | Q side 1 | 0 |
| 2 | Q side 2 | t |
| 3 | A side 0 | t |
| 4 | Q side 4 | -h+t |
| 5 | Q side 5 | -h |

For each entry, A_i equals the matched terminal endpoint plus the offset,
and A_(i+1) equals the matched initial endpoint plus the offset.
The map x -> (2,2)-x preserves orientation in two dimensions and maps A to Q;
it sends the six entries to all Q entries, negating their lattice offsets.
Thus no reflection or boundary orientation sign is missing. Translating these
identities pairs every actual directed edge occurrence in the entire family.
The pairing is an involution, with two distinct occurrences in every pair.
Uniqueness of the mate is stronger than the cancellation argument needs.

## Global-cover attack

The passage from the ledger to a tiling is valid; it does not assume a
pre-existing embedded torus or disjointness of a finite patch.

First, since det(h,t)>0, L is discrete. The representatives are compact, so
only finitely many translated representatives meet each compact set. Thus
the sum m of polygon indicator functions is locally integrable, and its
distributional derivative can be computed termwise on compact supports.
The derivative of a polygon indicator is its outward-normal boundary measure
with a fixed common minus sign. Reversing directed edges of counterclockwise
polygons reverses the outward normals. Hence the exact ledger cancels the
whole derivative, including at vertices (vertices have zero edge measure).
Partial contacts or unrelated crossing edges cannot spoil this cancellation.
A locally integrable function on the connected plane with both distributional
partial derivatives zero is constant almost everywhere.

Second, take a half-open fundamental parallelogram F for L. By nonnegativity
and the partition of the plane by F-ell, Tonelli gives, separately for each
representative P,

    integral_F sum_(ell in L) 1_(P+ell)(x) dx = area(P).

Thus integral_F m=2 area(A)=area(F), and the constant is exactly one. This
step remains true if the provisional representatives overlap or cross the
fundamental-cell boundary; it does not presuppose a tiling.

Third, an intersection of two tile interiors is open and has positive area,
contradicting m=1 almost everywhere. The locally finite union of closed tiles
is closed. An uncovered point therefore has an open uncovered neighborhood,
again contradicting m=1 almost everywhere. This upgrades the almost-everywhere
claim to complete coverage with disjoint interiors. Boundary multiplicities
are harmless and explicitly permitted by the tiling definition.

Finally translations by h and t permute the actual tile family, so this is
periodicity of the tiling, not just of its boundary support or multiplicity.

## Computation, defects, and remaining uncertainty

Replayed successfully:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-five-four-periodic-attack-2026-10-19.py

Also independently used Sage exact arithmetic to reconstruct both edge lists,
length squares and areas from the displayed vertices and substitute all six
ledger endpoint pairs directly. This check did not call the reviewed script's
polygon constructor or its lattice-mate search. The finite domain consists
of the two specified polygons and the 12 directed sides of two representatives;
the infinite claim follows from the mathematical argument above.

No mathematical defect or required repair was found. The extra detail above
makes explicit the local finiteness and mean-integral justifications already
correctly invoked by the source. There is no unresolved gap in this particular
periodic certificate. The overarching two-convex-prototile problem remains
unresolved by this counterexample.
