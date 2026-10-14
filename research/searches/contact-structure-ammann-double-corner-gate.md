# Ammann complete c-dimer two-corner replacement gate

Date: 2026-10-13; reviewed 2026-10-14. **Independently reviewed VALID for these fixed boundary gates and the 6/6 omission witness** ([review](../reviews/ammann-cross-source-resections-independent-review.md)). Scope is the fixed generic J0 source fixture and its four complete c-dimer corner-star patches.

This tests a changed replacement boundary after the single-corner triad fails: include BOTH exterior corner neighbors of the mandatory P1/P2 c-dimer. Using the exact definitions of contact-structure-ammann-corner-triad-gate.py, put A=ζ⁻²P1 and B=ζ⁻²P2. At their K endpoint choose H or P1 in its original canonical coordinates. At their L endpoint choose ζ⁻²+ζ⁻¹H or P2+(ζ⁻²−ζ²). These are exactly the two K-type and two L-type exterior-neighbor alternatives in the reviewed source atlas. Thus all four contact schemes are retained; no sampling or patch-size sweep selects a favorable branch.

The exact four-source patches have pairwise disjoint convex interiors and simple nonflat outer boundaries. The standalone checker cancels every reversed internal edge, traces the complete outer boundary, and classifies every turn using exact QQbar signs. Results by (K,L) exterior species are:

| exterior species | outer sides | reflex corners | forced binary side counts |
|---|---:|---:|---|
| H,H |12|3 noncollinear| impossible |
| H,P2 |11|2|6,7|
| P1,H |11|3 noncollinear| impossible |
| P1,P2 |10|2|6,6|

Two convex polygons with disjoint interiors have a straight common seam. Every reflex boundary corner must be on that seam. Three noncollinear reflex corners therefore prohibit a two-convex-piece partition. In each remaining patch the seam is forced between the two reflex corners; their cyclic boundary distances are exactly 5/6 or 5/5. These give at most the listed six/seven side counts, with no hidden inserted boundary vertices in a genuine polygon. Here all consecutive outer turns are nonzero; the checker retains their exact values. In particular, on each forced half-boundary all five or six inherited outer vertices remain genuine, and the seam endpoints have convex nonflat angles whenever that half is convex. No five-sided output is possible: if an endpoint becomes flat it must lie on the line of its adjacent old outer edge, whereas the checked reflex-to-reflex chord has nonzero cross product with every incident outer edge (this endpoint check is included).

Consequently this entire four-choice whole c-dimer corner replacement cannot supply a pentagon among exactly two convex output pieces. The statement does not assume these patches globally partition a source tiling, nor classify larger or fractional boundary schemes. It is a local decisive construction gate for a genuinely changed cross-source boundary mechanism.

## Original target scope and retained 6/6 escape

The absence of a pentagon only fails the construction preference, not the original unrestricted target, which permits two hexagons. The two exact strict-convex 6/6 outputs are now separately retained and checked by contact-structure-ammann-double-corner-six-six-escape.py. Its second hexagon has opposite edges e0=−e3 (indeed this follows symbolically from L−1+ζ⁻²J′=0). Rotating indices gives e2=−e5 and the explicit two-copy Q-only carrier printed by the producer. The exact producer checks all twelve endpoint identities and positive area/covolume, and prints both original hexagons and the complete omission witness in exact tenth-cyclotomic coordinates. The independent checker verifies every possibly overlapping lattice translate from exact lattice-coordinate bounding boxes, then proves full coverage using motif area=covolume and closed local finiteness. Thus THIS 6/6 pair is excluded by an actual periodic monohedral escape, not its side counts. The 6/7 branch’s tileability has not been classified. Any admissible convex realization nevertheless has exactly six/seven genuine sides and is excluded from aperiodicity by the reviewed [hexagon/higher-side theorem](../lemmas/hexagon-limit-and-periodicity.md), with its named imported unrestricted hexagon classification. Thus all four fixed double-corner replacement schemes are closed for the original target: two fail binary convex partition, the 6/7 branch fails the higher-side theorem, and the 6/6 branch has the explicit periodic omission escape.
