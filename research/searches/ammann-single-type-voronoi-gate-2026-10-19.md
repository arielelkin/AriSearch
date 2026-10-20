# Single-source-type Ammann mean-site Voronoi gate

Status: exact finite obstruction; [independent Sol hostile review](../reviews/ammann-single-type-voronoi-hostile-sol-2026-10-19.md) PASS. This tests three distinct ordinary Voronoi rules: keep only the arithmetic vertex means of H6, only P1, or only P2, in the genuine reviewed Ammann source at J=1/2+(4/5)w. It changes the site population, beyond the closed weighted box obstruction. No source aperiodicity is transferred.

## Relative density before geometry

Each type is relatively dense in every legal source. The reviewed [hierarchy and embedding](../lemmas/weighted-ammann-power-small-box-obstruction-2026-10-15.md) gives arbitrary-depth Robinson composition. Each red or blue parent has a red child. Hence every level-10 Robinson parent half contains a level-9 red supertile. The exact embedding replay below puts the retained source contexts, including complete polygons of all three types, inside that red supertile. This supplies one chosen-type site in each level-10 half. The diameter of either unit Robinson half is less than 2; scaling gives the uniform covering radius 2 phi^10. Every point is in a level-10 half (including boundary points by either adjacent half), so this is a bound for every legal source. The sites are uniformly separated because each is the interior mean of a convex tile and the finite prototype family has a positive minimum distance to supporting lines. Thus all three ordinary Voronoi rules exist globally with bounded cells.

## Certified first obstructions

The [script](ammann-single-type-voronoi-gate-2026-10-19.py) reads the reviewed exact source certificate and computes exact AA half-plane clips. Original source face indices are retained.

| Retained type | Source face indices | Genuine corner counts | Obstruction |
|---|---|---|---|
| H6 | 75,73 | 6,4 | Face 73 is a quadrilateral, excluded by the at-least-five-sides gate |
| P1 | 76,71,70 | 6,5,6 | Three incongruent cells; the two hexagons have inequivalent exact edge Gram matrices |
| P2 | 81,72,79 | 5,7,6 | Three incongruent cells by corner counts |

Each rule stops at its first certified obstruction. Intermediate representatives are retained to make stopping behavior reproducible. Congruence allows reflection. For equal corner counts, the script tests every cyclic shift and reversal of the full edge Gram matrix, which is a complete Euclidean congruence invariant for the ordered polygon edge vectors.

## Exact finite cutoff and occurrence

For each candidate c the script intersects the same-type competitor halfplanes from sites at distance at most 4, starting with a square of radius 10. It removes duplicate and collinear vertices and proves strict positive turns. No resulting vertex touches a square edge, so the square is redundant. Let B be the maximum distance of its resulting vertices from c. The finite cell lies in the B-disk. Any site at distance d>2B is redundant on that disk, because d²-2Bd>0. The script proves 2B<4, checks every omitted finite competitor, and proves the source patch boundary distance is greater than 2B+2R, where R is the reviewed maximum prototype mean-to-vertex distance. Every missing tile either lies outside the patch or meets its boundary, and has diameter at most 2R. Thus every missing mean is farther than 2B and the clipped polygon equals the global Voronoi cell.

To avoid any centered-seed extendability assumption, the script selects every decorated source rhomb having a vertex within 2B+2R+2+1/1000 of any retained witness. Unit rhomb diameter is less than 2, so this includes all rhombs needed for the finite source contexts. It verifies all 209 exact typed decorated frames under the reviewed translation delta=34+8w+26w²−13w³ into the ninth subdivision of one red Robinson triangle. The existing every-source level-10 composition bridge then makes all these witnesses occur in every legal source. All cutoff comparisons and frame matches are exact; approximate numbers in the JSON are diagnostics. The certificate retains exact vertex minimal polynomials with isolating intervals and the selected frames.

## Replay and scope

Run `mise exec -- conda run --no-capture-output -n arisearch python research/searches/ammann-single-type-voronoi-gate-2026-10-19.py`. It rewrites the [certificate](../certificates/ammann-single-type-voronoi-gate-2026-10-19.json). The reviewed source reconstruction and hierarchy are dependencies. This excludes these three fixed single-type mean rules. It does not exclude other site rules, other source metrics, or the unrestricted polygon problem; no decoder or aperiodicity theorem for the new Voronoi tilings is asserted.
