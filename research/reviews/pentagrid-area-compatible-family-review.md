# Fresh audit of the exact area-compatible U/V family

Reviewer: root,2026-10-10. The metric agent developed this family; root
independently audited it. **Verdict: valid** for every real b,c>0, with mixed
whole-plane tilability and aperiodic forcing unresolved.

The [family record](../searches/pentagrid-golden-metric-area-compatible.md)
defines exact directions and positive linear lengths. The
[independent checker](verify_pentagrid_area_family_independent.py) imports
no search implementation. It reconstructs an exact tenth root, uses real
algebraic coordinate pairs, and compares all four vertex bases and all30
support coefficient pairs against the certificate. Closure holds separately
for both parameter bases. Every side and supporting cross product has
nonnegative b,c coefficients with positive sum. Thus strict global convexity
holds for all positive parameters, including real lengths outside Q(sqrt5).
This is a positive coefficient proof, not sampling.

The independent shoelace calculation gives U normalized area coefficients
phi^3,2phi^2,phi^2/2 and V coefficients phi times these. The area ratio is
correct. No geometric subdivision or hierarchy follows from that identity.
Angle words give distinct congruence classes. Under the separately reviewed,
explicitly imported Rao classification, U is monohedrally untileable;
V's after-side gates both require b=phi*(b+c), impossible for positive
parameters. This conditional individual exclusion applies to the full family.

All three count-matrix powers agree with exact area conservation. The
reviewed minimum-six theorem excludes phi and phi^2 substitutions. No valid
larger macrogeometry is inferred. The checker reconstructs both b=c=1 and
b=1,c=sqrt2 exact examples and all support inequalities; these illustrate
the proved parameter domain, not plane existence.

Attacks checked: wrong embedding, closure at only one parameter, local
turns substituted for global support, vanishing support at positive b,c,
wrong sine normalization, mirror gate indexing, and ambiguous area counts.
No substantive defect or repair was needed. With assertions enabled:

```text
conda run --no-capture-output -n arisearch python research/reviews/verify_pentagrid_area_family_independent.py
```

The checker passes30 support pairs, four vertex bases, three area coefficient
identities and three matrix powers. The subsequently proposed six/seven
macrodivision is separately falsified by its boundary length field. This
review certifies the exact family, not an aperiodic pair.
