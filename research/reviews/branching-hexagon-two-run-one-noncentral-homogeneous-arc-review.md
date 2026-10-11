# Fresh review: one noncentral homogeneous arc

**Verdict: VALID for the exact stated A(delta)/binary-two-run family.**

Fresh reviewer: branching_hexagons. Reviewed the current repaired [lemma](../lemmas/branching-hexagon-two-run-one-noncentral-homogeneous-arc.md), independently reconstructed its native contacts and boundary counts, and retained the [independent checker](verify_branching_hexagon_one_noncentral_homogeneous_arc_independent.py). No author module, solver answer, finite quotient, or assumption that both species survive a limit is used. Root contributed the mixed-capacity argument and independently identified an earlier wording error; this review checks the repaired proof independently.

## Domain, normalization and imported limit

The exact hypotheses are positive distinct p,q, strict convexity, 0<delta<30, A's displayed alternating directions, B's pppqqq word, exactly one arc allowing a homogeneous repeated-corner triple, and that arc not having both native angles120. Normalize q to1 first. If the homogeneous arc is qq, the native block start changes to old side3 and the reviewed A reflection restores the same delta after the common length swap: new p=q/p, new q1. The total common scale, in the original lengths, is1/p. Native B arc angles exchange; homogeneous-triple legality, unordered pairing and noncentrality persist. The checker freshly verifies all six symbolic A edge identities using rational half-angle coordinates and the B block/index exchange.

The already independently VALID defect-free limit theorem in [hexagon limits](../lemmas/hexagon-limit-and-periodicity.md) permits passing from any admitted unrestricted tiling to an actual trivalent edge-to-edge tiling, including possible omission of one species. The present proof does not use any further sparse-defect limit. Select tiles by a point such as their centroids and vertices/seams by their positions/midpoints in Q_R. Changing these conventions changes every ledger by O(R): an affected tile lies in a fixed-width boundary band, and bounded tile diameters and positive minimum area bound the number of such tiles by O(R). Each tile has only six vertices/sides, so charges and corner/seam inventories inherit that bound. Coverage gives total selected tile count Omega(R^2), with no separate lower density of A or B assumed.

## Binary incidence and mixed homogeneous cases

The checker exhausts all1664 native label-compatible oriented corner triples, retaining both mirror states independently. A three-ray cycle has either zero or two changes of the distinct length labels. Thus each nonhomogeneous star has two mixed and one homogeneous corner; only B has homogeneous corners. Double counting gives 2V_m=6N_A+2N_B+O(R) and4N_B=V_m+3Y_p+3Y_q+O(R), hence N_A=N_B-Y_p-Y_q+O(R). No qq homogeneous multiset is legal, so Y_q0.

Both whole-side identifications of A's H/L endpoints require either two120 fillers or the pair120-2delta,120+2delta. Therefore AAp is impossible when qq is nonhomogeneous and unpaired. For a mixed pp homogeneous equation, neither pp120 nor paired pp is possible outside the center, so AAq is also impossible. A trivalent star cannot contain two A tiles because they would share a whole radial seam. Every A corner then consumes a distinct B mixed native-corner occurrence, yielding6N_A<=2N_B+O(R). All six pairwise intersections of the four pp homogeneous resonance planes are exactly alpha=beta120. Consequently only one mixed multiset is legal in this case, and each pure star consumes two occurrences of its repeated pp native slot: Y_p<=N_B/2+O(R). Thus N_A>=N_B/2-O(R) and N_A<=N_B/3+O(R), forcing both counts O(R), contrary to quadratic total count. This also covers an alleged tiling using none of the legally permitted homogeneous stars.

## Pure120 slot: reflection and seam charging

Reflection/reindexing swaps pp slots and simultaneously qq slots, so alpha120 may be assumed without changing the unordered qq hypotheses. With beta!=120, the only legal pure pp star is3alpha. Native B side1 has endpoints alpha,beta. In both possible endpoint identifications of a side1/side1 seam, an endpoint contains beta and two other pp corners; it cannot belong to the sole legal pure triple. Hence that whole-side match is impossible.

