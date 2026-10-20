# Independent hostile Sol review: two pure twelve-star orbits

Date: 2026-10-19. Reviewer: fresh independent Sol agent, not Astra. **Verdict: PASS**, with the explicitly imported defect-free limit and monohedral classification dependencies retained. No author lemma, producer, or certificate was edited.

Reviewed the two-orbit lemma, its producer and certificate, the native atlas builder and reviewed 180-row certificate, the fixed-native unrestricted-periodicity lemma and its hostile PASS review, the defect-limit re-review, and the classification attribution in the shared limit lemma.

## Independent finite reconstruction

Executed an independent inline Python reconstruction through `mise exec -- conda run --no-capture-output -n arisearch python`. It did not import the author producer or atlas builder. It constructed all ordered triples of the 24 signed native ports, allowing repeats, canonicalized only cyclic rotation, checked each adjacent incoming/outgoing native-side color, and repeatedly deleted triples lacking the reversed pair of remote endpoint ports on any seam. Side j has endpoints corners j-1 and j; handedness is retained at the remote endpoint. This independently verifies the critical seam rule, including reflection signs and pair reversal.

For both B=(0,0,2,1,1,3) and B=(0,1,0,2,1,3), all twelve rotations/reversed rotations were reconstructed. Each has precisely twelve fixed stars, four A-only and eight B-only, and covers all twelve native corner slots. Every reconstructed star set, initial count, and pruning history agrees exactly with the corresponding reviewed 180-row atlas entry. The two representative lists and histories also agree with the new certificate.

Each orbit has size twelve and their intersection is empty. Independently selecting all rows in the 180-row certificate with twelve fixed stars, full corner cover, and one formal corona gives exactly their 24-word union. Thus these are exactly the two claimed orbits within that stratum, without color permutation or changing A. The formal corona records agree with the reviewed atlas; the independent reconstruction here verifies stars and pruning, while the existing atlas review supplies the corona enumeration audit. The one-corona count is unnecessary for the purity obstruction.

The executed reconstruction exited zero and printed PASS for each twelve-word orbit and for equality with exactly 24 selected rows. This review did not rerun the author producer because that script rewrites its certificate; the independent reconstruction verified its finite claims directly.

## Geometric audit

Every actual trivalent edge-to-edge star is an initial compatible signed native triple. For each seam, its actual other endpoint witnesses the required reversed remote pair. Induction therefore retains every actual star in every pruning round, even with infinitely many absolute tile orientations. This proves that the fixed atlas is a necessary upper atlas; no claim of metric sufficiency is involved.

A full edge joining different species forces a mixed-species triple at each endpoint, contrary to the reconstructed purity. In a tiling by finitely many fixed compact polygons, positive minimum tile area and bounded diameter imply local finiteness. Between any two interior points a compact path can be perturbed off the finitely many nearby vertices and across edges transversely. It meets finitely many tiles and gives a sequence of full-edge neighbours. Consequently the full-edge adjacency graph is connected, and the absence of cross-species edges forces the entire trivalent edge-to-edge plane source to be monohedral. No assumption of positive species density or repetitivity is required.

## Unrestricted-contact transfer and omission

The defect-free limit theorem is explicitly imported with its reviewed uniform sector-disk separation repair. It applies to the same two fixed actual closed strictly convex hexagons, independently of native ordering, and yields an edge-to-edge everywhere-trivalent plane tiling. A species can disappear. The purity argument applies whether one or both species initially survive and forces the limit to contain a sole species.

The named imported Zhu–Wang–Yan monohedral convex-hexagon classification, as scoped in the shared lemma and existing structural/synthesis reviews, then supplies a periodic tiling by that sole occurring original polygon. This review accepts that classification as the declared external theorem; it does not claim to reprove it. Omission is expressly permitted, so this monohedral periodic tiling is an admitted periodic escape of the pair. Neither full twelve-corner cover of an actual monohedral source nor a mixed limit is assumed.

The statement correctly concerns existence of a periodic escape, not periodicity or edge-to-edge structure of the original unrestricted-contact tiling. It requires actual closed strictly convex metrics with five pairwise distinct positive native lengths. It neither realizes arbitrary formal words/coronas nor settles the general two-convex-polygon problem. The 32-star/100-corona orbit remains outside scope. Skipping support enumeration and metric construction is justified because a mixed trivalent source is already impossible.

**Final verdict: PASS** for finite purity, exact two-orbit identification, mixed-source impossibility, and the restricted unrestricted-contact periodic-escape implication with its named imported dependencies.
