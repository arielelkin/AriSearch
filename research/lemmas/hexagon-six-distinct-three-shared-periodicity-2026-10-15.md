# A six-distinct hexagon with at most three shared side lengths

Date: 2026-10-15. Status: independently hostile-reviewed VALID;
[review](../reviews/hexagon-private-a-three-shared-hostile-2026-10-15.md). No novelty claim. This is a restricted periodic-escape theorem,
not a resolution for arbitrary pairs of convex polygons.

## Statement

Let A and B be convex hexagons with six actual corners and nonempty
interiors. Assume the six numerical side lengths of A are pairwise distinct,
and at most three numerical side lengths occur in both A and B. If the pair
tiles the plane, allowing all isometries and unrestricted contacts, it admits
a doubly periodic tiling.

More precisely, a defect-free mixed tiling exists only if exactly three
lengths are shared, A alternates shared and private lengths, and B has only
those three lengths, each occurring twice. In such a mixed tiling either B
is centrally symmetric, or the entire mixed tiling is geometrically
deterministic and doubly periodic.

Dependencies: the reviewed defect-free limit theorem in
[hexagon-limit-and-periodicity.md](hexagon-limit-and-periodicity.md), its
reviewed monohedral convex-hexagon periodicity input, and the discrete
cocompact planar-group argument in
[hexagon-five-length-intrinsic-determinism.md](hexagon-five-length-intrinsic-determinism.md).
The proof below supplies an UNFRAMED determinism argument; it does not assume
that arbitrary choices of B's symmetric native indices are coherent states.

## 1. Private sides and the exact three-sharing reduction

Work in an everywhere-trivalent whole-native-edge limit tiling. A alone
cannot tile this way: at a trivalent vertex its three ray lengths are
pairwise distinct, and its corner length graph would need a triangle,
whereas A's graph is a simple six-cycle. If only B occurs, the monohedral
hexagon theorem gives the required periodic escape. Hence consider a mixed
limit tiling.

Two consecutive A sides cannot both have lengths private to A. At their
corner, the two neighbors along those sides are also A; hence the vertex
would be AAA, again giving a triangle in A's simple six-cycle. Therefore
private A lengths are isolated and there are at most three. At most three
shared lengths thus means exactly three, with alternating word

    A = (x,u,y,v,z,w),

where x,y,z are shared, u,v,w private, and all six values are different.
Use actual A corner names xu, uy, yv, vz, zw, wx; let their angles be
alpha_xu, alpha_uy, alpha_yv, alpha_vz, alpha_zw, alpha_wx.

At every A corner, its private ray has an A neighbor in the same unique
native side slot. The third tile cannot be A, so every such vertex is AAB.
The two shared rays at that vertex are AB contacts. Consequently every
shared A side has a B neighbor.

At a B corner touching A, both B sides adjacent to that corner meet A.
Following either full side to its other endpoint again gives an AAB vertex;
this propagates around all six sides of that B tile. Thus a B touching A
has all sides AB. There can be no boundary from this mixed component into
B tiles surrounded by B: the full-side adjacency graph is connected, and
all A and B tiles reached from an A have only the neighbors just described.
Every B side is therefore AB; B has no private numerical side length and
all vertices are AAB.

Let N_A(R), N_B(R) count tiles in a radius-R disk, with boundary convention
irrelevant up to O(R). Uniform tile diameters and positive inradii imply
O(R) boundary tiles and total count Theta(R^2). AAB corner counting gives

    6 N_A(R) = 12 N_B(R) + O(R).

If m_x is the number of B sides of length x, AB edge counting gives

    N_A(R) = m_x N_B(R) + O(R),

and likewise for y,z. The first identity and total density imply
N_B(R)=Theta(R^2); division forces m_x=m_y=m_z=2. These are exact integer
multiplicities, not an assumed limiting tile frequency.

## 2. Signed AA seam law

For each unordered pair of distinct shared labels, there is one private A
side between them: u for xy, v for yz, w for zx. An AA contact along such a
private side uses the SAME native slot on both copies. There are precisely
two possible placements with opposite interior half-planes:

* Endpoint exchange: the neighbor is the half-turn about the side midpoint.
  If its adjacent shared labels are r,s, both seam endpoints have a B corner
  with the unordered arm pair rs. Each such B angle is
  2pi minus the sum of A's two endpoint angles on that private side.
* Endpoint preservation: the neighbor is reflection across the side line.
  The two B corners have arms rr and ss respectively. Their angles are
  2pi minus twice the corresponding native A endpoint angle.

This records actual native sides and both endpoints. A numerical ray
triangle alone would not impose the second endpoint condition.

At every B side of length r, its A neighbor uses A's unique r side. The two
ends of this A side meet its two DIFFERENT adjacent private slots. Thus the
private seam choices at consecutive B corners on either end of this side
must be precisely those two different slots. Call this the corona rule.
At an unequal B corner rs, its private slot is uniquely the one between r,s.
At a repeated B corner rr, its private slot is initially one of the two
adjacent to A's r side; the same slot is used by both A copies at that corner.

## 3. The corona rule leaves two words, without enumeration

