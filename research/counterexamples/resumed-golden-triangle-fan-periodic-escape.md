# Golden-triangle fan periodic escape and periodic dissection inheritance

Date:2026-10-13. Status: exact internally proved counterexample and compiler theorem; independent review status is maintained by the root agent. Scope: three same-apex unit golden triangle fans and literal dissections of periodic sources. Not unrestricted convex-pair impossibility.

Definitions: φ=(1+√5)/2. Triangle C has sides1,1,φ−1 and distinguished apex36°; O has sides1,1,φ and distinguished apex108°. Consecutive common-apex fans glue equal unit radial sides. The source compiler record and finite eight-word proposal domain are in research/searches/resumed-source-compiler.md.

## Exact fan gate

The apex angle is36a+108o, where a+o=3. A strict convex fan requires this angle<180. If o≥1, the angle≥180: o=1 is flat and yields a genuine quadrilateral, while o≥2 is reflex. Thus the only genuine convex pentagon is CCC, up to congruence. This conclusion exhausts all eight words analytically; no solver is used.

Its exact vertices in counterclockwise order are

P=[(0,0),(1,0),(c,s),(d,t),(-d,t)],

where c=(1+√5)/4, d=(√5−1)/4, s=√(10−2√5)/4, t=√(10+2√5)/4, with positive square roots. Its angles at these vertices are(108,72,144,144,72) degrees. The following direct periodic witness avoids importing pentagon classification.

Put e=(1,0) and form the half-turn mate e−P, joined along[(0,0),e]. Interiors are disjoint: P lies above the x-axis and its mate below. The seam endpoint angles are108+72=180 at both ends, so they disappear from the genuine outer polygon. The union is the convex centrally symmetric hexagon

H=[v1,v2,v3,e−v1,e−v2,e−v3],

where v1=(c,s), v2=(d,t), v3=(−d,t). All six remaining corner angles are inherited strict angles. Center=e/2. Every centrally symmetric convex hexagon tiles by translation: with consecutive vertices h0,...,h5 and h(i+3)=e−hi, use lattice vectors L1=h0+h1−e and L2=h1+h2−e. Opposite edge pairs meet via L1,L2,L2−L1. These match all boundary edges and produce the standard parallelohexagon tiling; the lattice fundamental area equals area(H), so it covers the plane without overlap. Equivalently obtain it by replacing vertices of a fundamental parallelogram with opposite triangular caps. Cutting each carrier into P and e−P yields a rank-two periodic P-only tiling.

Consequently every target pair containing this fan pentagon fails the original aperiodicity condition, regardless of its partner. The three-triangle fan proposal is falsified. Its only possible second strict convex pentagon is congruent to P, so it also fails the exactly-two-congruence-class gate. No larger fan enumeration is warranted without a different assembly mechanism.

## Periodic inheritance gate for literal source dissection

Theorem. Let a finite protoset Q admit a periodic tiling with a finite motif. Suppose every Q shape is finitely dissected into copies of members of a finite target protoset R. Then R admits a periodic tiling. Convexity, matching of subdivision endpoints across parent boundaries, edge-to-edge contacts and use of every target type are unnecessary.

Proof. Dissect each tile in one finite motif according to a fixed dissection of its Q representative transported by its motif isometry. Repeat those same dissected motif tiles by the original period lattice. The targets cover each parent exactly with disjoint interiors; distinct parents have disjoint interiors. Hence targets cover the plane without interior overlaps. The original two independent lattice periods preserve the repeated dissection. Extra target seams can end at parent boundaries because contacts are unrestricted. Omission is legal. ∎

Corollary. Even a dissection of just ONE plain Penrose rhomb into the proposed final two shapes kills their aperiodicity: that rhomb alone tiles by its two edge vectors, and those same translations repeat the dissection. Generic internal angle/length forcing cannot rescue any literal source-by-source dissection of ordinary rhombs. A reassembly that crosses parent boundaries, or modifies their edges into geometry enforcing Penrose rules, is essential. Marked Penrose legality cannot be transported to a final unmarked pair by assertion.

This gate is independent of the previously retained Ammann area-rank obstruction, because the Ammann shapes themselves do not have the plain-rhomb periodic witness. It does not apply merely because an atom can be intersected with parent boundaries: those intersections need not be complete target copies.


Exact check: research/searches/resumed-source-fan-check.py. Replay: mise exec -- conda run --no-capture-output -n arisearch python research/searches/resumed-source-fan-check.py. Checks pass strict convexity, half-turn symmetry, whole-side lattice mates and exact determinant=carrier area. Aperiodicity is excluded for every pair containing the fan pentagon, even if the second type is never used.
