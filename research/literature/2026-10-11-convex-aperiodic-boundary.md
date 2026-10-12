# Literature boundary: convex aperiodic sets, Ammann's three polygons, and the 3.7.1 periodicity statement

**Date:** 2026-10-11. This extends [2026-10-02](2026-10-02-search.md),
[2026-10-09](2026-10-09-search.md), [2026-10-10](2026-10-10-search.md),
[2026-10-11](2026-10-11-search.md) and the
[Ammann convex audit](../reviews/ammann-convex-source-audit.md). It does not
repeat their findings except where new primary text changes them. It is a
bounded search record. It is not a completeness or priority claim.

**Current boundary:** Healey 2011 proves the three-shape benchmark under its
complete-edge convention; the repository verifies/strengthens it on G* with
reflections and arbitrary contacts. The correction below supersedes the
initial search's missing-proof conclusion. No two-shape solution was located
in this bounded search; this checkpoint adds no new literature search.

## Target convention (for comparison)

The target is two unmarked convex polygons. All isometries are allowed,
including reflections. Contacts are arbitrary, so the tilings need not be
edge-to-edge. A tiling may use only one of the two shapes. The set must
admit a tiling, and **every** tiling must have no nonzero translation. In
the Mozes / Smith–Myers–Kaplan–Goodman-Strauss terminology this is "strongly
aperiodic". The target therefore states the strong notion directly and
does not need any weak-to-strong reduction.

## Databases, archives and tools

* arXiv API (`export.arxiv.org/api/query`), arXiv PDFs.
* Internet Archive full-text search (FTS) backend
  `be-api.us.archive.org/fts/v1/search` and its Open Library front end
  `openlibrary.org/search/inside.json`. This search returns OCR highlight
  snippets for loan-restricted books, including the scanned 1987 Freeman
  *Tilings and Patterns* (item `isbn_0716711931`). All verbatim book text
  below was **stitched from these OCR snippets**. Some symbols were
  OCR-garbled (for example `.9'`, `ff`, `f/'` for the script S, and `^1` /
  `^■^` for script T); I restored them as S and T. No page images were seen.
* archive.org metadata and advanced-search APIs. The `inside.php` search
  for the restricted book returned "Item not available".
* Google Books: the API returned 429 (quota 0) and the web search page
  redirected. Neither was usable.
* Web search, used for leads only. Secondary results were not used as
  evidence.
* Downloads went to `/tmp/claude-1000/lit-convex/` and were treated as
  untrusted data.

### Exact queries

arXiv API (sorted by submission date):
`all:convex AND all:aperiodic`; `abs:"convex polygons" AND abs:tiling`;
`abs:"aperiodic" AND abs:"two tiles"`; `abs:undecidable AND abs:tiling AND abs:polygons`;
`abs:"convex hexagons" AND abs:tiling`; `abs:dihedral AND abs:tilings AND abs:convex`;
`abs:aperiodic AND abs:polygons AND abs:reflections`; `ti:aperiodic AND ti:convex`;
`au:Sugimoto_Teruhisa`; `au:Goodman_Strauss`; `au:Socolar_J`;
`abs:"aperiodic" AND abs:"convex" AND abs:tile`.
I also fetched metadata by ID for 2106.08155, 2409.15880, 2404.00534,
2501.07090, 2609.09603, 2508.01404, 2507.20867, 2409.11582, 2506.11628,
2111.03979, 2110.08915, 2506.18473, 2106.03655, 2412.17382, 2603.27827,
2610.05438, 1708.00274, 1911.12752, 2405.04843 and 2307.08184.

Internet Archive FTS. Book-restricted queries took the form
`(<phrase>) AND identifier:isbn_0716711931`. Phrases used:
`"one hexagon and two pentagons"`, `"recomposition of one by Penrose"`,
`"must be chosen"`, `"different lengths"`, `"It contains only three tiles"`,
`"using the markings shown in"`, `"tiling by these convex polygons"`,
`"for we must have"`, `"three unmarked"`, `"remarkable example of such a set"`,
`"each of which is an unmarked"`, `"the smallest sets of aperiodic prototiles"`,
`"interesting problem of finding the"`, `"admits a periodic tiling"`,
`"which possesses a translation"`, `"By a polygon we mean a topological"`,
`"disk bounded by a finite"`, `"of prototiles and suppose that each"`,
`"polygon. Suppose further that"`, `"admits an edge-to-edge tiling"`,
`"Prove that if a finite set"`, `"be as in Statement"`, `"Prove that any patch"`,
`"directly congruent"`, `"mirror image"`, `"580"`, `"581 "`, `"582"`,
`"Pentagrid"`, `"unmarked convex tiles"`, `Ammann`, plus phrases that
returned nothing: `"three convex"`, `"10.3.28"`, `"two convex"`,
`"asterisks"`, `"research problem"`, `"exercises marked"`.

