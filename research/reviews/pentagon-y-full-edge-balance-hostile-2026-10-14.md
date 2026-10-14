# Fresh hostile review of the pentagon Y full-edge torus balance

Date: 2026-10-14. Reviewer: sol_hexagons, independent of root derivation and
sol_ammann verification. Verdict: VALID after the angle-atlas correction.

Reviewed: [full-edge balance proof](../lemmas/pentagon-y-full-edge-torus-balance-2026-10-14.md) and
pentagon-y-equal-count-torus-obstruction-2026-10-14.py in this directory.
Root extracted the unchanged reviewed proof from its working review path. Independent reviewer checker:
pentagon-y-full-edge-balance-hostile-2026-10-14.py.

The first draft incorrectly described five stars as the angle-only atlas,
and its initial assertion failed. Exact angle enumeration gives seven:
aad, abg, ggr, bbcc, bcrr, ccdr, rrrr. The author corrected the manuscript
and checker to include the complete angle atlas followed by a separate
whole-native-edge arm-length gate. This gate excludes bcrr and ccdr. Fresh
independent enumeration over every cyclic ordering and both arm orientations
confirms precisely the five remaining stars. The corrected premise is valid.

Use x,y,z,t,w for counts of rgg,aad,bbcc,abg,rrrr, respectively. Actual face
corner incidences give x+4w=p, 2y+t=2p, 2z+t=2p, 2z=2q, 2x+t=2q, y=q.
These equations imply y=z=q, t=2p-2q, x=2q-p, p=q+2w. They count actual
corner occurrences, so repeated face indices at a quotient vertex cause
no change in the equations.

The new contact invariant withstands the endpoint-count objection. From
coordinates, each P has exactly two squared-length-4 sides with endpoints
r,a; each Q has exactly one squared-length-4 side with endpoints g,g.
The only atlas star containing two g corners is rgg. Independent arm-loop
enumeration forces its ray records to be gg squared-length 2 and two gr
squared-length 4. Hence Q's squared-length-4 GG side cannot pair another
Q side. Every Q GG side pairs a P RA side.

Every such Q-P edge has one gr endpoint and one ag endpoint, including
when both endpoints project to the same quotient vertex. Count these
endpoint incidences separately. Each rgg vertex contributes two gr
incidences, while each abg vertex contributes one ag incidence. Independent
enumeration forces the latter rays to be ab length-squared 5, ag 4, bg 2.
Since there are q Q GG edges, both endpoint classes have q incidences.
Thus 2x=q and t=q. This counts one endpoint of each class per edge;
it does not mistake edges for twice-counted corner incidences.

Solving the full exact linear system gives

    (x,y,z,t,w,p,q) = w(2,4,4,4,1,6,4).

The reviewer checker confirms the coefficient matrix has a one-dimensional
nullspace with exactly this vector. Integer vertex counts imply integer
w; positive face counts require w>=1. Consequently every finite full-native-
edge flat torus has P count divisible by 6 and Q count divisible by 4, with
ratio 3:2. Ten faces is the smallest count permitted by this necessary gate,
not a demonstrated ten-face tiling. The Euler identity is consistent.

Reflections reverse arm ordering and were all included in local enumeration.
Loop edges, repeated vertices and self-adjacencies do not invalidate incidence
counting, because the quotient metric still has circular vertex links and
native corner occurrences counted with multiplicity. No orientation or
period lattice hypothesis stronger than the stated flat torus is used.

Scope: finite flat tori formed from entire native sides only. Partial contacts
can subdivide the length-4 sides and alter vertex sectors, so this theorem
does not exclude unrestricted periodic tilings or unrestricted infinite
coverings. No infinite frequency extrapolation or universal recognition is
asserted. A non-edge-to-edge periodic covering could evade this gate.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/pentagon-y-full-edge-balance-hostile-2026-10-14.py

Completed successfully. The fixed 2P+2Q attack stops analytically, without
pairing enumeration or enlarged bounds. Changing equal counts or native
whole-edge gluing is necessary before restarting that attack.
