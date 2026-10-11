# Primary prior-art audit: two hexagons with internally distinct side lengths

**Search date:** 2026-10-09. **Status:** mechanism-specific literature audit;
no priority or novelty claim. This record consolidates the three narrow
queries previously retained in the side-order search record and adds the
broader checks below. It is independent of the mathematical hostile review.

## Exact claim being compared

The repository theorem in
[hexagon-holonomy-distinct-lengths.md](../lemmas/hexagon-holonomy-distinct-lengths.md)
says that a tileable pair of genuine compact convex hexagons, each with six
pairwise distinct numerical side lengths, admits a doubly periodic tiling.
Cross-type side lengths may coincide; reflections and partial-side contacts
are allowed. Its conclusion concerns existence of a periodic witness, not
periodicity of every original tiling. The proof first obtains a trivalent,
edge-to-edge limit, then uses two simple side-length cycles and legal graph
triangles to select a four-face flat torus.

The specific mechanisms sought were: encoding corners by adjacent side
lengths; selecting legal triangle covers from two six-cycles; duplicating two
whole tiles of each type; and completing a flat torus from angle sums.

## Finding and remaining boundary

No matching theorem or matching length-cycle selection argument was located
in the queries and primary portions inspected here. That statement describes
this search, not the whole literature. The unrestricted-contact limit
mechanism and the geometric development of a flat quotient have substantial
classical precedent. The periodic witness's finite symmetry topology is also
within the scope of old 2-isohedral tiling catalogs. Consequently neither
flat-torus development nor the mere enumeration of periodic quotients should
be presented as new.

The part not matched by the inspected sources is the implication from an
arbitrary tileable internally-distinct pair to an angle-legal four-triangle
ring: the k>=4 argument, complete two-cycle classification, typed-corner
coverage selection, formal length splitting, and octahedron angle-partition
argument. This is a precise comparison boundary, not evidence sufficient
for an originality claim.

## Primary sources and mechanism comparisons

### 1. Zhu, Wang, Yan: monohedral hexagons and local linear systems

