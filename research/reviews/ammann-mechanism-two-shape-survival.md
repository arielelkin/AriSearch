# Which parts of the Ammann/Healey forcing mechanism survive with two convex shapes

Date: 2026-10-11. Root strategy analysis. It is not a final result.
Lemma S below is an **unresolved attempted reduction**, not a proved result.
The proposed design criteria below are heuristics, not necessary conditions
for all two-shape derivations. Computed conclusions apply only on their
stated domains.

## Benchmarks

* Healey, RHUMJ 12(2) (2011), Thm 4.5 / Cor 4.7: Ammann's three convex tiles
  (two pentagons, one hexagon) are aperiodic. Every tiling is mutually
  locally derivable (MLD) with a Penrose rhomb tiling. Hypotheses: a
  complete-edge convention, four distinct edge lengths, and exhaustive
  angle relations; reflections are not discussed.
* Ammann-Grunbaum-Shephard, DCG 8 (1992): composition technique (unique
  grouping into supertiles plus inherited matching), with reflections, for
  sets A2-A5.
* Repo verification/strengthening:
  [ammann-forcing-aperiodicity.md](../lemmas/ammann-forcing-aperiodicity.md)
  (no edge-to-edge convention; explicit reflections; exact atlas; genericity
  (G1)+(G2')). Two hostile reviews: local part VALID, reconstruction VALID,
  all repairs validated by the [fresh rereview](ammann-forcing-repair-rereview.md).

## The mechanism, layer by layer

| Layer | Role in the three-tile proof | Survives with two convex shapes? |
|---|---|---|
| S. Source aperiodicity | Penrose rhombs with arrows; unique composition proved on the source | **Yes, unchanged.** It is source-agnostic: nothing is asked of the convex tiles. |
| D. Local derivation (recomposition) | Interior points J, K, L; rhomb edges erased; faces are the tiles; gives existence and one MLD direction | **With exactly two final congruence classes.** Distinct source face orbits can in principle become congruent; the dimension count below is only a design heuristic. Lemma S is unresolved. |
| C. Length coding | Distinct lengths a, b, r, c replace arrows | **Yes**, as a method. A two-hexagon pair has 12 sides against Ammann's 16; the surviving pentagon/higher-polygon case has no established total-side cap. |
| G. Angle genericity | Angles are 36 deg combinations plus free chi, psi, kappa; no relation sums to 180 deg, so no T-junctions and a finite 360 deg list | **Yes, when the required exact nonresonance conditions hold.** A free parameter can help obtain genericity; neither its necessity nor its loss under every collapse is proved. |
| A. Atlas closure | Local pruning to the legal stars (Healey Claim 4.6; repo 162 to 14) | **Yes**, as a method (exact, local). |
| R. Inverse derivation | Cut tiles along fixed segments to recover arrowed rhombs, so MLD holds and aperiodicity is inherited | **Yes**, as a method, if D yields an inverse. |
| H. Handedness | Single-handed atlas makes reflections harmless | **Yes**, as a property to check. |
| AGS self-composition | Prototiles group into similar supertiles | **Excluded only in the stated cases.** Healey notes Ammann tilings lack unique composition, so that construction inherits aperiodicity via MLD. For two convex tiles the repo's [dissection Euler lemma](../lemmas/convex-substitution-dissection-euler.md) excludes homothetic self-dissection for (6,6) and (6,n>=7), and lambda=phi for (5,5),(5,6) (internal, unreviewed). |
| AGS shape-for-marking via notches (A2-style) | Notches and tabs carry markings | **No.** Convexity forbids notches; markings must be carried only by lengths and angles (layers C, G). |

## Why the three-to-two collapse fails, and what it teaches

Ammann's derivation has **three face orbits**: the hexagon around each thin
rhomb, and two pentagons from each thick rhomb. Making two orbits congruent
imposes congruence equations: up to 2n-3 = 7 real conditions for pentagons,
modulo coincidences. The decoration has only the two real parameters of J.
This motivates a heuristic expectation of isolated solutions, but independence
of the congruence equations has not been established. The exact search
found exactly one admissible point, the circumcentre of BCD
([record](../searches/ammann-two-class-search.md)). There every angle lies in
the 36 deg lattice, so layer G is lost, and the hexagon becomes centrally
symmetric and tiles alone. (Dimension count: heuristic. The single-point
outcome is computed exactly on the stated domain.)

**Proposed design criterion (C1), heuristic:** seek a derivation with
**exactly two face orbits** before imposing congruence equations. This may
avoid the parameter loss observed in the recorded Ammann collapse. It is
not a necessary condition: congruence constraints can be dependent, and
an isolated exact parameter can still satisfy nonresonance. Two orbits
alone also do not guarantee a free parameter or genericity.

**Checkpoint scope correction (2026-10-12):** C1 and the layer-by-layer
comments do not establish a necessary classification. Independent hostile
review of the collapse classification and any replacement for Lemma S
remains outstanding.

## Proposed Lemma S (one face per rhomb forces hexagons): unresolved

**Setting.** Let P be a Penrose rhomb tiling with thin and thick rhomb
densities t and T, where t/T is irrational. A *per-rhomb decoration* puts,
inside every rhomb of each type, the same configuration up to the rhomb's
isometry:

* i_t (resp. i_T) interior points;
* e_t (resp. e_T) segments joining interior points and rhomb vertices,
  disjoint from rhomb-edge interiors.

All rhomb edges are erased. Assume:

* (i) every rhomb vertex is an endpoint of at least three segments;
* (ii) all faces of the resulting plane graph G are strictly convex
  polygons;
* (iii) the face density is exactly t + T (one face per rhomb on average).

**Unestablished claim.** Every face of G has 4 or 6 sides, and if all faces have 6 sides
then G is trivalent. Hence a two-class convex recomposition of this kind is
either a quadrilateral pair, which tiles periodically, or a pair of convex
hexagons. The pentagon-hexagon type of Ammann's set cannot arise.

**Attempted proof (incomplete).**

1. **Vertices and degrees.** By (ii), no vertex of G has degree 2: two
   strictly convex corners cannot sum to 360 deg. By (i), every rhomb vertex
   has degree at least 3, and every interior point has degree at least 3
   because it is a corner of at least three strictly convex faces.
2. **Counting relations.** Take densities over a van Hove sequence. Penrose
   rhomb vertices have density t + T (Euler for the rhomb tiling, whose
   faces have density t + T and edges 2(t + T)). Hence
   V = (1 + i_t) t + (1 + i_T) T and E = e_t t + e_T T. Euler's formula in
   the van Hove limit gives V - E + F = 0 in density. With (iii):
   F = E - V = (e_t - 1 - i_t) t + (e_T - 1 - i_T) T = t + T.
   Since t/T is irrational and all coefficients are rational,
   e_t = 2 + i_t and e_T = 2 + i_T.
3. **Side count.** Each segment borders exactly two faces, so the total side
   count is 2E = (4 + 2 i_t) t + (4 + 2 i_T) T. Let face classes with n_k
   sides have densities a_k t + b_k T, where sum_k a_k = sum_k b_k = 1 by
   (iii). Matching coefficients again gives sum_k a_k n_k = 4 + 2 i_t and
   sum_k b_k n_k = 4 + 2 i_T.
4. **Hexagons need trivalence.** The standard identity
   sum_f (6 - n_f) = 2 sum_v (d_v - 3) holds in density. If all faces are
   hexagons, every vertex therefore has degree 3.
5. **Restricting the side counts.** If every face has n in {5, 6}, the
   weighted averages force 4 + 2i = 5 or 6. Since i is an integer, i = 1
   and every face is a hexagon. Faces with n >= 7 combined with n <= 5 are
   excluded for two convex classes by the reviewed
   [side-count obstructions](../lemmas/side-count-and-monohedral-obstructions.md):
   a hexagon or heptagon pair is not aperiodic, and a protoset member must
   have at most 6 sides. Quadrilaterals tile alone.

**Checkpoint correction (2026-10-12).** Step 3 does not justify a
nonnegative rational decomposition of each face-class density as a_k t+b_k T.
Without that property, matching coefficients and bounding both weighted
averages in Step 5 is unsupported. Step 5 also does not exclude general
pentagon/higher-polygon pairs by the cited side-count theorem. The statement
about every face having 4 or 6 sides is therefore not established by this
argument. Independent hostile review remains outstanding; no current route
may rely on Lemma S as proved. Ammann's own derivation has density t+2T and
is outside hypothesis (iii) in any event.

**Conditional application only.** If a separate valid argument puts a
recomposition in the two-hexagon class, the reviewed
[SFT reduction](../lemmas/two-hexagon-global-sft-encoding.md) applies. The
[census](../lemmas/two-hexagon-global-census.md) checks all 316 stored covering
rank≤3 types; higher ranks 4..10 remain open. It is not a complete exclusion
of the one-face-per-rhomb sub-route.

## What survives, in one sentence

Everything except the shape economy survives. The source's unique
composition, length coding, angle-genericity edge forcing, atlas pruning,
inverse derivation and handedness are all shape-count independent. What must
be replaced is the way Ammann distributes the Penrose information over three
face orbits. Criterion C1 proposes seeking two face orbits with a surviving free
parameter; neither is established as necessary. Neither final shape may
tile alone. The retained self-dissection obstructions exclude the stated
side-count and inflation-factor cases, not every convex self-composition.

## Concrete next gates (proposed, not run)

1. **Two-orbit derivations with face density other than t + T** (pentagon
   pairs need degree >= 4 vertices at positive density). First gate:
   enumerate per-rhomb Penrose decorations with exactly two face orbits and
   at least one free parameter, before any congruence equation is imposed.
   Kill by monohedral escape. This is a proposed enlargement motivated
   by C1, not a proved requirement or authorization to resume the search.
2. **Two-hexagon census coverage.** The stored rank≤3 covering census and
   repaired-reduction review are complete. Continue from all low-rank parents
   into rank4, measuring inherited escapes first. Lemma S does not currently
   justify applying this route to every one-face-per-rhomb decoration.
3. **Genericity with two shapes.** For any candidate, check exactly that no
   angle relation sums to 180 deg (layer G). An isolated parameter also needs an exact
   nonresonance check. If nonresonance fails, analyze the resulting
   T-junctions and extra stars explicitly.
