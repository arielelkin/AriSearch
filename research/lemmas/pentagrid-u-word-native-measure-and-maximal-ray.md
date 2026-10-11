# Native-corner measure reduction and a finite mirror-U obstruction

**Status:** adversarially reviewed; the [fresh hostile review](../reviews/pentagrid-u-word-native-measure-and-maximal-ray-review.md) is VALID for the native-measure reduction, finite mirror-U untileability, and finite-U edge-to-edge obstruction. The
extension to every asymmetric U metric is unresolved. This does not resolve
the unrestricted two-convex-polygon problem.

## Statement and exact metric form

Let F be any nonempty finite collection of genuine convex pentagons, each
having cyclic angles(36,108,144,144,108) degrees, up to rotation and reflection
of its vertex word. Arbitrary positive side lengths and all isometries are
allowed. If F tiles the plane, it has an admitted translated-limit tiling with only
the three zero-weight star types listed below. If, additionally, every
reference shape has equal acute-incident lengths A=B, then F admits no
plane tiling. Both statements allow unrestricted partial-edge contacts and
omission of any types. There is no algebraicity or common-scale assumption,
and no monohedral classification is imported. Additionally, no such finite F admits an edge-to-edge plane tiling, even when its metrics are asymmetric.

For each reference polygon choose a counterclockwise labeling with angles
after successive sides equal to(1,3,4,4,3)*pi/5. The lengths are(A,B,b,c,d);
the acute36 corner lies between A,B, and c joins the two144 corners.
The b,d sides each join144 to108. Let z=exp(pi*i/5), phi=(1+sqrt(5))/2.
After rotating side0 to direction1, the five directions are

    1,z^4,z^6,z^7,z^8.

Exact vector closure, solved in its two real components, gives

    A=phi*b+phi*c+d,  B=b+phi*c+phi*d.                    (1)

For example these are verified by substituting in
A+B*z^4+b*z^6+c*z^7+d*z^8=0, and the two A,B directions are independent.
Thus both acute-incident long sides strictly exceed every one of that
polygon's other three sides. Also

    phi*A-B=phi*b+c>0, phi*B-A=c+phi*d>0,
    A<phi*B, B<phi*A.                                   (2)

A reflection only reverses the relevant corner/side labeling; these formulas
and symmetric ratio bounds cover every reference shape.

## A nonnegative native-corner measure

Give native36,108,144 corners weights2,1,-2 respectively. The sum on any
one U-word pentagon is2+2-4=0. For a hypothetical tiling define the locally
finite signed measure

    mu=sum over all native tile corners v of w(angle(v))*delta_v,

adding contributions when vertices coincide. Local finiteness follows from
fixed positive minimum area, bounded diameter, and a finite reference set.

At a point carrying a genuine native corner, there is at most one straight
sector from a tile-side interior. Its native-angle weights, in pi/5 units,
therefore sum to10 for a full star or5 for a star with one straight sector.
No edge-to-edge assumption is made. Write n1,n3,n4 for its native36,108,144
multiplicities. The combined atom weight is

    h=2n1+n3-2n4.

For full stars n1+3n3+4n4=10 and h=5(4-n3-2n4)>=0.
For half stars n1+3n3+4n4=5 and h=5(2-n3-2n4)>=0.
The inequalities follow directly from n_i>=0 and the two budgets: in a full
star n4=0,1,2 forces n3<=3,2,0 respectively; in a half star n4=0,1 forces
n3<=1,0. Hence mu is actually a nonnegative atomic measure. Its zero stars
are exactly

    full:(108,108,144), full:(36,36,144,144),
    half:(36,144) plus one straight180 sector.             (3)

Every nonzero atom has weight at least5. Positive weights bound all native
star valences by10, so no infinite-corner star has been omitted.

## A zero-measure admitted limit, including merging partial vertices

For every translated square W_R of side2R,

    mu(W_R)=O(R),                                        (4)

uniformly in translation. To prove it, compare the native-corner sum in
W_R with the sum from every tile whose centroid is in W_R. The latter is
zero because every tile has total weight0. Only tiles in a fixed-width
boundary strip can change the count, and there are O(R) such tiles by
bounded diameter and disjoint interiors of a fixed positive minimum area.
Each supplies a bounded number and size of weights. Thus even the absolute
signed difference is O(R); nonnegativity of mu then proves(4).

Let bad points be positions of positive mu atoms. Since each has weight>=5,
their count is uniformly O(R). For each fixed H>0 some radius-H disk misses
all bad points. Otherwise their radius-H disks would cover a large square;
only O(R+H) relevant bad points lie in its H-enlargement, and their disks
have total area O((R+H)H^2), below4R^2 for large R. Translate a sequence of
bad-free disks with radii tending to infinity to the origin.

Extract a diagonal local placement limit. Fixed positive-area reference
shapes bound the number of centroids in each bounded enlargement; centroid
positions and orientation matrices in compact O(2) have convergent
subsequences. Every point remains in a covering tile of centroid distance
at most the fixed diameter bound, whose closed limiting polygon contains
it. Any open interior overlap, including collapse of two copies to the
same positive-area polygon, would persist in approximating placements.
The limit is therefore an admitted locally finite plane tiling by F.

