# Six auxiliary side colors force an unmarked hexagon periodic escape

Date:2026-10-15. Status: independently hostile-reviewed VALID;
[review](../reviews/hexagon-six-colors-arbitrary-partner-hostile-2026-10-15.md).
This extends the reviewed A6/B>=5 color theorem to an arbitrary partner.
It is a restricted source theorem, not a complete two-polygon result.

## Statement

Let A,B be genuine convex hexagons, with indexed native sides carrying
auxiliary colors. Suppose A has six distinct colors; B has arbitrary color
multiplicities. Every occurrence carries an indexed reference isometry.
Same-colored native sides have equal physical lengths, but DIFFERENT colors
may have equal physical lengths. Suppose there exists a full-side,
everywhere-trivalent plane tiling T matching equal colors across seams.
Then the underlying UNMARKED pair admits a tiling with a nonzero translation.

The source hypothesis is full-side; we do not pass a colored partial-contact
tiling through an uncolored limit. Reflections and physically symmetric
polygons are permitted. The target has no imposed color rules.

## Exhaustive reduction and reviewed five-color branch

If either unmarked member tiles alone, its reviewed monohedral convex-hexagon
periodic escape proves the conclusion. Hence assume neither tiles alone.
Both types occur in T. In particular every native corner occurs, since each
placed copy includes every indexed corner. Let b be B's number of colors,
and k the number of colors shared between A and B.

If b>=5, apply the independently reviewed
[six-color/five-color source theorem](hexagon-six-five-formal-color-periodic-escape-2026-10-15.md).
It explicitly handles accidental physical equalities and reference symmetries.
Suppose henceforth b<=4. If k<=3 use Section1 below. Otherwise b=k=4;
B's four color multiplicities are either(2,2,1,1) or(3,1,1,1), covered by
Sections2 and3. These are all cases.

## 1. At most three shared colors

Audit the [three-sharing proof](hexagon-six-distinct-three-shared-periodicity-2026-10-15.md)
using COLORS in every incidence and native-arm statement. A's color graph
is a simple six-cycle and contains no triangle. At an A corner both private
colors would force an AAA star. Its three rays would have distinct colors
because A has no equal adjacent colors, contradicting the triangle-free
cycle. Hence private A colors are isolated. With at most three shared
colors, exactly three are shared and A alternates

    (x,u,y,v,z,w),

where u,v,w are private. Across each private side stands A in that SAME
native side slot, because A colors are unique. At each A corner the third
tile must be B: an AAA color triangle is impossible. Thus each A corner
is AAB and each shared A side is AB. Propagating around a B touching A
shows all its sides are AB; connected full-side adjacency propagates this
to all B occurrences. All vertices are AAB.

The original proof's boundary incidence counts are now COLOR counts:
6N_A=12N_B+O(R), N_A=m_x N_B+O(R), and similarly for y,z. Physical areas
and inradii provide the same packing and boundary bounds. Hence B has only
x,y,z and each occurs twice. No numerical inequality is used here.

Across private u (between x,y), an indexed endpoint-exchanging AA match
is its midpoint half-turn; an endpoint-preserving match is its side-line
reflection. The third B corner(s) must respectively have color arms xy,
or xx and yy at the two endpoints. The corresponding angle formulas in
the reviewed proof remain true. At a B side colored r, its A neighbor uses
A's unique r slot; its two endpoint private slots differ. This is the same
corona rule, now determined by colors rather than metric inequality.
It leaves only B=(x,y,z,x,y,z) or B=(x,x,y,z,z,y), by the complete direct
word argument of Sections2–3 of that proof.

For the first word, opposite B angles and side lengths are equal: equal
colors prescribe equal lengths and the private-AA endpoint angle formulas
prescribe equal angles. The exterior-turn argument makes B centrally
symmetric, and its unmarked lattice tiling is a periodic escape.

For the second word, private u,v neighbors must be midpoint half-turns
and private w neighbors side-line reflections, because missing COLOR loops
exclude the other endpoint maps. These determine COMPLETE INDEXED relative
maps of A. Physical symmetries cause no ambiguity: the actual host frame,
unique native private color, ordered endpoints and opposite interior
half-plane determine the neighbor frame, as in the reviewed color theorem.
The private-AA graph is connected: the six A neighbors around each B form
an AA cycle, so full-adjacency paths through B can be bypassed.

Transport between any two indexed A occurrences commutes with these three
native private-neighbor maps. It therefore maps the indexed A carrier onto
itself, by connectedness and closure under all three neighbor operations.
This argument does not require the PHYSICAL A to be asymmetric. The
complement of its closed union is exactly the union of B interiors, since
all B edges are AB and all vertices AAB. Transport consequently permutes
unmarked B tiles. The resulting group is transitive on A, has finitely
many B orbits, and is discrete and cocompact; finite physical polygon
symmetry suffices for discreteness. The reviewed planar group argument
gives a rank-two translation lattice. Section1 is proved.

