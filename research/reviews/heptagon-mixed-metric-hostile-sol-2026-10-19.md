# Hostile review: mixed heptagon metric obstruction

Date: 2026-10-19. Verdict: **PASS for the two stated exclusions**, conditional on the cited reviewed complementary-angle necessary theorem. The four other mixed words remain unresolved. No counterexample or substantive flaw was found.

Reviewed artifact: `research/searches/heptagon-mixed-qq-mechanism-sol-2026-10-19.md` and its adjacent Sage replay. No Git or log files were edited.

## Independent reconstruction

Index vertices 0 through 6 counterclockwise, with vertex 0 labeled A, and let side j go from vertex j to vertex j+1. Its heading increases at vertex j+1 by 180 minus that vertex angle. With d=126−alpha, the B turn is 54+d, the C turn is 54−d, and the closing A turn is 36. Summing turns independently gives exactly the two heading rows in the producer. Reversing the cyclic word changes the orientation convention, without altering whether a positive-length polygon closes.

At the unique A, both incident Q sides face pentagons in a PPA star. At each subsequent B or C in a defect-free tiling exactly one incident side faces Q. Propagating this binary choice around the six-corner run forces sides 1,3,5 to face Q and sides 0,2,4,6 to face P. The latter lengths are one. For both words side 1 is BB and side 5 is CC. Side 3 is BC for ABBBCCC and CB for ABBCBCC. These labels are indexed independently of the producer's formulas.

Every QQ endpoint is a PBC vertex, so the angle on the other Q must be the complementary label. Thus BB can meet only CC, forcing their lengths to agree for the single fixed Q metric. BC can meet only a BC/CB side with complementary labels at corresponding physical endpoints. A reflected neighboring copy does not change this endpoint fact. Allowing arbitrary reflection choices therefore cannot evade x=length(side 1)=length(side 5)>0. No equality between x and the remaining length z is needed.

## Direct sign check over the whole real interval

Put U=e(162+d). Cross products of U with the four unit sides give, independently by sine addition,

- sides 0 and 6: sin(−162−d)+sin(162−d)=2 cos(18) sin(d);
- sides 2 and 4: sin(−54+d)+sin(54+d)=2 cos(54) sin(d).

Their sum is strictly positive for every real 0<d<18. The two x sides contribute sin(−108)+sin(108)=0. For ABBCBCC the z side is parallel to U and contributes zero. Closure is impossible even with signed x,z. For ABBBCCC it contributes z sin(2d), also positive when z>0. Equivalently closure forces z=−(cos(18)+cos(54))/cos(d)<0. All divisions and strict signs are valid throughout the stated open interval, including d=6 (alpha=120). Reflecting the entire polygon reverses every cross-product sign together and preserves both contradictions. Neither argument relies on sampled parameters or a convexity relaxation.

The exact Sage replay was run through the required environment wrapper and returned `PASS: exact formal all-parameter closure obstructions for ABBCBCC and ABBBCCC`. Its cyclotomic angle unit is 18 degrees, so the use of CyclotomicField(20) and w^5=i is consistent.

## Resonance and the inference to untileability

For either word b=c=3. At alpha=120, the theorem's B/C incidence equations imply 3 times the number of BBB vertices in a square is O(R). The constants can depend on the fixed metric. Each defective tile touches one of these vertices, with at most three tiles per vertex, so the number of defective tiles meeting an enlarged square is also O(R). For any fixed disk radius r, their r-neighborhoods have O_r(R) area. They cannot cover the interior of squares of area proportional to R squared. Choosing successively larger squares yields defect-free disks of arbitrarily large radii.

Translating those disks and taking a local subsequence is valid for the fixed finite prototile set: positive tile area and bounded diameter bound the number of tiles meeting each fixed window; rigid-motion parameters then have convergent subsequences. Nonoverlap and coverage pass to the limit. One may also stabilize the finite contact incidence data on each window, so a new BBB contact cannot appear from a varying contact pattern in the limit. The resulting plane tiling has only PPA and PBC stars. A pentagon-only limit is impossible because 108-degree pentagon corners cannot form a full vertex (nor a permitted side-interior contact). Hence the limit contains Q and imposes the same intrinsic side constraints on the original fixed Q. Applying the closure contradiction to this purified tiling legitimately excludes the original resonant tiling as well.

The conclusion is consequently untileability of each fixed pair P,Q in the stated angle-word classes and open alpha interval, under unrestricted contacts and arbitrary isometries. It does not assert that the angle words themselves have no convex metric realization: it rules out realizations satisfying the necessary tiling metric constraints.

## Remaining words and global mechanism

The directed BB-to-CC seam graph has one incoming and one outgoing seam at each Q, and the remaining BC seams form a matching. Strict convexity rules out two distinct copies sharing two different full sides. Thus the asserted cycle-or-double-infinite-strand decomposition is sound. It imposes no proven geometric axis, holonomy commutation, finite quotient, or plane extension. The producer explicitly declines those inferences and correctly leaves ABBCCBC, ABBCCCB, ABCBBCC, and ACBBBCC unresolved.
