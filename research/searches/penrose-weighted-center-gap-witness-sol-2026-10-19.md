# Penrose weighted center: one gap witness gate

Status: exact finite parameter witness, independently [hostile-reviewed PASS](../reviews/penrose-weighted-center-gap-witness-hostile-sol-2026-10-19.md) within the stated source dependency and interval.

Fixed sample: delta = -3/4, strictly in the previously unclosed gap
(A,-1/4), where A=-21/44-9phi/22 and phi=(1+sqrt(5))/2.
Weight is delta for thick/blue type 1 and zero for thin/red type 0.
The existing level-5 Preshing source has 890 triangles and 430 complete
unit rhombs. No enlargement, alternate weight, or other sample was used.

The first center in exact increasing squared-distance order is source index
25 (thick). It has a complete strict convex quadrilateral at the sample,
with counterclockwise support indices [26,70,328,374]. Coordinates and
all limiting vertex/site pairs are retained exactly in the adjacent JSON.
Pairs [a,b] mean a+b phi. Vertex coordinates are relative to the center in
z=x+i sin(36 degrees)y; the center itself is in the cyclotomic basis.

For these four particular affine support intersections, the maximal interval
allowed by every finite source inequality is

    (-1/4-phi/2, -1/44-2phi/11].

The lower endpoint collapses all turns and is excluded; the upper endpoint
has four strict positive turns and is included, although additional sites
meet a vertex there. Each inequality is affine in delta; taking their exact
root extrema proves maximality for this specific support cell. This does
not classify other supports outside this interval. Exact quadratic Bernstein
coefficients of all four turns are nonnegative, with positive interior
values, establishing strict convexity throughout the open interval and at
the upper endpoint.

The exact squared distance from the center to the source boundary is
93/4+149phi/4 > 64. Every affine vertex at both interval endpoints has
squared radius <4, hence convexity bounds every intermediate radius by 2.
Also |delta|<2 throughout. Every omitted center lies outside the source
rhomb union, so its distance D from this center exceeds 8. Its power
inequality slack at every vertex is at least D^2-2DR-|delta|>30.
Thus omitted centers cannot cut the cell; this is an infinite-tail certificate
uniform on the whole stated interval. At the fixed sample a stronger local
bound R<1 is also checked.

This interval overlaps neither reviewed interval delta<=A nor delta>=-1/4.
It certifies an interior portion of the finite gap but leaves two gaps:
(A,-1/4-phi/2] and (-1/44-2phi/11,-1/4).
No conclusion about either remaining gap or the full family follows.
Stop after this first gate under section 5; no further sampling is authorized
by this artifact.

Reproduce with the adjacent Python script, or pass --check to compare its
exact recomputation against the JSON. Numeric polygon clipping only
proposes support indices; every claimed inequality, turn, interval endpoint,
and tail bound is checked in Sage exact algebraic arithmetic. The script
reconstructs and checks the original source and boundary before certification.
The only new artifacts are this report and its adjacent Python and JSON.
