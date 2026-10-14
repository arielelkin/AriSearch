# A sixty-degree pentagon cannot surround an equiangular dodecagon

Date: 2026-10-13. Status: adversarially reviewed VALID; [fresh review](../reviews/sixty-degree-pentagon-equiangular-dodecagon-omission-hostile-review.md).

## Exact statement

Let P be any genuine convex pentagon with one 60-degree corner and four
120-degree corners. Let Q be any genuine convex dodecagon with twelve
150-degree corners. Side lengths are arbitrary and reflections and partial
contacts are permitted. In every admitted plane tiling by P and Q, no Q
occurs. This is an omission theorem, not by itself a classification of P-only
tilings or an unrestricted two-convex impossibility theorem.

## Proof

At a native Q corner, a flat incident tile would contribute 180 degrees,
leaving 30 degrees, smaller than every available native corner. Thus all
incident tiles have native corners there. If exactly one Q corner occurs,
the other angles, integer multiples of 60 degrees, would need to sum to
210 degrees, impossible. Three Q corners already exceed 360 degrees.
Consequently the only native star containing Q is

    150 + 150 + 60 = 360.

In particular, at each Q vertex one incident native Q side has a Q neighbor
and the other has a P neighbor. A Q corner cannot end inside any other tile
side: after the host's 180-degree sector the remaining angle would again
be 30 degrees. Therefore every positive-length Q-Q contact extends along
a whole native side of both tiles; a first ending endpoint in the interior
of the other side would be impossible. The Q-Q side slots of each Q
alternate with Q-P side slots. Choose a native Q-P side e.

At both endpoints of e the P neighbor has its unique 60-degree corner.
Start from one endpoint and follow e. The first P tile occupies a positive
initial interval of e along a native P edge incident to its 60-degree
corner. The other endpoint of that P edge has 120 degrees. The edge cannot extend beyond e's far endpoint, because that would put a native Q150 corner inside a P side, the forbidden 30-degree flat case. It cannot be
the other endpoint of e, whose required P angle is 60 degrees.

At this first internal endpoint, Q contributes the flat 180-degree host
sector and the first P contributes 120 degrees. Exactly 60 degrees remain.
Thus exactly one next P tile starts there at its 60-degree corner. No Q
corner can appear at an internal point of e, by the earlier 30-degree
obstruction. The next P edge again ends at a 120-degree corner. Inductively
every internal transition along e is

    Q host 180 + preceding P 120 + following P 60.

Every successive interval therefore starts at 60 and ends at 120. None
can terminate at e's far endpoint, which requires 60. There cannot be an
infinite sequence accumulating along e: all these intervals are whole
native P edges incident to its 60-degree corner and have length at least
the smaller of the two fixed positive lengths incident to that corner.
Hence e cannot be covered. This contradicts the occurrence of Q.

The possible flat star with three P 60-degree corners does not invalidate
the induction: an interval arriving from the initial endpoint always
ends with a 120-degree corner, leaving only one 60-degree sector, rather
than three. Every step is along actual tile edges, without markings or
an edge-to-edge convention.

## Remaining scope

The pair may still admit a tiling omitting Q. A periodicity conclusion for
that case needs a separate theorem or explicit carrier for the given P.
No count-based edge-to-edge approximation, solver search, metric bound or
literature classification is used in the omission proof.

## Infinite equiangular-partner extension

Status of this extension: independently reviewed VALID in the linked review.

Let n >= 9 be an integer satisfying both n != 2 (mod 4) and n != 4 (mod 16).
Put theta = 720/n, beta = 135 - theta/4 and gamma = 180 - theta/2,
in degrees. Let P have one theta corner and four beta corners; let Q be an
equiangular n-gon with all corners gamma. In every admitted plane tiling
of this pair, Q is absent, at all positive side lengths and with arbitrary
partial contacts.

Here 0 < theta <= 80 < beta < 135 and gamma >= 140. A native Q corner
cannot occur in a flat star because the remainder after gamma + 180 is
theta/2, smaller than every available native corner. Three Q corners
exceed 360. Two Q corners leave exactly theta, filled by one P acute
corner. With just one Q corner, the remaining angle is 180 + theta/2.
It cannot contain two beta corners: their sum is 270 - theta/2, larger
since theta < 90. If it contains no beta, it must contain

    (180 + theta/2)/theta = (n + 2)/4

acute corners, an integer only when n = 2 (mod 4). If it contains one
beta, it must contain

    (180 + theta/2 - beta)/theta = (n + 12)/16

acute corners, an integer only when n = 4 (mod 16). Both cases are
excluded. Therefore every Q vertex again has precisely two Q corners
and one P acute corner. Native QQ contacts are whole on both sides,
and QQ/QP slots alternate. For odd n this alternation already excludes Q.

For even n choose a QP side and repeat the preceding directed-edge proof,
replacing 60 by theta and 120 by beta. A first P acute leg starts at theta
and ends at beta. At an internal endpoint, the host Q contributes 180 and
the preceding guest beta. The remaining angle is

    180 - beta = 45 + theta/4 < beta.

No flat second guest or Q corner fits that angle, so every other guest
corner there is theta. If the number (n + 4)/16 is not an integer, no
such endpoint is legal at all. If it is an integer, several theta sectors
may lie between the preceding P and the outgoing Q-side guest; the guest
incident to the forward ray of the Q side still has a theta corner.
Its entire incident P leg again ends at beta. Thus the directed side
chain can never finish at its far endpoint, where theta is required.
The fixed positive minimum acute-leg length prevents accumulation.

