# Fresh hostile review: five-plus-one B saturated-chain reduction

Date:2026-10-13. Reviewer:luna, independent of terra construction/reduction.
**Verdict: VALID for the stated angle family, actual polygons and two-word exclusion.** The nine surviving words remain necessary candidates, not proved tilable or periodic.

## Claim and hypotheses reviewed

Reviewed [the reduction](../lemmas/terra-five-one-b-saturated-chain-reduction.md) and its [exact palette checker](verify_terra_five_one_b_chain_palette.py). For112.5<x<126, x!=120, actual convex A has two each of x,y=720-5x,z=4x-360; actual convex B has five r=360-2x and one s=10x-1080. Original tilings allow rotations, reflections, partial contacts and omission. The reviewed unrestricted whole-side/trivalent hexagon limit was checked for applicability, not redundantly re-audited.

The claim is: an admitted tiling has an admitted defect-free translated limit in which every remaining B has BB-degree2; if B disappears the pair has a monohedral A periodic escape. A001221 andA011022 cannot support the saturated mixed limit and consequently have such an escape at all actual metrics. No chain periodicity theorem is claimed for the other nine words.

## Exact angle language

All five angles are strictly between0 and180 on the stated open interval. In particular s>45 ands<180; y>90, z>90, r>108. The displayed slopes1,-5,4,-2,10 are distinct and every angle equals120 atx=120, so all five values are distinct away from120. A angles sum720 and5r+s=720.

Each triple sum equals360 atx=120. Thus a nonidentity triple equation can have no root other than120: if its slope were0, its constant would already be360 and it would be an identity. Independently checking the slope equations for all35 unordered triples leaves only(x,x,r),(x,y,z),(y,y,s),(z,r,r). Hence the four-star list is complete for trivalent fields, including irrational x and all actual side metrics. There is no BBB star. Partial or higher-valence original contacts are addressed by the preceding defect-free-limit theorem, not by assigning these four stars to the original tiling.

## Native BB indexing and capacity

With special B corner0=s and native sidei joining cornersi,i+1, sides0 and5 touch s and cannot be BB. Eligible native sides are exactly1,2,3,4. Two adjacent BB sides would put three B tiles at their common vertex, requiring a forbidden BBB star. The largest nonadjacent subset has size2, with native masks{1,3},{1,4},{2,4}.

The alternative masks{0,2},{0,3},{1,3} are labels within the four-edge eligible path after subtracting1; in particular eligible-path{0,3} is native{1,4}. Native side0 is NOT eligible under special-corner0 indexing. The artifact and checker consistently use the correct native convention. Reflection about corner0 exchanges native{1,3} with{2,4} and preserves{1,4}; arbitrary rotations transport the special-corner index. No untested reflected mask is missing.

For genuine convex disjoint tile copies, one neighbor cannot share two different noncollinear native sides: their convex intersection would contain positive area. Thus BB-side degree agrees with the number of B neighbors, and the eventual degree2 adjacency graph has no hidden parallel-edge interpretation.

## Uniform deficiency count

Native A0/A1 counting gives2NA=2Y0+U+O(R) and2NA=2Y1+U+O(R), hence Y0-Y1=O(R). The one s corner per B occurs only at AAB1, yieldingY1=NB+O(R). The five r corners give5NB=Y0+2Z+O(R).

The factor inZ=sum d_B+O(R) is correct. Every ABB2 star is an endpoint of its unique BB seam, and each BB seam has two endpoints. Separately, summing BB degrees over its two B endpoints counts each seam twice. The two factors therefore agree. Converting tile-centroid and star windows affects only native incidences in a fixed-width boundary strip. Fixed shape diameters, positive inradii and native corner counts give uniform O(R) errors for every translated square.

WritingD=sum(2-d_B), local capacity makesD nonnegative. ThenZ=2NB-D+O(R), so5NB=Y0+4NB-2D+O(R), orY0=NB+2D+O(R). CompareY0=Y1+O(R)=NB+O(R) to obtainD=O(R). No species frequency, positive B density or ergodic assumption is used. Each degree0/1 B has positive integer deficiency, giving a uniform linear count bound for their centroids.

## Clean translated limit and omission

For fixed L, quadratically many disjoint candidate disks in a sufficiently large square outnumber the O(R) deficient B centroids. A clean radiusL+D disk contains no such centroid; its radiusL interior consequently meets no deficient B tile. This argument remains valid when B is sparse or absent.

Translate clean disks of increasing radius and take indexed placement compactness. The reviewed uniform native-vertex separation preserves whole matching sides, trivalence and native labels. A B tile and its bounded-distance neighbors in the limit persist in the approximants, so it retains exactly two B neighbors. This does not assert deficient tiles never occur in the original field.

The limit may omit B. Then the surviving A tiles give a monohedral plane tiling, and the named unrestricted convex-hexagon theorem supplies a periodic omission escape. A pure B trivalent limit would require a BBB star and is impossible. If both types remain, the B adjacency graph is a disjoint union of finite cycles or bi-infinite chains, since it is a locally finite simple graph of degree2. This graph statement alone proves neither existence of a particular chain carrier nor periodicity of the final plane tiling.

## Palettes, all11 words and finite tuple count

At B corner0 the A color is1. At an r corner incident to a BB side it is2; at the remaining r corner it is0. Therefore the AB-side unordered endpoint demands are independently recovered as follows:

* native{1,3}/{2,4}:22,02,01,12;
* native{1,4}:02 and12, each occurring twice.

Whole AB seams must match these endpoint colors before side lengths are considered. Length coincidences cannot supply a missing native color pair because the angle values are distinct. A001221 lacks02 andA011022 lacks12, so neither can support any saturated mask. Their originally admitted tilings therefore produce a pure A clean limit and periodic escape. The seven single-mask and two three-mask survivors listed in the artifact are exactly the remaining nine of all11 fixed-color bracelets.

The prior complementary two-of-each B colour-permutation orbit theorem cannot be imported here: B's changed5+1 multiplicities distinguish the colors. The new checker correctly tests every fixed-color bracelet directly.

For every AB side, each matching native A side gives one placement when endpoint colors differ, or two when they agree. The actual inward half-plane fixes the direct/reflected placement once endpoint identification is chosen. Multiplying the four independent AB-side option counts and retaining all12 indexed B placements gives1392 partial tuples. This count is a complete necessary finite domain before metrics; it is not1392 actual geometric modules or full-plane extensions.

The checker was executed: PASS35 triple types, four identities, three masks, all11 palettes, nine survivors and1392 partial AB tuples.

## Closure gate and exact non-consequences

With B side0 along1 andR=180-r=2x-180, directions are exp(ijR). For masks{1,3}/{2,4}, the two BB-column separation is2R in(90,144), so its determinant is nonzero. For{1,4} it is3R in(135,216); its only possible180-degree value isR=60, orx=120, excluded. Thus actual closure uniquely determines the two BB lengths from four AB lengths. Positive lengths and polygon geometry must still be checked; the existence of an invertible linear system is not an existence theorem.

No consequential defect was found. The exact native-index distinction was checked explicitly; no repair to the artifact/checker is required. Fresh hostile review of subsequent BB-partner placements, geometric fans, infinite chains or periodic extensions will be needed if constructed. Final verdict: **VALID on the stated reduction/two-word-exclusion scope**, with the nine remaining native words open.
