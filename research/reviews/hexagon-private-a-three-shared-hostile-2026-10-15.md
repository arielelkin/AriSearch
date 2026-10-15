# Independent hostile audit: private A sides and exactly three shared lengths

Date: 2026-10-15. Verdict: **VALID for the full periodic-escape theorem** in
`research/lemmas/hexagon-six-distinct-three-shared-periodicity-2026-10-15.md`.
The complete written author artifact was read after independent reconstruction
of the structural and symmetry-group steps. The phrase "B arbitrary" means
arbitrary length multiplicities of a HEXAGON, not an arbitrary side count.
This review includes the independent structural proof and the final complete
corona/periodicity audit below.

## Exact statement

Let T be an edge-to-edge, everywhere-trivalent tiling by genuine compact
convex hexagons A,B, with reflections allowed. Suppose A has six distinct
side lengths and some A occurs. A length private to A occurs in no side
of B. Then each private side slot of A has two neighboring A side slots
whose lengths are shared with B. Thus A has at least three shared lengths.

If precisely three lengths are shared, then:

* A alternates private and shared sides;
* every private side is AA and every shared A side is AB;
* every B side is AB, every vertex has two A tiles and one B;
* B has exactly the three shared lengths, each occurring twice;
* for centered radius-R windows, NA(R)=2NB(R)+O(R), and each type has
  a uniformly positive quadratic lower count as R tends to infinity.

In particular a mixed trivalent tiling with A present and B having exactly
four distinct side lengths cannot have at most three shared lengths. If
A disappears after applying the separate reviewed defect-free limit,
B alone tiles; the periodic monohedral-hexagon escape is a named existing
dependency, not a consequence of these new incidence statements alone.

## Both native-edge endpoint maps, including reflections

Choose an A-private side of length u, with neighboring lengths v,w in the
A cycle. Across it lies another A using its unique native u side. There
are exactly two native endpoint correspondences. If endpoints interchange,
the two A corners at each endpoint have non-u arms v and w. The third
corner must join numerical lengths v,w. It cannot be an A corner, since
v,w are distance two apart around A's six-cycle. Therefore it is a B
corner, and v,w are both shared.

If endpoints preserve their actual A slot indices, one endpoint has two
copies of the A corner with arms u,v, and its third corner has arms v,v.
The other endpoint similarly forces w,w. Neither third corner can belong
to A because its side lengths are distinct, so both are B corners. Again
v,w are shared. Endpoint-preserving placement is possible in principle
through a reflected neighbor and must not be discarded. No assumption on
B's corner graph, loop absence, or side multiplicities was used.

Thus private A slots are isolated and at most three in a six-cycle. If
there are exactly three shared slots, the three private slots alternate
with them. Every A corner is incident to one private side; its private
mate is A and its remaining corner is B by the preceding argument.
Therefore every vertex incident to A is AAB. Across the other, shared
A side at that endpoint lies B, and full-edge matching makes the entire
shared side AB. This is a statement about actual copies and native sides,
not a labeling of abstract graph triangles.

## Propagation around each actual B

A B adjacent to A has, at either endpoint of their common side, an AAB
star. Both incident sides of that B at the vertex are therefore AB.
Propagate around its six native vertices: all six B sides are AB. The
collection of all A tiles and their adjacent B tiles is closed under
full-side adjacency. Such adjacency is connected: local finiteness follows
from contained-disk packing, and a generic compact path connecting tile
interiors crosses finitely many sides while avoiding native vertices.
Since this collection is nonempty, it is the entire tiling. Every B side
is AB and every vertex is AAB. No positive-density assumption was used
to justify this propagation.

Every B length is one of the three shared A values. Every one of the
three values occurs in B, because each shared A side has a full B mate.
This gives exactly three distinct lengths in B; their multiplicities
require the incidence estimate below.

## Precise O(R) bound and positive densities