This establishes the same omission conclusion for the stated infinite
family. The excluded residue classes admit additional native Q stars;
no conclusion about those cases is asserted. P-only tilings remain a
separate question, as in the original twelve-sided case.

## Stronger complete size-family obstruction

Status: independently reviewed VALID in the linked review.

For the same definitions theta=720/n, beta=135-theta/4 and
 gamma=180-theta/2, every pair with n>=9 and n!=12 is untileable at every
positive metric. For n=12 the proved Q-omission conclusion remains; no
P-only classification is claimed.

A full star containing A beta corners, B theta corners and C gamma corners
satisfies

    A(3n-4)+16B+4C(n-2)=8n.

A flat-host star has the right side 4n instead. If a beta corner occurs,
A>=1. Since beta>90 and gamma>=140, at a full star the only possibilities
are A=1,C=0; A=1,C=1; A=2,C=0; or A=3,C=0. They respectively require

    B=(5n+4)/16, B=(n+12)/16, B=(n+4)/8, B=(12-n)/16.

The last is possible only at n=12, with B=0. At a flat star containing
beta, only A=1,C=0 is possible, requiring B=(n+4)/16. Consequently beta
can occur in a full or flat star only when n=4 (mod 8). For every other
n>=9, P cannot occur anywhere. Q alone cannot tile: three gamma corners
exceed 360, one or two do not reach 360, and a flat host leaves too little
room for another gamma corner. Therefore these pairs are untileable.

Write the remaining sizes as n=16k+12 or n=16k+4.

For n=16k+12 with k>=1, the earlier directed-edge theorem excludes Q.
The complete P-only full stars are two beta corners plus 2k+2 theta
corners, one beta plus 5k+4 theta corners, and a theta-only full star.
The complete flat-host stars are one beta plus k+1 theta corners, and a
theta-only flat star. Assign weight 1 to theta and -(k+1) to beta.
The two-beta and beta-flat scores are zero. The one-beta full score is
4k+3>0; theta-only stars have positive score. Each entire P tile, however,
has total corner weight 1-4(k+1)=-4k-3<0. This rules out a P-only tiling.
The extra three-beta star at k=0 is why n=12 is excluded from this step.

For n=16k+4 with k>=1, assign the native weights

    theta: 1, beta: -(2k+1)/2, gamma: -1/2.

The complete full stars with a nonacute corner are

    2 beta + (2k+1) theta,
    beta + gamma + (k+1) theta,
    2 gamma + theta.

Every displayed score is zero. The remaining full stars are theta-only,
with positive score. The only flat-host stars are theta-only, again with
positive score. The per-tile totals are

    P: -4k-1 < 0, Q: -n/2 < 0.

Both species therefore have negative corner totals while every interior
star has nonnegative score, an impossibility.

The corner-weight contradiction is unrestricted and requires no frequency
limit: in a square window, sum entire tiles whose centroids lie inside.
Boundary-intersecting tiles lie in a fixed-width boundary collar, whose tile
count is O(R), by positive minimum area and bounded diameter. The fixed
weights and finite corner counts make the difference from summing complete
interior stars O(R). Coverage forces quadratically many tiles, so the
negative tile sum is at most -cR^2 while the nonnegative interior-star sum
is at least zero, a contradiction for large R. This argument also handles
partial contacts: the host's flat sector has no native-corner weight.

The proof covers the full stated size/angle family, not arbitrary pentagons
or arbitrary higher-sided partners. No bounded search or monohedral
classification is imported.

## The twelve-sided exception has an explicit omission escape

Status: independently reviewed VALID in the linked complete review.

At n=12, every P has adjacent 60 and 120 corners. Choose the native edge
joining such a pair, with endpoints A,B, and put h(z)=A+B-z. Convexity
places P and h(P) on opposite closed halfplanes of this supporting line,
so their interiors are disjoint and their union has no gap at the shared
edge. At each endpoint the joined angle is 60+120=180. Delete these two
collinear vertices from the union's boundary: its remaining six native
corners are 120 degrees, so the union is a genuine convex hexagon H.
It is centrally symmetric about (A+B)/2 and consists of two copies of P.

For completeness, every genuine centrally symmetric convex hexagon admits
an elementary translation carrier. Move its center to 0 and list its CCW
vertices v0,v1,v2,-v0,-v1,-v2. Put

    a=v0+v1, b=v1+v2.

The displacement between its first three edges and their opposites is,
respectively, a,b,b-a. Thus all six directed edges pair in reverse modulo
the lattice Za+Zb. Direct expansion gives

    det(a,b)=cross(v0,v1)+cross(v1,v2)+cross(v0,v2)=area(H)>0.

The lattice family is locally finite. Its integer multiplicity has zero
distributional gradient by the three complete opposite-edge pairings and
mean area(H)/det(a,b)=1. Therefore it has multiplicity one almost
everywhere. An interior overlap or open gap would have positive area,
contradicting this equality; closedness by local finiteness gives coverage
of every point. Subdivide each translated H by its original P/h(P) seam.
This is a legal rank-two periodic P-only tiling at every original metric.

Combining this explicit carrier with the independently reviewed size-family
obstruction, no pair in the entire family n>=9, P=(720/n,
(135-180/n)^4), Q=equiangular n-gon, is aperiodic under the unrestricted
problem definitions: n!=12 is untileable and n=12 has a periodic omission
escape. The proof uses no pentagon classification and no matching rule.
