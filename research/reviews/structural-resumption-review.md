# Independent hostile re-review of unrestricted structural reductions

**Date:** 2026-10-10. **Reviewer independence:** this reviewer did not develop
or repair the submitted global side-count or hexagon/higher-side arguments.
The reviewed versions were read afresh, including their earlier hostile
reviews. No existing lemma was modified during this review.

## Exact claims and verdicts

1. No finite protoset of fixed compact convex polygons with nonempty
   interiors and at least seven genuine native sides per polygon tiles the
   plane, even allowing all isometries and partial-edge contacts.
   **Verdict: valid.** The repaired proof has now received fresh independent
   hostile re-review.
2. Its quantitative form, for tiles whose interiors meet the interior of a
   translated square Q_R, is sum_T(n(T)-6)<=C R+C', with constants depending
   only on the protoset, uniformly over square centers and admitted tilings.
   **Verdict: valid.**
3. If a fixed convex hexagon and a fixed convex n-gon, n>6, tile the plane,
   the hexagon tiles monohedrally and has a periodic monohedral witness.
   Thus the pair cannot be aperiodic under the problem's conventions.
   **Verdict: valid using the named imported unrestricted monohedral
   classification and its classical periodic sufficiency constructions.**
   The repaired sparse-disk/compactness argument has now received fresh
   independent hostile re-review.

These verdicts cover these claims only, not every other theorem in the
shared files. In particular this review does not promote the conditional
finite-state periodicity theorem or unrestricted branching-hexagon
periodicity.

**Submitted artifacts:**
[side-count-and-monohedral-obstructions.md](../lemmas/side-count-and-monohedral-obstructions.md),
[global-side-count-review.md](global-side-count-review.md),
[hexagon-limit-and-periodicity.md](../lemmas/hexagon-limit-and-periodicity.md),
and [hexagon-higher-side-review.md](hexagon-higher-side-review.md).

## Assumptions checked

The finite set consists of fixed genuine convex polygons. Native sides
are maximal straight boundary segments; redundant collinear vertices
are not additional sides. Minimum area a>0, maximum diameter D, and
maximum side count s are therefore finite uniform constants. Tile interiors
are disjoint, tiles cover the plane, and copies are not rescaled or deformed.
Local finiteness is derived, not assumed. No finite local complexity,
repetitivity, use of both types, orientation restriction, or edge-to-edge
hypothesis is inserted.

The same constants work for every admitted tiling of the given protoset.
This is needed when translating windows and taking limits. Convexity is
needed for the native-corner degree lower bound; the proof does not claim
that bound for nonconvex polygons.

## Boundary, separation, and topology attacks

**Unbounded incidence from arbitrarily close contacts.** A tile meeting a
bounded set K lies in its D-neighborhood. Comparing this neighborhood's
area with the sum of the disjoint tile interior areas bounds tile count.
For neighbors of one tile, fix a point in it; all touching tiles lie in a
uniform disk of radius 2D around that point. This bounds neighbors even
when many contacts are tiny or only points. Two interior-disjoint convex
polygons intersect, if at all, in a point or segment, so contact endpoints
per pair are uniformly bounded. A finite native side count bounds all
remaining corners. Thus graph subdivisions per tile are uniformly bounded.
No minimum contact length or vertex separation is required here.

**Disconnected graph from square selection.** Each selected convex tile
has a point in int Q_R and is connected to Q_R; the union covers Q_R.
The selected union is connected. Its boundary graph is also connected:
the intersection graph of finitely many closed selected tiles is connected,
and each nonempty tile intersection connects their polygon boundary cycles.
A point contact is at a native corner of at least one polygon, so it is
included among retained graph vertices. If two side-interior points of
disjoint convex interiors meet, their supporting lines coincide locally,
which gives a segment contact rather than an isolated transverse crossing.
There are no unrecorded graph crossings.

**Holes and pinch points.** Selected unions need not be disks and their
boundaries need not be disjoint Jordan curves. The proof's Euler equation
uses H, the number of bounded complementary components. The connected
embedded graph has N tile faces, H hole faces, and one unbounded face,
so V-E+N=1-H is correct even at pinches. Each hole has an exposed boundary
edge. Boundary edges have a unique complement face on their exposed side,
so H<=B. Every boundary vertex lies on the finite exposed-edge subgraph;
it has at least two boundary rays because a finite union of polygons has
no isolated missing-point complement. Thus V_b<=B also holds at pinches.
The artifact's weaker V_b<=B+O(1) is sufficient.

**Degree-two vertices and subdivisions.** A retained native corner has
angle strictly below pi. Two rays cannot fill a full neighborhood with
convex interior-disjoint tile sectors: the complementary sector exceeds
pi. At a genuine subdivision, the transverse incident rays likewise
force at least degree three. A boundary vertex lies on a tile boundary
cycle and has degree at least two. Suppression of collinear degree-two
vertices never removes a genuine native corner. The degree inequality
2E>=3V-V_b follows.

**Boundary tiles well inside the square.** A selected tile not meeting
partial Q_R must lie wholly within int Q_R, by connectedness. A generic
point of an exposed edge would then be in int Q_R, and the tile across
that point would also have interior in int Q_R and would be selected.
This contradicts exposure. Thus every boundary-edge contributor touches
partial Q_R and lies in its D-neighborhood. This strip has area O(R),
so boundary tiles number O(R); the uniform contact bound proves B=O(R).
Point-only outside contacts do not create boundary edges or spoil this
localization.