Unrestricted FTS queries: `"two convex pentagons"`, `"three convex polygons"`,
`"convex pentagons and a convex hexagon"`, `"aperiodic with no matching"`,
`"forces nonperiodicity"`, `Ammann AND "convex" AND "pentagons" AND "hexagon" AND aperiodic`.
Phrase follow-ups were run inside `oldnewunsolvedpr0000klee` (Klee–Wagon),
`unsolvedproblems0000crof` (Croft–Falconer–Guy) and `penrosetilestotr00gard`
(Gardner).

Web search: `Ammann "two pentagons and a hexagon" aperiodic convex Penrose rhombs`;
`"Tilings and Patterns" Ammann convex polygons aperiodic "three convex" pentagons hexagon 10.5`;
`Grünbaum Shephard "Tilings and Patterns" second edition Dover 2016 appendix updates aperiodic`;
`"Unsolved Problems in Geometry" C18 aperiodic "convex" Ammann "three" tiles`;
`aperiodic set "convex polygons" no markings smallest known Ammann three convex reflections allowed proof`;
`Grünbaum Shephard "Theorem 3.7.1" tiling translation periodic`;
`"Tilings and Patterns" theorem "singly periodic" OR "one translation" ...`;
`Goodman-Strauss "Open questions in tiling" weakly aperiodic strongly aperiodic ...`;
`"Tilings and Patterns" ... exercises "two asterisks" ...`.

## 1. Ammann's three convex polygons: primary text recovered

**Location correction.** The construction is in *Tilings and Patterns*
(Freeman 1987), Section 10.3, Figure 10.3.28, on pp. 547–548. The figure
caption appears immediately before the running head "548 APERIODIC TILINGS".
The book index (recovered by OCR) reads "Aperiodic sets of convex polygons,
547-549" and "Convex polygons: aperiodic tiling by, 547-549, 581". Wagon,
*Mathematica in Action* (1991), cites it as "[GS, Fig. 10.3.28]". Sugimoto's
citation "pp. 580–582" points into Section 10.7 *Notes and References*,
which includes the pentagrid discussion (index: "Pentagrid, 581-582"). The
p. 581 convex-polygon note was **not** recovered; none of the FTS phrases
hit it.

**Main text (p. 547, stitched OCR):**
"... as in the original kite and dart tiling.) This raises the interesting
problem of finding the smallest sets of aperiodic prototiles, each of which
is an unmarked convex polygon. Ammann has produced a remarkable example of
such a set by recomposition from the set P3. It contains only three tiles —
one hexagon and two pentagons, see Figure 10.3.28."

**Caption of Figure 10.3.28 (stitched OCR):**
"An aperiodic tiling due to Ammann which uses three unmarked convex polygons
as prototiles — one hexagon and two pentagons. This tiling is a
recomposition of one by Penrose rhombs (set P3) and is obtained from it
using the markings shown in (a). These markings are completely determined
by the choice of the point L, for we must have AJ = LF, JB = LG = KC, and
DK = HL. For aperiodicity L must be chosen so that FL, GL, HL and JK are of
different lengths. In (b) the relationship between a tiling by these convex
polygons and a tiling by the set P3 is indicated by dashed lines on the
left."

Sugimoto 1602.06372v2 Fig. 4 states the same relations with relabelled
points: GL = DJ, FL = CJ = EK, HK = BJ, with DJ, CJ, BJ, KL distinct, and
free point J.

**Findings**

* No exact coordinates are given for L. There is no substitution matrix,
  and no proof in the recovered text. "For aperiodicity L must be chosen
  so that ..." is a stated **necessary** genericity condition. It is not a
  sufficiency argument. Nothing recovered shows that all tilings,
  including non-edge-to-edge ones, reconstruct P3.
