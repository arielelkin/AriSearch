# Two private octagon slots: an unrestricted all-metric periodic escape

Date:2026-10-13. Status: independently reviewed VALID synthesis. A restricted-family theorem, not unrestricted two-convex impossibility.

Fresh complete reviews: [source-track audit](../reviews/contact-right-angle-two-private-general-hostile-review.md) and [affine-track audit](../reviews/contact-structure-two-private-octagon-core-all-metric-synthesis-review.md).

## Theorem and exact hypotheses

Let P be any genuine compact convex pentagon with one90-degree corner and four112.5-degree corners. Let Q be any genuine compact convex octagon with eight135-degree corners. Let u,v be the two P side lengths incident with its90corner, and assumeu!=v. Suppose EXACTLY TWO native Q side slots have lengths absent from ALL five native P side lengths. Those private lengths may be equal or distinct. Other native length collisions are allowed.

If this pair admits any plane tiling under the unrestricted definitions, it also admits a tiling invariant under a nonzero translation. Therefore no pair in this family is aperiodic. It is NOT claimed that every original tiling is periodic, that every pair is tileable, or that a doubly periodic tiling exists.

## Reviewed dependencies

1. [Unrestricted native reduction](contact-right-angle-unrestricted-native-reduction.md), [hostile review](../reviews/contact-right-angle-hosted-side-necessity-hostile-review.md): constant native side-neighbor species, P wordsR/S, no Q-hosted flat stars, all Q contacts whole, QQslots at mosttwo and separated by3/4, and private slots mustbeQQ.
2. [Clean typeR limit](contact-structure-two-private-octagon-clean-r-limit.md), [independent review](../reviews/contact-structure-two-private-octagon-core-clean-limit-review.md): fixedQQmask gives a plane limit with onlyPPQ/PQQ native stars, hence ETE/trivalent and all PtypeR. The proof counts positive-score stars directly and preserves additive corner-occurrence scores through coalescence; it does not invoke zero weight for each tile.
3. [Periodic QQ cores](contact-structure-two-private-octagon-periodic-core.md), [review](../reviews/contact-structure-two-private-octagon-core-hostile-review.md); [complement bands](contact-structure-two-private-octagon-complement-bands.md), [component/synthesis review](../reviews/contact-structure-two-private-octagon-core-complement-synthesis-review.md).
4. [Anchored-strip periodic completion](periodic-scaffold-anchored-strip-completion.md), [review](../reviews/periodic-scaffold-anchored-strip-hostile-review.md).
5. [Equal-private tagged geometry audit](../reviews/contact-structure-two-private-octagon-core-equal-length-geometry-review.md), conditional on the actual cleanR tiling.

The geometric core and band proofs below use only unique half-turn QQneighbors with two nonadjacent slots. Their original distinct-length hypothesis was a sufficient way to derive that uniqueness; equal-length uniqueness is proved separately here.

## Native lengths, masks, and the clean limit

Orient P counterclockwise with its five native edge lengths(x,u,v,y,w) and edge vectors

    (x*c,-x*t), (u/r,u/r), (-v/r,v/r), (-y*c,-y*t), (0,-w),

wherec=cos(pi/8),t=sin(pi/8),r=sqrt2. All lengths are positive. Closure gives

    u-v=r*c*(y-x), w=(u+v)/r-t*(x+y).

Thus u!=v impliesx!=y. Every P admits this normalization up to an isometry, with its unique90corner between u,v. TypeR has Q neighbors on u,v,w and P neighbors onx,y. TypeS has Q neighbors onx,y and P neighbors onu,v,w.

Privacy and the reviewed native word theorem force exactly two QQneighbors for each Q, at the private slots. Up to dihedral indexing their positions are0,3or0,4. Arbitrary full-side aliases at other slots do not create further QQneighbors because the local two-neighbor maximum is already attained.

Let p,q count tiles uniformly in square windows. FixedQQdegree implies y_PQQ=2q+O(R), and native angle incidence implies p=2q+O(R), with four-right and flat star countsO(R). The clean-limit theorem supplies a plane tiling of the SAME polygons, with onlyPPQ/PQQ vertices. In it all Pacute corners are PQQ, so every P is typeR. Neither species can disappear: neither single-species palette can fill the P112.5orQ135native corners.

## Tagged public sides and equal-private shape symmetry

At a Q vertex incident to a QQedge, the remaining P sector is90. A public Q side incident with such a vertex therefore matches a Pacute-adjacent leg, taggeduorv. A public Q side with neither endpoint at a QQvertex matches Pmiddle sidew: its P side has112.5at both endpoints, and no other typeR Q-labeled P side does. Mask spacing ensures no public side has QQvertices at both ends.

These endpoint tags remain unambiguous whenw=uorw=v. The nonacute Pslotsx,y cannot serve public Q edges in this tiling even if their numerical lengths coincide, because their derived typeR neighbor species isP. Each P contributes exactly one Qcontact of each tagu,v,w. Each native Q side's tag is fixed by its endpoints and length; u!=v distinguishes the acute tags. Counting gives N_tag*q=p+O(R) for each tag. Sincep=2q+O(R) andq has uniform positive quadratic count, each Q has exactly two sides of each tag. Thus the four acute-tag public slots consist of two u and two v; the two remaining slots arew.

Suppose now the two private lengths coincide,H.

