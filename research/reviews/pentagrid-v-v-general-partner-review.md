# Fresh hostile review: arbitrary V pentagons have periodic V partners

**Verdict: VALID.** Root reviewed the new
[general double-Y theorem](../lemmas/pentagrid-v-v-general-double-y-partners.md)
on2026-10-10 and did not develop its algebra, patch, winding proof or partner
formula. The reviewer independently reconstructed both native walks and all
formal boundaries in the [fresh verifier](verify_pentagrid_v_v_general_partner_independent.py),
importing no author code.

The complete positive cone is correct. B closure uniquely gives
l=phi*(x+k)-f and m=phi*(f-x)-k; positivity gives the two bounds on f.
A closure gives r=phi*(x+f)-y and e=f+phi*(x-y); e positivity gives the
bound on y, while r-f=x/phi+(x+f/phi-y)>0. This last strict inequality
uses the actual unique72-to72 side to exclude congruence, including reversal.
No hidden old mirror-parameter positivity is retained. All positive closed
native walks have strictly cyclic edge directions and therefore strict
supporting half-planes, justifying the general convexity claim.

The independent formal checker starts with native walks based at0 and places
them from the prescribed exposed vertex and central spine. It then cancels
opposite directed edge pairs without using the author's seam table. Exactly
five internal pairs disappear and ten exterior native edges remain. Their
actual successor graph is one cycle. Removing formally collinear vertices
gives exactly the six macro vertices, with central symmetry and the declared
periods. Thus the winding identity is a geometric oriented-chain equality,
not an assumed topological cut tree. All four child loops are positively
oriented convex polygons, so their nonnegative winding numbers prove
containment, absence of every interior overlap, and degree-one coverage.
Boundary closure gives coverage at every point, including seam crossings.

The macro's side lengths y,e+l,m+r are positive. The determinant is exactly
y*(e+l)+phi*y*(m+r)+(e+l)*(m+r)>0. The usual three opposite side pairs
have the reviewed central-hexagon links, each containing72,144,144. The
specified map to the ordinary period lattice torus is a local isometry and
its macro area equals the lattice covolume. Consequently its degree is1,
which proves the stated infinite coverage and independence of both periods.
Native partial contacts across carriers are permitted by the original
problem and do not invalidate the macro gluing.

The fresh fixture verification uses separating supporting edges, rather
than the author's clipping method. It derives the complete inverse-lattice
bounding boxes and checks all56 possible nontrivial intersections, including
self-translates. Every pair is separated. The domain agrees exactly with
the retained list. Replay passed:

    conda run --no-capture-output -n arisearch python research/reviews/verify_pentagrid_v_v_general_partner_independent.py

For any prescribed positive V pentagon, its two real closure equations are
exactly the B equations. Therefore its actual metrics supply admissible
x,k,f, and the interval for y is nonempty. The mirror choice y=x always
lies strictly inside it. Changing y changes the unique72-to72 edge length,
so the continuum of partners is pairwise noncongruent. The reflected partner
uses the other144-to108 adjacent side, as stated. These are constructive
existence claims about a chosen partner. They do not classify the tiling
space of an unrelated pair containing the same V. I attacked that quantifier
upgrade and found it explicitly excluded.

No defect, numerical dependence, unproved patch extension, or concealed
edge-to-edge convention remains. The generic aperiodic-pair problem and
arbitrary V/V pairings remain unresolved. No novelty assertion is reviewed.
