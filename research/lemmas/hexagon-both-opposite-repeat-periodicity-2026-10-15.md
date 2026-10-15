# Two hexagons with common five colors and opposite repeated sides

Date:2026-10-15. Status: independently hostile-reviewed VALID and exactly
certified; [fresh review](../reviews/hexagon-both-opposite-repeat-hostile-2026-10-15.md). This is a restricted periodic-escape theorem.

## Theorem

Let A,B be genuine convex hexagons whose side lengths take the SAME five
numerical values. Each value occurs once except for one doubled value per
shape. If both doubled pairs are opposite sides, any plane tiling by these
shapes, with reflections and partial contacts allowed, implies a doubly
periodic tiling. The doubled numerical values may agree or differ.

The stronger formal source statement holds with five common auxiliary
colors: same-colored sides have equal physical lengths, different colors
may physically coincide, and an indexed full-side trivalent color-matching
plane source exists. Then the unmarked shapes have a doubly periodic escape.
These colors are only a proof device. No target placement rules are imposed.
The numerical statement follows from the reviewed
[defect-free limit theorem](hexagon-limit-and-periodicity.md).

## Monohedral escape and the complete word domain

Write A=(0,1,2,0,3,4). Every B has a reading

    B=(p,q0,q1,p,q2,q3),

where p ranges over the five values and q over24 permutations of the other
four. Thus120 words exhaust the domain without any quotient. Corner i is
between native sides i and i+1, with all indices modulo6.

Adjacent colors differ, so each trivalent source vertex has three distinct
ray colors. Its native corners are the three edges of a color triangle.
The corner graph of EITHER shape with opposite repeated sides consists of
two triangles meeting at its repeated color. A pure star therefore uses
native corners {0,1,2} or {3,4,5}. Either triple having angle sum2pi forces
the other, since the six angles sum4pi.

In that case the same shape alone admits an explicit periodic escape.
Take two equally oriented copies. Within each face pair side0 to side3;
pair each remaining side1,2,4,5 to the same native side of the other face.
All pairings reverse boundary endpoints and match lengths. The quotient
is connected, orientable, and has four circular triple corner links, twice
each of {0,1,2} and {3,4,5}. Thus V4,E6,F2 and every cone sum is2pi. It is
a compact flat torus whose universal cover develops to the Euclidean plane.
The lifted faces tile with two independent deck translations. This also
handles every source using only one species.

We may henceforth assume BOTH shapes occur and NO actual source star is
pure. Each of the twelve native corners then occurs in a mixed star.
Deleting all pure stars from the possible atlas is valid under this case
assumption, including those that might be metrically legal but unused.

## Complete mixed native gate and four exceptional word classes

The [standalone exact producer](../searches/hexagon-both-opposite-repeat-gate-2026-10-15.py)
and [retained certificate](../certificates/hexagon-both-opposite-repeat-gate-2026-10-15.json)
list every native star and every complete endpoint obligation. For each
of120 words, form all actual corner triples realizing color triangles,
remove pure triples, and prune any star having a full-side far-end pair
contained in no remaining star. Iterate to a fixed point. Every actual
occurring star survives this operation inductively. Both occurrences of
repeated colors and all three rays of every star are checked.

Connect native side slots meeting on each ray of a remaining star. The
actual seam graph is a subgraph; its component partition refines this
full possible graph partition. Components only join slots of the same
original color. If one shape's doubled slots remain disconnected, all
six of its slots lie in distinct actual components. Recolor those actual
components. The other shape retains at least five colors because this is
a refinement of its original five. The reviewed
[six/five formal-color theorem](hexagon-six-five-formal-color-periodic-escape-2026-10-15.md)
therefore supplies a doubly periodic unmarked escape for the same metrics.

The exact120-word gate yields80 without a twelve-corner cover,24 with
this six-color escape, and16 remaining words. Every remaining word has
an explicit common color bijection and independent dihedral readings of
A,B carrying it to exactly one of four representatives:

    B1=(0,1,2,0,3,4), B2=(0,1,2,0,4,3),
    B3=(0,1,3,0,2,4), B4=(0,1,4,0,3,2).

Each represents four raw words. The retained maps are verified pointwise
on both side cycles. All four have the SAME doubled color; the different-
doubled-value case is already disposed of by the preceding branches.

## All actual supports and positive finite witnesses

For each representative exhaust every subset of its fixed mixed atlas,
keeping those covering all twelve native corners and internally meeting
every exact far-end demand. The four support counts are141,1,27,57, total226.
Actual occurring-star sets EQUAL one of these supports. The argument does
not replace actual equality by containment of a minimal support.

For B1,B3,B4 form positive torus witnesses using two indexed A and two
indexed B faces. Choose all8 relative orientations modulo global reversal.
The side-color classes have sizes8,4,4,4,4; all within-color perfect
matchings give105*3^4 choices. Hence each witness atlas has68040 gluings.
For each, reverse boundary endpoints of paired sides, check connectivity,
orientability, circular three-corner links and Euler characteristic zero.
Retain actual connected trivalent torus gluings, grouping only their native
angle-equation supports. No larger quotient is searched or assumed complete.

