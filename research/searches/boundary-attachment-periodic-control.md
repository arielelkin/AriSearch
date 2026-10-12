# Boundary attachment: exact two-pentagon periodic control

**Status:** falsified as an aperiodic candidate, uniformly for every parameter.
This is a verification control, not a new aperiodic construction or a
promising replacement for Penrose recomposition. It tests the requested
order: exactly two prescribed shapes, varying angle, periodic escape,
then stop before reconstruction.

Let
\[
H=[(0,0),(2,0),(3,1),(2,2),(0,2),(-1,1)],\quad 0<t<\tfrac14,
\]
and define \(p=(\tfrac12-t,0)\), \(q=(\tfrac12+t,2)\). The two
counter-clockwise boundary words are
\[
 A_t=[p,q,(0,2),(-1,1),(0,0)],\qquad
 B_t=[p,(2,0),(3,1),(2,2),q].
\]
These are the intersections of \(H\) with the two half-planes separated by
\(x=\tfrac12+t(y-1)\). Both are strictly convex pentagons throughout the
stated interval; the endpoints stay strictly inside the bottom and top
hexagon sides, and the cut is transverse to both. Their exact areas are
\(2\) and \(4\), so they are distinct congruence classes even when reflections
are allowed. The two cut angles are
\(\pi/2+\arctan t\) and \(\pi/2-\arctan t\); their derivative magnitudes
are \(1/(1+t^2)\). This is actual angle variation after normalization,
not scaling or a rigid motion.

At \(t=0\), the source is the same hexagon split by the vertical segment
\(pq\). Increasing \(t\) transfers two triangles across that old internal
boundary, replacing it by the tilted segment. Thus this is a small
boundary-transfer family with two boundary words by construction. Its
source is periodic, so it is a control only. It does not assert that a
Penrose kite/dart decomposition with the same economy exists.

## Exact mixed periodic escape

The hexagon translates under the lattice
\[
 \Lambda=\mathbb Z(3,1)+\mathbb Z(0,2).
\]
Its area and lattice covolume both equal \(6\). Its bounding box has width
\(4\) and height \(2\). A nonzero lattice translate can therefore overlap
its interior only if \(|3m|<4\) and \(|m+2n|<2\), leaving exactly four
translations \(\pm(3,1)\), \(\pm(3,-1)\). In each case the intersection
is a boundary edge, with zero area. Thus all translates have disjoint
interiors. Equal area and covolume give coverage almost everywhere; the
union is closed and locally finite, so a missing point would imply a
missing open disk and positive missing area. Hence the translates tile
the entire plane.

Subdivide every translated \(H\) with the same \(A_t,B_t\) cut. This is a
plane tiling by the two shapes and is invariant under both lattice
generators for **every** \(t\) in the interval. Partial contacts at opposite
hexagon edges are permitted by the problem definition. The family is
therefore killed by an explicit mixed periodic witness. No reconstruction
or source-recognizability argument is appropriate.

## Replay

[Exact rational verifier](boundary-attachment-periodic-control.py) checks
all turn polynomials using strictly positive Bernstein coefficients on
\([0,1/4]\), constant exact areas, and exact rational clipping for all four
potential lattice overlaps. It writes
[the certificate](../certificates/boundary-attachment-periodic-control.json).

```sh
conda run --no-capture-output -n arisearch python research/searches/boundary-attachment-periodic-control.py --output research/certificates/boundary-attachment-periodic-control.json
```

## Boundaries for the next serious specification

No promising exact two-shape Penrose boundary-attachment family was found
in this preparation pass. A larger graph alphabet is not a substitute for
such a family. Before running another enumeration, prescribe two cyclic
boundary words and impose all face-to-word full-distance congruences jointly,
allowing cyclic shifts and reversal. Establish a nonempty strict convex
parameter interval, check that a normalized corner angle actually varies,
and run periodic escapes before source reconstruction.

Two local obstructions constrain the next topology:

* If two source-interior centres are both joined to two shared boundary
  endpoints, the four segments form a retained quadrilateral whenever they
  embed as a simple plane cycle. With no other interior nodes, the cycle's
  interior contains no vertices that can subdivide it. Erasing source edges
  leaves that bounded face. If it is convex, it gives an immediate
  monohedral periodic escape; otherwise it fails the convexity gate.
* A centre-centre edge and one shared attachment endpoint similarly form a
  retained triangle. To avoid these immediate escapes, a two-centre source
  graph can use at most one common endpoint and cannot join the centres
  when they share an endpoint.
* Adding an external tab while retaining a nonempty boundary subsegment
  of the old straight source edge cannot produce a convex result. A
  boundary line of a convex body supports the body on only one side,
  whereas the old source interior and new tab occupy opposite sides.
  A valid transfer must recut the remaining boundary or erase that entire
  supporting-edge subsegment, rather than merely append a triangle.

Degree-two boundary endpoints must be straight-through in a convex final
partition. This only removes their corners; it does not forbid angle
variation elsewhere. These obstructions do not exclude arbitrary
boundary attachments, more interior centres, or neighbour-aware rules.

## A serious small P2 transfer family: two-donor notch repair is killed

This separate obstruction is relevant to the Penrose source rather than to
the periodic control. It is a derived restriction, not a launched search.
Take a closed source star at the dart reflex vertex: the dart's corner 2
and two kite corners 1 and 3. Keep the dart's other three original corners
\(A,B,D\). Allow it to borrow connected pieces only from those two adjacent
kites, replacing the reflex chain \(B-C-D\); require each remaining donor
kite to be one convex tile. The new notch boundary passes through the interiors of these two donors
and crosses their common seam once; it does not follow their outer
boundaries or absorb any additional native source corner. No extra tile
is inserted, and neither donor is split into several remaining tiles.

In the interior of either convex source kite, its common boundary between
the final convex dart and the convex remaining donor must be a single
straight segment. Indeed, two convex sets with disjoint interiors can be
separated by a line; any positive-length common boundary lies on that line.
The two donor kites have one common source seam. Consequently the new dart
boundary across them consists of at most two segments, \(B-X\) and \(X-D\),
where \(X\) lies on that seam. The new dart has boundary word
\([A,B,X,D]\), with at most four actual corners after removing flat points.
If it is convex and nondegenerate, it is a triangle or quadrilateral and
admits a periodic monohedral tiling. The two-shape pair therefore fails
immediately, regardless of the donation parameter or whether the remaining
kites collapse to one congruence class. A nonconvex or degenerate result
fails the preceding geometry gate.

This kills the small two-donor family throughout its stated domain. It
does not say that every neighbor-dependent Penrose transfer reduces to
this family. To produce a convex dart replacement with at least five
actual corners, a future specification must cross at least three donor
regions, or change another retained source vertex, or absorb another old source corner, or permit a donor to
split into multiple tiles. That larger mechanism still needs two prescribed
final boundary words and a joint congruence proof before it is a viable
next construction family.
