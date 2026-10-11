# No all-obtuse pentagon partners a regular polygon with at least thirteen sides

**Status:** adversarially reviewed; the [fresh hostile review](../reviews/all-obtuse-pentagon-regular-large-polygon-review.md) is VALID without repair for every integer n>=13. No finite patch search, metric classifier, or novelty claim is used.
This is a restricted impossibility theorem, not the unrestricted main result.

## Theorem and dependencies

For every integer n>=13, let Q be the regular unit-side n-gon. For every
genuine convex pentagon P whose five angles are strictly between pi/2 and pi,
{P,Q} has no plane tiling under the original unrestricted definition.
All rotations, reflections, arbitrary positive P side lengths, partial
original contacts, and omission of either type are covered.

Use the independently reviewed [all-obtuse forcing theorem](obtuse-edge-forcing.md):
any hypothetical tiling would be full native-edge and trivalent. For the
n=14 case, use the reviewed translated defect-free limit procedure detailed
in [the regular-heptagon classification](all-obtuse-pentagon-regular-heptagon-classification.md).
Its hypotheses are fixed compact positive-area shapes, uniform O(R) bad-tile
counts, and whole-side/native-star persistence. The new application is
spelled out below; no assumption of pointwise saturation in the original
tiling is made.

## Uniform windows and the unique large native corner

Let N_P,N_Q count tile centroids in an arbitrary translated square of side2R.
Fixed positive minimum area and bounded diameter imply only O(R) boundary
tiles and N_P+N_Q=Theta(R^2), uniformly in translation. Switching counts
between centroids, sides, and vertices therefore changes each equation by
O(R). Angle and native-corner totals in a trivalent tiling give

    N_P=(n-6)N_Q+O(R).                                    (1)

In particular N_Q=Theta(R^2), so neither type can be omitted or occur only
with subquadratic count. Q has angle eta=(n-2)pi/n. A vertex with two Q
corners would require a P angle4pi/n<=pi/2, impossible; three Q corners
are impossible too. Thus every Q side meets P, every Q corner belongs to
Q,P,P, and P has at most two nonadjacent Q side neighbors.

At a Q,P,P star its two P angles sum to

    S=2pi-eta=pi+2pi/n.

Each is strictly below

    H=S-pi/2=pi/2+2pi/n < 2pi/3,                          (2)

because the other is strictly obtuse. There must be some P copy with two
Q side neighbors: otherwise counting P--Q sides gives
nN_Q<=N_P+O(R)=(n-6)N_Q+O(R), contradicting N_Q=Theta(R^2).
Its two Q sides are nonadjacent and touch four distinct native corners of P.
Consequently four of P's native angles are strictly below H.

Let Z count P,P,P stars. Every Q,P,P star accounts for one Q corner,
so native P counts give

    5N_P=2nN_Q+3Z+O(R),
    Z=(n-10)N_Q+O(R).                                    (3)

There are quadratically many P,P,P stars. Each needs an angle at least
2pi/3, since three angles strictly below that value cannot sum to2pi.
By the preceding four-small-corner result P therefore has exactly one
native corner beta>=2pi/3, and its other four native corners are <H.
Every beta incidence is P,P,P because beta>H.

If beta=2pi/3, every P,P,P star must consist of three beta sectors: a small
sector would make its total <2pi. Then N_P=3Z+O(R), and(1),(3) imply
(n-6)=3(n-10), hence n=12, contrary to n>=13. Thus

    beta>2pi/3.                                         (4)

A P,P,P star has one or two beta corners: at least one because all other
angles are below2pi/3, and at most two because3beta>2pi. Write X,Y for the
counts with two and one beta corners, respectively. Counting beta sectors
and stars gives

    2X+Y=N_P+O(R), X+Y=Z,
    X=4N_Q+O(R), Y=(n-14)N_Q+O(R).                       (5)

These are counts of actual stars, not assumed frequencies or signed defects.

## Excluding n=13 and all n>=16

For n=13, Y=-N_Q+O(R) contradicts Y>=0 and N_Q=Theta(R^2).
There are quadratically many two-beta stars for every hypothetical case,
by X=4N_Q+O(R). Their third angle is strictly greater than pi/2, so

    beta<3pi/4.                                         (6)

For n>=16, Y is quadratically positive and some one-beta star occurs.
Its two small angles are both <H, so its angle sum requires

    beta>2pi-2H=pi-4pi/n >=3pi/4.

This contradicts(6). No parameter, cyclic-order, or length exception remains.

## Excluding n=15 by integer angle multiplicities

Here H=19pi/30 and S=17pi/15. Since one-beta stars occur, the preceding
strict inequality gives

    11pi/15 < beta <3pi/4.

Every two-beta star has a third angle

    alpha=2pi-2beta, pi/2<alpha<8pi/15.                   (7)

