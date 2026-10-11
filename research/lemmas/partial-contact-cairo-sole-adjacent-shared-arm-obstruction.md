# Sole shared e-adjacent arm: complete optional-seam obstruction

**Status: independently adversarially reviewed VALID**; see [the fresh model and dual audit](../reviews/partial-contact-cairo-optional-seam-obstruction-review.md). Both the original102 chamber route and a weaker16-model order-free route have passed independently.

## Exact scoped statement

Let P=(s,b,c,d,e) and Q=(A,B,C,s,f) be Cairo pentagons with native
side directions0,90,150,240,300 degrees and positive side lengths. Let each
species have four distinct native right-angle arms. Assume the only equality
between any of the eight native arm slots is Pa=Qd=s. Then the pair cannot
tile the plane, allowing all isometries, reflections, arbitrary partial
contacts and omission of either species.

This concerns the e-adjacent120 arm in both species. Native reflection maps
(a,b,c,d,e) to(d,c,b,a,e), so it includes all orientations of this same
shared-arm orbit. It does not include an isolated120 arm b/c shared with an
e-adjacent arm, the both-isolated orbit, additional cross sharing, internal
repeated arms, other pentagon angles, or arbitrary convex polygon pairs.

## Reviewed reduction and exact finite domain

The independently reviewed [event-flat reduction](partial-contact-cairo-one-shared-event-flat-reduction.md)
and [fresh audit](../reviews/partial-contact-cairo-one-shared-event-flat-reduction-review.md)
reduce every possible metric satisfying these hypotheses to one of exactly
16 relative-open dimension2 strata, including common scale. All deeper
arrangement resonances are separately enumerated and excluded. Positive
normalization s=1 leaves one parameter. Removing all privacy and inactive
event roots and cutting at native arm-order changes yields exactly102 open
chambers, with complete exact native side forms and intervals in the
retained certificate. Proper-event roots move to already excluded deeper
flats; privacy roots leave the statement's hypotheses.

The computation below constructs a necessary finite balance model in each
of these102 chambers. It retains exact rational duals in every case. No
finite plane patch search, bounded periodic search, or sufficiency assumption
is used. The four separately reviewed notch obstructions are independent
confirmation only, not needed by the proposed complete seam proof.

## Complete optional subdivision inventory

All possible angular stars are90^4,120^3, or90+90+180. Every native120
vertex is a three-native-corner star; every subdivision point is a T. The
[reviewed two-T switch](partial-contact-cairo-two-t-switch.md) proves that
every native side has at most one interior T and that each perpendicular
seam at a T is whole90-to120 on both bank tiles.

Keep the actual native arm slots i=0,...,7 with perpendicular involution
(1,0,3,2,5,4,7,6). A native event is an ordered pair(i,j) whose perpendicular
arms have equal lengths; its bank total is L_i+L_j. Let S_i contain precisely
the totals of events actually containing bank slot i. Self pairs are
permitted, and the one shared arm has both actual slots retained.

A whole native side is always included as an optional occurrence, even
when other contacts later make it impossible. A fifth side can additionally
be cut into either ordered bank pair of any actual event whose total equals
its native length. Each piece has positive length and endpoints120/180.

For a native arm of length M with an interior T, start from its120 endpoint.
The opposing first bank has length m<M and ends at that T. The two-T switch
gives events containing that actual bank slot and this actual host slot,
with the same total: m+n=M+q,0<m<M<m+n. Consequently m belongs to a native
slot j with S_j intersect S_host nonempty. Include every such smaller m as
a possible cut, making ordered pieces(m,M-m) from120 to90, or the reverse
in native boundary order. This is an overapproximation: a common event total
is not asserted to suffice. Every real cut is present. All independent
combinations of these optional cuts on the five native sides are retained;
any unrealizable combination only enlarges the model.

The set of permissible smaller native arms is constant on each reviewed
arm-order chamber. Fifth-side/event identities and all event-total identities
are constant on its relative stratum. Thus there is no inference from a
single metric sample to a changing contact inventory.

## Refined edges, corners, reflections and conservative colors

A refined edge signature records species, native side index, its complete
ordered partition, and the segment index. Its endpoints retain native
boundary labels0 and1. The signature ignores other cuts on the same tile;
identical actual edge geometries may therefore share a signature.

The finite corner state records the actual angle and the ordered incoming
and outgoing edge signatures. A tile variant supplies the multiset of all
these corner states, including any introduced180 points. Different variants
may share a corner state. Each state has both original and reflected sector
orientations: outgoing/incoming endpoint labels(0,1) or reflected(1,0).
No restriction on physical rotation is imposed; sector angle and ray data
are invariant under it.

For ray compatibility, a refined piece color records its number of120
endpoints (0,1,2). If at least one endpoint is120, also record its exact
length form on the entire flat. The length is either a native bank arm or
a whole fifth side. Their equality changes are already completely covered
by native privacy and the reviewed arrangement. A120 endpoint cannot occur
inside any native side or meet90/180, so opposite copies of a genuine shared
piece have the same120-endpoint count. Their positive lengths are equal.

