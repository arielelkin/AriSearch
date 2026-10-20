# Independent hostile review: Method 3 external incidence

Date: 2026-10-19. Verdict: PASS for the stated local algebraic ambiguity; no global extension conclusion.

Reviewed `research/lemmas/sugimoto-method3-external-incidence-gate-2026-10-19.md`, its exact verifier, and the imported t=3/5 coordinate fixture. No blocking mathematical defect was found in the local certificate.

## Independently checked geometry

The fixture closes after its fourteen unit edges. Its actual coordinate differences equal the stated direction vectors. The resulting cyclic interior-angle word is exactly `270,120,90,120,270,120,90,240,90,240,90,120,180,120`. Thus the five 120-degree corners are precisely X2, X4, X6, X12, X14, and the four 90-degree corners are precisely X3, X7, X9, X11. The straight corner X13 cannot fit either missing sector. Each missing sector is too small to contain two incident parent sectors, since each parent sector is at least 90 degrees. This establishes the claimed single-corner domain under the stipulated exact notch-filling condition.

For every insertion I checked the coordinate equalities identifying the inserted outgoing unit ray with the seed incoming reverse ray, and the inserted incoming reverse ray with the seed outgoing unit ray. These checks use coordinates independently of the verifier's direction congruence assertion. Every transformation has determinant +1. None needs reflection. The five or four rigid transformations at each seed corner have distinct transformed ordered parent coordinates.

The rotations independently obtained are:

| Seed notch | Inserted corners | Rotations in degrees |
| --- | --- | --- |
| X8 | X2, X4, X6, X12, X14 | 30, 240, 270, 60, 0 |
| X10 | X2, X4, X6, X12, X14 | 60, 270, 300, 90, 30 |
| X1 | X3, X7, X9, X11 | 120, 0, 330, 300 |
| X5 | X3, X7, X9, X11 | 240, 120, 90, 60 |

## Independent whole-parent overlap test

The independent checker uses projection intervals onto edge normals from both convex polygons. It checks `max(P) <= min(Q)` or its reverse on each axis, allowing boundary contact but excluding overlap of interiors. This is independently implemented rather than calling the retained verifier's oriented-halfplane separator. All arithmetic is exact in Q(sqrt(3)).

All 450 pairs (25 convex-child pairs for each of 18 insertions) pass. The checker additionally verifies pairwise disjoint interiors of the original five children. The imported fixture verifies their strict convexity, incidences, and exact total parent area. Together with the explicit boundary dissection, these justify the whole-parent implication. No floating-point tolerance or raster evidence is used. Parent coordinates contain no t, so using t=3/5 for this decomposition does not restrict the parent-placement result.

Reproducible independent checker:

```text
mise exec -- conda run --no-capture-output -n arisearch python research/reviews/sugimoto-method3-external-incidence-independent-sat-2026-10-19.py
```

Observed final line: `INDEPENDENT PASS: all 18, 450 convex-pair SAT checks`.

## Limits and interpretation

These are 18 admissible inserted parents counted over four specified seed notches. They are not a claim of 18 globally different rigid transformations across all seed notches, a complete catalog including reflected insertions, or infinitely extendible source states. Proper rotations already suffice to demonstrate the advertised local ambiguity; permitting reflected parents cannot invalidate those witnesses. Distinct parent corners may select congruent child shapes while giving distinct incident placements.

The note explicitly reserves the chiral extension/collar gate. Its deterministic-continuation conclusion should continue to be read as lack of a uniquely forced continuation from the certified single-parent local data. The successful tests do not refute determinism after imposing additional global source constraints, and do not establish failed global holonomy. No discovery log was changed.