Combining Euler and degrees gives E<=3N+V_b-3+3H. Each native side has
at least one graph piece, and pieces are incident to at most two tile
faces, hence S<=2E. Therefore S-6N<=2V_b-6+6H=O(R). For all native side
counts >=7 this gives N=O(R), contradicting N>=4R^2/A. This is an actual
proof contradiction, not a bounded computational observation.

## Sparse-type disks and compactness attacks

For a hexagon/n-gon pair, the quantitative inequality gives
(n-6)N_n(Q_R)<=C R+C', uniformly in the translated window. The artifact
occasionally calls this the number of tiles "meeting" Q_R although its
selection counts interior intersections. This harmless convention is
bridged by enlarging the square by any fixed positive margin: a tile
meeting closed Q_R has some interior point in int Q_(R+epsilon). The
linear bound remains uniform. No new hypothesis is needed.

Fix L. Candidate centers at mutual spacing greater than 2(L+D) give
Omega(R^2/(L+D)^2) disks inside the square. One higher-sided tile cannot
intersect two such disks: points in the two intersections would have
separation exceeding D. Even a bounded-number variant suffices. Since
only O(R) higher-sided tiles are present, taking R sufficiently large
compared with (L+D)^2 provides a radius-L disk avoiding them. A sparse
network of barriers, nonrepetitive clustering, and long strips cannot
invalidate this counting argument.

For compactness one can choose an interior anchor and a common protected
inball radius rho>0 for the finite reference set. Tile anchors then have
pairwise separation at least 2rho. Anchor counts in bounded windows are
uniformly bounded; orthogonal placement matrices lie in compact O(2).
A diagonal subsequence of bounded indexed placements gives a locally
finite limiting collection, without requiring finitely many orientations.
Distinct tiles cannot merge because their protected inballs stay separated.
An interior overlap persists under placement convergence. Coverage is also
closed: for any fixed point only uniformly finitely many bounded-anchor
slots can cover it, and some converging slot does so along a subsequence.
Every limit tile is a genuine copy of one fixed prototile. Translated disks
with radii tending to infinity exclude all higher-sided occurrences from
any fixed limit window. Thus the limit is a monohedral hexagon tiling.

Uniform separation of **native vertices** is unnecessary for this sparse
limit: the conclusion only needs a tiling by hexagons, not preservation of
edge-to-edge contacts. The separately reviewed sector-disk separation
repair matters when obtaining the trivalent edge-to-edge limit. It is not
silently reused as a hypothesis for arbitrary initial tilings.

## Classification dependency and source inspection

The imported source is Zhu, Wang, Yan,
[Hexagonal Tiling of the Plane, arXiv:2508.01404v2](https://arxiv.org/html/2508.01404v2),
revised 2026-04-28. Fresh primary-source inspection checked the Main Theorem,
its introduction's convexity implication, Section 2's unrestricted-contact
setup, and its treatment of flipped first-layer copies. The theorem concerns
one congruence class with at least three incident tiles at each vertex and
concludes the three Reinhardt types. Convex tilings satisfy the incidence
hypothesis. This review accepts that imported theorem; it does not
independently reexecute the source's full classification calculations.

The elementary classical sufficiency constructions for those types give
periodic witnesses, not a claim that every original monohedral tiling is
periodic. Since the target permits omission of either member, the witness
alone defeats the pair's universal aperiodicity. The source theorem is
monohedral and cannot be applied directly to two different hexagons.

## Defects, repairs, and remaining uncertainty

No substantive defect requiring repair was found in the two submitted
structural arguments. The interior/closed-window wording above is a
clarification with a direct implication, not a change of theorem. The
unrelated triangle/quadrilateral corollary contains the apparent typo
"Hence neither shape has a periodic monohedral tiling" immediately after
constructing such tilings; the intended word is "either". This review's
verdict does not depend on that sentence.

The only external dependency in the higher-side verdict is the named
monohedral classification and classical periodic constructions. This is
an imported theorem boundary, not a proof of unrestricted mixed periodicity.
No proof-relevant finite search was needed for the re-review. Therefore
there is no finite solver domain or new certificate to promote.

## Consequence and the branching target

The proofs still leave exactly the necessary candidate alternatives:
a pair with a pentagon, or two hexagons. The hexagon argument does not
force deterministic neighbors, finitely many absolute orientations, or a
periodic admissible quotient.

A NEW concrete strengthening was extracted during this audit in
[two-type-uniform-density.md](../lemmas/two-type-uniform-density.md): if a
proper subset of a fixed finite convex protoset does not tile, every admitted
tiling has a common bounded-radius occurrence guarantee for the complement,
uniformly over all tilings. In a hypothetical aperiodic hexagon pair, neither
member tiles monohedrally, so both types have uniformly positive lower tile
and area densities, including in every defect-free limit. This extension
is authored by the present reviewer and **is not independently reviewed by
this record**; the root is separately reviewing it.

That strengthening removes disappearance and arbitrarily dilute type
sequences as possibilities for a fixed hypothetical aperiodic pair. It
does not resolve branching: syndetic type occurrence does not determine
which side slots meet, identify complete neighbor isometries, or guarantee
that an angle/length-legal local language has a flat periodic quotient.
A material next mechanism must prove one of those geometric compatibility
facts for repeated side words outside already reviewed periodic cones.
