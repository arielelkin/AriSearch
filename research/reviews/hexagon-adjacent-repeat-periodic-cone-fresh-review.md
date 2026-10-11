# Fresh hostile review of the branching repeated-length hexagon cone

**Verdict: VALID for the full constructive cone, the two-class adjacent-repeat
subfamily, its monohedral obstructions and its two local physical branches.**
Reviewer: `/root/penrose_extension_gate`, 2026-10-10. The reviewer authored neither
[the lemma](../lemmas/hexagon-adjacent-repeat-periodic-cone.md),
[producer](../searches/hexagon-adjacent-repeat-periodic-cone.py) nor
[certificate](../certificates/hexagon-adjacent-repeat-periodic-cone.json).
No theorem defect or missing strict-positive metric case was found. This is
an independent review of the current construction, not a use of the earlier
intrinsic-determinism or angle-only diagnostic claims.

## Full cone and genuine whole polygons

I independently reconstructed both native walks in Q(exp(pi*i/3))[p,q,a,c].
Solving the four closure equations in the rational basis (1,w) gives a
rank-four dependent-variable matrix and exactly

    b=p+a-c, d=q+a-c, r=p+2(a-c), s=q+2(a-c).

The eight positive quantities p,q,a,c,b,d,r,s are precisely the positive-side
domain of these two displayed formal words. There is no extra mirror constraint,
no assumption that labels are numerically different, and no hidden restriction
on the four free parameters. The cone is open, nonempty and four-dimensional.
It is a cone for this construction; it is not claimed necessary for unrelated
hexagon pairs.

The supporting-line identities at all six sides of each native walk were
checked symbolically. At cyclic offsets 2,3,4,5 their determinants divided by
sin(pi/3) are

    Li*Li+1, Li*(Li+1+Li+2), Li*(Li+1+Li+2), Li*Li-1.

All are strictly positive throughout the cone. These are global supporting
conditions, proving embedded strictly convex polygons and six actual
120-degree corners. The four placements are translations or half-turns and
remain counterclockwise. Coincident numerical lengths cause no convexity loss.

## Endpoint identities, actual links and full-plane covering

The new [independent checker](verify_hexagon_adjacent_repeat_cone_independent.py)
imports no author code. It derives all 24 directed side twins from reversed
native edges and actual integer shifts of the complex-coordinate periods,
rather than trusting the prescribed seam table. Each twin is mutually inverse;
there are precisely twelve undirected seams, agreeing with the certificate.
It follows the actual corner successor and gets eight circles of three corners
on three distinct reference faces. All 24 corners occur once, each circle has
angle 360 degrees, and each accumulated integer shift is (0,0). The zero-shift
side graph connects all four faces.

Thus the abstract quotient is a connected compact oriented surface with honest
local Euclidean charts, including the vertices. Numerical coincidences among
formal length roles do not change this selected quotient. Every seam coordinate
identity holds over the entire polynomial parameter ring. Positive corner
sectors and reversed edge endpoints ensure that the map to the displayed
lattice torus is locally Euclidean, not a many-times wound vertex link.

Independently, the checker verifies

    det(u,v)=sqrt(3)*(2pq+3pa+3qa+4a^2-pc-qc-4ac)
            =2area(A)+2area(B)>0.

The compact local map to R^2/(Zu+Zv) is a finite covering. This area identity
gives degree one and proves disjoint interiors and complete coverage of the
infinite plane by the displayed translates. It also validates the source's
equivalent complete flat universal-cover argument. Since the zero-shift graph
connects all faces, seams carrying u and v give actual holonomy loops; every
other seam shift lies in their integer span. These are a rank-two basis for
this quotient's deck group, while extra periods of the unmarked final tiling
remain possible as the source states.

No intrinsic-determinism premise is needed. Additional legal matchings after
length collisions do not destroy the existence of this particular torus.
If A and B are congruent the same quotient still tiles; the theorem properly
qualifies its exactly-two-class conclusion.

## Adjacent-repeat domain, reflections and monohedral exclusions

