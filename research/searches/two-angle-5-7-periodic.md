# Exact periodic witness in the 4pi/7–5pi/7 pentagon–heptagon family

**Date:** 2026-10-09. **Status:** exact witness found and independently checked; fresh whole-claim review valid.

**Question:** does this two-angle multiplicity signature by itself force aperiodicity after both shapes are excluded from monohedral tilability?

**Exact object:** [counterexample definitions/proof](../counterexamples/two-angle-5-7-periodic-instance.md). Coordinates in the isolated 28th cyclotomic field are retained in [the coordinate certificate](../certificates/two_angle_5_7_periodic.json). This is a direct algebraic construction, not an exhaustive parameter search. Side lengths1,2,4,6 fixed to1; the remaining three solve exact H-closure and the selected P-seam direction. All values positive.

**Verification domain:** four placements (H,-H+d0,P,-P+c) modulo L=Zu+Zv. The checker computes their exact lattice-basis bounding boxes and every ordered-pair integer shift range that could even have box intersection. After excluding identical placement at zero shift, there are exactly34 cases. All pair domains are retained in [verification output](../certificates/two_angle_5_7_periodic_verification.json). All remaining lattice shifts have disjoint boxes by the analytic bound. Exact separating-axis inequalities prove no interior overlap; exact area equality and closed-union integration prove infinite coverage.

**Encoding:** rational coefficient lists modulo Phi28, with an exact rational isolating rectangle for its complex embedding. Sage QQ/NumberField/QQbar/AA arithmetic only; no float branches, solver or seed. Checker imports none of the generator and separately certifies root uniqueness, raw-coordinate reality, global convexity by supporting-side inequalities, halfturn congruences, rank-two lattice, cyclic angles, positive H lengths, overlap inequalities, and area equality.

**Environment/completion:** Conda arisearch, Python3.12.13, Sage10.9, Linux x86_64. No configured timeout or memory cap. Generator and independent checker completed exit0. The initial checker had P's beta corner indexed second; its exact angle assertion exposed the mismatch. It was corrected to beta first, with the multiset unchanged. A hostile reviewer required raw-coordinate reality and global convexity checks; these were added and independently rechecked before final valid verdict.

```text
conda run --no-capture-output -n arisearch python3 research/searches/two_angle_5_7_periodic_witness.py
conda run --no-capture-output -n arisearch python3 research/reviews/verify_two_angle_5_7_periodic.py
```

Both commands print certificates; compare parsed JSON to retained files and keep assertions enabled. Do not overwrite certificates on replay. [Fresh review](../reviews/two-angle-5-7-periodic-review.md) audits full-plane proof and metric checks.

**Result:** this exact pair has two independent periods although neither member tiles monohedrally. It is falsified as an aperiodic candidate. No claim about other metrics with the same angle signature or about the unrestricted problem follows.
