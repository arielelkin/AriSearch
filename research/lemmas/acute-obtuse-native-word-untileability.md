# The acute/obtuse native pentagon words are untileable at every metric

Status: [fresh hostile review VALID](../reviews/acute-obtuse-native-word-untileability-review.md);
[separate independent audit VALID](../reviews/acute-obtuse-native-word-untileability-fresh-independent-review.md).

Let A,B be any actual strictly convex pentagons with respective native words

    A=(65,140.5,147.5,75,112),
    B=(40,144.5,136,47,172.5),

in degrees. There is **no plane tiling** by this pair, with arbitrary
reflections, rotations, partial contacts and vertex valences. No equality
or inequality among native side lengths is assumed.

The proof combines native angular adjacency with corner capacities.
The earlier exact four-tile cap is a valid local patch, but cannot extend
to a plane at any metric of these words. Changing its flat-fan middle
corner or internal matched lengths cannot repair this family.

## Exact native support and one geometrically forbidden star

Write alpha=A65, z=A140.5, x=A147.5, beta=A75, y=A112,
gamma=B40, delta=B144.5, u=B136, v=B47, w=B172.5.
The complete native180 census is only

    T=(alpha,beta,gamma).

Therefore all other native corners are non-flat-eligible. The complete
native360 census is

    (alpha,x,x), (z,beta,delta), (z,v,w), (x,gamma,w),
    (y,y,u), (alpha,y,u,v), (alpha,alpha,u,v,v),
    (alpha,alpha,beta,beta,gamma,gamma), nine gamma.

These lists are exact doubled-integer-degree enumerations of all native
valences up to9, retained in the [feature certificate](../certificates/acute-obtuse-long-edge-feature.json).

The full star(alpha,x,x) is geometrically impossible, independent of all
lengths. At x the two incident native sides are A1 to z and A2 to beta;
at alpha they are A0 to z and A4 to y. A seam from x to alpha using
the x-side A1 has far endpoints z/z or z/y. Both are non-flat-eligible,
so unequal lengths would put a far endpoint inside the other side and
are impossible. Equal lengths would require a full far-star completion,
but z/z leaves79 and z/y leaves107.5, both absent from the native sum
census. Thus both x copies must use A2 toward alpha. Their mutual seam
then uses A1 on both sides and has far z/z, again impossible.

The underlying continuation fact is simple: along a positive seam ray,
two non-flat-eligible far endpoints force equal lengths and coincident
far endpoints; the latter must admit a full native star. In every use
below their combined angle exceeds180, so an additional flat incidence
at that far vertex is also impossible.

## Flat T and unused w resources have only boundary-size counts

Each A native x is non-flat and, after the exclusion above, belongs to
the unique full type P=(x,gamma,w). Every B native delta is non-flat
and belongs to D=(z,beta,delta). These stars each contain just one of
the distinguished resource corners. Every T additionally consumes beta
and gamma at a distinct flat vertex.

Count tile anchors and starred vertices in a radiusR disk. All associations
move bounded distance. Fixed positive inscribed radii and bounded tile
diameters imply O(R) anchors and vertices in fixed-width annuli, so

    b_R >= a_R+T_R-O(R),
    a_R >= b_R+T_R-O(R).

Consequently T_R=O(R) and |a_R-b_R|=O(R). Furthermore w can occur only
in P or Q=(z,v,w). Since P_R=a_R+O(R) and b_R=P_R+Q_R+O(R),

    Q_R=O(R).

This counts sparse defects directly; no invariant measure, finite local
complexity or pentagon defect-free-limit theorem is assumed.

## All possible whole A1 partners

An A1 endpoint is z or x. Both are non-flat-eligible, and each has angle
greater than140 while every native angle is at least40. Thus a full
seam endpoint with any partner cannot include a flat sector; its two
native angles already exceed180. Checking the full-star list at both
endpoints leaves only these possible native partner types:

| Whole A1 partner | Required endpoint order | z endpoint star |
|---|---|---|
| A2 | z-to-beta, x-to-x | D=(z,beta,delta) |
| B0 | z-to-delta, x-to-gamma | D=(z,beta,delta) |
| B3 | z-to-v, x-to-w | Q=(z,v,w) |
| B4 | z-to-w, x-to-gamma | Q=(z,v,w) |

All other native partner types and reversed endpoint orders fail at least
one endpoint census. Coincident lengths do not change this angular table.

The A2 option already contains the forbidden(alpha,x,x) star at its x
endpoint, so it never occurs. The B3/B4 options consume a distinct Q
through the unique native z of the A tile. There are only O(R) of these.

## A whole A1/B0 match forces a nearby T

At its z-to-delta endpoint, a third tile has beta. The A1 side already
faces B0, so the other A0 side of z faces either A2 or A3 of that beta
copy.

If it faces A3, the third seam from this vertex is A2 against B1. Their
far endpoints are x and u, both non-flat-eligible. The continuation fact
forces equal lengths and a full far endpoint. But x+u=283.5 leaves76.5,
below two minimum40 corners and equal to no native angle. This branch
is impossible at every metric.

Thus A0 faces A2, with far endpoints alpha and x. If A0>A2, the far x
lies inside A0, impossible. If A0=A2, the full far vertex containing
alpha+x has only the forbidden(alpha,x,x) completion. Hence

    A0<A2.

Its native alpha endpoint lies strictly inside that beta copy's A2 side,
so it is a T vertex. This associates each whole A1/B0 match to a distinct
T through the unique alpha corner of its A tile. Therefore these matches
also number O(R). Unlike the earlier normalized-family argument, this
does not claim that an individual A1/B0 patch is impossible for every
metric: it can force a sparse T, and the counting closes the plane proof.

## Count A1 side types and contradict area coverage

Every A1 either has a whole native partner or has an interior contact
junction. A single longer side cannot cover it: either source endpoint
would then lie in that side interior, contrary to its non-flat eligibility. In the latter case its flat host sector forces a T. Selecting
one interior T for each partial A1 is injective: a native vertex cannot
have two flat host sectors together with positive native angles.

Thus partial A1 sides are bounded by T_R up to boundary errors, whole
A1/B0 sides are bounded by another T_R, whole A1/B3 or B4 sides by Q_R,
and whole A1/A2 sides are impossible. Since there is one A1 per A,

    a_R <= 2*T_R+Q_R+O(R)=O(R).

Then b_R=a_R+O(R)=O(R). But a plane covering by fixed bounded-area
tiles requires a_R+b_R=Omega(R²), contradiction.

This proves untileability for every actual side metric and rules out
isolated-defect or zero-species-density loopholes. It is a theorem about
these native cyclic words; rearranging their corner adjacency or changing
their angles changes a premise and needs a new early continuation audit.
