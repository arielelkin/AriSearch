# Whole-child fusion saturation: exact Method 3 scope

Status: independently Sol-reviewed within its stated scope. 2026-10-19.
[Hostile review](../reviews/sugimoto-method3-saturation-scope-sol-hostile-review-2026-10-19.md).
Dependencies: exact coordinates and incidence in
`research/searches/sugimoto-method3-two-class-first-gate-2026-10-19.md`.
No finite patch enumeration is used.

## Saturation lemma

In a tiling by convex polygons, let K be the convex union of a finite
set of whole tiles. If two selected tiles meet at p with disjoint interior
sectors of total angle greater than 180 degrees, then p is an interior
point of K. Hence every tile incident with p must belong to the selected
set (if its interior meets arbitrarily small neighborhoods of p).

Proof: a boundary point of a convex polygon has available angle at most
180 degrees. Since K contains the two sectors it cannot have p on its
boundary. A disk around p lies in K; omitting any incident tile would
omit an open sector of that disk, contradicting disjoint tile interiors.
The same proof handles a vertex lying in the interior of another side,
where the corresponding tile contributes 180 degrees.

Apply the rule repeatedly to obtain a necessary closure operator on
selected tiles. Every finite convex union is closed under this operator.
Closed sets need not be convex. Termination of closure is not ruled out
by the existence of one over-180 endpoint per seam.

## All-size exclusion inside a single Method 3 parent

Use the source children A,B,C,D,H and parameter 0<t<1 from the dependency.
There is no convex union of two or more whole children all contained in
one source parent.

Proof: a connected union with more than one tile must contain two tiles
with segment contact. The only contact edges are A-H, B-H, C-H, D-H,
B-C, C-D. If A and H occur, their sectors at X1 total 270 degrees; the
missing 90 degrees lies outside the source parent, so the union fails
convexity. If B and C occur, their sectors at X8 total 240 degrees;
the missing 120 degrees lies outside the source. The same argument
excludes C and D at X10. If H and B occur, R has selected angle 255
and saturation forces C. If H and C occur, saturation forces B at R
and D at S. If H and D occur, S forces C. In each case one of the
already excluded B-C or C-D pairs is obtained. Other contacts are
point contacts only and cannot make a full-dimensional convex union
of two disjoint-interior polygons. This exhausts all connected cases,
independently of cluster size.

## What global propagation actually forces

For a convex cluster crossing source parents, the same rule now requires:

* selected B+C at X8: include the unique external child contributing
  the remaining 120 degree sector;
* selected C+D at X10: include the unique external child contributing
  the remaining 120 degree sector;
* selected A+H at X1 or X5: include the unique external child contributing
  the remaining 90 degree sector.

Uniqueness follows because the smallest child angle is 75 degrees, and
both residual sectors are smaller than 150 degrees. These external
children exist in the original source-derived tiling. The 120 degree
sector may belong to A, B/C/D, or H; the 90 degree sector belongs to a
pentagonal child. Their incident edge lengths, possible T contacts and
source-parent placement determine subsequent closure. The single-parent
incidence graph alone does not specify these data. In particular, the
above step does not immediately force every child in the new parent.
An infinite-propagation claim needs an additional exact invariant or a
complete collar transition theorem, neither supplied here.

## Counterexample to the general infinite-propagation inference

Even a convex tiling in which every elementary interface has an endpoint
with incident selected-pair angle greater than 180 degrees can contain a
finite convex multitile cluster.

Take a regular unit-circumradius hexagon with counterclockwise vertices
v_j=(cos(j*pi/3),sin(j*pi/3)), j=0,...,5, and center O. Let m_j be the
midpoint of v_j v_(j+1). Join O to m_0,m_2,m_4. This partitions the
hexagon into three congruent strict convex pentagons, one being
(O,m_0,v_1,v_2,m_2). Its angle word is (120,90,120,120,90).
Each pair of pentagons shares a radial seam; their sectors at O sum
to 240 degrees. Thus no pair fuses convexly, but all three form the
convex hexagon. Saturation forces the third tile and stops.

To make a plane tiling, use the regular-hexagon honeycomb and repeat this
same subdivision by translations of the hexagon centers. For elementary
interfaces along a parent hexagon side, each subsegment has a hexagon
corner endpoint. At that corner, any pair of incident children has
120+120=240 degrees. Midpoint T contacts cause no problem: the common
interface subsegment still reaches a hexagon corner. Every radial seam
has the center endpoint with 240 degrees. Thus the stated over-180
endpoint property holds throughout this periodic convex-pentagon tiling,
yet each three-pentagon parent is a finite convex union. Its coordinates
are exact in Q(sqrt(3)). This is a counterexample to the general inference,
not a Method 3 counterexample.

## Scope and restart condition

The Method 3 parent-contained all-size exclusion is proved above. The
absence of arbitrary finite convex whole-child clusters across source
parents is unresolved. No bounded cluster-size search would settle that
unbounded statement. Reopen it only with exact external-collar transitions
and a monotone/infinite-path invariant, or with an exact finite convex
cluster counterexample. Reflections and partial contacts must be retained
in that transition analysis. No discovery-log edit was made.
