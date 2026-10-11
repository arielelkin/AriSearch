# Saturated binary two-run chains and actual B–A–B bridges

Status: **PENDING fresh independent review.** These are necessary consequences for an admitted tiling under the hypotheses below. Pure chains have a period, but no conclusion that the entire tiling is periodic is made. The mixed-chain exceptional geometries already have constructive periodic escapes; the remaining pure-chain bridge geometries are not classified here.

## Hypotheses and native notation

Fix 0<delta<30, q=1 and p>0 with p unequal to q. A has native side word (p,q,p,q,p,q), directions (0,60+delta,120,180+delta,240,300+delta), and native angles A_H=120+delta at even vertices and A_L=120-delta at odd vertices. B is a fixed strictly convex closed hexagon with native side word (p,p,p,q,q,q). Its corners B_1=alpha and B_2=beta are pp; B_4,B_5 are qq; B_0,B_3 are pq.

Assume there is no legal homogeneous trivalent star: no multiset of three B pp corners has angle sum 360 and no multiset of three B qq corners has sum 360. Repetition is allowed in these multisets. Also assume an A–A q seam cannot occur in a trivalent edge-to-edge tiling of the pair. A sufficient exact test for this last condition is that neither alpha nor beta is 120 and the pp corner set does not contain both 120-2delta and 120+2delta. An A–A q seam's endpoint fillers would be either two 120 corners or the two 120±2delta corners; its third corners must be B pp, since A has only mixed corners.

If the pair tiles the plane unrestrictedly, the reviewed hexagon compactness theorem supplies an admitted trivalent edge-to-edge tiling, possibly monohedral. Under these hypotheses the corner-label count below forces both species to occur in that tiling. All subsequent reasoning takes place in actual edge-to-edge tilings; angle sums alone do not assert geometric realizability.

## Boundary counts and first saturation

Select tiles with centers in a square of side 2R. Fixed positive tile areas and a fixed diameter bound give O(R) boundary tiles, corners, and seams, with constants depending only on the two shapes. Interior star/seam counts differ from the total selected tile-incidence counts by O(R), uniformly over translations of the square and admitted tilings. Write N_A(R),N_B(R) for the selected counts. Their sum is Omega(R^2).

There are 6N_A+2N_B mixed corner occurrences and 4N_B homogeneous corner occurrences. In a trivalent star without homogeneous stars, exactly two corners are mixed and one is homogeneous: its three side labels are not all equal, and cyclically they change twice. Thus

    6N_A+2N_B = 2V + O(R),       4N_B = V + O(R),

and N_A=N_B+O(R). A monohedral limit is impossible because then one count is zero whereas their sum is Omega(R^2).

All A q sides meet B q sides, since A–A q seams are prohibited and p differs from q. Counting q incidences gives

    3N_A = E_AB,q + O(R),
    3N_B = E_AB,q + 2E_BB,q + O(R).

Hence the number of B–B q seams is O(R). This does not assert that those seams are absent pointwise.

We may extract another admitted limit in which every q seam is A–B. Here is the requisite defect selection explicitly. For each fixed avoidance distance L, the union of radius-L disks about O(R) bad seam midpoints in a square of radius R has area O(R L^2). Choose R sufficiently large compared with L^2, and exclude an additional boundary band of width L plus the tile diameter. A point remains in the interior whose L-neighborhood contains no bad seam. Translate it to the origin, take L tending to infinity, and use the reviewed compactness theorem with its positive sector separation. No bad seam occurs in any fixed compact region of the resulting tiling. This produces an actual admitted limit, not a pointwise assertion inferred from an O(R) estimate. Trivalent edge-to-edge structure and the prohibited local stars persist in this limit.

## Forced qq angles and p contacts

At each B qq corner both neighboring tiles across its two q sides are A. Thus its actual vertex star is B+A+A. Its angle is one of 120-2delta, 120, 120+2delta. The value 120 is prohibited because three repeated copies of that B qq corner would be a legal homogeneous qqq star. If both native B qq corners had angle 120-2delta, their two-A stars would consume 4N_B A_H corner incidences, more than the available 3N_A by order R^2. The same contradiction applies to two 120+2delta corners using A_L incidences. Therefore one qq angle is 120-2delta and the other is 120+2delta. By choosing the native direction of traversal of B, normalize

    B_4=120-2delta,       B_5=120+2delta.

This changes only native indexing of the same shape. Each qq star is respectively two A_H corners or two A_L corners, and its two A tiles share a full p side: the third seam between the two A corners has label p.

B's middle p side p1 cannot meet any B p side. If it met p0 or p2, at least one endpoint would be pp+pp; if it met p1 both endpoints would be pp+pp. The third corner would then also be pp, giving a forbidden homogeneous star. Consequently every B p1 side meets an A p side.

At either endpoint of such a seam, the third tile cannot be A, because its seam with the first A would have label q and would be an A–A q seam. It is therefore B, at a mixed pq corner. This forces both B outside p sides p0 and p2 to meet B p sides. They cannot meet B p1, by the preceding argument, so the B p0/p2 contacts form a degree-two graph on B tiles. Self adjacency of a tile is impossible in an actual plane tiling; quotient carriers may represent it only through different translated copies.

## At most one A–B p side and the second saturated limit

Every A q side meets one of the three B q slots q3,q4,q5. Each of those slots has at least one qq endpoint. At that endpoint, the preceding qq-star argument forces an A–A p side adjacent to this A q side. The three distinct q sides of an A therefore force at least two distinct A–A p sides: each of its p sides is adjacent to at most two of its q sides. Every A has at most one A–B p side.

Each B has exactly one B–A p seam, namely its p1 seam. If Z counts A tiles with zero A–B p sides, actual seam counting therefore gives

    N_A-Z = N_B+O(R),       Z=O(R).

