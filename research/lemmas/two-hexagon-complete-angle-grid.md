# A complete rational angle grid for all two-hexagon triple types

Date: 2026-10-12. **Status: adversarially reviewed exact proof;** [fresh review](../reviews/two-hexagon-complete-angle-grid-review.md).
This supplies a complete angle grid for the global SFT query. It does not
settle any SFT, enumerate the higher-rank flats, or decide joint polygon
and side-length realisability.

## Statement

Angles are measured in degrees. Number the twelve native corners as in
the global SFT encoding, with species A at indices 0,...,5 and B at 6,...,11.
There are 364 three-element multisets of these indices. An exact closed
triple type T is the set of all triples whose sum-360 equation follows
rationally from the equations of T and the two species sum-720 equations.
Rank k means additional rank modulo those two species equations, so
0<=k<=10. All the equations share the all-120-degree solution.

**Theorem.** Every exact closed type T has a representative

    alpha_c = a_c / 5394,  a_c an integer,
    0 < a_c < 180*5394,
    sum_A a_c = sum_B a_c = 720*5394,

such that sum_{c in t} a_c = 360*5394 holds **if and only if** t belongs
to T. In fact the representative lies in the open angle interval (60,180)
and can be written alpha_c=120+v_c/5394, with integer |v_c|<=323632.

Every integer denominator K>=5394 works by the same construction. If a
representative in (119,121) is desired, every K>=323633 works. These are
safe constants proved below, not a claim of the globally smallest possible
grid denominator.

Consequently `Query(grid=5394)` in the global CEGAR code represents every
rationally closed exact angle type. It is a complete angle relaxation,
in contrast to an arbitrary small grid. A grid-SAT result still does not
establish polygon realisability or infinite tilability.

## 1. Centering and primitive integer equations

Put u_c=alpha_c-120. The two species equations become

    sum_A u_c = sum_B u_c = 0.

A triple equation becomes sum_{c in t}u_c=0, including multiplicities.
Let n_A,n_B denote the disjoint six-entry indicator rows. A triple row
m_t counts its multiplicities. If t=(c,c,c), use the equivalent primitive
row e_c=m_t/3; otherwise retain m_t. Every row remains integer.

Choose k independent primitive triple rows in addition to n_A,n_B, and
let M be the resulting (k+2)-by-12 matrix. Its rank is k+2 and its kernel
has dimension d=10-k. The kernel is the centered flat of T. Closure means
that for every t not in T the linear form sum_{c in t}u_c is nonzero on
this kernel. No angle-box feasibility assumption is needed: the common
all-120 point and arbitrarily small generic perturbations already give it.

## 2. Uniform bounds for determinant minors

Project a primitive triple row m orthogonally off n_A,n_B, whose squared
norms are six and whose supports are disjoint. Its squared projected norm is

    ||m||^2 - ((sum_A m)^2+(sum_B m)^2)/6.

For the possible multiplicity/species patterns, the values are:

| Primitive triple pattern | Squared projected norm |
|---|---:|
| All three copies of one corner, primitive row e_c | 5/6 |
| Multiplicities 2+1, both corners in one species | 7/2 |
| Multiplicities 2+1, corners in different species | 25/6 |
| Three distinct corners in one species | 3/2 |
| Three distinct corners distributed between species | 13/6 |

The maximum is 25/6. For any (k+2)-column minor of M, subtracting the full
species projections from its triple rows is a determinant-preserving row
operation after restricting to those columns. The restricted projected
rows have norm no larger than their full twelve-entry norms. Hadamard's
inequality therefore gives

    |det minor| <= 6*(5/sqrt(6))^k.

Every such determinant is an integer. Thus all minors satisfy

    |det minor| <= D_k,
    D_k = floor(sqrt(36*25^k/6^k)).                 (1)

This argument applies to every minor, including singular minors. It does
not assume that restricted species rows remain orthogonal to the projected
triple rows.

## 3. A bounded integer basis spanning the kernel

Choose pivot columns J so that B=M[:,J] is a nonsingular square matrix,
and set Delta=det(B). For each free column j, construct a vector b_j with

    b_j(j)=Delta;
    b_j(i)=0 at every other free column;
    b_j(J_a)=-det(B with column a replaced by M[:,j]).

Cramer's rule gives M b_j=0. Every coordinate is an integer minor of M,
so |b_j(c)|<=D_k by (1). The free-coordinate submatrix is Delta times the
identity, proving that these d vectors form a basis of the full kernel
over Q and over R. They need not form a saturated basis of the entire
integer-kernel lattice; that stronger property is unnecessary.

For each forbidden triple t not in T, the coefficients

    gamma_t(j) = sum_{c in t} b_j(c)

are not all zero, because its linear form is nonzero on the full kernel.

## 4. Avoiding all forbidden triple hyperplanes with bounded coefficients