For p=a,q=c the exact positive domain is a>0,0<c<3a/2. Excluding c=a makes
all four numerical values a,b=2a-c,c,r=3a-2c distinct: every pair difference
is a nonzero multiple of a-c. A has multiplicities 3,2,1 and B has 2,2,1,1,
so they are noncongruent even under reflections. The determinant reduces to
sqrt(3)*(7a^2-c^2)>0. The endpoints c=0 and c=3a/2 have zero native lengths and
are outside the strict theorem. At c=a the shapes coincide as regular hexagons;
it remains covered by the general construction but not by the distinct-label,
monohedrally obstructed branching statement.

A vertex containing a 120-degree corner cannot also contain a straight
180-degree sector: 120m+180k=360 with m>=1 only has m=3,k=0. Consequently all
native vertices are three-corner vertices and all native-side contacts are
whole sides, including when reflections are allowed initially. The unordered
corner graphs are exactly the stated ones. A's actual bc corner cannot belong
to an A-only three-ray star, and B's actual rc corner cannot belong to a B-only
star. These are direct geometric local obstructions throughout the subfamily;
no external monohedral classification or limit deletion of a native corner
is used.

Independent enumeration of all twenty ray multisets gives exactly the nine
listed mixed possibilities. They describe local availability only. Reading
actual outgoing side labels around the eight quotient links gives aaa,abc,acr,
bbc twice each, as stated. Dihedral side-word enumeration, valid because the
four lengths are distinct, gives one nontrivial intrinsic reflection of A and
none of B; both have only the identity rotation. The coordinate identity
(x,y)->(a-x,y) realizes A's reflection. The two branch mates have different
congruence classes and cannot be identified by an intrinsic reflection quotient.

## Full-domain physical branches, not merely corner counts

The checker independently constructs the A mate, the rotated B mate, both
left fillers and the common right filler. It matches the retained coordinates
and verifies all five whole-side contacts in each patch, accounting for the
clockwise native order of the reflected left B filler. A native reflection
can preserve displayed endpoint order while reversing geometric boundary
orientation; the explicit endpoints show the contacts are legal.

For every a>0,0<c<3a/2, I checked whole-polygon containment in the source's
endpoint convex cones, with their actual origins and rays. At (0,0) the sectors
are [0,120], [240,360], [120,240], and at (a,0) they are [60,180], [180,300],
[300,420]. Every unit-ray supporting height is a homogeneous linear form in
a,c; exact nonnegative evaluation at c/a=0 and 3/2 proves its nonnegativity
throughout the interval. Strict convexity puts the polygon interiors in the
open sectors. The entire left filler has x<=0 and the right filler has x>=a.
These facts separate all six whole-tile pairs in either patch throughout the
full domain, not just near the seam endpoints or at one fixture.

Both native A side0 and the selected mate have the full segment [0,a] as their
matched side. The two endpoint stars are complete in each patch. The first
patch is precisely the selected four-face periodic motif and has a global
extension. The second is a genuinely different compatible finite whole-tile
patch. **Its infinite extension is not proved or asserted.** Thus the result
establishes physical local branching without promoting that branch to a
second infinite tiling.

## Exact replay and quantifiers

Successful commands:

```text
conda run --no-capture-output -n arisearch python research/searches/hexagon-adjacent-repeat-periodic-cone.py
conda run --no-capture-output -n arisearch python research/reviews/verify_hexagon_adjacent_repeat_cone_independent.py
```

The normal producer's stdout was captured and compared byte-for-byte with the
retained certificate; it matches, and all PASS checks are emitted on stderr.
The independent checker reconstructs the full formal and fixture coordinates,
periods, native words and closure matrix and checks the retained seam/link data.
At a=1,c=3/4 it independently recomputes all sixteen exact ordered-face-pair
lattice bounding records and every listed integer translate, giving 24 complete
nontrivial separating-axis comparisons. It also checks all twelve unordered
pairwise comparisons across the two local branch patches. Algebraic separation
allows boundary contact and handles the reflected clockwise polygon correctly.
The finite domains are exact overlap domains derived from lattice coordinates,
not an arbitrary neighborhood or bounded period search.

The theorem proves that **every metric in the displayed cone has a selected
periodic whole-plane witness**. It does not prove every admitted tiling periodic,
classify all repeated-side hexagon pairs, or extend every locally compatible
branch. The adjacent-repeat subfamily supplies two noncongruent, individually
untileable shapes with a periodic pair tiling and multiple physical local
neighbors. This is a valid constructive exclusion family for universal
aperiodicity and no more. No new research mechanism was launched by this audit.
