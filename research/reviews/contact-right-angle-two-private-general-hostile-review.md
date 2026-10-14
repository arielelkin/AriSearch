# Fresh independent hostile audit: all-metric nonsymmetric two-private escape

Date:2026-10-13. Reviewer source_recovery. Verdict: VALID.
Final synthesis reviewed:
research/lemmas/contact-right-angle-two-private-all-metric-periodic-escape.md.
Dependencies independently examined: unrestricted native reduction,
contact-structure-two-private-octagon-clean-r-limit.md, periodic-core.md,
complement-bands.md and periodic-scaffold-anchored-strip-completion.md.
The obsolete duplicate draft is not used as a theorem dependency.

## Scope and exact quantifiers

P has one90 and four112.5 native angles, Q eight135; P's acute lengths u,v
are unequal. Exactly two NATIVE Q slots have numerical lengths absent from
ALL P native lengths. Those two lengths may coincide. All other coincidences,
reflections and initial partial contacts are allowed. The conclusion is:
ANY plane tiling existence implies existence of SOME nonzero-translation
periodic tiling of the SAME unmarked polygons. Original fillings are not
claimed periodic; doubly periodic completion is not asserted.

No omission loophole exists in the cleaner plane tiling: neither P-only nor
Q-only can fill its native112.5 or135 corners using the admitted angular
language. The compactness construction need not artificially force species
persistence; it follows again from the original angle palette after the limit.

## Direct clean-limit repair checked

The main initial risk was misapplying the existing zero-per-prototile potential
lemma: weights(112.5,90,135)=(1,4,-2) give Ptotal8,Qtotal-16, not individual
zero. The final proof explicitly DOES NOT make that invocation.

Instead wholeQQ incidence and fixed degree2 give y_PQQ=2q+O(radius).
The native corner ledger gives y=4q-p+O(radius) and
p=2q+2z+t+O(radius), hence p=2q+O(radius),2z+t=O(radius) uniformly in
square centre. Boundaries involve only fixed-diameter positive-area packing.
Thus positive-score stars (fourright score16, flat score8) are linearly sparse.
Disjoint growing candidate disks versus this linear bound give genuinely
clean disks of arbitrary radius.

Indexed-placement compactness preserves coverage and interior nonoverlap
without assuming a finite orientation set or vertex separation. At a limiting
native-corner position, isolate its finite corner-occurrence cluster. The
approximating corner multiset is in bijection with the limiting occurrences;
grouping it by actual approximating positions gives ENTIRE zero-score stars.
Adding their weights gives exactly zero limiting score, even if positions
coalesce. Side-interior hosts contribute zero, so no native/flat bookkeeping
weight changes. This is additive score preservation, not an unsupported claim
that all finite contact languages are closed under limits.

The fixed palette admits only PPQ/PQQ zero stars. Therefore the limit has no
flat or fourright vertices and is edge-to-edge/trivalent. Every Pacute corner
has twoQ neighbors, so all P are typeR. Privacy and native reduction again fix
bothQQ slots in this NEW tiling. No second S-free/FLC step is required.

## Endpoint tags and all numerical aliases

In typeR the only Q-labeled P slots are u,v,w. Native x/y slots remain PP,
even when their numerical values collide with u/v/w. A public Q edge next
to a private edge has a90 P endpoint and is acute-tagged u orv. A public edge
with neither endpoint QQ has two112.5 P endpoints and is w-tagged; no other
typeR Q-labeled P edge fits those endpoint tags. Mask spacing excludes a
public side with QQ at BOTH ends.

Thus w=u orw=v does not introduce an alternate acute-vs-middle assignment.
Each P contributes one Qcontact of each tag. Whole-contact incidence and
p=2q+O(radius), with q quadratically large, give twoQ sides of each tag.
The argument counts fixed indexed TAGS, not distinct numerical lengths.

## Equal-private geometry independently crosschecked

After dihedral normalization the only two masks are0,3 or0,4.
For0,3 write the side word(H0,a,b,H3,c,w,w,d), acute a,b,c,d in{u,v}.
I independently derived closure

    H0=(1+sqrt2)w-sqrt2*a+c-b,
    H3=(1+sqrt2)w-sqrt2*b+d-a.

