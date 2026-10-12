# Reordered pentagon forcing feature and immediate periodic closure

Status: [fresh independent review VALID after the five-host repair](../reviews/reordered-acute-pentagon-four-face-carrier-independent-review.md).

After the previous native-order family was proved untileable at all
metrics, reorder only A:

    A=(65,140.5,75,147.5,112),
    B=(40,144.5,136,47,172.5).

The prospective new feature was a forced flat-fan middle corner. The
native180 support remains exactly(65A,75A,40B), while A65 and A75
cannot share a direct seam: all four far endpoint pairs are non-flat
eligible and unfillable. Thus B40 must be the middle native corner in
any such flat star. The three prospective internal-seam branches require

* A0=B0 and A1=B4;
* A0=B0 and A2=B4;
* A0=B4 and A1=B0.

These were only angular/internal metric necessities, not a valid
infinite carrier. Immediate far-end and host-endpoint attacks exclude
every actual flat fan, before a multi-parameter coordinate search:
the A2/B4 internal branch has an unextendible x/w endpoint; the other
branches have outer far y/x and only five possible host types, all
locally excluded. Eligible host endpoints require separate A2/B4 cases;
those were explicitly added during hostile review. No T contact remains
in any whole-plane tiling.

Further native full-star forcing gives the complete proposed tileability
criterion

    A0=B1, A2=B0, A3=B3.

There is a direct actual-metric periodic realization: two A and two B
faces glue to an orientable flat torus with six native vertex links,
two each of(140.5,75,144.5),(147.5,40,172.5),(65,112,136,47).
Every link has angle360. Its complete flat universal cover is the plane,
with a rank-two translation lattice preserving the actual tile faces.
Thus the surviving pair has full-plane existence and an immediate
periodic escape; it is not an aperiodic construction candidate.

The positive metric domain is nonempty. Normalize A2=1 and choose free
t=A1,d=A3. With Cj=cos(j*pi/360), Sj=sin(j*pi/360), set

    A4=-(t*S79+S289+d*S354)/S490,
    A0=-(t*C79+C289+d*C354+A4*C490),
    B0=1, B1=A0, B3=d,
    rx=-(B0+B1*C71+B3*C425),
    ry=-(B1*S71+B3*S425), D=C159*S440-S159*C440,
    B2=(rx*S440-ry*C440)/D,
    B4=(C159*ry-S159*rx)/D.

Native coordinates are partial sums of length_i times the unit vectors
at doubled-degree directions A=(0,79,289,354,490),
B=(0,71,159,425,440). At t=1/10,d=1/5, all lengths are positive,
closure is exact, and all strict supporting determinants are positive:

    A approximately(1.242006948,.1,1,.2,.722467553),
    B approximately(1,1.242006948,1.122706438,.2,2.672241614).

Every computation is exact in Q(zeta720), using QQbar/AA; these decimals
are display only. Positivity and strict convexity persist in an open
two-parameter neighbourhood, and the same four-face carrier realizes
every actual metric satisfying the three aliases. No shape parameter
enumeration was used.

Artifacts:

* [Formal native forcing and periodic carrier proof](../lemmas/reordered-acute-pentagon-four-face-periodic-carrier.md).
* [Independent exact support/torus checker](../reviews/verify_reordered_acute_pentagon_four_face_carrier.py).
* [Support, edge pairing and vertex-link certificate](../certificates/reordered-acute-pentagon-four-face-carrier.json).
* [Exact coordinate producer](reordered-acute-pentagon-periodic-sample.py).
* [Coordinate formulas and positive sample](../certificates/reordered-acute-pentagon-periodic-sample.json).

The formal iff theorem has passed fresh independent review. No broader
impossibility for all convex unmarked pairs is inferred. Further metric
search within either audited native order is unnecessary; a different
native adjacency or angle inventory is a genuinely different problem.
