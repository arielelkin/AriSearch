# Independent hostile review: general contact deformation

Date: 2026-10-15. Reviewer: the independent reviewer of the earlier A5/B5 deformation theorem, not an author of this general strengthening.

**Final verdict: VALID after independently checked repair of the monohedral branch.** The [current general statement](../lemmas/hexagon-contact-deformation-general-2026-10-15.md) asserts an allowed periodic escape for arbitrary hexagon partners. Its mixed-source deformation branch constructs a full-side periodic witness; an original monohedral source is handled directly by the imported unrestricted monohedral theorem. The rank obstruction is proved for every choice of indexing and every admitted defect-free source tiling.

## Claims checked and surviving proof

The original [deformation review](hexagon-fixed-angle-contact-deformation-hostile-2026-10-15.md) checks polygon closure, strict convexity, uniform-template completeness, equality preservation, distinctness of shape classes, indexing and reflections. Those checks remain applicable. Arbitrarily many repeated native pairs introduce no new linear difficulty: if each difference functional is nonzero on ker M, its vanishing locus is a proper subspace there; a finite union of proper real subspaces cannot cover ker M. One vector consequently separates all repeated pairs simultaneously. The failure of simultaneous separation is exactly the existence of at least one difference functional in row M, not the conjunction of all such conditions.

The rank-one transfer is valid and needs no finite torus. For one nonzero translation tau of the changed tiling, every tile orbit is infinite. Choose a native frame on one tile per orbit and transport it equivariantly by tau. Restore the original polygon metrics to this indexed abstract complex. The finite facewise affine templates give a global bilipschitz homeomorphism, so the restored metric plane is complete and flat. The same underlying automorphism tau is now an intrinsic isometry; its absence of fixed points and its preservation of orientation are topological properties unchanged by replacing the metric. After developing the restored plane to Euclidean space, it is therefore a nonzero translation. Symmetries of individual original reference polygons cause no obstruction because the frames were chosen equivariantly on the changed witness.

The additional whole-edge conditions in the private-AA chain SFT are also valid. Finite candidate placements make the existence of a whole-edge opposite-interior mate a finite-window Boolean condition, with a uniformly bounded window because of tile diameter and slab width. Only uniformly finitely many fixed A edges meet a window by packing. Every actual source filling satisfies the enlarged predicates, so nonemptiness is preserved. Every selected B lies in one band. A fixed A nonprivate edge, including both endpoints, avoids every separator curve: the curves lie in interiors of A or of private AA seams and avoid all native vertices. The connected closed edge therefore belongs to one open band. Private edges already have fixed whole-edge A mates. Thus imposing the edge predicates independently in each band and synchronizing periodic cycles preserves them globally. Whole-edge opposite-interior mates, coverage and disjoint interiors together imply the resulting tiling is full-side, with no extra T junction hidden along a paired edge.

## Defect found and repair independently checked

The first draft claimed full-side monohedral periodic witnesses in every branch merely from the imported classification and the trivalent setting. That extra conclusion needed justification; the review initially withheld a validity verdict. The author repaired the proof, and I reread the exact repaired artifact in full.

The corrected proof handles an ORIGINAL monohedral source directly: that original polygon already admits its unrestricted periodic monohedral escape, so neither deformation nor transfer is needed. It then restricts to a mixed source, which remains mixed after remetricization.

For a changed partner with at most three distinct lengths, the mixed-source portion of the reviewed three-sharing theorem applies directly. I reread its complete proof to check this point. Its private-A isolation, local AAB propagation around B, and full adjacency connectivity show pointwise that every B side is AB. The bounded-window incidence counts then force each shared length to occur twice in B, and the corona law leaves the centrally symmetric word or the intrinsically deterministic word. None of these mixed-source deductions assumes B lacks other monohedral tilings or uses the uniform unavoidable-type lemma. Thus one can apply this proof to the supplied mixed changed tiling even when B might also tile alone. The centrally symmetric result has a whole-side lattice witness; the deterministic result makes the given full-side mixed tiling doubly periodic.