A residual piece without a120 endpoint deliberately discards its length.
This permits even unequal residuals to share a ray in the finite model and
is a safe overapproximation. In particular no new residual-length equality
hyperplane needs to be assumed absent. Retaining fewer constraints can never
create an invalid obstruction certificate. No edge identity or length-class
transitive closure replaces the actual corner or seam signatures.

Enumerate every cyclic star of three or four oriented corner states having
total angle360, matching ray colors, and require a90/90 ray to have exactly
one120 endpoint on its full shared piece. The latter is necessary because
a perpendicular90/90 seam is a whole native arm on both tiles. These stars
include every actual tiling vertex. Rotation of the cyclic sector list is
the only deduplication; both reflected sector orientations are retained.
The producer's least-index recursion is a finite enumeration optimization,
not an additional geometric restriction.

## Two-ended seam potentials

For a shared ray between refined edge signatures x,y at native endpoint
labels epsilon_x,epsilon_y, sort x<=y and use feature

    (x,y,epsilon_x XOR epsilon_y),

with coefficient+1 if the sorted first edge's endpoint label is0 and-1
if it is1. At the opposite end of this same actual shared segment both
labels flip, preserving the feature and reversing its coefficient.
Thus its feature cancels when both endpoint stars are summed. When x=y and
the endpoint labels differ, omit the feature: it has no distinguished first
edge, and setting its potential0 is conservative. All other keys have the
stated canonical sign. Segments are fully refined at every native or T
endpoint, so this cancellation concerns actual complete shared pieces.

For each chamber the retained certificate gives rational corner weights W
and rational signed seam potentials Y. The exact inequalities are:

- every permitted oriented star has corner charge plus seam charge>=0;
- every optional whole/T tile variant has total corner charge<=-1.

The producer reconstructs proposals from a numeric optimizer, then verifies
every inequality with exact Fraction arithmetic. Numeric infeasibility alone
is never a certificate. All102 models have retained exact duals; none is
accepted on a numerical equality tolerance or an unrecorded search.

## Why such a finite dual excludes a plane tiling

Fix any actual metric in one chamber. All native side lengths and all
possible subdivision lengths are positive, with finite inventories. Tiles
have fixed positive area, bounded diameter, and at most ten refined corner
occurrences. The number of tiles meeting a fixed-width annulus about a disk
of radius R is O(R): their interiors are disjoint, each has a positive fixed
area, and all lie in a slightly thicker annulus. At least Omega(R^2) tiles
lie inside the disk, by coverage and the fixed maximum tile area.

Sum the corner weights of all tiles contained in the disk. Their total is
at most minus their number. Reorganize by complete interior stars and the
remaining boundary corner occurrences. Only O(R) occurrences are incomplete,
and all weights have a finite bound. Every complete star is bounded below
by minus its signed seam potentials. Interior segments cancel their two
endpoint potentials; segments touching the incomplete boundary account
for only O(R) further bounded features. Thus the same total corner charge
is at least-O(R), contradicting its at most-Omega(R^2) bound for sufficiently
large R. This is an unrestricted plane obstruction, not an assumption that
frequencies of all individual variants exist.

The argument permits either species frequency to vanish; each variant of
each species has charge<=-1. The preceding event-flat missing-corner
reduction separately justified omission using the reviewed distinct-arm
monohedral obstruction.

## Computation and remaining review obligations

[Producer](../searches/partial-contact-cairo-one-shared-optional-seam-balance.py)
and [retained duals](../certificates/partial-contact-cairo-one-shared-optional-seam-balance.json).
Normal replay is read-only; use --output only to explicitly retain results.
The exact finite domain is16 reviewed relative strata and their102 chambers,
all optional native cuts just defined, all corresponding native corner
orientations and cyclic stars, and their two-ended seam inequalities. No
random seed, geometric cutoff, orientation cutoff or time cutoff is used.

    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-one-shared-optional-seam-balance.py

The completed independent review reconstructs subdivision completeness, mirrored
endpoint labels, safe colors and chamber invariance, all stars, every dual
inequality, and the boundary growth argument. The original problem remains
unresolved even if this scoped theorem survives review.


## Reviewed order-free shortcut

A separate [sixteen-model certificate](../certificates/partial-contact-cairo-one-shared-order-free-seam-balance.json) drops every strict bank-order test m<M and includes all different bank forms sharing an actual event total with the host. Some abstract residuals are then negative, but their length is never used and no polygon geometry is claimed for these extra variants. Every actual positive cut is retained. This further relaxation still has exact duals for every one of the16 full relative flats. The fresh review independently reconstructs all3532 star inequalities and624 negative variant inequalities. It supplies a shorter full-flat proof requiring no102-chamber decomposition. The original reviewed chamber proof is retained as a separate exact check.
