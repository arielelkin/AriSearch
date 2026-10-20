# Independent hostile review: Q7 five-boundary incidence gate

Date: 2026-10-19. Reviewer: independent Sol agent. Verdict: **VALID**, within the explicit cap assumptions. The unrestricted research problem remains unresolved.

## Exact claim and assumptions checked

Reviewed `research-problem.md`, protocol sections 8, 11, 19, the adjacent gate MD/Python/JSON, the universal six-child wheel seam conventions and substitution-consequences identities, the earlier Q7 obstruction and two-parent cap-design report.

The claim is emptiness of a simple triangulated dual disk with ten vertices, five distinct vertices on its boundary cycle, five interior vertices of degree at least five; its intended application is a Q7 partition into 7P+3Q with defect allocation (B,J,D,H)=(5,0,0,0), one connected outer arc per boundary child, and native incidences. No prescribed geometry, congruence, species placement or angle assignment is required for the contradiction.

## Independent analytic reconstruction

Euler and the trivalent seam degree sum give E=I+F-1 and I+B=2F-2. With F=10 and B=5 this is I=13, E=22. Independently, a simple triangulated disk has E=3n-b-3=22. Distinct successive boundary children supply five distinct boundary-boundary edges, so eBB>=5, even if there are additional boundary chords. The interior degree sum is at least 25. Thus 25<=2eII+eIB=eII+22-eBB<=eII+17, forcing eII>=8.

Let G be the embedded induced graph on the five interior vertices. Simplicity bounds each vertex's G-degree by four, so its full degree requirement gives it a boundary neighbor. The full boundary cycle is a Jordan curve enclosing G. Every boundary vertex therefore lies in the unbounded component of the complement of G: it can leave the full disk outward without encountering G. For an interior-to-boundary edge, its open arc misses G and is connected to this component. Its interior endpoint consequently belongs to the boundary of the unbounded face of G. Every vertex of G has this property, which is precisely an outerplane embedding. The simple outerplanar bound gives eII<=2*5-3=7, a contradiction.

This is a proof, rather than an inference from the finite replay.

## Attacks on topology and contact conventions

Disconnected G causes no exception. A component nested inside a cycle of another component could not have an edge reaching a boundary vertex without crossing that cycle. Cut vertices and bridges can repeat in outer-face boundary walks; the argument requires incidence with the unbounded face, not a simple facial walk. Isolated vertices also have that incidence. The standard outerplanar edge bound holds for all these cases; one may connect components and augment to a maximal outerplanar graph. No assertion that the original outer boundary of G is a five-cycle is needed.

Point-only contacts are not dual edges and cannot provide a neighbor. This does not weaken the native side lower bound: each side of a child without positive outer contact must be covered in positive length by other children. Convexity and disjoint interiors prevent the same neighbor from covering portions on two distinct supporting lines. Hence an interior pentagon has at least five distinct positive-length neighbors even before using H=0. Under H=0, any seam node inserted in a side interior would give a flat child-angle incidence; therefore there are no such subdivisions and interior dual degree equals the native side count. T contacts would have a flat incidence and are excluded by H=0. Higher junctions are excluded by D=0. Reflections, equal angles or lengths, and partial contacts produce no alternative in this fixed domain.

An interior child in the original terminology has no positive outer contact and could initially be suspected of touching the parent at an isolated point. At a parent-side isolated contact it would occupy a sector with two incident seams, violating active-boundary seam degree one (D=0); at a parent corner this violates J=0. It therefore does not obstruct the disk correspondence here. Repeated outer labels or several outer arcs for one child are explicitly outside the cap assumptions. The positivity and genuine native corners of convex polygons exclude zero-length sides and flat inserted native corners. The direct disk statement is also independently sufficient, so its validity does not rest on extending the six-child theorem to ten children.

## Computation audit and replay

Replay command:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/q7-five-boundary-incidence-gate-2026-10-19.py

Completed successfully: Python 3.12.13, NetworkX 3.6.1; 1024 labeled simple five-vertex graphs, 56 with at least eight edges, zero outerplanar graphs among those 56, maximum outerplanar edge count seven. No timeout, seed, symmetry quotient, floating arithmetic or SAT solver. The script uses the valid equivalence between outerplanarity and planarity after adding a universal vertex. Its encoding exhausts the ten possible unordered pairs. The counts also agree independently with binomial counting: C(10,8)+C(10,9)+C(10,10)=56. NetworkX is supplementary; no independent certificate for every cone is needed by this analytic proof. The replay rewrites the adjacent JSON with the same reported result.

## Generalization and scope

For the same simple triangulated disk assumptions with exactly k=5 interior vertices and b>=3 boundary vertices, E=2b+12 and eBB>=b imply eII>=13-b. The boundary-neighbor argument still gives eII<=7, so necessarily b>=6. Thus b<=5 is impossible in this precise class. This is a necessary condition; b>=6 is not an existence assertion. Disk boundary lengths one or two are unavailable in a simple boundary cycle and need separate conventions if discussed.

No defect found; no repair made. No unresolved uncertainty remains in the restricted graph obstruction. It does not exclude the substitution matrix under another defect allocation or boundary structure, arbitrary pentagon/heptagon pairs, arbitrary contacts outside this cap, plane tilings, or the objective of forcing aperiodicity. Protocol section 19 does not authorize ending the overall research because this route fails. Stopping this fixed gate is compatible with continuing other mechanisms under the root task. Discovery log and git were not edited by this review.
