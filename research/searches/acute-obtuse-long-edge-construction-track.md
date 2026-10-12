# Acute/obtuse long-edge feature: exact module, then global budget rejection

Status: exploratory family rejected as untileable. Independent root
forcing-budget audit agrees; geometry/star replay is retained.

Subsequent stronger result: the root-reviewed
[native-word untileability theorem](../lemmas/acute-obtuse-native-word-untileability.md)
excludes every actual metric of these native words, without the long-edge,
minimum-edge or matched-length assumptions. The narrower exact modules
and capacity gates below remain valid independent artifacts. Further
metric changes within these same words cannot produce a plane tiling.

The new intended feature was an A native edge joining65 and140.5 degrees.
Putting an obtuse, non-flat-eligible angle at one endpoint escapes the
[doubling obstruction](../lemmas/flat-star-endpoints-cannot-block-native-full-seams.md)
for edges whose two endpoints participate in flat stars. The native words
are

    A=(65,140.5,147.5,75,112),
    B=(40,144.5,136,47,172.5).

Each sums540 and every angle is strictly between0 and180. These native
orders were selected after a cheap endpoint-continuation attack killed
an earlier order: a formal vertex inventory alone does not guarantee
that the acute corners can actually meet along their incident sides.

## Exact angle gates

If two full copies of A's designated side meet in reflected order, their
140.5 endpoints contribute281 degrees, leaving79. No native angle is79;
two native angles already contribute at least80. In half-turn order the
endpoints contribute205.5, leaving154.5. Exhausting all native multisets
of at most three corners gives no completion. A flat incidence is also
impossible at either obstruction point, since the two prescribed native
angles already exceed180. Thus both full same-native-side orders are
forbidden, including reflections and arbitrary vertex valence.

The complete pure-A native360 census contains only(65,147.5,147.5);
the pure-B census contains only nine40 corners. Neither species has a
native180 star. Consequently neither shape tiles the plane alone, for
any actual metric: most of its native corners cannot appear at any
monohedral vertex, with or without partial contacts. No external
classification theorem is needed for this gate.

There is a positive formal corner ledger for2A+1B:

* flat(65,75,40);
* full(147.5,147.5,65);
* full(140.5,144.5,75);
* full(112,112,136);
* full(140.5,47,172.5).

These consume exactly all15 native corners. It was therefore worthwhile
to test actual geometry; the later contradiction comes from the forced
number of hosted flat contacts, not this unconstrained ledger.

## A normalized three-parameter coordinate family

Define `Cj=cos(j*pi/360)`, `Sj=sin(j*pi/360)`, in the exact cyclotomic
field Q(zeta720). A's side directions in doubled degrees are
`(0,79,144,354,490)`; B's are `(0,71,159,425,440)`.

Normalize A2=1 and choose positive free parameters t=A1, h=B0, k=B1.
Put

    A3=A4=(t*S79+S144)/(-S490-S354),
    A0=-(t*C79+C144+A3*C354+A4*C490),
    B4=1,
    rx=-(h+k*C71+C440), ry=-(k*S71+S440),
    D=C159*S425-S159*C425,
    B2=(rx*S425-ry*C425)/D,
    B3=(C159*ry-S159*rx)/D.

These formulas close both polygons exactly. Choose the open region where
all lengths are positive, `A0>max(A1,A2,A3,A4,B0,...,B4)` and `0<h<A0`.
It is nonempty: t=1/10, h=A0/2, k=1/2 yields

    A lengths approximately(1.302505587,.1,1,1.188170736,1.188170736),
    B lengths approximately(.651252794,.5,.621144166,.480750244,1).

The approximations are display only. The checker computes positivity,
closure, convexity and intersections in exact QQbar/AA using zeta720.
Native coordinates are the partial sums of the specified directed side
vectors. These are actual strictly convex polygons with a strictly long
A0 edge, rather than an angle word awaiting realization.

## Actual four-tile partial-contact module

Reflect one A in the horizontal axis as host, with its A0 edge running
from(0,0) to(A0,0). Set q=(A0−h,0). Above this flat host side place:

* B translated by q, its40 corner occupying sector0–40;
* A reflected horizontally about its75 corner, then rotated292 degrees
  and translated to q, occupying sector40–115;
* A mapped by(x,y)→(-x,y) and translated to q, its65 corner occupying
  sector115–180.

All three are contained in their disjoint angular sectors. The two
internal contact rays have exactly matched full seams: B4=A2=1 at40
degrees, and A3=A4 at115 degrees. Their far endpoint angle deficits
are respectively40 and136, both available native corners. B0 ends
exactly at the host140.5 endpoint, where144.5+140.5 leaves75. The cap
A0 extends to(-h,0), so the host65 endpoint lies strictly inside it,
leaving75+40 to complete another flat star. Exact clipping verifies
all four interiors disjoint and all stated seam endpoints coincide.

Since A0 exceeds every other native side length, a whole matching side
could only be another A0. The angle gate excludes that. Thus every A
tile in any hypothetical tiling must have an interior junction on A0:
genuine partial contacts are forced, not merely permitted by the module.

## Hosted-flat budget excludes the entire constrained family

The complete joint native180 census contains only(65A,75A,40B).
The complete joint native360 census contains nine multisets. The sole
one containing B144.5 is(140.5A,75A,144.5B). B144.5 cannot lie on
a flat contact because its remaining angle35.5 is below the minimum40.

Every A0 hosts at least one interior flat contact. Local finiteness gives
a finite side subdivision; otherwise one neighbouring side would cover
all A0, which its strictly smaller length or the same-A0 angle obstruction
forbids. Such a contact consumes one A75 and one B40. Different flat
hosts cannot coincide at one vertex, since two flat180 incidences leave
no room for native corners.

Let a,b be tile intensities and H the intensity of these hosted contacts.
Native corner counting requires

    H>=a,
    a>=H+b,
    b>=H.

The second inequality counts distinct A75 corners used by hosted contacts
and by every B144.5 full star. It implies b=0; the third then implies
H=0 and the first a=0, impossible for a plane covering.

No positive-frequency assumption about a preselected species is needed.
Alternatively count tiles and vertex incidences in radiusR patches.
The same inequalities hold with O(R) errors, since all tiles have bounded
diameter and a common positive area lower bound. They force both species
counts to be O(R), whereas covering a disk requires Omega(R²) tiles.
This proves impossibility even for sparse defects and arbitrary partial
contacts, without finite-local-complexity or orientation assumptions.

The exact local cap survives, but **the entire specified long-edge
metric family has no plane tiling**. A periodic search or speculative
hierarchy would add no value after this contradiction. Further construction
needs a changed inventory or a changed requirement on hosted contacts;
the formal2A+1B ledger is not a credible existence route.

Artifacts:

* [Exact angle/geometry replay](acute-obtuse-long-edge-feature.py).
* [Certificate and coordinate definitions](../certificates/acute-obtuse-long-edge-feature.json).

Replay:

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python3 research/searches/acute-obtuse-long-edge-feature.py --output /tmp/acute-obtuse-long-edge-replay.json
