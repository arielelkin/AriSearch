# Independent hostile review: corrected thirtytwo-star native metric

Date: 2026-10-19. Verdict: **PASS / valid for the corrected local analytic metric family and exclusion of H1/H2/H3**, with the length-language correction below. The old uncorrected branch remains invalid for native support; this verdict does not rehabilitate it.

## Exact scope and editorial defect

Reviewed the same-stem corrected lemma, producer and certificate. There are five pairwise distinct positive length parameters across the pair: A=(0,1,2,0,3,4) uses all five, whereas B=(0,1,2,0,3,1) uses only four. Exactly four numerical lengths are common to both polygons. Thus “five positive distinct common lengths” is misleading if “common” means present in both. Replace it by “five pairwise distinct positive length parameters, with A using five values and B four.” No theorem requiring five distinct values in each polygon applies to B. B has two repeated values, symbols0 and1, and they are both included in the audit.

## Native convention, closure and IFT

Native corner c is between sides c,c+1, at the end of side c in positive traversal. The corrected formula phi_j=sum(k<j)(pi-alpha_k) therefore uses precisely the correct native angles. The four support triples use those same variables without a shift. Their affine matrix has rank five; the certificate nullspace has rank seven and annihilates all six rows. The equiangular origin satisfies each polygon total and every support sum.

The independent checker differentiates trigonometric closure expressions directly, rather than importing the producer Jacobian routine. It reproduces the complete 4-by-7 Jacobian, solved minor, determinant -3/4, and angle tangent. Both base closures vanish. The four-dimensional invertible minor permits analytic IFT solving x0..x3 with x4=t,x5=x6=0 and the stated length path. IFT supplies an unspecified neighborhood, which suffices for an existence statement for every sufficiently small positive t. It does not supply a prescribed numerical positive t or explicit algebraic coordinates.

The base vertices are (0,0),(2,0),(5/2,sqrt(3)/2),(2,sqrt(3)),(0,sqrt(3)),(-1/2,sqrt(3)/2). Every nonincident vertex lies strictly left of every positively oriented boundary edge, checked exactly. These finitely many strict inequalities persist along the analytic branch, establishing simplicity and strict convexity. For 0<t<1/4, 1+t through1+4t are distinct positive values below2. Side-length multisets differ, so the two polygons are distinct congruence classes.

## Complete monohedral systems and external convention

The source [Zhu–Wang–Yan, Hexagonal Tiling of the Plane, v2, introduction](https://arxiv.org/html/2508.01404v2) labels corner i at the start of edge i. Its H1 requires corners0,1,2 to sum2pi and edges2,5 equal; H2 requires corners0,1,3 to sum2pi and edges1,3 and2,5 equal; H3 requires three adjacent equal-length pairs and alternate angles120 degrees. Its Main Theorem covers unrestricted straight-edge congruent-hexagon tilings whenever at least three tiles meet at each vertex, which strict convexity ensures. The exclusion conclusion below imports that theorem; its completeness proof was not independently reconstructed in this review.

For a forward reading with physical side indices s_i=k+i, source start corner i is native alpha_(s_i-1). For a reversed reading s_i=k-i, source start corner i is native alpha_(s_i). The independent checker uses precisely these source-start formulas with source H1 indices0,1,2 and H2 indices0,1,3. This independently agrees with the producer's end-side/complement encoding.

Across all twelve dihedral readings per polygon, A has four H1 length matches, no H2 and no H3; B has four H1, two H2 and no H3. Thus B's additional repeat is not overlooked. Every H1 matched sum has derivative plus/minus1. Both B H2 matched sums have derivative plus/minus1. Every relevant residual vanishes at t=0 and has nonzero derivative; hence it is nonzero for every sufficiently small positive t. Intersecting the finitely many valid neighborhoods excludes every H1/H2 label simultaneously. H3 fails already by lengths. Under the external classification neither polygon tiles the plane alone.

## Attacks, repairs and remaining gaps

Attacks covered the previous off-by-one defect, reflected start/end conversion, minor singularity, support rank, accidental length collisions, omitted B repeat, base self-intersection, all dihedral monohedral labels, and confusion between first-order evidence and exact analytic nonvanishing. No mathematical defect remains within the scoped statement. No edits to the producer or source lemma were made by this reviewer; the length wording requires correction by its owner.

No corona, mixed-plane tiling, periodic mixed escape, aperiodicity, or finite explicit coordinate witness follows. Native angle compatibility alone is weaker than geometric support realization. External classification is an explicit imported assumption, separate from the unconditional local IFT construction.

## Reproduction

`mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hexagon-thirtytwo-star-end-corner-analytic-metric-hostile-sol-2026-10-19.py`

Result: PASS. The retained independent checker reads the corrected certificate, constructs closure symbolically, verifies exact derivatives and support, checks all strict base halfplanes, and enumerates24 source-convention side readings. It uses SymPy exact arithmetic, no floating point, search seed, solver, timeout, extension enumeration, or new support search. The mathematical IFT/openness and external classification implications are audited in this review rather than inferred from finite computation.
