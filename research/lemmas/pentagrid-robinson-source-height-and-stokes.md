# Five-direction heights and exterior-square Stokes for Robinson source patches

**Status:** adversarially reviewed; the [distinct fresh hostile review](../reviews/pentagrid-robinson-source-height-and-stokes-review.md) is VALID for the analytic source invariant, including exterior completion and residual mate pairing. The fixed finite producer has a
[separate independent audit](../reviews/pentagrid-robinson-height-boundary-review.md).
These necessary conditions exclude neither tested macro shape and do not
supply a triangle assembly or an aperiodic pair.

## Source, lifts, and the exact scope

Let z=exp(pi*i/5), phi=(1+sqrt(5))/2=z+z^(-1), and s=phi^(-1)=phi-1.
Assume an actual locally finite edge-to-edge plane tiling by unit thin and
fat rhombs whose oriented unit edges lie in the ten directions z^k. Cut
thin rhombs along their short diagonal and fat rhombs along their long
diagonal, giving the unit triangles [0,1,z] and [0,1,z^3], up to allowed
source translations, rotations and reflections. No Penrose arrow rule is
used by the following necessity theorem. It therefore applies, in
particular, to the hypothesized actual unit Penrose rhomb source.

Use the free abelian group Z^5 with basis e0,...,e4. Define E_k for every
integer k by E_(k+10)=E_k and E_(k+5)=-E_k, with E_i=e_i for 0<=i<=4.
The physical projection p sends E_k to z^k. Set

    R=e0-e1+e2-e3+e4.

Then p(R)=0, but R is a nonzero element of the free height group. In fact
ker(p)=Z*R. A proof is that the minimal polynomial of z is
x^4-x^3+x^2-x+1: it is Phi_5(-x), and Phi_5(x) is irreducible by applying
Eisenstein at 5 to Phi_5(x+1). Any integral polynomial of degree at most
4 vanishing at z is consequently an integral multiple of this monic
polynomial.

A macro patch below means a finite union of whole source triangles whose
union is the stated convex pentagon and whose outer boundary follows whole
native source triangle edges. A dissection that cuts triangles, or one
with T-junctions that does not come from the specified source, is outside
this hypothesis. Source legality remains stronger than these necessary
conditions.

## Global height map

Orient a rhomb outer edge of physical displacement z^k and give it height
displacement E_k. Every rhomb face has two pairs of opposite sides; its
oriented boundary lift is E_a+E_b-E_a-E_b=0. The edge graph is connected:
a segment between two vertices meets finitely many rhombs, giving an edge
or vertex adjacency path through their finite boundaries.

Every finite closed edge walk decomposes into finitely many simple cycles
and reversed-edge cancellations. A simple cycle encloses a bounded region.
Because the source is an edge-to-edge rhomb cellulation of the whole plane,
its interior is a finite union of source faces. Finiteness follows from
bounded diameter and a positive minimum rhomb area. Summing the oriented
face boundaries cancels internal edges and gives that cycle. Thus every
closed edge walk has zero lift, not merely zero physical projection.

Fix a reference vertex. Summing edge lifts along a path defines a global
map H from source vertices into Z^5, independent of path. It is unique up
to adding a constant height. No injectivity of p, density assertion,
orientation recurrence, or quasiperiodicity is used here. Simply connected
plane coverage and the entire matching native rhomb edges are the relevant
hypotheses; a general abstract graph with physical edge directions alone
would not suffice.

Triangle diagonals introduce no new vertices. Their height displacement is
the difference of the already defined endpoint heights. The canonical
positive length lifts along physical direction z^k are

    unit:     D_u(k)=E_k,
    long:     D_l(k)=E_(k-1)+E_(k+1),
    short:    D_s(k)=E_(k-2)+E_(k+2).                    (1)

Their physical projections are z^k, phi*z^k and s*z^k. To check the actual
source diagonal, the reference thin diagonal z-1=s*z^3 has height
E_1-E_0=D_s(3), while the reference fat diagonal z^3-1=phi*z^4 has height
E_3-E_0=D_l(4). Rotating by a power of z acts by the corresponding signed
basis permutation, and reflection gives the same signed-index formulas.
Alternatively each expression follows by lifting either two-unit-edge
path in the parent rhomb; the rhomb loop makes both paths agree.

For a closed macro boundary the sum of all steps in (1) must therefore be
exactly zero in Z^5. Closure modulo R, although sufficient for physical
closure, is not sufficient for a source cluster.

