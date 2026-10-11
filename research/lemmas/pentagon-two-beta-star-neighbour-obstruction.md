# A one-large-corner pentagon cannot have just one Q side

**Status:** adversarially reviewed; the fresh reviewer independently read this
standalone text and found it valid without repair. See the explicit follow-up
in the [large-polygon review](../reviews/all-obtuse-pentagon-regular-large-polygon-review.md).
This local lemma supplies the n=14 final step in the general regular-polygon
obstruction. It supersedes the narrower two-angle n14 metric candidate
analysis, whose length calculations are unnecessary for the contradiction.

## Exact local hypotheses

Consider an admitted edge-to-edge, trivalent plane tiling by a genuine
convex pentagon P and a genuine convex polygon Q. Assume:

1. Every Q vertex has type P,P,Q; in particular two Q sectors never meet.
2. P has exactly one native beta corner. This corner is always P,P,P.
3. Every P,P,P star has exactly two beta corners and one alpha corner,
   where alpha!=beta. All other native P corners differ from beta.

No equal side lengths, regular Q, finite orientation set, or restriction on
reflection is assumed in this local lemma. Then every P has exactly two
Q side neighbors, in nonadjacent positions.

## A beta-beta edge forces at least one Q side

At the beta corner of a P, the other two sectors are a second P-beta corner
and a P-alpha corner. In a trivalent full-edge tiling these are its two
side neighbors at that corner. Thus one beta-incident edge is a P-to-P
contact with beta endpoints on both copies.

At the contact's opposite endpoint both copies contribute native P corners
different from beta, because P has only one beta vertex. That endpoint
cannot be P,P,P: its two already present nonbeta sectors leave room for
at most one beta sector, whereas assumption3 requires two. It must be
P,P,Q. Its Q sector shares the other incident side of each P at that
endpoint. Therefore every P has at least one Q side.

Two Q side neighbors cannot be consecutive around P, since their common
P corner would give a P,Q,Q star, excluded by assumption1. A pentagon thus
has at most two Q side neighbors. It remains to exclude exactly one.

## One Q side is locally impossible

Suppose a P has exactly one Q side. At its two endpoints the star is
P,P,Q. At each of its other three native vertices the two side neighbors
are P, and the star is P,P,P. Those three vertices form a path of three
consecutive vertices in the native pentagon cycle. One is the unique beta
corner; the other two are alpha corners by assumption3.

If beta is the middle vertex of that path, both beta-incident edges have
opposite endpoints at P,P,P alpha corners. However the preceding
beta-beta edge argument proved that one such opposite endpoint must be
P,P,Q. This is a contradiction.

If beta is an end of the path, the two alpha P,P,P corners are adjacent.
Their shared native side is a P-to-P edge. At each endpoint, both other
sectors are beta, so the single P copy across that whole edge would have
to supply beta at both native endpoints. This is impossible: P has exactly
one beta native vertex and the shared side has positive length.

The two cases exhaust the path. Hence a P cannot have one Q side, proving
it has exactly two. The proof treats reflected copies in exactly the same
way; only endpoint identities and native corner counts are used.

## n=14 application and compactness boundary

In the regular-unit14-gon application, Q's angle is6pi/7. A hypothetical
all-obtuse P,Q tiling gives N_P=8N_Q+O(R). A P with two nonadjacent Q sides
exists, since otherwise14N_Q<=N_P+O(R), contradicting quadratic counts.
Its four Q-star P corners are strictly below
H=2pi-6pi/7-pi/2=9pi/14<2pi/3. Thus the prototile has four low corners and
one unique angle beta>=2pi/3. The equality beta=2pi/3 would force every
P,P,P star to have three beta corners, contradicting N_P=8N_Q+O(R) and
V_PPP=4N_Q+O(R). Therefore beta>2pi/3, and every P,P,P star has one or two
beta sectors. Native beta corners always belong to P,P,P.

Write T1,T2 for those star counts. The whole-plane incidence identities are

    T1+T2=4N_Q+O(R),
    T1+2T2=N_P+O(R)=8N_Q+O(R).

Consequently T1=O(R), uniformly in translated windows. This is not a
pointwise conclusion about the original tiling. Mark every tile incident
to a one-beta star bad, extract growing bad-free disks, and take the
admitted good limit by the independently reviewed full-edge compactness
argument in the
[heptagon classification](all-obtuse-pentagon-regular-heptagon-classification.md).
The limit has only two-beta P,P,P stars. Their third corner is always
alpha=2pi-2beta, so it satisfies all three local hypotheses.

The local lemma gives exactly two P-to-Q sides per P in the limit, while
Q has fourteen P sides. Full-side counting then gives

    2N_P=14N_Q+O(R).

The curvature identity for that same admitted limit is still
N_P=8N_Q+O(R), with N_Q=Theta(R^2). These identities contradict each other.
Thus no strictly obtuse convex pentagon tiles with the regular14-gon.
No angle-multiplicity classification or metric candidate is required.

## Scope, imports, and source boundary

The local lemma itself uses only its explicit trivalent full-edge star
hypotheses. Its application imports the reviewed all-obtuse forcing result
and the reviewed bad-free translated-limit argument. It does not assert
that a linear defect count vanishes pointwise in an original tiling.
Neither the local result nor this application establishes an unrestricted
two-convex-tile theorem. No computation or certificate is needed. No current
primary-literature novelty audit was performed for this exact obstruction,
so no novelty or priority is claimed.
