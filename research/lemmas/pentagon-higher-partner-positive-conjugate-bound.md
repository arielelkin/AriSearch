# A pentagon with any higher-sided convex partner: a substitution bound

Date: 2026-10-13. Status: Independently adversarially reviewed VALID;
[review](../reviews/pentagon-higher-partner-positive-conjugate-bound-review.md).
This is a finite dissection and ordinary similarity-substitution obstruction.
It is not an impossibility theorem for plane tilings.

## Finite dissection theorem

Let C be a genuine compact convex pentagon with positive area. Suppose C is
partitioned into F>1 compact genuine convex polygons, each having at least
five sides, with pairwise disjoint interiors. Then F>=6. Contacts need not be
edge-to-edge. The children need not have equal side counts or be congruent.

### Proof

Planarize all common boundaries at genuine polygon corners and contact
endpoints, and suppress straight degree-two nodes that are no polygon corner.
The internal seam graph includes boundary endpoints. Write I for interior
nodes, B for nodes on relative interiors of the five outer sides, J for
outer corners incident with a seam, E for seam edges, and H for inserted
straight-angle incidences on child boundaries. If child i has n_i sides,
angle summation, in units of pi, gives

    sum_i(n_i-2)+H = 2I+3+B.                         (1)

Every interior node has seam degree at least three; every active boundary
node has degree at least one. Euler for the disk gives F=E-I+1.
If the nonempty seam graph is a forest with k>=1 components, then

    E=I+B+J-k,  B+J=F+k-1,  I<=B+J-2k.

Since n_i>=5, (1) yields

    3F+H <= 2I+3+B
           <= 3(B+J)-4k-J+3
            = 3F-k-J.

Thus H<=-k-J<0, a contradiction. The seam graph has a simple cycle.
Its bounded side contains a child interior and is separated from the outer
boundary by internal seam edges; the cycle meets the outer boundary at most
in isolated nodes. A child on that bounded side has no positive-length
contact with the outer boundary, so each of its at least five genuine sides
has positive-length contact with another child. Distinct sides require
distinct neighboring children: the intersection of two convex sets with
disjoint interiors is convex with empty interior, so it cannot contain
segments on two different supporting lines. There are at least five
neighbors and the interior child itself, proving F>=6.

Dependencies: planar disk Euler and elementary convex intersection. This
extends the all-pentagon argument in
[pentagrid-golden-metric-small-substitution-obstruction.md](pentagrid-golden-metric-small-substitution-obstruction.md)
to arbitrary children of at least five sides.

## Similarity-substitution theorem

Let exactly two compact genuine convex polygon prototiles A,B of positive
area have respectively five and n>=5 sides. An ordinary geometric
substitution partitions a common similarity image of each prototile into
isometric copies of A and B. Let lambda>1 be the linear similarity factor,
and mu=lambda^2 the area factor. If mu is an irrational real quadratic
number and its algebraic conjugate mu' is positive, then

    mu >= (5+sqrt(13))/2.

The bound is a necessary matrix/dissection condition, not a construction.

### Proof

Write M=[[a,b],[c,d]], with columns counting children of A and B. Its
entries are nonnegative integers. The positive area row vector v obeys
v M=mu v. The characteristic polynomial of M is the minimal polynomial
of mu, so det M=mu mu'>0. Irrationality implies b,c>=1, since triangular
integer matrices have integer eigenvalues. Positive determinant implies
a,d>=1. A zero-child image cannot cover A. A one-child image is impossible:
a single A gives mu=1, and a single B would make column one (0,1),
contradicting det M>0. The finite dissection theorem therefore gives

    a+c>=6,  ad>bc.

The positive area eigenvector implies mu is the Perron root of M. For
positive b,c it is

    mu=(a+d+sqrt((a-d)^2+4bc))/2.

The Perron root is nondecreasing in each nonnegative matrix entry (or use
the positive-eigenvector comparison). If a>=5, mu>a>=5, exceeding the
stated bound. Otherwise four cases exhaust a:

* a=1: c>=5, b>=1, ad>bc gives d>=6; mu>d>=6.
* a=2: c>=4, b>=1 gives d>=3; compare [[2,1],[4,3]],
  whose Perron root is (5+sqrt(17))/2.
* a=3: c>=3, b>=1 gives d>=2; compare [[3,1],[3,2]],
  whose Perron root is (5+sqrt(13))/2.
* a=4: c>=2, b>=1 gives d>=1; compare [[4,1],[2,1]],
  whose Perron root is (5+sqrt(17))/2.

This proves the bound. The integer matrix [[3,1],[3,2]] attains equality
in these necessary algebraic constraints. No convex geometric realization
is supplied, so no geometrically sharp bound is claimed.

## Consequences and limits

Linear inflation phi=(1+sqrt(5))/2 gives area factor (3+sqrt(5))/2,
which is below the bound and has positive conjugate. Thus it cannot define
an ordinary two-species substitution for any pentagon and any convex
n-gon with n>=5. This includes higher-sided partners and arbitrary metrics,
rotations, reflections, and partial seams in the inflated polygons.

For two pentagons, the existing reviewed bound mu>=6 is stronger. An area
factor with nonpositive conjugate, more than two species, nonconvex parents,
or a hierarchy not defined by similarity images of the two native polygons
is outside this theorem. No infinite tiling, intrinsic recognition, omission
exclusion, or aperiodicity conclusion follows. In particular this does not
justify discarding arbitrary pentagon/higher-partner tilings.

## Exact computation and novelty

No computer-assisted proof component or new enumeration is used. The four
matrix cases above form a complete analytic classification for a<=4;
a>=5 is handled analytically. No certificate is needed. A current primary
literature boundary has not yet established novelty of this extension;
no novelty claim is made. Independent review checked the forest argument, cycle separation,
partial seams, and the nonnegative-matrix minimum and found no unresolved defect.
