# Reordered acute pentagons: exact tileability criterion and four-tile periodic escape

Status: [fresh independent review VALID after the five-host repair](../reviews/reordered-acute-pentagon-four-face-carrier-independent-review.md).

Let A,B be actual strictly convex pentagons with native cyclic words

    A=(65,140.5,75,147.5,112),
    B=(40,144.5,136,47,172.5),

in degrees. Native side i joins corners i and i+1 modulo5. Admit all
rotations, reflections, vertex valences and partial contacts. Then:

**Theorem.** The fixed pair tiles the plane if and only if its actual lengths
satisfy

    A0=B1, A2=B0, A3=B3.

Whenever these three equalities hold, it has a periodic plane tiling with
a fundamental domain containing two A and two B tiles. In every admitted
tiling of these native words, corner-on-side T contacts are impossible.
The theorem therefore excludes these words as an aperiodic pair mechanism.
It does not assert that every admitted whole-side tiling is periodic.

No metric search, invariant measure, substitution or hexagon limit is used.

## Exact native support and continuation rules

Write alpha=A65, z=A140.5, beta=A75, x=A147.5, y=A112,
gamma=B40, delta=B144.5, u=B136, v=B47, w=B172.5. The sole native180
multiset is T=(alpha,beta,gamma). All other native angles are non-flat-eligible.
The complete native360 census is

    (alpha,x,x), D=(z,beta,delta), Q=(z,v,w), P=(x,gamma,w),
    (y,y,u), F=(alpha,y,u,v), (alpha,alpha,u,v,v),
    (alpha,alpha,beta,beta,gamma,gamma), nine gamma.

The [independent checker](../reviews/verify_reordered_acute_pentagon_four_face_carrier.py)
enumerates both supports exactly in doubled integer degrees.

Along a seam ray, two non-flat-eligible far endpoints force equal side
lengths: otherwise the shorter side's native endpoint lies strictly inside
the other side. Their coincident far vertex must have an allowed full native
star: an additional flat sector would make each far corner flat-eligible,
contradicting the premise. All internal forbidden-seam pairs below also
have combined angle greater than180, which independently excludes a flat
sector. Once T is excluded, every seam is whole and every far pair must
have full native support, regardless of endpoint eligibility.

Two useful forbidden pairs of far endpoints are

    y+delta=256.5 (remaining103.5), y+w=284.5 (remaining75.5).

They have no completion. Thus an x/gamma seam cannot use native A3:
its far y would meet delta or w, both non-flat-eligible. Likewise every
alpha/beta seam is impossible: their far pairs are z/z,z/x,y/z,y/x,
all non-flat-eligible with respective unfillable remainders79,72,107.5,100.5.

## No flat T fan can extend to a tiling

At T, alpha and beta cannot be adjacent, so gamma must be the middle
native sector of the half-plane opposite its flat host.

If beta uses A2 toward gamma, the only supported far pair is x/w,
using B4. These far endpoints are non-flat-eligible, so the internal ray
must whole-match A2/B4. At its far P vertex, x already faces w using A2;
its other A3 must face the third gamma tile. The y/delta or y/w far pair
is forbidden by the preceding continuation rule. Thus this branch cannot
occur. Beta must use A1 internally and has outer side A2 with far x.

Alpha uses A0 internally: using A4 would give the forbidden far y/delta
or y/w pair. It therefore has outer side A4 with far y. The two outer
native endpoints of the T fan are consequently y and x.

Checking support at the non-flat-eligible host endpoints leaves only
native host types A2,A3,A4,B3,B4. Eligible host endpoints may lie inside
an outer side, so full-endpoint coincidence alone would miss A2 and B4.
The certificate retains both the full-coincidence table and this complete
five-case necessary table. Other host types cannot complete at least one
non-flat endpoint. The five cases are excluded as follows:

* On A2, its non-flat x endpoint must coincide with the fan's far x,
  on an outer A2 side of exactly the host length. This places T at the
  other host endpoint, contradicting an interior junction.
* On A4, its non-flat y endpoint must coincide with the fan's far y
  endpoint, on an outer A4 side of exactly the host length. This places
  the T at the other host endpoint, contradicting an interior junction.