At a3alpha star, each native corner exposes sides0 and1. Exhausting all eight mirror assignments, excluding1/1 forces all three radial matches0/1 and the same chirality for the three B occurrences. Each radial seam is a distinct actual edge; positive edge length prevents an endpoint loop. Its opposite end has mixed B0 and pp beta, so it cannot be charged by any other3alpha star. Consequently E>=3Y-O(R), where E counts all BBp seams. AAp absence supplies3N_A=3N_B-2E+O(R), while the corner ledger supplies N_A=N_B-Y+O(R). Their exact elimination gives3Y=2E+O(R). The two bounds imply Y,E=O(R) and N_A=N_B+O(R). No disappearance of these seams pointwise is asserted.

A B pp native-corner occurrence is bad only if incident to a BBp seam; at most4E+O(R) pp occurrences are bad, since a seam has two endpoints with at most two B sectors each. Every other pp occurrence has two A neighbors. Good alpha120 consumes one H and one L. Good beta can exist only for beta120 or120±2delta. The center is excluded; if neither remaining value applies, N_B=O(R) already contradicts the preceding equality and total count. For low beta, good alpha and beta stars consume3N_B-O(R) H corners, so any additional X_H stars consume only O(R) H corners. These good stars are distinct from X_H because they have two A sectors, whereas X_H has one. The high-beta case gives the same conclusion for X_L.

## Actual middle-q endpoint necessity

Both endpoint bijections for B middle-q side4 against every B q side3,4,5 produce at least one qq/qq endpoint. The third corner there is necessarily qq by cyclic ray labels, yielding a forbidden homogeneous triple. Thus side4 meets a whole A q side, which has opposite H/L endpoints.

At each B qq native corner, the already established side4 contact guarantees an A neighbor. A second A would create AAp along the other radial seam, forbidden. The remaining neighbor is B, and binary parity forces its corner to be mixed. This is exactly the repaired current paragraph. The earlier statement that an isolated Bqq corner with two B neighbors necessarily produces a qqq star was false (two B mixed corners are possible), but is absent and unnecessary in the reviewed proof.

Each middle-q seam therefore contributes one X_H and one X_L endpoint. Each such star has exactly one Bqq corner; that native corner belongs to exactly one B middle-q side4. The charges are injective, giving X_H,X_L>=N_B-O(R). This contradicts the applicable exhausted H or L capacity and completes the pure120 noncentral case, without presuming either species has positive density. At the excluded center beta120, middle-p seams can connect pure stars at both ends, so the stronger charge inequality need not hold; the exclusion is substantive.

## Positive branch and scope

If the nonhomogeneous arc is paired, the normalized pair falls in the independently VALID [paired-qq classification](../lemmas/branching-hexagon-two-run-paired-qq-classification.md). Its two exact positive periodic cones supply both necessity and actual periodic sufficiency, transferred back by inverse common scaling and native congruences. Their periods remain independent. No periodicity of every tiling is claimed.

Together with the reviewed no-homogeneous classification, the result leaves within this specified A(delta)/binary-two-run family only the two-homogeneous-arc cases and the exactly-one-homogeneous central arc cases. Equal lengths, delta boundaries, arbitrary A, and the unrestricted two-prototile target are outside this result. No unresolved defect remains in the current scoped theorem.

Replay:

    conda run --no-capture-output -n arisearch python research/reviews/verify_branching_hexagon_one_noncentral_homogeneous_arc_independent.py

PASS1664 oriented label-compatible native stars, binary ledgers, AA endpoint alternatives, all six homogeneous-plane intersections, all eight pure-star mirror assignments, native whole-side endpoint bijections, exact count eliminations, and all six swapped A edge identities. The finite checker audits local contact and algebraic obligations; the unbounded contradiction is the explicit boundary proof reviewed above.
