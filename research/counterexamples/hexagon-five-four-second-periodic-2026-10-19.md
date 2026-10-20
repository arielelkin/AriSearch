# Second five/four angle fixture: mixed periodic escape

Date: 2026-10-19. Status: exact positive certificate with a separate small verifier; independent hostile review pending. This pair is not aperiodic.

Let r=sqrt(3)>0. Side words A=(0,1,2,0,3,4), B=(0,1,1,0,2,3), shared lengths (1,4-2r,-4+3r,2-r,-6+4r), and side-END angles A=(90,150,90,120,150,120), B=(150,120,120,90,150,90). Exact coordinates are retained in the certificate. The producer checks exact closure, five distinct positive lengths, and strict supporting halfplanes, hence strict convexity and simplicity. Different length multisets imply distinct congruence classes.

## Monohedral audit

Both shapes fail all three Reinhardt systems under all twelve dihedral labels. The source convention labels corner i at the START of side i. Consequently, for side-END angles a_i, the systems read H1: a5+a0+a1=360 and l2=l5; H2: a5+a0+a2=360 and l1=l3,l2=l5; H3: a5=a1=a3=120 and l0=l1,l2=l3,l4=l5. The producer explicitly checks all cyclic/reflected readings. H2 and H3 also fail immediately because each needs more repeated side-length slots than available.

The Main Theorem of Zhu, Wang, Yan, [Hexagonal Tiling of the Plane, arXiv:2508.01404v2](https://arxiv.org/html/2508.01404v2), states necessity of these systems when every vertex meets at least three tiles; lines85–107 define conventions and explicitly state the assumption holds for convex hexagons. Lines126–128 permit non-edge-to-edge tilings. Thus, conditional on that imported published preprint theorem, each shape is individually untileable even with partial contacts and reflected copies. The mixed periodic witness below does not depend on this classification.

## Finite search domain

First enumerate all16 indexed AA full-side dimers: all equal-length native side pairs and both chiralities. Complete each seam endpoint by full-edge fans of at most four incident tiles (minimum corner90). Then complete fans at every vertex of the two seed A tiles, in their stored order. Frontier cap1000 was declared before this extension and never hit. This search imposes full-side contacts; it is not exhaustive over partial contacts.

The necessary private-color seam is A slot5, color4 (not slot4). Its unreflected midpoint-halfturn dimer has one two-endpoint completion and four full vertex coronas. No reflected slot5 endpoint fan survives. From each completed finite corona, enumerate candidate period vectors equal to translation differences of identically oriented tiles of the same type; enumerate ordered pairs with positive determinant. Quotient the finite patch modulo each candidate lattice, retain one representative per congruent translation class, and test exact edge cancellation and area. Four successful carriers were found across the16 seed cases, including two from the private-color dimer. These are positive witnesses, not minimality claims. No larger negative search is asserted.

## Exact periodic witness and proof

A retained carrier has two A and two B representatives, with periods

    h=(1+r/2,13/2-3r), t=(4-4r,8-4r).

The four exact coordinate lists are in research/certificates/hexagon-five-four-second-periodic-2026-10-19.json. The independent verifier imports no producer. It checks each representative by all pairwise squared distances against its prototile under a cyclic/reflected vertex permutation, checks strict convexity, and finds exactly one reversed edge mate modulo Zh+Zt for every representative side. It also checks that the sum of all four areas is det(h,t)>0.

These checks prove an infinite tiling. The lattice family is locally finite. Its multiplicity function m has zero distributional gradient because all oriented boundary measures cancel in reversed pairs. Therefore m is constant almost everywhere on the connected plane. Its mean over one lattice cell equals total representative area/det(h,t)=1. Thus interiors cannot overlap. The locally finite union of closed polygons is closed, so any uncovered point would give an uncovered open set, contradicting m=1 almost everywhere. Consequently all translates of these four representatives form a plane tiling with two independent nonzero periods.

## Replay

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-five-four-second-dimer-audit-2026-10-19.py
    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_hexagon_five_four_second_periodic.py

Producer evidence: research/certificates/hexagon-five-four-second-dimer-audit-2026-10-19.json. Compact positive certificate: research/certificates/hexagon-five-four-second-periodic-2026-10-19.json. This counterexample kills exactly the stated pair; it does not classify all39 angle-grid representatives or prove a general five/four theorem.
