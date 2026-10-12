# Hostile review: Ammann forcing — rhomb reconstruction, Penrose composition, existence

**Status update (2026-10-12):** this is the original review and defect record.
The repairs are complete and have a [VALID fresh rereview](ammann-forcing-repair-rereview.md).
Read the [current lemma](../lemmas/ammann-forcing-aperiodicity.md) for its G* hypotheses.


**Date:** 2026-10-11
**Reviewer:** independent hostile reviewer (did not develop the work).
**Artifacts reviewed:**
[ammann-forcing-aperiodicity.md](../lemmas/ammann-forcing-aperiodicity.md) (Lemmas 5, 6 and Theorem items 1, 3),
[ammann-forcing-penrose-composition.py](../searches/ammann-forcing-penrose-composition.py),
[ammann-forcing-penrose-composition.json](../certificates/ammann-forcing-penrose-composition.json).
Tile data come from [ammann-two-class-reconstruction.md](../lemmas/ammann-two-class-reconstruction.md).

**Scope.** As instructed, Lemmas 3 and 4 are taken as given: every tiling is
edge-to-edge, and every vertex star is one of the 14 listed stars, all of one
handedness. Genericity (G1)/(G2) is also assumed, and it is reviewed separately.
"No counterexample found" is not treated as validity. Each verdict below rests
on a proof check plus an exact re-implementation.

## Verdicts

| claim | verdict |
|---|---|
| R1: regrouping into a legal marked rhomb tiling; symmetries carried over | **VALID** (conditional on Lemmas 3–4, as scoped) |
| R2: unique translation-equivariant composition; no nonzero translation | **VALID**. The closure argument as written is incomplete (D1); repaired here by exact check. |
| R2: the arrow set is the Penrose P3 rule set | **VALID as evidence** (D3). Lemma 6 does not need it. |
| R3: decoration of any legal rhomb tiling gives an Ammann tiling | **VALID**. Existence of a legal rhomb tiling of the whole plane is not proved in the files (D2); repaired here. |

No invalidating defect was found.

## Independent checkers (no author code imported; exact arithmetic only)

| checker | what it does | result |
|---|---|---|
| [verify_ammann_forcing_reconstruction_rhombs.py](verify_ammann_forcing_reconstruction_rhombs.py) | Derives the rhomb stars from scratch as exact covers of the 10 sectors (not as corner sequences). Prunes geometrically. Builds radius-1 patches from rhomb sets with an extra interior-overlap test. Finds parents by **brute force** over all 20 big marked rhombs and all their deflation children, not by the authors' inverse formulas. Checks closure of composition and of deflation exactly, and checks genuine P3 patches. | all pass (about 25 s) |
| [verify_ammann_forcing_reconstruction_pieces.py](verify_ammann_forcing_reconstruction_pieces.py) | Works in Q(ω) with exact division. At 5 values of J, assembles the 6 J/K/L stars by gluing corners along full edges. Checks piece congruences, a-ends and areas. Checks all 16 legal edge gluings for the decoration direction. | all pass |
| [verify_ammann_forcing_reconstruction_pentagrid.py](verify_ammann_forcing_reconstruction_pentagrid.py) | Builds de Bruijn pentagrid rhomb tilings exactly (floors decided in Q(√5)). Uses exact 2-SAT to decide whether the lemma's arrows can be placed consistently. | Σγ=0: markable. Σγ=1/2 and Σγ=1/5: **not** markable. N=3,5,7, up to 2250 rhombs. |

Replay: `conda run --no-capture-output -n arisearch python3 research/reviews/verify_ammann_forcing_reconstruction_<rhombs|pieces|pentagrid>.py`.

I also replayed the authors' script. It gives a certificate identical to the committed JSON (85 patches, 564 cases, 0 failures).

## R1 — regrouping (Lemma 5)

**Proof check.** Each of the 6 J/K/L stars contains exactly one triangle-apex corner of each relevant type:

* J-stars: χ = P1-J′; ψ = P2-J2 or H6-J″.
* K-stars: χ = P1-J′ or H6-J′.
* L-stars: ψ = P2-J2 or H6-J″.

