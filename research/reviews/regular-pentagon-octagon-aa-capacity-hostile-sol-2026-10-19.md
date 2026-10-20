# Independent hostile review: AA capacity obstruction

**Verdict: valid**, for the restricted regular pentagon / four-144°, four-126° octagon family in the reviewed lemma. This excludes plane tilability when Q has at least three AA sides, including the first-gate `AAAABBBB` candidate. It does not resolve the unrestricted two-convex-polygon problem.

## Claim and assumptions reviewed

Reviewed `research/lemmas/regular-pentagon-octagon-aa-side-density-obstruction-2026-10-19.md`, after reading `research-problem.md`, protocol §§8,11,19, the regular-pentagon-octagon first gate, and its prior independent hostile review. P is a regular unit pentagon; Q is a fixed strictly convex octagon with exactly four angles A=144° and four B=126°. Copies are isometric, may be reflected, and initially have unrestricted contacts. No periodicity, positive-frequency hypothesis, global extension, or imposed edge matching is assumed.

The review is an independent analytic reconstruction. No computational certificate or new numerical decision is used. The previous metric and finite-neighborhood certificates are not required for the obstruction itself; identifying the named isolated candidate uses the first gate's indexing convention.

## Unrestricted contacts and angle stars

Let D bound both tile diameters and m>0 be their smaller area. Any tile meeting a bounded set K lies within its D-neighborhood. Disjoint interiors therefore bound the number of such tiles by the area of that neighborhood divided by m. This proves local finiteness directly from the problem's definitions, so a sector decomposition around any contact point is legitimate.

At a corner lying inside another tile side, the latter supplies a 180° sector. The remaining 180° cannot be one corner, since all corners are 108°,126°,144°, and cannot be at least two corners, since each is at least 108°. Two straight sectors would already fill the circle and leave no room for the corner. Thus no corner can lie in an open side. Partial side contacts would require such an endpoint and are excluded. Every side has a single whole-side neighbor.

At each vertex exactly three corners meet: at most two sum to less than 360° and at least four exceed it. In units of 18°, the only triples from 6,7,8 summing to 20 are 6+6+8 and 6+7+7. These are PPQ at A and PQQ at B. In particular neither tile alone tiles the plane. At A the two Q edges face P, and the two P tiles share their other incident edges. At B the sole P has Q neighbors on both incident sides. This reconstructs the edge-to-edge conclusion without assuming it.

## Local capacity attack

Label the five sides of a P cyclically by 0,...,4. Two PP sides cannot be consecutive: the common P corner would then have P on both adjacent sectors, contradicting the exhaustive star list. Hence the PP sides form a matching of C5, containing at most two edges.

If side i of P faces an AA side of Q, each endpoint is a PPQ star. Consequently sides i-1 and i+1 of P are PP sides (indices modulo 5). These are distinct. Two disjoint edges in C5 have exactly one side lying between them and adjacent to both. Explicitly, after rotating the pair to {0,2}, that side is 1. Therefore at most one P side can face an AA side. With fewer than two PP sides there is no such side. This proof counts physical pentagons, so a Q whose two unit-side neighbors happen to coincide cannot bypass capacity. Reflections preserve every step.

## Uniform finite-region count and zero-density attack

Take S_R=[0,R]^2 and choose an interior reference point in each prototile, transported with each copy. Let p_R,q_R count references inside S_R. All references are within D of their tile points. Every discrepancy between counting a reference and counting an incident vertex or neighboring reference occurs within a fixed-width neighborhood of the square boundary. The number of tiles meeting that neighborhood is O(R+1): enlarge it by D and divide its area by m. Each tile has boundedly many corners and edges. The error constants depend only on P,Q and are independent of the tiling. The same argument applies to counting vertices near the boundary, since each is a tile corner.

Let a_R,b_R count PPQ and PQQ vertices in S_R. Counting Q corners and P corners gives

    a_R = 4 q_R + O(R+1),
    2 b_R = 4 q_R + O(R+1),
    5 p_R = 2 a_R + b_R + O(R+1).

Thus p_R=2q_R+O(R+1). If each Q has a AA sides, sending each such side to its neighboring P is globally injective by local capacity. Restricting to reference points in S_R introduces only the same boundary error, so a q_R <= p_R+O(R+1). For a>=3, q_R=O(R+1), and then p_R=O(R+1).

This cannot describe a plane cover. Tiles covering S_R have references in its D-neighborhood; only O(R+1) of those references lie outside S_R. If M is the larger tile area, then

    R^2 <= M (p_R+q_R+O(R+1)).

The derived linear bound contradicts this inequality. This explicitly handles a hypothetical sequence of squares with vanishing Q density: corner balance also makes P subquadratic, which the covering forbids. No ergodic theorem, density limit, or periodic exhaustion is involved.

## Words, defects, and scope

For a cyclic word, AA sides are indices i with both letters i and i+1 equal to A, indices modulo 8. `AABBAABB` has AA sides 0,4; `AAABBABB` has 0,1; `AAAABBBB` has 0,1,2. With the same outgoing-edge convention, `AAAABBBB` has B positions 4,5,6,7 and QQ matching (4,6), precisely the first-gate candidate. Rotation or reversal preserves the AA count.

Attacks checked were hidden local finiteness, non-edge-to-edge contacts, reflected stars, repeated physical neighbors, a pentagon with fewer PP sides, multiple flanked sides on C5, boundary concentration, absent density limits, Q of vanishing frequency, single-type tilings, and cyclic indexing. None invalidates the proof. No substantive defect or mathematical repair was required; the estimates above make the source's existing boundary argument explicit.

For a=2 the count alone permits a subquadratic population of pentagons with unused capacity. It supplies neither pointwise saturation nor plane existence for either surviving word. The review makes no claim about the continuum's local-neighborhood audit, novelty, or universal aperiodicity. The exclusion is valid for every fixed Q satisfying its stated palette and AA hypothesis, independently of the earlier local seam checks.
