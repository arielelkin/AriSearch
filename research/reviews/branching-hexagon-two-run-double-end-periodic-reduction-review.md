# Fresh independent review: actual double-ended contacts force periodic escape

**Verdict: VALID under the stated no-homogeneous-star and no-A–A-q-seam hypotheses.**

Reviewer: branching_hexagons, freshly assigned by root. Root proposed the middle-q normalization and is not its sole reviewer. Reviewed the actual [double-end theorem](../lemmas/branching-hexagon-two-run-double-end-periodic-reduction.md) freshly, including its stronger geometric argument rather than importing the earlier pending chain manuscript. The [independent checker](verify_branching_hexagon_double_end_independent.py) imports no author module and verifies the binary incidence/end cases and exact native closure factors. Compactness and full positive-cone constructions are separately reviewed dependencies.

## First saturation is legitimate and sufficient

Distinct p,q gives actual binary native side labels, and the two native length words distinguish A from B up to congruence. In the reviewed trivalent edge-to-edge limit, a homogeneous star would use only B pp or B qq corners, prohibited by the explicit repeated-angle test. Every other cyclic three-ray star has exactly two label changes, hence two mixed and one homogeneous corner. The independent checker enumerates all binary three-ray cycles and verifies this fact. Boundary incidence counts give N_A=N_B+O(R), while total count is Omega(R^2), so neither species can be absent.

No A–A q seam makes all A q incidences A–B. Comparing the three q sides of each species gives only O(R) B–B q seams. The defect estimate is uniform over translated squares because the two shapes have fixed bounded diameter and positive minimum area. For avoidance radius L, choosing R much larger than L^2 leaves a point outside all O(R) radius-L bad-midpoint disks and an appropriate boundary band. Letting L tend to infinity and using the reviewed admitted compactness yields a limit with no B–B q seam in any fixed compact set. If a seam intersects such a set, its midpoint is within a fixed additional tile diameter, so the expanding avoidance radii cover the full seam condition. Edge-to-edge trivalence and the forbidden local types persist through the fixed positive sector separation. This is a valid existence of a specially saturated limit, not a claim of pointwise absence from a sparse count.

## Pointwise qq normalization and actual endpoint assignment

All B q neighbors in that limit are A. Its qq stars are B+A+A, hence have angles120-2delta,120 or120+2delta. The120 value is forbidden by the repeated homogeneous qqq test. Crucially, the SAME A tile covers the whole B middle q4 side; that A q side has one H and one L endpoint. Therefore B4 and B5 are necessarily opposite low/high values. No second density or defect-limit argument is required. Reversing B's native traversal and restoring its pppqqq start exchanges B4/B5, allowing the stated normalization without changing the unmarked shape.

The independent endpoint table verifies that Bmiddlep1 cannot mate ANY B p side: some endpoint would have pp+pp, forcing a forbidden homogeneous ppp star. Thus p1 meets A. A third A at either end would create the prohibited A–A q seam, so the third tile is B mixed, forcing each outer p side to meet B. Such outer mates must exchange mixed/pp endpoint types; their other placement gives pp+pp at one end. The mate is p0 or p2 because no Bmiddlep may meet B.

Across Bq3 the actual A has H at B4 and therefore L at B3. Across Bq5 it has L at B5 and therefore H at B0. A reflection cannot change those numerical corner angles of the SAME whole-side neighbor. At the actual Bp0 seam its host B0 filler is thus fixed H. Same-slot mates contribute alpha and cross-slot mates beta, yielding respectively B0+alpha=240-delta or B0+beta=240-delta. The previously broader180+2delta phase alternative is genuinely excluded by these double-ended contacts.

## Native closure exhausts the possibilities

Writing t for the actual q3 direction, strict convexity and traversal give the q directions t,t+60+2delta,t+120 and phase rho=t-120+delta for the nonzero p-chain S. This fixes the phase branch by actual directions, without a principal-argument assumption. Hence B0=60+rho-delta and B3=420-rho+delta-alpha-beta.

A same-slot seam forces alpha+rho=180. Independently reconstructing S and the q-chain yields closure p*(exp(i*alpha)-1+exp(-i*beta))+2cos(delta)=0. In positive half-angle coordinates u=tan(alpha/2),v=tan(beta/2), its imaginary part is2*(u-v)*(1-u*v)/((1+u^2)*(1+v^2)). Thus beta=alpha or180-alpha are the only possibilities. Real closure and the strict B0/B3 upper bounds give exactly the previously reviewed equal-pp or complementary-pp open domains and p formulas.

A cross-slot seam instead forces beta+rho=180. Its independent closure imaginary part factors as4*u*v*(u-v)/((1+u^2)*(1+v^2)). Since0<alpha,beta<180 makes u,v positive finite, alpha=beta is forced. This independently confirms the manuscript's trigonometric factor and excludes another cross-slot branch. There is an actual Bp0 seam because B occurs, so these alternatives exhaust the necessary metric possibilities.

The already independently reviewed positive cones supply actual periodic escape tilings for both resulting families. No quotient is imposed on the original tiling, no periodicity of all tilings is claimed, and no pending whole-chain or bridge assembly argument is imported.

Completed readonly replay:

    conda run --no-capture-output -n arisearch python research/reviews/verify_branching_hexagon_double_end_independent.py

PASS binary vertex incidence, middle/outer p endpoint tables, H/L opposite endpoints, raw same/cross native closure and exact complete factor/real-branch equations. No substantive defect was found. The explicit no-homogeneous-star/no-A–A-q hypotheses and p!=q are essential; the gamma60 counterexample to an unconditional Bqq→twoA statement is correctly excluded. Families admitting the excluded contacts and the unrestricted two-polygon target remain open.
