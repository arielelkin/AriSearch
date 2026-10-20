# Residual exact hexagons: ETE chains give a periodic escape

Date: 2026-10-19. Status: proved and [independently Sol-reviewed](../reviews/hexagon-five-four-ete-chain-sol-review-2026-10-19.md).
No novelty claim. No new enumeration, larger collar, or plane extension from
patches is used.

## Theorem and scope

For each exact polygon pair at zero-based rows 15,16,23,26,31 of
`research/certificates/hexagon-five-four-39-omissions-2026-10-19.json`,
if the pair tiles the plane, it admits a tiling invariant under a nonzero
translation. This is conditional existence of a periodic escape; it does
not assert that any of these five pairs tiles. It does not assert a period
of every original unrestricted tiling or a rank-two period lattice.

The proof imports the reviewed defect-free convex-hexagon limit theorem,
the monohedral exclusions for these exact rows, and the existing complete
native dimer-corona enumeration and exact residual geometry checks.
References and replay commands are listed below. The geometric extension
of the reviewed private-AA chain theorem is proved here rather than
assuming the residual nonprivate A3 seam satisfies its stated hypotheses.

## 1. Every A in every defect-free ETE source has two halfturn seams

Take an admitted edge-to-edge trivalent plane tiling, supplied by the
hexagon limit theorem if an unrestricted plane tiling exists. Both types
occur, since neither exact polygon tiles alone by the retained monohedral
audit. Native words are A=(0,1,2,0,3,4), B=(0,1,1,0,2,3), and the five
colors are five distinct numerical lengths.

Every A5 side has an A5 mate. A reflecting mate puts two (3,4) corners at
one endpoint and requires a (3,3) third corner; neither prototype has one.
Thus this seam is a midpoint halfturn. This remains true for reflected
copies.

The native atlas is a necessary upper atlas, not a sufficient plane-tiling
model. Every actual trivalent star is a cyclic signed triple whose adjacent
side colors agree. Its opposite endpoints are also actual stars, so every
actual star survives every endpoint-pruning iteration. Normalize a chosen
A placement by an isometry, allowing reflection, to the reference A with
positive handedness. Its A5 mate then has positive handedness too. Walking
the ten-edge boundary of this actual dimer reads exactly a cycle of the
finite boundary factors in the atlas producer. All corner identities and
handednesses are retained in those factors. Consequently this cycle is
one of the seven enumerated corona states. No global continuation of an
arbitrary enumerated cycle is assumed.

For each residual metric, the existing exact geometry checker places all
seven cycles. Six fail necessary tile identity, nonoverlap, or complete
angle coverage. Only corona6 survives. An actual dimer corona cannot fail
any of these tests. Hence every A in any such ETE tiling has precisely the
retained corona6. In particular its A3 and A5 neighbors are the same-slot
midpoint halfturns; its other four sides meet the uniquely specified B
placements. This implication is universal within the ETE source, not a
claim inferred from the existence of one finite patch. Conjugating the
normalization handles all reflected A placements.

Write p0,...,p5 for reference A vertices and H_j(x)=p_j+p_{j+1}-x, with
indices modulo six. Then H3 H5 is translation by

    v=p3+p4-p5-p0=2(m3-m5).

The midpoints m3 and m5 are distinct in a strictly convex hexagon, so v is
nonzero. The earlier exact strip check independently verifies v for all
five metrics.

## 2. The two seams define proper nonbranching chains

On the set of actual A tiles, retain the two contacts across native sides
3 and5. This is a degree-two graph. Its two neighbors cannot coincide:
otherwise H3(A)=H5(A), forcing compact A to be invariant under the nonzero
translation H3 H5. Following a component alternates the two seam slots.
Every second step is translation by the physical image of v, up to sign.
Thus there are no finite components; each component is a bi-infinite
periodic chain of A tiles, with period length ell=|v|.

Choose the fixed interior anchor (m3+m5)/2 in reference A and connect it
to m3 and m5 by straight segments (the two halves of the midpoint chord). Transport this path to every A. Across a
retained seam the paths join at its interior midpoint. Their union within
a chain is an embedded line: interiors of different tiles are disjoint,
and at a retained seam midpoint only its two tiles are present. The two
anchor segments in one convex tile meet only at the anchor. The line is
proper and stays within a uniformly bounded distance C of its straight
period axis because its motif repeats after two tiles. Distinct chain
lines are disjoint. Two disjoint proper lines lying in bounded strips
around nonparallel axes cannot exist: the two tails of one eventually
lie in the opposite halfplanes outside the other's strip, and Jordan
separation forces an intersection. Therefore all chain axes are parallel.
All periods have the same length ell, including reflected chains. Fix one
physical vector T of that length in the common axis direction. Every
chain, every A tile, and every separator line is invariant under T.
This proves global nonbranching and synchronization of the A carrier.

## 3. Periodic filling of the complementary bands

