# Periodic private-AA chains give a translational escape

Date:2026-10-15. Status: independently hostile-reviewed VALID;
[review](../reviews/private-aa-chain-hostile-2026-10-15.md).
This is a restricted periodic-escape theorem, not the main problem's solution.

## Statement

Let A,B be genuine convex hexagons with nonempty interiors. Suppose A has six
pairwise distinct native side lengths and exactly two of them, u,v, are
private to A. Assume that B does not have adjacent equal-length sides at TWO
DIFFERENT numerical lengths. Then if the pair tiles the plane with arbitrary
isometries and contacts, the pair admits a tiling with a nonzero translation.

In particular the extra assumption holds when B has exactly four distinct
lengths with multiplicities (3,1,1,1): only the tripled length can have a loop.
No double periodicity or periodicity of every original tiling is asserted.

Dependencies: the reviewed defect-free limit theorem and unrestricted
monohedral hexagon periodicity theorem recorded in
[hexagon-limit-and-periodicity.md](hexagon-limit-and-periodicity.md), and the
reviewed [uniform unavoidable-type occurrence theorem](two-type-uniform-density.md).
The elementary Jordan separation theorem for a proper embedded line is used
below (equivalently apply the Jordan curve theorem after one-point
compactification). No bounded search, solver, or finite-patch inference occurs.

## 1. Two compulsory half-turn neighbors

If B tiles alone, its monohedral periodic escape suffices. Thus assume B has
no plane tiling. Take a defect-free, edge-to-edge, trivalent tiling by A,B.
It contains A, and A is uniformly unavoidable: every radius-L disk intersects
A, for some finite L depending only on the two shapes. Let D bound their
diameters and choose contained anchor disks of common positive radius rho.
These give a uniform bound on the number of tiles meeting any fixed-size
ball, by disk packing, and hence local finiteness.

Across a private A side of length u stands another A using that same unique
native side slot. There are exactly two opposite-interior endpoint maps:
the half-turn about the side midpoint, exchanging its endpoint slots; and
reflection in its line, preserving its endpoint slots. Let x,y be the two
other native lengths at its endpoints. A's distinct lengths give x!=y.
For the reflecting map the remaining B corners must have arm pairs xx and
yy. They cannot be A corners, because A has no equal adjacent side lengths.
Thus B would need loops at two different numerical lengths. The hypothesis
excludes this. Both private AA neighbors are therefore forced midpoint
half-turns, at every occurrence and with every reflected placement.

Let m_u,m_v be the distinct midpoints of the two private sides in A's
reference placement. Their half-turns compose to translation

    T_A=2(m_v-m_u) !=0.

The private AA graph has degree two. Its components are bi-infinite chains:
alternating u,v steps contain all translates of an A by integer multiples
of T_A, so a finite component would contradict T_A!=0 and disjoint interiors.
Two incident neighbors cannot be the same A, for that would make this
nonzero translation preserve a compact A. Each component consists of two
periodic placement sequences, giving a genuine period gT_A for an initial
placement isometry with linear part g. In particular every component has
the SAME positive period length ell=|T_A|.

## 2. Proper periodic separators force all chain axes parallel

In each placed A choose its anchor point, transported from one fixed
reference interior point. Connect it to the midpoints of its two private
sides by straight segments. The open segments lie inside the A interior.
Across a private seam the adjacent segments meet at the common side midpoint.
Following one private-AA component gives a simple polygonal embedded line:
different tiles have disjoint interiors, and the curve avoids all native
vertices; at a seam midpoint only the two tiles of that component occur.
It cannot self-intersect. Every two steps translate by its period vector,
so it is proper, periodic, and contained in a bounded-width strip around
a line parallel to that vector. The width is uniformly bounded by a constant
C depending only on A and u,v; a two-tile fundamental path is compact.

Curves belonging to different private components are disjoint, including
at seams, because each point of a curve is in an A interior or the interior
of its private AA edge. Such a point cannot belong to another component.

