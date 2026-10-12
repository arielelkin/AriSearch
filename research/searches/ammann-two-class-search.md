# Search record: collapsing Ammann's three convex tiles to two

**Date:** 2026-10-11 **Completion status:** complete over the stated finite
domains (no timeouts). **Outcome:** there is exactly one two-class point, and it
is killed. The bottom line is **Falsified** for every candidate in the domain.

## Question

Ammann's recomposition of Penrose rhombs gives two convex pentagons \(P_1,P_2\)
and one convex hexagon \(H_6\). The question has three parts:

1. Reconstruct the recomposition exactly.
2. Find every choice of the free point \(J\) for which \(\{P_1,P_2,H_6\}\) has
   at most 2 congruence classes (mirror images identified).
3. Search a bounded family of other decorations of the marked Penrose rhombs
   for decorations whose faces form at most 2 classes of convex polygons.

Every two-class candidate must then pass the monohedral-escape test.

## Part 1: exact reconstruction

Formulas and proofs are in `research/lemmas/ammann-two-class-reconstruction.md`.
Source: Sugimoto, arXiv:1602.06372v2, Figure 4. The figure was downloaded to
scratch and viewed as untrusted data only; its arrows are \(A\to B\), \(C\to B\),
\(E\to F\), \(E\to H\).

* **Encoding.** The field is \(K=\mathbb Q(\omega)\) with \(\omega=e^{i\pi/5}\),
  and \(J=s+t\omega\). Gluing forces \(K=\omega^2+\omega^6(J-1)\) and
  \(L=1+\omega^7(J-1-\omega)\); there is no branch freedom inside the rhombs.
  The tiles are
  \(H_6=[0,J',1,J,\omega,J'']\), \(P_1=[0,J',1,L,K]\),
  \(P_2=[K,L,1+\omega^2,J_2,\omega^2]\).
* **Independent check.** `ammann-two-class-reconstruct.py` builds an exact
  Robinson-deflation patch. It tries all 4 anchorings of the decoration to the
  arrow labels, traces faces of the decorated graph after erasing rhomb edges,
  and checks that the face areas sum exactly to the patch area. It then
  classifies interior faces exactly. Only the figure's anchoring gives
  3 classes. Those classes equal \(H_6,P_1,P_2\) directly, with no mirrors and
  all faces strictly convex. This holds for 3 rational choices of \(J\) on the
  4-fold patch (230 faces) and the 6-fold patch (1770 faces).
* **Admissible region.** Computationally, it is \(0<s,t<1\) and
  \(|J|^2>s+t\), i.e. \(J\) is outside the circumcircle of \(ABD\). This is
  sampling evidence. All decisions below are exact at the points concerned.

## Part 2: collapse of Ammann's tiles (`ammann-two-class-collapse.py`)

**Domain.** All \(J\in\mathbb C\) (equations), then filtered exactly by the
closed admissible region. The cases are:

* (a) \(P_1\sim P_2\);
* (b) \(H_6\) minus one straight vertex \(m\) (6 choices) is congruent to
  \(P_1\) or \(P_2\);
* each case for all 5 cyclic shifts, direct or mirror.

**Encoding.** For direct congruence the equations are holomorphic polynomials
in \(J\) over \(K\); we take their gcd and roots in QQbar, then check
unimodularity exactly. For mirror congruence we use Groebner bases over
\(K[s,t]\), closed under complex conjugation.

**Result: Proved by exact computation.** The only point in the region is
\(s=t=(5+\sqrt5)/10\), where \(J\) is the circumcentre of \(BCD\) and
\(P_1\cong P_2\) directly.

**Case (c).** Quadrilateral degenerations (a straight angle in \(P_1\) or
\(P_2\), or two in \(H_6\)) are discarded without solving, since every
quadrilateral tiles periodically.

**Kill (exact).** At that point \(H_6\) is equilateral with
\(e_i=-e_{i+3}\) and angles \(72,144,144,72,144,144\). It tiles by
translations, so the pair is **not aperiodic**.

Certificate: `research/certificates/ammann-two-class-collapse.json`.

## Part 3: generalized decorations

