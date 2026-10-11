# Complete classification of the single-120 / qq-low-high metric slice

Status: **VALID after fresh independent inventory, arrangement/native-seam and actual-phase audits, with [whole-theorem synthesis](../reviews/branching-hexagon-two-run-single-120-complete-slice-synthesis-review.md).** This is a complete specified two-parameter resonance slice, not a classification of all homogeneous-star resonances or a resolution of the unrestricted target. No outcome is inferred from a bounded quotient search or a timeout.

## Exact actual domain and result

Fix0<delta<30,q=1 and0<beta<180. Define

    P_beta=1+exp(i60)+exp(i(240-beta)),
    rho=arg(P_beta),     p=2cos(delta)/|P_beta|.

Restrict to p unequal to1 and rho+beta>120+delta. A has native side word(p,q,p,q,p,q) and directions(0,60+delta,120,180+delta,240,300+delta). B has native side word(p,p,p,q,q,q) and directions

    (0,60,240-beta,rho+120-delta,rho+180+delta,rho+240-delta).

Its native angle list is

    (60+rho-delta,120,beta,300-rho+delta-beta,
     120-2delta,120+2delta).

Closure, positive lengths and strict convexity on exactly this domain are detailed in `branching-hexagon-two-run-single-120-exceptional-stars.md`. In particular P_beta has positive real/imaginary parts and never vanishes, so rho is an unambiguous principal phase in(0,90). This is the actual metric domain, not independent free angle data.

**Theorem. The pair tiles the plane if and only if beta120. At beta120 it admits a doubly periodic tiling; every other beta in the actual domain is untileable even with unrestricted contacts.**

At beta120, P_beta=2exp(i60), rho60,p=cos(delta). The pair is exactly the independently reviewed periodic first curve. The negative result follows from a complete indexed-slot separation on an explicit linear angle envelope, followed by the exact nonlinear metric filter below. Both species frequencies remain free and omission is allowed in the negative certificates.

## Complete angle arrangement and its linear envelope

The earlier exact48 named angle-type inventory has five identity star types and14 extra star equations in(delta,beta,rho), after removing delta0. All14 are retained, even where some coincide or have no solution on the nonlinear metric slice:

    beta=120,120±2delta;
    rho=60+k delta, k=-2,0,1,2,4;
    rho+beta=180+k delta, k=-2,0,1,2,4;
    2rho+beta=240+2delta.

Use the full strict linear angle envelope

    0<delta<30, 0<beta<180, 0<rho<90, rho+beta>120+delta.

It includes all actual metric points, and may include points that fail rho=arg(P_beta) or p unequal to1. SAT in this envelope is only a necessary balance outcome and never a tiling claim.

Represent an affine equation by its coefficient row in the coordinate order(constant,delta,beta,rho). Enumerate every subset of size0,1,2 or3 of the14 rows, retaining all470 raw generator subsets. For a consistent subset, take its rational row space inQ^4 as the canonical flat description. All52 distinct consistent flats are retained, with every generating subset. A subset is inconsistent if its augmented rank exceeds its variable-coefficient rank.

For each flat, the active equation set is **all** of the14 rows in that row space. Its stratum means the flat minus all remaining nonactive hyperplanes, intersected with the strict linear envelope. Genericity here is only a definition of its complete active set; no actual geometry is assumed.

Four flats do not meet the strict envelope; their exact bases/generator subsets are retained. The48 remaining flats have a nonempty relative-open envelope intersection. Excluding finitely many hyperplanes that do not contain the flat cannot remove that open intersection. A retained rational envelope sample proves only linear feasibility and may lie on extra nonactive hyperplanes; it is not asserted to be a generic sample or metric placement.

Every actual metric point belongs to exactly one such full-active stratum. Indeed take all14 equations vanishing at it; their affine row rank is at most3 for a consistent point, so a basis of at most3 rows occurs among the470 generators. Every row in its span also vanishes at the point, so the canonical closure recovers exactly the complete active set. Thus no intersection can acquire extra stars outside the enumerated strata.

## Full native-star and seam system on each stratum

Retain all12 indexed native corners: the three A_H slots, three A_L slots, and all six B slots. Their exact affine angle vectors are fixed by the displayed native angles. Enumerate every multiset of three indexed corners. It sums360 throughout a stratum exactly when its angle-sum-minus360 row is in the flat's row space. If another such equality holds only on a smaller intersection, that point belongs to the separate smaller stratum and is not silently covered by the larger generic star set.

For each legal multiset enumerate every permutation and every reflection choice. Keep precisely the cyclic binary side-label matches, identifying only cyclic rotations of the whole star. Include all legal homogeneous ppp/qqq stars. Thus every actual oriented star at a point of that stratum is included. No A/B frequency ratio or mirror restriction is inserted.

For a whole shared seam use the reviewed indexed slot-pair/xor-parity signed potential. Its sign is+ at reference endpoint0 of the smaller typed slot and- at endpoint1. Both endpoint flags reverse at the other end, so it cancels. If the two typed slots coincide and parity1, the feature is0 because no occurrence is distinguished; all other keys have the unambiguous sign. These definitions are used to retain every star's12 corner counts and full signed seam vector.

