# Straight-edge corner resection preserves a two-hexagon periodic escape

Date: 2026-10-13. Adversarially reviewed VALID.
Fresh whole-family review: `research/reviews/affine-two-convex-straight-edge-resection-hostile-review.md`.

Let Q=(q0,...,q5) be any strictly convex hexagon in counterclockwise order with directed native edges e2=-e5, where ei=q(i+1)-qi with cyclic indices. Then Q alone admits a periodic plane tiling by translations and halfturns. This immediately excludes any two-prototile proposal containing Q from the main target, because omission of the other tile is allowed.

Translate coordinates to q0=0. The edge condition says q3=q2+q5. Set T=q1, a=q2, b=q3+q4-q1. Use the two congruent positively oriented representatives F0=Q and F1=-Q+T at all shifts ma+nb, m,n integers. The following six reversed-edge pairs cancel all twelve directed native edges:

    F0 edge0 <-> F1 edge0 at shift0;
    F0 edge1 <-> F1 edge1 at shifta;
    F0 edge2 <-> F0 edge5 at shifta;
    F0 edge3 <-> F1 edge3 at shiftb;
    F0 edge4 <-> F1 edge4 at shiftb-a;
    F1 edge2 <-> F1 edge5 at shift-a.

Each endpoint identity follows directly from q3=q2+q5; these are full native-edge pairings, with no partial-contact assumption needed. Shoelace gives

    2 area(Q)=q1×q2+q2×q3+q3×q4+q4×q5
             =q2×(q5+q4-q1)=det(a,b).

Thus a,b are independent and their positive covolume is precisely the sum of the two representative areas. The periodized indicator multiplicity is locally finite. Its distributional gradient is zero because all oriented boundaries cancel, so it is constant almost everywhere on the connected plane. Its cell mean is 2area(Q)/det(a,b)=1. Hence it equals one almost everywhere. Positive-area overlaps are impossible, and the closed locally finite family covers every point: any uncovered point would have an open uncovered neighborhood. This proves an actual periodic tiling, without importing the monohedral hexagon classification or merely asserting a periodic combinatorial development.

## Application to the changed pinwheel corner

The proposed common-corner resection has, at parameter δ, hexagon

    Qδ=((-2/5,-16/5),(4/5+6δ/5,-8/5+8δ/5),
        (0,-1),(-24/25,-32/25),(-54/25,-72/25),(-34/25,-87/25)).

Only vertex1 moves along the existing straight outer edge. Its directed edges2 and5 remain respectively (-24/25,-7/25) and (24/25,7/25), for EVERY δ. Whenever the moved pentagon and hexagon remain genuine convex polygons, the theorem therefore gives a Qδ-only periodic escape. It closes the entire admissible straight-edge resection family, not only a numerical quarter-cut example or the finite source-address parent compiler. There is no need to infer forced reunion across the modified seam.

For δ=1/4, Q has area17/4 and the periods in the original coordinates are

    a=(2/5,11/5), b=(-191/50,6/25), det(a,b)=17/2.

The exact standalone producer `research/searches/affine-two-convex-quarter-cut-q-periodic-carrier.py` imports no earlier polygon helpers. It checks rational strict convexity, the antiparallel-edge identity, representative congruence by explicit halfturn, and area/covolume equality. It solves unrestricted lattice coordinates for every candidate reversed edge pair and verifies exactly one partner for every directed edge, rather than restricting shifts to a bounded window. Its retained output is `research/certificates/affine-two-convex-quarter-cut-q-periodic-carrier.json`.

The earlier exact 200-source-cell packing compiler independently fails for this quarter-cut fixture, but that finite failure is now secondary. Changing subdivision depth or source address bounds cannot repair the periodic omission. Reopening requires a materially changed boundary direction or shared-side topology that removes the antiparallel equal-edge condition; this lemma does not exclude such changes.
