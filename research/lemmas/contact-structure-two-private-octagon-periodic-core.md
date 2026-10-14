# Two distinct private octagon slots force a common periodic Q core

Date: 2026-10-13. Status: independently reviewed VALID for the Q scaffold; [core review](../reviews/contact-structure-two-private-octagon-core-hostile-review.md).
This is a periodic-subtiling theorem. Completing the remaining P regions
periodically is a separate obligation, not asserted here.

## Statement

Let P,Q satisfy the reviewed
[unrestricted native reduction](contact-right-angle-unrestricted-native-reduction.md):
P has one90corner and four112.5corners; Q has eight135corners. Let u,v be
P acute-adjacent lengths and suppose u!=v. Suppose Q has exactly two native
side slots i,j whose lengths occur nowhere among P native side lengths, and
these two private lengths are distinct.

In any admitted plane tiling, the union of all Q tiles is invariant under a
common nonzero translation v0. More precisely write mi,mj for the midpoints
of those two native Q sides. Every Q-Q adjacency component is a two-sided
infinite chain; its set of tiles is invariant under a translation of length

    ell=2*|mi-mj|>0.

All these chain translation vectors are parallel. Choosing either sign of
one such vector v0 makes v0 a period of every chain and hence of their union.
This statement permits every initially unrestricted partial contact. The
whole tiling need not itself have period v0: P completion is not proved here.

## Unique matching and halfturn transport

The native reduction forces every private Q slot to have a Q neighbor and
permits at most two Q-neighbor slots. Thus the Q-Q degree is exactly two,
with its neighbor mask exactly {i,j}. Each private length occurs on only one
Q native side: if it occurred in another slot that slot would also be private,
contradicting exactly two private slots with distinct lengths.

A Q-Q contact consequently identifies the same indexed native side on both
copies. Relative to one copy there are only two placements on the opposite
side of that segment: reflection across its supporting line (endpoints fixed),
or halfturn about its midpoint (endpoints reversed). The other two rigid
endpoint maps place interiors on the same side and are impossible.
At a QQ endpoint the third sector is P90. If the neighbor were the reflected
copy, the two outgoing QP sides at that endpoint would have equal lengths.
They are whole contacts by the native reduction, so P would have equal acute
legs, contradicting u!=v. Thus every QQ neighbor is the halfturned copy.
This argument concerns actual polygon sets and does not impose markings.
Native indexing only records the unique private lengths.

Let Hi(x)=2mi-x and Hj(x)=2mj-x. Starting with indexed placement gQ, cross
side i to obtain gHiQ, then cross the other private side j to obtain

    gHiHjQ = g(Q+2(mi-mj)).

Repeating two steps gives translation by w=R_g[2(mi-mj)], where R_g is g
orthogonal part. Midpoints of distinct genuine sides cannot coincide, so
w!=0. Traversing backwards gives the inverse translation.

There is no finite QQ component. The recursively transported placements
satisfy Q_(n+2)=Q_n+w for every integer n: at an odd starting step both the
native product order and the orthogonal part change signs, leaving the same
world vector w. If a graph cycle had length k, the nonbacktracking traversal
would give Q_(n+2k)=Q_n, but the recurrence gives Q_n+k*w, impossible for a
compact polygon and w!=0. This argument excludes even and odd cycles without
any polygon-symmetry premise. Hence every component is an infinite chain and
is periodic by w, with |w|=ell.

## Embedded periodic cores and parallelism

Distinct Q tiles not QQ-adjacent cannot even touch. A point contact would
have two135corner sectors; the only allowed star containing them is
P90+Q135+Q135, whose two Q sectors share a positive boundary ray and hence
a whole QQ side. A Q corner cannot lie in a side interior. Thus nonadjacent
Q tiles have disjoint boundaries as well as interiors.

Choose the centroid in every Q tile and join it to the midpoints of its two
QQ sides. The resulting component core is a simple, proper two-sided
polygonal curve. The pieces lie inside tile interiors except at their common
seam midpoints; pieces in one tile intersect only at its centroid. The two
private sides are distinct and have disjoint endpoints by the reviewed native
mask spacing, so no degenerate junction occurs. Nonneighbor contact exclusion
prevents selfintersection, and different chain cores are disjoint.

Each core is invariant under its two-step translation w and consists of a
fixed finite motif translated by integer multiples of w. It therefore lies
within bounded distance of a straight line parallel to w and has two ends
approaching the two opposite directions of that line. Properness follows
from w!=0 and the finite motif. This also supplies a uniform width bound
depending only on Q.

An elementary proper-arc separation consequence of the Jordan curve theorem
says that two disjoint such curves cannot have nonparallel asymptotic lines.
For clarity, a proper simple curve lying in a fixed-width neighborhood of a
line and running to opposite ends separates the plane; the far halfplanes
on the two sides of that line belong to opposite components. This follows
by closing a sufficiently long central subarc outside a sufficiently large
rectangle and applying Jordan separation, or by the one-point compactification
of the proper arc. A second curve whose asymptotic line is nonparallel has
one end in each of those far halfplanes and must intersect the first.
The intersection would lie in the interiors of their disjoint Q-chain unions,
which is impossible. Hence all chain vectors are parallel.

Their lengths are all ell, so each equals v0 or -v0. Either choice is a
period of each chain tile set. Taking their union proves the theorem.

## Exact scope and next obligation

No finite-local-complexity assumption, orientation restriction, species
frequency or bounded search is used. The finite transport motif is derived
from two unique private native lengths and the P acute-leg inequality.
The same argument does not apply when private lengths coincide, when there
is at most one private slot, or when u=v: reflected QQ gluings then remain
possible. All other metric coincidences are allowed in the stated theorem.

The separate plane-wide P completion obligation is now completed by the
[complementary-bands theorem](contact-structure-two-private-octagon-complement-bands.md)
and [anchored-strip theorem](periodic-scaffold-anchored-strip-completion.md),
as integrated in the [reviewed all-metric synthesis](contact-right-angle-two-private-all-metric-periodic-escape.md).
This file establishes only the Q core and does not assert that every original
P completion is periodic.
No computation or novelty claim is made.
