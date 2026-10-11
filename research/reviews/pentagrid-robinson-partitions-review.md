# Fresh hostile review of the Robinson repartition attempt

**Verdict: valid within its stated scope.** The two retained assemblies
are exact geometric partitions. Their failure as the selected edge-to-edge
source compiler is certified. The complete finite boundary tests, including
the added disk Euler filter, pass for both shapes and do not reject other
compilers or establish any global repartition.

This reviewer did not develop the [partition producer](../searches/pentagrid-golden-metric-robinson-partitions.py),
[boundary producer](../searches/pentagrid-golden-metric-robinson-boundary.py),
or [search record](../searches/pentagrid-golden-metric-robinson-partitions.md).
The independent checker is
[verify_pentagrid_robinson_partitions_independent.py](verify_pentagrid_robinson_partitions_independent.py).
It imports neither author module. Geometry is checked in the exact chosen
cyclotomic embedding, using real support inequalities and separating axes;
the complete contact list is reconstructed. Boundary fan counts use a
weighted transfer recurrence, and ordered words use fixed-length Cartesian
products rather than the producer's recursion.

## Partition geometry and source rejection

The checker reconstructs both parent vertex lists and checks their strict
supporting-side inequalities. Every retained triangle is checked against
its exact unit thin or fat reference via the retained orthogonal map and
translation, permitting reflection. Thus the assemblies have exactly
7 thin and9 fat triangles in U, and9 thin and16 fat triangles in V.
All child vertices lie in all five parent supporting half-planes. All
120 and300 unordered triangle pairs have disjoint interiors, and the exact
child-area sum equals the respective parent area.

These conditions prove coverage, including the parent's boundary. A missing
interior point of the finite closed union would give positive missing area.
An omitted boundary point would likewise have a neighborhood containing
parent interior points of positive area. Hence the geometric partitions
are valid without an unproved patch-extension step.

The checker derives every positive collinear triangle contact, including
exact overlap endpoints and whether both native edges coincide entirely.
Its list matches the retained certificate: U has20 positive contacts,
of which4 are partial; V has36, of which15 are partial. These counts
demonstrate that the retained triangles are not edge-to-edge patches.
There is no contradiction with their validity as partitions under
unrestricted partial contacts.

The hypothesis tested by the compiler is an actual edge-to-edge tiling
by unit Penrose rhombs cut along the specified thin-short/fat-long
diagonals. Such a cut preserves whole rhomb outer edges and has whole
triangle-to-triangle contacts. The retained partial triangle contacts
therefore reject that source use even before any arrow legality or recovery
from unmarked pentagons is considered.

The short V rejection has the claimed wider scope over refinements of the
**specified** macro pieces. The chosen medial cap has genuine macro corner
M=phi^2*z^3. In any finite refinement by nondegenerate contained triangles,
at least one child contains that corner. It cannot contain it only in a
straight edge interior, since the edge would continue beyond one of the
two supporting rays of the genuine macro corner. Thus M remains a native
source triangle vertex.

The chosen unit rhomb row has the whole edge [2*z^3,3*z^3]. The exact
coefficient comparison verifies2<phi^2<3, so M lies strictly inside it.
The checker verifies the actual cap triangles5,6,10,11 containing M and
row triangle16 carrying that edge.

That row edge cannot be subdivided into permitted whole native source
edges. If nonnegative counts of unit, long, and short lengths sum to1,
then

    n_u+n_l*phi+n_s*(phi-1)=1

forces n_l+n_s=0 and n_u-n_s=1 by rational independence of1,phi.
Consequently it is a single unit edge. M therefore remains a native corner
in another whole edge's relative interior. This contradicts the required
edge-to-edge source geometry. Allowing Penrose arrow labels cannot alter
that contradiction.

The macro interfaces are essential to this rejection. It neither proves
uniqueness of phi-fat triangle subdivisions nor excludes other unit source
partitions of V. Changing cap or row geometry, allowing clusters to cross
their macro interfaces, or changing source scales is outside its scope.
It does not establish that the U/V pentagons tile the plane.

## Necessary boundary test and the disk Euler addition

The boundary-length enumeration is exhaustive for the tested unit triangle
scales. A native source edge lying on a convex parent's supporting line
cannot extend beyond a genuine parent corner while its triangle remains
inside the parent. Hence each parent side is a concatenation of whole
source edges. For a length a+b*phi, coefficient comparison gives

    n_l+n_s=b,   n_u-n_s=a.

All nonnegative choices are covered by n_s=0,...,b. The checker obtains the
same ordered words independently, including every permutation. The
successive side-word counts are25,25,1,1,1 for U and1,129,1,13,13 for V.

At a boundary vertex an edge-to-edge triangle patch supplies a fan of
native sectors. The four typed corner transitions are exactly thin36
u-u, thin72 u-s, fat108 u-u, and fat36 u-l, with weights1,2,3,1 in
pi/5 units. Reversing each nonloop transition covers reflected corners.
Positive weights bound every fan length by its angle budget. The transfer
recurrence independently checks all45 endpoint/budget fan counts, including
all nine flat weight5 endpoint pairs. These are necessary local constraints,
without a triangle placement or source-arrow sufficiency assertion.

Among all625 and21801 ordered boundary choices, respectively299 and18576
pass the local fan gate. The original first witnesses have B=9 and10
outer native edges. They are valid local witnesses with corner demand
within the available counts, but fail the Euler parity for an actual
triangular disk. The revised artifact correctly retains them with this
limitation recorded.

For an edge-to-edge triangular disk, let F be the face count, I the interior
vertex count, and B the number of outer native edges. Counting edge
incidences and applying disk Euler gives

    3F=2E_internal+B,  E_internal=I+F-1,
    F=2I+B-2.

The unit triangle face counts are fixed to F=16 and25 by the exact parent
areas and rational independence of the thin/fat area ratio phi. Thus
F-B must be even and I=(F-B+2)/2 nonnegative. The independent replay leaves
150 U boundary choices and9288 V choices after this additional filter.

The revised explicit witnesses have B=10 for U and11 for V, requiring
I=4 and8. The checker verifies every retained fan transition, its full
angle budget and terminal symbols, total native corner demand, and available
corner counts for those witnesses. They pass both necessary tests. This
does not supply actual triangle placement, a marked Penrose cluster,
global repartition, recognizability, or shape-only forcing.

The content matrix [[7,9],[9,16]] also has the stated determinant31,
commutes with [[1,1],[1,2]], and has eigenvector (1,phi) with eigenvalue
7+9phi. These are compatible arithmetic identities, not a substitute for
the missing legal geometry.

## Replay and conclusion

```text
conda run --no-capture-output -n arisearch python research/reviews/verify_pentagrid_robinson_partitions_independent.py
```

The independent checker passed the exact partitions, all420 triangle-pair
tests, the complete contact records, the midpoint witness, the full
boundary-word/fan tables, the Euler-filtered counts, and both corrected
witnesses. It uses no author imports, numerical decisions, solver,
stochastic seed, geometric cutoff, or bounded period search. The result
is a falsified concrete source compiler with valid geometric assemblies;
the broader unmarked U/V construction remains unresolved.
