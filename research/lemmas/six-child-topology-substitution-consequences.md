# Substitution consequences of the universal six-child wheel

Date:2026-10-13. Status: independently hostile-reviewed VALID; [review](../reviews/six-child-topology-hostile-review.md).
Depends on the independently reviewed universal wheel theorem at
six-child-topology-universal-wheel.md. No infinite tiling or aperiodicity
result is asserted.

## No finite convex-pentagon protoset substitutes into six children per parent

Suppose a finite protoset of genuine convex pentagons has a geometric
similarity substitution with common linear factor lambda>1 and exactly six
whole children in every parent. Isometries and partial contacts are allowed.
Let Amin be the smallest prototile area. In its inflated copy the six children
each have area>=Amin, so lambda^2>=6. Let L be the longest native side among
ALL prototiles, and choose a prototile having it. The universal wheel theorem
makes its inflated side the union of exactly two complete native child sides,
each length<=L. Thus lambda*L<=2L, giving lambda<=2, a contradiction.
No angle distinctness, equal species areas or common edge-length hypothesis
is used. Finiteness supplies both extrema.

If a finite irreducible convex-pentagon substitution has every parent image
NONTRIVIAL (more than one child), every column of its nonnegative count matrix
has sum>=6 by the finite-dissection theorem. The Perron root mu=lambda^2 is
at least6. If mu=6, multiplying the count matrix by its positive RIGHT Perron
vector and then the all-ones row forces each column sum exactly6. The preceding
six-per-parent contradiction rules this out. Hence mu>6.

The nontrivial-image assumption must not be dropped merely from irreducibility.
An irreducible integer count matrix can have a one-child column. In particular
this argument does not establish mu>6 for arbitrary negative-conjugate
similarity substitutions of two differently sized similar pentagons.

For exactly two pentagons and irrational quadratic mu with positive conjugate,
nontrivial columns DO follow: the matrix has positive determinant, nonzero
integer off-diagonal entries (otherwise its eigenvalues are integers), and
positive diagonal entries. Each column then has at least two children. Thus
this class has the strict strengthened bound mu>6.

## General convex boundary-defect inequality

Let a genuine convex p-gon be partitioned nontrivially into F genuine convex
children with native side counts ni. Use planarized seam counts I,B,J,E,H and
D from the universal wheel proof. Euler E=I+F-1 and the seam-degree identity
2E=3I+B+J+D give

    I+B+J+D=2F-2.

Summed native angles with inserted straight incidences give

    sum ni-2F+H=2I+p-2+B.

Elimination yields the exact identity

    sum(6-ni)=6-p+B+2J+2D+H.                 (1)

Any nontrivial convex partition has at least two active boundary seam nodes:
if there are zero or one, deleting the possible node leaves a connected parent
boundary arc. The incident child label is locally constant there because a
change between child boundary intervals requires a seam endpoint. The connected
arc therefore belongs to one child. Closure makes the entire parent boundary
belong to that child; convexity then makes the entire parent belong to it,
contradicting nontriviality. Hence B+J>=2. From(1),

    sum(6-ni)>=8-p.                         (2)

This is a general finite convex dissection bound, with arbitrary partial
contacts. No claim about two boundary endpoints PER seam component is needed.

## Forest gate for a parent containing an equal-or-higher-sided child

Let every child have at least five sides, and suppose a convex p-gon parent
has a child with at least p sides. Its internal seam graph cannot be a forest.
Indeed, if the nonempty seam forest has h>=1 components, then

    B+J=F+h-1, I<=B+J-2h.

The native-angle identity implies

    3F+sum(ni-5)+H=2I+p-2+B
      <=3(B+J)-J-4h+p-2
       =3F+p-5-h-J.

Thus sum(ni-5)+H<=p-6. The designated child's contribution is>=p-5,
a contradiction. The graph has a cycle. By the previously reviewed cycle
separation argument, some child has no positive outer contact and at least
five distinct neighbors, so the entire dissection has at least six children.
The coefficient of J above is ONE, not two; no stronger corner bound is used.

## Positive-conjugate bounds for a pentagon and an n-gon, n>=6

Let the two prototiles be a genuine convex pentagon P and genuine convex
n-gon Q, and suppose ordinary geometric similarity substitution has common
area factor mu>1, irrational real quadratic with positive algebraic conjugate.
Write the count matrix with columns for P,Q as

    M=[[a,b],[c,d]].

