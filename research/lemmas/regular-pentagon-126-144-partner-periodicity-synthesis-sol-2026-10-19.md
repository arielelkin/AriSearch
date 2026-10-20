# Regular pentagon with the full 126°/144° partner palette

Date: 2026-10-19. **Complete restricted theorem; independent whole-proof hostile review PASS.** The [whole-proof review](../reviews/regular-pentagon-126-144-whole-synthesis-hostile-sol-2026-10-19.md) audited the full case split, unrestricted contacts/reflections, metric completeness, boundary counting and all three independently reviewed periodic carriers. This is a scoped theorem, not a solution of the unrestricted two-convex-polygon problem. No novelty assertion is made.

## Exact theorem

Let P be a regular pentagon of side length one, and let Q be any compact strictly convex polygon each of whose native interior angles belongs to {126°,144°}. Isometric copies of either polygon, including reflected copies, may meet with unrestricted contacts, and use of both types is not assumed. If {P,Q} tiles the Euclidean plane, then {P,Q} admits a tiling invariant under a rank-two lattice of translations. In particular it admits a nonzero translational symmetry.

The q-dimer positive existence certificate and global covering argument have passed independent hostile review; completeness of its finite carrier search is unnecessary. The full synthesis also passed [independent whole-proof hostile review](../reviews/regular-pentagon-126-144-whole-synthesis-hostile-sol-2026-10-19.md). Arbitrary positive real side lengths, including transcendental parameters, are covered.

## Unrestricted-contact reduction

A tiling by these two fixed positive-area bounded shapes is locally finite: tiles meeting a compact set lie within its fixed-diameter enlargement, and their disjoint positive-area interiors bound their number. Thus the sector argument at every tile corner is legitimate. Every native angle is at least108° and less than180°. A corner on a side interior would leave180° to be filled by native corners, impossible with one corner or with two or more. No native corner lies in any other tile side interior. Crossing side interiors would force overlapping interiors. Therefore every side is shared whole with one other side: a change of neighbor along it would create the forbidden corner-on-side contact. Unrestricted contacts have consequently become edge-to-edge.

At a vertex there are exactly three corners (two are too small and four exceed360°). In units of18° the available angles are6,8,7. The only sums equal to20 are6+6+8 and6+7+7. Hence the only stars are PPQ at an A=144° corner, and PQQ at B=126°. This also rules out a tiling using only one prototile. Reflections change neither argument.

At A both incident Q sides face P. At B one incident Q side faces P and the other faces Q. Thus the QQ sides form a perfect matching of B corners in the cyclic boundary graph. Every other Q side faces a unit P side, so has length exactly one. This derives side roles from geometry, with no assumption of generic lengths or marked edges. Accidental equalities between private and public lengths do not create additional role assignments. The matching is selected by the tiling, not by testing which lengths coincide.

## Exhaustion of side counts and angle words

Write a,b for the counts of A,B. The angle sum gives

    144a+126b=180(a+b-2), hence 2a+3b=20.

Nonnegative integral solutions are exactly

    (a,b,n)=(1,6,7),(4,4,8),(7,2,9),(10,0,10).

Indeed b is even and0<=b<=6; substituting b=0,2,4,6 gives precisely these four cases. No unspecified side count remains.

If A occurs, break the cyclic word into maximal B runs. Every B run must have even length: a QQ side cannot meet A, so its B-path needs a perfect matching. Each even B path has exactly one matching, pairing consecutive vertices from either endpoint. Odd B runs are impossible regardless of metric.

For n=7 the only word up to rotation/reflection is ABBBBBB, with QQ sides1,3,5 when the sole A is vertex0 and side i starts at vertex i. For n=8 the B runs are either one run of4, giving AAAABBBB, or two runs of2. In the latter case the two positive A-run lengths total4, so are1,3 or2,2 up to interchange. These give AAABBABB and AABBAABB. This proves word completeness without relying on a numerical search. Their QQ indices are respectively(3,6),(2,6); for AAAABBBB they are(4,6). For n=9 the B pair must be adjacent; the only word is AAAAAAABB. For n=10 the word is AAAAAAAAAA and there are no QQ sides. All statements are up to dihedral relabeling, which is permitted by unrestricted isometries.

