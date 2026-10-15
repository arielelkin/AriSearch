# Fresh hostile review: periodic private-AA chains and strip filling

Date: 2026-10-15. Verdict: **VALID** for the full written theorem in
`research/lemmas/periodic-private-aa-chain-escape-2026-10-15.md`.
Reviewer: independent of the author; developed no part of the author proof.
The full proof and its uniform-occurrence dependency were read. No
substantive defect found, no repair to the author proof required.

## Exact scope and dependencies

A,B are genuine convex hexagons; A has six distinct lengths and exactly
two A-private native sides. B has loops (equal adjacent sides) at at most
one numerical length. Tileability with arbitrary isometries and contacts
implies existence of a tiling with a nonzero translation. The conclusion
is rank-one periodic escape; double periodicity or periodicity of every
original tiling is not asserted. In particular this applies to B having
four distinct lengths with multiplicities (3,1,1,1) when exactly four A
lengths are shared.

Imported reviewed dependencies are the defect-free limit, monohedral
hexagon periodicity, and uniform unavoidable-type occurrence. The proper-
line Jordan separation theorem is explicitly used. This review checks the
new unbounded geometric/finite-state bridge, not merely the intermediate
periodic A carrier. No finite computation or numerical certificate is
claimed by the author; no artificial checker is needed to replace this
written geometric audit. Novelty remains a separate obligation.

## Forced native neighbors and the chain curves

Across a private A side the neighbor is A in the same unique native slot.
Endpoint preservation gives two third-tile loop corners at its distinct
endpoint-adjacent lengths. A cannot supply either loop, so B would need
two different loop labels, contrary to the hypothesis. Thus every private
AA neighbor is the actual midpoint half-turn, including reflected hosts.
Two such half-turns have nonzero translation 2(mv-mu), since distinct
native side midpoints of a genuine convex polygon differ. Alternating
private-slot walks cannot close, and their two-step placements repeat by
that vector. Thus every degree-two component is a bi-infinite two-A chain,
with the same positive translation length ell.

The chosen anchor-to-midpoint segments are valid simple arcs in each A.
Two distinct boundary midpoints cannot lie in the same ray from a strict
interior anchor of a convex polygon; hence the two segments do not retrace.
Their interiors stay strictly inside A. At a private midpoint the union
of the two adjoining A tiles contains a neighborhood of that point.
Therefore the assembled curve is a simple embedded line and no other
component curve or B tile can meet it. Two-step translation makes it proper
and confines it to a uniform strip. These arguments do not presume that a
native chain boundary is itself straight.

Proper Jordan separation justifies the common-axis conclusion: the two
outside half-planes of a strip-bounded proper line lie in different
components of its complement. A line bounded about a nonparallel axis has
its two tails in these different half-planes, forcing intersection.
Disjoint chain curves therefore have parallel axes. Equal positive period
lengths then make their periods exactly plus or minus ONE common vector T.
Thus every A component, the entire A carrier, and every separator curve
are individually T-invariant. Arbitrary chain phases do not affect this.

## Ordering and the uniform band width

Modulo T each proper curve is an embedded essential circle on a cylinder.
The curve family is locally finite there: a compact cylinder rectangle
lifts to one bounded horizontal period rectangle, and every meeting curve
contains a segment in an A tile meeting that compact rectangle; packing
allows only finitely many such A tiles. Disjoint essential circles are
linearly ordered. Local finiteness prevents finite-height accumulation,
and A unavoidability rules out first or last curves. Therefore the order
has consecutive curves on both sides and its bands exhaust the complement
of the separators. This rules out a hidden dense family or a single
unbounded final band.

The proof correctly establishes that only the two boundary chains' A tiles
can enter an open consecutive band. Any other A has a connected interior
containing its own separator arc. To enter that band from elsewhere it
would cross a boundary separator, whose points are in interiors of the
fixed A carrier, impossible for another tile interior. If its arc were
already inside the band, that arc's full separator would be an intervening
curve, contradicting consecutiveness.

Each boundary-chain A lies within its diameter bound D of that curve.
If the axis-height gap exceeded 2(C+D+L), the intermediate straight strip
would contain a radius-L disk inside the band and farther than D from
both curves, hence free of A. This contradicts the reviewed uniform-
occurrence theorem, which applies after excluding B monohedral tilability.
Very reversed axis heights would already contradict the ordering of the
curves and their bounded axis strips. The stated enlarged W bounds every
band's vertical extent. Overhangs and cavities are allowed; no component
of the A complement is incorrectly declared invariant under T.

