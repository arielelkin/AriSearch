# One boundary-junction cycle for the two-parent P5/Q7 seed

Date: 2026-10-19. Status: **proved obstruction; [independent Sol hostile review](../reviews/q7-five-pentagon-three-heptagon-hostile-sol-2026-10-19.md) VALID**.
No coordinate search or map enumeration was run. The two-parent incidence pair
in this stated class is impossible, because its Q parent cannot exist.
The stronger matrix obstruction derived below is also pending independent review.

## Fixed question and conventions

The columns of M=[[7,5],[2,3]] prescribe 7P+2Q in P and 5P+3Q in Q.
All children and parents are genuine convex native polygons. Use the seam
conventions of `research/lemmas/six-child-topology-universal-wheel.md`:
I internal nodes; B seam nodes inside parent sides; J parent corners carrying
seams; E seam edges; D total seam-degree excess above internal degree three
and active boundary degree one; H flat child-angle incidences. The changed
allocations are P:(B,J,D,H)=(2,1,0,0), Q:(1,1,0,0).
Thus the one J node is a seam endpoint at a genuine parent corner, not an
extra high-degree junction. No assumption of one outer arc per child is
needed for the Q obstruction below.

## Exact disk and dual constraints

Euler and the seam-degree identity give

    E=I+F-1,
    I+B+J+D=2F-2,
    sum(6-ni)=6-p+B+2J+2D+H.

Consequently the P disk has F=9,I=13,E=21 and three active boundary nodes;
the Q disk has F=8,I=12,E=19 and two active boundary nodes. All internal
seam nodes are trivalent; every active boundary node has one seam edge.
Since H=0, every child incidence at these nodes is a native corner. At a
B node the two angles sum to pi; at the J node they sum to the corresponding
parent corner angle; each of the other p-1 parent corners lies in a single
child. Each internal node has three angles summing to 2pi. Total native-side
counts are 49 for P and 46 for Q. The summed-angle checks are respectively
31pi=26pi+3pi+2pi and 30pi=24pi+5pi+pi. These necessary totals alone do not
supply a map.

A boundary label can change only at an active node. The two sectors at each
active node belong to distinct children: otherwise that convex child would
have interior on both sides of its emanating seam. Thus Q's two cyclic open
boundary arcs have two distinct labels A,B, each occurring once. In P's
three-arc boundary cycle each consecutive pair must likewise be distinct,
forcing three distinct outer children. In particular, even allowing repeated
boundary contacts initially, these budgets force exactly three outer children
for P and exactly two for Q; all other children have no positive boundary arc.

For P, positive-length child contacts give a simple dual triangulated disk
with three boundary vertices and six interior vertices. It has 21 edges and
13 triangles. Interior child dual degrees must equal their native side
counts, hence be at least five. If eII,eIB,eBB count interior-interior,
interior-boundary, and boundary-boundary dual edges, then

    30 <= 2eII+eIB = eII+21-eBB,
    eBB>=3, eII<=3*6-6=12.

Therefore eII=12,eBB=3,eIB=6 and every interior child would have degree
exactly five; in particular all Q children would have to be outer. The induced six-vertex interior graph is maximal planar. In its inherited
embedding its outer face is a triangle and its other three vertices are
strictly inside that triangle. None can connect to a boundary child without
crossing that triangle, so each of these three trapped vertices must obtain
its required degree five from all five other interior vertices. In particular
they are each adjacent to all three vertices of the outer triangle, yielding
a K3,3 subgraph, impossible in a planar graph. Thus P also fails in this
class, independently of the Q obstruction.
For Q the analogous boundary is a digon: its two active nodes would give two
dual boundary edges between the same two outer children. This violates the
single-segment intersection condition for convex children, as the direct
geometric proof below makes independent of dual conventions.

## Two-active-node obstruction

**Lemma.** A finite partition of a convex polygon into convex positive-area
children, with exactly two active boundary seam nodes, has exactly two children.

**Proof.** Let the two nodes be x,y. Deleting them leaves two connected open
parent-boundary arcs. The incident child is locally constant on each arc,
so each whole arc belongs to one child, respectively A and B, by closure.
These labels are distinct by the seam-sector observation above.
The line through x,y divides the convex parent C into two closed caps.
Each cap is the convex hull of its boundary arc together with x,y: intersect
C with the appropriate closed half-plane, whose boundary is that arc and
the chord [x,y]. This elementary convex-polygon identity also holds when
x,y lie on the same supporting side, with one cap degenerate. Since A,B
are closed and convex, they contain their respective caps. The caps cover
C. Thus A union B=C, leaving no positive-area interior for any other child.
If a cap is degenerate, the other child contains all C and the partition
is already nontrivially impossible. Otherwise exactly A,B remain. QED.

