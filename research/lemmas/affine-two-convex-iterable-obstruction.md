# Iterable affine substitutions: an anisotropic obstruction

Status: adversarially reviewed VALID after scalar-orientation wording correction. Independent review: `research/reviews/affine-two-convex-iterable-hostile-review.md`. This is a restricted substitution theorem, not an unrestricted two-polygon impossibility result.

## Definitions and theorem

Let P be any finite collection of convex polygons with nonempty interiors, M an invertible expanding real 2 by 2 matrix, and suppose every MP has a finite dissection into isometric copies RQ+t of members Q of P. Require **equivariant iterability**: for each orthogonal part R used in these dissections and each integer n>=0, M^n R M^(-n) is orthogonal. This is the standard sufficient hypothesis allowing the same dissection to be transported to all inflated oriented copies without changing congruence classes. We do not claim every possible self-affine hierarchy satisfies it.

If M is not a Euclidean similarity, exactly one of the following necessary alternatives holds:

1. M has two real eigendirections, and all eigenvalues have unequal absolute values. Then every polygon of P is a parallelogram with those two side directions. In particular each individual member tiles periodically.
2. M has a positive integer power that is a nonzero scalar matrix. Its substitution can be iterated that many times to give an ordinary scalar similarity inflation; a negative scalar includes a half-turn. The original matrix M may itself reverse orientation.

A nondiagonalizable matrix with one eigenline cannot satisfy the hypotheses. A matrix with complex eigenvalues and irrational eigenargument cannot satisfy them either. The theorem therefore kills long-term anisotropic equivariantly iterable inflation as a forcing mechanism; it leaves the finite projective-order case open.

## Proof

Put H={R in O(2): M^n R M^(-n) is orthogonal for every n>=0}. H is a group. Every member commutes with the nonscalar positive definite matrix S=M^T M, since orthogonality of M R M^(-1) gives R^T S R=S. In an orthonormal eigenbasis of S its orthogonal centralizer is precisely the four diagonal sign matrices. Thus H has at most four elements. All dissection orientations lie in H.

Conjugation by M takes H into H: the n-th condition for M R M^(-1) is the (n+1)-th condition for R. Conjugation is injective, and H is finite, so it permutes H.

Let D0 be the union of unoriented side directions of the prototiles, and D=H D0. Each side of each MP is covered by finitely many child boundary segments. Interior-disjoint polygon dissections have this boundary covering property even with partial edge contacts: choose a point away from the finitely many child vertices; an incident child must have a side locally on the straight parent boundary. Consequently every member of M D0 lies in D. For h in H, M h D0=(M h M^(-1)) M D0 also lies in D. Thus M D is a subset of D. Invertibility makes its action injective, and finiteness gives M D=D.

Every line in D is therefore periodic under the projective action of M. For a real diagonalizable M with unequal eigenvalue moduli, writing a line as span(a e1+b e2) shows periodicity forces a=0 or b=0, because (lambda1/lambda2)^k is never 1. Hence D consists of its two eigenlines. A compact convex polygon with nonempty interior and only two unoriented side directions is a parallelogram: after removing redundant collinear vertices it has exactly four sides, one in each oriented direction, and opposite sides are parallel. Translations by the two adjacent edge vectors tile the plane, giving a monohedral periodic escape.

For a real Jordan matrix, every non-eigenline has infinite projective orbit (the Jordan shear accumulates linearly), leaving only one direction, incompatible with a polygon of nonempty interior. For real diagonalizable matrices with equal eigenvalue moduli, the nonscalar case has eigenvalues lambda,-lambda and M^2=lambda^2 I. For complex eigenvalues rho exp(plus/minus i theta), a real linear change of coordinates conjugates M/rho to a rotation. Existence of any periodic real projective line forces k theta to be an integer multiple of pi, so M^k is scalar. These cover all real invertible 2 by 2 matrices.

## Exact finite-projective-order escape from the obstruction

M=((0,-2),(1,0)) is expanding and nonsimilar, but M^2=-2I. Thus “not a similarity” alone is not enough to invoke alternative 1. This is an essential scope restriction. A construction here would still need exact dissection and unrestricted geometry-only forcing; no candidate dissection is asserted.

## Dependencies and non-consequences

Only elementary Euclidean linear algebra and convex polygon boundary covering are used. No finite direction assumption is imposed independently; it follows from equivariant iterability. Orientation-dependent rules, shape permutations under conjugation, inflation systems with growing orientation alphabets, and nonstationary constructions remain outside the theorem. Nothing here excludes an arbitrary two-convex aperiodic pair.