Area eigenvectors give the Perron root mu. Irrationality forces b,c>=1;
positive determinant ad>bc forces a,d>=1. The two image columns are nontrivial.
The P image has at least seven children: six would force ALL children to be
pentagons by the universal wheel theorem, contrary to c>=1 and n>=6. The
Q image contains a Q child (d>=1), so the forest gate forces at least six.
Thus

    a+c>=7, b+d>=6, ad>bc.

Put k=n-6>=0. Applying the boundary-defect inequality(2) to the two images gives

    a-k*c>=3, b-k*d>=2-k.                   (3)

In particular a>=k+3 and b>=2+k(d-1). Monotonicity of the Perron root
under nonnegative entry increases now proves

    n=6:  mu >=(7+sqrt33)/2;
    n=7:  mu >=(7+sqrt41)/2;
    n=8:  mu >=4+2sqrt2;
    n>=9: mu >=(n-2+sqrt((n-4)^2+20))/2.      (4)

Here is a complete analytic minimum, without an unbounded search disguised
as a finite cutoff. Every comparison is to a componentwise lower matrix.
For n6, a>=3. Put c_min=max(1,7-a). When a>=7, mu>a>=7, exceeding the
claimed minimum. For a3..6, all b>=2 are exhausted by these lower(b,d)
pairs; the final pair in each row also covers every larger b:

    a3,c4: (2,4); b>=3 gives (3,5) via ad>bc.
    a4,c3: (2,4),(3,3); b>=4 gives (4,4) via ad>bc.
    a5,c2: (2,4),(3,3),(4,2); b>=5 gives (5,3).
    a6,c1: (2,4),(3,3),(4,2); b>=5 gives (5,1).

The respective Perron roots are

    a3: (7+sqrt33)/2, 4+sqrt13;
    a4: 4+sqrt6, (7+sqrt37)/2, 4+sqrt12;
    a5: (9+sqrt17)/2, 4+sqrt7, (7+sqrt41)/2, 4+sqrt11;
    a6: 5+sqrt3, (9+sqrt21)/2, 4+2sqrt2, (7+sqrt45)/2.

Each is at least(7+sqrt33)/2, with equality only at the first lower matrix
[[3,2],[4,4]]. These radical comparisons follow by positive squaring.

For n7, a-c>=3 and a+c>=7 give a>=5. At a5, necessarily c2.
For d1, b>=5; for d2,b>=4; for d>=3,b>=d+1>=4.
Compare respectively [[5,5],[2,1]], [[5,4],[2,2]], [[5,4],[2,3]],
whose roots are3+sqrt14,(7+sqrt41)/2,7. The middle is smallest.
At a6,c>=1, d1 requires b5, d2 b4, d>=3 b>=4. The lower roots are
(7+sqrt45)/2,4+2sqrt2,7, all larger. At a>=7, mu>a>=7.

For n8, a-2c>=3 and a+c>=7 force a>=6. At a6,c>=1;
d1 requires b>=5, d2 requires b>=4, and d>=3 requires b>=6.
Compare [[6,5],[1,1]], [[6,4],[1,2]], [[6,6],[1,3]]. Their roots are
(7+sqrt45)/2,4+2sqrt2,(9+sqrt33)/2, so the middle is smallest.
At a>=7, mu>a>=7 exceeds it.

For n>=9, k>=3 and a>=n-3,c>=1. If d1, b+d>=6 forces b>=5.
If d>=2, (3) gives b>=k+2>=5. Consequently every matrix is
componentwise at least [[n-3,5],[1,1]], whose root is(4).

The displayed minimizing matrices satisfy the stated algebraic conditions,
but NO convex geometric realization is supplied. These are necessary lower
bounds; algebraic attainment is not geometric sharpness. The positive-conjugate
hypothesis and ordinary whole-native-polygon substitution are essential.
Nonpositive-conjugate inflation, extra tile species, compound-parent hierarchies
or arbitrary plane tilings remain outside these statements.

## Computation and review

All inequalities and finite matrix case splits above are analytic. No solver,
new enumeration or certificate is used. Independent review checked the boundary-label argument, Euler conventions,
Perron-vector orientation and matrix hypotheses, and found no unresolved defect.