## Finite exact placements despite phases and orientations

For any B in a band, choose a nearby A anchor from the LOWER boundary
chain. Uniform band width and a two-tile periodic motif bound this distance
independently of the band and upper-chain phase. A generic short path
within a fixed-size ball avoids all native vertices and crosses full sides.
Contained-disk packing bounds all tiles meeting that ball by K, uniformly.
After erasing repeats its native-adjacency path has length at most K.
It is harmless that this path can leave the band: it is used only to list
possible relative placements from a chosen lower A, in the original tiling.

Full-side indexed matches have a finite alphabet H of COMPLETE relative
isometries, since both native side slots and ordered endpoint match are
chosen, and opposite interiors select the extension. Finite products up
to K give finitely many actual B placements from an indexed lower A. Even
if B has intrinsic symmetries, an arbitrary indexed placement of each
actual tile uses one of these finitely many possibilities; no coherent
B framing or unique transition rule is required. Lower-chain A placements
have at most two representatives modulo T. Thus the uniform bound C0 is
valid. Continuous upper-boundary phase cannot evade the bounded-path list.

Filtering templates against the fixed carrier and band is T-equivariant.
A B tile has connected interior and cannot cross or touch a separator
inside the A carrier, so every original B is wholly in one open band.
Every retained candidate orbit therefore stays in that band and avoids
A interiors. The original filling uses only these finite candidate orbits.
This is the crucial finite-local-complexity step; merely noting that A
is periodic would not prove it.

## The whole-band SFT and synchronization

Normalize each candidate anchor into one half-open horizontal period slab.
The at-most-C0 binary decisions per slab give a finite alphabet. B diameters
bound all possible overlaps and all contributors to coverage of one slab
to a uniformly bounded number 2q+1 of neighboring slabs. Band geometry,
fixed A carrier, and template admissibility are all T-invariant, so the
same allowed-word condition applies at every slab index.

The coverage predicate is genuinely finite. A period slab of the band has
bounded height; its two polygonal boundary curves have finitely many edges
per period. Only boundary-chain A tiles enter the band, as proved above,
so their fixed obstacle edges also form a finite arrangement in that window.
Together with finitely many candidate polygon edges this partitions a
compact rectangle into finitely many open two-dimensional cells. Requiring
exact coverage where A is absent and no B overlap elsewhere is a finite
Boolean condition. Closed tiles and local finiteness then cover all lower-
dimensional boundaries. Any selected tile violating A-disjointness was
already filtered out. This works even for backtracking separators and
multiple bounded carrier cavities inside one band.

Thus the band language is a one-dimensional shift of finite type with
uniformly bounded alphabet and memory, not a symbolic model assuming
extension. Its actual original filling gives a bi-infinite admissible
sequence. The finite overlap graph therefore has a directed cycle, which
can be chosen simple with length at most a common M. Repeating that cycle
constructs an entire admissible band filling with period mT, 1<=m<=M.
The bound M=(2^C0)^(2q) is a valid generous de Bruijn-state bound after
choosing window length 2q+1.

There are countably many locally finite consecutive bands. Choose a
periodic filling in each and let N=lcm(1,...,M). Every replacement filling
and the A carrier are invariant under the same nonzero NT. Distinct band
fillings have disjoint interiors because all their tiles stay in their
bands. The separators are already covered by the A carrier, so coverage
and disjointness hold globally. No passage from arbitrarily large unrelated
patches to an infinite tiling is used: explicit periodic graph cycles fill
each whole band, and their common-period union fills the plane.

## Final verdict and nonconsequences

The theorem's hypotheses and periodic-escape quantifier are respected at
every step, including reflections, partial initial contacts, possible
monohedral limits, arbitrary phases, variable B orientations, cavity
permutations and infinitely many bands. No unresolved defect found.
The loop restriction is essential to the stated forced-half-turn proof;
the result does not by itself cover two distinct B loop labels or all
six-distinct/four-distinct pairs. It is a restricted family theorem, not
a complete solution of research-problem.md.
