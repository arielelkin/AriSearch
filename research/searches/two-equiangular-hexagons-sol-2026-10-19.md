# Two equiangular hexagons: rigorous structure and a metric counterexample

Date: 2026-10-19. Status: bounded analytic cycle; **general gate unresolved and blocked**. Internal derivations, not independently reviewed. No bounded patch or torus search was performed. No novelty claim is made.

## Question and dependencies

For arbitrary strictly convex equiangular 120-degree hexagons A,B, does plane tileability by their unmarked congruent copies imply existence of a tiling with a nonzero translation? Reflections, arbitrary contacts, arbitrary positive closing metrics, and omission of either species are allowed. This note does not prove the implication or produce an aperiodic pair.

Read: research-problem.md; research-protocol.md sections 5 and 19; current discovery-log.md (including the stopped broad-obtuse cycle and Q-only classification entry); obtuse-two-convex-periodicity-sol-2026-10-19.md; resonance-qonly-hexagon-sol-2026-10-19.md; and ../lemmas/obtuse-edge-forcing.md. Root owns log integration. This assignment owns only this report.

## Structural reduction without assuming honeycomb connectivity

A finite family of positive-area compact polygons gives local finiteness: choose an inscribed disk in each type and a common bound on diameter. All tiles intersecting a fixed compact region have disjoint inscribed disks of uniformly positive radius in a fixed bounded enlargement.

At a tile corner p, a straight-through side of another tile would leave a half-plane angle of 180 degrees to partition. One genuine 120-degree corner leaves 60 degrees unfilled, and two exceed 180 degrees. Thus no corner lies strictly inside any side. A partial positive-length contact would have such an endpoint, so all contacts are whole native sides. At each vertex precisely three 120-degree corners meet. This specializes the reviewed obtuse-edge-forcing proof and includes reflections.

Take the cellular dual of the resulting plane decomposition. Convexity and full-side matching give a plane triangulation, with six triangles around each dual vertex because every primal face is a hexagon. Assign each abstract dual triangle a unit equilateral metric. Every dual vertex then has angle 2*pi, and the metric is flat everywhere. It is complete: the unit equilateral triangulation is locally finite with bounded degree; its path metric is quasi-isometric to its graph metric (a path can be replaced by a path in the 1-skeleton with uniformly bounded multiplicative/additive cost, using the uniform triangle shape). Finite graph balls follow from bounded degree. Equivalently the intrinsic closed bounded balls are compact. Its underlying surface is the plane, hence simply connected.

Development of a complete simply connected flat surface is a global Euclidean isometry. For clarity, local straight segments lift for their full length by completeness; development is therefore a covering of the Euclidean plane, and that target is simply connected. The developed unit triangles are consequently the ordinary equilateral triangulation. Its dual gives the ordinary honeycomb **as an abstract cell complex**. This derives honeycomb connectivity; it does not assume the original metric embedding is a regular honeycomb or is periodic.

Independently, any one hexagon has its six directed side headings separated successively by 60 degrees. Across a shared edge its neighbor has exactly the same three unoriented side directions. The tile adjacency graph is connected, so there is one global set of three unoriented directions for every edge in the plane. After a global rotation these are 0,60,120 degrees. At a vertex the three outgoing rays are either 0,120,240 or 60,180,300 degrees; their types alternate along every edge. This also gives the bipartition of the honeycomb vertices directly.

The precise line statement is that every edge lies on a supporting line in one of three parallel-direction families. It does **not** say the edge network contains complete straight lines: no two incident edges at a trivalent vertex are collinear. Nor have we proved that the offsets of all lines in a family form a discrete arithmetic progression. Such an assertion would add substantive metric information.

## Exact periodic pair refuting the intermediate claim that all occurring tiles are central

Here is a tilable pair containing a noncentrally symmetric equiangular hexagon. Thus applying the monohedral classification independently to each occurring shape is invalid.

Put u_k=(cos(k*pi/3),sin(k*pi/3)), and use triangular-lattice sites

    c_(i,j)=2*i*u_0+2*j*u_1,    i,j in Z.

Give site (i,j) weight w=1 if i-j=0 modulo 3, and w=0 otherwise. Its power cell is

    C_c={x: |x-c|^2-w_c <= |x-d|^2-w_d for every lattice site d}.