* **Reflections.** *Tilings and Patterns* uses "congruent" copies by default
  and writes "directly congruent" whenever it excludes reflections. Both
  usages were confirmed in the OCR, for example "edge-to-edge tilings in
  which only directly congruent copies of the prototile are allowed". The
  passage above does not restrict to direct congruence, so by the book's
  convention the asserted aperiodicity implicitly **includes reflections**.
  It is still an unproved assertion in the recovered text. Sugimoto
  2404.00534v5 observes that the displayed tiling uses no reflected pieces.
* **Later reproductions, none with a proof:**
  * Klee & Wagon, *Old and New Unsolved Problems in Plane Geometry and
    Number Theory* (MAA 1991), Problem 7 and Figure 7.8: "an aperiodic set
    consisting of two convex pentagons and a convex hexagon. The
    aperiodicity of this set of three convex tiles is enforced by shape
    alone. FIGURE 7.8 An aperiodic tiling due [to Ammann]"; also
    "... Penrose rhombs shown in Figure 7.7, followed by recomposition into
    a convex hexagon and two convex pentagons."
  * Croft, Falconer & Guy, *Unsolved Problems in Geometry* (1991), C18:
    "There is a set of three convex polygons that are aperiodic with no
    matching condition on the edges, but are two or even one such convex
    prototiles possible?"
  * Gardner, *Penrose Tiles to Trapdoor Ciphers* (1989), and the *Colossal
    Book*: "One set, consisting of two convex pentagons and a convex
    hexagon, forces nonperiodicity without any edge markings."
  * Glassner, *Andrew Glassner's Notebook* (1999), p. ~210: "The three
    Ammann tiles — two pentagons and one hexagon".
  * Sugimoto 1602.06372 and 2404.00534 (already audited).

  All of these are restatements. None of the recovered snippets contains a
  proof or a reflection/contact analysis.
* **Senechal, Baake–Grimm, Goodman-Strauss, Socolar.** Senechal's book was
  not found in the IA FTS index for these phrases. No proof of the convex
  Ammann set was located in arXiv material by Goodman-Strauss or Socolar
  (`au:` searches); the Socolar hits are physics papers. The 1992
  Ammann–Grünbaum–Shephard DCG paper concerns A2–A5 and remains
  inapplicable (prior audit).
* **2nd edition (Dover 2016).** The publisher and retail listings describe
  it as an "unabridged, corrected republication" of the 1987 edition, with
  a new preface and an Appendix (p. 653) of later references. The Appendix
  was not inspected, so it is unknown whether it updates the convex-set
  status. The arXiv papers citing [GS16] (e.g. 2303.10798) use the same
  theorem numbering as 1987.

**Status.** The 1987 recovered text asserts the three-polygon result.
Healey 2011 supplies a later published proof under its complete-edge
convention, as detailed in the correction below. The missing-proof conclusion
of the initial search and earlier source audit is superseded. The repository
has a separately reviewed generic-J strengthening for unrestricted contacts
and reflections.

## 2. Aperiodic sets of unmarked convex polygons with a full proof

Ammann's three-shape set has the Healey 2011 proof described below. Its stated
conventions must be distinguished from the unrestricted target. Other
located constructions have the following scope:

* Sugimoto 2404.00534v5: three convex types. Front and back are treated as
  distinct and reflections are forbidden. The paper says aperiodicity is
  not confirmed, and that reflected pieces yield periodic tilings (prior
  audit).
* Sugimoto 2307.08184v3: converts hat/Tile(1,1) tilings into non-periodic
  tilings by three pentagon types. The paper itself notes that each convex
  pentagon used is a convex pentagonal monotile, which tiles periodically.
  This gives non-periodic tilings, not an aperiodic set.
* Džuklevski 2507.20867: six convex tiles, but σ-morphic, not aperiodic
  (prior audit).
* Winkler 2106.08155 (math.GM): non-convex polyrhomb "snake/dog" pairs.
* Van Dongen 2110.08915 and 2111.03979: triangle+rhombus and
  single-triangle tilings forced by **substitution rules**, not by shape.
  The tiles themselves tile periodically.

The corrected benchmark is Ammann's three shapes with Healey's proof;
this bounded search did not locate a two-convex-shape solution. This does not
constitute a completeness or priority assertion.

## 3. Work from 2023 to 2026

* No arXiv paper from 2023 to 2026-10-11 constructs one or two convex
  aperiodic tiles. None proves that two (or three) cannot exist.