### Domain, stated exactly

Each arrow-marked rhomb (vertex labels 0..3 fixed by the marking, as in
Part 1) carries a plane graph with:

* at most two interior nodes \(P,Q\);
* edges chosen from \(P\!-\!i\), \(Q\!-\!i\), \(P\!-\!Q\) and the diagonals
  \(0\!-\!2\), \(1\!-\!3\);
* every interior node of degree \(\ge3\);
* every inner face a simple cycle.

Planar embeddings are enumerated exhaustively: Euler genus 0 with \(0123\) as
the outer face, and \(P\leftrightarrow Q\) relabeling identified. This gives
**98 abstract types per rhomb** (3 with no point, 9 with one, 86 with two).
That is a superset of the geometrically realizable types.

Placement uses orientation-preserving maps of the marked frame. All labelings
are enumerated, so this covers every arrow-consistent placement. The only
remaining freedom is global chirality, which is reduced by mirror symmetry.
The interior points are free parameters \(z_j\in\mathbb C\), up to 4 complex
in total. This gives **9604 (thin, thick) pairs**.

The Robinson half-rhomb version is contained in this domain when each half
carries at most one interior point and the triangles pair into rhombs (P3).
Kite/dart (P2-paired) triangle decorations are **not** covered.

### Stages

1. **Combinatorial kill** (`ammann-two-class-pairs.py`, exact \(\mathbb Z[\omega]\)
   arithmetic, 6-fold patch with 1140 rhombs). Pieces are glued across rhomb
   edges, and only tiles strictly inside the patch are used. Those are genuine
   tiles of every Penrose tiling, so each kill below is valid for all
   parameters.
   * Slit: 1127 pairs.
   * Pinched tile: 418 pairs.
   * Tile not simply connected: 468 pairs.
   * Tile with \(\le4\) corners after deleting identically straight vertices:
     7578 pairs. Such a tile is a triangle or quadrilateral, which tiles alone.
   * Remaining: 13 pairs, 4 of them with no bounded tile in the patch.
2. **Sector test** (`ammann-two-class-sector.py`, exact in units of 36°). At an
   interior vertex, segment-free full corners totalling \(\ge180°\) inside one
   sector force a reflex corner. This kills 4 pairs. The pair with both
   rhombs undecorated has no tiles at all (the face is the whole plane).
   * The 8 survivors are 4 mirror twins:
     (thin 4, thick 27) = Ammann's graph with free \(J,K,L\) and its twin (2,15);
     (27,3)/(15,1); (76,1)/(76,3); (76,27)/(76,15).
   * Their generic class lists (6, 5, 3 and 5 classes) are identical on the
     6- and 7-fold patches.
   * Twinning was checked numerically: the tile shapes correspond under the
     mirror parameter map.
3. **Pairwise congruence ideals** (`ammann-two-class-survivor-collapse.py`).
   For every class pair, every straight-vertex deletion set leaving at least 5
   corners, all shifts and both orientations, we form the ideal over \(K[s,t,u]\).
   It contains:
   * edge proportionality and its complex conjugate;
   * unimodularity;
   * straightness of each deleted vertex;
   * \(u\,|e_0|^2|f_k|^2=1\), since edges cannot vanish when interior points
     are strictly interior.

   Non-unit ideals are kept as options.
4. **Group search** (`ammann-two-class-group-search.py`). For every partition
   of the classes into at most 2 blocks, we fix a representative, a target
   corner count and a deletion set for each block, and run a depth-first
   search over member options. The ideals are summed, including across the two
   blocks, and pruned when they reach (1). The search used 1659, 2116, 558,
   533, 22, 22, 101 and 55 Groebner checks.
   * Every complete non-unit combination is **zero-dimensional**; there are
     0 positive-dimensional ones.
   * Each real point was tested exactly: actual class count at the point
     (straight vertices removed, mirrors identified) and weak convexity of
     every tile.

### Result (`research/certificates/ammann-two-class-generalized.json`)

The only convex two-class points in the whole domain are:

* Ammann's circumcentre point from Part 2, in pair (4,27): thin
  \(P=J=(\tfrac{5+\sqrt5}{10},\tfrac{5+\sqrt5}{10})\), with thick \(P,Q\) equal
  to \(K,L\) from the closed formulas;
* its mirror twin in pair (2,15).

Both are killed by the centrally symmetric hexagon.

The other points found are not candidates:

* (27,3)/(15,1): 2 classes, but the tiles are not convex and the parameters lie
  outside the rhombs.
* (76,1)/(76,3): 3 classes and non-convex; the point sits on a rhomb vertex.
* (76,27)/(76,15): no combination survives.

### Monohedral and periodic-torus tests

The single candidate dies at the first test: its hexagon tiles by itself
periodically. The unintended-vertex / torus search was therefore not needed.

## Dimension count

Part 2 has 2 real parameters. Pentagon congruence costs 7 real conditions, so
no collapse is expected; the isolated solution comes from the mirror symmetry
\(b=r\) on the diagonal \(AC\).

In Part 3 the Ammann survivor has 6 real parameters. The 3-class Ammann family
is a 2-dimensional subfamily of it, cut out by making the thin and thick
triangles coincide. The 2-class locus is a single point.

## What this proves and what it does not

**Proved, by exact computation with the numeric steps listed below:**

* Ammann's recomposition, as reconstructed, has no two-class specialization
  that escapes periodicity.
* Within the 98×98 decoration domain, every two-class convex specialization is
  Ammann's point or its mirror, and is periodic-killed.

**Numeric steps, all reconnaissance-grade and documented in the scripts:**

* angle ordering in the face trace of Part 1, guarded by the exact area
  identity;
* the sign of the dot product at vertices whose cross product vanishes
  *identically*, used to call them straight vs spike;
* the redundancy of the admissible-region inequalities.

**Conservative conventions.** Class lists come from finite patches, so they
are lower bounds. Necessary congruence constraints from retained interior
faces cannot exclude a genuine global two-class collapse, but finite class
counts alone do not establish a global two-class construction. Kills
use genuine interior tiles.

**Not covered:**

* more than 2 interior points per rhomb;
* points on rhomb edges, or segments ending at edge interiors;
* decorations that depend on neighbours, or anything beyond the rhomb marking;
* kite/dart substrates and other aperiodic substrates.

Aperiodicity of the generic three-tile set under reflections and arbitrary
contacts is now separately [adversarially reviewed](../lemmas/ammann-forcing-aperiodicity.md)
on its stated G* domain. That verification does not independently audit the
exhaustive two-class collapse search.

## Replay

The old agent-specific scratch directory is not a retained input. Set
`W=/tmp/arisearch-ammann-replay`, create it with
`conda run --no-capture-output -n arisearch mkdir -p "$W"`, and set
`C="conda run --no-capture-output -n arisearch python3"`. The commands below
regenerate intermediates in order; the first two and the final summary command
write their explicit output paths, so use temporary output to preserve the
retained certificates.

```
$C research/searches/ammann-two-class-reconstruct.py research/certificates/ammann-two-class-reconstruction.json   # ~10 min
$C research/searches/ammann-two-class-collapse.py research/certificates/ammann-two-class-collapse.json             # ~10 s
$C research/searches/ammann-two-class-decorations.py $W/types.json
$C research/searches/ammann-two-class-patchdata.py 6 $W/patch6.json
$C research/searches/ammann-two-class-patchdata.py 7 $W/patch7.json
$C research/searches/ammann-two-class-pairs.py $W/types.json $W/patch6.json $W/pairs6.json 6   # ~25 min
$C research/searches/ammann-two-class-sector.py $W/types.json $W/pairs6.json $W/patch7.json $W/survivors.json
for k in 0 1 2 3 4 5 6 7; do $C research/searches/ammann-two-class-survivor-collapse.py $W/types.json $W/patch7.json $W/pw$k.json $k; done
for k in 0 1 2 3 4 5 6 7; do $C research/searches/ammann-two-class-group-search.py $W/types.json $W/patch7.json $W/pw$k.json $W/gs$k.json; done
$C research/searches/ammann-two-class-summarize.py $W research/certificates/ammann-two-class-generalized.json
```