These cells cover the whole plane and have disjoint interiors: the power minimum is attained because the lattice is discrete and the weights are bounded. All adjacent lattice sites have different residues. The six nearest sites to c are c+2*u_k. Their inequalities, in coordinates y=x-c, are

    y dot u_k <= 1+(w_c-w_(c+2*u_k))/4.

At a weight-one site all six bounds are 5/4, producing a regular hexagon B. At a weight-zero site the bounds alternate a=3/4 and b=1, producing a strict equiangular hexagon A; the two zero residue classes interchange a and b, hence are congruent by a 60-degree rotation.

No further site cuts these hexagons. Each candidate cell is contained in the regular hexagon of inradius 5/4 and hence in the disk of radius 5/(2*sqrt(3)). Every non-nearest site has distance D>=2*sqrt(3), and its half-plane has boundary at signed distance

    (D^2+w_c-w_d)/(2*D) >= (D^2-1)/(2*D)
                              >= 11/(4*sqrt(3))
                              > 5/(2*sqrt(3)).

Thus the six displayed inequalities are the full power cell. Consecutive normals differ by 60 degrees, so every interior angle is 120 degrees. For alternating support distances a,b the side with normal u_k has length

    (h_(k-1)+h_(k+1)-h_k)/sin(60 degrees).

Consequently A has alternating side lengths

    L=5/(2*sqrt(3)), S=1/sqrt(3), L,S,L,S,L,S,

whereas B has all six sides L. Both are strict convex hexagons; A is not centrally symmetric because opposite side lengths differ. This is an exact coordinate description by six linear inequalities over Q(sqrt(3)).

The pair has a mixed rank-two periodic tiling. For example the weight field is preserved by the independent site translations (i,j)->(i+1,j+1) and (i,j)->(i+3,j), giving physical periods

    2*u_0+2*u_1=(3,sqrt(3)),   6*u_0=(6,0).

Every fundamental three-site quotient has one B and two A cells. At each geometric vertex the incident cells have the three residue classes, hence the star is AAB. The construction also has the simpler B-only regular-hexagon omission escape. It is a counterexample to the intermediate centrality claim, not a counterexample to periodic escape and not a pair with two noncentral members.

## What the monohedral and central cases do establish

If either A or B is centrally symmetric, that member alone gives a lattice tiling; the other member can be omitted. If a given pair admits a monohedral tiling, the cited Zhu-Wang-Yan classification and its equiangular specialization in the Q-only note similarly imply that occurring member is central and hence supplies a lattice escape. This classification is an external trust boundary only for that monohedral assertion; the explicit construction above does not use it.

The unresolved case is therefore a genuinely mixed pair with neither member central. The structural reduction above does not rule out its tileability and does not produce a period. In particular, a trivalent plane map with all faces hexagons fixes the abstract honeycomb but leaves its species field and its embedding by unequal edge lengths undetermined.

## Exact blocked obligation

Let a honeycomb cell complex carry copies of two fixed positive closing six-tuples of side lengths, each with successive turns 60 degrees, with arbitrary native-side alignments and reflection parity, and suppose that its development is an embedded covering of the plane. Prove either that one shape is centrally symmetric, or that these same two shapes admit some embedded development with a nonzero Euclidean translation. An alternative useful intermediate theorem would provide an exact repeatable complete strip with matching transverse boundary displacements from every such realizable two-shape metric.

Neither shared directions, equilateral-dual flatness, nor the native closure identity supplies that repeatable strip. Writing z=exp(i*pi/3), each individual shape obeys

    s0-s3 = s2-s5 = -(s1-s4),

but its unequal opposite differences need not vanish: the exact A above has nonzero differences and occurs in a plane tiling. A finite set of side lengths and native alignments likewise gives no proved finite state space for transverse line offsets or return displacement. The line-spacing dynamics therefore remains theorem-strength, and this bounded analytic cycle stops under section 5. No enlargement of finite patches or periodic quotients follows.

A justified restart requires a new global constraint on the two noncentral six-tuples or an exact transverse carrier construction, rather than the already-established honeycomb topology. No finite search, numerical experiment, or literature novelty inference is claimed in this cycle. A symbolic SymPy sanity check solved each of the six consecutive 2-by-2 support-line systems, checked all 36 vertex/half-plane incidences for each shape, and reproduced the displayed side lengths and the exact non-neighbor clearance sqrt(3)/12. This check is diagnostic; the formulas and inequalities above provide the proof without software.