The target Q parent has eight positive-area children but B+J=2. The lemma
contradicts this before native-role, angle, length, or coordinate assignment.
It excludes the entire stated J=1,D=H=0 two-parent class, including any
initial permission for multiple outer arcs or isolated point contacts.

Equivalently, the augmented dual with exterior vertex O has degree two at O.
The two active nodes demand two triangular faces OAB sharing the same three
edges. Convexity permits at most one A-B contact segment. Those two faces
then exhaust the sphere around this triangle, leaving no place for the six
other children. The cap proof avoids relying on this dual interpretation.

## Scope and stop

This is one changed incidence cycle on the same matrix. No child incidence
pair, boundary-word witness, angle system, or coordinates survive, and no
solver was invoked. The Q obstruction suffices; the P obstruction applies only to its stated three-outer-child simple-dual
class. The next meaningful restart
must change Q's allocation so that B+J>=3 (or change another hypothesis).
For Q's defect budget three, B+2J+2D+H=3 and B+J>=3 force
(B,J,D,H)=(3,0,0,0). Hence **any convex Q dissection with this inventory**
actually has that saturated allocation. Here those formerly chosen dual hypotheses can themselves be derived.

## Stronger consequence: the Q inventory is impossible

This section is independently reviewed VALID; the standalone [lemma](../lemmas/heptagon-five-pentagons-three-heptagons-obstruction-2026-10-19.md) contains the complete proof. Suppose any convex
heptagon is dissected into five genuine pentagons and three genuine heptagons,
allowing partial contacts and arbitrary metrics. The general identity gives
B+2J+2D+H=3. The reviewed general boundary-label argument gives B+J>=2;
the two-active-node lemma excludes equality for eight children. Hence
B+J>=3. Subtracting yields J+2D+H<=0, forcing B=3,J=D=H=0.

The three active nodes split the cyclic parent boundary into three arcs.
Each arc belongs to a single child; adjacent arcs have distinct labels,
so all three labels are distinct. Thus exactly three children have positive
outer contact, each in one connected arc. No other child can touch the
parent even at an isolated point: at a genuine parent corner such contact
would make J positive; at a side-interior point, a child with zero boundary
arc would have two internal boundary rays terminating there, making seam
degree at least two and hence D positive. Thus the five remaining children
are strictly interior.

For distinct convex children their intersection is convex and has empty
planar interior, hence is empty, a point, or one segment. Consequently the
positive-contact dual is simple. A contact cannot be subdivided by a third
child corner: that would either give a flat incidence on one of its hosts
(H>0), or a higher-degree seam node (D>0). All interior primal nodes are
therefore ordinary three-child native vertices. The three single outer arcs
and their three degree-one seam endpoints give exactly the simple triangular
boundary of the dual; there are no repeated dual boundary vertices or edges.
The dual is a triangulated disk with eight vertices, three boundary vertices,
five interior vertices and E=3*8-3-3=18 edges. Every interior dual degree is
its native side count, at least five. If eII counts edges among the five
interior vertices and eBB counts edges among boundary vertices, then

    25 <= 2eII+eIB = eII+18-eBB <= eII+15,

so eII>=10. A simple planar graph on five vertices has at most nine edges.
Contradiction. This excludes the entire Q inventory, independent of the P
parent, and consequently excludes any ordinary whole-polygon geometric
substitution with this matrix. It does not exclude other matrices, general
convex P5/Q7 pairs, or unrestricted two-convex-polygon tilings.

No discovery-log or git operation was performed. Inputs read:
`research-problem.md`; `research-protocol.md` sections 5,11,19;
`discovery-log.md` recent 19:22 entries;
`research/searches/progress-assessment-2026-10-19-1922.md`;
`research/searches/two-parent-p5-q7-cap-design-2026-10-19.md` and its hostile
review; the two six-child topology lemmas cited above. The adjacent Python replay verifies the displayed count identities and
exhausts the defect-allocation domain b=0..3,j=0..1,d=0..1,h=0..3;
nonnegative solutions of budget three all lie in these bounds. It uses Python
integer arithmetic, no external dependency, randomness, solver, or timeout.
It does not verify the analytic topology proof. Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/two-parent-junction-design-2026-10-19.py

The independent review verified the stronger theorem and its narrow scope.