Let H=364-|T|. When d>=1, set the first basis coefficient to one. Each
forbidden linear form is then a nonzero affine form in the remaining
coefficients: if its remaining coefficients all vanish, its first
coefficient is a nonzero constant.

Choose each remaining coefficient from the integer interval

    I_H = {-floor(H/2),...,ceil(H/2)},

which contains H+1 values. A nonconstant affine hyperplane contains at
most (H+1)^(d-2) points of I_H^(d-1); a nonzero constant form excludes no
points. Thus H forbidden hyperplanes cannot cover that entire grid.
For d=1, the fixed coefficient one already avoids every forbidden form.

Equivalently, there is a deterministic greedy construction. At each step,
keep every forbidden expression nonzero as an affine form in the
unassigned variables. A form can become identically zero at the next
assignment only if the current variable is its last nonzero unassigned
coefficient. That form forbids at most one scalar value. There are at most
H forms and H+1 available integers, so a valid choice always exists.
After the last step every forbidden expression is a nonzero constant.
This needs polynomially many exact rational operations, rather than
enumeration of the whole coefficient grid.

With these coefficients a_j, the integer vector v=sum_j a_j b_j satisfies

    sum_A v_c = sum_B v_c = 0;
    sum_{c in t}v_c = 0 iff t belongs to T;
    |v_c| <= D_k*(1+(d-1)*ceil(H/2)).              (2)

At least k distinct triples occur in T, because k independent triple
rows were selected from it. Hence H<=364-k. Substituting this bound into
(2) gives the following entirely integer table.

| k | d | H bound | D_k | Coefficient cap | Deviation bound B_k | Safe angle grid floor(B_k/60)+1 |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 10 | 364 | 6 | 182 | 9834 | 164 |
| 1 | 9 | 363 | 12 | 182 | 17484 | 292 |
| 2 | 8 | 362 | 25 | 181 | 31700 | 529 |
| 3 | 7 | 361 | 51 | 181 | 55437 | 924 |
| 4 | 6 | 360 | 104 | 180 | 93704 | 1562 |
| 5 | 5 | 359 | 212 | 180 | 152852 | 2548 |
| 6 | 4 | 358 | 434 | 179 | 233492 | 3892 |
| 7 | 3 | 357 | 885 | 179 | 317715 | 5296 |
| 8 | 2 | 356 | 1808 | 178 | 323632 | 5394 |
| 9 | 1 | 355 | 3691 | 178 | 3691 | 62 |

For k=10 the kernel is zero-dimensional. Closure then gives all 364
triples, and v=0 suffices for every denominator.

## 5. Completing the representative and the query consequence

The maximum deviation bound is 323632. Since

    323632 < 60*5394 = 323640,

the integer numerators a_c=120*5394+v_c yield angles strictly between
60 and 180. The species sums follow from v's kernel membership, and
exact triple membership follows from the nonzero forbidden evaluations.
This proves the theorem. With K=323633 the same bound is less than K,
placing all angles strictly between 119 and 121.

An arbitrary original geometrically realisable pair need not have angles
on this grid. Its exact triple set T does have a grid representative,
and the original side-equality relation e may be carried over unchanged
as formal length data. The SFT depends only on T and e, so its legal
patches and tori are unchanged. The representative angles need not close
actual polygons compatible with that e. Completeness here concerns the
angle relaxation, not joint geometric realisability.

The grid query's reified equivalence

    t_tau iff sum_{c in tau} a_c = 360*K

automatically enforces rational closure. Thus an inherited-escape query
at K=5394 can eliminate its iterative angle-closure refinement without
excluding any exact angle type. Infeasibility of the relaxed query has
its usual global covering meaning; feasibility and UNKNOWN retain their
usual limits. This theorem supplies no solver outcome or proof log.

## Exact arithmetic replay and constructive example

The [verifier](../reviews/verify_two_hexagon_complete_angle_grid.py)
enumerates all 364 primitive projected norms using rational arithmetic,
recomputes every integer bound in the table, and constructs a representative
for the retained minimal covering rank-five obstruction. It computes
its kernel independently with SymPy, constructs the Cramer basis, greedily
avoids the forbidden triples, and verifies every resulting species sum,
triple equality and strict angle bound.

The [retained numeric and constructive certificate](../certificates/two-hexagon-complete-angle-grid.json)
records the complete bound table, integer basis, chosen coefficients,
deviation vector and angle numerators. No SAT/LP or geometric solver is
used. The certificate does not independently enumerate all exact types;
the theorem proves coverage uniformly without such an enumeration.

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python3 research/reviews/verify_two_hexagon_complete_angle_grid.py --check research/certificates/two-hexagon-complete-angle-grid.json

To construct a representative of another closed triple set:

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python3 research/reviews/verify_two_hexagon_complete_angle_grid.py --input TYPE.json --output OUTPUT.json