If H0=H3, factor the nonzero u-v from acute tags. The remaining integer
coefficients of1 andsqrt2 force a=b,c=d. Two-each tag counts then force the
pairs to be opposite tags. This independently verifies the final proof's
short-gap full PP x/y argument, including all w/u/v collisions.
The cyclic word(H,u,u,H,v,w,w,v) has an actual reflection exchanging slots0,3;
its ordered positive equiangular edge cycle determines the reflected polygon
set, not merely a symbolic word.

For0,4 the opposite private and w vectors cancel; closure of diagonal acute
slots forces a=c,b=d. Hence Q is centrally symmetric, with its halfturn
exchanging private0,4. No noncentrality assumption may be used in this case.

Any alias match to the second private slot is equivalent, after composing
with the proved Qsymmetry, to a match to the first. The physical neighboring
polygon options reduce to endpoint-fixed reflection or midpoint halfturn.
The reflection forces equal outgoing QP acute lengths at a P90 corner,
contradicting u!=v. Thus only the actual midpoint-halfturn placement survives.
The argument quotients actual polygon sets and adds no orientation mark.

## Central-Q cycle repair and common scaffold

The consistent indexed lift records the entering private slot, so the next
step uses the other slot. If Q0=gQ, then Q1=gHiQ,Q2=gHiHjQ=Q0+a;
Q3=Q1+a. Thus Q_(n+2)=Q_n+a for ALL integer n, with
|a|=2|mi-mj|>0. If a physical cycle has ktiles,2ksteps simultaneously give
Q_(n+2k)=Q_n andQ_n+k*a, impossible for a compact polygon. This is valid even
for centrally symmetric Q and avoids the old false odd-cycle shortcut.

Centroid-to-midpoint core pieces lie inside convex Qinteriors, and onlyQQ
neighbors meet along their seam points. Nonneighbor Qpoint contacts are
excluded by the PPQ/PQQ language (twoQ forcepositiveQQ boundary). These
cores are simple proper curves consisting of a finite repeated motif, with
uniform bounded distance to their period lines. Proper-line Jordan separation
forces parallel directions for disjoint cores. Period lengths are identical
for the fixed Q and private pair, so sign choice gives one common nonzero
scaffold period. Qsymmetries swapping private indices change only its sign.

## Complement-band and periodic-completion gates

A chain of convex disks joined at two nonadjacent full sides is a proper
closed topological strip. Translation preserves both longitudinal boundary
curves individually, not merely the chain support. Disjoint proper cores have
a total transverse order. Finiteness between two chains follows by translating
centroid representatives into a compact longitudinal period band and area
packing; local finiteness alone would not have sufficed.

Every P has wholeQ anchors, so every Ppoint is within diameter(P) of K.
This removes outermost chains / outside halfplanes. Adjacent-chain average
heights and fixed Qdiameter bounds give the coarse uniform band width
10DQ+2DP. None of these arguments assumes the cores are horizontal graphs.
All complement components are individually invariant bands; holes and
translation-permuted regions are not silently discarded.

Whole side anchoring yields finitely many candidate Pplacements per period
slab, with a uniform bound using strip width, tile diameters and Qarea.
Selection/coverage/nonoverlap are finite-window predicates, hence a genuine
one-dimensional SFT. A nonempty bi-infinite completion implies a directed
cycle, providing SOME periodic band filling of uniformly bounded period.
The lcm of all possible bounded periods is common to even infinitely many
bands. Candidate tiles stay inside their band interiors apart from boundaries,
so different replacements cannot overlap. Local finiteness and closure restore
coverage of every boundary point. This proves a legal periodic escape of the
original shapes, not that all original Pfillings are periodic.

## Attempts to break the synthesis and verdict

Checked Qsymmetry index aliases, centralQQ4, w=u/v, x/y numerical aliases,
species loss, native corner coalescence, band permutations, outside halfplanes,
infinite chain density, PPpartial contact in the original field and independent
strip periods. Each is covered by an explicit final proof step. The old distinct
core scope is used only AFTER newly proved equal-private halfturn uniqueness;
its geometry extends under exactly that stated hypothesis.

No numerical search, enlarged bounded domain or new solver certificate was
needed for this analytic audit. Exactly-two-private slots and u!=v remain
essential. SymmetricP, zero/one-privateQ and other angle palettes are outside
this reviewed theorem. No mathematical defect or quantifier weakening remains.