The 8 Penrose-type stars contain no χ or ψ corner. So every X- or Y-triangle is assigned exactly once. Every H6 quad is in one thin group. Every P1/P2 quad is in one thick group, because P1-K and P2-K occur only together, sharing the c-edge (Lemma 4(ii)). Hence the pieces partition into groups.

**Exact assembly check.** At J ∈ {(1/2,4/5), (9/20,3/4), (11/20,17/20), (3/7,5/6), (5/11,7/9)}, walking around each star with full-edge gluing gives these results:

* Each star closes up.
* The χ-tile's triangle lands exactly on BCJ with its a-end at C. In a K-star it lands on HEK with its a-end at E.
* The ψ-tile's triangle lands on CDJ with its a-end at C. In an L-star it lands on FGL with its a-end at F.
* In K- and L-stars the P2 lands exactly in standard position (quad KLGH).
* J, K and L are strictly inside their rhombs, and every piece is strictly convex.
* Exact area sums hold for both rhombs and all three tiles.

Lemma 1 says every edge vector is a fixed unit times one of four affine vectors. So the gluing rotations do not depend on J, and every placed vertex is complex-affine in J. Agreement at these sample points therefore extends to all of D.

**Arrows.** The rhombs are genuine and edge-to-edge, and the arrow reading is consistent from both sides of every edge:

* Every rhomb edge is a chord of exactly one tile. That tile's quad is on one side and its triangle on the other.
* The a-end reading reproduces the stated arrows: A→B, C→B, A→D, C→D, E→F, E→H, F→G, H→G.
* Both sides read the same triangle, so the marks agree.

**Canonicity.** The grouping is defined from tile labels and stars alone. So it commutes with every isometry, and any symmetry of the Ammann tiling (in particular any translation) is a symmetry of the rhomb tiling. **VALID.**

## R2 — composition (Lemma 6)

**Vertex stars.** Re-derived from scratch:

* 14 raw star types (up to rotation; reflections are counted separately, though here they coincide).
* 116 placed stars at the origin.
* Pruning removes 6 types: EEEACAC, EEACACAC, EACEACAC, EACACACAC, FHCACA and (AC)^5.
* 8 survive: E⁵, E⁴AC, EEACEAC, EAFHC, FBH, G⁵, GGGD, GDD.

These 8 are **exactly** the complete vertex stars seen in a genuine P3 patch (2896 complete vertices in a sun deflated 7 times). Completeness of the raw list follows from exhaustive exact-cover enumeration. Pruning is sound because the edge condition is necessary.

**85 patches.** Reproduced: 1, 1, 2, 50, 7, 11, 4, 9. All 85 also have pairwise interior-disjoint rhombs, an exact test the authors do not use. Completeness: every star of a legal tiling is among the 8, the patch is the star at 0 plus the full stars at every vertex of those rhombs, and the enumeration places every star in all 10 rotations at each neighbour, subject only to angular consistency. So the list is a superset of the real patches. Fixing the origin star at rotation 0 is harmless, because the problem is equivariant under rotations by 36°.

**Uniqueness and locality.** I searched for parents independently, by brute force over big marked rhombs whose Robinson deflation contains t. This gives 2 candidates for a red t and 3 for a blue t, and in all 564 cases exactly **one** is valid. I also checked, independently, that all children of each candidate big rhomb share a point that is a vertex of t. So validity in the tiling equals validity in the patch.

From this the partition argument goes through:

* If H is valid then so is its twin H\*, so siblings get the same parent.
* Two valid parents with overlapping interiors would share a child, which uniqueness forbids.
* So the valid φ-rhombs tile the plane.
* The rule is defined geometrically, so C(T+x) = C(T)+x.

Existence of a parent is part of the same check (≥1 valid in every patch). It is not presupposed.

**Closure (C(T) legal).** Proved for every big rhomb R and every child h of R whose twin lies outside R (80 cases). Each candidate parent R′ of that twin either overlaps R in its interior (40 candidates; excluded, since valid parents are disjoint) or shares with R the **whole** edge carrying the base of h, with the same type and direction (160 candidates, 0 defects). Every edge of R carries such a base. So C(T) is edge-to-edge and legal at scale φ, and C(T)/φ is legal again.

