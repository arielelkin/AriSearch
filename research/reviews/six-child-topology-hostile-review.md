# Fresh hostile review: universal six-child pentagonal wheel

Date: 2026-10-13. Independent reviewer: contact_structure.
Artifact: [universal topology lemma](../lemmas/six-child-topology-universal-wheel.md).
Verdict: VALID with its full universal convex-partition quantifiers.
No computation, congruence or edge-to-edge premise is needed.

## Dependencies and unique central child

The already reviewed finite-dissection cycle theorem supplies a child with
no positive-length parent-boundary contact. It may initially have isolated
outer contacts; the proof does not erase that case. Every native side of
such a child has positive contact with other children, and convex intersection
prevents one other child from contacting two noncollinear sides. With six
children it has exactly five sides and all five other children as neighbors.
The adjacency graph with exterior vertex is planar as the dual of the
polygon partition; contact segments can be chosen away from endpoints,
with arcs through each convex face interior. The exterior arcs can be drawn
in the outside face (equivalently on the sphere with the exterior point).
Three interior children give K3,3 against the remaining three children;
exactly two give K3,3 using those two plus the exterior against three of the
four outer-contact children. Hence there is exactly one central child Z.
No multi-edge or point contact is promoted to a dual edge.

Five different neighbors on the five Z sides force exactly one neighbor
covering each whole central side. A different child touching a central vertex
while already touching a nonincident central side would have a positive-area
convex intersection with Z. Genuine convexity ensures that vertex is off the
nonincident side supporting line. Thus at each interior central vertex only
the two adjacent side neighbors join Z, giving exactly three tile sectors
(possibly a flat sector at this stage). Its exterior-seam degree is one.

## External cycles, paths and boundary coincidences

An exterior seam cycle cannot pass through an interior central vertex, whose
exterior degree is one. A central boundary vertex has no exterior branching
that could add another sector between its two side neighbors: the parent
boundary separates those neighbors. Thus an exterior cycle is separated
from Z. A Jordan curve contained in convex C has its bounded region contained
in C, and no parent boundary point can be strictly inside that region, by a
supporting-line argument. Its seam edges have no positive parent contact.
If the cycle surrounds Z it encloses a positive outer-child region as well;
if not it encloses only outer children. A child interior cannot cross the seam
curve, so some whole outer-child interior is inside, with no positive outer
contact, contradicting uniqueness. Point contact with the parent does not
rescue that child.

For an exterior path between distinct central vertices, choose a simple path
with no central vertex in its interior. It cannot meet a central side in its
interior, since each central side has one whole neighbor. Together with a
central boundary arc it forms a Jordan curve enclosing a nonempty region
outside Z. An exterior path cannot coincide with a central arc, and convexity
precludes an outside zero-area chord. That region is a union of whole
outer-child interiors: all its boundary segments are seams or central edges.
It meets the parent boundary only in finitely many nodes, by the same support
argument. Again an outer child without positive outer contact is forced.
This excludes branches sharing any boundary endpoint, as well as connections
to central vertices initially on the boundary.

The remaining exterior graph is a forest. Each component rooted at an
interior central vertex has a boundary node: otherwise all its other vertices
would have degree at least three while the central root is its only leaf,
which is impossible for a finite tree. Boundary central vertices count as
their own boundary nodes. Distinct roots have distinct boundary nodes, so
B+J>=5 without assuming strict central interior.

## Exact count and final wheel

For the disk partition Euler gives E=I+5. Its validity follows either from
the full cell decomposition or the exterior forest attachment to the central
cycle and parent boundary. The stated seam degree excess is nonnegative and
counts a central boundary touch with degree at least two. The degree sum
therefore gives I+B+J+D=10. The child native-angle sum plus flat incidences
is exactly 2I+3+B. Active boundary nodes cannot support a flat child sector,
which would consume the whole parent aperture and leave no seam sector.
Thus H only counts internal flat incidences, including unrestricted T contacts.
The lower bound on native sides gives B+2J+2D+H<=5.
Together with B+J>=5 this forces B=5,J=D=H=0,I=5 and all six native side
counts equal five. An isolated central boundary contact necessarily occurs
at a central vertex (contact in a central side interior would give a positive
outer segment); its boundary degree at least two would violate D=0. So Z
really is strictly interior.