Crucially no uniform separation of partial vertices is assumed. The native
corner measure is continuous under this placement limit in the following
explicit sense. For any compactly supported continuous test function f,
all contributing corners belong to uniformly finitely many tiles with
centroids in a fixed enlargement. Extract those finite placements, and
choose an exhaustion boundary avoiding the limit centroids. Their native
corner coordinates converge and their reference weights remain fixed,
so the finite signed sums of w*f(v) converge. This is vague convergence of
the native corner measures to the native corner measure of the limit.
Every such sum is zero in the approximating tilings once the growing
bad-free disk contains the support of f. Thus the limit measure is zero.
Coincident vertices, including merging T-junctions, add their weights;
the zero conclusion survives without combinatorial persistence of a
particular earlier star.

Apply the original full/half native-star classification to this admitted
limit tiling. Every star has zero weight, and hence is one of(3). In
particular a native108 corner in another side's relative interior is
impossible: its straight sector leaves72 degrees, necessarily supplied by
two36 corners, giving the positive-weight half star(108,36,36).

## Maximum-long-side contradiction in the zero-star tiling

Let M be the largest value of A or B over the finite reference collection.
The maximum is attained, and a copy of a type attaining it occurs if we
restrict the collection to the nonempty subset actually used in the limit.
By(1), EVERY short b,c,d side of a used reference shape has length strictly
less than M. Choose a tile T with an acute-incident long side of length M,
and call its acute endpoint x and its other108-degree endpoint x+M*e,
where e is a unit vector along that side.

Every zero star containing36 has a native144 neighbor along at least one
acute ray: this follows from the full(36,36,144,144) cyclic orders and the
half(36,144) star. If the reference shape has A=B=M, either ray has the
maximum length, so choose the ray with that neighbor. For an asymmetric
shape, a maximum-length ray may instead meet the other36 sector of a full
star; the following contradiction is conditional on the maximum ray itself
meeting144. No replacement of that ray by a shorter acute side is valid.

Let R be that144 neighbor. The shared R edge has length b,c,or d, all<M.
If it is b or d, its other endpoint has native108 and lies strictly inside
T's long side, forbidden. Hence it is c, whose other endpoint y=x+c*e
has native144. T has a straight side sector at y, so(3) forces a second
native36 tile S in the opposite half-plane. Its two acute rays are exactly
the continuation of T's long side forward from y and R's other incident
b or d side. Call their long lengths L and K respectively, and call that
other R side length r=b or d.

On the second ray, if K differs from r, the shorter side's native108
endpoint lies strictly inside the longer side. Thus K=r. On the forward
ray the same endpoint argument gives L=M-c. The ratio bounds(2) for S
therefore imply

    M=c+L<c+phi*K=c+phi*r.                               (5)

If r=b, R has long A=phi*b+phi*c+d>phi*b+c; if r=d, R has long
B=b+phi*c+phi*d>phi*d+c. Either exceeds M by(5), contradicting maximality.

## Edge-to-edge corollary for all finite U collections

If the original tiling is edge-to-edge, the zero-measure placement limit
can be chosen edge-to-edge as well. Every native side of each limiting tile
had an entire matching native side in each approximant. Its neighboring
centroid remains in a fixed bounded enlargement; the finite possible types,
side indices and reflection choices have a constant subsequence, and the
full endpoint equality passes to the limit. Hence every limiting native
side still has a full native-side neighbor. No interior contact can appear
in addition, since it would overlap those two limiting tiles' interiors.

Now choose a used tile with a globally largest long side M, and let L be
its other long side. At least one acute ray has a144 neighbor in a zero
star. Call that ray's length x, so x is M or L. In the edge-to-edge limit,
the144 neighbor has a short native side b,c,or d of length exactly x.
Closure(1) shows that at least one of its long sides is strictly greater
than phi*x: use A for b, either A or B for c, and B for d.
If x=M this contradicts the global maximum. If x=L, equation(2) gives
M<phi*L, again a contradiction. Thus EVERY finite collection of U-word
pentagons, with arbitrary asymmetric metrics, fails edge-to-edge tilability.
This corollary does not exclude partial-contact tilings.

## Mirror corollary and current asymmetric gap

If every reference shape has A=B, a used type attaining M has both acute
sides of length M. At least one has a144 neighbor, so the preceding
contradiction applies. This proves untileability of ANY finite collection
of mirror U(b,c) polygons with arbitrary positive metrics and relative
scales. It includes the proposed swapped pair U(b,c),U(c,b); the additional
all-short-below-all-long hypothesis of its initial local proof is unnecessary.

For asymmetric U metrics, the zero-measure reduction and the conditional
maximal-ray exclusion remain valid, but a maximum ray can instead have
an acute36 neighbor in a full1144 star, or border the straight180 sector
in a half14 star while its shorter acute ray borders144. A general
no-tiling theorem needs a new invariant or argument handling both these
maximum-ray configurations. The ratio bound alone does not resolve them. This exact asymmetric gap is not promoted to a theorem;
no larger finite patch search is justified merely by restating it.

The native-measure compactness argument avoids assuming vertex separation
in an acute/partial-contact tiling and may be reused by other avenues within its reviewed hypotheses. No external monohedral classification is used.
