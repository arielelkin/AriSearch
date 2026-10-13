# Independent hostile review: A010122 used-AA22 periodic escape

Date: 2026-10-13. Reviewer: support agent, independent of the cross010122
author. Verdict: **VALID** for the stated local native-seam theorem in
[terra-five-one-010122-full-cross-22-escape.md](../lemmas/terra-five-one-010122-full-cross-22-escape.md).
The review does not itself establish a no-cross periodic lift or the
original unrestricted two-convex-polygon objective.

## Claim and assumptions checked

A is an actual strictly convex hexagon with native angles (x,y,x,y,z,z),
where y=720-5x, z=4x-360, and 108<x<126 with x!=120. An actual whole-side,
trivalent field has stars AAAxyz, AABxxr, AAByys, ABBzrr. If any A uses
its native side 4 against another A, the actual A metric satisfies a
sufficient Reinhardt H1/H2 periodic monohedral criterion. Omission of B
then gives an admitted periodic tiling of the pair.

The imported H1/H2 sufficient criteria and their indexing were checked
against the already independently reviewed native001122 coverage artifact:
H1 requires corners 0,1,2 to sum 360 and sides 2=5; H2 requires corners
0,1,3 to sum 360 and sides 1=3,2=5, after cyclic/reflected relabelling.
This review uses these sufficient criteria as a settled dependency, not a
newly proved classification or an assertion of novelty.

## Independent attacks and reconstruction

Both endpoints of a used AA22 side must be AAAxyz: AAB stars have only
x,x or y,y A corners. Thus its partner endpoints cannot be z. Precisely
native sides 0,1,2 avoid z in A010122. Every one is xy and permits both
endpoint alignments. At either endpoint the third A supplies the missing
colour; two native corners and two incident-arm orders give four offers.
The necessary domain has exactly 3*2*4*4=96 cases. Reflections and native
corner aliases are included. Treating the two third copies independently
is an overapproximation and cannot discard any actual seam, even if some
choices globally overlap or cannot extend.

The independent checker builds these patterns through native endpoint
sets and set differences of incident arms. It builds equality components
by graph traversal, reconstructs all side maps of reflected relabellings
from endpoint incidence, and tests angle sums as exact affine functions
of x. It imports no producer code. It checks the retained certificate
against its independently generated 96 cases and all H1/H2 witnesses.

The reconstruction finds 36 required equality partitions and exactly three
minimal ancestors:

- (0,1,2,0,2,3): a0=a3,a2=a4, giving H2 at forward start 1;
- (0,1,2,3,0,2): a0=a4,a2=a5, giving H2 at forward start 3;
- (0,1,2,3,1,4): a1=a4, giving H1 at forward start 2.

Each of the 96 cases already satisfies H1/H2. Independently generating all
203 set partitions of six sides retains exactly 71 compatible actual
partitions, all with sufficient monohedral witnesses. Thus no unexamined
length merger, special metric stratum, or assumed distinctness remains.
The checker also reconstructs all 64 optional native AAA cycles and verifies
the corresponding certificate equalities. No positive-closure exception is
needed: failing closure only removes a formal case, while every actual
case already has a sufficient periodic construction.

## Global implications and limitations

There is no local-to-global extension inference. The source field is an
explicit premise; the conclusion is supplied by an imported sufficient
monohedral family of the actual polygon. Likewise a4=aj alone does not
invoke the theorem: the proof needs the seam actually used and its two
AAA endpoints. Its contrapositive gives unused-AA22 support in any actual
field of a polygon without a monohedral escape, retaining every metric
alias. Composition with the separately reviewed support theorem is sound
only after its saturation and field hypotheses have been provided.

The full interval is respected. The proof uses the affine identity
x+y+z=360 and actual strict convexity, with no angle>90 assumption, numerical
sampling, density claim, or separator denominator. Endpoints 108,126 and
the all120 value remain excluded as stated.

No mathematical defect or omitted case was found. No repair was required.
The remaining dependencies are the explicitly imported sufficient H1/H2
criteria and the extraction results when applying this local theorem to
an original unrestricted tiling; this review does not silently replace
either with a finite computation.

## Reproduction

[Independent checker](verify_five_one_010122_cross22_independent.py):

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_five_one_010122_cross22_independent.py

Result: PASS, independent 96 patterns, 36 requirements, 3 minimal ancestors,
203 partitions, 71 compatible, all H1/H2. The full retained cross-case and
actual-partition certificate and its witness lists were checked. No files
are generated or overwritten by this check.
