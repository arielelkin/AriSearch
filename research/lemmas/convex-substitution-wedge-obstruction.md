# Local wedge obstruction for homothetic dissections

**Status:** proved internally (convex-substitution route, 2026-10-11); not
independently reviewed. A finite-dissection statement; it says nothing about
plane tilings.

## Setting

All angles of the shapes A, B are multiples of pi/N and all sides lie in the 2N
directions after rotation (N = 4, 5, 6 in the code). The complete
corner-filling search of [`convex-substitution-core.py`](../searches/convex-substitution-core.py)
(`Dissector`) branches, at a tracked point whose uncovered sector is a run of
m < N basic sectors starting at direction a, over every copy of A or B having a
corner there with outgoing side direction a and angle <= m. That this is
exhaustive, and that any choice rule over such points is allowed, is argued in
the [search record](../searches/convex-substitution-search.md#tools-all-exact).

## Statement

Let W be the wedge of angle alpha (units pi/N) at the origin c, realised in the
code as a parallelogram with legs 4000 (`wedge_test`). Run the search with
unlimited child counts, always choosing the admissible point nearest c. Suppose
the search tree is finite and contains no leaf at which the nearest admissible
point is farther than 60 from c (status `dead`), and let maxd be the largest
distance from c of a vertex of an accepted child. Put
R* = maxd + max(diam A, diam B).

Then no convex polygon P with a corner c of angle alpha, whose corner region
satisfies P ∩ D(c, R*) = W ∩ D(c, R*), can be partitioned into copies of A, B
(any finite counts).

In particular, if h is the distance from the corner c of a shape X to the chord
joining its two neighbouring vertices, then lambda X has no such partition for
every lambda > R*/h: lambda X contains the triangle on c and its neighbours,
which contains W ∩ D(c, lambda h), and lambda X lies inside W.

## Proof

Assume a partition of P exists. Run the search on P with the same choice rule
and follow the branch that agrees with the given partition. As long as all
tracked points and children lie in D(c, R*), the two searches see the same
masks (the parent exterior there is bounded by the same two rays), the same
containment answers (a candidate child anchored within maxd lies in
D(c, R*), where P and W coincide) and the same overlap answers; the counts in P
only remove options. Every branch of the wedge tree stops, inside distance
maxd, at a point with no admissible child. The followed branch therefore stops
too, contradicting that the partition supplies an admissible child there.

Float distances are used only to choose the order of points and to record maxd
and R* (with a 1e-6 margin); every geometric decision is exact in Z[w].

## Controls

Penrose rhombs fill a 36-degree wedge (status `radius`, 46 nodes). For the
Robinson triangles, every angle hit the node limit and none was reported
`dead`. A `node-limit` or `radius` status gives no conclusion.

## Applications

The golden U/V pair: [all-lambda lemma](convex-substitution-golden-uv-all-lambda.md).
The pentagon-pair domains K8/K9 of the search record.