## Boundary word equation and the fixed U,V fixtures

Use length symbols u=1, l=phi, and s=phi-1. If a side has length a+b*phi,
its positive native edge word has counts

    n_u=a+n_s,  n_l=b-n_s.

For the fixtures below, a,b>=0 and 0<=n_s<=b. Irrationality of phi makes
these equations exact and exhaustive. Every ordering of these counts must
be considered. The word's lift along direction z^k is

    a*E_k+b*D_l(k)+n_s*(-1)^k*R.                       (2)

Indeed D_u(k)+D_s(k)-D_l(k)=(-1)^k*R, as follows directly from the signed
index definition. Its number of native edges is a+b+n_s.

Take the fixed b=c=1 pentagons from the
[reviewed metric family](../searches/pentagrid-golden-metric-area-compatible.md):

    U directions (0,4,6,7,8),
      lengths in (1,phi) coefficients ((1,2),(1,2),(1,0),(1,0),(1,0));
    V directions (0,3,6,7,9),
      lengths ((1,0),(1,3),(1,0),(0,2),(0,2)).

Their vertices are

    U=[0,phi^3,z+z^2+z^3,z^2+z^3,z^3],
    V=[0,1,1+(1+3phi)*z^3,2phi^2*z^3,2phi*z^4].

Sum the n_s=0 terms in (2). For U the result is -R; for V it is 3*R.
Only U sides 0,1 and V sides 1,3,4 can contain short edges. On the U
variable sides (-1)^k=1, and on the V variable sides it is -1. Therefore
necessary exact source closure is

    U: n_s(0)+n_s(1)=1,
    V: n_s(1)+n_s(3)+n_s(4)=3.                         (3)

Summing a+b+n_s gives exactly 10 boundary edges for U and 13 for V.
Each has exactly six unit boundary edges. Its remaining four U edges or
seven V edges are source diagonals. No ordering of a fixed count changes
the total lift, although it can change the exterior-square invariant below.

## Exterior-square Stokes, signs, and the triangle factor

Use the basis e_i wedge e_j for 0<=i<j<=4 of the exterior square of Z^5.
For a counterclockwise closed boundary with successive lifted vertices
H_0,...,H_m=H_0, define

    Q(boundary)=sum_(r=0)^(m-1) H_r wedge H_(r+1).       (4)

This is invariant under adding the same constant to all heights, because
the boundary lift is exactly closed. Summing (4) over every oriented source
triangle in a macro patch cancels every internal oriented edge against its
opposite copy. Only outer boundary terms remain. This is an exact equality
in the free rank-ten exterior-square group.

Translate the height of a triangle's unit-edge apex to zero, and write the
other two heights as A and B, with their order counterclockwise. These are
signed basis vectors E_a and E_b. Its value of (4) is A wedge B. It is
one signed basis wedge, rather than one-half of a wedge.

For i<j the physical signed cross product of p(e_i),p(e_j) is
sin((j-i)*pi/5)>0. The source triangle's counterclockwise physical cross
product is also positive. Thus the sign of its basis wedge must be positive:
every triangle contributes exactly +e_i wedge e_j for a unique pair i<j.
Consequently all ten boundary coefficients q_ij must be nonnegative
integers, and they count the source triangles in the ten unoriented unit
axis pairs. This includes reflected source triangles, since each actual
triangle boundary is oriented counterclockwise in the plane.

Under the physical cross-product functional, (4) equals twice the ordinary
signed polygon area. A unit thin triangle has area sin(pi/5)/2 and hence
contributes sin(pi/5); a unit fat triangle contributes sin(2*pi/5), equal to
phi*sin(pi/5). A whole unit rhomb contributes two identical basis wedges,
in accord with its two triangles. There is no rhomb-to-triangle factor
missing from (4).

The thin coefficients are precisely the pairs with j-i in {1,4}; the fat
coefficients have j-i in {2,3}. The verified fixture areas satisfy

    2*area(U)/sin(pi/5)=7+9*phi,
    2*area(V)/sin(pi/5)=9+16*phi.

Applying the physical functional to (4) and using irrationality of phi
forces respectively

    sum(thin q_ij)=7, sum(fat q_ij)=9;
    sum(thin q_ij)=9, sum(fat q_ij)=16.                 (5)

These sums follow even for integer closed lifts with some negative q_ij;
nonnegativity is the stronger source-cluster condition. No arrow or
whole-plane extension follows merely from nonnegative coefficients.

