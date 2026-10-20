# Shape-first P5/Q6 local star and branch

**Status: exact local candidate only (2026-10-20).** No plane tiling or
aperiodicity claim. Replay with
`mise exec -- conda run --no-capture-output -n arisearch python research/searches/shape-first-p5q6-star-2026-10-20.py`.

## Deduplication boundary

This is a nonregular pentagon and a noncentral equiangular hexagon, with
pentagon angle word `(120,135,60,135,90)` degrees and hexagon side word
`(5,1,4,3,3,2)`. These exact words differ from the Cairo 90/120 pentagons,
the pentagrid pentagons, both long-edge P5/P5 fixtures, the earlier 66/162
P5/Q6 scaffold, and the P5/Q7 palettes indexed in
[`shape-first-dedup-audit-2026-10-20.md`](shape-first-dedup-audit-2026-10-20.md).
The hexagon's cyclic word is also distinct, including under reversal and
scale, from the recorded H6/H6 seeds. The mechanism tested here is a
length-1 bridge at a P/Q/Q 120-degree star, rather than a source dissection,
power cell, or long-edge T contact. This is a repository deduplication check,
not a literature novelty claim.

## Exact polygons

Work in the real embedding of `K=Q(sqrt(2),sqrt(3))`. Put `r=sqrt(2)>0`,
`s=sqrt(3)>0`. Define P by successive edge directions
`(0,45,165,210,300)` degrees and side lengths

```
(5, 3, (13r-3s+3)/2, (3rs-13+5s)/2, 4).
```

Start at `(0,0)` and cumulatively add these edge vectors. Define Q from
`(0,0)` by successive edge directions `(0,60,120,180,240,300)` degrees
and lengths `(5,1,4,3,3,2)`. The script prints every vertex in the quartic
field presentation `t=r+s`, `t^4-10t^2+1=0`, positive real root.

Exact vector sums close both polygons. Every successive edge cross product
is strictly positive, so they are strictly convex. P has side lengths about
`(5,3,8.0943,1.5044,4)`; decimals only identify the numerical equality
pattern. Q has two adjacent length-3 sides, and its opposite sides are not
all equal (`5 != 3`), so it is noncentral. P and Q are distinct by side count.

## Legal patches and conditional feature

Let P's 120-degree vertex be the origin. At it, P has outgoing radial sides
of lengths 5 along direction 0 and 4 along direction 120. Place `Qa` with
its native corner 1 at the origin, native side 0 on the length-5 ray and
native side 1 on the length-1 ray at 240 degrees. Place `Qb` with native
corner 2 at the origin, native side 1 on that length-1 ray and native side
2 on P's length-4 ray. Thus the three exact 120-degree sectors fill 360
degrees, and the three full radial edges match. The script computes the
isometries and checks all three pairwise interiors disjoint by an exact
separating-axis test.

Conditional on a **trivalent full-edge 120-degree completion** with a Q
across P's length-5 side, this continuation is forced by native lengths:
Q's length-5 side can expose length 1 or 2 at the center, while its only
route to P's length-4 radial side uses its `(1,4)` corner. The length-2
choice has no `(2,4)` Q corner. This is a concrete local forcing feature,
not an unrestricted tiling rule; partial contacts or extra vertices can
evade the condition.

From the exact P/Qa/Qb patch, Qb has two exposed length-3 sides, native
slots 3 and 4. Attaching a fourth Q with either native length-3 side to
either exposed host side gives **eight** distinct legal patches: every
`(host,new)` in `{3,4} x {3,4}`, with both orientation-preserving and
reflected attachments. The script prints every fourth-tile vertex and
verifies disjoint interiors exactly. The first version of the verifier
wrongly required positive polygon orientation for reflected copies and
reported only four branches; this was corrected before this report.
Hence the first forced star does **not** determine a unique next tile.

## Focused continuation: full-edge obstruction

The pair has **no edge-to-edge plane tiling**. P's side 2 has unique length
`(13r-3s+3)/2`, different from all other P and Q side lengths. Therefore
every P side 2 in a full-edge tiling must meet another P side 2. Its
endpoints have angles 60 and 135 degrees. A 60-plus-135 pair cannot be
completed to 360 by further full corners from the available angle palette
`{60,90,120,135}`: the remaining 165 is not a sum of members of that
palette. Thus the two 60 endpoints meet, as do the two 135 endpoints.

At the latter endpoint the angle sum is `135+135`; the only full-corner
completion is P's 90-degree corner. Each 135 endpoint incident to P side 2
also has a P side of length `l3=(3rs-13+5s)/2`. The two remaining radial
edges at the vertex consequently both have length `l3`, whereas the P
90-degree corner has adjacent lengths `l3` and 4. It cannot fill the
vertex. This exact local contradiction applies to every P copy, with
reflections included. It blocks edge-to-edge growth of even the displayed
P/Q/Q star, despite its legal finite patches.

## Escape checks and remaining obligations

P has no adjacent supplementary-angle pair. The replay script evaluates
all fifteen Rao monohedral pentagon types under both cyclic orientations,
using the repository's reviewed Table 2 transcription and exact side
equalities; there is no match. This uses the imported pentagon classification
as a dependency for the P-only exclusion. Q is equiangular and noncentral;
the imported equiangular specialization of the monohedral hexagon theorem
rules out a Q-only tiling (see
[`two-equiangular-hexagons-sol-2026-10-19.md`](two-equiangular-hexagons-sol-2026-10-19.md)).
These checks exclude the immediate monohedral periodic carriers only.
The full-edge obstruction is stronger locally but does not exclude tilings
with partial contacts; the 60+120 supplementary pair leaves that possibility
open. No unrestricted partial-contact search, mixed flat torus, or global
extension has been checked. Since any plane extension must depend
essentially on partial contacts, this pair is **stopped as an edge-to-edge
construction**. Reopen it only with a specific viable T-contact mechanism,
not more growth of the eight full-edge fourth-Q branches.
