# Hostile whole-theorem review: regular pentagon and full 126°/144° partner palette

Date: 2026-10-19. Verdict: **PASS** for the restricted theorem: if a unit regular pentagon P and any compact strictly convex polygon Q whose every native interior angle belongs to {126°,144°} tile the plane under arbitrary isometries and unrestricted contacts, the pair admits a doubly periodic plane tiling. This asserts existence of a periodic tiling, not periodicity of every admitted tiling. It does not solve the unrestricted research problem.

The manuscript reviewed is `research/lemmas/regular-pentagon-126-144-partner-periodicity-synthesis-sol-2026-10-19.md`, read after it appeared. At review time it still called the q-dimer premise pending and the theorem conditional. The completed q-dimer hostile review and its independently replayed checker discharge that premise. Those status labels should be updated; they are stale administrative qualifications, not a remaining mathematical lemma. No additional angle hypothesis is needed. In particular, “belongs to” permits an all-144° partner; that Q10 case is explicitly excluded. It need not be assumed that both angles occur.

## Sources and independent work

Read AGENTS.md, research-problem.md, research-protocol.md, the synthesis, Q7 and Q8 first-gate reports, Q7 full-family lemma, Q8 AA-capacity lemma including Q9/Q10 corollary, both Q8 periodic lemmas, and relevant hostile reviews. Independently reconstructed the following analytic chain rather than accepting a collection of component PASS labels. Inspected the three positive independent checker sources and replayed all three successfully; their source contains no producer-code imports. Existing exact carrier tables are used as finite certificates, with the global inference separately audited below. No new bounded tiling search or literature claim enters this review.

## Contacts and angle stars

Let D be the larger tile diameter and m the smaller positive tile area. Every tile meeting a compact K lies within its D enlargement. Since their interiors are disjoint, area bounds the number of such tiles by that enlargement area divided by m. This proves local finiteness, including boundary-only contacts, so small-circle sector counting is valid.

A corner lying in an open side leaves 180° after the side tile's straight sector. One remaining corner is less than 180°; two or more total at least 216°. Two straight sectors already consume the circle. Thus corner-on-open-side contacts are impossible. Crossing open sides would cause interior overlap. Any neighbor change along a side would create a forbidden corner-on-open-side endpoint. Consequently every full side has one full-side neighbor of equal length. This conclusion is derived for unrestricted tilings, including reflections.

At a vertex two corners total at most 288°, while four total at least 432°. Exactly three meet. Solving 6p+8a+7b=20 gives only (p,a,b)=(2,1,0),(1,0,2). These are PPQ at A and PQQ at B. No all-P or all-Q star exists, so omission of either prototile cannot produce an overlooked monohedral tiling. At A both Q edges face P; at B exactly one faces P and one faces Q. A QQ edge must therefore be BB, and the QQ edges form a perfect matching of B vertices on the cyclic boundary. All other edges have the unit P length. Equal numerical lengths never change these endpoint-imposed roles.

## Complete discrete classification

The angle sum is exactly 2a+3b=20. Nonnegative integer solutions have b even and 0≤b≤6, giving only (a,b,n)=(1,6,7),(4,4,8),(7,2,9),(10,0,10). In particular A is always present, so no overlooked all-B cyclic matching exception exists.

Cutting at A vertices gives B paths; each needs an internal perfect matching. Each path has even length and its matching is unique, by matching its first endpoint and induction. For Q7 the sole word is ABBBBBB, with private edges 1,3,5. For Q8, B-run partitions are 4 or 2+2. The former gives AAAABBBB, private edges 4,6. The latter has positive A-run lengths summing to four, so up to reversal/interchange they are 1+3 or 2+2, giving AAABBABB (3,6) and AABBAABB (2,6). For Q9 the two B vertices must be adjacent; for Q10 all corners are A. Rotation and reflection remove no physical congruence class because the problem permits all isometries. This is an analytic exhaustive list, independent of first-gate enumeration output.

## Complete metric transfer

Choose the counterclockwise boundary orientation (reflecting the input if needed), a listed cyclic starting vertex, and rotate its first public edge to direction 1. Its length is already one, forced by P; this normalization imposes no restriction on Q. Turns are 36° at A and 54° at B, fixing all directed rays.

For Q7 the private directions are w³,w⁹,w¹⁵. The first two are real linearly independent. The exact particular solution (t,t,t) and kernel vector (1,k,1), t=2cos18°, k=2cos72° in (0,1), therefore give every real solution, not just algebraic ones. Lengths are (1,t+h,1,t+kh,1,t+h,1); positivity is precisely h>−t since the middle private length is (1−k)t+k(h+t). The replayed AA[x] checker proves all 35 supporting tests for Q and 15 for P coefficientwise positive at x=h+t>0. Thus the entire necessary metric interval, including transcendental h, has genuine simple strict convexity and a positive carrier.

