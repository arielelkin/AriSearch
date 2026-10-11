# Hostile review of the full fixed-B hexagon family classification

**Reviewer:** partial_contacts, independently assigned by root. This reviewer
neither authored nor repaired the classification proof. The author supplied
only the artifact path and requested attacks. The reviewer read the entire
new proof, its two prior reviewed mechanisms, and the unrestricted hexagon
limit dependency. No author code was executed or imported; this is a
proof-only artifact with no numerical component.

**Artifact:** [full classification](../lemmas/branching-hexagon-new-fixed-b-classification.md).
**Verdict:** **VALID after an explicit species-omission clarification.** Root
independently identified the missing A-only exclusion and supplied its short
argument. This reviewer freshly inspected the author's actual insertion,
which excludes the A-only limit by the odd pq three-ray cycle, and the B-only
limit under S!=360 by the r-dimer star. Both arguments are valid. The author's
revised compactness coverage paragraph was also independently checked: a
dense set of generic straight segments crosses at most the bounded number
of convex tiles, and the finite closed adjacency-ball union then covers the
entire disk. This review covers those exact revisions.

## Scope audited

A is a fixed genuine strictly convex threefold alternating p,q hexagon with
p!=q and alternating angles120+delta,120-delta,0<delta<60. B is a fixed genuine
strictly convex hexagon with word(r,p,q,q,q,q), r,p,q pairwise distinct. Every
isometry is allowed. The conclusion is existence of an admitted tiling with
a nonzero translation whenever the pair tiles, including original arbitrary
contacts. It does not say every original tiling is periodic, prove arbitrary
two-hexagon periodicity, or impose a marking or chirality rule.

## Local ledger and exhaustive angle cases

The unique r seam cannot use its reflected same-slot mate: two rp corners
would force pp, absent from both shapes. Its half-turn mate gives B0/B1 at
both ends. A B2 filler there would give beta0+beta1+beta2=360 and hence
S=beta3+beta4+beta5=360, already supplying the independently verified two-B
periodic escape. Otherwise the filler is A of fixed angle kappa. This fixes
both adjacent A placements since its three equal slots are intrinsic
rotations and its two orientation signs exchange the distinct alternating
angles at a selected endpoint.

At B2 the known A has kappa'=240-kappa, leaving a B qq target of angle
mu=360-beta2-kappa'. Angle total720 gives S=240+mu. If two qq slots equal mu,
the third nu satisfies mu+nu=240. All four possible multisets have excess
(2k-3)(mu-120), k=0,1,2,3, which cannot vanish under S!=360. This really
excludes all ten native multisets despite the repeated value, and licenses
exactly the reviewed nonresonant chain theorem. Three copies of mu force
mu=120,S=360. Only a unique required slot remains. No independent qq
resonance is silently discarded.

Two sources cannot use one target: they would be two B pq sectors at one
vertex with their p sides opposite one another, contradicting the already
forced A p neighbors. With a unique required slot, the source-to-owner map
is therefore an injection on B copies, not an assumed bijection.

## Saturation: no zero-density-to-absence leap

Source and target owners are within a fixed distance2D. Sources with centers
in radius R-2D inject into owners in radius R, so unused owners in radius R
number at most N_B(R)-N_B(R-2D). The annular O(R) bound follows from fixed
positive B area and disjoint interiors, with the annulus enlarged by D on
both boundaries. It does not require a species frequency or lattice.

For fixed n, the union of radius n+3D disks about these O(R) centers has
area O(n^2 R), while an inner disk has area proportional to R^2. Taking
R sufficiently larger than n^2 leaves an unoccupied center point. Restricting
to the inner disk ensures centers outside radius R cannot intrude into the
chosen radius n+3D disk. Every A q side meets B (an A/A q seam needs a pp
filler), so a B root is uniformly close to that point. Rooting by an isometry
retains unused-target-free disks whose radius tends to infinity.

