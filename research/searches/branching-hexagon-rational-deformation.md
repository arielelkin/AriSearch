# Exact search record: rational branching hexagon deformation

Date: 2026-10-10. Status: complete exact symbolic check and fixture certificate; independent hostile review VALID. This is a changed geometry, not a larger branch-word search.

Question: Can the four-face reversed-side topology support genuinely branching repeated-side hexagons outside the completed 120-degree cone, without assuming finite-patch extension? Answer: the explicit 3D cone in the linked lemma has a global periodic torus and two compatible whole-tile branch patches. The second branch's infinite extension is unproved.

[The proof](../lemmas/branching-hexagon-rational-deformation.md) gives the infinite-domain mathematical argument. Computation has these exact domains:

* All twelve fixed seam pairs, all twenty-four endpoints, all twenty-four face corners and their eight actual circular links. Symbolic coefficients lie in QQ[a,c,r].
* All ten branch-patch full-side contacts; exact symbolic QQ[a,c,r] endpoint equations.
* The rational fixture (a,c,r)=(1,3/4,3/2). Six support lines against all four nonadjacent vertices for each of two polygons.
* Every ordered pair of the four periodic motifs and every integer lattice translation in the complete exact bounding-box ranges. There are 24 comparisons excluding identity. Convex separating-axis projections are rational; equality allows boundary contact.
* Every unordered pair of four tiles in each of the two physical branch patches: 12 comparisons.
* All twelve dihedral maps of each six-vertex shape, tested against all 36 pairwise squared distances.
* All 35 three-ray multisets from five numerical labels; graph legality only. This does not assert global extension.

Encoding: cumulative directed rational vector edges; rotations and reflections are explicit rational matrices. Symmetry reduction: none for seam or overlap checks; intrinsic dihedral enumeration is exhaustive. Solver: no SAT/SMT, exact Sage rational and polynomial arithmetic. No random seed, timeout or truncated domain. Replay completed with Python 3.12.13 and Sage 10.9. Initial exploratory hand arithmetic had an E3 transcription error of 1/1250; this was corrected by deriving E3 automatically from closure before any retained certificate was produced. No permanent claim depends on that discarded reconnaissance.

Replay, nondestructive by default:

    conda run --no-capture-output -n arisearch python research/searches/branching-hexagon-rational-deformation.py

Explicit certificate production:

    conda run --no-capture-output -n arisearch python research/searches/branching-hexagon-rational-deformation.py --output research/certificates/branching-hexagon-rational-deformation.json

[Retained certificate](../certificates/branching-hexagon-rational-deformation.json). Expected summary: PASS: 12 polynomial seams, 8 trivalent links, 24 complete lattice separations, 12 branch separations.

The topological and global developing argument is in the proof artifact. The certificate itself does not establish an arbitrary-pair theorem, universality of periods, or infinite extension of the second local branch. The [independent review](../reviews/branching-hexagon-rational-deformation-review.md) is VALID. Replay its no-author-import checker with:

    conda run --no-capture-output -n arisearch python research/reviews/verify_branching_hexagon_rational_deformation_independent.py
