# Interface-first three-arm pentagon pair

**Later status (2026-10-15):** [unrestricted untileability](../lemmas/pentagon-y-unrestricted-2026-10-15.md)
now closes the former partial-contact gap for the fixed pair. This record
retains its original scoped proof; historical existence questions below are superseded.

Date: 2026-10-14. New fixed Y topology; no larger search of an old family.
The bounded experiment certifies a mixed three-child parent, rules out both
monohedral omissions, and rules out plane assemblies of intact copies of that
parent. Infinite existence and universal recognition remain UNPROVED.

## Boundary specification before coordinates

Take a reflection-symmetric hexagonal parent with bottom and top horizontal
sides, unequal lengths, and four oblique sides. Three internal seams form a Y
from one central point to a point inside the bottom side and corresponding
points inside the two upper oblique sides. Each resulting region has five
genuine corners. Reflection identifies the two bottom-side regions P; the
top region is Q. This changes the old two-child topology and the far-corner
correlations. No central symmetry or translation-tile parent is imposed.
The three boundary seam endpoints must be flat: P90+P90 and P b+Q c.
The internal junction is 2P a+Q d. These equations must hold at the actual
far endpoints, with the incident side lengths matching, not merely as sums.

## Exact geometry

Let theta=atan(2), with 0<theta<pi/2. Counterclockwise polygons are

    P=((0,0),(2,0),(3,2),(2,3),(0,2))
    Q=((2,3),(1,4),(-1,4),(-2,3),(0,2))
    H=((-2,0),(2,0),(3,2),(1,4),(-1,4),(-3,2)).

P, its reflection in x=0, and Q partition H. The seams are (0,0)-(0,2),
(0,2)-(2,3), and (0,2)-(-2,3). Their lengths are 2,sqrt(5),sqrt(5).
The areas are 13/2,13/2,5, summing to 18. All turns are strictly positive;
all polygons are convex and simple, with interiors of the three children
disjoint. The seams cancel exactly, including all three external endpoints.

Use corner labels

| Label | Species | Angle | Incident lengths | Far corners on those arms |
|---|---|---|---|---|
| r | P | 90 | 2,2 | a,a |
| a | P | 180-theta | 2,sqrt(5) | r,b |
| b | P | 45+theta | sqrt(5),sqrt(2) | a,b |
| c | Q | 135-theta | sqrt(2),sqrt(5) | g,d |
| g | Q | 135 | sqrt(2),2 | c,g |
| d | Q | 2theta | sqrt(5),sqrt(5) | c,c |

P has labels r,a,b,b,a; Q has c,g,g,c,d. P has one right corner; Q has
none, so the shapes are noncongruent. The seam endpoints are r+r=180 and
b+c=180; the Y center has a+a+d=360. These are exact native occurrences.

## Both omission proofs with arbitrary partial contacts

Theta/pi is irrational. Otherwise exp(2i theta) would be a root of unity,
and 2cos(2theta)=-6/5 would be a rational algebraic integer, impossible.
Thus angular sums can be compared independently in the basis (pi/4,theta).
At a vertex, sectors consist of genuine native corners and possibly a single
flat 180 sector. Two flats leave no room for a genuine corner.

In a P-only tiling, theta coefficients force equal numbers n of a and b
sectors. The remaining coefficient equation is 5n+2r=8 (no flat) or 4
(one flat). These require n=0. No a or b corner can occur, contrary to every
P carrying such corners. P cannot tile alone. In a Q-only tiling, theta
coefficients force c=2d, and the remaining equation is 3(c+g)=8 or 4.
Neither is possible. Q cannot tile alone. These arguments allow reflections,
higher valence, and arbitrary T contacts.

## Bounded interface and endpoint experiment

The producer exhausts native sector multisets of valence at most five and
flat-sector multisets of valence at most three. Every native angle is greater
than 60 degrees, so these bounds are complete. Full native stars are

    rgg, aad, abg, rrrr, rrbc, rccd, bbcc.