**No translations.** Suppose T+x = T. Then C^k(T)+x = C^k(T), because C^k(T) is defined from T alone and commutes with translations. The tiles of C^k(T) have inradius φ^k·r₀. Once that exceeds |x|, Π and Π+x overlap in interior, so Π = Π+x, a contradiction. This also covers translation symmetry mapping supertiles to supertiles, since C^k is a function of T. The argument is correct.

**Is it Penrose's rule set?** Two checks were attempted:

* *Primary-source figure comparison:* unsuccessful. Wikipedia describes curve/bump rules, the AMS column returned HTTP 403, and the arrows in Gähler's paper are in figures only. No textual statement of the single/double-arrow convention was obtained.
* *Computational identification instead:*
  * Robinson (Preshing) P3 patches obey the marking (0 conflicts on 5905 shared edges).
  * The 8 surviving stars are exactly the P3 stars.
  * Pentagrid tilings with Σγ = 0 are markable.
  * Generalized (non-Penrose) pentagrid tilings with Σγ = 1/2 or 1/5 are **not** markable.

So the rule set is strong enough to reject generalized Penrose tilings, and it admits the genuine ones. It is not a weaker set. Lemma 6 does not depend on this identification anyway.

**Periodic counterexample attempt.** None is possible if Lemma 6 is right, and the proof checks out. The direct attempt was the generalized pentagrid tilings, which fail the marking at finite size.

## R3 — existence (decoration direction)

All 16 gluings across marked edges were checked: (rhomb kind × marked edge) × (rhomb kind × marked edge), with equal type and direction and interiors on opposite sides. In every case:

* Exactly one side carries a quad. An X edge has its quad on the left of the arrow and a Y edge on the right, in both rhombs.
* The triangle supplied by **either** possible neighbour (thin or thick) is exactly the triangle of H6, P1 or P2 on that edge: J′, J″, J′ or J2.

Each triangle belongs to exactly one tile (the quad across its base). So the pieces of any legal rhomb tiling regroup into a tiling by directly congruent copies of H6, P1 and P2, and it covers the plane because the rhombs do. **VALID**, given that a legal rhomb tiling of the plane exists (D2).

## Defects

* **D1 (minor; proof gap, repaired).** In Lemma 6 ("Edge-to-edge with matching marks"), the sentence "Twin children share their B and C labels. So the parent across any edge e has e as a full edge…" skips a case analysis. The outside twin can a priori be a child of its parent in another role. An example is blue(Q,R,B), whose base lies on the parent's *diagonal*. Such roles must be excluded, using disjointness of valid parents. The statement is true, as shown by the closure check above (40 overlapping roles excluded, 0 defects). **Repair:** add this role analysis, or cite the closure check.
* **D2 (minor; missing step, repaired).** Theorem item 1 ("admits tilings") needs a legal marked rhomb tiling of the **whole plane**. Lemma 5's existence clause is conditional on one. The files never prove that one exists, and Lemma 6 claims to be citation-free. **Repair**, either of:
  * cite Penrose/de Bruijn together with the identification; or
  * use the self-contained route checked here. Deflation σ maps legal tilings and patches to legal ones (exact local check over every legal edge-adjacency of two big rhombs, 1360 leg checks, 0 defects). Hence σⁿ of one rhomb gives legal patches of unbounded inradius, and compactness (finite local complexity) gives a legal plane tiling.
* **D3 (minor; overclaim).** "The 8-star count and the deflation check show that it is that marking" is not a valid inference:
  * an equal star count does not show the rule sets are identical;
  * the author's deflation sanity check tests parent recovery only, never mark consistency.

  The identification is supported by the Robinson and pentagrid checks above, as computational evidence on finite patches. It is not needed for the theorem. **Repair:** reword the sentence, or cite these checks.
* **D4 (cosmetic).** Lemma 5's existence direction does not state why every legal edge has a quad on exactly one side. The reason is the orientation argument: X edges have their quad on the left, Y edges on the right. This should be stated.

## Remaining uncertainty

* Everything rests on Lemmas 3–4 (edge-to-edge, 14 stars, single handedness) and on genericity of J. All are outside this review.
* Pieces were checked at 5 values of J. Extending to all of D uses Lemma 1 (J-independent edge rotations), which I did not re-verify.
* The P3 identification is computational evidence on finite patches, but it is logically unnecessary.
* The compactness step in the D2 repair is standard and was not formalised.