A common period for A alone is insufficient. We now give the filling
argument, following Sections3–5 of the independently reviewed private-AA
chain theorem. It does not require every B to touch A or belong to one
chain corona.

Since B has no monohedral plane tiling, A is uniformly unavoidable: there
is L such that every radius-L disk in every admitted tiling meets A.
Otherwise arbitrarily large A-free disks, translated to the origin, have
a convergent tiling subsequence giving an all-B plane tiling. This uses
compactness of placements of two fixed positive-area bounded polygons.
Contained anchor disks and a diameter bound D give uniform local
finiteness by disk packing.

Quotient by T. The disjoint proper periodic separators become locally
finite disjoint essential circles in a cylinder. They are linearly
ordered, with consecutive circles on both sides: an extreme would leave
arbitrarily large A-free disks, contradicting L. No third A chain can
enter an open band between consecutive separators; its interior path to
its own separator would have to cross a boundary separator. A tiles from
the boundary chains stay within D of those chains. Since each chain stays
within C of its axis, consecutive axis heights differ by at most
2(C+D+L). Thus all bands have a uniform transverse width bound W. They
are individually T-invariant, including any polygonal overhangs.

Fix one band and its lower boundary chain. Every B in it can be joined to
an A anchor on that chain by a bounded-length generic path in a uniformly
bounded disk. Disk packing bounds the number K of tiles crossed,
uniformly over all bands and boundary phases. Removing loops gives a
whole-side adjacency path of length at most K in the original ETE source.
Each step has finitely many exact relative isometries: choose the two
types, their native side slots, and endpoint correspondence. Reflections
are included. As the lower A chain has two placements modulo T, all B
placements occurring in the original band filling belong modulo T to a
uniformly bounded finite set, of size at most

    C0=2 sum(j=0,...,K) |H|^j,

where H is the finite relative-isometry set. This bound does not assume
finitely many absolute orientations or a discrete set of arbitrary
boundary phases. It derives all placements from the fixed lower chain.

Take these candidate placement orbits and discard candidates leaving the
band or overlapping the fixed A carrier. Both tests commute with T. In
each period slab choose a subset of the at most C0 candidates anchored
there. Diameter bounds give a uniform finite window of slabs sufficient
to test every interior overlap and every coverage condition. Coverage is
a finite condition: arrange the finitely many polygon boundaries that
can meet the compact slab portion of this bounded-width band, then require
each open arrangement cell outside A to be covered exactly once. Closed
tiles and local finiteness supply coverage of boundary points as well.
These conditions define a one-dimensional shift of finite type with
uniformly bounded alphabet and window sizes. The original B filling is
a bi-infinite accepted sequence, so the finite overlap graph has a cycle.
A simple cycle has length at most a uniform integer M. Repeating it
supplies an actual infinite band filling with period mT, 1<=m<=M.

Independently replace the filling of every band by one such cycle filling.
With N=lcm(1,...,M), all replacements and the fixed A carrier are invariant
under NT. Band interiors are disjoint, their separator boundaries lie
inside the fixed A carrier, and all open cells are covered. The union is
therefore an admitted plane tiling with the nonzero period NT. This proves
the theorem without assuming that any chosen finite patch extends.

## Exact dependencies and limits

* Native completeness: `research/searches/hexagon-five-four-forced-dimer-2026-10-19.py`,
  its independent `...-check-...py`, and retained certificate; 180 native B
  words, signed stars allowing repeats, endpoint fixed point, seven full
  dimer boundary cycles for this B word. No new finite domain is opened.
* Metric elimination: `research/searches/hexagon-five-four-five-residual-coronas-2026-10-19.py`
  and its certificate: exactly five rows times seven coronas, arithmetic
  in Q(sqrt(3)), both handednesses represented. Only corona6 is valid.
* Translation data: `research/lemmas/hexagon-five-four-corona-translation-strip-2026-10-19.md`
  and its exact certificate. The strip's failure to self-stack is irrelevant
  to the band fillings taken from an assumed actual ETE source.
* Imported chain-filling proof and hostile review:
  `research/lemmas/periodic-private-aa-chain-escape-2026-10-15.md` and
  `research/reviews/private-aa-chain-hostile-2026-10-15.md`.
* Limit theorem: `research/lemmas/hexagon-limit-and-periodicity.md`.
* Monohedral exclusions: `research/certificates/hexagon-five-four-39-omissions-2026-10-19.json`
  and `research/reviews/hexagon-five-four-39-omissions-hostile-review-2026-10-19.md`.

No assertion that every B belongs to a translated ten-tile corona is needed
or established here. No direct second strip stacking, radius expansion,
finite quotient search, arbitrary-tiling recognition, or stronger plane
existence claim follows. The exact remaining audit obligation is the
necessity/completeness passage from an arbitrary ETE dimer to the retained
seven cycles, plus the imported separator/SFT argument's stated hypotheses.
