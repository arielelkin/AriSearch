# Fresh audit of the fixed Robinson height/wedge boundary screen

**Reviewer:** pending_reviews. The reviewer did not develop the root-owned
height producer or its retained certificate. The source-height/Stokes
invariant was supplied by the root as a mathematical proposal; this audit
independently derived its lift equations and checked signs and factors.
The reviewer wrote the companion analytic formalization, whose text should
receive a separate fresh review before it is promoted as independently
reviewed in its own right.

**Verdict: valid** for the proposed necessary invariant and the complete
fixed boundary screen. No substantive defect was found. The screen excludes
neither U nor V. No actual source cluster or infinite tiling is certified.

## Claim and assumptions checked

The source is an actual edge-to-edge unit rhomb tiling of the whole plane,
with the specified short thin and long fat diagonal cuts. Every source unit
edge is in a fixed ten-direction frame. A macro compiler uses finitely many
whole source triangles and its convex outer boundary follows their whole
native edges. Arrow legality is not assumed or inferred by these necessary
checks. A patch with cuts or T-junctions outside this source hypothesis cannot
use its boundary data as a source witness.

The signed unit lift E_k has period 10 and E_(k+5)=-E_k. Every rhomb loop
has lift zero. The locally finite rhomb cellulation fills the simply connected
plane, so a finite closed edge walk is a finite sum of face boundaries.
This proves a path-independent global height in Z^5. The physical kernel
Z*R, R=(1,-1,1,-1,1), does not weaken required exact height closure.
The proposed diagonal lifts were checked on the thin and fat references:
z-1=s*z^3 lifts to E_1-E_0, and z^3-1=phi*z^4 lifts to E_3-E_0.

For a side a+b*phi, the independent lift calculation gives

    a*E_k+b*(E_(k-1)+E_(k+1))+n_s*(-1)^k*R.

The U base sum is -R and its variable directions have even k. The V base
sum is 3R and its variable directions have odd k. Thus U requires total
n_s=1 on sides 0,1, and V requires total n_s=3 on sides 1,3,4. Their exact
boundary edge counts are 10 and 13; each has six unit edges. The latter V
count sharpens the older fan/parity witness with 11 edges, which was only
necessary local data and is correctly rejected by this stronger filter.

## Wedge signs and factors attacked

With a counterclockwise closed lifted boundary, Q=sum H_j wedge H_(j+1)
is constant-height invariant. Interior edges cancel on summing oriented
triangle boundaries. Setting a unit-edge triangle apex to zero leaves
Q=A wedge B, where A,B are its two signed unit lifts. Physical cross product
is positive on every basis wedge e_i wedge e_j with i<j, since its angle
is (j-i)*pi/5 in (0,pi). Therefore every counterclockwise allowed triangle
has exactly one positive coefficient, independently of reflection. Physical
projection gives twice its area. A rhomb contributes two wedges, and a
triangle contributes one, so no one-half factor is missing.

Pairs with difference 1 or 4 are thin, and 2 or 3 are fat. The exact fixture
areas and irrationality of phi force the counts (7,9) and (9,16). Boundary
word order can change Q even though it cannot change the total height;
the producer retains every ordered word rather than reducing to side counts.
Rotated and reflected source placements act by the appropriate signed
basis permutations and orientation reversal, preserving these necessary
positive-pair tests.

The companion formalization also records the additional paired-diagonal
condition q_ij>=b_ij and q_ij=b_ij modulo 2, where b_ij counts boundary
source diagonals of that pair. Its proof is the zero/one/two triangle count
inside each source rhomb. This condition is NOT part of the producer stage
counts reviewed here. The necessity of completing each forced boundary diagonal half to its
whole source rhomb was also checked: the mate is its diagonal-midpoint
half-turn; distinct boundary diagonals correspond to distinct parent rhombs;
these parents must be interior-disjoint and edge-to-edge even outside the
macro. Removing the forced halves leaves precisely 6 U or 9 V whole rhombs
with pair counts (q_ij-b_ij)/2. No new geometry producer, containment/overlap
result, or completion-screen count is audited in this review.

## Independent computation and completeness

The [producer](../searches/pentagrid-robinson-height-boundary.py) and
[certificate](../certificates/pentagrid-robinson-height-boundary.json) were
read. The [independent checker](verify_pentagrid_robinson_height_boundary_independent.py)
imports neither the producer nor its boundary dependency. It derives words
by Cartesian products of symbols and exact irrational-basis coefficients;
it tests fan existence by Boolean dynamic programming rather than walk
enumeration; and it computes Q directly from the lifted vertex shoelace.
Every retained stage count, the complete wedge histogram, and the retained
first passing boundary are checked.

| Fixture | All words | Zero height | Height and fans | Height and nonnegative Q | All three | Distinct final Q |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| U | 625 | 72 | 42 | 36 | 30 | 30 |
| V | 21,801 | 2,483 | 2,315 | 311 | 311 | 221 |

The independent checker passed. Its finite domain is the two stated fixture
side tables and every positive ordered word in the alphabet {1,phi,phi-1};
no arbitrary side-length or placement search was performed. All decisions
use integers. No timeout, random seed, solver result, or numerical equality
is involved.

## Defects, repairs, and limits

Counterexample attempts included nontrivial physical-kernel closure,
misusing a nonsimply-connected graph, a diagonal with inconsistent two-edge
lifts, signed unit directions outside 0,...,4, reflected source triangles,
confusing a rhomb wedge with a half-triangle wedge, loss of boundary order,
and promoting passing height or fan data to geometric assembly. The explicit
source and whole-triangle hypotheses handle these attacks. No repair was
needed, and no remaining uncertainty was found in the reviewed necessary
screen. Global source extraction, geometric patch existence, arrow matching
and shape-only forcing remain unproved. No novelty or priority claim was
examined or made.

```text
conda run --no-capture-output -n arisearch python research/reviews/verify_pentagrid_robinson_height_boundary_independent.py
```

The [companion analytic formalization](../lemmas/pentagrid-robinson-source-height-and-stokes.md)
preserves the full derivation and its exact scope; this review does not
replace a distinct fresh review of that reviewer-authored text.
