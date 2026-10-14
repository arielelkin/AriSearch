# No distinct-angle two-size six-child pentagon wheel

Date:2026-10-13. Status: independently adversarially reviewed VALID.
[Combined review](../reviews/resumed-two-size-wheel-complete-counts-review.md)
and [initial wheel review](../reviews/resumed-two-size-wheel-review.md).
This is a computer-assisted finite-dissection theorem, not an impossibility
theorem for unrestricted plane tilings.

## Exact theorem and hypotheses

Let P be a compact genuine convex pentagon with five pairwise distinct
native angles and positive native lengths l_i, i modulo5. Let b>0,d>=0
be integers with b+d=6, mu>1 satisfy mu²=dmu+b, and lambda=sqrt(mu).
There is no partition of mu P into b isometric copies of P and d
isometric copies of lambda P having this particular wheel scheme:

* One child is central and the five others each occupy a different genuine
  parent corner by one native corner equal to the entire parent angle.
* Each corner child has two complete consecutive sides on the parent rays.
* Every parent side is exactly the union of the full native boundary sides
  of its two endpoint corner children, with no other boundary child.

All child reflections and arbitrary real lengths are allowed. Inner seams are not restricted by the original boundary proof. The new
universal topology consequence below establishes that every six-pentagon
partition automatically has this scheme.

## New unrestricted-topology consequence

The [universal six-child topology theorem](six-child-topology-universal-wheel.md), independently reviewed in [its hostile audit](../reviews/six-child-topology-hostile-review.md), proves that every dissection of a convex pentagon into exactly six convex children with at least five sides automatically has all three wheel properties above. Consequently, under the distinct-angle, two-size and count/area hypotheses in the statement, there is no such six-child dissection of **any topology**, including partial contacts. This implication uses no additional computational domain: the same1120 determinant certificates and analytic row exclusions apply after the universal geometric topology reduction.

The topology theorem itself has no native-angle distinctness or congruence hypothesis. The boundary determinant theorem still requires five pairwise distinct angles of P, both specified sizes1andlambda, and mu²=dmu+b. A general repeated-angle pentagon or different count relation is not covered by this synthesis. The direct synthesis passed [fresh combined review](../reviews/six-child-topology-two-size-synthesis-review.md) as VALID.

## Necessary boundary matrix

Index a reference vertex i and the following native side i of P. Distinct
angles force the child occupying parent vertex i to use native vertex i.
Let t_i in{1,lambda} be its scale, r_i in{0,1} its direct/reflected placement.
The full boundary-length equation is

    mu*l_i = t_i*(l_i if r_i=0 else l_(i-1))
             +t_(i+1)*(l_i if r_(i+1)=0 else l_(i+1)).

These equations express necessary coverage, not additional placement rules.
Let C be the nonnegative matrix on the right, so C*l=mu*l. Its row sums
are t_i+t_(i+1)<=2lambda. Choosing an index of maximal positive l_i proves
mu<=max row sum<=2lambda, hence mu<=4.

## Complete count split and analytic exclusions

b+d=6 and b>0 leave d=0,...,5. The positive roots are respectively
sqrt6, (1+sqrt21)/2, 1+sqrt5, (3+sqrt21)/2, 2+sqrt6,
and(5+sqrt29)/2. Each is irrational with a negative quadratic conjugate.

For d4 andd5, mu>4 violates the row bound. For d0 every corner scale is1,
so the row bound is2<sqrt6. For d1 there is at most one large corner;
all row sums are at most1+lambda. With mu=(1+sqrt21)/2 in(1,3),
(mu-1)²-mu=6-2mu>0, giving1+lambda<mu. These four cases are impossible.

## Exact finite certificates for the remaining two cases

For d2,b4, if central is small there are C(5,2)*32=320 patterns; if
central is large there are C(5,1)*32=160. Total480, no symmetry reduction.
For d3,b3 the respective corner choices give320 and320, total640.
All reflection bit vectors of length5 are included.

For each pattern compute M=mu*I-C over Q(a), a=lambda. The irreducible
polynomials are a⁴-2a²-4 for d2 and a⁴-3a²-3 for d3. Irreducibility
follows because mu is quadratic with negative conjugate and hence cannot
be a square in its real quadratic field. Certificates retain complete case
labels and four integer determinant coefficients in basis1,a,a²,a³:

* [480-case certificate](../certificates/resumed_intrinsic_two_size_wheel.json)
* [640-case certificate](../certificates/resumed_intrinsic_wheel_d3.json)

All1120 determinants are nonzero. Each embedding of a number field is
injective, so they remain nonzero in the positive real embedding. Thus the
boundary equations have no nonzero real length vector in either case,
which proves the theorem independently of inner geometry and closure.

The producers use Sage number-field elimination. Independent verifiers
assemble a separate two-ray corner block for each child and compute the
120-term Leibniz determinant with Python integer polynomial arithmetic,
reducing powers by the respective monic quartic. They check every retained
coefficient and the complete unique case keys; neither imports the producer
or Sage. Both domains and both independent checks passed.

## Replay and dependencies

From repository root, via the locked arisearch environment:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/resumed_intrinsic_two_size_wheel.py --check research/certificates/resumed_intrinsic_two_size_wheel.json
    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/resumed-two-size-wheel-independent.py
    mise exec -- conda run --no-capture-output -n arisearch python research/searches/resumed_intrinsic_wheel_d3.py --check research/certificates/resumed_intrinsic_wheel_d3.json
    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/resumed-two-size-wheel-complete-counts-independent.py

Precise finite-domain records: [initial480](../searches/resumed-two-size-six-wheel.md)
and [complete count decision](../searches/resumed-two-size-wheel-complete-counts.md).
No random seed, numerical branch, solver verdict or interrupted enumeration.
No pentagon monohedral classification is used. The theorem only depends on
the explicit boundary equations, elementary quadratic algebra and the
independently verified finite certificates. No novelty claim is made.

## Non-consequences and restart

Repeated native angles, more than six children and nonconvex parents
are outside this theorem. Under the exact six-child convex hypotheses,
subdivided parent corners, extra boundary children and alternative
topologies are excluded by the reviewed universal topology theorem. There is no infinite covering, intrinsic decoder
or aperiodicity claim. A new construction must give an exact changed contact
scheme. The repeated-angle U word has16 native-corner assignments, but its
[completed 7680-case boundary audit](../searches/resumed-two-size-repeated-u-wheel.md)
excludes the stated wheel at mu=1+sqrt5. The older
[unrestricted two-U theorem](pentagrid-two-asymmetric-u-obstruction.md)
already excludes every two-U metric pair. A new repeated-angle proposal
must use geometry outside those completed exclusions.
