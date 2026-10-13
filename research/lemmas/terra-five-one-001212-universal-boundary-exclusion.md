# A001212 on B5+1: universal boundary-row angle obstruction

Date: 2026-10-13. Status: [independent hostile review VALID](../reviews/terra-five-one-001212-universal-boundary-fresh-hostile-review.md); exact native checks PASS. The [full-interval scope review](../reviews/five-one-full-strict-convex-angle-line-extension-review.md) extends this coverage mechanism to 108 < x < 126, x != 120. Restricted-family result, not the original research problem.

## Statement

Let x in (112.5,126), x!=120, y=720-5x, z=4x-360, r=360-2x, s=360-2y. Let actual strictly convex A have native cyclic angle word (x,x,y,z,y,z), and actual strictly convex B have angle word (s,r,r,r,r,r). Side lengths are arbitrary positive values consistent with the actual polygons, and may have any equality specialization. If the pair admits an unrestricted plane tiling, it admits a tiling with nonzero translational symmetry.

A stronger intermediate statement holds: no actual defect-free saturated mixed field in the reviewed honeycomb reduction exists for these angle words. Any extracted field must omit B and hence admit the established pure-A periodic escape.

Dependencies: reviewed [five-plus-one saturation extraction and palette](terra-five-one-b-saturated-chain-reduction.md), reviewed actual honeycomb development, root's [opposite BB row lemma](five-one-middle-mask-b-rows-and-bounded-a-strips.md), and the settled unrestricted convex-hexagon monohedral escape classification. The no-AAA binary lifting theorem is not needed for this exclusion. Original partial contacts and reflections enter through the reviewed saturation/honeycomb reductions, not through an assumption that the original tiling is already a row field.

## Allowed stars and forced B rows

The complete allowed star language is AAA(x,y,z), AAB(x,x,r), AAB(y,y,s), ABB(z,r,r). In a saturated mixed field every B has degree two. Native A colours are C=(0,0,1,2,1,2), standing for x,y,z. Its endpoint-pair word is (00,01,12,12,12,02). B outer masks would require an A22 side, which is absent; hence only native BB mask {1,4} survives. The two BB directions are opposite. The reviewed row lemma therefore makes every B component a complete lattice row, with all such rows parallel, and at least one full A row between B rows. The argument also applies if there is an infinite A half-plane rather than a subsequent B row.

## A strip cannot have width one

B AB sides have only endpoint palettes02 and12, since the outer masks are absent. Native A sides0 (00) and1 (01) must therefore both be AA, irrespective of any length merges. They are adjacent sides. In a width-one A strip between B rows, an A has A neighbours only in its two opposite row directions. Its two AA sides are consequently opposite, and cannot include the two adjacent private native sides0,1. Rotations and reflections preserve adjacency, so no A placement realizes a width-one strip. This is a native angle-palette obstruction, not a metric inequality.

Thus every A strip adjacent to a B row has at least two A rows, or is an A half-plane. Its boundary A row has inward AAA vertices and outward AAB vertices.

## Complete boundary native gate

Choose common row-direction AA sides at global slots2,5. For the lower boundary of a B row (A has B above), the two AB sides are0,1 and their common global corner1 must have colour z, by ABB(z,r,r). All twelve native rotations/reflections are

    corners[k]=C[(rotation+sign*k) mod6].

Exactly four have z at corner1:

| State | Rotation/sign | Global corner colours0,...,5 |
|---|---|---|
| 0 | (0,-) | 0,2,1,2,1,0 |
| 1 | (2,+) | 1,2,1,2,0,0 |
| 2 | (4,+) | 1,2,0,0,1,2 |
| 3 | (4,-) | 1,2,1,0,0,2 |

For a left/right boundary A pair across row-AA sides2/5, the outward AAB A colours are (left corner2,right corner0), and inward AAA A colours are (left corner3,right corner5). The outward pair must be equal x/x or y/y; the inward pair must be distinct for a rainbow AAA star. Among the16 eligible pairs, exactly four satisfy these necessary angle conditions:

| Directed states | Outward colours | Inward colours | Native AA metric equality |
|---|---|---|---|
| 0→1 | y,y | z,x | a3=a1 |
| 1→1 | y,y | z,x | a4=a1 |
| 3→2 | y,y | x,z | a1=a3 |
| 3→3 | y,y | x,z | a1=a4 |

Every accepted outward pair is y/y; there is no x/x pair. The full graph's bi-infinite paths are constant state1 or constant state3, with a1=a4. This transfer detail is retained, but the universal exclusion needs only the y/y conclusion, not boundary periodicity or the additional metric relation.

The opposite face is checked directly. Here A has B below: its AB sides3,4 meet at global z corner4. The four native placements are (1,+),(1,-),(3,-),(5,+). Outward pairs are (left corner3,right corner5), inward pairs (left corner2,right corner0). The resulting directed graph and native metric conditions are identical. Every outward AAB vertex again has y/y. This includes global reflection without assuming the actual polygon has an intrinsic reflection symmetry.

## Contradiction and actual-pair consequence

Each B has exactly two AAB vertices, native corners0 and3, on its opposite row faces; its other four vertices are ABB. Both adjacent boundary A rows require y/y at their outward AAB vertices. By the allowed language, both of these B vertices must have angle s. But B has only one native s corner, while its other AAB corner is r. The contradiction excludes any B row, hence every mixed saturated field.

If the original actual pair tiles, the reviewed extraction must consequently produce a B-omitting all-A plane tiling. The settled monohedral convex-hexagon classification gives a periodic A-only tiling, which is admitted by the original pair. This handles arbitrary A/B metrics and all further equality specializations: they never affect the angle contradiction. There is no need to enumerate203 side partitions, solve positive polygon closure, or increase any spatial search domain after this uniform exclusion.

## Exact computation and scope

Finite domain stated before computation:2 faces*12*12 native A pairs, plus12 width-one A placements. The producer retains all native corner/edge profiles, both four-state transfer graphs, exact side equalities, and all width-one failures. The independent checker imports no producer code; it reconstructs native sides from ordered native vertex pairs, scans the full288 pair domain, independently computes cyclic states by reachability, and checks the exact certificate.

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/searches/terra-five-one-001212-boundary-transfer.py
    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_terra_five_one_001212_boundary_transfer.py

Certificate: `research/certificates/terra-five-one-001212-boundary-transfer.json`. The producer and independent checker pass. The retained MISE_AUTO_INSTALL=0 workaround skips installation of unrelated tooling; it does not waive provenance checks or mutate configuration.

What this proves: the complete A001212 native angle family on the stated changed-multiplicity line cannot force aperiodicity, at every positive actual metric and every length alias. It does not cover the remaining native words, a different angle resonance or multiplicity, a non-honeycomb source without the reviewed reduction, or the full original acceptance criteria. A cycle in the retained boundary graph is only local compatibility; no global A strip or plane tiling is inferred from it.
