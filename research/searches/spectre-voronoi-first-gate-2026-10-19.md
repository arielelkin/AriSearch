# Spectre corner-mean Voronoi first gate

**Status:** exact restricted exclusion; [independent Sol hostile review](../reviews/spectre-voronoi-first-gate-sol-review-2026-10-19.md) passed after the regularity wording below was clarified.
The fixed site rule below produces cells with 5, 6 and 7 sides in a genuine
Spectre substitution source. Thus this rule does not produce only two
congruence classes. Other site rules and the unrestricted target remain open.

## Primary source and source shape

Smith, Myers, Kaplan and Goodman-Strauss, *A chiral aperiodic monotile*,
Combinatorial Theory 4(2), 2024; arXiv:2305.17743v2:
https://arxiv.org/html/2305.17743v2 . Relevant material: Lemma 2.1,
Theorem 2.2, Figure 5.3, and Appendix A.

Author resource: https://cs.uwaterloo.ca/~csk/spectre/ ; implementation:
https://cs.uwaterloo.ca/~csk/spectre/spectre.js . Retrieved 2026-10-19 and
retained verbatim as `research/sources/spectre-author-2026-10-19.js`, SHA256
`d4d7758f268e2e5f3f56deb771f6f783e519f5351b46f8e6e05c0f629d2f6df1`.
The producer checks that digest. This source is read as mathematical data,
not executed. The producer transcribes `buildSpectreBase`'s polygon, Mystic
placement, and `buildSupertiles`'s eight-placement chain, nine label rules,
and key-point update. Decimal coordinates become their exact
Q(sqrt(3)) values; trigonometry becomes exact multiples of 30 or 60 degrees.

Fix a sufficiently small regular smooth centrally symmetric nonstraight
edge path as in Lemma 2.1, chosen so that the resulting Spectre X is a
topological disk and its 13 nonstraight corner points are exactly the
original skeleton corners. This X is not the unmodified polygon Tile(1,1).
The lemma states that every homochiral skeleton
tiling `{g Tile(1,1)}` yields `{g X}` with exactly the same placements.
The conclusion below applies to this fixed X, and equally to any such X
retaining that corner template and the site transported from it. It needs no
claim that the polygon skeleton is aperiodic when reflections are allowed.
The website's default straight rendering is a skeleton representation;
its decimal curved-rendering controls are not used as a certified source shape.

## Fixed equivariant site

Let v[0],...,v[13] be the exact fourteen template points in the producer,
including the midpoint of the long straight skeleton side. Define

`c = (1/14) sum(v[k], k=0,...,13)`.

For an unmarked copy gX, put its site at gc. This is one fixed rule, including
under reflections. It is independent of substitution labels and hierarchy.
The Spectre template has no nonidentity isometric stabilizer: the cyclic
sequence of its nonstraight corner angles and their positions already
distinguishes its corners (the unique long skeleton side can equivalently
be recovered from the smooth-corner template). Consequently the transported
site is well-defined. No colors or extra placement rules are output.

The producer checks exactly that c is inside the skeleton, its distance
from every skeleton edge exceeds 1/4, and every skeleton vertex is less
than 5/2 from c. A polygon is contained in the convex hull of its vertices,
so each entire skeleton support lies in B(gc,5/2). In every associated
skeleton plane tiling, the site set is therefore relatively dense with
covering radius rho=5/2. The open radius-1/4 disks about the sites lie in
disjoint skeleton interiors, so distinct sites have separation at least
1/2. Thus the sites are Delone. Using the skeleton to prove these two
facts is legitimate because its isometries and sites are the same as for X.
The actual curved Spectre support need not have radius rho.

## Genuine occurrence and complete neighbors

The finite domain is the level-3 Delta supertile from the author's exact
nine-category recurrence, with 559 skeleton supports. This is not an
arbitrary locally legal patch. The paper establishes the source hierarchy
and Appendix A constructs its geometric supertiles. Every category rule
contains a Delta child at position 1. Hence every level-4 supertile in the
paper's infinite hierarchy contains an actual level-3 Delta supertile.
In particular the three selected occurrences coexist in a genuine infinite
source tiling. The source occurrence and extension rely on the cited
Spectre theorem and recurrence, not on inference from finite growth alone.

The producer cancels exactly matched unit skeleton edges to obtain the
exposed boundary of the 559-support patch (758 edges). Paired edges must
have opposite orientation and multiplicity is at most two. At each selected
site p, every exposed edge is at distance strictly greater than 13. Since
p lies inside its own support and the patch is the genuine substitution
patch, the disk B(p,13) lies in the support union.

The exact computation intersects the bisector halfplanes for all retained
sites q with |q-p|<=8. It obtains a convex polygon C wholly inside B(p,4).
Any site farther than 8 cannot cut C, by the triangle inequality:
|x-q| >= |q-p|-|x-p| > 8-4 > |x-p| for x in C.
Every site of an additional source tile outside the finite patch is also
farther than 8. Indeed if such a site's distance from p were at most 8,
its entire skeleton support would lie in B(p,8+5/2), inside B(p,13),
contradicting disjoint interiors with the patch supports. The retained
13 margin is the conservative `2R+2rho = 8+5` margin. This proves complete
neighbors for the infinite tiling, including all unknown exterior tiles.

## Exact result and verification scope

The producer uses SciPy Voronoi only to suggest vertex and neighbor orders.
It reconstructs each proposed vertex by exact 2-by-2 bisector intersection
in Q(sqrt(3)). It verifies strict feasibility against every nonincident
retained bisector, positive consecutive turns, distinct side labels,
the radius bound |x-p|<4, and the complete boundary margin. Those exact
inequalities certify nondegenerate cells and imply stability under a
sufficiently small perturbation of the fixed template site. No explicit
parameter neighborhood is claimed.

| occurrence index | exact side count |
| --- | --- |
| 71 | 7 |
| 78 | 5 |
| 127 | 6 |

Side count is invariant under every planar isometry, so these cells are
three distinct congruence classes. Only this fixed corner-mean rule is
excluded. It is unnecessary to classify all cells after this first failure.
There is no claim of an intrinsic decoder or aperiodicity of arbitrary
tilings by any output cells.

Producer: `research/searches/spectre-voronoi-first-gate-2026-10-19.py`.
Certificate: `research/certificates/spectre-voronoi-first-gate-2026-10-19.json`.
The certificate records the exact site, witnesses, neighbors and relative
vertices; scalar coordinates are rational pairs `[a,b]` for a+b sqrt(3).
The producer borrows only exact scalar and affine primitives from
`source-decoration-hat-patch.py`; no Hat patch or Hat substitution is used.
Deterministic enumeration, no random seed, no solver, no truncation or
timeout; it stops upon the third side count. Retained source provenance is
checked locally and replay does not access the network.

Replay:

```
mise exec -- conda run --no-capture-output -n arisearch python research/searches/spectre-voronoi-first-gate-2026-10-19.py
```

The independent Sol audit checked the recurrence transcription, source
occurrence, exact geometry, and boundary argument. The exclusion remains
limited to this fixed site rule.