## 2. Four shared B colors of multiplicities(2,2,1,1)

Use the exact finite lemma of the independently reviewed
[double-pair proof](hexagon-six-four-double-pair-periodicity-2026-10-15.md).
Normalize A's six COLORS to0,...,5. Its two private colors are nonadjacent,
since adjacent private colors would give an impossible AAA color triangle.
Their possible separation is therefore two or three. B uses the other
four colors, twice twice once once. This is precisely the retained2160word
finite domain, without any change of inputs.

Its atlas uses actual native indices and all simultaneous arm microstates,
including repeated ray colors. Every test is color equality; physical
inequality between different labels is never used. Thus the actual support
of T is one of its93closed corner covers. Seventy-one directly contain a
formal four-triangle ring; twenty-two have four ring angle equations derived
by88retained rational row identities from the actual stars and polygon
angle totals. All target ring side matches have equal COLORS and hence
physical lengths. The reviewed formal-ring flat-torus bridge therefore
works unchanged and gives a doubly periodic unmarked witness. This is a
proof interpretation of the existing narrow certificate, not an extra
numerical classification or an unproved extension principle.

## 3. Four shared B colors of multiplicities(3,1,1,1)

Here exactly two A colors u,v are private, and B can have equal adjacent
colors at ONLY ONE color. Across private u, the neighbor A uses the same
native slot. The two complete indexed opposite-interior maps are the
midpoint half-turn and the side-line reflection. For the reflection, the
third corners at its endpoints would have arm colors xx and yy, where
x,y are the different COLORS flanking u in A. These cannot be A corners,
and would require loops in B at TWO different colors. Impossible. Thus
both private neighbors are forced midpoint half-turns.

This is precisely the geometric hypothesis needed by the reviewed
[periodic-chain proof](periodic-private-aa-chain-escape-2026-10-15.md).
The remainder of that proof uses no numerical distinction between u and v:
its nonzero vector2(m_v-m_u) follows because midpoints of two different
native edges of a genuine convex polygon are different. The actual indexed
half-turn rules make every private-AA component a two-tile periodic chain.
Their separator curves are proper, disjoint and strip-bounded, so all axes
are parallel and their common period length is the fixed|2(m_v-m_u)|.

Uniform unavoidability of A applies to the UNMARKED shapes: B was assumed
not to tile alone at the beginning. It bounds consecutive separator bands.
Inradius packing and a bounded full-side path to a fixed lower chain give
a finite set of complete B candidate placements modulo the common period.
All physical side coincidences merely enlarge the finite one-step relative
map set; finiteness and the bounded path argument survive. A need not be
physically asymmetric: carry its source indexed frame along every chain;
the fixed midpoint half-turns prescribe the two indexed placements per
period. This is all the framing the finite candidate derivation needs.

The original finite-window no-overlap/coverage shift then produces a
periodic filling in each band with a uniform period bound. Synchronizing
these bounds gives one nonzero translation of the unmarked completed tiling.
The final filling may ignore the auxiliary colors, which is permitted by
the target. Its full geometric correctness is the already reviewed chain
proof; no new strip finite-model assumption is made. Section3 is proved,
and the exhaustive cases prove the theorem. QED.

## Actual-seam necessity

For any indexed full-side trivalent unmarked tiling, let E be the connected
components of the graph on its twelve native side slots generated by ALL
actually occurring full seam types. Each class has one physical length.
Give every slot its E-class as color. Then the source hypothesis holds.
If no class contains two A slots, A has six colors and the theorem gives
an unmarked periodic escape, irrespective of B's colors. Exchange A/B
for the symmetric statement.

Thus a hypothetical aperiodic two-hexagon pair must in EVERY indexed
defect-free tiling connect two DIFFERENT native slots of A by actually
occurring seam types, and likewise two native slots of B. Connected slots
necessarily have equal physical lengths. This strengthens the reviewed
necessary numerical repetition to a necessary ACTUAL contact connection.
It neither asserts existence nor classifies the residual connected cases.
Pentagon-containing pairs are outside the theorem. No unrestricted
impossibility claim follows.

## Dependencies and review boundary

The proof uses the reviewed A6/B>=5 color theorem, the three-sharing corona
proof with its framing replacement explicitly given above, the unchanged
narrow double-pair certificate and rational-row checker, the reviewed chain
geometry, and the reviewed uniform-unavoidability and defect-free-limit
lemmas. No new finite enumeration or solver result is claimed. Fresh review
must check each numerical-inequality replacement, physical reference
symmetry, private-color versus private-length distinction, and the fact
that the final unmarked strip completion need not preserve colors.
