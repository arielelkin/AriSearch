# Independent hostile review: weighted Penrose-center gap witness

Date: 2026-10-19. Verdict: **PASS for this fixed-source affine-support interval**, subject to the already disclosed standard infinite Robinson/Penrose base-pairing property. No whole-family exclusion is established.

Reviewed the matching gap-witness Markdown, Python and JSON, the reviewed unweighted source and its hostile review, and the central weighted and complementary-tail gates and reviews. The only sampled parameter is delta=-3/4; no other delta or enlarged source was searched. No git or research-log files were edited.

The independent checker is `research/reviews/verify_penrose_weighted_center_gap_sol_independent.py`. It reuses the earlier reviewer's independent real-coordinate source reconstruction, imports no producer, and works over Q(sqrt(5)) with metric x²+((3-phi)/4)y². It checks the claimed affine vertices directly rather than trusting floating clipping or cyclotomic intersections. Its exact replay passed with assertions enabled, as did the producer's JSON replay with `--check`.

## Source, weight sign and complete cell

The independent reconstruction checks 890 triangles, 430 distinct centers, labelled level-1 inclusion in level 5, unit apex edges, both geometric base lengths, ordered same-color opposite-apex pairing, all unit rhomb sides, and every unmatched base on the outer decagon. This is the same reviewed nested plane source; standard infinite pairing remains an imported source property, rather than a theorem proved from one finite patch.

Index 25 is thick and is the first center in exact increasing squared-distance/index order; the scan record is exactly [25]. Its exported center agrees with reconstruction. Supports are exactly [26,70,328,374]. Expanding power squared-distance-minus-weight gives 2(q-c) dot v <= |q-c|²+weight(c)-weight(q), confirming the sign for thick weight delta and thin weight zero.

All 1720 vertex/site affine residuals satisfy their inequalities at both exact interval endpoints. Affinity proves every finite inequality throughout the closed interval. Both endpoint vertices of every claimed edge lie identically on its supporting power line, checked coefficient by coefficient. Four positive cyclic turns make the polygon strict convex with genuine positive-length supporting edges. Its four support halfplanes therefore intersect in exactly this polygon; feasibility against all other halfplanes proves it is the entire finite cell. This establishes completeness rather than merely exhibiting an inscribed quadrilateral.

## Maximal interval and endpoint strictness

Independently maximizing every lower root and minimizing every upper root gives precisely

    L=-1/4-phi/2, U=-1/44-2phi/11.

All limiting vertex/site pairs match the JSON. Thus [L,U] is the maximal finite feasibility interval for these particular four affine vertices and supports. Strict quadrilaterality changes it to (L,U]. This is not a maximality claim under changes of supports.

For each turn, use u=(delta-L)/(U-L). The independent checker recovers the quadratic as u*(a*u+b), verifies b>=0 and a+b>0 exactly, and hence proves positivity for every 0<u<=1. All four turns vanish at L; all four are positive at U, whose vertices are distinct. Consequently excluding L and including U is correct. Extra endpoint equalities do not eliminate a side at U. The sample -3/4 lies strictly inside this interval and the previously unclosed gap.

## Uniform infinite-source tail

The independently recomputed minimum squared distance from center 25 to every exposed segment of the retained rhomb union is

    M=93/4+149phi/4 >64.

The center is interior to its retained rhomb; the disk of radius sqrt(M) lies in the union. Every omitted genuine rhomb center is interior to an omitted rhomb with disjoint interior, so D>=sqrt(M)>8. This includes future partners of boundary triangles and requires no rhomb-radius subtraction.

Every affine vertex has squared radius <4 at both L and U. Convexity of squared norm extends this bound throughout the parameter interval, and polygon convexity extends it to every cell point. Also -2<L<U<2. Therefore every omitted site's doubled power slack is at least D²-2DR-|delta|>D²-4D-2>30. This is uniform for the full interval, including U; the stronger sample bound R<1 also passes. Hence the finite quadrilateral equals the actual infinite-source power cell throughout (L,U].

## Remaining scope

Combining the previously reviewed (-infinity,A] and [-1/4,infinity), where A=-21/44-9phi/22, with this new interval leaves exactly

    (A,L] and (U,-1/4).

Both gaps have positive length: L-A=(5-2phi)/22 and -1/4-U=(4phi-5)/22. The lower gap includes L because this affine witness degenerates there; this asserts only absence of coverage by these certificates. Neither gap is classified.

Each certified strict convex quadrilateral tiles periodically by half-turn copies, so a proposed protoset containing every output class of this fixed source admits a periodic omission tiling on the covered parameters. This establishes neither a two-class census nor exclusion of other weighted rules, other sources, or the remaining parameters. No substantive defect was found in the scoped witness.

Replay both commands through `mise exec -- conda run --no-capture-output -n arisearch`:

    python research/searches/penrose-weighted-center-gap-witness-sol-2026-10-19.py --check
    python research/reviews/verify_penrose_weighted_center_gap_sol_independent.py