We can repeat the preceding defect-selection compactness argument, now avoiding centers of these A tiles as well as preserving the all-A–B q limit. It yields a further admitted tiling where each A has exactly one A–B p side and exactly two A–A p sides. Its local properties are inherited from the first limit. Again the conclusion is for a specially extracted admitted limit, not necessarily the original tiling.

A tile meeting a B middle q4 side has both its q-side endpoints in B qq stars and therefore has both adjacent p sides A–A. If an A met two distinct B q4 sides, the two distinct A q sides would force all three A p sides to be A–A, which is now impossible. Thus every A meets at most one B middle q4 side. Each B supplies exactly one such incidence. The number of A tiles meeting none is N_A-N_B+O(R)=O(R). One more simultaneous extraction avoids these exceptions. In the resulting admitted tiling each A has exactly one B middle q4 neighbor. Its two adjacent p sides are A–A; its unique A–B p side is the opposite native side. This is an actual B–A–B bridge, not just frequency balance.

## Actual pure-chain isometries and endpoint tests

Normalize a B copy in complex coordinates with native vertices v0=0, v1=p and set

    u=180-alpha,   v=360-alpha-beta,
    v2=p(1+exp(iu)),   v3=v2+p exp(iv).

Any B p0/p2 seam must swap a mixed endpoint and a pp endpoint at each end. Pairing mixed with mixed at one endpoint would pair pp with pp at the other and give the prohibited homogeneous star. Same-slot mates therefore have the same chirality. Their actual plane isometries are the halfturns

    H0(z)=p-z,            H2(z)=v2+v3-z.

A pure same-slot chain alternates p0–p0 and p2–p2 contacts. Two steps give a nonzero translation

    T_same = v2+v3-p = p(1+2 exp(iu)+exp(iv)).

It is nonzero because zero would make the midpoints of two distinct sides p0 and p2 equal, impossible for a strictly convex polygon.

Cross-slot mates have opposite chirality. Mapping native side p2 of the neighboring B onto host side p0 with the required endpoint exchange is

    G(z)=exp(iv) conjugate(z-v2).

Indeed G(v2)=v0 and G(v3)=v1. A pure cross-slot chain is generated by this glide reflection; two steps give

    T_cross = -v2-exp(iv) conjugate(v2)
      = 4p sin(alpha/2) sin(beta/2) exp(-i(alpha+beta)/2).

The factor is strictly positive because alpha,beta lie in (0,180), so this period is nonzero. The image of each successive B is the unique adjacent actual copy along that chain. These periods prove only the translational periodicity of the isolated pure B chain, not of all its A attachments or of the whole tiling.

Let rho be the argument of the unit p-chain sum, with the branch fixed by the actual normalized q-chain directions. Closure and the normalized qq angles give

    B_0=60+rho-delta,
    B_3=420-rho+delta-alpha-beta.

Every B–B p seam has one B pp and one B mixed corner at each endpoint; its third tile must be A. For a same-slot seam the endpoint B angle sums are B_0+alpha and B_3+beta. They sum to 480 and must be the complementary pair 240-delta,240+delta. Thus a necessary endpoint test is

    same-slot: alpha+rho belongs to {180,180+2delta}.

For a cross-slot seam the sums are B_0+beta and B_3+alpha, so its necessary endpoint test is

    cross-slot: beta+rho belongs to {180,180+2delta}.

These are necessary geometric endpoint tests in an admitted tiling. They do not assert that any shape satisfying them admits a globally consistent attachment.

If both tests hold, then either alpha=beta or beta-alpha=±2delta. If alpha=beta, the p-chain sum is exp(-i alpha)(2cos(alpha)-1). Its nonzero phase and the tests force alpha>60 and rho=180-alpha. Strict convexity of B_3 then forces alpha>60+delta. This is the previously constructed equal-pp-angle cone.

If beta=alpha+2delta, the tests require alpha+rho=180 and beta+rho=180+2delta. The imaginary part of exp(i alpha) times the p-chain is sin(alpha)-sin(beta)=0, hence alpha+beta=180, giving

    alpha=90-delta,       beta=90+delta.

This is a slice of the independently reviewed complementary-pp cone; closure gives p=2cos(delta).

If alpha=beta+2delta, the tests instead require beta+rho=180 and alpha+rho=180+2delta. The imaginary part of exp(i beta) times the p-chain is

    sin(beta)+sin(2delta)-sin(beta+2delta)
      = 2sin(delta)[cos(delta)-cos(beta+delta)].

Here 0<beta<180-2delta, so delta<beta+delta<180-delta and the bracket is strictly positive. It cannot vanish. Thus no such simultaneous-test geometry exists.

Consequently every admitted geometry with both seam kinds available already has a known constructive periodic escape. For a geometry outside these periodic families, at most one seam kind is allowed; hence all its B chains are pure and carry the explicit periods above. The remaining proof gap is to determine the possible B–A–B bridge placements between these periodic chains, or construct a compatible full periodic quotient. This manuscript does not resolve that gap or promote an angle-only test to a periodicity theorem.

## Dependencies and review obligations

The defect-free trivalent ETE reduction and compactness are the reviewed `research/lemmas/hexagon-limit-and-periodicity.md`. The two positive escapes are `branching-hexagon-new-two-run-two-parameter-periodic-cone.md` and `branching-hexagon-new-two-run-complementary-pp-periodic-cone.md`. Fresh review must independently attack the multiple saturation extractions, all incidence counts, actual mirror conventions, phase normalization, and chain-isometry signs. No computational producer is required for this symbolic necessary mechanism. No Git, log, or previous-artifact edits were made.
