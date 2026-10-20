# Independent Sol hostile review: five residual ETE chain escape

Date: 2026-10-19. Reviewer: fresh independent Sol reviewer; no author edits.

**Verdict: VALID for the stated conditional rank-one periodic escape, importing the named reviewed defect-free limit and monohedral classification. No substantive defect found.**

The reviewed statement concerns precisely zero-based rows 15,16,23,26,31. It proves that plane tileability implies existence of some tiling with a nonzero translation. It establishes neither plane tileability nor rank-two periodicity nor periodicity of an arbitrary original tiling.

## Material read and computational checks

Read the submitted ETE-chain proof, native atlas producer and endpoint checker, exact residual-corona producer, retained certificates, translation-strip lemma, old private-AA chain theorem and hostile review, defect-free limit and uniform-density lemmas, and the retained monohedral omissions review. Dependencies on the external unrestricted monohedral classification remain imported mathematical dependencies.

Read-only verification performed through the required mise/conda wrapper:

* Ran `research/searches/hexagon-five-four-forced-dimer-check-2026-10-19.py`: PASS.
* Regenerated the complete atlas for B=(0,1,1,0,2,3) from the producer and compared every field to the retained row: identical, 22 fixed stars and seven boundary cycles.
* Replayed the residual-corona producer in memory with its certificate-write statement replaced by an equality assertion against the existing JSON: all 35 results exactly matched; corona6 alone survives in every row.
* Independently checked the retained corona6 A-placement matrices and translations over Q(sqrt(3)): the root A3 neighbor is x -> p3+p4-x, the mate A3 neighbor is x -> x+p5+p0-p3-p4, and the chain translation is nonzero in all five metrics. The latter matrix is +I in the root frame because it is the composition of two halfturns; it is a halfturn relative to the mate frame.

No author proof or certificate was modified.

## Atlas necessity, reflections, and uniqueness

The central completeness passage is valid. Native corner j has side arms j,j+1; in Euclidean vertex coordinates it is vertex p(j+1). The producer stores both handednesses and allows repeated corner ports, so it does not silently discard repeated native slots or copies of the same species. A genuine trivalent star is an initial signed cyclic triple. Reversing a shared edge exchanges its endpoint corner labels and reverses the cyclic pair, exactly as implemented by `far` and `needs`. The actual opposite endpoint star supplies each pruning witness at every iteration. Therefore every actual star survives the fixed point.

Side5 is private and unique in A. Reflecting across it would require a third (3,3) corner at one endpoint, absent in both words. Thus its mate is the same-slot midpoint halfturn, with the same handedness. Normalize any chosen A, including a reflected occurrence, by an arbitrary Euclidean isometry to positive reference A. Its halfturned mate is then positive too.

The dimer boundary is p0,...,p4 followed by the corresponding five mate vertices. Its ordinary vertices are precisely positive native corners0,...,3, which supply factors1,...,4. At each seam endpoint the two dimer sectors are the positive corners4,5 in the producer order; factor0 records the remaining single exterior tile across both boundary edges. Hence the real boundary reads `factors+factors` and closes. Equality of edge states retains the exterior native side and handedness across both endpoints. Every real dimer corona therefore appears among the seven cycles, even if an exterior tile occurs on multiple edges. The enumeration need not enforce every nonlocal tile identification to remain a necessary upper atlas.

The metric rejection tests are necessary for an actual ETE corona. At a seam junction the single third tile must be the same Euclidean polygon on both incident edges. Distinct actual tiles cannot overlap in their interiors. Every dimer-boundary star is completely represented by incident boundary neighbors, so its angle sum must be360. In particular a missing fourth tile cannot repair a rejected ordinary vertex in an everywhere-trivalent source. Exact replay confirms six rejections and one survivor in each metric. Thus corona6 is forced at EVERY actual A; the argument does not select a favorable finite patch or assume its extension. Reflection normalization makes this conclusion universal for both host handednesses.