If the macro is moved by a rotation in the source direction group, its
height basis is signed-permuted. The induced action permutes positive
wedges. A reflection reverses physical orientation as well, so putting
its boundary back into counterclockwise order again permutes positive
wedges. Thus this necessity test does not discard allowed reflected macros
or depend on an artificial source frame.

## An additional paired-diagonal necessity

For each i<j let b_ij count the macro boundary diagonal edges whose source
triangle has wedge e_i wedge e_j. The diagonal type is determined uniquely
by its symbol and direction in (1). A source rhomb contributes two triangles
of that same wedge pair. It can supply zero, one, or two triangles to the
macro. Exactly in the one-triangle case its internal source diagonal is
on the macro boundary. Hence

    q_ij=2*r_ij+b_ij, with r_ij a nonnegative integer.   (6)

In particular q_ij>=b_ij and q_ij is congruent to b_ij modulo 2. This
necessary pairing condition is stronger than nonnegative wedge coefficients.
It is not included in the finite stage counts reported next.

There is also a unique geometric completion that is a necessary source test.
For a counterclockwise boundary step from x to x+D, the interior triangle's
unit apex is

    a=x+z^(k+2) when D=s*z^k;
    a=x+z^(k+1) when D=phi*z^k.

It is the unique unit-distance point from both endpoints on the left of the
step. Its mate's apex is x+D-a+x, the half-turn image about the diagonal
midpoint. Thus its full source parent rhomb has the counterclockwise
vertices [x, 2*x+D-a, x+D, a]. The mate lies on the exterior side of the
macro supporting line. Every actual source realization must contain this
full rhomb, including its exterior half.

Different native boundary diagonal edges belong to different source parent
rhombs: one rhomb has just one prescribed cut diagonal, and a convex simple
macro boundary cannot list the same diagonal twice. The completed parent
rhombs must therefore be pairwise interior-disjoint, and any positive
contact between them must be a full native unit edge on each. Testing their
outside halves is necessary even though those halves are not macro children.

After removing the four U or seven V forced boundary half-triangles, every
remaining source triangle has its mate inside the macro. Otherwise that
triangle's whole diagonal would be an additional macro boundary diagonal,
already accounted for. Hence the residual is exactly six whole source
rhombs for U, or nine for V, with pair counts r_ij=(q_ij-b_ij)/2 from (6).
This is a fixed natural source assembly obligation. No containment,
intersection, completion-screen count, or existence claim for these rhombs
is inferred from the analytic proof; those are separate geometry checks.

## Complete fixed boundary screen and non-consequences

The [producer](../searches/pentagrid-robinson-height-boundary.py) enumerates
all positive ordered native-edge words on the five fixture sides. There
are 625 U boundaries and 21,801 V boundaries. It then tests exact lift
closure, the previously established open native-corner fan conditions,
and nonnegative exterior-square coefficients. The independent checker
imports no producer, enumerates words by Cartesian symbol powers, recognizes
fans by Boolean dynamic programming, and reconstructs all lifted vertex
shoelaces.

| Fixture | All words | Zero height | Zero height and fans | Zero height and nonnegative Q | All three |
| --- | ---: | ---: | ---: | ---: | ---: |
| U | 625 | 72 | 42 | 36 | 30 |
| V | 21,801 | 2,483 | 2,315 | 311 | 311 |

The surviving U boundaries have 30 distinct wedge vectors; V has 221.
Every closed lift has B=10 for U or B=13 for V. With the respective forced
triangle counts 16 and 25, an actual triangulated disk would have 4 or 7
interior vertices by F=2I+B-2. These are necessary counts, not placements.
The screen excludes neither fixture. Passing a word, a fan, a height loop,
or a nonnegative wedge vector does not prove a source cluster, a rhomb
pairing, Penrose arrow legality, a plane recomposition, or shape-only forcing.

The [retained certificate](../certificates/pentagrid-robinson-height-boundary.json)
and the [fresh finite audit](../reviews/pentagrid-robinson-height-boundary-review.md)
record this scoped non-exclusion. No bounded search result is upgraded to
an infinite existence or aperiodicity claim. The original unrestricted
two-convex-polygon problem remains unresolved.

```text
conda run --no-capture-output -n arisearch python research/searches/pentagrid-robinson-height-boundary.py
conda run --no-capture-output -n arisearch python research/reviews/verify_pentagrid_robinson_height_boundary_independent.py
```
