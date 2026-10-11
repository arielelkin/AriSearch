# Generic parameter independence forbids every homothetic substitution

**Status:** adversarially reviewed as valid, including the complementary field case, in the [fresh audit](../reviews/pentagrid-generic-metric-substitution-review.md). This concerns
finite whole-polygon subdivisions of an exact family, not arbitrary plane
tilings or shape-only aperiodicity. Date2026-10-10.

## Statement

Let K=Q(sqrt5), phi=(1+sqrt5)/2, and b,c>0 with c/b not in K.
Take the [area-compatible convex pentagons](../searches/pentagrid-golden-metric-area-compatible.md):

    U: (phi^2*b+phi*c, phi^2*b+phi*c, b, c, b),
    V: (b, 2*phi*b+phi^2*c, b, phi*(b+c), phi*(b+c)),

with their fixed U,V pentagrid angle words. Their areas satisfy
area(V)=phi*area(U). Assume the reviewed monohedral exclusion of U, whose
dependency is explicitly imported Rao classification.

There is no real linear inflation lambda>1 for which lambda U can be
partitioned into finitely many isometric whole copies of U and V, even
allowing reflections and partial contacts.
In particular no homothetic two-prototile substitution exists in this
parameter subfamily. An exact member is b=1,c=sqrt2; sqrt2 is not in K.

The statement does not cover c/b in K, including b=c=1. It does not
exclude nonhomothetic substitutions, compound supertiles, arbitrary plane
tilings or aperiodic forcing by this pair.

## Boundary segments are whole child sides

In a finite partition of a convex polygon into convex polygons, each
child lies inside the parent. A positive-length contact with a supporting
parent side lies on a complete native side of that child: a child vertex
cannot lie strictly inside a native side, and the parent side endpoints
cannot truncate the child side, because continuing beyond either endpoint
would leave the convex parent at a genuine corner. Thus every parent side
is a finite concatenation of whole child sides. Native side subdivisions
by other children do not change their complete lengths on the outer
boundary. Overlaps of boundary intervals have zero length unless child
interiors overlap near that interval. Consequently boundary length equals
a sum of complete child-side lengths with nonnegative integer counts.

Every child side has length alpha*b+beta*c with alpha,beta in K and
alpha,beta>=0 in the positive real embedding. The only sides with beta=0
are pure b sides, of length exactly b. The only sides with alpha=0 are
pure c sides, of length exactly c. All other listed side lengths have
both coefficients strictly positive.

## Area and two boundary equations

Let a,d be the nonnegative integer numbers of U,V in the lambda U
partition. Exact area conservation gives

    lambda^2=a+d*phi in K.                         (1)

The lambda U boundary contains a side of length lambda*b and a side of
length lambda*c. Whole-side boundary sums therefore give

    lambda*b=A*b+B*c,
    lambda*c=C*b+D*c,                             (2)

where A,B,C,D lie in K and are nonnegative in its positive real embedding.
These are two actual boundary sides of the same macro-polygon; they need
not use the same boundary word. There is no rational or minimum-length
assumption beyond the explicit coefficients of the child sides.

If lambda belongs to K, the K-linear independence of b,c makes B=0 and
A=lambda in the first equation. Nonnegative coefficients then allow only
pure b child sides there. Each has length b, so lambda=A is a positive
integer. In particular lambda^2 is an integer.

If lambda does not belong to K, (1) gives its degree-two minimal polynomial
t^2-lambda^2 over K. Equation(2) makes lambda an eigenvalue of the real
two-by-two K-matrix [[A,B],[C,D]], with eigenvector(b,c). Its monic
characteristic polynomial must be that minimal polynomial. Hence

    A+D=0, lambda^2=B*C.

Nonnegativity forces A=D=0. The first boundary sum can therefore contain
only pure c sides, so B is a positive integer. The second can contain
only pure b sides, so C is a positive integer. Again lambda^2 is an integer.
This exhausts arbitrary real lambda>1; it does not assume a power of phi.

## Integer area scaling would force an impossible monohedral tiling

Write N=lambda^2, a positive integer greater than1. Since1,phi are
rationally independent, (1) forces exactly N U and zero V children in
lambda U. The corresponding lambda V partition, if present, would also
have zero U and N V children. The first partition alone is enough for
the contradiction.

Iterate its homothetic dissection. At level r, lambda^r U is partitioned
into isometric copies of the original U, with rotations and reflections
allowed. Its inradius tends to infinity. Translate these patches to contain
arbitrarily large centered disks. Fixed positive area, bounded diameter,
compact orientation space and local compactness of placements yield a
subsequential whole-plane monohedral U tiling: interiors remain disjoint,
and every bounded disk stays covered. Equivalently, use the usual exact
finite-prototile tiling compactness argument.

But every positive U-angle pentagon is monohedrally untileable under
[the reviewed Rao filter](pentagrid-pentagon-monohedral-filter.md).
Thus the subdivision cannot exist, proving the theorem.

For the explicit parameter c/b=sqrt2, if sqrt2=x+y*sqrt5 with rational
x,y, squaring gives xy=0, followed by x^2=2 or5y^2=2. Neither has a rational
solution. The example therefore satisfies the stated independence exactly.

## Complementary field-valued parameter case

For c/b in K, every child length lies in the one-dimensional K-module b*K.
Any finite subdivision of lambda U has a macro side of length lambda*b,
so its whole-child-side boundary sum forces lambda in K. In particular the
b=c=1 proposal lambda=sqrt(5+phi), with area counts6/7, is impossible:
Norm_K/Q(5+phi)=29, while a square in K has rational-square norm.

Area conservation also implies lambda^2 in Z[phi]. Thus lambda is an
algebraic integer, by transitivity of integrality, and lambda in K implies
lambda in the ring of integers Z[phi]. Writing lambda=p+q*phi with integers
p,q gives

    lambda^2=(p^2+q^2)+(2pq+q^2)*phi.

Consequently candidate counts must have a=p^2+q^2 and d=2pq+q^2>=0,
with U-parent counts(a,d) and V-parent counts(d,a+d). The case d=0 would
again be a monohedral reptile and is impossible for U. These are only
necessary arithmetic conditions; they give no geometric subdivision.
The quadratic-field integer ring used here is the standard exact ring
of integers of Q(sqrt5). This additional case has received the same valid fresh review.

## Dependencies and unresolved scope

The area-family geometry and identity have an exact certificate and a valid
[fresh independent audit](../reviews/pentagrid-area-compatible-family-review.md). U's monohedral exclusion has a valid fresh source/algebra
review, conditional on the explicitly imported complete monohedral theorem.
The separate fresh hostile review checked whole-side boundary sums,
arbitrary lambda, the complementary field case and the repeated-dissection limit.
No finite search or numerical threshold is used here.