All five internal nodes are now the central vertices. The other five seams
must be direct edges to the five boundary nodes; no extra forest component
or extra internal bending node can remain. At a central or boundary junction
H=0 forbids a suppressed flat child corner. Each outer child therefore has
three inner native sides plus k+1 outer native sides, where k is the number
of genuine parent corners on its boundary arc. Its five sides force k=1.
The arcs partition the outer boundary; each seam endpoint lies in a parent
side interior, so there is one endpoint on each parent side and no split
parent corner. This proves the exact wheel claimed, including full outer
native side decomposition and absence of partial contacts.

## Scope and counterexample attempts

I attacked isolated boundary touch of Z, shared radial endpoints, loops in
an exterior seam component, tangential central contacts, higher-sided outer
children, outer corners divided between children, and initially flat sectors.
Each is explicitly charged to either the Jordan isolation contradiction or
the nonnegative exact degree/flat-angle budget. Convexity and exactly six
children are essential; none of the arguments is extended to seven children
or nonconvex polygons. A wheel incidence theorem is not an infinite tiling,
recognizability or aperiodicity theorem. No unresolved finding remains.

## Fresh review: substitution and boundary-defect consequences

Reviewed [corollaries](../lemmas/six-child-topology-substitution-consequences.md).
Verdict: VALID, including the stated analytic lower bounds and their scope.
The finite exact-six-every-parent obstruction uses global extrema correctly:
minimum-area parent forces lambda squared at least six, while the globally
longest parent side is exactly two complete child sides by the wheel and
forces lambda at most two. No common prototile area or equal side length is
assumed. The strict Perron bound mu>6 correctly REQUIRES every image
nontrivial; irreducibility alone is expressly insufficient. Positive quadratic
conjugate in the two-species case supplies positive determinant and positive
diagonals/offdiagonals, hence the needed nontriviality. The right Perron
vector is the correct vector for summing column sums.

The general seam-angle identity is exact for arbitrary convex partitions.
At least two active boundary seam nodes follow from connected boundary-label
constancy if there were at most one; one convex child would otherwise contain
all parent boundary and its convex hull, leaving no other child interior.
This uses a global boundary statement, not a false per-component claim.
The forest inequality has the correct -J coefficient; the designated child
contributes at least p-5, exceeding p-6. The resulting cycle yields at least
six children by the already reviewed dissection argument.

For pentagon plus n>=6, positive-conjugate hypotheses really force c,d>=1.
A six-child P image would consist entirely of pentagons, so its first column
has sum at least seven. The Q image includes Q and the forest gate makes
its column sum at least six. The boundary-defect inequalities are
 a-(n-6)c>=3 and b-(n-6)d>=8-n. Their rearranged lower bounds are correct.
I checked every displayed finite matrix comparison, all eigenvalue radicals,
and all complete large-entry regimes. Some comparison matrices may themselves
be inadmissible (for example n7,d1), which is harmless: they remain valid
componentwise lower bounds for the stated class. No admissible parameter
range is discarded as a numerical cutoff. The minimizing legal lower matrices
are [[3,2],[4,4]] for n6, [[5,4],[2,2]] for n7, [[6,4],[1,2]] for n8,
and [[n-3,5],[1,1]] for n>=9. Their Perron roots equal exactly the listed
bounds. The neighboring radical comparisons follow by positive squaring,
including the close n7 comparison 3+sqrt14 > (7+sqrt41)/2 and n8 comparison
(7+sqrt45)/2 > 4+2sqrt2. Determinants of the minimizing matrices are positive.

These are necessary substitution bounds; algebraic attainment is expressly
not a convex geometric realization. No consequence for arbitrary plane
tilability, nonpositive-conjugate substitutions, or a final aperiodic pair
is imported. No unresolved objection remains.