A retained positive witness is valid for original metrics whenever its
vertex sums are2pi: same-colored sides have equal lengths, circular links
exclude surface singularities other than cone angles, and the equations
remove those cones. The resulting compact oriented flat torus has complete
Euclidean universal cover, tiled by the lifted polygon faces with disjoint
interiors. Its deck lattice gives two independent translations. No embedded
source patch resembling the quotient is required.

Normalize source angles by pi. For each actual source support, impose total4
for A and B and total2 for each of its star triples. The certificate chooses
an actual positive torus whenever all of its target star equations are exact
rational combinations of these source equations. Coverage counts are

    B1:139/141, B2:0/1 (no torus atlas needed),
    B3:25/27, B4:57/57.

All884 rational weighted-row identities are retained for direct exact
checking. This proves periodic escape on221 supports; lack of a bounded
witness is never interpreted as an impossibility or aperiodicity claim.
The remaining FIVE exact supports are handled next by intrinsic isometries.

## One support with every native corner unique

The sole B2 support is

    {(0,2,7),(1,6,8),(3,5,10),(4,9,11)}.

It partitions all twelve corners. A host native endpoint has one unique
star; its side color selects one guest corner and one native guest side.
Matching ordered side endpoints and choosing the opposite interior
half-plane determines the complete indexed relative isometry. This holds
on every side and with all physical symmetries allowed. Connected full-side
adjacency propagates any indexed same-type tile map to a symmetry of the
whole framed tiling. The symmetry group is discrete and cocompact, so the
reviewed planar crystallographic argument gives two independent translations.
This is the same intrinsic frame mechanism proved in the
[changed-word lemma](hexagon-shared-repeat-changed-family-periodicity-2026-10-15.md).

## Four supports with an alternating-side state

For B1 the two uncovered supports are

    T1={(0,1,8),(0,2,7),(1,2,6),(3,4,11),(3,5,10),(4,5,9)},
    T2={(0,7,8),(1,6,8),(2,6,7),(3,10,11),(4,9,11),(5,9,10)}.

For B3 they are

    U1={(0,1,9),(0,3,7),(1,2,6),(2,5,10),(3,4,11),(4,5,8)},
    U2={(0,7,8),(1,6,9),(2,10,11),(3,6,7),(4,8,11),(5,9,10)}.

In T1,U1 all vertices are AAB and every B native corner appears in exactly
one star. In T2,U2 interchange species. It suffices to prove the AAB case.

A placed indexed B has a uniquely prescribed A neighbor on every side:
its unique endpoint star and the side color fix the actual guest corner,
guest slot and both ordered endpoints, with the opposite interior selecting
the whole plane isometry. At each A vertex exactly ONE of its two incident
sides meets B, since every star is AAB. Thus the B-neighbor sides of A are
exactly its three alternating sides. Carry their even/odd PARITY as an
additional finite state of A. A known incoming B neighbor fixes that state.
An A frame ALONE need not fix this state; the proof does not assume it does.

For each of these four actual supports the certificate explicitly checks
that whenever an A side meets B, its guest B corner and side are unique.
It checks BOTH host endpoints, including agreement on the guest native
side and distinct guest endpoint corners. Thus an indexed A frame plus
its parity determines all three B-neighbor placements. B frames determine
their A-neighbor frames AND their parity via the incoming side. Every map
in this enriched AB propagation is therefore fixed by its finite state.

The graph using ONLY AB adjacencies is connected. Indeed the full-side
graph is connected by local finiteness and a generic compact crossing path.
Any AA edge on such a path can be bypassed by two AB edges: at either
endpoint its third incident tile is B and has a full side against each A.
There are no BB edges. Replacing every AA step gives an AB path.

Consequently an isometry between ANY two indexed B occurrences propagates
through this connected AB graph, transporting every A frame with its parity
and every B frame. It preserves the whole framed tiling. The resulting
symmetry group is discrete; it is cocompact because it is transitive on B
and every A belongs to the finite six-A neighbor corona of some B. In
particular it has finitely many tile orbits (at most seven suffices).
The planar crystallographic argument again supplies a rank-two translation
lattice. This closes all four supports, and hence the theorem. QED.

## Exact scope, replay and review obligations

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-both-opposite-repeat-gate-2026-10-15.py

Default stdout is the complete deterministic JSON; --output PATH explicitly
retains it. Domains:120 raw words, all subsets of the four fixed atlases,
and three fixed68040-gluing positive atlases. No randomness, timeout or
parameter sampling is used. The computation uses integers and Fraction.
The [independent no-import verifier](../reviews/hexagon-both-opposite-repeat-independent-2026-10-15.py)
reconstructs the complete gates, explicit word
bijections, all226 support sets, positive surface links and884 weighted
identities and actual indexed endpoint maps. Every check passed; the fresh
whole-proof audit also confirmed the enriched parity-state propagation proof.
No geometric existence is asserted for abstract source supports.

Together with the reviewed
[both-separation-two theorem](hexagon-different-repeat-separation-two-periodicity-2026-10-15.md)
and [mixed-separation theorem](hexagon-mixed-separation-repeat-periodicity-2026-10-15.md),
this proves periodic escape for common-five-length genuine hexagon pairs
whose repeated sides are nonadjacent in BOTH shapes. Adjacent repeated
sides, other shared-length sets, lower length multiplicities and all
pentagon-containing pairs are outside this result. The main unrestricted
problem is unresolved.