## Capacity exclusion, including zero-frequency attacks

On a P, PP sides cannot be consecutive: the common corner would see three P sectors, contrary to the star list. There are therefore at most two PP sides. A PQ side facing an AA side must have PP sides immediately before and after it. In the five-cycle of P sides, two nonconsecutive sides flank at most one intervening side. Each physical P can consequently face at most one AA side of Q. This includes repeated-neighbor possibilities and pentagons with fewer than two PP sides.

For a square of side R, count tile reference points inside it as p_R,q_R. A fixed-width boundary strip meets O(R+1) tiles, uniformly over all tilings: enlarge the strip by a maximum tile diameter and divide its area by the smaller tile area. Every corner or neighbor counting discrepancy lies in such a strip. Counting PPQ and PQQ corners gives

    5p_R=(2a+b/2)q_R+O(R+1).

If each Q has m AA sides, injection of those sides into their P neighbors gives

    mq_R<=p_R+O(R+1).

Thus m>(2a+b/2)/5 forces q_R=O(R+1), then p_R=O(R+1). But coverage and bounded tile areas require p_R+q_R=Omega(R²), a contradiction. This uses no density limit or assumption that Q has positive asymptotic frequency.

For Q8 word AAAABBBB, m=3 whereas the corner ratio is2. For Q9 the adjacent B pair leaves six AA sides whereas the ratio is3. For Q10 there are ten AA sides whereas the ratio is4. All are impossible. Other Q9 words already fail the B-matching condition. Only Q7 and the two remaining Q8 words need positive carriers.

## Complete necessary metric families

Let w=exp(2πi/20), t=w+w^(-1)=2cos18°, k=2cos72° in(0,1). Normalize the first directed Q side to1. Directions follow solely from the angle word: outgoing direction at vertex i is the preceding direction multiplied by w² at A_i or w³ at B_i. Every public side has length1. Closure is two real linear equations in the remaining QQ lengths; it is essential to solve these equations, rather than merely exhibit a convenient metric.

For Q7 the directions are w^(3i),0<=i<=6. Closure has real kernel spanned by(1,k,1) on private indices1,3,5, since directions w³,w⁹ are not parallel. A particular solution is(t,t,t). The entire necessary family is therefore

    lengths=(1,t+h,1,t+kh,1,t+h,1), h>-t.

The middle private length remains positive on this interval because t+kh=(1-k)t+k(h+t)>0. Conversely positive private lengths force h>-t. The reviewed transfer verifies strict supporting half-plane inequalities throughout this interval, so every member is a genuine strictly convex heptagon.

For AABBAABB the direction exponents are(0,2,5,8,10,12,15,18). Its private directions w⁵,w¹⁵ are opposite, and the six public unit vectors sum to zero. Thus closure forces precisely the equal private lengths h,h with h>0. There is no additional parameter. The reviewed carrier verifies strict convexity for every h>0.

For AAABBABB the exponents are(0,2,4,7,10,12,15,18). The two private directions w⁷,w¹⁵ are not real parallel. Closure uniquely forces both private lengths to t. The first-gate independent review checks this exact solution and all strict supporting inequalities. AAAABBBB is already excluded without needing its isolated metric. These arguments cover arbitrary real lengths and all reflection classes; an arbitrary reflected input Q is congruent to one of the normalized representatives or its reflected copy, which defines the same allowed congruence class.

## Positive existence premises and global mechanism

The following exact existence results finish the finite case split. They concern existence of one periodic tiling for each necessary metric; no classification of all admitted tilings is needed.

