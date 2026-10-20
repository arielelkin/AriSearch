# Hostile Sol review: open metric families

Date: 2026-10-19. Reviewer: Sol (not Astra).

**Verdict: PASS.** Reviewed `research/lemmas/hexagon-five-four-open-metric-families-sol-2026-10-19.md` and its shared replay producer. No author artifact edited.

The shared producer replay completed with exit 0 using the prescribed mise/conda command. In addition, independently entered the displayed matrix, exact length vector and both four-triple lists into a fresh Sage process without importing the producer or reading its certificate. Verified M l=0, the final-four-column determinant -1/4, coefficient and augmented ranks both 5, the equiangular point in each affine support, and exhaustive enumeration of all 364 triples returning exactly the displayed lists.

## Determinant and family dimension

The nonzero determinant establishes a unique normalized length solution near the fixture by an explicit analytic inverse. No implicit function theorem regularity condition is missing; the explicit inverse is stronger than necessary. The affine angle space has dimension 12-5=7. Restricting the analytic solution to a nonempty relative neighborhood in that space preserves all strict positivity, length distinctness and strict supporting halfplane inequalities checked at the base point. The polygon angles are recovered from the constructed side directions because exterior turns stay between zero and pi, total turn is 2pi, and strict supporting halfplanes ensure the intended simple convex polygon. Closure is imposed by the solve itself. Hence the resulting normalized metric graph has dimension seven, including realizable nonequiangular points. This argument does not claim a global parametrization of every feasible metric on the support.

## Generic exclusions

The equiangular point need not belong to the feasible neighborhood: membership in the affine space suffices to test whether an affine relation is an identity. At that point every angle is 2pi/3. A nonempty integer corner multiset cannot have sum pi identically; an identity with sum 2pi must have exactly three corners. Independent row-space enumeration verifies the only such triples are precisely the listed four for each support.

After restricting to angles greater than pi/3, a 2pi multiset has at most five entries and a pi multiset at most two. With twelve corner types this is a finite list, including repetitions. Each remaining relation defines a proper affine hyperplane or the empty set. A finite union of these cannot cover the nonempty relatively open feasible neighborhood, and its complement is open dense there. Thus the simultaneous exclusions, including all pi-sum multisets, are justified for actual metric pairs. No uncountable or countably infinite exclusion argument has been smuggled into the claim.

## Counts and periodicity boundary

In either four-triple system each native A corner occurs in exactly one triple and each native B corner occurs in exactly one triple. Each triple has an A corner, so its multiplicity equals the number of A faces. Each also has a B corner, so the same multiplicity equals the number of B faces. Thus the common number N gives V=4N, E=6N, F=2N and Euler characteristic zero, as claimed. This is a necessary count and does not assert existence of a torus carrier.

For edge-to-edge tilings, every local vertex equation is among the finite candidate multisets above, so the generic exclusion applies simultaneously to all finite torus carriers with a nonidentity vertex row. It does not eliminate carriers using only the four identities. A valid length-compatible orientable flat torus carrier would develop periodically, as established in the separate mask41032 proof; compatibility and nonsingular vertex links remain part of validity. The artifact expressly retains the separate obligations of establishing such a carrier for mask33416, or excluding all such carriers, and proving existence of a plane tiling. Its stated boundary is correct.

No blocking issue found.