The only flat stars are 180+rr and 180+bc. For each full native star,
enumerate cyclic orders and both arm orientations, equate every adjacent
whole-side length, then check an exact angle completion at each far endpoint.
The certificate counts indexed type/arm records, not geometric congruence
classes. Outcomes (length-compatible / far-end-compatible records) are

    rgg 6/6; aad 6/6; abg 6/6; rrrr 16/16;
    rrbc 0/0; rccd 0/0; bbcc 12/8.

For abg the rays have lengths sqrt(5),sqrt(2),2. Far pairs are b+a, b+c,
g+r and admit respectively g, a flat sector (or rr or bc), and g.
For rgg, the two length-2 rays have far a+g, completed by b. The
sqrt(2) ray has c+c, completed by bb OR r+d. The latter alternative is
important: a far-end completion need not be a single third tile.
For bbcc four records fail because a sqrt(5) c-c edge would have d+d
at its far end, with no angular completion. Other bbcc orders survive.
These are necessary endpoint tests; they do not certify extensions at all
new corners. Partial contacts are outside the equal-length filtering.

Thus the Y star is not forced by the local angle/length/endpoint conditions.
An angle-only argument for a unique Y grouping is invalid. This does not
prove that a surviving alternative star extends to a plane tiling, and does
not independently disprove universal recognition in actual plane tilings.

## Intact-parent assembly fails exactly

H has angles a,a,b,g,g,b, all strictly greater than 90 degrees. Any plane
tiling by H must therefore be edge-to-edge and trivalent: a flat incidence
plus a corner cannot be completed, and four native corners exceed 360.
The sole possible native star is abg, since theta coefficients force equal
a and b counts, and their pi/4 coefficients plus g give 5n+3g=8.
At H's a,b,g corners the incident arm lengths are respectively
(4,sqrt(5)), (sqrt(5),sqrt(8)), (sqrt(8),2). At a trivalent star each
length must occur twice among the six arms. The lengths 4 and 2 each occur
once. Therefore no actual H star exists. This excludes intact H parent
tilings with arbitrary original contacts, not only translations or a fixed
orientation. No monohexagon classification is imported.

## Stopping condition and changed assumption

The explicit scheme was an intact-H plane partition with intrinsic Y grouping.
The experiment stops at the exact unmatched 4-versus-2 parent arms, not at a
solver cap or larger patch request. No intact-H infinite covering is possible,
and the local recognition gate admits different stars. The atomic pair itself
is NOT excluded: mixed assembly crossing the proposed H boundaries remains
open, and both omission gates are passed.

To restart, replace the single intact parent interface: use a second parent
type, cross-parent seam exchanges, or a nonpolygonal/infinite boundary rule.
Keeping these exact intact H parents while increasing their assembly count
cannot fix the obstruction. A changed scheme must first give a repeatable
cross-boundary extension rule and then separately prove every-tiling decoding.
No patch-size increase is prescribed or performed.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/pentagon-y-interface-2026-10-14.py

Producer: pentagon-y-interface-2026-10-14.py. Frozen certificate:
../certificates/pentagon-y-interface-2026-10-14.json. [Fresh independent hostile review](../reviews/pentagon-y-interface-2026-10-14-hostile-review.md)
validates these scoped claims; its separate verifier reconstructs rational
convex clipping, geometry, and the complete native/endpoint table.

## Later alternative-assembly attacks

The subsequent [fixed 6P+4Q CP-SAT model](pentagon-y-6p4q-flat-torus-cpsat-2026-10-14.md) returned INFEASIBLE. The independently checked [whole-edge native propagation theorem](../lemmas/pentagon-y-whole-edge-native-propagation-2026-10-14.md) now excludes every whole-edge plane tiling of these atoms, beyond any finite quotient bound. Mixed existence with partial-edge contacts remains unresolved. No larger whole-edge search is justified.
