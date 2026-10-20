# Q7 with 7P+3Q: five-boundary-child incidence gate

Date: 2026-10-19. Status: **proved narrow obstruction; [independent Sol hostile review](../reviews/q7-five-boundary-incidence-hostile-sol-2026-10-19.md) VALID**. The unrestricted two-convex-polygon objective remains unresolved. The reusable generalization is the [five-interior cap lemma](../lemmas/five-interior-native-cap-boundary-obstruction-2026-10-19.md).

## Fixed domain

One Q7 parent, ten children comprising seven pentagons and three heptagons, five distinct boundary children each occupying exactly one connected outer arc, and five interior children. Every internal seam vertex is trivalent; the defect vector is (B,J,D,H)=(5,0,0,0). All child corners are native, and the contact dual is simple. The requested witness would be a triangulated disk on ten child vertices with boundary cycle length five, decorated by seven parent corners distributed along the five outer arcs. Interior dual degree equals native side count (five or seven); a boundary child's native count additionally includes its outer-arc edges. No species, corner-role, or geometry assignments are assumed beyond these requirements.

This domain is empty. Consequently there are no ordered parent boundary words or seam endpoints satisfying it.

## Analytic obstruction

The reviewed seam identities give I+B=2F-2, hence I=13 and E=I+F-1=22. Equivalently, a triangulated disk with n=10 and b=5 has E=3n-b-3=22 dual edges. Let eII,eIB,eBB count interior-interior, cross, and boundary-boundary edges. The five successive boundary labels are distinct and supply a cycle, so eBB>=5. All five interior children have at least five distinct neighbors. Thus

    25 <= 2eII+eIB = eII+22-eBB <= eII+17,

and therefore eII>=8. Heptagons among the interior children only strengthen this inequality.

Let G be the induced embedded graph on the five interior vertices. Every vertex of G has internal degree at most four, because the dual is simple. Since its full degree is at least five, every vertex of G has a neighbor among the boundary children.

All boundary-child vertices lie on the outer boundary cycle of the full dual disk, so they are in the unbounded face of G. Each edge from an interior vertex to a boundary vertex has its open arc disjoint from G, and hence witnesses that its interior endpoint is incident to the unbounded face of G. Therefore every vertex of G is incident to the unbounded face in the inherited embedding: G is outerplanar. This reasoning also allows G to be disconnected or have cut vertices.

A simple outerplanar graph on five vertices has at most 2*5-3=7 edges. For completeness, add noncrossing edges within the disk until the graph becomes maximal outerplanar on the same five vertices. Its outer cycle has five edges and its bounded faces are triangles; Euler's formula then gives seven edges. Disconnected graphs can first be connected in the outer face. Thus eII<=7, contradicting eII>=8.

The proof uses only disk topology and simplicity. It precedes angles, lengths, similarity, coordinates, convex realizability, and congruence checks. In particular an abstract disk witness already fails, even if every boundary child is allowed arbitrary positive native side count.

## Supplementary exact finite check

The adjacent Python script exhausts all 2^10=1024 labeled simple graphs on the five interior vertices. Object encoding: a ten-bit mask on lexicographically ordered unordered vertex pairs. No symmetry reduction, random seed, solver, or floating arithmetic is used. A graph is outerplanar exactly when its cone (one new universal vertex) is planar; NetworkX checks that six-vertex graph. All 56 graphs with at least eight edges have nonplanar cones; maximum outerplanar edge count is seven. This is a supplementary finite check, not a dependency of the analytic proof. The program retains aggregate exact counts and environment versions in the adjacent JSON. No full disk maps are enumerated and no search for patches is performed.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/q7-five-boundary-incidence-gate-2026-10-19.py

Environment: Python 3.12.13, NetworkX 3.6.1. Completion: all 1024 cases, no timeout imposed (under one second of enumeration); no external SAT solver. The finite result is complete for the stated labeled graph domain.

## Stop and exact restart gap

Stop this single incidence gate under protocol section 5. Matrix [[9,7],[2,3]] is not supplied by this mechanism: its Q column cannot use the stated five-boundary/five-interior all-native trivalent simple cap. This does not exclude that entire matrix under other defect allocations or boundary-contact structures, and does not exclude arbitrary pentagon/heptagon pairs.

The exact missing construction step is an explicit native Q7 child-incidence disk with inventory 7P+3Q outside this five-single-arc-boundary, five-interior domain, together with its seam endpoint lists and ordered parent boundary words. No such alternative is supplied here. Changing metric or assigning angle roles cannot repair the contradiction. No P-parent map, substitution claim, generic solver, or patch growth is pursued.

Dependencies: research-problem.md; research-protocol.md sections 5,11,19; research/lemmas/heptagon-five-pentagons-three-heptagons-obstruction-2026-10-19.md; research/searches/two-parent-p5-q7-cap-design-2026-10-19.md. Discovery log and git were not edited.