Fix an interior anchor in each reference shape, choose a common contained
disk radius rho>0, and let D bound all tile diameters and anchor-to-tile
point distances. Count tiles with anchors in the radius-R disk. A full
side adjacency whose two anchors are on opposite sides of the window
boundary has both anchors in the annulus of width at most D (or any fixed
larger multiple of D). The contained disks of such tiles have disjoint
interiors, lie in a fixed-width enlarged annulus, and each has area
pi*rho^2. Hence there are O(R) boundary tiles and O(R) boundary adjacency
incidences, uniformly in the window center. The constants depend only on
the two fixed shapes.

Every A has three AB sides and every B has six. Counting AB incidences
from their two ends gives

    3 NA(R) - 6 NB(R) = O(R).

The tiles covering the radius-(R-D) disk have anchors inside radius R.
If M is the larger tile area, NA(R)+NB(R)>=pi*(R-D)^2/M. Together with
the incidence estimate this implies NB(R)>=c R^2-O(R) and NA(R)>=2c R^2-O(R)
for some c>0, uniformly in window center. In particular neither type can
have zero density in this branch; no unspecified limiting frequency or
unique ergodicity is required.

For each shared length x let mx be its number of native B side occurrences.
Each A has exactly one x side, and every B x side has an A mate. Thus

    NA(R) - mx NB(R) = O(R).

Combining with NA(R)-2NB(R)=O(R) yields (mx-2)NB(R)=O(R). The uniform
quadratic lower bound forces mx=2 exactly. This proves the multiplicity
claim and the stated NA=2NB asymptotics. The proof does not assume that
a periodic quotient, invariant measure, or individual tile frequency
already exists.

## Independent finite check and limitations

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hexagon-private-a-native-edge-independent-2026-10-15.py

The checker imports only the standard library. It explicitly reconstructs
both endpoint maps of an AA private edge, checks their necessary B corner
incidences on all 729 words over compressed symbols {v,w,other}, enumerates
the two alternating shared-slot subsets of size three, and verifies the
unique positive equal-multiplicity solution (2,2,2). There are 90 indexed
B words with these multiplicities. The finite check is not a plane tiling
search or a replacement for the written unbounded density argument.

No substantive defect found. The mixed structural theorem is valid. A
statement for nonhexagonal B would need to change the side count and
multiplicity conclusions; it is not asserted here. The result does not give a universal arbitrary-pair impossibility theorem.
The final artifact-specific audit below settles the A-six/at-most-three-
shared hexagon branch; novelty remains a separate obligation.


## Additional audited bridge: connected private-AA adjacency

**VALID conditional lemma.** In the exact-three-shared branch above, suppose
that for each of A's three private side slots, all its AA contacts use one
fixed native endpoint correspondence (swap or preserve). Then the tiling
has two linearly independent translational periods. B need not have a
canonical indexed placement or be asymmetric.

At a B vertex the two adjacent A neighbors share a full private AA side.
Going around a B therefore places all its A neighbors in the same private-
AA adjacency component. Any full-side path between A tiles can replace
its A-B-A passages by these AA paths around B. Hence the private-AA graph
on all A tiles is connected.

For two indexed A placements gU,gW the plane isometry F=gW*gU^-1 maps U
to W. Across a private side, its fixed endpoint correspondence plus
opposite interiors gives a unique full relative isometry, either the
half-turn about the side midpoint or reflection in its supporting line.
Thus F maps neighbors to neighbors and propagates through the connected
private-AA graph, giving F(all A tiles) contained in all A tiles. Apply
exactly the same argument to F^-1, which also maps one A tile to another,
to obtain equality. This inverse step is needed because the A collection
alone does not cover the plane.

Let X be the union of the closed A tiles. Local finiteness makes X closed.
Every B boundary edge and vertex belongs to X, because all B edges are AB
and every vertex is AAB. Therefore the connected components of the open
complement of X are exactly the individual B interiors. F preserves X,
so it permutes these components and their closures, and preserves the
entire tiling. The resulting symmetry group is A-transitive, discrete by
the usual interior-point/finite-polygon-symmetry argument, and cocompact
because every point of every B lies at a uniformly bounded distance from
an adjacent A. The elementary discrete cocompact plane-isometry argument
in the reviewed intrinsic-determinism lemma gives a rank-two translation
lattice. No symmetry-breaking indexing of B or bounded quotient guess is
required.

