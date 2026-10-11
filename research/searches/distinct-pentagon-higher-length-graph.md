# Exact distinct-length all-obtuse (5,n) classification

**Date:** 2026-10-09. **Status:** complete finite domain, independently verified; fresh mathematical hostile review requested. This supports [the restricted theorem](../lemmas/distinct-length-obtuse-pentagon-higher.md).

**Question:** what internally distinct P=C5/Q=Cn length cycles, n>=7, can cover every corner by a trivalent angle-legal star, and do these force a periodic witness or contradiction under strictly obtuse angles?

**Analytic domain bound:** private symbols must have two shared neighbours and an opposite-cycle shortcut. Thus they are isolated; k<=5 common symbols implies n-k<=floor(n/2), so n<=10. Hence n=7,...,10 and max(3,ceil(n/2))<=k<=5 are complete for the unrestricted side count under the metric hypotheses.

**Generator finite domain:** P=(0,1,2,3,4); choose its k shared symbols, every common cyclic order in Q, and n-k isolated private insertions. Private labels canonicalized by first occurrence; Q cyclic rotation and reversal quotiented; no geometric symmetry assumption. Exactly 387 normalized candidate words, yielding 21 graph survivors. Under dihedral relabelings of P there are five classes. The original graph-only certificate was expanded in place to retain actual corner-typed stars, orbit representatives, and ring choices before promoting the theorem; no discarded result is used as evidence.

**Independent domain:** all common/private interleavings, allowing adjacent private labels. Exactly 3,777 normalized words. Triangle-cover survivors match all 21 retained words. The verifier independently enumerates each four-common-symbol split and checks 20 actual four-face torus endpoint maps: 24 sides, 12 pairings, 8 three-corner vertices, connectedness, circular links as three sectors, orientation by boundary reversal. Its formal labels use a different offset from the generator.

**Angle audit:** all star subsets covering every actual corner, with polygon angle sums appended. There are 66 corner-covering supports across the retained words. Exact Fraction row-space calculation proves some ring angle equations for n=7, forces a P-corner to pi/2 for n=8, and an inconsistent constant equation for n=10. No n=9 survivor exists. Positivity constraints are not substituted for these equalities; the mathematical proof applies strictly obtuse angles to the forced right angle.

**Encoding:** integer side symbols, unordered corner edges retaining type occurrences, exact augmented rational linear equations. No numerical geometry, solver, randomized seed, imposed marking, or incomplete timeout result. Both source shapes' existing full side lengths and angles instantiate the quotient; metric closure is given by the assumed original polygons.

**Environment:** Linux x86_64, Conda arisearch, Python3.12.13, standard library only. No configured timeout or memory cap. Generator and checker completed with exit0. Generator stdout parsed equal to retained [main certificate](../certificates/distinct_pentagon_higher_length_graph.json). Exact independent [verification output](../certificates/distinct_pentagon_higher_verification.json) retained.

```text
conda run --no-capture-output -n arisearch python3 research/searches/distinct_pentagon_higher_length_graph.py
conda run --no-capture-output -n arisearch python3 research/reviews/verify_distinct_pentagon_higher.py
```

Keep assertions enabled. These commands print JSON; replay must compare parsed data to retained certificates without overwriting. The checker imports none of the generator. A first checker implementation blindly reversed Q for every orbit; an endpoint assertion failed on an already opposite projected cycle. It was corrected to choose Q's orientation from projected common-symbol order, as explicitly required by the mathematical proof. All maps then passed. This was a checker implementation error, not a theorem exception.

**Result/non-consequences:** all-obtuse internally-distinct (5,n),n>=7 pairs are untileable except possibly n=7, where tilability forces a periodic witness. This excludes only that metric family. Repeated lengths and nonobtuse angles remain outside the finite encoding and theorem. No original-problem resolution or universal priority assertion follows.