1. Q7: the four-face carrier has2P+2Q for every h>-t. Its reviewed construction and proof are [whole-interval transfer](../searches/regular-pentagon-heptagon-periodic-transfer-sol-2026-10-19.md) and [independent hostile review](../reviews/regular-pentagon-heptagon-periodic-transfer-hostile-sol-2026-10-19.md). With P vertices partial sums of w^(4j) and Q vertices partial sums of the edge vectors above, its developed faces are P,1-P,1-w⁶Q,w⁶Q. Its lattice is L1=wh+2w⁴+w²+2 and L2=(w⁷-w⁵+w³-w)h+3w⁶-w⁴+w²-3. Writing x=h+t, its positive covolume is sin36° x²+(4+k)x+2t+4sin36°, equal to2area(P)+2area(Q).
2. Q8 AABBAABB: the reviewed three-face carrier has2P+Q for every h>0. See [minimal carrier](../searches/regular-pentagon-octagon-minimal-carrier-sol-2026-10-19.md) and [independent hostile review](../reviews/regular-pentagon-octagon-minimal-carrier-hostile-sol-2026-10-19.md). Developed faces are P,1-P,1+w⁴-w⁴Q. The lattice is L1=w⁶+w⁴+w² and L2=(w⁷-w⁵+w³-w)h+2w⁶-1; its determinant is positive for all h>0 and equals2area(P)+area(Q).
3. Q8 AAABBABB: the **independently reviewed** six-face carrier has4P+2Q for its unique metric. See [q-dimer construction](../searches/regular-pentagon-octagon-qdimer-carrier-sol-2026-10-19.md), its companion Sage script and JSON. The six rotations are(w⁶,w⁸,w¹⁶,w¹⁸,1,-1), translations(0,w⁴+1,2w⁶-w⁴-2,w⁶+w²,w⁶-1,w⁶-w⁴-1), and lattice basis L1=w⁶-2w⁴-w²-3, L2=-3w⁶-2w²+2. Its positive determinant is -13w⁷+8w⁵-3w³+16w=4area(P)+2area(Q). Its18 full edge-pair endpoint equations and12 single vertex links are explicitly retained in that report and certificate. Its positive geometry and global covering proof are independently validated in the [q-dimer hostile review](../reviews/regular-pentagon-octagon-qdimer-hostile-sol-2026-10-19.md), including an additional exhaustive 36-translate intersection check.

For clarity, the common global implication of those certificates is as follows. Glue the oriented polygon disks along the prescribed reversed full edges. Every dart is paired once, the face adjacency is connected, and each vertex has a single link of three positive corners summing to2π. The quotient is a compact connected surface locally Euclidean at vertices as well as edges and face interiors. Exact endpoint congruences define a map to the flat torus of the stated rank-two lattice. Across each edge the oriented interiors lie on opposite sides; around each vertex the consecutive positive sectors turn exactly once. Thus the map is a local isometry everywhere. Compactness and connectedness imply a finite surjective covering of the target torus. The exact equality of positive total face area with positive lattice covolume makes its degree one. The lifted faces tile the whole plane with disjoint interiors and both lattice periods. No bounded overlap test or finite-patch extension assumption supplies this global step.

The three existence premises are explicit finite gluing certificates plus algebraic identities; their complete edge tables remain in the linked source artifacts to avoid introducing a second inconsistent transcription. The present proof is self-contained at the synthesis level, with those stated exact carrier lemmas as dependencies. It is not an independent replay of their certificates.

## Conclusion and review scope

Starting from an arbitrary tiling forces one of the four side counts, the complete word list, and the necessary metric families above. Capacity eliminates Q9,Q10 and AAAABBBB Q8. The reviewed carriers cover all Q7 and AABBAABB Q8 metrics. The independently reviewed q-dimer existence result covers the last isolated AAABBABB metric, completing the restricted theorem.

The [independent whole-proof review](../reviews/regular-pentagon-126-144-whole-synthesis-hostile-sol-2026-10-19.md) found no substantive mathematical gap. It checked local finiteness and unrestricted-contact reduction; the exhaustive Diophantine and even-B-run classification; native-index/direction conventions; metric necessity under reflections and accidental length equalities; local AA capacity and uniform boundary estimates without density limits; coverage of the full real parameter intervals; and the global covering argument of each imported carrier. Search completeness at minimal carrier inventory is unnecessary for this theorem, as are pointwise saturation conclusions for P. The q-dimer hostile review validated its positive geometric certificate and degree-one argument, beyond its finite enumeration.

No Git operation or discovery-log edit accompanies this synthesis.
