# Paired Ammann H/D cannot be convexified without changing face incidence

Date:2026-10-13. Author:luna, using root's local HH-seam argument.
Status: **[fresh independent hostile review VALID](../reviews/ammann-hd-incidence-preserving-convexification-fresh-hostile-review.md)**. This kills a concrete cross-boundary reassembly mechanism, not arbitrary two convex polygons.

## Exact infinite precursor and changed proposal

Fix any generic J in the reviewedG* domain. Every admitted unmarked source tiling by H6,P1,P2 has the reviewed14-star atlas and a unique P1/P2 pairing across the full c seam, with K matched toK andL toL. Replace each paired P1/P2 by its unionD, leaving each H6 as oneH face. This gives an exact infinite two-shape H/D covering with disjoint interiors. At the reference placement,

    D=(0,J',1,L,1+w^2,J2,w^2,K).

D is a positive-area nonconvex support; K,L are its two reflex boundary corners because the omitted third source tile has angle strictly less thanpi there. H is the original convex hexagon. This precursor does not satisfy the original convex-tile requirement.

The proposed changed mechanism fills D's reflex notches and transfers corresponding regions from adjacent H/D faces, or moves shared vertices, while retaining the same macro face identities. It changes the earlier whole-source/cut hypotheses. Before hull or patch enumeration, there is a local incidence obstruction.

Define incidence-preserving convexification precisely: final faces correspond one-to-one to the original H/D faces, with the same embedded boundary graph/cyclic face incidence, possibly moving its vertices and deleting degree2 vertices or inserting straight degree2 subdivisions. No new branching vertex, third face at a former two-face vertex, face split/fusion or additional native boundary corner is permitted. Every final face must be a compact convex polygon with nonempty interior. A graph degeneration changing those incidences is outside the definition.

## Reviewed native labels and exact c pairing

Write H corners in order

    0=A,1=J',2=B,3=J,4=D,5=J''.

Its native sides have labels(a,b,b,r,r,a): side3 joins J toD and side4 joins D toJ''. G1 makes a,b,r,c pairwise distinct. The relevant reviewed atlas stars are

    K-type:(H-J',P1-K,P2-K) or(P1-J',P1-K,P2-K),
    L-type:(H-J'',P2-L,P1-L) or(P2-J2,P2-L,P1-L),
    J-type:(H-J,P1-J',H-J'') or(H-J,P1-J',P2-J2),
    Penrose-type:(H-D,H-D,P2-G).

P1-K/P2-K share their unique c sides at a K vertex; the far endpoints areL/L. Likewise P1-L/P2-L share c atL with far endpointsK/K. Thus these pairs are exactly the same reviewed c-partnerD, not two unrelated polygons that merely touch at one corner.

Every H-J' is K-type and becomes a degree2 macro boundary vertex between thatH and oneD. An H-J'' which is L-type also becomes degree2 between thatH and oneD. HOWEVER H-J'' may instead be J-type; it is false that every H-J'' is universally L-type. The following local argument supplies a required L-type occurrence without making that false quantifier change.

## Local lemma: a J-type H-J'' has an H neighbor with L-type J''

Suppose H2-J'' occurs in J-type(H1-J,P1-J',H2-J''). At the H1-J corner, its only r arm is native side3; at H2-J'', its only r arm is native side4. Their shared whole seam is therefore H1 side3(J-toD) against H2 side4(D-toJ''). Its opposite endpoint carries D corners of BOTH H copies.

The two H copies are distinct: one positive-length seam has different native endpoints, and one genuine polygon cannot place two distinct native vertices at the same source point. At the far endpoint the reviewed atlas forces exactly(H1-D,H2-D,P2-G). Therefore H1's OTHER r side, its side4, has P2 as neighbor there rather thanH. If H1-J'' were J-type, that corner would force side4 to be an HH seam, contradiction to this actual full-side neighbor. Equivalently, it would place three H sectors at the D/D endpoint, a star absent from the complete atlas. H1-J'' must be L-type. QED.

The argument survives reflection of the entire source field: the native labels and unique r-arm endpoint match remain the same. It uses no source-patch occurrence, primitivity, empirical star frequency or hierarchy extrapolation.

## Theorem: every incidence-preserving convexification has a small-face escape

Every admitted generic source field contains H copies; this follows from the reviewed universal anchored source count h(R)=Theta(R^2). Choose anyH. If its J'' is L-type, retain it. Otherwise the local lemma gives an adjacentH whose J'' is L-type. Thus every source field has an H occurrence with both universally K-type J' and L-type J''.

In the paired H/D precursor, that H face has TWO degree2 boundary vertices, at its distinct native J',J'' corners. At a degree2 vertex with two incident convex final faces, their local sectors sum2pi and each is at mostpi. Both sectors are therefore exactlypi. Each such vertex is flat and cannot be a genuine native polygon corner. If it has been deleted as a degree2 subdivision already, the same absence of a native corner holds.

The H boundary originally has six vertices and the incidence-preserving operation creates no additional native boundary vertices. At leastJ',J'' disappear from its genuine corner count. Hence the corresponding final H face has at most four genuine corners. Positive area and convexity force at least three. Every triangle or convex quadrilateral tiles periodically alone under unrestricted isometries. Any proposed final protoset containing this face shape therefore has an admitted periodic omission escape.

Consequently no incidence-preserving convexification of this exact H/D precursor can yield an aperiodic pair of unmarked convex polygons. If it branches into additional congruence classes, it already fails the two-shape requirement; even if only two classes survive, the small-face escape kills aperiodicity. No claim that every final tiling is periodic is made. QED.

## Why the elementary notch transfer falls in this family

At D's K reflex corner the source-third tile contains the exact X triangleHEK, and atL it contains the Y triangleFGL, in the reviewed thick frame. Filling those notches and removing the same triangular regions from the third source macro replaces a two-edge boundary path by its chord. The endpoints already belong to the source Penrose boundary graph; no third macro face is inserted at the vanished apex. As a pure boundary exchange retaining H/D face identities, this is precisely degree2 suppression, so the preceding theorem applies before computing hull caps or checking their congruence.

A more complicated transfer that creates a new branching endpoint or splits a face is a genuinely changed hypothesis and is not silently covered. It must give exact new boundary words, positive containment and convex geometry before any broader enumeration.

## Scope, blockers and restart point

The original cross-boundary proposal supplied a real infinite nonconvex H/D precursor, stronger than an isolated two-pentagon module. Its simple incidence-preserving convexification is nevertheless **excluded** by a reusable local spatial obstruction. Whole-Ammann source-supported parity and source-by-source area-module failures are separate exclusions; this theorem does not assume either, nor area rank3.

The next construction must change the actual failure hypothesis by adding a third final face at the forced two-face H vertices, introducing new branching boundary vertices/cuts, splitting an H/D macro, or using a different source/parameter outsideG*. Merely shifting J,K,L coordinates, filling the same caps or enlarging a source patch preserves the obstruction. No further hull-cap or finite-word enumeration was run after this local killer was established.

Such an explicitly changed construction would still need exact infinite covering and unrestricted shape-only forcing, including reflections, partial contacts and omission. Those remain unproved. No novelty or unrestricted impossibility claim is made.

## Dependencies and review

Only the reviewed generic source14-star atlas, G1 edge labels, unique c pairing, positive H existence and the elementary two-convex-sector/triangle-quadrilateral periodic facts are used. The source forcing theorem was checked for applicability, not re-audited. There is no search, solver, numerical approximation, finite source-hull claim or computational certificate behind this analytic argument. Fresh hostile review should attack the HH seam endpoint labels, distinction of c partners and final face-incidence hypothesis.
