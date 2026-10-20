# A P5/P5 half-side split with one closed midpoint branch

Date: 2026-10-20. Status: **exact conditional local star; no global forcing**. This is a separate geometry from the [first half-side fixture](terra-p5p5-halfside-2026-10-20.md), selected after its Q full-side escape was found.

## Exact shapes and deduplication

Use the same rational host pentagon

```
P=((0,0),(5,0),(6,2),(3,5),(-1,3))
```

and change the partner to

```
Q=((0,0),(5,0),(6,2),(3,8),(1,7)).
```

The exact turn determinants are `P=(15,10,9,18,14)` and `Q=(35,10,12,15,13)`, so both polygons are strict convex pentagons. Their doubled areas are 48 and 65, proving distinct congruence classes. Squared side words are `P=(25,5,18,20,10)` and `Q=(25,5,45,5,50)`. Q has **no side of squared length 20**. The neighboring-ray dot words are `P=(-5,-5,-3,-6,-2)` and `Q=(5,-5,-9,0,-9)`; Q has an acute first vertex and a right fourth vertex. Neither shape has consecutive supplementary angles, so the basic half-turn monohedral shortcut is absent. Other monohedral carriers are unclassified.

These angle and side words exclude exact duplication of the prior Cairo 90/120 and R/B/G families, pentagrid U/V/W, the `(60,60,150,120,150)` long-edge family, and the previous acute/obtuse metric in the [deduplication audit](shape-first-dedup-audit-2026-10-20.md). This construction does not cut a Y parent or an Ammann source tile. Its proposed contact is a P/Q/Q split of one side, with a Q/Q seam through the split point.

## Exact three-tile patch and conditional branch

The P edge `(3,5)->(-1,3)` has squared length 20 and midpoint `M=(1,4)`. Each half has squared length 5, matching Q edge 3. Under the prescription that one *full native Q edge* occupies each half and interiors are disjoint, four placements exist on each half. Exactly **one** of the sixteen ordered combinations is nonoverlapping. It is also a complete local star at M: the two Q right angles fill P's flat 180-degree sector, and the remaining Q rays continue on a shared seam. The exact copies are

```
Q1=((4,12),(-1,12),(-2,10),(1,4),(3,5))
Q2=((-36/5,32/5),(-21/5,52/5),(-2,10),(1,4),(-1,3)).
```

Q1 and Q2 share the segment `M->(-2,10)`; each meets its assigned half of P's side. Exact separating-axis checks verify pairwise disjoint interiors. Thus the patch gives a concrete conditional continuation: *if* the P side is split into these two full Q edges, their collision-free assembly determines this closed midpoint branch within the stated sixteen placements. It does not classify arbitrary partial contacts or larger stars.

The host side still has a legal **P/P whole-side alternative**, obtained by reflecting P across that side. The second P copy has vertices

```
((-14/5,28/5),(1/5,48/5),(12/5,46/5),(3,5),(-1,3)).
```

Its interior is disjoint from the host's. Thus the Q/Q split is not locally compulsory; no universal forcing, plane tiling, aperiodicity, or species-omission result follows. The P/P alternative is the immediate obstruction to promoting this fixture. A future change would need an endpoint incompatibility that excludes P/P in an actual global context, not a larger patch around this same midpoint alone.

## Replay and scope

```
mise exec -- conda run --no-capture-output -n arisearch python research/searches/terra-p5p5-closed-midpoint-2026-10-20.py
```

The checker imports exact rational rigid-motion and convex-separation helpers from the first fixture's script. Its assertions check convexity, unequal areas, acute Q angle, lack of consecutive supplementary pairs, absence of a full Q side of squared length 20, uniqueness of the nonoverlapping half-side pair in the declared domain, a closed midpoint star, and a P/P whole-side alternative. No search outside that finite local prescription is claimed.