Two such proper curves with nonparallel axes cannot be disjoint. One curve
separates the plane into two components. Outside its bounded axis strip,
the two open half-planes lie in its opposite complementary components
(as follows from Jordan separation of a proper line). The two tails of a
nonparallel strip-bounded proper line eventually lie in these two different
half-planes. Its connected path must intersect the separating curve.
This contradicts disjointness. Thus all private-AA chain axes are parallel.

Rotate the coordinate frame so their common direction is horizontal.
Every component's period vector then equals T=(ell,0) or -T. Therefore
translation by the SAME nonzero T preserves every A chain, all A tiles,
and each of the chosen separator curves individually. This conclusion
concerns the A carrier; no periodicity of the B filling is inferred yet.

## 3. Consecutive separator bands have uniformly bounded width

Pass to the cylinder obtained by quotienting the plane by translation T.
Each separator projects to an embedded essential circle. They are disjoint
and locally finite: a compact cylinder segment lifts to a bounded planar
rectangle plus a uniformly bounded horizontal margin C+D; only uniformly
finitely many A tiles meet it, and every crossing separator uses one of
those tiles. Disjoint essential circles on a cylinder are linearly ordered
and cut it into annular bands. Local finiteness prevents a finite-height
accumulation. Unavoidability of A prevents a first or last circle: beyond
an extreme chain all sufficiently distant points would have A-free disks
of radius L. Thus there is a consecutive band on each side of every curve,
and these bands exhaust the cylinder off its curves.

Here are explicit reasons their vertical extents have a uniform bound.
A tile not belonging to either boundary chain cannot meet the OPEN region
between two consecutive separator curves. If it did, its connected interior,
which contains its own separator segment, would have to cross one boundary
curve to leave that band, impossible because different A interiors cannot
meet that curve. Its own separator would therefore lie in the band,
contradicting consecutiveness. Boundary-chain A tiles lie within distance D
of their own curve. Choose the axis strips of the two boundary curves with
half-width C. If their horizontal axis heights differ by more than
2(C+D+L), the middle horizontal line contains a point whose radius-L disk
lies farther than D from both boundary curves and stays in the band.
That disk meets no A, contradicting unavoidability. Hence axis heights are
separated by at most2(C+D+L), and every lifted band lies in a straight
horizontal strip of uniformly bounded width W=4C+2D+2L. Enlarging C slightly
to cover the chosen fundamental anchor paths changes nothing.

Each lifted band is individually T-invariant, since translation preserves
both boundary curves and their order. It may have nonstraight, overhanging
boundaries. We work with the entire band, including any bounded cavities
of the A carrier inside it; we never assume that individual components of
the complement of the A union are individually T-invariant.

## 4. Uniformly finite candidate B placements in a period slab

Fix one lifted band and its lower periodic boundary chain. Every B tile in
that band is at a uniformly bounded Euclidean distance R0 from an A anchor
on that chosen chain. Indeed its y coordinate lies in a strip of width W,
and along the lower curve's two-tile period motif some anchor can be chosen
with x coordinate within ell+2D+C. Thus R0 depends only on the fixed shapes,
L and ell, not the band or its upper-boundary phase.

A generic polygonal path from an interior point of that B to this A anchor
can be chosen inside a ball of radius R0+2D+1, avoiding all native vertices
and crossing sides transversely. Disk packing bounds the number of tiles
meeting that ball by a common integer K. Removing loops from its adjacency
walk gives a full-side tile path of length at most K. This path need not
stay inside the band: its sole purpose is to bound placements. Its length
bound is uniform over all bands and B occurrences.

For two indexed reference polygons, an entire-side match has finitely many
relative isometries: choose the neighbor type, its side slot, and its
endpoint correspondence, then opposite interior half-planes select the
isometric extension. Reflections are included in these finite choices.
There is therefore a finite set H of possible complete relative isometries
for one adjacency step. A path of length at most K has relative placement
in the finite collection of products H^{<=K}. No finiteness of absolute B
orientations is assumed; it is derived here from the bounded path.

