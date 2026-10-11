# Independent hostile review: rational branching hexagon deformation

Date: 2026-10-10. Reviewer: partial_contacts, independent of construction.

**Final verdict: VALID for the exact quantified claims in the current lemma.**
This is a3D sufficient periodic family plus two finite branch patches. It is
not a general periodicity theorem, an aperiodic pair, or a proof that the
B-mate branch extends infinitely.

## Exact claim and assumptions reviewed

The raw definitions and proof in
[branching-hexagon-rational-deformation.md](../lemmas/branching-hexagon-rational-deformation.md),
the producer, search record and retained certificate were read. The reviewer
did not import or execute the author producer. Parameters a,c,r are arbitrary
real numbers in the stated strict homogeneous domain, not only the rational
fixture. Reflections, rotations, native whole tiles and species omission
remain allowed. The no-monohedral statements are restricted to the distinct
five-label subdomain, as required by their corner graphs.

## Full-cone convexity attacks

Checked edge closure from the raw rational linear formulas. E3 has positive
y and negative x throughout750c<1129a. The cross expression
c(4516a-3000c)/3125 is positive there, placing E3 strictly between E2 and
180 degrees. In B, the two strict determinants place F2 inside the sector
from F1 to F3, because this sector has width below180; their intersection
cannot select the complementary angular branch. Thus F2 is nonzero.
The remaining fixed edge directions have every turn in(0,180), including
F5 to F0 and the large A E3-toE4 gap. The standard supporting-half-plane
argument for a closed edge list with one complete strict turn is valid;
no self-crossing or hidden flat side remains.

All inequalities are strict. Boundary limits where a determinant vanishes
are excluded and are not silently claimed. The rational fixture lies
strictly inside all six constraints. The domain need not be assumed convex
or connected; the proof is pointwise throughout its stated cone.

## Actual links, cone angles and plane coverage

All12 reversed endpoint seam identities were reconstructed symbolically.
A separate DSU on24 corners finds8 classes of size3. Each class has a
single circular link, and following that link has zero exact translational
holonomy. Seam chart derivatives are identity because the displayed faces
are actual congruent placements and the identifications are translations.
The three positive convex sector angles therefore sum to an integer
multiple of360. Their sum is below540, hence exactly360, including all
parameter-dependent stars. The proof does not reuse equiangular120 sums.

The side-paired surface is connected, orientable, closed and has Euler
characteristic8-12+4=0, hence is a torus. Its complete flat universal cover
is EuclideanR2, so the lifted whole faces cover without interior overlap.
This prevents a locally legal seam diagram from being mistaken for plane
extension. The zero-shift seam graph connects all faces; u and v shifts
therefore give deck holonomy loops. Their exact determinant equals the
positive total face area2area(A)+2area(B). They are two independent periods.

At the retained fixture, the independent checker exhausts every integer
lattice shift in the exact transformed-coordinate bounding ranges,24
nonidentity translated face comparisons. Each is separated by a rational
supporting axis. Equal covolume and motif area independently verify the
same coverage claim. This fixture check is additional evidence, not an
extrapolation to the full cone.

## Whole branch patches and physical distinction

Both fixed matrices are exactly orthogonal, with determinants+1 and-1.
All10 stated native-side contacts were reconstructed as unordered endpoint
sets, respecting the reflected face orientation. The endpoint corner cones
are correctly assigned: in the B branch, R*B at the left endpoint occupies
[-180+t/2,0], H*B occupies[t,180+t/2], and A occupies[0,t]. These partition
the full circle. At the right endpoint the three cones are also the stated
partition, unchanged from the A branch.

Every whole convex tile lies in its endpoint cone. This separates every
pair involving a seam tile over the entire parameter domain. The remaining
filler pair is separated by x<=0 and x>=a, since the left cone lies inside
[90,270] and the right G cone inside[270,450]. Strict a>0 supplies separation.
The independent fixture SAT checks all12 unordered branch pairs as well.
No infinite extension of the B branch is asserted or inferred.

In the five-label domain the A repetition word has just one possible
nonidentity dihedral reflection. It exchanges corners0,1, whose angles t
and360-2t differ because cos(t)=-7/25 != -1/2. B has four unique labels and
no nonidentity dihedral symmetry. Different A/B length multiplicities prove
noncongruence. Hence the two physical neighbor patches remain distinct.

## Monohedral and non-affine scope

The cited defect-free hexagon limit theorem applies to a single species
and permits all partial contacts in the starting tiling. Its repaired
uniform sector-disk proof and valid fresh review are retained in the cited
source. In the resulting trivalent ETE limit, A's actual bc corner has
no possible third ray in its native corner graph, and B's rc corner has
no third ray in its graph. These exclusions include reflected faces.
They require distinct numerical a,c,b,r,s; the theorem states that condition.

E0 is horizontal but E3 has nonzero vertical component throughout a>0.
These opposite sides are not parallel. Affine maps preserve parallelism,
so neither A geometry belongs to an affine image of any equiangular120
hexagon. Irrationality of t/pi follows rigorously from the rational
noninteger root-of-unity trace2cos(t)=-14/25. No novelty inference is made.

## Defects, repairs and residual uncertainty

No substantive defect was found and no author repair was requested.
There is no remaining proof gap in the stated sufficient periodic cone
or finite physical branch claims. The imported hexagon limit theorem is
an explicit dependency of the no-monohedral exclusion, not of periodic
existence. Arbitrary repeated hexagon pairs and global B-branch extension
remain outside this review.

## Independent exact verifier

[verify_branching_hexagon_rational_deformation_independent.py](verify_branching_hexagon_rational_deformation_independent.py)
contains raw rational formulas and reads only the certificate for comparison;
there are no author imports or producer execution. It checks symbolically
all12 seams,8 actual links and their zero holonomy, determinant inequalities,
covolume identity and10 branch contacts. It independently checks fixture
strict convexity,24 exhaustive lattice comparisons,12 branch comparisons,
all12 intrinsic dihedral candidates per shape, and retained certificate
edge/vertex/period/link data. Arithmetic is exact Sage QQ[a,c,r] and QQ.

Replay completed successfully:

    conda run --no-capture-output -n arisearch python research/reviews/verify_branching_hexagon_rational_deformation_independent.py

Result: PASS: independent3D identities,8 actual links,10 branch contacts,
24 complete lattice/12 branch separations, certificate comparison.
Neither checker nor review mutates any retained certificate.
