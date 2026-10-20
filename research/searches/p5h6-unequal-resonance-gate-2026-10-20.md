# Unequal resonance P5/H6: exact local closure and competing host contacts

**Status: named split excluded from every plane tiling (2026-10-20).** This changed metric closes the compulsory second contact without equating P's two short sides, so it avoids the immediate Rao Type 2 omission that kills the `q=1/2` metric. An independent exact attack follows all eight F caps through their compulsory next P80 contacts and rules them out. Whole H0/H0 attachments and a single H3 cover are also excluded. Other multipiece H0 covers remain unclassified; no global untileability, plane extension, or periodicity conclusion follows.

## Exact shapes and omission gates

Use `K=Q(zeta_36)` in its standard complex embedding and `u(d)=zeta_36^(d/10)`. Fix `a=3/2`, `r=1/2`, `q=a-r=1`. P has directed edge angles `(0,50,150,200,280)` and lengths `(p,a,q,s,r)`, where `p,s` uniquely solve

`p u(0)+s u(200)=-a u(50)-q u(150)-r u(280)`.

Set `L=p+q`. H has directions `(0,50,100,180,230,280)` and lengths `(L,1,1,c,r,e)`, where `c,e` uniquely solve

`c u(180)+e u(280)=-L-u(50)-u(100)-r u(230)`.

The [exact Sage replay](p5h6-unequal-resonance-gate-2026-10-20.sage) proves both closures, positive side lengths, strict convexity and pairwise distinctness of the eight numerical lengths. Approximate values are `p=2.99292479285`, `s=3.38185574956`, `L=3.99292479285`, `c=4.38185574956`, `e=1.38893095672`. P angles are `(100,130,80,130,100)`; H angles are `(100,130,130,100,130,130)`.

All 15 stored Rao pentagon families and 10 dihedral relabelings give no P-only hit, conditional on the repository's reviewed transcription and the imported complete classification. H-only tilings are impossible directly: H angles exceed90, so a side-interior T-contact cannot be completed; every H 100-degree corner needs two H130 corners, and at H corner0 no pair of H130 numerical side pairs bridges its adjacent lengths `e` and `L`. This proves an H-only obstruction without a monohedral hexagon classification.

## Named P split and resonant second contact

Fix H above side0 `[0,L]`, with P side0 length `p` and P side2 length `q` below it in either order. The complete domain of two orders, two source-side directions per P and two reflection choices per P has `2×2^4=32` placements. Exactly two, one per order, have pairwise disjoint interiors. Both put P100 and P80 at the split, with coincident outgoing P4 length `r=1/2` and P1 length `a=3/2` rays.

At the endpoint of P4, the remaining long ray has length `a-r=q=1`. The vacant angle80 must be P vertex2. Its two incident-edge assignments, two boundary-ray assignments and two reflection choices give eight exact isometries; two pass ray and overlap checks in each split order. One continues with P side1 length `a=3/2` and overhangs the original side by `r=1/2`, producing a 130-degree vertex against a side interior and an unfillable 50-degree sector. The other continues with P side2 length `q=1` and ends **exactly** at the original P1 endpoint. Those two P130 corners leave a 100-degree sector. Among the four native 100-degree corner slots (P0, P4, H0, H3) and eight edge/ray/reflection maps per slot, eight distinct exact nonoverlapping full-corner images fill the 100-degree sector for each split order. The independent [restricted kill certificate](p5h6-resonant-escape-attack-2026-10-20.md) proves five fail at their next endpoint. The remaining three P images force another P80 corner on a straight side with remaining length `s-r`, `s-p`, or `p-r`. Exact inequalities are `s-r>3/2`, `0<s-p<1`, and `p-r>3/2`; P80's incident sides have lengths 1 and 3/2. Each choice puts a 130-degree far corner strictly inside the other tile's side, leaving an unfillable 50-degree sector. **All eight F caps fail, so neither order of the named P0+P2 split can occur in a complete plane tiling.** The eight placements are legal only as bounded first-corner patches.

## Whole H0/H0 first contacts and exclusion

Of the four full-side H/H source-direction/reflection placements, both the mirror and halfturn are two-tile nonoverlap contacts. For the halfturn, the two H0 endpoints each leave a 130-degree sector, with 12 legal P/H single-corner placements per endpoint among the six native 130-degree slots and their ray maps. For the mirror, the right endpoint leaves a 100-degree sector with eight legal single-corner placements. The left endpoint leaves160 degrees, requiring two P80 corners; four of the 16 incident-side/reflection pairs are nonoverlapping. The two pairs with unequal shared-ray side lengths create an unfillable 50-degree T sector at their next endpoint. The two equal-length pairs close at P130+P130 and each has eight nonoverlapping P/H 100-degree first-corner placements. These counts are strictly local. The separate [exact escape attack](p5h6-resonant-escape-attack-2026-10-20.md) follows compulsory endpoint contacts and proves that **both whole H0/H0 attachments are impossible in a complete tiling**, despite these legal first contacts. It also excludes a single H3 side covering H0. Arbitrary H0 partitions by multiple segments remain outside both audits.

A quick [2P+2H trivalent torus screen](p5h6-unequal-resonance-small-torus-2026-10-20.py) found no positive witness over eight reflection assignments. Its negative result is only a narrow finite observation: in fact no trivalent vertex can contain P's 80-degree corner, so this quotient model cannot represent a tiling using P. Four-valent vertices, partial contacts, other inventories and periodic carriers remain untested. The script retains the full eight-result [JSON](p5h6-unequal-resonance-small-torus-2026-10-20.json).

## Scope and comparison

The unequal resonance is distinct from the [q=1/2 Type 2 omission](p5h6-resonant-offset-gate-2026-10-20.md), the [nonresonant 50-degree obstruction](p5h6-offset-t-gate-2026-10-20.md), and the old equal-unit omission. The metric and contact topology also differ from prior P5/Q6 and P5/Q7 entries in the [repository deduplication audit](shape-first-dedup-audit-2026-10-20.md). This is not a literature novelty claim. The fixed metric is stopped because its named construction and whole-side H0 mechanisms fail, while arbitrary multipiece host covers lack a global extension or forcing mechanism.

```text
mise exec -- conda run --no-capture-output -n arisearch sage research/searches/p5h6-unequal-resonance-gate-2026-10-20.sage
mise exec -- conda run --no-capture-output -n arisearch python research/searches/p5h6-unequal-resonance-small-torus-2026-10-20.py
```
