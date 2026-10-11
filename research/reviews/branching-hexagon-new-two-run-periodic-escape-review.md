# Fresh hostile review: four-face two-run hexagon periodic curve

Reviewer: root, independently of the structural-audit construction author.
Verdict **VALID** for the entire stated0<delta<30 curve and the exact
cos15 instance. [Reviewed theorem](../lemmas/branching-hexagon-new-two-run-periodic-escape.md).

For C=cos(delta),S=sin(delta), A's threefold edge orbits close separately.
B's first three p=C edges sum(C,sqrt3*C); its three q=1 edges sum their
negative, exactly for every parameter. All consecutive directions make
strict turns in(0,180), and all edge lengths are positive. The cyclic
supporting-height argument proves genuine strict convexity throughout,
not merely at the computed delta15 instance. The distinct binary side words
alternating versus two runs prove noncongruence since0<C<1.

The fixed12 pairing labels exhaust all24 native sides. Equal p/q labels
ensure equal lengths at every parameter; reversing boundary endpoints
preserves orientation. The face graph remains connected, and the exact
corner-successor cycles remain the same8 circular links. Root independently
checked each angle as an affine form in delta: every link has constant
term360 and delta coefficient zero. Thus the same connected orientable
quotient is a compact flat torus throughout the curve, with plane universal
cover and nonzero rank2 translation deck group. This proves whole-plane
periodic existence using original rigid tiles. No original edge-to-edge
necessity or absence-of-T claim is required for an escape witness.

[The independent checker](verify_two_run_four_face_periodic_independent.py)
imports no producer or solver. It defines sqrt2,sqrt3 in the real field
g^4-10g^2+1, g in(3.1,3.2), constructs all directed edges and both polygons,
checks closure and every strict support determinant, and reconstructs all
paired endpoints and actual circular links. An independent BFS development
checks every cycle as a translation, all coordinates integral in the stated
U,V, gcd of all integer rank2 minors1, and exact primitive covolume
9/2+3sqrt3 equal2area(A)+2area(B). All8 affine angle identities are checked
symbolically as separate coefficients. Replay returns PASS.

The specific16-lift search gives a positive certificate; its bounded domain
is not used for a negative claim. The instance's numerical frequency gate
never supplied its existence proof. No substantive defect or repair remains.
Other two-run metrics and the other finite-angle catalog survivors are
outside the periodic curve and still need their own global analysis.
