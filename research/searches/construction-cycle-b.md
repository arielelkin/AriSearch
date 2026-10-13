# Construction cycle B: bevelled-chair parents

Date: 2026-10-13. Status: completed and independently reviewed; aperiodic construction falsified. Finite question fixed before computation.

## Fixed question and domain

Use the chair boundary C=((1/2,0),(2,0),(2,1),(1,1),(1,2),(0,2),(0,1/2)) and seam from reflex R=(1,1) to S=(1/6,1/3), an interior point of its bevel. Atomic polygons are P=(S,(1/2,0),(2,0),(2,1),R) and Q=(S,R,(1,2),(0,2),(0,1/2)). The only finite geometric computation is this single pair, its P/Q seam, and the four rotations of C in the classical scale-2 chair assembly. No parameter sweep or adjacency atlas enlargement is authorized. The finite question: do these two strictly convex, distinct pentagons realize a geometrically recognizable chair parent compatible with that four-child scale-2 chair assembly?

Parent types proposed are the four rotations of C; their boundary vectors are (3/2,0),(0,1),(-1,0),(0,1),(-1,0),(0,-3/2),(1/2,-1/2). Exact coordinates are authoritative. (The initial handwritten vector word contained an extra initial vector; corrected before calculation.) The shared seam is R-to-S for P and S-to-R for Q, so cancellation is exact. Proposed next-level assembly is the classical four-chair dissection of the L triomino, with the same fixed bevels removed from each child. It must cover the scaled bevelled chair exactly; this is tested before making any infinite-covering claim.

## Early universal-forcing obligations

Recognition must pair every P with a Q across its oblique seam in every unrestricted tiling, including rotations/reflections, partial contacts, and omission. Recognition must remain translation equivariant at every scale. A nonempty level-n marker set separated by distances tending to infinity would exclude even one nonzero period. Private seam length alone does not establish that recognition. Monohedral escape and scale-2 area/union compatibility are the first hostile gates.

At most one specifically justified repair is allowed, only after a concrete failure. If no repair addresses both existence and universal forcing, stop this scheme with its exact obstruction; do not enlarge its finite domain. The B5+1 family is untouched.

## Exact fixed placements and pre-computation prediction

Writing J(x,y)=(-y,x), the four classical chair placements are C, C+(1,1), J(C)+(4,0), and -J(C)+(0,4). Their corresponding UNBEVELLED L-triominoes dissect 2L. No alternative placement is searched. The point w=(3/4,1/16) is inside C and outside 2C because w_x+w_y=13/16<1, while the large bevel requires x+y>=1 near its lower-left corner. This is an explicit extension failure prediction, to be checked exactly. Both atomic shapes retain adjacent right angles, giving an independent periodic-omission attack via halfturn fusion.

## Completed exact realization and obstruction (not a solution)

The fixed computation completed using Python Fraction arithmetic. P and Q are strictly convex pentagons with areas 3/2 and 11/8, so they are distinct even allowing reflections. Their interiors partition C, whose area is 23/8: the common seam is R-S, and no other boundary crossing occurs. Convexity, the seam partition, and the union are independently checked by the hostile reviewer. Native closure is the sum of consecutive vertex differences; the retained coordinates specify every edge. The pair therefore satisfies the exact atomic geometry gate.

The proposed four-child extension fails. The fixed unbevelled placements do dissect 2L, but the bevelled placement C contains w=(3/4,1/16), which lies outside 2C. Area equality alone (four children have total area 23/2) does not repair the protrusion. This fixed repeated extension provides no nested covering.

An independent existence theorem nevertheless holds for the atomic pair: P alone tiles the full plane periodically. Let h(x,y)=(4-x,1-y). Joining P and h(P) across the side ((2,0),(2,1)) cancels two flat junctions and yields the strictly convex central hexagon

H=(S,(1/2,0),(3,0),(23/6,2/3),(7/2,1),(1,1)).

Set u=(17/6,-1/3), v=(10/3,2/3). The hexagon has area 3=det(u,v). Exact separating-axis checks establish disjoint interiors for all 24 nonzero lattice differences (i,j) in [-2,2]^2. This finite domain suffices for ALL lattice neighbors: for every a,b in H the lattice coordinates of a-b have absolute value at most 14/9 and 23/18 respectively, hence less than 3 (the extrema occur at vertex pairs since each coordinate is linear); any overlapping translate must have integer coordinates inside that range. Thus all H+iu+jv have disjoint interiors. Their images in the lattice torus have full area 3. The image is closed, and any missing point would have an open positive-area neighborhood, contradicting full area. Therefore their translates cover the torus and plane. Splitting each H into P,h(P) proves an exact infinite atomic tiling. This proves existence early and independently of the failed hierarchy.

The plane tiling has nonzero periods u and v, so it refutes even the weaker claim of forbidding a single-direction period. It uses rotations and no reflections; allowing reflections only preserves this counterexample. It omits Q entirely, as the unrestricted definitions explicitly permit. All contacts in this covering are legal without an edge-to-edge condition; no prohibition of partial contacts can be inferred from the candidate. Consequently the proposed universal P-Q pairing is false and there can be no translation-equivariant hierarchy with nonempty increasingly separated markers on every admitted tiling: applying u to such markers contradicts separation once d_n>|u|.

No repair is spent. Adjusting only bevel endpoints or seam endpoints leaves the same halfturn-carrier escape while the atomic polygons remain convex and retain the two stated adjacent right-angle corners. Restoring both extension and universal forcing would need a materially different atomic/parent boundary mechanism, which is outside this singleton cycle. The exact pair and proposed hierarchy are Falsified as an aperiodic construction. The general pentagon-containing problem remains unresolved; neither B5+1 nor any parameter sweep was resumed.

## Evidence and replay

- Producer/check: research/searches/construction-cycle-b.py
- Exact certificate: research/certificates/construction-cycle-b.json
- Independent hostile review: research/reviews/construction-cycle-b-hostile-review.md (VALID exact counterexample/extension failure). Independent checker: research/reviews/check_construction_cycle_b_independent.py; evidence: research/reviews/construction-cycle-b-independent-check.json. It additionally certifies Q-only periodic omission.
- Replay command: mise exec -- conda run --no-capture-output -n arisearch python research/searches/construction-cycle-b.py --check research/certificates/construction-cycle-b.json
- Python 3.12.13 (conda-forge), standard-library fractions/json/argparse/pathlib only. Deterministic, solver-free; no timeout, seeds or symmetry search; one fixed pair and four fixed parent placements; 24 exact neighbor inequalities. Output writes are optional and must target disposable paths during registered replay.

Next concrete obligation for this mechanism: supply a new exact two-shape parent geometry in which the adjacent-right-angle central-hexagon omission carrier is absent AND the next-level child union equals the parent pointwise. Neither a longer chair-patch computation nor tuning this fixed bevel supplies that obligation. No novelty claim is made; the carrier principle is elementary.
