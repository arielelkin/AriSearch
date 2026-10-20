# Two further universal periodic support omissions

Date: 2026-10-19. Status: proved; [independent Sol hostile review](../reviews/hexagon-five-four-two-more-support-sol-review-2026-10-19.md) PASS.

## Statement

Use native words A=(0,1,2,0,3,4), B=(0,1,1,0,2,3), with a common positive length for each color. Angles a0,...,a5,b0,...,b5 are in units of pi; angle j is between sides j and j+1. Use the reviewed 22-star signed atlas and mask convention of the seven-support gate.

For every pair of strictly convex closed native polygons satisfying mask20774, A alone has a two-orbit monohedral periodic tiling. For every such pair satisfying mask22550, both A and B separately have such tilings. Thus either support condition gives a universal periodic escape, conditional only on metric existence. No metric existence assertion is needed for this implication. Distinct colors may have equal numerical lengths without affecting this positive result.

## Proof

The star equations and each polygon's angle total4 imply, by exact augmented rational row reduction:

* mask20774: a3=b5 and a4+a5+b5=2;
* mask22550: b0+b1+b2=2, b3+b4+b5=2, a0=b2, a1+a2+b2=2, a3=b5, and a4+a5+b5=2.

For20774 these give a3+a4+a5=2, and the A total gives a0+a1+a2=2. For22550 the displayed equations give both A triples equal2 as well as both B triples equal2. The accompanying checker reconstructs the original signed stars and verifies these consequences without relying on the prior support RREF certificate.

For any strictly convex closed polygon with a0+a1+a2=2, the three strictly positive exterior turns sum pi. Its sides0 and3 therefore have antiparallel directions. Both native words assign equal lengths to these sides. The general universal strip proof in [the independently reviewed nonresonance/support artifact](../searches/hexagon-five-four-nonresonant-support-2026-10-19.md), section “Universal periodic omission on the three block-angle supports”, applies to each such polygon: equal antiparallel sides give two height-monotone two-edge lateral chains; their periodic strip boundaries are invariant under side-midpoint halfturns; alternating strips cover the plane with two lattice orbits. This argument uses translations and halfturns of the original metric polygon, including when its side-to-side strip period is oblique. Hence the conclusion holds for every closed strictly convex metric on the stated supports.

## Exact boundary for the other two masks

For33416 and41032, exhaustive rowspace membership over all20 triples of distinct corner indices of each species finds no single-species triple sum2 identity. Membership over all15 single-species angle-equality pairs likewise finds none. Thus the affine angle equations alone do not force the H1 antiparallel condition. This statement is about affine identities; nonlinear closure can in principle force further relations.

A stronger concrete check uses zero-based row1 of the retained39-metric certificate. This exact closed strictly convex common-length pair satisfies both masks, but neither species satisfies H1. Its angles in degrees are A=(90,150,90,120,150,120), B=(150,120,120,90,150,90); its lengths are (1,4-2sqrt3,-4+3sqrt3,2-sqrt3,-6+4sqrt3). The existing independent39-metric verifier establishes closure, strict convexity, distinct positive lengths, and the H1 failures. Thus adding metric closure does not force an H1 escape on either remaining family.

For pairwise distinct color lengths, both words fail every cyclic/reflected H2 required equal-side pattern (opposite pair2,5 plus distance-two pair1,3) and H3 required three adjacent equal pairs. The checker exhausts these finite label patterns. These exclusions concern only those constructors and use the reviewed39-case report's conventions; they assert no unrestricted classification theorem here.

No mixed periodic template was established by these affine implications. A prospective mixed template still needs an explicit Euclidean placement, independent nonzero periods, cancellation of all exposed boundaries, and proof of coverage without overlaps for every closed metric in either family. Neither trivalent angle balances nor a combinatorial torus supplies those vector and coverage obligations. The earlier exact39-metric carrier and residual-strip results do not prove them universally. Stop this structural gate here; no nonlinear solver, enlarged collar, torus search, or timeout increase was run.

## Replay and scope

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-five-four-four-support-structural-gate-2026-10-19.py
    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_hexagon_five_four_39_omissions.py

The first command passed. Domain: four fixed supports, reconstructed atlas,40 triple equations and30 angle equalities per support, all12 cyclic/reflected H2 indexings per word, both H3 adjacent partitions, and one previously retained exact metric. Exact Sage rational arithmetic; no seed, solver, or search timeout. The second command is the prior independent geometric fixture verifier. These are restricted-support exclusions, not a solution of the two-convex-tile problem. Combined with the three already reviewed universal omissions, five of the seven minimal supports now admit universal periodic escapes;33416 and41032 remain unresolved.
