# A chain limit for the nonadjacent-alpha 108/144 octagon family

**Status:** adversarially reviewed; [fresh hostile review](../reviews/obtuse-pentagon-octagon-chain-review.md) valid. This is a
necessary tiling reduction and does not establish periodicity or aperiodicity.

## Exact scope

Let P be a genuine convex equiangular pentagon, with angle alpha=3pi/5.
Let Q be a genuine convex octagon with exactly two alpha corners and six
beta=4pi/5 corners. Suppose Q's two alpha corners are nonadjacent.
If {P,Q} tiles the plane under the unrestricted problem definition, then
it has an admitted plane tiling with all the following properties:

* Each P has exactly two P side neighbours, in nonadjacent positions, and
  exactly three Q side neighbours.
* Each Q has exactly two Q side neighbours and six P side neighbours.
  Exactly one Q-to-Q side is incident to each alpha corner of Q.
* Every Q-to-Q side has alpha and beta endpoints, matched to beta and alpha
  respectively on the other Q. Every endpoint star is P,Q,Q.
* All other stars are P,P,Q. Each P has exactly one P,Q,Q corner and four
  P,P,Q corners. Each Q has four corners of each star type.
* The P-to-P and Q-to-Q adjacency graphs are both simple2-regular graphs:
  their components are finite cycles or double-infinite paths.

These statements are about a potentially different translated-limit tiling.
An original tiling can have a set of exceptional contacts of linear window
count; average saturation does not exclude those contacts pointwise.
Side lengths and orientations remain arbitrary. No finite-state uniqueness
or translational symmetry is asserted for either family of chains.

## Nonnegative contact deficits

By [all-obtuse forcing](obtuse-edge-forcing.md), every tiling is edge-to-edge
and trivalent, and every star has two alpha sectors and one beta sector.
At a P-corner the two side neighbours cannot both be P, so P has at least
three Q side neighbours. Write d_P for the number of such neighbours minus3.
Then d_P is a nonnegative integer.

At either alpha corner of Q, one of its two side neighbours must contribute
beta and hence have type Q. Since Q's two alpha corners are nonadjacent,
a single side cannot cover both. Thus Q has at least two Q side neighbours,
or at most six P side neighbours. Write d_Q for6 minus its number of P side
neighbours. Again d_Q is a nonnegative integer.

For tile-centre windows W_R, bounded diameter and positive minimum area give
uniformly in translation of the window only O(R) boundary tiles and total
N_P+N_Q=Theta(R^2). Corner counts give

    5N_P+2N_Q = 2*(6N_Q)+O(R),
    N_P=2N_Q+O(R).                                      (1)

Double counting P-to-Q sides gives

    3N_P + sum_P d_P = 6N_Q - sum_Q d_Q + O(R).          (2)

Consequently sum_P d_P+sum_Q d_Q=O(R), uniformly in translated windows.
A bad tile is one with positive deficit. Since a positive deficit is at
least1, bad-tile centres also have O(R) window count. The constants depend
only on the fixed shapes and the uniform boundary-count estimates.

## Extracting a defect-free plane limit

For each L>0 there is a disk of radius L containing no bad-tile centre.
Otherwise every point of a square of side2R would lie within L of a bad
centre in its L-enlargement. The number of relevant centres is O(R+L), and
the union of their radius-L disks has area at most O((R+L)L^2), less than
4R^2 for sufficiently large R. This is a contradiction. Translate such a
disk to the origin and let L tend to infinity.

Finite fixed positive-area shapes, bounded diameter, and compactness of O(2)
give a diagonal local limit of these tilings. A bounded window meets only
uniformly many tiles; their isometries can be jointly converged after
subsequences. The limiting copies cover and have disjoint interiors: an
uncovered open disk or an overlapping open disk would persist under small
perturbations. Tiles meeting a radius-M disk have centres within M+D, so all
are good once L>M+D before the limit.

Full native-side contacts and distinct vertex stars persist as well. Here is
the needed uniform separation justification, rather than an assumption of
combinatorial compactness. Choose r>0 below the minimum, over both reference
polygons and all their native vertices, of distances from that vertex to
other vertices and nonincident sides. At any tiling vertex v, the three
incident corner sectors cover B(v,r), and each corresponding tile inside
that disk coincides with its corner wedge. No other tiling vertex can lie
in B(v,r): on an internal wedge ray a new vertex would subdivide a native
side, excluded by full-edge forcing, and inside a wedge it would enter a
tile interior. Therefore distinct tiling vertices are uniformly separated.
This is the same independently re-reviewed separation argument as the
[hexagon defect-free limit](hexagon-limit-and-periodicity.md).

In a fixed window, extract convergent placements also for each whole-side
neighbour of each selected tile. Shared whole sides stay coincident; their
positive fixed lengths prevent collapse, and uniform vertex separation
prevents distinct stars from merging. Each side already retains its unique
neighbour, and all-obtuse forcing also holds automatically for the admitted
limit tiling. The numbers of P/Q neighbours are therefore preserved. Every
limit tile has deficit0, establishing the first two claimed properties.

## Chain and corner structure in the limit

Each Q has exactly two Q-to-Q sides. Because its two nonadjacent alpha
corners each require such a side, exactly one is incident to each alpha
corner. The other side neighbour at that corner is P. Hence every alpha-Q
star is P,Q,Q, with its Q neighbour contributing beta.

A Q-to-Q side cannot have beta at both ends on one Q: it would then have
alpha at both ends on the other, impossible since Q has no alpha-alpha
side. It cannot have alpha at both ends for the same reason, and beta-beta
endpoint pairing would place two beta sectors at one star. Thus its ends
are alpha-beta on each Q, in opposite correspondence. Every such endpoint
is P,Q,Q. These sides have four distinct endpoints on each Q: if two met at
one beta corner, the star would have Q,Q,Q, with its two alpha-Q sectors each
having two Q side neighbours, contradicting the preceding property.
The other four Q vertices are P,P,Q.

The two P-neighbour positions around each P are nonadjacent. Removing those
two positions from the five-cycle leaves exactly one consecutive pair of
Q-neighbour positions. That corner is P,Q,Q. The other four P corners are
P,P,Q. A Q,Q,Q star is impossible because it would contain two alpha-Q
sectors, each incident to two Q-to-Q sides. These exhaust the permitted stars.

Convex interior-disjoint tiles cannot share two distinct whole native sides:
the convex hull of the two noncollinear side segments would have positive
area in their intersection. No tile neighbours itself. Thus the same-type
adjacency graphs are simple and every vertex has degree2. A connected
locally finite simple graph with all degrees2 is a finite cycle or a
double-infinite path, proving the chain claim.

## Exact remaining obligations

This theorem gives a concrete geometric model for a surviving signature.
The [private-side regular-pentagon theorem](regular-pentagon-private-octagon-periodicity.md)
now establishes a periodic escape when P is regular and Q has six unit sides
and two distinct nonunit sides. Its straight midpoint-chord argument is
independently reviewed. The wider metric family below remains open.
It does not show that any chosen length data have such a tiling, does not
bound cycle lengths, and does not force either chain to be periodic. Local
placement choices can branch. An aperiodic construction would still need
whole-plane existence and proof that all admitted original and limit tilings
exclude periods. An impossibility route needs a new argument producing a
periodic whole-plane assembly from actual chain geometry, not a rational
frequency or local-neighbour count alone.

Adjacent-alpha octagons are outside the saturation bound: their two alpha
corners can be covered by one Q-to-Q side, leaving seven P contacts, so (2)
need not have nonnegative deficit relative to6. No computation is used.
