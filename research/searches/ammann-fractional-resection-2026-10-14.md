# Ammann fractional edge-fan transfer: exact global cover, immediate omission obstruction

Date: 2026-10-14. Status: **independently hostile-reviewed VALID** ([review and separate complex-coordinate checker](../reviews/ammann-fractional-resection-2026-10-14-independent-hostile-review.md)).
This records one changed surgery and its failure, not an aperiodic pair.
No contact-class catalogue or source-patch enumeration was run.

## Predeclared domain and two boundary words

Fix the reviewed generic Ammann source at
`J=1/2+(4/5)zeta`, `zeta=exp(i*pi/5)`. Use the canonical marked thin/thick
rhomb partition of [the reviewed reconstruction](../lemmas/ammann-forcing-aperiodicity.md),
Lemma 5. Its full-plane existence is supplied by that lemma and Lemma 7,
not by a finite fixture. Write thin vertices `(A,B,C,D)=(0,1,1+zeta,zeta)`
and thick vertices `(E,F,G,H)=(0,1,1+zeta^2,zeta^2)`.

The source neighborhood domain is every actual pair of marked rhombs sharing
a full edge. In a finite contact model these are contained in the domain of
two rhomb types, ten rotations of the partner, four native edges of each,
and translations determined by identifying the two edge endpoints. Equal
mark type/direction and opposite interior sides are required. This finite
domain is declared for scope only: **it was not enumerated**, since the
geometric obstruction below applies even without matching restrictions.

Put `o_R` at the diagonal intersection of every rhomb `R`. Cut `R` along
the four segments from `o_R` to its vertices. For each shared edge
`e=[u,v]`, glue the two fan triangles with base `e`; these triangles belong
to different rhombs. Orient `u->v` by the native arrow, and name the centers
on the right/left `o_-/o_+`. The two proposed output boundary words are

    A_X(e) = (u, o_-, v, o_+)  for an X edge,
    B_Y(e) = (u, o_-, v, o_+)  for a Y edge.

These are boundary-word templates over the explicitly specified contact
domain, not an assertion that each template gives one congruence class.
For example, the exact thin/thin X contact with left edge A->B and right
edge C->B gives `(0,(1+zeta^(-1))/2,1,(1+zeta)/2)`.
The thick/thick Y contact, left edge F->G and right edge H->G, similarly
gives `(0,(1-zeta^2)/2,1,(1-zeta^(-2))/2)` after normalizing its native arrow
to `0->1`. These reference words are specified before any computation.

This genuinely changes H/D face incidence: every thin or thick reconstructed
rhomb is split into four sectors, and the final faces are indexed by rhomb
edges, rather than by original H or c-paired P1/P2 faces. Old macro face
identities and their cyclic incidences are not retained. Consequently the
reviewed incidence-preserving H/D theorem does not exclude this rule by its
hypotheses. The rule is instead excluded directly below.

## Fractional conservation and global compatibility

Each fan triangle has exactly one quarter of its rhomb's area. An output
therefore receives one quarter of each of its two incident rhombs; its
content is not an equal whole H/P1/P2 triad. Every fan triangle belongs to
exactly one edge, and every edge to exactly two incident rhombs. Thus the
new polygons have disjoint interiors and cover the entire plane. This is
an actual global partition of the already established infinite rhomb
tiling. There is no compatibility or extension assumption beyond the
reviewed rhomb partition.

Let `h(R),T(R)` be thin/thick anchor counts in a square of side R.
Each rhomb has two X and two Y edges, and each edge is counted from two
rhombs. Bounded displacement gives

    n_X(R)=h(R)+T(R)+O(R),
    n_Y(R)=h(R)+T(R)+O(R).

Total new area is exactly the old rhomb area, or
`h(R)*sin(pi/5)+T(R)*sin(2*pi/5)+O(R)` in a large window.
The source ratio `T/h -> phi` is compatible with these equal mark-category
counts. Thus the equal-whole-triad mismatch `(1,phi,phi)` has actually been
removed for this partition. Equal category counts do not prove a two-shape
collapse.

## Exact convexity and cheap failure

Normalize any common arrow to `u=0,v=1`. A rhomb center on either side has
coordinates `(x, +/-h)` where

    x=(1 +/- cos(theta))/2, h=sin(theta)/2,
    theta in {pi/5,2*pi/5}.

In particular `0<x<1` and `h>0`. Write the right center `(x_r,-h_r)` and
left center `(x_l,h_l)`. The four successive signed turns of the output
word, starting at 0, are

    x_l*h_r+x_r*h_l,
    h_r,
    (1-x_r)*h_l+(1-x_l)*h_r,
    h_l.

They are all strictly positive. The two fan triangles are on opposite
sides of their common base, so their union is a simple strict convex
quadrilateral with exactly these four vertices. Its area is
`(h_r+h_l)/2`, the sum of the fan areas. All these statements hold for the
larger domain of every two unit thin/thick rhombs with opposite sides of
the same edge, so no atlas search is needed.

Every convex quadrilateral tiles periodically alone; see the elementary
[side-count/omission argument](../lemmas/side-count-and-monohedral-obstructions.md).
Therefore retaining **any** output congruence class as a final prototile
already admits a periodic omission tiling. This conclusion holds whether
the proposed X/Y categories collapse to two classes or produce more.
No detailed contact-class enumeration is justified. No >=5-side repair
with an explicit compatible boundary rule was available, and none was
executed.

## Decoder and forcing remain separate

On the constructed partition, remembering each quadrilateral's common
base and its two parent fan triangles recovers the chosen rhomb tiling.
Those are auxiliary construction data. No intrinsic decoder from the
unmarked output polygons was proved. In particular a decoder defined on
all admitted output tilings and equivariant under translations could not
reconstruct only the reviewed aperiodic source, because periodic omission
tilings are admitted. Existence of this exact global cover supplies no
unrestricted aperiodicity.

The exact checker verifies the center-coordinate inequalities, four turn
formulas, quarter-area conservation, the X/Y incidence count matrix, and
the two reference words. Its 16 geometry rows are a proof check over the
four possible centers on each side, not a new marked-contact census.
It writes a small certificate under the same prefix.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/ammann-fractional-resection-2026-10-14.py --check research/certificates/ammann-fractional-resection-2026-10-14.json

Scope: only the stated center fan transfer. It excludes no asymmetric
branching surgery, no pentagon/heptagon compiler, and no arbitrary convex
pair. No new literature or novelty claim is made.
