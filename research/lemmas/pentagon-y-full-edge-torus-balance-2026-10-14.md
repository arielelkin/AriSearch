# Full-edge flat-torus balance for the interface-first Y pentagons

Date: 2026-10-14. Status: **independently hostile-reviewed VALID** on the full-native-edge finite flat-torus domain. No pairing census performed. See the [fresh review](../reviews/pentagon-y-full-edge-balance-hostile-2026-10-14.md).

**Theorem.** For the exact P and Q below, any finite flat torus made by gluing whole native sides of copies of P and Q has face counts p=6w and q=4w for a positive integer w. Reflections are allowed. This is necessary only, and no such torus is constructed.

The proposed bounded attack was a flat torus made from 2P+2Q, pairing only equal-length full native sides and admitting every face reflection. Before its 23,625 length-pairing cases were enumerated, the root supplied a corner-count obstruction. This artifact independently verifies it and stops the attack at that gate.

Use the P and Q coordinates in [the Y interface checker](../searches/pentagon-y-interface-2026-10-14.py). Independently read off their counterclockwise corner labels as P=`rabba` and Q=`cggcd`. In the basis `(pi/4,theta)`, theta=atan(2), the angles are r=(2,0), a=(4,-1), b=(1,1), c=(3,-1), g=(3,0), d=(0,2). Theta/pi is irrational: if it were rational, exp(2i theta) would be a root of unity, so its trace 2cos(2theta)=-6/5 would be a rational algebraic integer, which it is not.

Every corner angle exceeds 60 degrees and is below 180 degrees. Thus a full native vertex has two to five corners. Exact coefficient enumeration gives seven unordered angle stars: `rgg`, `aad`, `bbcc`, `abg`, `rrrr`, `rrbc`, `rccd`. Full-side length compatibility excludes the last two. In `rccd`, r's two length-2 arms have no matching arm at any other corner. In `rrbc`, the two r corners may match each other on one ray, but their remaining length-2 arms cannot match b or c, whose arms have squared lengths 2 and 5. Thus the length-compatible native atlas consists precisely of the first five stars. The independent checker allows every cyclic order and reflected arm order in verifying this five-star atlas.

Let p,q count faces and let x,y,z,t,w respectively count those five stars. Native corner incidence gives

    x+4w=p, 2y+t=2p, 2z+t=2p,
    2z=2q, 2x+t=2q, y=q.

Consequently y=z=q, t=2(p-q), x=2q-p, and **p=q+2w**, t=4w. If p=q, both `rrrr` and `abg` are absent. The fixed 2P+2Q experiment therefore has the only possible star-count tuple `(x,y,z,t,w)=(2,2,2,0,0)`.

Every P has native length-2 sides joining r to a. Only P r-a sides and Q g-g sides have this length. A full-side contact of two P r-a sides either identifies r with a at its endpoints, which no atlas star permits, or identifies r with r and a with a, which requires the forbidden `rrrr` star at the r-r endpoint. A full-side contact with Q identifies a with g at one endpoint, which requires the forbidden `abg` star. Thus none of these P sides can be covered. The contradiction applies regardless of face chirality, pairings elsewhere, loop edges, or torus holonomy.

The conclusion is stronger than exhaustion of the fixed four-face domain: **no finite flat full-edge torus with equal positive P and Q counts exists**. It does not exclude arbitrary partial-side contacts, unequal-count tori, or an infinite covering. It also does not exclude finite gluings with cone singularities; those do not provide the sought Euclidean plane cover.

## Stronger necessary ratio from ray lengths

The root subsequently proposed a stronger invariant, independently checked here. At r both native arms have squared length 4; at g the arm lengths squared are 2 and 4. Therefore, in a length-compatible `rgg` star, each r-g ray must have squared length 4 and the g-g ray must have squared length 2. A Q g-g side of squared length 4 consequently cannot pair with another such Q side: their endpoint g-g adjacency has no length-compatible star. Every Q length-2 side pairs to a P r-a side instead.

There are exactly q such Q sides and hence q P-Q length-2 seams. Every such seam has one r-g endpoint and one a-g endpoint. Each `rgg` star supplies exactly two r-g seam endpoints. Each `abg` star supplies exactly one a-g seam endpoint, because the three ray lengths are forced: r is absent, G-A has squared length 4, A-B has squared length 5, B-G has squared length 2. Therefore **2x=q and t=q**. Combining this with the native incidence equations above gives

    p=6w, q=4w, x=2w, y=z=t=4w.

Thus every finite positive full-native-edge flat torus must use face ratio P:Q=3:2, with counts multiples of 6 and 4. The smallest count permitted by these necessary conditions has ten faces. This is only a necessary condition, not an existence claim, and no ten-face gluing experiment was executed at this earlier count-gate stage. The later user-authorized [6P+4Q CP-SAT experiment](../searches/pentagon-y-6p4q-flat-torus-cpsat-2026-10-14.md) returned INFEASIBLE; the subsequent [native propagation theorem](pentagon-y-whole-edge-native-propagation-2026-10-14.md) excludes all whole-edge plane tilings. The rule depends on full native side matching; it is not asserted for partial contacts or for general infinite tilings.

The independent checker imports neither the atom module nor its enumeration. It verifies coordinates' length-2 endpoint labels, the exact five-star atlas, absence of the necessary endpoint completions, and the unique count tuple for 2P+2Q. Its tiny count loop is bounded by six possible torus vertices, rather than an enlarged geometric search.

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/pentagon-y-equal-count-torus-obstruction-2026-10-14.py

The mathematical assumption that must change before restarting this attack is equal face counts or the full-native-side gluing model. After enforcing the additional ray-length invariant, the necessary count rule first permits p=6,q=4, but this count-gate stage did not execute that ten-face experiment. The subsequent user-authorized experiment and stronger propagation proof linked above supersede this finite-domain restart. No plane-covering or recognition milestone has been reached by this gate.
