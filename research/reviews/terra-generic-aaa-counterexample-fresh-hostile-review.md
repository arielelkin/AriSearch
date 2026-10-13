# Fresh hostile review: generic AAA without a monohedral escape

Date: 2026-10-13. Independent reviewer: sol. **Verdict: VALID** for the exact
single-polygon counterexample. No infinite two-shape tiling is asserted.

## Exact geometry and finite patch

I reconstructed the determinant-kernel edge lengths independently in the
specified complex embedding. Phi360 together with Re(z)>99/100 and the
stated rational imaginary-part interval isolates the primitive root at1
degree: the interval lies strictly between the imaginary parts of neighbouring
eligible roots, and the real-part condition excludes roots near179 degrees.
The exact AA check confirms the specified root satisfies both interval
inequalities. The retained verifier confirms positive three pairwise-distinct
class lengths, exact closure and all24 strict supports. Consecutive directions
have exterior turns67,59,59,54,54,67, giving exactly angles113,113,121,121,126,126.
Thus the object is an actual strictly convex hexagon, not just formal lengths.

The original arm-matching description can be made completely explicit. Let
p0,...,p5 be the given vertices. Take three whole direct copies:

    P0 = {p_j},
    P4 = {z^(-126)(p_j-p4)},
    P2 = {z^(113)(p_j-p2)}.

Their native corners0,4,2 lie at the origin. The polygons lie respectively
in angular wedges[0,113], [113,239], [239,360] degrees. Every transformed
vertex satisfies both exact half-plane inequalities defining its wedge;
convexity extends those inequalities to the whole polygon. Wedge interiors
are disjoint, hence polygon interiors are disjoint. The common ray endpoints
are exactly P0[1]=P2[1], P0[5]=P4[5], P4[3]=P2[3]. This verifies all three
whole-side contacts and an actual three-copy AAA patch. The independent
retained whole-copy checker confirms these equalities and wedge inequalities.
No patch-to-plane extension is inferred.

## Imported monohedral theorem and symmetry completeness

The primary source [Zhu, Wang and Yan, Hexagonal Tiling of the Plane,
arXiv2508.01404v2](https://arxiv.org/html/2508.01404v2), refreshed13 October2026,
was checked directly. Its Introduction specifies precisely the three family
conditions used by the verifier, with sides connecting successive numbered
corners. Its Main Theorem covers straight-edge hexagons whenever every vertex
meets at least three tiles; genuine convexity satisfies that assumption and
partial-side contacts are expressly allowed. Cyclic relabelling and reversal
are included in its family equivalence. This is an imported current preprint
theorem, not a newly proved classification.

The retained checker handles all twelve dihedral relabellings. In particular,
under reflection the side index is k-i-1, matching the reversal of endpoint
indices k-i and k-i-1. H1 and H2 each require an opposite-side equality, but
this polygon's side word(a,a,b,b,c,c), with three distinct classes, has no
opposite-side equality. H3 requires angles120, absent here. The exclusions
are therefore immediate even independently of the12-case code. Reflections
and source partial contacts provide no untested monohedral escape under the
named classification. Opposite inequalities also directly exclude centrality.
The six complementary angle types have exactly the five generic ternary
identity triples, as verified in the earlier fixture certificate.

## Falsified extension and non-consequences

This refutes extending the A012012 lemma's premise across arbitrary native
orders as either 'a legal AAA star forces centrality' or 'a legal AAA star
forces monohedral tileability'. It supplies a concrete changed native-word
hypothesis,001122, on which those assertions fail. It does not refute the
periodic-escape theorem in its opposite-angle scope, the possibility of a
periodic mixed tiling, or global two-convex-tile impossibility. It gives no B
shape, compatible mixed neighbourhood, infinite covering, recognizability,
shape-only forcing or universal aperiodicity.

Finite domains: one exact polygon,24 support tests,12 monohedral relabellings,
and three actual whole copies with18 vertex wedge tests. No solver, random
seed, timeout, floating-point acceptance or finite-to-infinite inference.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_terra_noncentral_aaa_hexagon.py
    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_terra_001122_whole_copy_star.py

Both outcomes: PASS. A compatible mixed neighbourhood is the next concrete
obligation; enlarging unrelated periodic-patch searches is not implied.
