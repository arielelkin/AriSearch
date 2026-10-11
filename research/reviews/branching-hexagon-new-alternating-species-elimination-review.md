# Hostile review: both branches of alternating-species elimination

**Reviewer:** partial_contacts, independently assigned by root. The reviewer
neither authored nor repaired this proof. Read the complete author artifact,
the unrestricted defect-free hexagon limit, and the separately reviewed
uniform compactness proof. No author producer was imported or executed.
This is a proof-only result; no numerical fixture or computation is needed.

**Artifact:** [alternating species elimination](../lemmas/branching-hexagon-new-alternating-species-elimination.md).
**Verdict:** **VALID for both actual revised branches**, with the named monohedral hexagon classification an
explicit imported dependency only for the final periodic escape. The new
A-elimination and existence of a B-only tiling are proved directly from the
reviewed compactness and defect-free-limit reductions.

## Native length words and scope

A has native word(p,q,p,q,p,q), with arbitrary fixed strictly convex angles.
B has exactly two p sides, three q sides and one r side, r adjacent to p and
q, with no pp corner. The two cyclic words(r,p,q,q,p,q) and(r,p,q,p,q,q)
indeed exhaust those constraints up to reversal and cyclic rotation. Their
corner inventory is rp once,rq once,pq three times,qq once. Distinct p,q,r
is essential and is retained throughout the proof. All physical reflections
and original partial contacts are allowed. The conclusion is existence of
an admitted B-only tiling, hence a periodic escape, not absence of A from
every original tiling or an unrestricted classification of pairs.

## Exhaustive trivalent native-star audit

After the separately reviewed defect-free limit, all contacts are full
native sides and every vertex has three sectors. The unique r side can
only meet another B r side. Its endpoint-preserving reflected mate gives
two rp corners at its p endpoint and forces a pp third corner, absent.
The half-turn mate instead gives one rp and one rq corner at each endpoint,
with pq third sector. There can be no further r ray: three sectors have
at most three r halfedges, while every ray requires two, and no rr corner
exists. Thus every r vertex is precisely rp,rq,pq.

At a non-r vertex every corner is pq or qq. Its number of p halfedges is
even, at most three, and there is no pp corner. Exactly zero or two sectors
are pq. Thus the only remaining stars are pq,pq,qq and qq,qq,qq. This
native-ray argument does not assume any angle equation, chirality or
unproved local extension. Species omission is also covered: the A-only
trivalent tiling is locally impossible by the odd all-pq three-ray cycle;
B-only limits are admitted and already give the first conclusion.

## Counts and uniform boundary control

Every B contributes exactly two r-adjacent corners, while every r vertex
contains two. Every A contributes six pq corners, every B three, while r
vertices consume one and X stars consume two. Every B contributes one qq
corner, while X consumes one and Y consumes three. Hence, with errors
bounded in absolute value by a common boundary constant times R,

    J=NB+O(R),
    J+2X=6NA+3NB+O(R),
    X+3Y=NB+O(R).

Their algebra gives X=3NA+NB+O(R), hence NA+Y=O(R). Nonnegative counts
give NA<=C R; an unspecified signed O(R) is never used as a positive
quantity without this absolute bound.

I attacked vertices or tile centers on the window boundary, very small
angles, and changing species frequencies. The proof's fixed positive
minimum tile area and fixed diameter bound settle all of them. A tile whose
center and counted corner lie on opposite sides of the square boundary
meets the D strip, and its whole polygon lies in the2D strip. Disjoint
interiors bound those tiles by strip area/minimum tile area, O(R) uniformly
in the translated square center. Each has at most six corners; every
incidence mismatch belongs to such a tile. Tile area and diameters are
fixed, so acute angles do not destroy this estimate. Omitted species need
no special density assumption. Enlarging the counted square by D gives
the same linear bound for A tiles meeting the original square or a disk.

This is a stronger boundary-uniform statement than merely a limiting zero
frequency; no existence or irrationality of species frequencies is invoked.

## Sparse disks and an actual B-only plane tiling

Given n, only O(R) A tiles meet QR. Their centers exclude at most
O((n+D)^2 R) area by disks of radius n+D. For R sufficiently larger than
(n+D)^2 an inner square retains a point outside that union and at least
n+D from the window boundary. Any A tile meeting the radius-n disk there
would meet QR and would have its center in the excluded union. Thus the
disk is genuinely A-free, not merely low-density. Both interior coverage
and original admitted contacts remain those of the source tiling.

The referenced unrestricted compactness proof parametrizes occurrences by
type, an interior anchor and O(2), with uniformly separated anchors because
each tile contains a common positive-radius anchor disk. It allows continuous
orientations, all reflections and arbitrary partial contacts. Its finite
prefix diagonal convergence prevents anchor merging, preserves interior
disjointness, and preserves coverage using the finite bound on tiles near
each point. Growing A-free disks force every limiting occurrence to be B.
Therefore this is a complete admitted B-only plane tiling. No periodic
finite patch or local-to-global extension is inferred.

## Fresh added binary-length branch audit

The author added a separate theorem after the initial audit. I read its
actual revised statement and complete proof afresh from disk. B now has
only lengths p,q, and h counts homogeneous pp or qq native corners. This
is a separate family, so the original distinct private-r assumption is not
carried into it. A still has six mixed pq corners and no homogeneous corner.

At a three-sector vertex of binary-length rays, an all-mixed corner cycle
is impossible: three rays cannot alternate distinct p and q cyclically.
Thus every vertex consumes at least one homogeneous native B corner. The
same fixed-area boundary estimate gives exact corner totals up to O(R),

    3V=6(NA+NB)+O(R),  V<=h NB+O(R),

hence 2NA+(2-h)NB<=C R for a uniform absolute error bound. The inequality
permits vertices with more than one homogeneous corner; it uses only a
lower budget, so none is overlooked.

For h=0 the total tile count would be O(R), contradicting coverage of the
inner square, whose quadratic area requires at least its area divided by
the maximum tile area many tiles centered in the outer square. For h=2,
NA=O(R), and the fully checked sparse-disk/compactness passage supplies a
B-only admitted tiling. Both species omission possibilities are included.
Cyclic binary transitions have even number, so h=0,2,4,6 exhausts the six
native positions. The theorem excludes exactly h=0 and h=2 and does not
silently extend its budget to h=4 or h=6. Reflection reverses the word but
preserves h and every incidence count. Arbitrary angles and original
partial contacts are handled by the same imported defect-free limit.

This actual added branch receives a separate fresh **VALID** verdict. No
substantive defect or repair was found.

## Classification dependency checked

The last implication uses Zhu, Wang and Yan,
[Hexagonal Tiling of the Plane, v2](https://arxiv.org/html/2508.01404v2),
Main Theorem. I checked its primary statement and the accompanying convex
specialization: it classifies congruent straight-edge hexagon tilings
without requiring edge-to-edge contacts, under a vertex condition that
convexity supplies. Its three Reinhardt types and their recorded periodic
constructions justify the periodic escape. This review treats that theorem
as imported and does not claim to reprove its classification. The proof up
to a B-only admitted tiling has no such external dependency.

## Verdict limits

All native-star cases and boundary incidences are accounted for, and the
compactness passage is supported by its separately reviewed explicit proof.
The private-r two words and the added binary h=0,2 words are eliminated
for every fixed genuine convex metric and arbitrary angles of A, with
original reflections, partial contacts and species omission. The result
does not cover the four-q private-r B family by this count, binary h=4,6
words, or arbitrary pairs. Equal p=q remains excluded.
No substantive defect or repair was required. **VALID.**
