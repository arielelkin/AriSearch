# Sugimoto Method 3: exact two-class first gate

Status: independently Sol-reviewed scheme exclusions.
[Hostile review](../reviews/sugimoto-method3-two-class-first-gate-sol-hostile-review-2026-10-19.md).
No pair is proposed and no patch search was run. Checked 2026-10-19.

## Primary source and scope

Teruhisa Sugimoto, *Aperiodic sets of three types of convex polygons*,
[arXiv:2404.00534v5](https://arxiv.org/html/2404.00534v5), Sections 1, 2,
2.2 and Figure 15. The paper forbids reflected pieces. Section 2 and Figure 2
supply a periodic Tile(1,1) tiling using reflections, and explicitly explain
that every published convex dissection inherits periodic tilings when
reflections are admitted. Section 3 also qualifies the paper's positive
claims by its source assumption; those claims are not an unrestricted
shape-only forcing theorem usable here.

This note reconstructs Method 3 exactly, with source edge length one, and
examines (i) any fixed parent-contained repartition and (ii) merging two
whole children along one contact, including a contact across source parents.
Cross-parent boundary-moving exchanges or larger fusions are outside (ii).

## Exact source and incidence

Put X1=(0,0). Successive unit edges Xi to X(i+1), including X14 to X1,
have directions in degrees

`60,120,210,270,180,240,330,270,0,300,30,90,90,150`.

This is an exact definition in Q(sqrt(3)); the vector sum is zero. X13 is a
straight boundary subdivision vertex. For 0<t<1 set

* Q=X6+(t,0);
* R=X8+t*(sqrt(3)/2,1/2);
* S=X10+t*(1/2,sqrt(3)/2);
* T=X12+(0,t).

The five children, in cyclic boundary order, are

* A=(X3,X4,X5,X1,X2);
* B=(X7,X8,R,Q,X6);
* C=(X9,X10,S,R,X8);
* D=(X11,X12,T,S,X10);
* H=(X14,X1,X5,Q,R,S,T).

B,C,D are congruent. Their angle word and A's angle word are
(90,120,105,105,120). H's angle word is
(120,165,165,75,150,150,75). Every listed vertex is strict for 0<t<1.
The internal contact list is exactly

`A-H: X5X1; B-H: QR; C-H: RS; D-H: ST; B-C: X8R; C-D: X10S`.

The remaining child sides form the source boundary. These statements can
be checked from the exact vectors above without measuring the figure.
To verify these assertions throughout 0<t<1, substitute the four affine
points in each edge vector. Each edge is a positive scalar multiple of a
fixed vector on that interval. At t=1 the Q-to-R vector is nonzero, and
its scalar only increases as t decreases; the same holds for RS and ST
by congruence. Thus the listed turns and strict convexity do not change.
Oriented internal edges cancel pairwise. The remaining oriented chain is
the source boundary, with X5X6 and X12X14 subdivided at Q and T. Winding
numbers then show that these five positively oriented convex interiors
cover the source exactly once. This proves the claimed partition without
relying on a drawing.

The paper's rational sample is t=3/5. A has four unit sides and one side of
length sqrt(6-3sqrt(3)); B has side word (1,t,L(t),t,1).
Consequently A and B cannot be congruent for 0<t<1: if t differs from one,
its multiplicity at least two cannot match the single nonunit A side.
At t=1 A and B do become congruent; this is the already published two-class
specialization with a periodically tiling hexagon (Methods 1/2 at 105
and Method 4 at 150). No claim about endpoint degeneration is needed below.

## First metric/topology gate: whole-child two-piece fusion

Lemma. If two compact strictly convex polygons with disjoint interiors have
a convex union with nonempty interior, their intersection is a whole side
of each polygon. At each seam endpoint the two interior angles sum to at
most 180 degrees.

Proof. Their common boundary is a segment on a separating line. At an
endpoint lying strictly inside a side of either polygon, that polygon has
a 180 degree sector and the other polygon has a positive sector on the
opposite side. The union then has angle greater than 180. Thus both
endpoints are vertices of both polygons, and the segment is a whole side
of both. The sector-sum condition is the definition of local convexity.

Every source-exposed side of A,B,C,D,H has at least one endpoint whose
child angle is at least 120 degrees. Every child angle is at least 75
degrees. Thus ANY two whole children belonging to different source
parents cannot have a convex union: at that endpoint the sum is at least
195 degrees. This uses neither edge-to-edge source contacts nor a chosen
source tiling; partial source-edge contacts cannot evade the lemma.
Mirrors preserve these angle bounds.

Within a parent the contact list also rules out all two-child convex
fusions. A-H fails at X1 (105+165=270); B-H fails at R
(105+150=255); C-H fails at R or S (105+150=255); D-H fails at S;
B-C fails at X8 (120+120=240); C-D fails at X10 (240).
Nonadjacent children have no segment contact and cannot form a convex
union. Therefore a single whole-child shared-edge fusion, inside OR
across parents, is unavailable throughout 0<t<1.

This is a narrow exact obstruction, not an exclusion of all cross-parent
resections, fusions of three or more children, or other source methods.

## Parent-contained repartition obstruction

Proposition. Let a polygon U admit a translationally periodic plane tiling
by congruent copies, with reflected copies allowed. Every finite dissection
of U into polygons F1,...,Fk yields an unrestricted periodic tiling by those
child congruence classes. In particular, if a new convex repartition of U
has exactly two child classes, those two classes fail the target.

Proof. Choose one fixed dissection of U. Transport it by the isometry
placing each parent in a periodic U tiling. On each translational orbit of
parents choose the same transported dissection. The resulting children
cover each parent exactly, so they tile the plane. The parent period
preserves the choices and therefore is a child-tiling period. Reflection
of a parent simply reflects all its children, which is permitted. If a
chosen period maps a parent through one of finitely many internal
symmetries, enlarge the period to preserve the finite dissection choice.
Equivalently first choose a translation fundamental domain of parents and
repeat its subdivisions. No decoding or local forcing assumption is used.

Apply this proposition to U=Tile(1,1) and Figure 2. It excludes EVERY fixed
parent-contained split/fusion/resection into two convex classes, even when
it was designed using only the chiral substitution. In particular, splitting
H into copies of A/B, moving internal seams, or specializing congruences
cannot remove the reflected periodic escape. The witness may have partial
contacts; those are allowed. A monohedral escape is not required because
a mixed periodic escape already suffices.

## Exact remaining gap and restart condition

To reopen this source, specify an exact exchange that changes boundaries
across source parents and passes a chiral-collar incidence gate before any
patch search. It must produce exactly two strict convex classes and provide
an explicit reason that the exchange cannot be repeated on the reflected
periodic source tiling. A deterministic translation-equivariant local rule
which is defined on that periodic source would again preserve a period.
A rule defined only on chiral source collars avoids this particular argument,
but then existence, geometric collar forcing in every target tiling, mirror
mixing exclusion, partial contacts, and omission of either class remain
separate proof obligations. No such exact cross-parent boundary-moving
topology is supplied by Method 3 or constructed here.

The source's conditional aperiodicity statement is not used in either
negative proof above. The unrestricted main problem remains unresolved.

## Replay

The retained independent exact arithmetic audit for t=3/5 is
`sugimoto-method3-two-class-first-gate-2026-10-19.py` in this directory.
Run from the repository root:

```text
mise exec -- conda run --no-capture-output -n arisearch python research/searches/sugimoto-method3-two-class-first-gate-2026-10-19.py
```

Observed result: PASS for exact angles, strict convexity, six incidences,
exposed-side angle bound, B/C/D congruences and area identity. It uses
SymPy exact radicals and exact trigonometric constants, with assertions
active. It is an arithmetic audit of this fixture, not an enumeration or
an independent review of the all-t prose argument.
