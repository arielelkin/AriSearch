# Hostile review: corrected private-edge dimer design cycle

Date: 2026-10-19. Verdict: **VALID within its explicitly stopped scope.** The corrected shapes are genuine distinct noncentral convex hexagons, each has a reflected-placement-inclusive monohedral obstruction, and every hypothetical mixed tiling has a canonical first partition into same-species private-edge dimers. No recursive hierarchy, mixed plane tiling, periodic escape, or aperiodicity is established.

Reviewed sources: [report](../searches/equiangular-private-dimer-recursion-sol-2026-10-19.md), [replay](../searches/equiangular-private-dimer-recursion-sol-2026-10-19.py), and [illustrative SVG](../searches/equiangular-private-dimer-recursion-sol-2026-10-19.svg). Read also the [honeycomb development theorem](../lemmas/equiangular-hexagon-honeycomb-development-2026-10-19.md). Research-problem definitions and the full-edge sector argument were independently checked in the preceding binary-partner review. This review does not import an existence conclusion from honeycomb development.

## Exact geometry and discarded input

In triangular coordinates the six directions are (1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1). Their weighted sum vanishes exactly when s0-s3=s2-s5=s4-s1. For corrected A=(5,3,3,4,4,2) all three differences are 1; for B=(1,3,3,2,2,4) all are -1. For the parameter family they are d and -d. Positivity follows from m>2d>0. The direction sequence turns positively through 60 degrees at every corner; the closed positive chain is strictly convex. Equivalently all nonincident vertices lie strictly to the left of each directed edge, as the source's supporting-line calculation shows. Opposite lengths differ, excluding central symmetry. Their different length multisets exclude congruence even under reflection.

The preliminary A=(5,2,3,4,4,3) has differences (1,0,2), does not close, and is explicitly discarded. Its only executable use is an assertion rejecting closure. It supplies no polygon, seam computation, SVG component, or proof premise.

Each corrected word has twelve distinct dihedral words: its unique private side fixes a possible symmetry axis or rotational phase, and its two neighboring lengths differ, excluding the remaining reflection. Side-word reversal covers reflected physical placements. The existence of arbitrary global rotations does not create additional relative mates along a fixed private segment.

## Full-edge matching and exhaustive relative placements

At a native corner-in-side incidence the side tile consumes 180 degrees; the remaining 180 degrees cannot be partitioned into 120-degree tile sectors. Therefore such incidences are impossible, and every side contact is full. Exactly three corners occur at each vertex. Thus a side with length m+2d can only pair A with A, and m-2d can only pair B with B. Each such side occurs once in its species and is absent from the other. Adjacency across it is an involution without fixed tiles, giving a disjoint perfect matching in each species. This establishes an intrinsic first grouping conditional on existence; it does not establish existence.

Place the private segment from (0,0) to (p,0) and its tile above it. An isometry taking the unique private segment to itself either fixes or exchanges its endpoints. The only maps giving a mate below it are reflection in its line and the halfturn about its midpoint. The identity and perpendicular-bisector reflection place the interior above instead. The two accepted maps give distinct component placements since the native private-edge neighbors have unequal lengths. Their interiors cannot overlap because the original polygon and mate lie in opposite supporting half-planes.

## Boundary and endpoint checks

For W=(s1,...,s5), traverse the first exposed chain from the right seam endpoint to the left. The halfturn mate's exposed chain continues with W; the reflection mate must be traversed in reverse native order and contributes reverse(W). Thus the boundary words are WW and W reverse(W), exactly as displayed. Each seam endpoint has union angle 240 degrees, the other eight vertices 120 degrees, and no boundary sides merge into a straight segment. This also checks the ten-edge count and both AA/BB tables.

With neighboring lengths L=s5,R=s1, halfturn endpoints require (L,R) twice; reflection endpoints require (L,L) and (R,R). Direct enumeration of the native cyclic corner pairs gives:

- AA halfturn: (2,3) at each endpoint, present only in B.
- AA reflection: (2,2), present only in B, and (3,3), present in either species.
- BB halfturn: (3,4) at each endpoint, present only in A.
- BB reflection: (4,4), present only in A, and (3,3), present in either species.

These statements remain exact when 2,3,4 are replaced by m-d,m,m+d, since all five labels remain distinct. A convex tile is contained in the tangent cone at each of its vertices. Consequently the compatible third tile at one endpoint fits wholly in the unoccupied 120-degree cone and has no interior overlap with either dimer component. This establishes individual endpoint realizability only. It does not establish simultaneous endpoint completion or any larger legal patch, and the source states that limit correctly.

The monohedral exclusions follow immediately and exhaust reflections: A halfturn needs a missing (2,3) corner and A reflection a missing (2,2) corner. B halfturn needs a missing (3,4) corner and B reflection a missing (4,4) corner. No monohedral omission escapes via partial contacts or a different private-edge isometry.

## Replay, illustration, and exact limit

Ran the documented replay through the required environment wrapper; it exited 0. It rejects the invalid preliminary word, checks exact vector closure of all dihedral states, checks state distinction and endpoint memberships, and checks 288 ordered prior-cone comparisons with no matches. Its affine coefficient reduction from m+kd to k is valid for m>2d>0 and d nonzero. The finite comparisons establish nonmembership in that specified cone, not nonexistence of periodic tilings outside it.

The replay forms and prints the boundary words by tuple concatenation; it does not independently derive polygon-union boundaries. Its reported endpoint arrays are literal output data, although the actual endpoint membership assertions derive their pairs from the native neighboring lengths. The boundary and endpoint geometry was therefore independently checked analytically above rather than inferred from printed JSON. The SVG source has four pairs of scaled corrected polygons, correct seam lengths and labels, and the stated words and endpoint labels. Its decimal coordinates are illustrative, not proof data.

After the matching, private lengths disappear from both supertile boundaries: the only remaining labels are m-d,m,m+d, shared by both species. Hence the identical unique-private-edge rule has no next application. This is a precise failure of this particular recursion proposal. Neither two locally viable seam choices nor shared boundary labels prove that every possible hierarchical recognition scheme fails. The source expressly preserves this distinction. The separate small periodic-carrier search was not independently reviewed here and is not used for this verdict.

No counterexample to the stated narrow conclusions was found. The exact missing work remains mixed infinite extension and either a proved recognizable recursive boundary substitution or a periodic escape. No discovery-log or Git changes were made by this review.
