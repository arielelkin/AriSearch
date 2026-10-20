# Regular pentagon / 144–126 octagon: exact first gate

Status: exact metric candidates and independently reviewed valid local gate, not a plane tiling construction. No claim about the unrestricted main problem.

## Shape and unrestricted contact reduction

Normalize the regular pentagon P to side one. Q has four A=144° and four B=126° corners. All angles of either tile exceed 90°. At a tiling vertex, a straight tile-side sector would leave 180°, which cannot be filled by two corners (each at least 108°), nor by one corner (none is 180°). Thus no T junction is possible. Four corner sectors exceed 360°; two cannot total 360°. Every vertex is edge-to-edge and trivalent. In units of 18°, the corner angles are 6,8,7; the only nonnegative triples summing to 20 are (6,6,8) and (6,7,7). Hence exactly PPQ at A and PQQ at B occur, including reflected placements. The same reasoning rules out either prototile tiling alone.

At A, both incident Q edges face P and have length one. At B, precisely one edge faces P and one Q. Therefore Q-facing edges form a perfect matching of the four B vertices along the cyclic boundary. There are two such edges, both BB; the other six sides have length one. This deduction uses unrestricted contacts, not an imposed matching rule.

## Finite exact domain and metric output

The script enumerates all 70 labeled cyclic 4A4B words, keeps the lexicographically least rotation/reflection representative, and enumerates all pairs of cycle edges whose four endpoints are exactly the B positions. The only outputs are AABBAABB with QQ edges (2,6), AAABBABB with (3,6), and AAAABBBB with (4,6), indexing from zero. The suggested AABBABBA is dihedrally equivalent to AAABBABB.

Let z=exp(2πi/20), edge direction d0=1, and di=d(i-1) z² at A_i or d(i-1) z³ at B_i. Solve Σ length_i d_i=0 exactly in Q(z). For AAABBABB and AAAABBBB the coefficient determinant is nonzero and the unique QQ lengths are both

L=−z⁷+z⁵−z³+2z=2cos(18°)>0.

All nonincident vertices lie strictly to the left of each directed polygon edge, checked exactly; these are strictly convex octagons. The two QQ sides can pair metrically. For AABBAABB, the QQ directions are opposite and the sum of the six unit vectors is zero, so the complete metric family is x=y=t>0. This family is strictly convex for every positive t: its direction sequence makes one positive complete turn, and it is the Minkowski sum of the t=0 convex hexagon and a segment in the QQ direction. This continuum was not subjected to a parameter-wide forced-neighbor overlap audit.

## Forced immediate neighborhoods

For each isolated metric, place the unique regular pentagon outside each of the six unit Q edges. Exact separating-axis checks find no pair of distinct forced P tiles with intersecting interiors. Exact coincident copies, if any, are identified rather than declared a collision. At every A vertex, the two incident P neighbors have exactly two common vertices, separated by unit distance: they share the required PP side. This is a necessary local check only.

The script also tests all immediate QQ joins: two choices of target BB edge, two choices of source BB edge, and both reflection parities. Each tested object consists only of Q and its six forced P neighbors. All 16 joins (eight for each isolated metric) pass without any distinct-tile interior collision; both reflection parities survive for every source/target choice. The certificate records every collision. A passed join establishes only the stated finite neighborhood.

## Strand implication and stopping boundary

In any plane tiling, each Q has exactly two Q neighbors, one across each whole BB edge. Distinct convex polygons cannot share two distinct noncollinear edges, so these are distinct neighbors. The Q adjacency graph is therefore a union of degree-two components (finite cycles or doubly infinite paths). The metric alone does not prove that paths are straight, monotone, periodic, or transversely completable. Both reflection parities survive at this immediate gate, so the gate branches rather than forcing a unique continuation.

The exact missing obligations are (1) prove at least one complete plane extension of one candidate, and (2) either exhibit a periodic plane extension or exclude every periodic extension and every nonzero translational symmetry. Degree-two strands and finite local legality do not establish either obligation. Under protocol §5, stop before larger patch or torus enumeration absent a new global invariant or a specifically derived complete carrier.

The [independent Sol hostile review](../reviews/regular-pentagon-octagon-144-126-hostile-sol-2026-10-19.md) reconstructed the word enumeration and metric gates and checked all 16 immediate joins with a separate Sage checker. It found no error within the stated finite scope. In particular, the singular continuum has no parameter-wide forced-neighborhood audit, and neither isolated metric has a proved plane extension or periodicity property.

A later [reviewed AA-side capacity theorem](../lemmas/regular-pentagon-octagon-aa-side-density-obstruction-2026-10-19.md) **excludes `AAAABBBB` from every plane tiling** despite its successful local joins. It counts at most one AA-facing side per P against three AA sides of each such Q, together with the global star ratio `p=2q+O(R)`. The `AAABBABB` isolated metric and `AABBAABB` continuum each have two AA sides and remain undecided.

## Replay and scope

Run:

```sh
mise exec -- conda run --no-capture-output -n arisearch sage research/searches/regular-pentagon-octagon-144-126-first-gate-2026-10-19.sage
```

The adjacent JSON is the retained certificate. Computation is deterministic, uses Sage cyclotomic and real algebraic arithmetic, and has no random seed or solver timeout. The finite domain is complete as stated. Numerical decimal lengths in JSON are display only; all decisions use exact algebraic signs and equalities. No unbounded patch or torus search is included. No literature or novelty claim is made. Scope: normalization to regular unit P and the specified four-A/four-B palette only.