The finite checker additionally enumerates all 90 indexed three-length B
words and both endpoint modes for each private A pair. This necessary
local mode test retains five unlabeled bracelets:

    001122 (12 words), 001212 (36), 001221 (18),
    010212 (18), 012012 (6).

Only 001122 has an ambiguous private-side endpoint mode. Every other
retained bracelet has a fixed mode for each private A side and therefore
falls under the conditional lemma, whether or not it is geometrically
realizable. The test is deliberately only necessary; for example, the
sole loop in 001212 cannot occur once all modes are fixed half-turns.
Discarding additional impossible configurations is unnecessary for the
periodicity implication. The 001122 branch remains outside this fixed-map bridge alone; the
stronger corona rule in the final author proof eliminates it, as checked
independently below. These five bracelets are a deliberately weak diagnostic
gate, not the final list of geometrically possible B words.


## Final complete author-artifact audit: corona rule and periodic escape

The final author theorem asserts: a tileable convex hexagon pair with A
six-distinct and at most three numerical side lengths shared between A and
B admits a doubly periodic tiling. **VALID.** Its first section correctly
handles A disappearing in the defect-free limit by the reviewed monohedral
hexagon periodicity theorem. If A occurs, its private-side argument and
mixed propagation agree with the independently reconstructed proof above.
Its shorter isolation proof is also valid: adjacent private A arms would
force an AAA star, impossible for A's distinct-length six-cycle.

The genuinely stronger new input is the corona rule. Each B side of length
r has as full mate A's unique native r slot. Its two endpoints are adjacent
to A's two DIFFERENT private side slots. Thus, at consecutive B corners on
that side, the AA seam slots must be exactly those two different slots.
At an unequal B corner rs, the AA private side is the unique one between
r,s in A. At a loop rr, both neighboring A copies use the SAME private slot
because their common AA edge has a private length unique in A. Its two
initial possibilities are the two private slots adjacent to A's r side.
This derivation uses actual native endpoints and excludes neither reflected
A neighbors nor equal B lengths.

The author's resulting two-word classification is correct. Without a loop,
a side whose predecessor and successor were equal would use the same
private slot at both endpoints. Three consecutive symbols must therefore
be distinct, forcing xyzxyz. With a double block rr, the outside symbols
cannot differ: if they were s and t, the two r sides would require opposite
choices rs and rt at their common loop, impossible. They are both s;
the two remaining t occurrences are adjacent, giving xxy zzy up to naming
and cyclic reading.

The independent checker tests this rule on ALL 90 indexed words with
multiplicities (2,2,2), enumerating every loop's native private-slot choice.
It retains exactly the bracelets 001221 (18 indexed words) and 012012
(6 indexed words). Each retained word has exactly one corona assignment.
In particular 001122 is eliminated rather than left as a branching case.

For xyzxyz, every private AA map exchanges endpoints; each numerical B
corner pair occurs at both endpoints of its corresponding private A seam.
The two copies of each B angle are therefore equal. The opposite B sides
also have equal lengths. The exterior-turn sequence repeats after three
corners, so its three-term sum is pi; opposite directed side vectors are
negatives. B is centrally symmetric and has the reviewed lattice tiling.

For xxy zzy, the seam laws force two private A maps to be midpoint
half-turns (the missing yy loop forbids reflection) and the third to be
side-line reflection (the absent zx corner forbids exchange). Thus each
private side has a fixed complete relative A isometry. The connected-AA
symmetry argument audited above applies. The author's surjectivity proof
is valid directly: the transported A collection is nonempty and closed
under all three target private-neighbor operations, so connectedness of
the target AA graph makes it all A tiles. The alternative inverse-map
argument above gives the same conclusion. Recovery of B as complement
components and the discrete cocompact group proof are sound.

No angle-only equality is mistaken for actual native adjacency, no
unbounded object is inferred from a finite patch, and no coherent framing
of the possibly symmetric B polygon is assumed. All rotations and
reflections are included. The full A-six/B-at-most-three-shared theorem,
its B-at-most-three-distinct consequence, and its exclusion of mixed
A-six/B-four tilings with at most three shared lengths are valid. No
substantive defect or unresolved qualification remains within that scope.
