# Fresh review of the generic metric substitution obstruction

Reviewed 2026-10-10 by an agent who did not develop the generic obstruction,
its boundary eigenvalue argument, or the area-compatible metric family.

**Verdict: valid under its explicit dependencies.** For b,c>0 with
c/b not in K=Q(sqrt5), the stated family admits no finite partition of
lambda U into whole U/V copies for any real lambda>1. The proof needs
no rule for lambda V. The complementary c/b in K arithmetic section,
added after the initial audit, was also freshly reviewed and is valid.
Neither conclusion classifies unrestricted plane tilings.

Reviewed artifact:
[generic metric substitution obstruction](../lemmas/pentagrid-generic-metric-substitution-obstruction.md).
Dependencies are the exact area-family identity and convexity, and the
reviewed U monohedral exclusion conditional on Rao's explicitly imported
classification. The present proof introduces no further external tiling
classification, fixed orientation rule, primitivity, or finite-local-
complexity assumption.

## Whole-child boundary sides, including partial contacts

The outer boundary assertion was attacked first because arbitrary interior
partial contacts are allowed. Let e be a native side of the genuine convex
parent. A child contained in the parent which meets the supporting line
of e in a positive segment has that line as a supporting line as well.
Its intersection with the line is one whole native child side. That side
is entirely inside the parent and hence entirely inside e; it cannot
continue past a genuine parent corner without leaving the parent.

Different children cannot overlap on positive boundary intervals, since
both lie on the same interior side of the parent's supporting line and
would then overlap in a small open region near a generic point of that
interval. The finite collection of child contacts covers e, so its length
is the sum of these entire native child-side lengths. Other children may
insert planarization points along such a side, but adding these points
does not cut away any of its total length from the boundary sum.

This reasoning would fail for concave parents or permitted cuts through
children. Both are absent. It does not assume that any interior seam
matches two whole native sides.

## The coefficient and eigenvalue argument

The family side lengths have coefficient pairs in the basis (b,c):

    U: (phi^2,phi), (phi^2,phi), (1,0), (0,1), (1,0);
    V: (1,0), (2phi,phi^2), (1,0), (phi,phi), (phi,phi).

All coefficients are nonnegative in the actual positive embedding of K.
The pure-b native sides all have length exactly b; the pure-c native sides
all have length exactly c. This special property is needed for integrality.
No claim about coefficient signs in K's other embedding is used.

If lambda U has a finite U/V partition, area conservation gives
lambda^2=a+d*phi in K, with a,d nonnegative integers. The parent's b and
c sides give two independent boundary sums

    lambda*b=A*b+B*c,    lambda*c=C*b+D*c,

with A,B,C,D in K, nonnegative in its actual embedding.

If lambda is in K, independence of b,c over K forces B=0 and A=lambda
in the first equation. A zero c coefficient cannot arise by cancellation:
all individual c coefficients are nonnegative. Therefore only pure-b
child sides occur there, and A is an integer number of b sides. Thus
lambda^2 is an integer.

If lambda is outside K, its square in K gives the irreducible minimal
polynomial t^2-lambda^2 of degree two. The two boundary equations make
lambda an eigenvalue of the two-by-two matrix over K. Its degree-two
monic characteristic polynomial is therefore exactly that minimal
polynomial; it is not merely divisible by a different degree-two factor.
This forces A+D=0 and B*C=lambda^2. Nonnegativity in the actual real
embedding gives A=D=0. Only pure-c sides remain in the first boundary
word, and only pure-b sides in the second. Therefore B,C are positive
integers and lambda^2 is again an integer.

These two cases exhaust every real lambda>1, including values not known
in advance to be algebraic. The area equation itself implies the required
algebraicity. The proof does not restrict lambda to powers of phi.

Writing N=lambda^2, rational independence of 1 and phi in the area equation
forces a=N and d=0. Thus the supposed lambda U rule is a monohedral
dissection into exactly N U copies. N>1 follows from lambda>1. No V rule
is used in this contradiction. If present, the lambda V rule would likewise
be monohedral, by the same area-basis calculation.

## Iterating the monohedral rule and obtaining the whole plane

A finite dissection of lambda U into unit-size isometric U copies can be
iterated exactly. Scale the previous patch by lambda; each resulting
lambda U copy receives the appropriately rotated, reflected, and translated
first-level dissection. This produces a finite tiling of lambda^r U by
unscaled copies of U. Scaling commutes with the orthogonal part of each
isometry, so arbitrary reflections cause no compatibility defect.

Fix an inscribed disk of U of radius rho>0 and center p. Translate the
level-r parent by -lambda^r p. The resulting patch covers the centered
disk of radius lambda^r rho, which tends to infinity.