For each stratum solve the exact necessary system

    sum_t C_t X_t = F_A M_A + F_B M_B,
    sum_t S_t X_t = 0,
    X_t>=0, F_A>=0, F_B>=0, F_A+F_B=1.

All48 feasible-envelope strata finish: **34 UNSAT with retained rational strong duals,14 SAT with retained rational primals,0 UNKNOWN.** A secondary mixed-species test happens to produce F_A=F_B=1/2 for all14 SAT records; that equality is an outcome, never a constraint.

Each of the34 strong duals is checked in exact Fraction arithmetic:

    W dot C_t+Y dot S_t>=0 for every retained star,
    W dot M_A<=-1 and W dot M_B<=-1.

Each retained SAT primal is also checked exactly against every corner and seam equation. The producer imposes a10-second timeout for each primary and dual solve; UNKNOWN would be recorded explicitly. None occurs. The decision used for rejection is the exact verified rational functional, not a solver status alone.

These strong duals exclude all actual metric tilings whose complete active set is one of the34 rejected strata. The infinite proof is the reviewed square-boundary mechanism: after passing to an actual trivalent edge-to-edge limit, selected tile W-charge is at most-N; complete stars have nonnegative augmented charge; every interior seam cancels; onlyO(R) boundary stars/seams remain. This contradicts N=Omega(R^2). No existence of frequencies or translation invariance is needed, and omission of either species cannot evade the negative per-tile charges.

## Complete exact nonlinear filter of the14 feasible records

Every one of the14 SAT flat bases implies at least one of

    beta120,    rho60,    rho+beta180.

The metric-filter certificate checks row-space membership of these three fixed rows for every retained SAT record. Each condition collapses to beta120 on the actual strict metric domain:

1. **beta120.** Directly P_beta=2exp(i60), so rho60 and p=cos(delta).
2. **rho60.** Multiplying P_beta by exp(i120) gives imaginary part sin120-sin(beta). With beta in(0,180), the branches are beta120 or beta60. At beta60,P_beta=exp(i60),rho60, and B's mixed angle m3=180+delta exceeds180. The latter branch is outside the strict convex domain; it is explicitly retained and rejected, not omitted from the trigonometric factorization.
3. **rho+beta180.** The imaginary part of exp(i beta)P_beta is sin(beta)-sin(beta-120)-sin120. Let u=tan(120/2)=sqrt3>0 and v=tan(beta/2)>0. This equals

       4uv(u-v)/[(1+u^2)(1+v^2)].

   Its only allowed zero is v=u, so beta120. There are no denominator poles: beta strictly lies in(0,180), v is positive finite, and the denominator is strictly positive.

For completeness the same numerator in case2 is

    sin120-sin(beta) = 2(u-v)(1-uv)/[(1+u^2)(1+v^2)],

giving explicitly v=u or v=1/u, the120/60 branches. P_beta never vanishes anywhere in the stipulated beta interval, so defining rho introduces no omitted zero-chain denominator root.

At beta120,rho60 and delta>0 the exact active14-equation set is indices[1,6,9] in the retained ordering, corresponding precisely to the three equations above. No other equation vanishes because each reduces to a nonzero multiple ofdelta. This is stratum33. It is the **only** retained SAT stratum that can contain an actual metric point. Larger SAT flats such as rho60 alone are not additional metric possibilities: their generic strata exclude the other two equations that actual geometry forces. SAT intersection flats imposing rho60±k delta also collapse to delta0 and are inadmissible. The filter compares complete active sets, not just intersection with the underlying flat.

The surviving whole delta interval beta120 is the actual periodic first curve, with its already reviewed side-pair quotient and flat-cover proof. This establishes both directions of the theorem. No new finite quotient search is needed.

## Stable retained artifacts and fresh-review scope

- `research/searches/branching-hexagon-two-run-single-120-strata-slot-balance.py`;
- `research/certificates/branching-hexagon-two-run-single-120-strata-slot-balance.json`;
- `research/searches/branching-hexagon-two-run-single-120-strata-metric-filter.py`;
- `research/certificates/branching-hexagon-two-run-single-120-strata-metric-filter.json`.

Both producers replay read-only by default; explicit`--output` is required to retain data. The full470 generator domain,52 consistent flats,4 infeasible-envelope flats,48 retained strata, all34 duals,14 primals and14 metric filters are preserved. The angle model imports the separate authoring48-type inventory to define coefficients; an independent verifier must reconstruct them without producer imports. Its linear-envelope model does not impose the nonlinear phase equation; that requirement is handled separately and exactly.

Dependencies: reviewed defect-free trivalent limit and signed-seam boundary invariant; separately reviewed single120 five-type obstruction and periodic first curve. Fresh review must independently reconstruct all470 flats, strict-domain feasibility, all native oriented star/seam vectors, every34 dual/14 primal and the generic-active-set metric filtering, as well as the stated exact domain. This specified resonance slice has received fresh independent VALID review; the remaining homogeneous resonance strata and unrestricted target remain unresolved.
