# Flat-star endpoint eligibility prevents an angle-only full-seam exclusion

Status: exact local obstruction; fresh review pending.

Work with unmarked strictly convex polygons, allowing reflections,
arbitrary native vertex valence and partial contacts. A flat star has one
side-interior incidence of angle180 degrees and a multiset S of native
corner incidences whose angles sum180 degrees. Call a native corner
flat-eligible if it occurs in some such S. Eligibility here concerns angle
stars only; no length or placement realization is assumed.

**Claim.** If both native endpoints of an edge are flat-eligible, angle-star
constraints alone cannot prohibit that edge from meeting a full copy of
the same native edge, in either reflected or half-turn endpoint order.

Let endpoint corners c,d have angles alpha,beta. Choose native incidence
multisets S_c,S_d, of total angle180 each, containing c,d respectively.
Then

    2 S_c and 2 S_d have total angle360,
    S_c+S_d has total angle360.

Their remaining multisets after removal of2c,2d, or c+d are nonnegative.
Thus a reflected edge pairing has angle-legal completions at its two
endpoints using2S_c and2S_d; a half-turn pairing has completions at both
endpoints using S_c+S_d. Put the two prescribed edge-neighbour sectors
adjacently in the cyclic star and place the remaining positive sectors
around them. Strict convexity ensures each prescribed angle is below180.
This is an allowed full native star in the angle-only language.

In particular, a three-acute flat star

    alpha+beta+gamma=180

always supplies the full six-corner star

    2alpha+2beta+2gamma=360.

It contains both2alpha and2beta and also alpha+beta, so replacing equal
acute endpoints by distinct or algebraically generic acute endpoints does
not remove the full same-native-edge endpoint completions if both remain
in that flat star. The doubling/addition identities persist under every
generic perturbation preserving the intended flat relation.

The claim does **not** construct a geometric neighbourhood of that edge:
lengths and nearby polygon interiors could obstruct its extension. It does
not prove a periodic patch, strip or plane. It excludes only the proposed
mechanism in which angle-star constraints themselves prohibit the full
pairing. At least one endpoint must cease to be flat-eligible, or an
additional actual metric/geometric constraint must supply the exclusion.
Forbidding high-valence native stars would change the claim's hypotheses;
such a restriction has no justification for unrestricted polygon tilings.

## A consistent positive-T pentagon inventory exists

The obstruction is not a blanket acute-angle inventory impossibility.
Here is a distinct-angle two-pentagon inventory with a positive formal
T density. Let alpha+beta+gamma=180 and set

    x=180−alpha/2,
    z=180+gamma+alpha/2−y,
    delta=y+alpha/2,
    u=360−2y,
    w=360−z−v.

Use A=(alpha,beta,x,y,z), with alpha,beta adjacent on its designated
long edge, and B=(gamma,delta,u,v,w). Both angle sums are540. For example

    A=(65,75,147.5,112,140.5),
    B=(40,144.5,136,105,114.5).

All angles lie strictly between0 and180, with three distinct acute
angles alpha,beta,gamma. For the native corner inventory of2A+1B, use
one of each star below:

* flat(alpha,beta,gamma), of native angle sum180;
* full(x,x,alpha), of angle sum360;
* full(z,delta,beta), of angle sum360;
* full(y,y,u), of angle sum360;
* full(z,v,w), of angle sum360.

These consume every native corner exactly once: the T consumes one
alpha and beta from the two A copies and gamma from B; the remaining
four stars consume all remaining corners. Native angles sum
`4*360+180=3*540`. Counting the flat incidence too gives five physical
vertices with total angle5*360. Thus the formal frequency ledger permits
one T per three tiles, and the inventory has an open parameter region
with the same strict angle bounds. This is an angle ledger, not a plane
tiling or even an exact contact patch.

Despite that consistency, the unavoidable full star
`(alpha,alpha,beta,beta,gamma,gamma)` remains angle-legal. Hence this
inventory cannot enforce partial long-edge contacts by the requested
angle-only blocking rule. Coordinates or a larger search for that rule
would not repair the exact local obstruction.