Here is the required compactness argument with its relevant hypotheses.
Every unit tile has the same area a_U>0 and bounded diameter D. A tile
meeting a fixed disk of radius R lies inside the disk of radius R+D.
Interior disjointness bounds their number by a constant depending only
on R,D,a_U, uniformly in r. Reference-point translations of such tiles
are bounded, and orthogonal placements range over compact O(2), including
both reflections and arbitrary rotations. Thus each bounded region has
a convergent subsequence of its finite tile collection; a diagonal
extraction over increasing disks produces a locally finite limiting
collection of isometric U copies.

Two limiting tiles cannot have overlapping interiors: a small open ball
in a hypothetical intersection would remain inside both tiles in all
sufficiently close preceding placements, contradicting patch disjointness.
For coverage, use the same extraction on the slightly larger disk R+D
to retain every tile which can cover a point in the disk R. The finite
unions cover disk R for all sufficiently large r; their limiting closed
tiles still cover it. Equivalently, for any fixed point choose a covering
tile and pass to a convergent covering subsequence within that retained
finite collection. Taking all R covers the entire plane.

This compactness argument does not infer a plane tiling from unrelated
finite patches. The patches have expanding inradii and consist of fixed
positive-area prototiles. It does not assume finitely many absolute
orientations, an edge-to-edge limit, recognizability, or a fixed point of
the one-step substitution. A monohedral plane tiling of U alone is enough
to contradict the reviewed monohedral exclusion.

## Exact example and scope attacks

For b=1,c=sqrt2, suppose sqrt2=x+y*sqrt5 with x,y rational. Squaring and
independence of 1,sqrt5 gives xy=0. The cases then require x^2=2 or
y^2=2/5, both impossible for rational x,y. Thus the explicit example
satisfies the hypothesis exactly. Its field independence supplies this
restricted substitution obstruction, not a proof against translational
periods of unrestricted tilings.

The argument does not apply when c/b lies in K. It does not exclude
compound parent regions, nonhomothetic inflation, shape rearrangements
which cross parent boundaries, or arbitrary tilings with no substitution.
Those cases cannot be silently folded into the theorem.

## Fresh review of the complementary field-valued case

This section was added to the theorem after the initial review and then
read and checked separately. If c/b is in K, each child-side length
belongs to b*K. The macro side of length lambda*b is a sum of those
lengths, and b>0, so division by b forces lambda in K. No parameter
independence is used in this complementary case.

The area equation lambda^2=a+d*phi, with a,d nonnegative integers, implies
that lambda is an algebraic integer. This can be seen directly, without
merely invoking transitivity of integrality: its monic integer polynomial is

    t^4-(2a+d)*t^2+(a^2+a*d-d^2).

Indeed this is (t^2-a-d*phi)(t^2-a-d*phi'), with phi'=1-phi.

The integer ring claim for K also has a short exact justification. If an
irrational algebraic integer x+y*sqrt5 in K is written with rational x,y,
its quadratic minimal polynomial has integer trace T=2x and norm N.
Thus5(2y)^2=T^2-4N is an integer. Writing 2y=u/v in lowest terms gives
v^2 dividing5, so v=1 and Q=2y is an integer. The norm identity gives
T^2-5Q^2 divisible by4, requiring T,Q to have the same parity. Therefore

    x+y*sqrt5 = (T-Q)/2 + Q*phi in Z[phi].

A rational algebraic integer is an integer. Conversely every p+q*phi
with integers p,q satisfies a monic integer quadratic, so the integer
ring is exactly Z[phi]. There is no denominator or other-field exception.

Consequently lambda=p+q*phi for integers p,q, and direct squaring gives

    lambda^2=(p^2+q^2)+(2pq+q^2)*phi.

The U-parent counts must be a=p^2+q^2 and d=2pq+q^2>=0; multiplication
by phi gives V-parent counts(d,a+d). If d=0, the U rule would again be a
monohedral reptile and is excluded by the already checked compactness
and Rao argument. This complementary section does not require p,q to
be nonnegative in every field-valued parameter family; that additional
restriction is specific to the separate b=c=1 boundary alphabet.

For the separately proposed b=c=1 expansion sqrt(5+phi), these boundary
facts supply an exact rejection. All child side lengths lie in K; the
parent has a unit-length side, so its inflated boundary sum would force
lambda into K. But

    Norm_(K/Q)(5+phi)=29,

and a square in K has a rational-square norm. Since29 is not a rational
square, sqrt(5+phi) is not in K. This kills that specific six/seven-piece
proposal. The complementary section supplies only necessary arithmetic
conditions for other field-valued parameters, not a blanket exclusion.

No mathematical repair was necessary. The proof is analytic and its
matrix argument is unbounded; no finite search or implementation is
trusted to establish it. The focused prior-art comparison is in
[the source audit](../literature/pentagrid-generic-substitution-source-audit.md).