* Sugimoto: the newest items are still 2404.00534v5 (2025-01-15),
  2501.07090v2 (2026-01-29) and 2609.09603v1 (2026-09-09, concave). No
  newer Sugimoto item appears on arXiv.
* Zhu–Wang–Yan 2508.01404 is at v2 (2026-04-28), and no newer version
  exists.
* Smith–Myers–Kaplan–Goodman-Strauss 2303.10798 accept Rao's result as
  "eliminating any remaining possibility that a convex polygon could be an
  einstein". They say nothing about convex pairs.
* **Undecidability.**
  * Demaine–Langerman, 2409.11582 (SoCG 2025): tiling with **three simple
    polygons** is co-RE-complete, with or without reflections. The tiles
    (wheel, shuriken, staple) have notches and reflex vertices; the staple
    has reflex defect 2α. They are **not convex**.
  * Stade, 2506.11628: **two** polygonal prototiles, with rotations and
    translations, made to work with or without reflections. The polygons
    are non-convex (jigsaw-style).
  * Yang–Zhang, 2412.17382: 7 polyominoes under translation only.

  By the standard Wang argument, these results imply aperiodic sets of
  size 3 / 2 in their classes, but **not** in the convex class. No
  undecidability result for finite sets of **convex** polygons was found.
  An undecidability theorem in that class would imply that convex
  aperiodic sets exist, but it would not bound their size by 2.
* Hyperbolic-plane convex monotile results (2603.27827, 2610.05438) are
  outside the Euclidean target.

## 4. The "one translation implies periodic" statement in Tilings and Patterns

**Primary text, Section 3.7, Statement 3.7.1 (stitched OCR):**
"Let S be a finite set of prototiles and suppose that each of these
prototiles is a polygon. Suppose further that S admits an edge-to-edge
tiling T which possesses a translation as a symmetry. Then S admits a
periodic tiling. By a polygon we mean a topological disk bounded by a
finite number of straight-line segments ..."

The book calls it "Statement 3.7.1", as Exercise 3 refers to "Statement
3.7.1". The hypotheses are:

1. finitely many prototiles;
2. polygons (topological disks bounded by finitely many segments, so
   convexity is not required);
3. the given translation-invariant tiling is **edge-to-edge**.

**Exercises 3.7 (stitched OCR):** "1. Prove Statement 3.7.2. **2. Prove that
if a finite set S of prototiles admits a tiling T which possesses a
translation as a symmetry, then S admits a periodic tiling. *3. Let S and T
be as in Statement 3.7.1. Prove that any patch of T is also a patch of a
periodic tiling admitted by S."

So the general, non-edge-to-edge version is a **double-asterisk exercise**,
not a theorem. The book's meaning of "**" could not be recovered by OCR
search. Klee–Wagon (1991) indicates that the non-edge-to-edge case was open:

* Their Theorem 7.4: "If a finite set S of polygonal prototiles admits an
  edge-to-edge tiling that has a translational symmetry, then S also admits
  a periodic tiling."
* Their discussion of convex pentagons: "... some tiling T by an aperiodic
  convex pentagon does admit translative symmetries in one direction. (By
  Theorem 7.4, such a tiling could not be edge-to-edge.) We mention this
  possibility and the one in Problem 7.3 ..."

Secondary sources differ in how they restate it:

* Handbook of DCG, 3rd ed., ch. 3 (Harriss–Schattschneider–Senechal),
  "Main results" 1, and SMKG 2303.10798 §1 both keep the **edge-to-edge**
  hypothesis.
* SMKG's introduction ("a set of 'normal' tiles is weakly aperiodic iff
  strongly aperiodic [GS16, Thm 3.7.1]") and Greenfeld–Kolountzakis
  2305.14028 ("for d ≤ 2 the two notions coincide [GS87, Thm 3.7.1]") state
  it **more broadly than the primary text supports**.

**Consequence for the target.** For finite sets of convex polygons with
partial contacts, the primary theorem does **not** apply. A singly periodic
non-edge-to-edge tiling is not known (from this literature) to upgrade to a
doubly periodic one. The target definition already forbids every nonzero
translation, so the right obligations are:

* **Aperiodicity claim:** it must exclude singly periodic tilings
  directly. Excluding doubly periodic ones is not enough unless an
  upgrade lemma for the specific pair is proved.
* **Periodicity escape:** one nonzero translation suffices.

## 5. Results forcing periodicity

