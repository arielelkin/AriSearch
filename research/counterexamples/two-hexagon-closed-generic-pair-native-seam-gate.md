# Actual generic convex hexagons can fail before a B ring closes

Date:2026-10-13. Geometry status: independently reviewed VALID;
[review](../reviews/two-hexagon-001221-rational-unit-geometry-review.md).
Spatial obstruction status: independently adversarially reviewed VALID;
[ring review](../reviews/terra-001221-native-ring-fresh-hostile-review.md). No infinite mixed covering is asserted.

## Exact pair

Let U=(3+4i)/5. Let V be the unique root in the rectangle
299/1000<Re(V)<300/1000 and954/1000<Im(V)<955/1000 of

    f(X)=X^12-113X^11/25+14833X^10/2000+11961X^9/2500
         -366807X^8/62500+395647X^7/312500+66847X^6/125000
         +395647X^5/312500-366807X^4/62500+11961X^3/2500
         +14833X^2/2000-113X/25+1.

The independent checker verifies irreducibility, unique isolation, unit
modulus and the intended complex embedding. Set W=-1/(UV). All U,V,W
have positive real and imaginary parts and unit modulus; their arguments
u,v,w are in(0,90) degrees and sum180.

Set S0=1+U, S1=UV(1+V), S2=U^-1-V. With cross(P,Q)=Im(conjugate(P)Q),
put r0=cross(S1,S2),r1=cross(S2,S0),r2=cross(S0,S1), and

    a=1, b=r1/r0, c=r2/r0.

All lengths are positive and pairwise distinct. Define A by cumulative sums
starting at0 of the edge vectors

    (a,aU,bUV,bUV^2,-cV,-cVW).

Define B similarly using edge directions

    (1,-U^-2,(UV)^-2,-1,W^-2,-U^2)

and lengths(a,a,b,c,b,a). Both sums are exactly zero, and all48 strict
nonincident supporting inequalities for the two polygons are positive.
Their native angle words are A001122 and B001221, with
A=(180-u,180-v,180-w) and B=(2u,2v,2w) as colour angle types.
The complete trivalent language is exactly the five generic ternary types.
Both actual polygons fail every cyclic/reflected Reinhardt H1/H2/H3
criterion, so neither tiles monohedrally under the imported unrestricted
classification. For orientation only, b is about1.19983029478 and c about
0.79640113273; these decimals are not defining data.

[Independent checker](../reviews/verify_two_hexagon_001221_rational_unit_independent.py),
[exact slice certificate](../certificates/two-hexagon-001221-rational-unit-slice.json).
The full root slice has six complex roots before filters; exactly one unit
acute branch survives. A prior high-degree slice U=exp(67degrees i) was
interrupted after six roots were reported but before geometric filtering;
its interruption record is retained separately and gives no geometric verdict.

## What this geometry falsifies

The general001122aabbcc family does not force all metrically closed B
words to be012012 or centrally symmetric. The fixed(113,121,126) fixture's
central-only B closure result cannot be extrapolated to all angles. The
actual polygons here have the same generic star language, compatible endpoint
palettes and closed positive convex boundaries, yet a further native spatial
gate is necessary. Positive angle balance and joint polygon realization are
still weaker than infinite tilability.

## Native seam obligation

No ABB stars occur, so any genuinely mixed defect-free field must isolate
B among six A neighbours. Endpoint-colour pairs determine its A neighbour
side uniquely. The two equal-colour B edges00 and22 permit two reflected
native choices each; all other edges permit one. Hence exactly48 full
indexed rings(12 B placements times4 tuples) meet the AB endpoint conditions.
The independent checker verifies that each has one a/c and one b/c
unequal AA seam for distinct a,b,c. This local empty certificate excludes mixed fields
at every actual geometry with these native class words. Since neither tile
has a monohedral escape, the present exact pair is then untileable.
The geometry and spatial obstruction have separately completed independent
reviews. The exact pair is untileable. No aperiodic
candidate, periodic witness or infinite extension follows from the algebraic
closure slice itself.
