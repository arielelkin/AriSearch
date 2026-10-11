# Exact two-obtuse-angle pentagon classification

**Date:** 2026-10-09. **Status:** complete exact finite enumeration; independent checker passed. Mathematical hostile review requested.

**Question:** If all angles are among alpha < beta in (pi/2,pi), and a trivalent plane tiling contains a pentagon, what angle signatures are compatible with its angle sum and a single vertex multiset?

**Finite domain:** p in {1,2}, k in {0,...,5}: twelve angle rows. For each surviving rational angle pair, enumerate n in {5,...,10} and l in {0,...,n} for second-face angle counts. The analytic proof in [the lemma](../lemmas/two-obtuse-angle-pentagon-reduction.md) handles p=0,3 and proves the unbounded n-reduction; their omission is justified rather than assumed.

**Encoding and constraints:** x=alpha/pi, y=beta/pi are exact Fractions; k*x+(5-k)*y=3, p*x+(3-p)*y=2, 1/2<x<y<1; second-face equation l*x+(n-l)*y=n-2. Counts are unlabeled angle multiplicities. No equivalence/symmetry reduction other than ordering the two distinct values x<y is used. No solver or stochastic seed.

**Environment:** Conda arisearch, Python 3.12.13, Linux x86_64; Python standard-library fractions/json only. No configured timeout or memory cap. Both generator and independent checker completed, exit status 0. Retained certificate is [two_obtuse_angle_pentagon.json](../certificates/two_obtuse_angle_pentagon.json).

**Replay:**

```text
conda run --no-capture-output -n arisearch python3 research/searches/two_obtuse_angle_pentagon.py
conda run --no-capture-output -n arisearch python3 research/reviews/verify_two_obtuse_angle_pentagon.py
```

The generator writes JSON to stdout. Do not overwrite the retained certificate during replay. The independent checker verifies every row by integer cross-products and compares the surviving table against separately stated exact values. It enumerates all second-face count pairs in the bounded domain independently of the generator's linear solve. It does not verify plane tilability, side-length closure, or periodicity.

**Result and non-consequences:** exactly three angle signatures survive the twelve algebraic rows. The accompanying proof eliminates the odd-face n=10 case, all n=5 cases, and all n=6 aperiodic cases (the last relying on the named external monohedral hexagon theorem). Four angle signatures remain as necessary candidates, without exact polygons or an existence proof. No aperiodicity or general impossibility result follows.