The chosen boundary chain has at most two indexed A placements modulo T.
Consequently ALL actual B placements in the band, modulo translations nT,
belong to a set of at most

    C0=2 sum_{j=0}^K |H|^j

possibilities. These are exact isometries, not just orientation symbols.
Take that finite candidate set and all its integer T translates, discard
placements leaving the band or overlapping the FIXED A carrier, and retain
all others. Both tests are T-equivariant. The original B filling uses only
these candidates. Upper-boundary phase cannot introduce a continuous
placement parameter: the bounded path to the fixed lower chain already
specified every candidate exactly. Different bands may have different
candidate sets, but their cardinalities have the same uniform bound C0.

## 5. A finite-state strip filling has a uniformly bounded periodic witness

Choose an anchor in each B reference polygon. For each orbit of candidates
under T choose the unique anchor x coordinate in[0,ell). In slab n specify
which of those at most C0 anchored candidates, translated by nT, are present.
This is an alphabet of at most2^{C0} possible selections.

The tile diameter bound gives a uniform integer q such that a tile meeting
one period slab has its anchor at most q slabs away. Thus no-overlap is a
constraint on at most2q+1 consecutive selections. Coverage of the part of
one slab outside the fixed A carrier is another finite-window condition:
only candidates anchored in those neighboring slabs can cover it. There are
finitely many candidate polygons in that window. Intersect their boundaries
and the fixed periodic A and band boundaries to obtain a finite arrangement
in a compact rectangle containing the slab portion of the band. Each open
two-dimensional arrangement cell must be covered once (and A interiors zero
times by B); finite no-overlap/coverage decisions impose a fixed set of
allowed selection words. Covering the open cells suffices for boundary
coverage because tiles are closed and only finitely many meet that slab.
The fixed A carrier is already present. The boundaries are polygonal with
finitely many segments per period, so the arrangement is finite even when
a band boundary backtracks horizontally.

We have a one-dimensional shift of finite type with alphabet size and
window size bounded UNIFORMLY over all bands. The original filling is a
bi-infinite allowed sequence, so its finite directed overlap graph has a
cycle. A simple directed cycle has length at most a common bound M on the
number of graph vertices, for example M=(2^{C0})^{2q}. Repeating it gives
an allowed periodic candidate selection and therefore a valid B filling
of the entire band, with period mT for some1<=m<=M. No finite patch is
promoted to an infinite filling: the repeated graph cycle explicitly
satisfies every finite-window constraint at every integer slab.

Let N=lcm(1,2,...,M). Independently choose one such periodic filling in
each consecutive band. All have the common nonzero period NT. The fixed
A tiles have period T and hence NT. Candidate B tiles stay inside their
bands, so fillings from different bands have disjoint interiors and cannot
create gaps across a separator lying inside the fixed A carrier. Together
with the A carrier they cover the plane. They form a tiling admitted by the
original pair, invariant under NT. This proves the theorem.

## Scope and audit obligations

The proof constructs existence of one translational escape, using whole-side
adjacency only to derive finite candidate positions from the original
limit tiling. The final strip fillings need satisfy only unrestricted
geometric disjointness and coverage, as allowed by the main definition.
The uniform period bound is existential; no ineffective bound is substituted
for a computer search certificate and no actual finite search is claimed.

The fresh independent review checked: proper-chain separation and cylinder
ordering; the band-width/unavoidability argument; bounded adjacency paths;
finite exact placements despite arbitrary initial phases; local coverage as
an SFT; and synchronization over infinitely many bands. A periodic A carrier
alone would be insufficient; Sections4-5 are essential. The theorem does
not cover the B double-loop branch without the stated no-two-loop hypothesis.