B is a cyclic word containing each of x,y,z twice.

If B has no consecutive repeated symbol, take any side r. Its predecessor
and successor labels must be different: if both were s, both B endpoints
would require the SAME private slot rs, violating the corona rule. Thus
three consecutive side labels are always distinct. On three symbols this
forces, up to relabeling and reversal,

    B = (x,y,z,x,y,z).

Each of its two xy corners has angle 2pi-alpha_xu-alpha_uy; similarly its
paired yz and zx corners have equal angles. Opposite B sides and opposite
B angles are equal. The exterior turns in each three-corner block sum to
pi, because both blocks are equal and their total is 2pi. Opposite directed
edge vectors are negatives; hence B is centrally symmetric. A convex
centrally symmetric hexagon has a monohedral lattice tiling, supplying the
periodic escape.

Otherwise B contains rr. Each r occurs exactly twice, so the symbols just
before and just after this double block are the other shared symbols. If
these two exterior symbols differed, the corona rule at the two r sides
would force different private slots at the common rr corner, impossible.
They are therefore equal, say s. The remaining two symbols are t,t, so
cyclic rotation and renaming give exactly

    B = (x,x,y,z,z,y).

Here the xx corner uses private w (between x,z), the zz corner also uses w,
and the xy and yz corners use u and v respectively. This conclusion uses
actual A side endpoints; it is stronger than a corner-cover condition.

## 4. Connected private-edge propagation in the double-block case

Here u and v AA seams must exchange endpoints: a reflected u seam would
need B loops xx and yy, and a reflected v seam would need yy and zz, but
there is no yy corner. The w seam must preserve endpoints because an
exchanged seam would need a B corner zx, which is absent. Thus across
A's three private sides the unique neighboring placed A sets are

    u: midpoint half-turn of A;
    v: midpoint half-turn of A;
    w: reflection of A in the side line.

These are full isometries determined by the placed A alone. No reference
indexing of B or global choices between its symmetric side slots are needed.
A has no nonidentity intrinsic symmetry since all six side lengths differ.

The graph on A tiles whose edges are their private AA contacts is connected.
Indeed the full tile adjacency graph is connected. Around any B tile its
six side-neighbor A tiles occur in a cycle: at every B corner, the two A
neighbors meet along the private AA ray at that AAB vertex. Since all
contacts are full sides, each such pair is an edge of the private AA graph.
Any full-adjacency path passing through B can therefore be replaced by an
AA path around that B. There are no BB edges, so this replaces every B
passage and connects any two A tiles in the private-edge graph.

For A tiles U,W, there is a unique placement isometry I carrying U to W,
including native side indices. Each of the three private-side neighbor
maps commutes with this transport: a transported side midpoint half-turn
is the midpoint half-turn of the transported side, and likewise for a
side-line reflection. Induction along the connected private-edge graph
therefore maps every A tile to an A tile. Its image is closed under all
three private neighbors; connectedness makes that image all A tiles.

The complement of the union of all closed A tiles is exactly the union of
B interiors. Every B boundary point belongs to an A because edges are AB
and vertices are AAB. Conversely distinct tile interiors are disjoint.
Local finiteness makes the A union closed, and each B interior is one
connected component of its complement. The isometry I, preserving the
A union, therefore permutes B interiors and their closures. It is a
symmetry of the full tiling.

The tiling symmetry group is transitive on A tiles. There are finitely many
B orbits as well: every B touches an A, and transport that A to a fixed
reference A sends B to one of its three B neighbors. The union K of that
reference A and its three B neighbors is compact and its group translates
cover the plane. Thus the group is cocompact. It is discrete because an
isometry sequence tending to the identity eventually fixes the reference
A as a set, and a nondegenerate polygon has only finitely many intrinsic
symmetries. The reviewed planar group argument in the intrinsic-determinism
dependency shows that a discrete cocompact plane-isometry group contains
a rank-two translation lattice. This mixed tiling is doubly periodic.

The connected-AA propagation was independently suggested by the root agent
while this proof was being written. It avoids any assumption of coherent
indexed states for the reflection-symmetric B polygon.

## Scope, verification, and restart consequence

The proof uses no new solver, coordinates, finite quotient bound, or word
census. All numerical coincidences in B allowed by the stated shared-length
hypothesis are covered; reflected contacts are explicitly included.

If A has six distinct lengths and B at most three, the shared-length
hypothesis is automatic: this whole domain has a periodic escape whenever
tileable. If B has four distinct lengths but only three or fewer are shared,
a mixed defect-free tiling is impossible; a B-only limit still supplies a
periodic escape. Thus the remaining A-six/B-four domain must share ALL FOUR
B lengths. The all-six/all-five results address separate cases. This does
not classify two polygons both having at most five distinct side lengths,
or pentagon-containing pairs.

The fresh hostile review validated the corona rule, both-end private seam
isometries, connectivity of the private AA graph, complement recovery of B,
and the unrestricted limit/monohedral dependencies. Independent native-edge
and90-word corona replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hexagon-private-a-native-edge-independent-2026-10-15.py
