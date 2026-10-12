# Search record: two-class convex decorations of other aperiodic sources (hat, spectre, …)

**Date:** 2026-10-11
**Completion status:** **Incomplete / abandoned.** The route was closed by root
decision: enlarging the decoration domain does not address the forcing
bottleneck. No search result was obtained and no claim is made.

## Question (as posed)

Take aperiodic source tilings (hat, spectre, then Ammann–Beenker and Penrose
kite/dart). Decorate each source tile with segments and erase the source edges.
Look for decorations whose faces are convex polygons with at least 5 corners
falling into exactly two congruence classes (mirror identified), and test each
such decoration for monohedral escape.

## What was computed

### 1. Exact hat patches — done and verified

Script: `research/searches/source-decoration-hat-patch.py`.

This is an independent exact re-implementation over \(\mathbb Q(\sqrt3)\) of
the H/T/P/F metatile substitution. It was written by reading Kaplan's hatviz
`hat.js`/`geometry.js` as data; that code was not executed.

* **Pitfall found.** The hatviz construction patch contains metatile placements
  that the supertile step later discards, and these overlap: two kites at
  level 0 are covered twice. Only expansions of genuine supertiles are valid
  patches.
* **Exact verification of the H-supertile expansions.**
  * Every hat decomposes into 8 grid kites.
  * No kite is covered twice.
  * All hats lie on one common kite grid.
  * Every grid hexagon is fully covered within the stated core radius.

| Level | Hats | Reflected hats | Gap-free core radius (hex sides) |
|---|---|---|---|
| 1 | 25 | 3 | 4.3 |
| 2 | 169 | 22 | 11.3 |
| 3 | 1156 | 147 | 27.1 |

Replay:

```
conda run --no-capture-output -n arisearch python3 research/searches/source-decoration-hat-patch.py 3 OUT.json
```

### 2. Hat decoration domain and encoding — built, search not finished

Scripts: `research/searches/source-decoration-hat-lattice.py`,
`research/searches/source-decoration-hat-search.py`.

**Domain.** A decoration is a set of primitive lattice segments with these
properties:

* endpoints in the hexPt lattice (kite vertices and kite-axis midpoints);
* no lattice point in the open segment;
* the segment lies in the closed reference hat;
* the segments are pairwise non-crossing.

The reference hat contains 24 lattice points (14 on its boundary) and
**154 candidate segments**. Reflected hats carry the mirrored decoration.
Faces are additionally required to have diameter below 7 hex sides.

**Encoding: z3 CEGAR.** All arithmetic is exact integer arithmetic.

* Static clauses:
  * local convexity at every core lattice point, which reduces to 1074 distinct
    clauses over the 154 segment variables;
  * no crossings inside a hat;
  * the decoration is non-empty.
* Lazy cuts, each valid for every decoration in the domain:
  * ray cuts bounding face diameter;
  * face cuts excluding a face with at most 4 corners or a non-convex face;
  * three-class cuts.

**Status when stopped.** The level-3 patch had 170 397 global segments. The
run had made about 100 iterations and added 100 face cuts, with no candidate
and no UNSAT result. It was killed at about 6 minutes.

**No result:** neither emptiness nor any candidate was established.

### 3. Spectre — not started

Shrx's `spectre.py` was downloaded as data and read but not executed. The
exact \(\mathbb Z[\zeta_{12}]\) form of the spectre outline was worked out:
edge directions in 30° units are [0,−2,1,3,0,2,5,7,4,6,6,8,−1,9]. No patch,
domain or search was built.

### 4. Ammann–Beenker and Penrose kite/dart — not started in this abandoned route.

Subsequent kite/dart work is a separate
[campaign](../certificates/penrose-kite-dart-campaign.json); this section is
not its current status.

## What this does and does not show

The repository retains the exact hat patch **producer** and an unfinished
encoding, not the original patch outputs or a completed search certificate.
This record proves nothing about two-class decorations of any source.
Downloaded files were reconnaissance inputs, formerly under
`/tmp/claude-1000/ammann-two-class/dl2/` and `/tmp/claude-1000/ammann-two-class/dl3/`;
discarded scratch outputs were under `/tmp/claude-1000/ammann-two-class/work/`
(`hat1..3.json`, `hatsearch.log`). These locations are historical, not restart
dependencies. Regenerate patches with the retained producer before relying
on new patch checks; no stable claim depends on those scratch files.

**Route closed by root decision.**