* Mask0,3 gives word(H,a,b,H,c,w,w,d), witha,b,c,d acute tags. At the common Qvertex of the shortgap sidesa,b, the two adjacent Ptiles meet along a whole side. Ifa!=b, this interface has lengthx on one P andy on the other, impossible becausex!=y. Hencea=b; two-each tag counts forcec=d to be the other tag. The word is(H,u,u,H,v,w,w,v), or its u/v-swapped version. Its equiangular geometry has a reflection symmetryF exchanging private slots0,3: the side word is cyclically palindromic, so the reflected boundary edge cycle agrees after that native relabeling.
* Mask0,4 gives word(H,a,w,b,H,c,w,d). The private and w opposite vectors cancel. Closure of the four diagonal edges givesa=candb=d, by its two Cartesian coordinates. The word is(H,u,w,v,H,u,w,v), up to swaps. Every pair of opposite sides is equal and parallel, so Q is centrally symmetric and its half-turnF exchanges private slots0,4.

This establishes equal-private Qsymmetry without a general metric search. It does not require u,v,w numerically distinct or x/y absent from the other numerical side values.

## Unique half-turn QQneighbors, including private aliases

If private lengths are distinct, each occurs on a single Qside. At each private contact the only two opposite-side placements are reflection across its supporting line and half-turn about its midpoint. Reflection fixes endpoints and makes the two outgoing QPside lengths at each endpoint equal; the remaining P90sector has two acute legsu,v, contradiction. Thus each actual QQneighbor is the midpoint half-turn.

If private lengths are equal, matching either native private slot initially offers two endpoint identifications each. The symmetryF above carries one native private edge to the other. Composing attachment isometries withF identifies these apparent alternatives as only TWO actual Qpolygon placements: the reflected copy across the supporting line and the midpoint half-turn of the reference polygon. The endpoint-fixed reflected placement is again impossible because it wouldforceu=v. Thus every QQneighbor is a midpoint half-turn here as well. Bookkeeping indices impose no marking rule; this argument quotients by actual polygon symmetries.

WriteH_i(z)=2m_i-z,H_j(z)=2m_j-z, with private side midpointsm_i,m_j. In indexed placementgQ the two neighbors aregH_iQ,gH_jQ. They are distinct: equality would make compactQ invariant under nonzero translation2(m_i-m_j). Follow the nonbacktracking QQchain. For every integern its polygon sets obey

    Q_(n+2)=Q_n+a, a=R_g[2(m_i-m_j)]!=0.

Odd-starting products reverse the native i/jorder but also reverse the placement's orthogonal part, giving the same world vectora. This excludes all finite QQcycles, EVEN WHEN Q IS CENTRALLY SYMMETRIC: a cycle of lengthk would implyQ_(n+2k)=Q_n, whereas the recurrence givesQ_n+k*a. Compactness forbids it. Every chain therefore has the same positive period length2|m_i-m_j|.

## Common periodic scaffold and periodic completion

Joining Qcentroids to their two private-side midpoints gives a simple proper core in each chain. Core pieces are inside Qinteriors except at full QQseams. Nonadjacent Qtiles cannot touch: the only native star containing twoQ135sectors isP90+Q135+Q135, which makes them QQadjacent. Thus different cores are disjoint. Each is a finite motif repeated by its nonzero chain period and lies within bounded distance of its period line.

Two such proper cores with nonparallel period directions wouldintersect by proper-arc Jordan separation: the second has its two ends in opposite far halfplanes of the first. Hence all period vectors are parallel. Their lengths coincide, so one choice of signa0is a period of every Qchain and of the entire Qscaffold.

Each chain union is a closed proper topological strip. Its two individuallya0-invariant boundary curves, nonneighbor-contact exclusion, finite packing in a period band, and whole P-Qanchoring show that complement components are invariant open bands between consecutive Qstrips with a uniform width bound; no outer halfplane can be filled because every P is within its diameter of Q. These are precisely the reviewed complement-band hypotheses.

A Pplacement is fixed by any whole native Qanchor edge, its Pnative side and an endpoint identification. Packing bounds the number of these candidates in each length|a0|band uniformly. The reviewed anchored-strip theorem therefore periodizes a completion independently in each open band, with periods bounded by one finite-state bound. A common finite multipleM a0is a period for all band fillings and the Qscaffold. Their closed supports cover the plane and have disjoint interiors. This gives the required admitted periodic tiling.

## Computation, scope and remaining target gaps

This synthesis is analytic and uses no bounded search or new solver certificate. Exact16-ring computations for one equal-private example are independent illustrative evidence, NOT a prerequisite for this all-metric argument. Positivity of actual shapes, the exact angle palette, u!=v and exactly two private Qside slots are essential. Symmetric P(u=v), Qwith zero/one private slot, other angle palettes and all arbitrary convex pairs remain outside. Source-forcing and infinite existence of a genuinely aperiodic pair remain unresolved. No novelty claim or final report is made.

## Complete two-private angle-palette corollary

The separately [proved symmetric theorem](contact-symmetric-two-private-all-metric-periodic-escape.md), its [independent synthesis review](../reviews/contact-symmetric-two-private-all-metric-synthesis-review.md), and its [independent symbolic-carrier audit](../reviews/contact-symmetric-two-private-symbolic-carrier-hostile-review.md) cover u=v. Its clean typeR limit forces equal private lengths. Mask3 has an explicit symbolic two-Q/four-P carrier and mask4 is the positive symmetric channel carrier. Neither branch assumes a rule for admitted placements.

Consequently EVERY pair in the stated right-pentagon/equiangular-octagon angle palette with exactly two private Q side slots has a periodic escape whenever tileable, at all positive side lengths, with all native length aliases, reflections and partial contacts permitted. The unequal-length proof above and the symmetric proof together exhaust the acute-leg cases. Zero/one-private Q partners and other angle palettes remain outside this corollary. The original unrestricted target is still unresolved.
