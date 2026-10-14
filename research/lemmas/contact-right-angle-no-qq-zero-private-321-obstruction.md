# Conditional zero-private (3,3,2) native-mask obstruction

Date: 2026-10-13. Status: independently reviewed VALID under the stated source hypotheses; [component review](../reviews/contact-right-angle-zero-private-generic-hostile-review.md). Exact symbolic mask checker passed.
This is a changed residual all-R geometry, not a claim that arbitrary zero-private shapes force all-R fields.

## Statement and assumptions

Let P have angles 90,112.5,112.5,112.5,112.5 and indexed CCW lengths (x,u,v,y,w), with all five lengths pairwise distinct. Let Q have eight 135 angles, all native side values in {u,v,w}, and native multiplicities a permutation of (3,3,2). There is no edge-to-edge plane tiling in which all P are type R and every Q has exactly two QQ sides. Type R means Q on u,v,w and P on x,y. Reflections are admitted. No privacy or restriction on equality between distinct occurrences of the same native length is assumed.

The statement is conditional on an actual tiling's contact types. It does not itself prove that every unrestricted zero-private pair reduces to this domain. The [reviewed generic synthesis](contact-right-angle-no-qq-generic-zero-private-reduction.md) supplies the reduction for its five-distinct/no-host family. The independent native reduction gives QQ separation three or four; all Q contacts are whole sides.

## Local bevel endpoint ledger

At a public Q side bordering a QQ endpoint, the P guest has its acute corner there and matches u or v. At the other endpoint its exposed PP side is x for a u guest and y for a v guest. A middle public side, with neither endpoint bordering QQ, matches P side w; its two exposed PP sides are x and y, one each. Because x!=y, consecutive guests at a PPQ corner must expose the same one of these indexed bevels.

For a distance-three mask rooted at QQ slots 0,3, the short two-public run has equal acute tags a,a: their exposed bevels must coincide. In the long run (c,w,w,d), the first w guest exposes the bevel of c then the other bevel; the next w guest must expose that other bevel then the original bevel. Consequently d=c. Thus the word is (A,a,a,B,c,w,w,c), with a,c in {u,v}. For a distance-four mask rooted at 0,4, each three-public run (a,w,b) has opposite acute tags b=the other of {u,v}, by the same two-end ledger.

In multiplicity (3,3,2), a=c in the distance-three case is impossible: it would give four occurrences of one native value in public slots alone. Hence its public counts are exactly two of each u,v,w. Distance-four already has exactly two of each. The two QQ values A,B are therefore the two values of native multiplicity three and are distinct. This conclusion is pointwise and uses no density limit.

## Complete symbolic closure and eligible-mask enumeration

Set r=sqrt(2) and directions d_i=(cos(i*pi/4),sin(i*pi/4)). Exact closure is sum L_i*d_i=0 in Q(r)^2. There are 36 rooted indexed words after filtering the two local-tag forms by native counts (3,3,2). The standalone checker

    research/searches/contact-right-angle-no-qq-zero-private-321-mask-check.py

constructs that entire domain, computes the exact two-by-three length-coefficient matrices, and checks every cyclically rooted eligible mask. It imports no producer and uses no metric sampling. Rank-two cases have no positive kernel ray with three distinct coordinates. Rank-one cases with two nonzero coefficients force equality of two native values. The only remaining words and scalar closure rows, in coefficient order (u,v,w), are:

    uuwvwvwu : (1+r,-r,-1)
    uvwuwuwv : (1-r,r,-1)
    vuwvwvwu : (r,1-r,-1)
    vvwuwuwv : (-r,1+r,-1)
    wuwvuvwu : (r-1,-r,1)
    wvwuuuwv : (-1-r,r,1)
    wuwvvvwu : (r,-1-r,1)
    wvwuvuwv : (-r,r-1,1)

Every one has its unique eligible QQ native mask {0,4}. This includes every candidate mask under cyclic indexing; QQ distance five is the reversed distance-three case. The verifier explicitly tests all eight cyclic roots against both local tag forms. Therefore an actual neighboring Q must also use that same eligible mask. Its two QQ lengths are different, so a QQ contact at slot 0 must meet slot 0, and at slot 4 must meet slot 4. Public occurrences of the same numeric value cannot be used as QQ sides, by the eligible-mask conclusion.

## Same-tag endpoint contradiction

In each of the eight words, the public native sides immediately before and after each QQ slot have the SAME tag: both u or both v. Given a full contact between a native segment and the same indexed segment of a congruent polygon on its other side, there are exactly two geometric isometries: reflection in the segment's supporting line, or half-turn about its midpoint. The former preserves the endpoints and the latter exchanges them. In either case the two outgoing public sides at either seam endpoint therefore have the same length, because both endpoint tags of that slot coincide. But this seam endpoint is a P90+Q135+Q135 star. Its P90 guest must have its two incident sides of lengths u and v. Equality of those two outgoing public side lengths contradicts u!=v. Both permitted QQ attachment geometries are impossible. An actual tiling needs a QQ edge, so no assumed tiling exists.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/contact-right-angle-no-qq-zero-private-321-mask-check.py

Observed: PASS, 36 rooted closure domains, eight residual distinct-metric words, unique mask {0,4} in each. No infinite tiling existence, substitution, privacy forcing, or global classification of zero-private pairs is asserted.