Full native side matching yields only finitely many neighbor placements:
type, native equal-length slot and orientation sign determine the isometry.
Diagonal stabilization of rooted adjacency balls thus uses exact finite
states, with no assumed globally finite orientation set. To check plane
coverage, every tile meeting a fixed disk is contained in its bounded
enlargement; positive minimum area bounds their number uniformly. A segment
from the root through that disk, perturbed off the finitely many vertices,
can be chosen to cross only boundedly many tiles. Convexity lets an
unperturbed segment meet each tile at most once; a sufficiently small
perturbation introduces only bounded local detours. Therefore a bounded
adjacency ball covers the disk in every approximant. Exact stabilization
preserves coverage, interior disjointness and all three-sector native stars.
A target's usage is determined by such a finite neighborhood, so every
target in the admitted limit is used. Only this limit is claimed saturated;
the source tiling is allowed to have infinitely many sparse unused targets.

## The three unique-target positions

**j=3.** At a side2/side3 or side2/side4 match, its other endpoint includes
an original B3 plus a qq mate. The saturation rule instead requires that
B3 have B2 and A there, ruling out both slots without any numerical
three-qq nonresonance. Side5 already meets A; the reflected same-slot2 match
requires pp. Side2 therefore matches its own slot by a half-turn. This
forces side3 to meet A. A side4/side4 mate would have two qq sectors and
the known pq A sector at its corner4, an impossible odd p halfedge count.
Thus sides1,3,4,5 have unique A placements. Every A q side meets one of
these B q sides, so the entire A set is determined by the B set.

The midpoint segment between distinct nonadjacent B sides0 and2 lies in B
interior and has positive length. Half-turn continuation advances by that
length at every seam and gives bi-infinite straight chains, each invariant
under a common-length two-step translation. The prior repaired crossing
argument covers intersections in a tile interior, seam midpoint and a
line tangent to the first seam: an interior ball from a nearby second-chain
point must overlap an incident first-chain B interior. Distinct chains
cannot cross, hence all are parallel. Their translation vectors agree up
to sign, which still gives one period of the whole B set. Its unique A
neighbor set inherits the same vector.

**j=5.** Since side5 meets A, every saturated B5 uses side4 opposite its
B2 source. This forces the global native side2/side4 matching in both
directions. The other seam endpoint is B3/B4 with a third qq sector.
It cannot be B5, whose saturated star includes A. At a vertex composed
only of B3 and B4, each B3 contributes exactly one native2 halfedge and
each B4 exactly one native4 halfedge. The forced matching equates their
counts, while three sectors gives an odd total. This is a local incidence
contradiction, not a limit or average parity claim.

**j=4.** A side2/side4 match would put B3 and B5 at its other endpoint,
contradicting the fixed A neighbor incident at B5. Thus side2 matches
side3, side4 meets A, and the other endpoint of a2/3 seam must be B3^3
because B4 is saturated with A and B5 has its fixed A neighbor. Hence
beta3=120. The A across side4 has kappa' at B4, kappa at B5; the A across
side5 has kappa at B0, kappa' at B5. Thus beta5=120. The only possible A
q-neighbor slots are4 and5.

I checked the ledger from native corner incidence: tag4 has an A p neighbor
at its kappa endpoint B5 and B p neighbor at its kappa' endpoint B4;
tag5 has a B p neighbor at its kappa endpoint B0 and A p neighbor at its
kappa' endpoint B5. Every A p side has one endpoint of each angle, so its
neighbor type can agree at both ends only when its adjacent q tags differ.
The three q sides alternate through three p sides in a closed odd cycle.
A two-coloring with every adjacent pair different is impossible. Reflection
reverses cyclic order but cannot remove odd parity.

## Dependencies and limits of the verdict

The unrestricted conclusion imports only the separately reviewed
[defect-free hexagon limit](../lemmas/hexagon-limit-and-periodicity.md), and
uses the already reviewed monohedral two-B construction and private-chain
proof in the stated cases. This audit does not silently extend their
hypotheses. Both original species may be omitted; the inserted A-only
exclusion repairs the sole presentation omission identified. The result closes
this fixed side-word family and its qq-resonant cases; it gives no
classification for other B words, non-threefold A or non-distinct r,p,q.

No exact computation is needed: the angle reduction is a four-value
identity, and all remaining finite parity statements were checked directly
from native side incidences. No bounded patch search or local-to-global
extension assumption is used.

**Fresh final insertion audit:** read the revised local-ledger and coverage
paragraphs from disk after the author announced completion. No substantive
new gap was found. The broad family theorem and all three unique-target
positions receive the VALID verdict above.
