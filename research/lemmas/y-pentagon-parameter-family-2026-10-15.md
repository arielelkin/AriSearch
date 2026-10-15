# A parameterized family of Y pentagon pairs is untileable

Date: 2026-10-15. Status: independently hostile-reviewed VALID. See
[review](../reviews/y-unrestricted-and-family-hostile-2026-10-15.md).
This is a restricted family exclusion, not a solution of research-problem.md.

## Exact family and theorem

Let t be any rational number satisfying

    (5+3sqrt(2))/7 < t < 1+sqrt(2).

Set R=(4t-2)/3, k=(t+1)/3, S=sqrt(2)k, L=sqrt(1+t^2),
and define counterclockwise convex pentagons

    P_t=((0,0),(R,0),(R+1,t),(t,R+1),(0,R)),
    Q_t=((t,1),(t-k,1+k),(-t+k,1+k),(-t,1),(0,0)).

**Theorem.** No tiling of the Euclidean plane by isometric copies of these
polygons exists. Reflections and arbitrary partial-side contacts are allowed.
A common positive similarity of the pair has the same conclusion. At t=2,
P_t is the earlier Y pentagon and Q_t is its earlier partner translated by
(0,-2). The theorem closes an infinite exact rational-coordinate family,
not only the previously retained pair.

We prove a metric-angle obstruction first, then verify its hypotheses for
the entire displayed parameter interval. All coordinates here are rational;
the square roots occur only in lengths.

## Abstract obstruction

Suppose two genuine convex pentagons have native corner/side cycles

    P: r --R-- a --L-- b --S-- b --L-- a --R-- r,
    Q: c --S-- g --R-- g --S-- c --L-- d --L-- c,

where

    r=pi/2, a=pi-theta, b=pi/4+theta,
    c=3pi/4-theta, g=3pi/4, d=2theta,
    pi/4 < theta < 3pi/8, theta/pi irrational,
    0<S<R<L<2S, 2R != 3S, 2L != 3S.

Then the two polygons admit no plane tiling under the unrestricted
conventions. These are explicit hypotheses, not assumptions on an unknown
candidate in the main problem.

### Local preliminaries

The smallest native angle is c>3pi/8>pi/3. At any actual tiling vertex,
there is at most one flat sector if a native corner is present. Such a
vertex contains finitely many tiles. Local finiteness follows by choosing
one contained disk of common positive radius in each reference shape:
the disk centers of tiles meeting a bounded set lie in a larger bounded
set and their disks have disjoint interiors.

Use angle coordinates in the independent basis (pi/4,theta):

    r=(2,0), a=(4,-1), b=(1,1),
    c=(3,-1), g=(3,0), d=(0,2).

Solving the two integer coefficient equations for at most five native
corners gives exactly the full stars

    rgg, aad, abg, rrrr, rrbc, rccd, bbcc.

With a flat sector the remaining native stars are precisely rr and bc.
This finite inventory is directly enumerable and checked by the replay.
In particular no A, D, or G corner can lie strictly inside another tile's
native side: their flat residuals theta, pi-2theta, pi/4 are each less than
c. A B at a flat side forces C, and a C at a flat side forces B.

### Endpoint obstruction on a right arm

If a P right corner R meets a Q corner G, and Q uses its short GC arm
along one of that P's RA arms, C lies at distance S from R inside RA,
since S<R. At C the P contributes a flat sector, forcing a B corner.
An arm of that B tile follows the remaining host RA ray. Its native length
is at least S, while the distance left to the host A is R-S<S. Thus host A
lies strictly inside that B arm. This is impossible by the preceding
flat-residual test. Consequently a G adjacent to R along an RA ray must
use its GG arm of length R and match that entire RA side.

### Every GG side has a full native mate

Its endpoints are G and cannot lie strictly inside a guest side. Thus any
positive contact intervals covering GG end or start at genuine guest
vertices at the two endpoints. An interior transition between guests is
also a genuine endpoint of each adjoining guest side: an interior point
of a convex guest side would occupy the whole opposite half-plane and
leave no angular room for another guest there. Consequently, if GG had
any interior transition, at least two complete guest native sides would
partition it, of total length at least 2S>R, impossible. Hence GG matches
one whole side of length R, either GG or RA.

A GG/GG match has at each endpoint two G corners. The unique completion is
R, since the residual is pi/2 and two smallest native corners exceed it.
Each adjacent G uses GC along one of that R's RA arms. The right-arm
obstruction rules this out. Therefore each GG has an RA mate. At its R-G
endpoint the completion is again RGG. The other G along the second RA arm
must also use its full GG by the right-arm obstruction. Both A corners of
this actual P therefore meet G, hence each is completed by B in an ABG
star. This conclusion does not assert that all sides in a tiling are full.

### Every BB side has a full native mate

Normalize a P BB side as [0,S] with P below its supporting line. Since S
is the shortest side, there are at most one interior guest transition:
between two consecutive transitions would lie a full native side shorter
than S. A guest corner on the interior of BB must be one of rr or bc.

If a guest side overhangs a B endpoint, that endpoint has a flat sector
opposite the host B, forcing C on the host's outside. The C arm along the
host's BA side must be CD of length L: if it were CG of length S, its G
endpoint would lie inside BA of length L, impossible. Thus its CG arm of
length S lies on the continuation of BB. These forced continuation segments
are the guards [-S,0] and [S,2S], whenever the corresponding endpoint is
overhung. A guest outward endpoint of type A,D,G must coincide with the
far guard G: before it gives a forbidden corner against a flat guard; after
it puts guard G inside a flat guest side.