Thus alpha is a native P angle. It cannot occur in a one-beta star:
alpha+any other small angle is <8pi/15+19pi/30=7pi/6,
whereas such a star needs its two small angles to sum2pi-beta>5pi/4.
Consequently P,P,P incidences of alpha are exactly X=4N_Q+O(R).

Set alpha'=S-alpha. These are distinct values because
alpha<8pi/15<S/2=17pi/30. Let m,m' be the integer numbers of native P
corners of values alpha,alpha'; m' may be zero. Let B' count alpha'
incidences in P,P,P stars. Alpha' cannot occur at a two-beta star, whose
small angle is alpha. It is not beta, because alpha'<H<beta. Thus all its
P,P,P incidences occur in one-beta stars, and

    0<=B'<=2Y=2N_Q+O(R).                                 (8)

Every Q,P,P star containing alpha contains exactly one alpha' as its other
P angle, and conversely, since those P angles sumS. Equating these two
incidence counts, and subtracting their P,P,P incidences, gives

    m*N_P-X=m'*N_P-B'+O(R),
    B'=(m'-m)N_P+X+O(R)
      =(9(m'-m)+4)N_Q+O(R).                             (9)

No integer k makes9k+4 lie in[0,2]: k>=0 gives>=4, and k<=-1 gives<=-5.
Equations(8),(9) contradict N_Q=Theta(R^2). This excludes every native
angle multiplicity and every metric for n=15.

## The saturated n=14 case and its defect-free limit

Equation(5) now gives Y=O(R), uniformly in translated windows. Mark a P
tile bad if it is incident to a one-beta P,P,P star. A star has three P
incidences, so bad-centroid counts are O(R). A disk of every fixed radius
can be translated to avoid bad centroids: otherwise O(R) disks of that
radius would cover a square of areaTheta(R^2). Choose bad-free radii tending
to infinity and apply the cited reviewed local compactness procedure.
Fixed positive areas bound tile counts in every bounded region; centroid
positions and O(2) orientations have compact subsequences. The limit covers
the plane with disjoint interiors. Whole-side contacts and native stars
persist because native edge lengths are fixed positive and distinct stars
have uniform separation, as proved in the cited lemma. Every bounded
neighborhood lies inside the growing bad-free disks for large enough radii.
The resulting admitted tiling has only two-beta P,P,P stars.

This tiling may differ from the original one. In it, every P,P,P star is

    beta,beta,alpha,  alpha=2pi-2beta,

and each P has exactly one native beta corner. Each beta corner meets one
beta and one alpha neighbor, so it has a beta--beta P contact along one of
its two incident sides.

The other endpoint of any such beta--beta side cannot be P,P,P. If it were,
either incident P would contribute a small native angle there, and a
beta,beta,alpha star would require the neighbor across that side to supply
beta at both endpoints. That neighbor has only one native beta corner.
More explicitly, both contacting tiles have already used their beta corner
at the first endpoint; at the second they both contribute small angles,
whereas a two-beta P,P,P star needs two beta sectors. The second endpoint
is therefore Q,P,P. The remaining side of either P at that endpoint meets Q.
Consequently every P has at least one Q side.

Suppose a P has exactly one Q side. Its two endpoints are its only Q,P,P
corners. Its other three vertices are P,P,P, forming a consecutive
three-vertex chain on the pentagon. They are its unique beta and two alpha
corners. If beta is at either end of that chain, the two alpha corners
are adjacent. Their common P--P side would need a neighbor contributing
beta at both endpoints to form the required stars, impossible for a tile
with one beta corner. If beta is in the middle, both beta-incident sides
end at P,P,P alpha corners. Its required beta--beta contact would then
have a P,P,P second endpoint, excluded above. These cases exhaust the
positions of beta in the chain, so no P has exactly one Q side.

Every P therefore has two Q side neighbors, since it has at most two.
Double counting gives14N_Q=2N_P+O(R), but(1) givesN_P=8N_Q+O(R).
This would force2N_Q=O(R), contradicting the positive quadratic count.
Thus the admitted defect-free limit cannot exist; neither can the original
tilings from which its existence was deduced. This excludes n=14.

## Consequences and precise limits

Every n>=13 has now been excluded. Combined with the separate n=8..11 gate,
regular-heptagon classification, and regular-dodecagon classification, this
narrows strictly obtuse pentagon partners of regular polygons to the stated
periodic escape families at n=7 and12 (plus regular3,4,6 monohedral escapes).
The dodecagon continuous-family theorem still requires its own fresh review;
this file does not promote that dependency before its audit.

Neither right/acute P corners nor nonregular Q polygons are covered. The
unrestricted two-convex-polygon problem is unchanged and unresolved. No
computational search or imported monohedral classifier occurs in this proof.
The n=14 local argument was independently reached by two authors before
extraction; that agreement is not a substitute for a fresh hostile review.
No current primary-source priority audit of this large-n theorem has been
completed, so no novelty or priority assertion is made.