For a changed partner with at least four distinct lengths, a monohedral tiler belongs to H1 or H2 under the imported classification: the third classified family has at most three distinct lengths. Explicit full-side flat tori for H1/H2 are given below. If such B cannot tile alone, all other branches of the existing synthesis give full-side tori or full-side deterministic tilings, except for the chain branch now strengthened by the checked SFT predicates. Consequently every mixed changed source needed by the deformation proof yields a full-side periodic witness.

The repaired proof therefore never needs a full-side assertion for the third monohedral family, nor a new sufficiency claim for its displayed conditions. Its original-monohedral escape uses the existing imported theorem only in its previously recorded unrestricted periodic scope. This closes the exact defect I found. No other gap remains.

## Explicit independent H1/H2 full-side witnesses

Use the primary source convention: native corner i has native sides i-1 and i, and native side i joins corners i and i+1, all modulo six. The current primary [Zhu--Wang--Yan v2 introduction](https://arxiv.org/html/2508.01404v2) supplies the classification and its H1/H2 conditions. Only its classification necessity and those stated systems are used in this new dependency check.

H1 has equal side lengths 2=5 and corner-angle sums 0+1+2=2pi and 3+4+5=2pi. H2 has equal side lengths 1=3 and 2=5, and angle sums 0+1+3=2pi and 2+4+5=2pi. Extra coincidences do not invalidate the following gluings.

An oriented face of sign s=+1 or -1 has native corner s*k modulo six at boundary position k. Its native edge at boundary position k is k for sign +1 and -k-1 modulo six for sign -1. An entry (f,k) below denotes this ORIENTED boundary edge, not necessarily native edge k. Pair every listed edge with reversed boundary endpoints.

For H1 take two faces of signs (+,+), with pairs:

    (0,0)--(1,0); (0,1)--(1,1); (0,2)--(0,5);
    (1,2)--(1,5); (0,3)--(1,3); (0,4)--(1,4).

There are four circular trivalent vertex links, two with native corners {0,1,2} and two with {3,4,5}. All pairings use identical native side slots except the allowed 2--5 pair. The connected orientable surface has V-E+F=4-6+2=0.

For H2 take four faces of signs (+,+,-,-), with pairs:

    (0,0)--(1,0); (2,5)--(3,5); (0,1)--(2,2);
    (0,3)--(2,4); (1,1)--(3,2); (1,3)--(3,4);
    (0,2)--(3,0); (0,5)--(3,3); (1,2)--(2,0);
    (1,5)--(2,3); (0,4)--(1,4); (2,1)--(3,1).

There are eight circular trivalent links, four with native corners {0,1,3} and four with {2,4,5}. Pairings use only the listed H2 equalities or the identical native slot. The connected orientable surface has V-E+F=8-12+4=0.

These are compact flat tori for every genuine convex metric satisfying the corresponding conditions: vertex angle sums are 2pi, native edge lengths agree, and the full circular links exclude singular or pinched vertices. Developing their complete simply connected covers supplies full-native-edge tilings with rank-two translation lattices.

The small independent checker [reinhardt-h1-h2-full-side-independent-2026-10-15.py](reinhardt-h1-h2-full-side-independent-2026-10-15.py) contains precisely these two fixed pairings. It checks that every oriented edge is paired exactly once, each native length match is justified, all full vertex-link cycles have length three and a permitted native angle multiset, the face adjacency graph is connected, and Euler characteristic is zero. There is no search, solver, floating-point arithmetic, random seed or producer import. Its exact finite domain consists of these six H1 and twelve H2 edge pairs. I derived the gluings independently by discarded reconnaissance enumeration; only the two retained explicit witnesses and their exhaustive direct checks enter the proof.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/reinhardt-h1-h2-full-side-independent-2026-10-15.py

Result: PASS H1 (2 faces, 6 edges, 4 trivalent vertices); PASS H2 (4 faces, 12 edges, 8 trivalent vertices).

## Final scope

The general rank obstruction is a proved necessary condition for any hypothetical aperiodic hexagon pair. It does not say that all repeated pairs are rigid, nor does it construct an aperiodic pair or classify all seam relations. The source tiling and its indexing determine M; the obstructed pair may depend on them. The earlier A5/B5 torus-transfer theorem remains an independently valid special case. No pentagon conclusion or solution of the unrestricted two-polygon problem follows. No full repository replay is claimed by this review.
