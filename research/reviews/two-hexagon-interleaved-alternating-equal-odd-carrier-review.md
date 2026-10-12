# Independent hostile review: equal-odd triangular carrier

Reviewed: [root carrier proof](../lemmas/two-hexagon-interleaved-alternating-equal-odd-carrier.md).
Verdict: valid for the stated actual strictly convex polygons and reflected
copies. This is a full-plane periodic escape, not just a patch.

The native direction sequence is consistent with every p/q corner,
including the final return at corner0. Summing its three odd vectors gives
`l sin(theta)(sqrt3,1)`, so closure indeed forces
`a0=a2−d, a4=a2+d`. The three even supporting lines form a60-degree
triangle. At a cut endpoint of angle p the removed-triangle angle is
alpha; at q it is beta. The sine law therefore gives carrier-side tails
Q at p endpoints and P at q endpoints. Side0 has Q,Q tails, side2 P,Q,
and side4 P,P. The three stated carrier lengths agree exactly.

P,Q>0 follows from |theta|<30, and the intervening even side lengths
are strictly positive by hypothesis. Thus the cuts lie on the carrier
edges in the required order; they do not extend beyond a carrier vertex
or cross another cut. The explicit carrier triangle coordinates agree
with its base endpoints and equilateral altitude. Actual convex A is
precisely the retained intersection, so no slit or missing sector occurs.

The reflection assignment is globally consistent. The proper colouring
`m+2n mod3` assigns distinct colours at each elementary carrier triangle.
Across an edge the shared two vertex colours are fixed and the opposite
vertex has the same remaining colour. The unique colour-preserving
triangle isometry on the adjacent chamber is exactly reflection across
that edge. This gives an explicit assignment independently of any path
of reflections and removes a possible monodromy concern.

At a carrier vertex each of its six removed triangles lies in a distinct
60-degree sector. Reflection identifies the cut endpoint along each
shared radial edge, including its distance from the vertex. Hence they
form one simple six-sided hole rather than separate slits or overlapping
regions. Adjacent A endpoints have identical native p or q angles, so
the hole angle is r or s. Each odd cut has one endpoint of each kind,
forcing the six hole angles to alternate. Their strict range (60,180)
and the simple boundary prove convexity. Equal positive side lengths and
the cyclic angle word determine the actual B uniquely up to isometry.

All removed corner pieces belong to exactly these vertex holes. Filling
them covers the plane, with disjoint interiors and whole-side seams.
Colour-preserving carrier translations preserve every assigned A and B
placement; three times each basis vector is an explicit period pair.
The construction therefore respects actual metrics, including arbitrary
positive even lengths allowed by closure, not merely an angular SFT.

The private-seam lemma is needed only to infer equal B side lengths from
a previous legal tiling. Once those lengths and angles are fixed, the
carrier construction stands alone. It does not require or force the
original tiling to use this carrier. No scope correction needed.
