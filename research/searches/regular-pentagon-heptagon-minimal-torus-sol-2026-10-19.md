# Minimal torus periodic witness: regular pentagon / Q7(144,126), h=0

Status: exact periodic witness, independently [hostile-reviewed VALID](../reviews/regular-pentagon-heptagon-minimal-torus-hostile-sol-2026-10-19.md). This falsifies aperiodicity of this specific h=0 pair. It does not settle the overall research problem or other h values. Search stopped at the prescribed 2P+2Q inventory.

## Exact construction

Let w=exp(2πi/20), in CyclotomicField(20), t=w+w^(-1). Let P have vertices p_i=sum_{j=0}^{i-1}w^(4j), i=0,...,4. Let Q have vertices q_i=sum_{j=0}^{i-1}l_j w^(3j), i=0,...,6, where l_j=t for odd j and 1 for even j. Thus Q has angle 144 at q0 and 126 elsewhere; its QQ sides are 1,3,5. This is exactly the reviewed first-gate h=0 metric.

Take four representative polygons, all with counterclockwise native vertex order:

- F0=P;
- F1=1−P;
- F2=1−w^6 Q;
- F3=w^6 Q.

Translate them by the lattice Λ=Z L1+Z L2, where

L1=2w^4+w^2+2,
L2=3w^6−w^4+w^2−3.

The retained JSON gives every representative vertex, every edge gluing and the lattice coefficients of every gluing displacement. Edges are numbered from zero. Its dart indices 0–4 are F0, 5–9 F1, 10–16 F2, 17–23 F3. The three QQ joins are (F2 edge1,F3 edge1), (F2 edge3,F3 edge3), (F2 edge5,F3 edge5); their endpoint displacements, taking first-edge start minus second-edge end, are respectively −L2, L1−L2, L1. This is an actual plane tiling with nonzero periods.

## Finite verification and coverage proof

The Sage script reconstructs all coordinates exactly in Q(w). It proves each paired edge has opposite equal vectors and that its endpoints differ by the declared integral lattice displacement. The two lattice vectors have nonzero determinant. It proves the covolume equals the sum of the four representative polygon areas.

For every ordered face pair (f,g), transform vertices to real lattice coordinates. If Ff and Fg+aL1+bL2 overlap, their two coordinate projection intervals must meet. This bounds a and b between ceil(min_f−max_g) and floor(max_f−min_g). The script checks all integer pairs in those exact bounds: 26 nonidentity ordered translate pairs. Every pair has disjoint interiors by an exact convex separating-axis test over AA. All other translates are excluded by the coordinate interval bounds. Identical representatives at shift zero are omitted only for f=g.

Consequently the four polygons project to a torus with disjoint interiors and area exactly its covolume. Their translates form a locally finite closed union. A point omitted from this union would have an open neighborhood omitted; this would yield a positive-area hole in the torus, contradicting equal area. Hence the translates cover the plane. This proves both nonoverlap and full coverage, including boundaries.

## Complete combinatorial domain

This enumerates one torus inventory 2P+2Q, with native faces, full-edge pairings and stars PPQ at Q's A vertex and PQQ at every B. No bound on lattice vectors or lattice shifts is imposed. All torus embeddings capable of realizing this inventory are represented before geometry filtering.

Star counting gives p=q and one PP edge in this inventory. Each P vertex incident to PP is an A vertex. Conversely every A incidence on P is incident to PP. A P edge with A at both ends cannot meet Q, whose four PQ edges have endpoint words AB, BB, BB, BA. If a pentagon had two PP edges, they could not be consecutive (that would produce PPP); their four distinct A endpoints would force an additional AA side in the five-cycle, requiring another PP edge and creating consecutive PP edges. Thus each P has at most one PP edge. The unique PP edge therefore joins the two distinct P faces. Rotations of the regular pentagons normalize its native edge labels to edge0 on both faces.

The remaining P edges are 1 (AB), 4 (BA), 2 and 3 (BB). Across an oriented gluing the endpoints reverse. There are 2! ways to match P edge1 to Q edge6, 2! ways to match P edge4 to Q edge0, 4! ways to match BB PQ edges, and 15 perfect matchings of the six QQ edges. Total: 1,440 pairings. No Q face or side-label symmetry reduction is applied. Vertex permutation next-face-dart composed with edge-pairing must have exclusively three-cycles with label multisets APP or BBP. Exactly two maps survive; both are connected and both have trivial rotational holonomy. They exchange the names of the two Q faces.

Reflections are permitted. Orientability of a translation torus allows all face boundaries to be read counterclockwise, forcing endpoint reversal in every edge gluing. Both prototiles are reflection-symmetric: P is regular and the script checks exactly {w^8 conjugate(q):q in Q}=Q. Thus reflecting a physical face introduces no omitted geometric configuration after relabeling its native counterclockwise boundary. All Q edge-label permutations induced by this relabeling are retained by the enumeration. There is no orientation restriction on physical tiles.

The complete pairing enumeration is not needed to trust the positive witness: the four exact polygons, lattice and finite verification stand independently. No UNSAT claim is made. No larger torus or patch search was run.

## Reproduction and limitations

Replay from repository root:

    mise exec -- conda run --no-capture-output -n arisearch sage research/searches/regular-pentagon-heptagon-minimal-torus-sol-2026-10-19.sage

The companion .json is stdout from the completed run, SageMath 10.9. No solver, random seed or timeout is used. Integer combinatorics and exact cyclotomic/AA arithmetic decide all branches. The first output attempt had a JSON serialization error after completed computation; the retained replay succeeds. There is no dependence on that failed output. The certificate stores exact cyclotomic area expressions; the script verifies their ordered equality in AA. No Git or discovery-log modifications were made.

Please subject the whole witness, coverage argument, reflection handling and finite translate bound to independent hostile review before treating the claim as reviewed.