For AABBAABB, directions are (0,2,5,8,10,12,15,18) in powers of w. The six public unit vectors sum to zero and private vectors w⁵,w¹⁵ are opposite; closure is exactly equality of private lengths h>0. There is no second parameter. The independently replayed checker proves all 48 strict supporting inequalities throughout h>0 as coefficientwise positive polynomials. For AAABBABB, private directions w⁷,w¹⁵ have nonzero real determinant. The q-dimer checker independently solves the real two-variable closure system and obtains equal positive lengths t. Hence this isolated metric is exhaustive. No metric solving is needed for the capacity-excluded word. Reflections are covered by congruence, and private/public length coincidences do not create alternate angle-compatible matchings. No omitted scaling is possible because public sides face the fixed unit P.

## Capacity and finite-window rigor

At any P corner, two incident PP sides would demand a PPP star, impossible. Thus PP side positions form an independent set of its five-cycle, of size at most two. A P side receiving an AA edge must have its two flanking sides PP. Two nonadjacent positions of a five-cycle have exactly one common flanked position; therefore each physical P receives at most one AA edge. This also handles pentagons with fewer PP sides and hypothetical repeated neighbors. Reflection changes nothing.

Count references in [0,R]². Every discrepancy between tile counts, corner counts and neighboring references occurs in a fixed-width boundary strip. Enlarge that strip by D and divide its O(R+1) area by m; this bounds all involved tiles uniformly over the tiling. With V_A,V_B the two star counts, V_A=a q_R+O(R+1), 2V_B=b q_R+O(R+1), and 5p_R=2V_A+V_B+O(R+1). Hence p_R=c q_R+O(R+1), c=(2a+b/2)/5. Injecting AA sides into their receiving P gives m_AA q_R≤p_R+O(R+1). If m_AA>c, then q_R and p_R are O(R+1). Coverage requires R²≤M(p_R+q_R+O(R+1)), M the larger tile area, a contradiction. No density limit, positive Q frequency, periodic exhaustion or pointwise saturation is assumed.

The excluded values are Q8 AAAABBBB: m_AA=3>c=2; Q9 adjacent BB: m_AA=6>c=3; Q10 all A: m_AA=10>c=4. Other Q9 words fail matching already. This proves all negative cases for arbitrary real metrics and reflected contacts.

## Positive global carriers

The remaining shapes are exactly the Q7 whole interval, Q8 AABBAABB whole interval and isolated Q8 AAABBABB. The three independent exact checkers completed exit 0:

- `sage research/reviews/regular-pentagon-heptagon-periodic-transfer-hostile-sol-2026-10-19.sage`: AA[x] convexity, all twelve edge-pair identities, eight single vertex cycles, connectedness, positive determinant and exact area identity for every x>0.
- `sage research/reviews/regular-pentagon-octagon-minimal-carrier-hostile-sol-2026-10-19.sage`: all-positive-parameter Q convexity, nine edge pairs, six single vertex cycles and positive determinant/area identity. Its extra 4,320-case domains are unnecessary to the existence inference.
- `sage research/reviews/regular-pentagon-octagon-qdimer-hostile-sol-2026-10-19.sage`: independently solved private lengths, strict convexity, eighteen uniquely recovered lattice mates, twelve single vertex cycles, connectedness, positive determinant and equal total area. Its complete translate-bound intersection audit also passed all 36 nonidentity candidates.

Every command was prefixed by `mise exec -- conda run --no-capture-output -n arisearch`. The checkers were inspected, not merely executed. The first two prove polynomial identities and positivity over entire open real parameter intervals; they do not sample parameters. The last solves the isolated algebraic metric exactly.

The common global proof is sound. Reverse full-edge pairings make a compact oriented surface; each single link circle and positive total angle 2π gives a genuine Euclidean vertex neighborhood. Connectedness is checked or immediate from the displayed pairing graph. Endpoint congruences define a continuous map to the rank-two lattice torus. Positive orientation gives opposite sectors at each edge and one full positive winding at each vertex, so this is a local isometry everywhere. A compact local homeomorphism to the connected torus is a finite surjective covering. Its degree equals positive total face area divided by lattice covolume, exactly one. It is therefore a homeomorphism, and the lifted faces cover the plane with pairwise disjoint interiors. This does not infer coverage from a bounded patch, and it does not assume the developed representatives are already disjoint. Nonzero rank-two lattice periods follow.

## Defects, repairs and final scope

No substantive mathematical defect or missing lemma was found. The manuscript's stale pending q-dimer labels can now be replaced by its completed reviewed positive-carrier premise. The theorem requires exactly the stated angle-membership hypothesis, strict convexity, fixed unit regular P and unrestricted isometries. It needs neither “both angles occur,” algebraic lengths, positive frequency, edge-to-edge input, prescribed chirality, nor any generic-length assumption.

The valid conclusion is that every tileable pair in this restricted palette has at least one doubly periodic tiling. It does not assert every tiling is periodic, nor exclude partners with other angles or a nonregular pentagon. No novelty claim was audited. No Git or discovery-log edit was made.
