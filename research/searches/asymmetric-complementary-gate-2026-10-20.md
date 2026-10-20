# First exact gate: asymmetric complementary-corner P5/P5 split

Date: 2026-10-20. **Status: one exact positive metric passes local construction, but fails the endpoint forcing gate.** This checks the first proposal in [Astra's independent assessment](astra-shape-first-assessment-2026-10-20-1259.md). It does not classify every metric with these angle words, prove a plane tiling, or establish aperiodicity.

Replay:

```sh
mise exec -- conda run --no-capture-output -n arisearch python research/searches/asymmetric-complementary-gate-2026-10-20.py
```

## Exact metric and deduplication

Take angle words `P=(80,110,100,120,130)` and `Q=(60,100,120,130,130)` degrees. These differ from the prior P5/P5 angle words and midpoint fixtures listed in the [deduplication audit](shape-first-dedup-audit-2026-10-20.md). The two complementary split corners are Q's native 60 and 120 corners; their incident host-side segments have unequal lengths 1 and 2. This is neither the preceding double-adjacent rational split nor the symmetric right/right midpoint contact.

Let `z=exp(i*pi/18)` with the positive-angle complex embedding and `e_d=z^d`. The successive edge-direction exponents are `P=(0,7,15,21,26)` and `Q=(0,8,14,19,24)`. Start each polygon at 0 and integrate its edge vectors. Set

```
P lengths = (3,3,p2,3,p4)
Q lengths = (1,2,q2,q3,23/10).
```

For complex vectors write `[u,v]=Im(conj(u)*v)`. Define

```
Wp = -3(e_0 + e_7 + e_21)
p2 = [Wp,e_26] / [e_15,e_26]
p4 = [e_15,Wp] / [e_15,e_26]
Wq = -(e_0 + 2e_8 + (23/10)e_24)
q2 = [Wq,e_19] / [e_14,e_19]
q3 = [e_14,Wq] / [e_14,e_19].
```

The formulas solve both vector closure equations exactly in `Q(zeta_36)`. Sage exact-algebraic evaluation gives `p2≈1.2527867482`, `p4≈1.9754832661`, `q2≈0.0733184031`, `q3≈0.1433083763`; all are strictly positive. All five exact turn signs for both shapes are positive. The polygons are distinct because their angle words differ. Against the repository's reviewed transcription of Rao's 15 convex-pentagon monohedral types, exact angle and exact algebraic length checks find no match for either fixed shape. Conditional on that imported classification, neither species tiles alone. This is the completed omission gate for this metric.

## Split patch and endpoint atlas

Use P native side 3, length 3, from its 120-degree vertex `A` to its 130-degree vertex `B`. For split order 0, place Q side 0 of length 1 on `A-M` with its 60 corner at M, and Q side 1 of length 2 on `M-B` with its 120 corner at M. Order 1 reverses the lengths. Both orderings have exactly one tested nonoverlapping reflection parity pair in the four-parity prescription. The residual Q rays at M coincide in direction but have unequal native lengths. The exact convex separating-axis check verifies the P/Q/Q interiors disjoint; the 60+120 corners fill the exterior flat angle.

At A, the P120 and Q100 corners leave 140 degrees. The full-corner completion uses P80 and Q60 in either radial order. At B, P130 and Q100 leave 130 degrees; P130, Q130 native vertex 3, and Q130 native vertex 4 are candidate corners. The script places each actual polygon corner by an exact isometry on the two remaining rays, includes both reflections, checks ray directions, and rejects interior overlaps. **Both host endpoints can be completed simultaneously** for either split order. The finite records include duplicate geometric placements caused by equivalent side/reflection encodings; existence, not their raw count, is the conclusion. A side-interior flat 180-degree sector cannot be added at either endpoint because each residual angle is less than 180.

For a P/P whole-host alternative using the *same native side 3* of the second P, both isolated seams are legal. A mirror seam leaves angular gaps 120 at A and 100 at B. Exact nonoverlapping simultaneous completions exist: P120 or Q120 (also two Q60) at A, and P100 or Q100 at B. A halfturn seam leaves 110 at each endpoint; two P110 corners complete them simultaneously. Thus the intended asymmetric split and **both** P/P host identifications survive the endpoint test for this exact metric, including reflected assemblies and partial native-side lengths along the outgoing rays.

This fixed metric has no endpoint exclusion or demonstrated successor rule, so it is stopped before corona growth or a mixed periodic quotient. A different metric with the same words remains unclassified. Reopening the words requires a specific metric relation that removes the competing completed P/P endpoint assemblies and an explicit propagation mechanism; a larger patch of the displayed metric alone does not supply that.
