# Fresh independent review: third periodic two-run curve

**Verdict: VALID throughout 0<delta<30 degrees, with arbitrary positive common scaling.**

Reviewer: branching_hexagons, freshly assigned by root. Root suggested the symbolic curve and is not the sole reviewer. This reviewer independently reconstructs raw geometry and quotient topology; no author imports or author producer execution are used.

Reviewed [theorem](../lemmas/branching-hexagon-new-two-run-third-curve-periodic-escape.md), [eight-face quotient](../certificates/branching-hexagon-new-two-run-third-orbit-eight-face-periodic.json) and [delta15 development](../certificates/branching-hexagon-new-two-run-third-orbit-eight-face-development.json). The result supplies an actual doubly periodic tiling for each pair on this curve. It does not classify all two-run pairs or resolve the original problem.

## Full parameter interval: exact native geometry

The [independent checker](verify_branching_hexagon_new_two_run_third_curve_independent.py) sets t=tan(delta/2), so 0<t<2-sqrt3, and uses cos(delta)=(1-t^2)/(1+t^2), sin(delta)=2t/(1+t^2). It reconstructs every raw Cartesian edge from the stated physical directions over the rational function field Q(sqrt3)(t), with p=2cos(delta)/(1+sqrt3). Both polygon closures are exact rational identities. Every edge's squared norm is its stated p^2 or 1. Positivity follows from t<2-sqrt3<1.

The affine indexed angles are independently derived by successive differences of the physical direction words, including the wrap at vertex0. They are exactly the displayed A and B angle words, and every angle is strictly between0 and180 degrees on the entire open interval. The checker independently verifies all48 nonincident vertex support determinants. Their numerator and denominator polynomials have no real root in the open interval, by exact real algebraic root isolation; their signs agree at an exact interior point. Thus every support determinant is strictly positive for the entire interval. This checks strict convexity directly from raw vertices, without continuity from delta15 or assuming that a closed cyclic edge walk is embedded.

Reflected references are the actual real-axis reflections with reversed vertex order, keeping vertex0 fixed. Their side labels reverse and their indexed angles become angle[-i mod6], as required. This distinguishes vertex-angle reversal from side-label reversal.

## Actual quotient links and global implication

All24 paired seams use equal physical side labels and all48 side occurrences appear exactly once. The independent link successor sends an outgoing native side at(u,i) to the partner's incoming corner(v,j+1); it is reconstructed directly from the seam list. Its cycles are exactly the16 listed vertex classes, each with three corners. Each actual cycle has affine angle sum360+0delta. Thus each vertex link is a single circle with full angle360; the check does not rely on the number of corner classes or a mere angle-frequency sum.

The face adjacency graph is connected. Every boundary gluing reverses its two boundary orientations, giving an oriented closed surface. Interiors and edges have Euclidean neighborhoods, and the independently checked circular360 links give nonsingular Euclidean neighborhoods at vertices. With8 faces,24 edges and16 vertices its Euler characteristic is0. It is therefore a compact connected orientable flat torus for every curve metric.

Its complete simply connected flat universal cover is the Euclidean plane. Lifted native faces cover this plane with disjoint interiors. The orientation-preserving Euclidean deck isometries act freely: any nonidentity orientation-preserving Euclidean isometry with a nonzero rotation has a fixed point, so every deck isometry is a translation. Compactness supplies a discrete rank2 translation lattice. This establishes a periodic whole-plane tiling for the complete curve without extending a bounded patch or assuming a sample deformation remains valid.

## Independent delta15 development and complete overlap domain

At delta15 the checker reconstructs the native vertices with exact real algebraic radicals, using p=1/sqrt2. It checks the retained cyclotomic reference vertices and all8 retained rigid face placements against those raw references. Every rotation has unit norm. All24 transformed seam vectors are opposite, and their endpoint differences equal the retained translational seam holonomies.

Put x=sqrt6/2+sqrt2. Every seam difference has integral coordinates in H=(x,0), K=(0,2x). The gcd of all2x2 minors of the24 integer coordinate vectors is1, proving that their generated module is the complete primitive Z^2 lattice, rather than a proper finite-index sublattice. The retained basis is independently decoded as U=(x,2x), V=(2x,6x), whose integer basis change H=3U-V, K=V-2U has determinant1. No claim about primitivity is inferred just from rational rank2.

Independent areas are area(A)=3/4+5sqrt3/8 and area(B)=1+3sqrt3/8. The8-face motif area is7+4sqrt3=2x^2, exactly the rectangular covolume and the retained certificate value.

As a separate planar check, for each ordered pair of placed native faces the checker bounds every potentially intersecting lattice translate by its exact Cartesian bounding boxes, dividing the horizontal interval differences by x and the vertical differences by2x and taking exact ceil/floor. Every translate outside those bounds has disjoint bounding boxes. There are48 nonidentical candidate comparisons, with maximum lattice index1. Every candidate passes exact convex separating-axis inequalities, including equality contacts. Thus all lattice copies have disjoint interiors. Equal motif area and covolume give mean multiplicity1; the closed locally finite periodic union cannot leave an open hole. This also independently proves full-plane coverage at the exact catalog member.

## Replay and boundary

Completed readonly replay:

    conda run --no-capture-output -n arisearch python research/reviews/verify_branching_hexagon_new_two_run_third_curve_independent.py

Output: PASS for raw rational closure,48 full-interval strict support inequalities,48 unique side occurrences,16 actual circular360+0delta links and the connected oriented torus; PASS for8 exact delta15 placements,24 translational holonomies, the complete primitive rectangular lattice, area/covolume and all48 complete lattice overlap candidates.

No substantive defect was found. The open interval endpoints are not claimed. Positive common scaling preserves every seam, angle, convexity inequality and translation period. The finite guided quotient-search enumeration is provenance for finding the retained witness, not a necessary component of the existence proof and not an untileability certificate for any other pair.