* **Rao, arXiv:1708.00274v1 (2017).** The abstract claims no more than the
  15 known pentagon families, "in particular ... no convex polygon which
  allows only non-periodic tilings". arXiv shows no journal reference.
  Sugimoto 2501.07090v2 still calls the classification not definitively
  established (prior record). Klaassen 2506.18473v3 explicitly assumes
  Rao. Status: computer-assisted and widely accepted by secondary sources
  (SMKG, Handbook ch. 3: "had not been verified at the time of writing").
  Its scope is monohedral, so it says nothing about mixed pairs.
* **Zhu–Wang–Yan 2508.01404v2.** A monohedral hexagon classification that
  covers non-edge-to-edge contacts and flips (prior records). There is no
  two-hexagon or hexagon–pentagon classification in it.
* **Sugimoto 1602.06372 and 1508.01864.** A convex polygon admitting an
  **edge-to-edge monohedral** tiling admits a periodic one.
* **Frettlöh–Glazyrin–Lángi 1911.12752** (normal non-edge-to-edge
  unit-area convex hexagon tilings with k irregular vertices) and
  **Yu–Wang–Yan 2405.04843** (degree-3 hexagon tilings) are monohedral or
  metric results. Neither is a mixed-pair periodicity theorem.
* No classification of tilings by two convex hexagons, or by a convex
  hexagon plus a convex pentagon, under arbitrary contacts was located.
* G–S Statement 3.7.1 gives "one translation ⇒ periodic" only for
  edge-to-edge tilings (§4).

## Novelty boundary (corrected)

Within the retained sources and queries, no two-unmarked-convex-polygon
construction satisfying the target, or unrestricted impossibility proof,
was located. The three-shape benchmark has Healey's published proof under
its conventions. The earlier claim that a repository proof would be the
first proved convex example is **retracted**. A two-shape construction would
address the size-two target; a two-shape impossibility theorem would not by
itself settle larger protosets. The undecidability sources located in this
search concern non-convex tiles and do not establish convex undecidability.

## Correction: established benchmarks supplied by the user (2026-10-11)

The earlier conclusion that no proof of Ammann's three convex tiles was
located is **superseded**. Two primary sources were opened directly.

* **V. O. Healey, "A Family of Recompositions of the Penrose Aperiodic
  Protoset and its Dynamic Properties", Rose-Hulman Undergraduate
  Mathematics Journal 12(2) (2011), pp. 91-113**
  (<https://scholar.rose-hulman.edu/rhumj/vol12/iss2/7/>; full text read
  from the Wayback Machine copy of the journal's archive PDF, because the
  live PDF returned a Cloudflare 403). Theorem 4.5 and Corollary 4.7: every
  tiling by Ammann's two pentagons and hexagon is mutually locally
  derivable with a Penrose rhomb tiling, so the protoset is aperiodic
  "without adjacency rules". The paper states this was "previously known but
  never proven in the literature". Hypotheses as written:
  - adjacent tiles must share a complete edge (p. 97), stated as a
    convention, not derived;
  - Q is "allowable": |AQ|, |BQ|, |CQ|, |RS| are pairwise distinct;
  - the edge and angle relations of Prop. 4.3 are treated as exhaustive
    (p. 100), with the vertex atlas deduced from them;
  - reflections are not discussed.
  The proof is a vertex-star-atlas argument: 8 stars from Penrose stars,
  6 at the added vertices, and 10 further locally legal stars excluded by
  hand (Claim 4.6).
* **R. Ammann, B. Grunbaum, G. C. Shephard, "Aperiodic Tiles", Discrete
  Comput. Geom. 8 (1992) 1-25** (GDZ scan PPN362609810_0008, pp. 1-2 read
  from page images). This gives rigorous proofs for Ammann sets A2-A5.
  Prototiles are congruent "directly or oppositely", so reflections are
  included. The method is the composition technique: (a) every tiling
  groups uniquely into supertile patches; (b) inherited markings give an
  equivalent matching condition for the supertiles. The convex
  recomposition is not one of these sets; Healey cites this paper.

Revised novelty boundary: an aperiodic set of three unmarked convex
polygons is **established** (Healey 2011, under the complete-edge
convention). Two convex tiles remain open within this boundary (no
construction or impossibility located). The repo's Ammann forcing lemma is a
verification and strengthening (no edge-to-edge convention, explicit
reflections, exact atlas, explicit genericity), not a discovery.