Ze Zhu, Erxiao Wang, Min Yan, *Hexagonal Tiling of the Plane*,
[arXiv:2508.01404v2](https://arxiv.org/html/2508.01404v2), revised 2026-04-28.
Inspected: introduction, Main Theorem, Lemma 1 discussion, and Section 3's
local edge/angle-equation setup.

The Main Theorem assumes **congruent hexagons** and at least three incident
tiles at every vertex. It concludes membership in the three Reinhardt
hexagon types. The introduction explicitly separates side-length
combinations from cyclic arrangements and discusses earlier
internally-distinct edge cases. The proof extracts arbitrarily large
trivalent edge-to-edge regions, then obtains side equalities and corner
angle equations from a nineteen-tile neighborhood.

This is close prior art for the defect-free-region principle and the use of
local length/angle constraints. Its single congruence class does not supply
the mixed two-cycle legal-cover selection used here. In particular, a
single six-cycle is triangle-free when all six side lengths are distinct;
the repository's new domain necessarily uses both types. No implication
from this monohedral theorem to arbitrary fixed hexagon pairs is claimed.

The paper's reference [2] is B. Bollobás, *Filling the plane with congruent
convex hexagons without overlapping*, Ann. Univ. Sci. Budapest. Eötvös Sect.
Math. 6 (1963), 117–123. The original seven-page paper was **not recovered**
in this audit. Statements about its detailed contents above are limited to
what Zhu–Wang–Yan explicitly discuss, not a claimed fresh original-text
inspection.

### 2. Delgado, Huson, Zamorzaeva: 2-isohedral catalogs

O. Delgado, D. H. Huson, E. Zamorzaeva, *The classification of 2-isohedral
tilings of the plane*, Geometriae Dedicata 42 (1992), 43–117,
[publisher abstract](https://link.springer.com/article/10.1007/BF00147644),
DOI 10.1007/BF00147644. The abstract states that geometric splitting/gluing
and enumeration of Delaney–Dress symbols produce 1,270 proper 2-isohedral
types. Full catalog text was not accessible through the inspected publisher
page; no exact catalog number for the repository quotient is asserted.

Related primary source: D. H. Huson, *The generation and classification of
tile-k-transitive tilings of the Euclidean plane, the sphere and the
hyperbolic plane*, Geometriae Dedicata 47 (1993), 269–296,
[publisher abstract](https://link.springer.com/article/10.1007/BF01263661),
DOI 10.1007/BF01263661. Its hypothesis is a prescribed finite number of
tile orbits under a symmetry group. Its algorithms enumerate equivariant
types within that hypothesis. They do not assert that any tileable finite
protoset has a tiling with that symmetry property.

Thus periodic topology enumeration has old precedent. The missing step
for an application to this pair is precisely selecting a permissible
periodic topology from an initially arbitrary tiling.

### 3. Delaney–Dress realization and finite quotient curvature

O. Delgado Friedrichs, A. Dress, D. Huson, *Tilings and Symbols: a Report
on the Uses of Symbolic Calculation in Tiling Theory*, Séminaire
Lotharingien de Combinatoire B34a (1995), 16 pp.,
[primary journal PDF](https://www.mat.univie.ac.at/~slc/wpapers/s34bielefeld1.pdf).
Inspected Section 3.1, printed p.4, by rendering the primary PDF: text
extraction has a broken font encoding.

Section 3.1 gives a curvature expression for a **finite** Delaney symbol,
distinguishing Euclidean, hyperbolic and spherical realization. It defines
tile-k-transitivity by k symmetry orbits, assumes a discrete group with
compact orbit space for the size bound, and explains enumeration by
prescribed symmetry group. It also reports the 1992 two-orbit enumeration
using symbols of size at most 24 and zero curvature.

This confirms that finite combinatorial quotients and curvature-controlled
Euclidean development are established methods. A length graph's vertices
in the repository are *numerical side lengths* and its edges are *corner
occurrences*. Those are different data from the chamber adjacency graph
of a Delaney symbol. The source does not provide the repository's
legal-triangle cover selection theorem for two metric hexagons.

### 4. Frettlöh, Garber: monocoronal local-to-global order

D. Frettlöh, A. Garber, *Symmetries of Monocoronal Tilings*, Discrete
Mathematics & Theoretical Computer Science 17 (2015), 203–234;
[primary author PDF](https://www.math.uni-bielefeld.de/~frettloe/papers/corona.pdf),
[arXiv:1402.4658](https://arxiv.org/abs/1402.4658), submitted 2014-02-19.
Inspected Theorems 2.1–2.2 and Appendix A.10, printed pp.21–22 of the
author PDF.

The assumption is that **every entire vertex corona is congruent**; a
corona includes its incident whole tiles. Direct congruence yields an
isogonal crystallographic tiling. Allowing reflected coronas yields
crystallographic or one-dimensionally periodic tilings. Appendix A.10
classifies the three-hexagon corona case and explicitly starts with the
three incident ray lengths distinct.

This is a closer local metric comparison than a general open-problem
summary, but its congruent-corona assumption is much stronger than
trivalent contact. The repository ring may use four different corner
triple kinds and does not establish congruence of whole coronas. Therefore
these theorems cannot replace the two-cycle selection argument. Conversely,
no originality should be assigned to local length-based corona analysis
as a general method.

### 5. Soto Sánchez: edge-labeled toroidal hexagonal graphs

J. E. Soto Sánchez, *On Periodic Tilings with Regular Polygons*, PhD thesis,
IMPA / VISGRAF, version dated 2020-08-11,
[primary author PDF](https://chequesoto.info/docs/Tilings_JESotoS_ebook.pdf).
Inspected title/abstract and Section 5.4, printed pp.95–96. Web open failed;
the primary PDF was downloaded and extracted locally.

The thesis studies **already periodic regular-polygon** tilings, particularly
triangle-square tilings. Their restricted duals are represented by
edge-labeled hexagonal graphs on a flat torus. Section 5.4 uses nonnegative
integer edge labels and fixed sixth-root directions; closure is an integer
linear system. It then studies bases of permitted labelings for a fixed
toroidal topology.

Here labels are numerical lengths on graph edges, and a graph face becomes
an equiangular hexagon. The repository graph instead has lengths as
vertices and corner pairs as edges; polygon angles remain arbitrary.
No arbitrary-pair periodicity conclusion or legal triangle-cover selection
is present in the inspected section. The shared ideas are exact graph
encoding, closure constraints, and periodic quotient realization.

### 6. Nobili, Novaga, Paolini: periodic double tilings

A. Nobili, M. Novaga, E. Paolini, *Periodic Double Tilings of the Plane*,
[primary author PDF](https://people.dm.unipi.it/novaga/papers/paolini/Due_Volumi.pdf),
dated 2025-02-07 in the inspected version. Inspected introduction and
Theorems 1.1 and 3.2. An alternative primary repository copy is
[CVGMT](https://cvgmt.sns.it/media/doc/paper/6987/main.pdf).

Theorem 1.1 assumes a nondegenerate **periodic** two-generator tiling
minimizing perimeter relative to a fixed lattice. It classifies three
curvilinear configurations, including a straight-sided (6;6) case with
120-degree angles. Theorem 3.2 optimizes the lattice within that
isoperimetric hexagon configuration.

These are metric optimization results in an already periodic class. They
allow shape changes while retaining prescribed areas. They neither
preserve an arbitrary given pair nor prove that its initial tiling can
be replaced by a periodic one. They do not discharge the repository's
length-cycle selection step.

### 7. Sugimoto: monohedral edge-to-edge aperiodicity boundary

T. Sugimoto, *Tiling Problem: Convex Pentagons for Edge-to-Edge Monohedral
Tiling and Convex Polygons for Aperiodic Tiling*,
[arXiv:1508.01864](https://arxiv.org/abs/1508.01864), v4 dated 2017-07-10.
The inspected abstract concerns monohedral, edge-to-edge tilings. It does
not establish mixed-pair periodicity with unrestricted contacts. This
source was included in the original narrow check; the newer mechanism
comparisons above are the substantive expansion.

## The four-face witness and the old symmetry catalogs

**Audit inference, not a catalog identification:** the repository gluing
has a simultaneous index-flip map A_0<->A_1 and B_0<->B_1. It preserves
the private pairings and the common pairings j=i xor h(x), including all
endpoint identifications. Because paired face copies have the same metric,
this is an intrinsic isometry of the constructed flat torus. Across a
private edge joining the same side slot, its developed plane lift is a
half-turn about that edge's midpoint. Together with deck translations,
it acts transitively on the A copies and separately on the B copies.
Consequently this witness has at most two tile orbits; for incongruent
types it is 2-isohedral under that subgroup. Generically one expects a p2
group, but this audit does not compute its full wallpaper group.

This places the selected topology inside the old two-orbit framework.
Finding its exact Delaney symbol/catalog row would improve attribution.
It would **not** show that all arbitrary tilings with the distinct-length
hypotheses contain or admit that periodic topology. The legal selection
argument remains the substantive point to compare against further prior art.

## Related equilateral rational-angle lemma: attribution caution

The repository's
[equilateral rational-angle obstruction](../lemmas/new-angle-equilateral-rational-obstruction.md)
imports its small vanishing-sum classification from Lam–Leung, rather than
claiming that arithmetic classification is original. Its nonregular
pentagons have an adjacent supplementary corner pair. This is the
classical pentagon Type 1 condition, equivalent to the other three corners
summing to 2pi. A primary depiction is T. Sugimoto,
[2012 Forma paper, Fig.1](https://forma.katachi-jp.com/pdf/2701/27010093.pdf).

Recent primary confirmation: B. Klaassen, *Old Problem Revisited: Which
Equilateral Convex Polygons Tile the Plane?*, Journal for Geometry and
Graphics 29 (2025), 161–171,
[published PDF](https://www.heldermann-verlag.de/jgg/jgg29/j29h2klaa.pdf),
[arXiv:2506.18473v3](https://arxiv.org/abs/2506.18473), revised 2025-11-10.
Inspected Proposition 1 and printed pp.165–166. Klaassen explicitly
identifies adjacent and nonadjacent supplementary pentagon angles with
Types 1 and 2, and comparable triples of hexagon angles with hexagon
Types 1 and 2. His proof uses the accepted fifteen-pentagon classification;
his proposition is **monohedral**, without the repository's rational-angle
restriction. It is presented as a simplified proof of older results.

Thus the periodic Type 1 pentagon escape and centrally symmetric hexagon
escape are classical. The local exclusion of the remaining hexagon
branches with a regular pentagon is a restricted mixed-pair argument,
whose exact statement was not found here. Do not describe the whole
rational pentagon/hexagon classification or its periodic constructions as
new. Do not label every arithmetic hexagon branch Type 1 or Type 2:
some branches are excluded from tilings, rather than known monohedral types.

Further old primary lead, not a new import into the proof: O. Bagina,
*Tiling the plane with congruent equilateral convex pentagons*, JCTA 105
(2004), 221–232, DOI 10.1016/j.jcta.2003.11.002,
[primary article repository copy](https://core.ac.uk/download/pdf/82081785.pdf).
Its published text's introduction/Theorem 1.1 attributes the complete
equilateral monohedral classification to Hirschhorn–Hunt (1985). The CORE
web open failed in this session; the result was exposed by search, so it
is retained as a retrieval lead rather than a claimed fresh PDF proof audit.

## Exact web-search queries

All queries below were issued on 2026-10-09. Quotation marks and exclusions
are part of the actual query strings. The three first queries are
consolidated from the agent's prior narrow check. No fixed recency filter
was applied; current papers and old mechanism sources were both sought.

```text
two convex hexagons distinct side lengths periodic tiling
two hexagons tiling plane periodic conjecture pair
convex hexagon two prototiles distinct edges aperiodic tiling torus
"two hexagons" "tiling" "periodic" -site:reddit.com -site:wikipedia.org
"hexagons" "distinct side lengths" "tiling"
"convex hexagons" "two" "aperiodic"
tiling convex polygons "length graph" triangles torus
"two" "hexagons" "isohedral" tilings
"2-isohedral" "hexagons"
"convex hexagons" "distinct" "sides" tiling pair
"two prototiles" "hexagonal" periodic theorem
"dihedral" "hexagons" tilings theorem
"duohedral" tilings hexagon
"two prototiles" "convex" "hexagons" -site:reddit.com -site:wikipedia.org
"two" "hexagons" "torus" tiling
Grünbaum Shephard "Tilings with two types of tiles"
Dress Huson "two" "hexagons" tiling
"dihedral tilings" hexagons Grünbaum
"duohedral" "hexagon" tilings
"2-isohedral tilings" "convex" hexagons
"two congruence classes" "hexagons" tilings
"hexagons" "side lengths" "periodic" tiling theorem pair
"length" "graph" "hexagons" "tilings"
Huson "tile-2-transitive" euclidean tilings fundamental
"2-isohedral" classification "tiles" Huson
"two-isohedral" "convex"
"two" "hexagons" "different lengths" tiling
"DHZ92" tilings
"GLST85" tilings
"tile-2-transitive" "classification" Huson "plane"
Huson "classifying" "two" tilings 1992
"The classification of 2-isohedral tilings of the plane" pdf
"The generation and classification of tile-k-transitive tilings" pdf
"polygonal" "flat torus" "tiling" theorem
"convex hexagons" "edge labels" tilings
"Tilings and Symbols" Huson pdf
"The classification of 2-isohedral" hexagons length
"two hexagons" "aperiodic" theorem polygon periodicity
"two convex hexagons" tile periodic
"Tilings and Symbols" "pdf" Dress Huson Delgado -site:researchgate.net
"distinct side lengths" "hexagonal" "tiling"
"two hexagons" "isoperimetric" periodic tiling
"tilings" "triangle cover" lengths hexagons
Sugimoto equilateral pentagons "Type 1" "Type 2"
"equilateral" "rational" "pentagons" tiling
"hexagons" "edge lengths" "triangle" "torus" tilings distinct
Bollobas "Filling the plane with congruent convex hexagons" pdf
"two hexagons" "tiling" Bollobás
"convex hexagons" "pairwise distinct"
"hexagon" "distinct side lengths" periodicity
Frettlöh Garber "Symmetries of monocoronal tilings" 2014 doi
Bagina "Tiling the plane with congruent equilateral convex pentagons" primary pdf
Hirschhorn Hunt "Equilateral convex pentagons which tile the plane" pdf
"hexagon tilings" "length graph"
"hexagons" "four" "torus" "tiling" "convex"
"two polygons" "edge lengths" "periodic tiling" hexagons
"hexagons" "six distinct" "tilings"
"pentagon" "heptagon" "distinct" "tiling" periodic
"pentagon" "heptagon" "obtuse" tiling
"two polygons" "distinct side lengths" tiling
"pentagon" "octagon" "side lengths" "tiling" theorem
```

## Follow-on comparison for the all-obtuse (5,n) theorem

The final four queries above were issued after reviewing the root's new
[internally-distinct all-obtuse (5,n) theorem](../lemmas/distinct-length-obtuse-pentagon-higher.md).
No matching arbitrary-pair implication was located in those query results;
the follow-on check is narrower than the main mechanism audit.

A close old topology example was identified in L. X. Benedict,
*The Physics of Fullerene-Related Materials*, Berkeley PhD thesis (1996),
[primary institutional PDF](https://escholarship.org/content/qt6b43q4fb/qt6b43q4fb.pdf?v=lg),
Chapter 12, printed pp.143–145 (PDF pages154–156), Figures12.1–12.2.
The periodic planar pentaheptite construction uses a bond rotation in a
four-hexagon cell, producing two pentagons and two heptagons with eight
trivalent vertices per cell. Each pentagon has one pentagon/four heptagon
neighbors, and each heptagon three heptagon/four pentagon neighbors.
There are two PPQ and six PQQ vertex incidences.

**Audit inference:** these are exactly the coarse face-neighbor and
vertex-type counts of the repository's four-triangle (5,7) ring quotient.
Counts alone do not establish an isomorphism of endpoint maps; none is
claimed here. Benedict studies a specific physical periodic network with
numerically annealed geometry. He does not prove periodic tilability of
arbitrary fixed convex pairs or the distinct-length triangle-cover
selection. This source reinforces that a four-face periodic (5,7)
construction topology should not be claimed new.

The search also found an author-hosted Deza et al. pentaheptite paper,
[retrieval lead](https://micheldeza.altervista.org/withFowler/penta.pdf).
Web retrieval timed out, direct HTTPS failed certificate verification, and
HTTP returned403. Its full text is not promoted to an inspected proof;
the successfully inspected institutional thesis above supplies the specific
comparison. The DD finite-symmetry and flat-quotient boundaries already
recorded in this file apply equally to the new (5,7) witness.

## Retrieval limitations and further concrete checks

The 1992 full 2-isohedral catalog, Bollobás's original 1963 paper, and the
full older Grünbaum–Shephard classification material remain unchecked.
Their absence prevents a comprehensive historical originality audit.
The primary author/journal texts above were preferred over the secondary
search results. Search hits about lozenge tilings of a hexagonal *region*,
marked Penrose/Taylor–Socolar hexagons, spherical tilings, and periodic
perimeter minimization were not treated as fixed unmarked-pair theorems.

The author website [Jaap Scherphuis's tiling results](https://www.jaapsch.net/tilings/)
was inspected as an original-computation lead. Its claimed exhaustive
two-tile-unit search assumes **two identical convex polygons**; it does
not cover two arbitrary hexagons or establish a periodicity implication.
The [EPINET Delaney–Dress introduction](https://epinet.anu.edu.au/page/epinet2_mathematics_delaney_dress)
was used to locate the original papers, not as a substitute for their
theorems. MathOverflow retrieval and some PDF web renders failed; no
theorem contents were inferred from those failures.

Useful next attribution work: produce the four-face witness's exact
Delaney symbol, identify its 1992 catalog type, and search the catalog's
metric realizability commentary for two simple six-cycle side words.
Useful next mathematical work is outside this audit: repeated length
symbols make ray labels repeat, so graph triangles can degenerate to
typed walks. The current selection theorem does not cover that case,
one internally-distinct member alone, or nonhexagonal partners.