* On A3, both host endpoints x,y and outer endpoints x,y are non-flat.
  Thus the two outer sides end exactly at the host endpoints and
  `A3=A2+A4`. At the x endpoint the full star is(alpha,x,x). The fan's
  x copy used A2 toward the host and retains A3 toward the third alpha.
  That seam either uses alpha's A0 and has forbidden far y/z, or its
  A4 and requires A3=A4 with far y/y. The latter contradicts A3=A2+A4.
* On B3 or B4, the host w endpoint meets the fan's far x, forcing P=(x,gamma,w).
  Here x already uses A2 toward w, so its other A3 faces the third gamma.
  The forbidden far y/delta or y/w pair again prevents completion.

All cases fail. Hence **T is pointwise impossible**, not merely of zero
density. A corner-on-side incidence would require T, so every admitted
tiling is edge-to-edge. Local finiteness follows from fixed positive area
and bounded tile diameter; there is no accumulation loophole.

## Full native star forcing yields the three metric equalities

In a T-free tiling, (alpha,x,x) is also impossible. Alpha's A0 can meet
an x corner only through that x's A2 (far z/beta gives D); its A4 can
meet the other x only through A3 (far y/y gives y,y,u). The other choices
have unsupported far y/z or y/beta. The two x tiles' remaining mutual
seam therefore uses A3/A2, whose far endpoints y/beta have no full support.

Every native x corner must consequently have P=(x,gamma,w), and every
native delta corner must have D=(z,beta,delta). Either species forces the
other locally. Every nonempty plane tiling therefore has both stars.

At P, the x/gamma seam uses only A2/B0: its far beta/delta pair has D,
while beta/w, y/delta and y/w have no full support. The x/w seam then
uses only A3/B3, with far y/v completed by F; y/gamma is unsupported.
These whole seams force A2=B0 and A3=B3.

At D, the beta/delta seam again uses only A2/B0. The beta/z seam uses
only A1/A1, since its alternative far z/alpha is unsupported. The remaining
z/delta seam is A0/B1, forcing A0=B1. Its far alpha/u has full support.
All statements include both native orientations and reflections.

## A four-face orientable flat torus realizes every surviving actual metric

Take counterclockwise native copies A+,A−,B+,B−. Identify the following
ten edge pairs by reversing boundary endpoints:

| First edge | Second edge |
|---|---|
| A+1 | A−1 |
| A+4 | A−4 |
| B+2 | B−2 |
| B+4 | B−4 |
| A+0 | B+1 |
| A−0 | B−1 |
| A+2 | B−0 |
| A−2 | B+0 |
| A+3 | B+3 |
| A−3 | B−3 |

Private equal-index pairs always have equal lengths. The three actual
metric equalities make all six cross pairs isometric as well. The finite
checker verifies every halfedge used once, a connected quotient, single
cyclic vertex links, and orientability from reverse boundary gluing.
There are four faces, ten edges and six vertices, giving Euler0. Vertex
links are exactly two copies each of D,P,F, all of angular sum360.
Thus this is an orientable compact connected Euclidean flat torus built
from the actual polygons, not only an angular diagram.

For completeness, its universal cover develops isometrically to the plane.
Local Euclidean charts extend on the simply connected cover; completeness
of the compact surface makes the developing local isometry a covering of
the complete Euclidean plane, hence an isometry. Its deck transformations
preserve orientation and act freely. A nontranslation orientation-preserving
Euclidean isometry is a rotation with a fixed point, so every nonidentity
deck transformation is a translation. Compactness gives a rank-two lattice.
The lifted actual polygon faces are disjoint and cover the plane, and deck
translations preserve their labels and native placements. This is the
claimed periodic mixed tiling with2A+2B per domain.

The positive carrier proves sufficiency for every actual metric satisfying
the aliases; the native forcing proves necessity. No additional geometric
realization step is hidden: actual strictly convex polygons are the input,
and the complete flat torus gives their plane realization.

## Artifacts and limits

* [Exact checker](../reviews/verify_reordered_acute_pentagon_four_face_carrier.py).
* [Complete support, edge pairs and vertex links](../certificates/reordered-acute-pentagon-four-face-carrier.json).

Replay:

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python3 research/reviews/verify_reordered_acute_pentagon_four_face_carrier.py --output /tmp/reordered-acute-carrier-replay.json

The theorem concerns these exact native cyclic words. A different cyclic
order or angle inventory needs a new adjacency audit. It establishes a
complete periodic escape for this family, not the impossibility of all
unmarked convex polygon pairs.