If the unique transition is at z in (0,S), both guests extend beyond their
respective host endpoints because their native sides have length at least
S. Both guards therefore exist. For rr, horizontal arms are both RA, and
their far A endpoints force z-R=-S and z+R=2S, hence 2R=3S, excluded.
For bc, C cannot use CG horizontally: its far G would fall inside the
guard. Thus C uses CD horizontally and CG on the internal common ray.
If B used BB horizontally, its BA internal arm of length L would contain
that C tile's G at distance S, impossible. Hence B uses BA horizontally.
Both horizontal arms now have length L, with far types A and D, forcing
z-L=-S and z+L=2S, hence 2L=3S, excluded. Reflections and both orders are
included because the two arm lengths in each argument are equal.

If there are zero transitions, a single guest side contains [0,S]. A
length-S side is exactly the desired mate. A longer side has length R or
L, both less than 2S. Every longer native side has at least one endpoint
of type A,D,G. If it overhung both host endpoints, its forbidden endpoint
would have to coincide with a far guard, requiring total length at least
2S to reach the other host endpoint, impossible. It must therefore be
flush at one end and overhang the other. The far endpoint is inside the
corresponding guard, so must be R, B, or C. The only surviving directed
profiles are consequently RA flush at A, AB flush at A, or CD flush at D.

For flush D+B, the residual 7pi/4-3theta is less than 2c (theta>pi/4),
so at most one corner could fill it. No native corner has theta coefficient
-3, impossible. For flush A+B the unique missing corner is G. If the
horizontal guest side is RA, both other rays have native length L; G's
GG arm ends at distance R<L inside one of them, impossible. If the
horizontal guest side is AB, its other A arm is RA of length R. The G
must put GG on RA (otherwise again G lies inside the host BA of length
L). G's GC arm ends at C inside that host BA, forcing B against its flat
sector. A B arm of length at least S then follows the remaining host ray
of length L-S<S, putting host A inside it, impossible.

This exhausts all BB contact patterns and proves the full-mate assertion.
Only P BB and Q CG have length S.

### Final native propagation

Take a Q occurrence. Its GG mate is RA, and the preceding argument forces
both A corners of that same P into ABG stars. Follow either P AB side from
its A endpoint. Its neighboring B corner could use BA of length L or BB
of length S on that ray. BB is impossible: its mandatory full length-S
mate cannot be this host's longer native AB side. The neighbor therefore
uses BA, giving a full AB/BA match. At the far end, the original P B meets
A and hence G in an ABG star. This occurs at both ends of its BB side.

The full mate of this BB side would have G at both endpoints. No native
length-S side has endpoints GG: the only choices are BB or CG. Contradiction.

If no Q occurs, the full star inventory leaves only rrrr among P-only
native stars, and rr with a flat; actual A and B corners cannot be covered.
Thus a P-only tiling also cannot exist. Q-only tilings were already excluded
by the GG/RA implication. This proves the abstract obstruction.

## Verification of the entire exact family

Put theta=atan(t). The interval begins at t0=(5+3sqrt(2))/7>1 and ends
at 1+sqrt(2)=tan(3pi/8); thus pi/4<theta<3pi/8. For rational t in this
interval, theta/pi is irrational. Otherwise exp(2i theta) would be a root
of unity; its rational real part would make

    2cos(2theta)=2(1-t^2)/(1+t^2)

a rational algebraic integer, hence one of -2,-1,0,1,2. The only positive
rational tangent values from this list are 1 (and the zero boundary case),
contrary to t>1. The possibilities t^2=1/3 or 3 are irrational tangents.

The displayed coordinate cycles have angles r,a,b,b,a and c,g,g,c,d;
all are strictly between zero and pi. Their positive edge lengths are
respectively R,L,S,L,R and S,R,S,L,L. Direct vector turns or elementary
right triangles verify these facts; the exact replay reconstructs them.
In particular the polygons are genuine convex pentagons and are distinct:
P has a right corner and Q has none on this interval.

The length inequalities follow without sampling. Explicitly,

    9(R^2-S^2)=14t^2-20t+2,
    9(L^2-R^2)=-7t^2+16t+5,
    9(4S^2-L^2)=-t^2+16t-1.

The first is positive for t>t0. The second is concave and positive at both
endpoints t0 and 1+sqrt(2), hence throughout the interval. So is the third.
Thus S<R<L<2S. Since R is positive rational and S is positive rational
multiple of sqrt(2), 2R != 3S. Also

    4L^2-9S^2=2(t-1)^2>0,

so 2L != 3S. Every abstract hypothesis now holds.

## Exact computation and limitations

Replay (no solver, randomness, or finite patch depth):

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/y-pentagon-family-2026-10-15.py

Finite domain: all multisets of the six indexed angle kinds of size 1..5
for a full star and 1..2 for a flat complement; symbolic identities in one
rational variable t; sign checks at the two exact algebraic endpoints for
three quadratic polynomials. The proof itself quantifies over every rational
t in the stated open interval and over all admitted unrestricted tilings.
No bounded failure to find a tiling is used.

Dependencies: elementary Euclidean geometry and local finiteness, plus
irrationality of a rational algebraic integer's nonintegral value. The
argument reproduces the needed shortest-side guard proof; it does not rely
on a numerical extension of the t=2 script. No claim about arbitrary
pentagon pairs, other parameters, or the main unrestricted objective follows.
Independent hostile review is VALID for the abstract and rational-family
claims. The independently reconstructed checker is
`research/searches/y-family-independent-hostile-check-2026-10-15.py`.
The [literature boundary](../literature/y-pentagon-family-boundary-2026-10-15.md)
records the limited prior-art search; no universal priority is claimed.