## The repeated A side and the old theorem

A has repeated color0 at slots0 and3; slot3 is not private. The old theorem cannot be applied directly: its six-distinct and two-private hypotheses fail. Its original private-side reflection obstruction would also not establish the new A3 seam.

The submitted proof correctly supplies a replacement: the complete necessary atlas and exact corona elimination force slot3 to meet slot3 by a midpoint halfturn, independently of privateness. Slot5 retains its direct private reflection obstruction. Subsequent chain and filling arguments use only these two forced same-slot involutions, convexity, bounded geometry, and absence of a B-only plane tiling. None uses the distinctness of the remaining A sides. Thus the repeated slot does not invalidate the imported geometric argument.

## Proper chains and complementary bands

The retained contact graph really has degree two: equality of its two neighbors would make compact A invariant under the nonzero product translation. Alternating the same-slot involutions gives a bi-infinite two-tile periodic chain. Its anchor is interior because it is the midpoint of a chord between two distinct side midpoints of a strictly convex polygon. The anchor-to-seam arcs have interiors strictly inside their tiles; seam midpoints have neighborhoods covered by their two chain tiles. They form embedded proper separators, disjoint between components. Repetition bounds distance from the period axis uniformly.

Disjoint proper separators with nonparallel strip axes would have to intersect by Jordan separation. All axes are parallel and all two-step period lengths equal |v|, so one common vector T preserves every chain, every A tile, and every separator. This conclusion concerns only the A carrier.

Disk-packing local finiteness descends to the cylinder modulo T. Its disjoint essential circles have a locally finite linear order. No extreme circle can occur: all A would then lie a bounded distance to one side, leaving arbitrarily large A-free disks. This contradicts compactness-derived uniform A occurrence when B cannot tile alone. Between consecutive separators no third-chain A can enter: its connected interior path to its own separator would cross a boundary curve inside another A carrier. Boundary-chain A lies within a diameter of its separator. Consequently excessive axis separation produces a radius-L A-free disk, yielding the claimed uniform band-width bound. Polygonal overhangs do not change this argument.

## Finite placements, SFT, and infinitely many bands

Every original B belongs wholly to one separator band. Its bounded transverse distance to the lower chain, together with the two-tile horizontal period, bounds its distance to an actual lower-chain A anchor uniformly. A generic bounded path between them avoids vertices and crosses whole sides in the original ETE source. Disk packing bounds the number of crossed tiles. The path may leave the band; its purpose is to bound relative placements, so that causes no defect.

Full-side endpoint matches of indexed polygons have finitely many complete relative isometries, including reflections. Products of uniformly bounded length, from at most two lower-chain placements modulo T, give the uniform finite candidate bound. This resolves arbitrary absolute orientations and arbitrary upper-chain phases without assuming a globally finite orientation set.

Filtering candidates against the fixed A carrier and the band is T-equivariant. Diameter bounds give a uniform finite slab window. The bounded band and finitely many periodic polygon edges admit a finite arrangement in each such window; exactly-once coverage of open cells and interior-disjointness are finite local predicates. Closedness and local finiteness supply boundary coverage. Thus the accepted language is a genuine one-dimensional SFT containing the original filling. A directed simple cycle supplies a complete periodic band filling, with cycle length bounded uniformly over all bands.

There are countably many bands, and every selected period multiplier is between1 and a common finite M. The single integer lcm(1,...,M) synchronizes them all, even for infinitely many bands. Distinct fillings stay in disjoint bands and separators lie in the fixed A carrier. Their union is therefore a plane tiling with nonzero common period. No finite-patch extension or unsupported second-strip stacking step enters.

## Defects and limits

No repair required. The proof remains conditional on the named imported limit and monohedral results and on the exact residual input data. The finite atlas is used only as a necessary upper model; no sufficiency claim is needed. The conclusion is exactly the five-row conditional translational escape stated above.
