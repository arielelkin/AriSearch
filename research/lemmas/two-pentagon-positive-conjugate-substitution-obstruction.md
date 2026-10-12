# Two convex pentagons: positive conjugate prevents small substitution inflation

Date: 2026-10-12. Status: [independently reviewed VALID](../reviews/two-pentagon-positive-conjugate-substitution-review.md).

Let an ordinary geometric substitution have exactly two compact genuine
convex pentagon prototiles, arbitrary lengths/angles, both reflections
allowed, and one common linear similarity factor lambda>1. Write
mu=lambda^2. If mu is an irrational real quadratic number whose algebraic
conjugate mu' is positive, then mu>=6. In particular linear inflation
lambda=phi or lambda=1+sqrt(2) is impossible for any such two-pentagon
substitution. This restricts a construction route, not infinite tilings.

## Proof including one-child images

Let M be the nonnegative integral 2-by-2 replacement matrix, its column j
listing the children in the image of parent j. The positive area vector a
satisfies a^T M=mu*a^T. Hence mu is an eigenvalue. Irrational quadratic mu
has degree two; therefore the characteristic polynomial of M is its
minimal polynomial and det(M)=mu*mu'>0.

A one-child image of the same prototile is impossible because its area
would require mu*a_j=a_j with mu>1. A one-child image of the other
prototile would give a column (0,1)^T or (1,0)^T. Its determinant is
nonpositive: respectively -M_01 or -M_10. This contradicts det(M)>0.
Zero-child images cannot cover the inflated parent. Thus both parent
images are nontrivial dissections. By the already reviewed
[general convex-pentagon dissection theorem](pentagrid-golden-metric-small-substitution-obstruction.md),
each has at least six children. Choose the smaller-area prototile with
area a_min. Its image has area mu*a_min and at least six children each
of area at least a_min, so mu>=6. QED.

For lambda=phi, mu=(3+sqrt(5))/2 and mu'=(3-sqrt(5))/2>0, with mu<6.
For lambda=1+sqrt(2), mu=3+2sqrt(2)<6 and mu'=3-2sqrt(2)>0.
Both contradict the bound. The statement requires precisely two species
and the ordinary whole-polygon replacement convention. Different parent
regions, more species, general hierarchical coverings and quadratic area
factors with nonpositive conjugates remain outside it. Nonsimilarity of
the prototiles is not required: determinant positivity handles potential
one-child replacements by differently sized similar pentagons.
