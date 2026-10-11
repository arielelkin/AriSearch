# Double-ended q contacts force the two known periodic cones

Status: **independently adversarially reviewed VALID**; see [the fresh review](../reviews/branching-hexagon-two-run-double-end-periodic-reduction-review.md). This is a conditional global reduction for a broader binary two-run family, derived from actual contacts. It does not classify pairs admitting homogeneous stars or A–A q seams. The positive constructions it uses have separate independent reviews. No fixed eight-face carrier is assumed in the necessity argument.

## Exact statement

Fix 0<delta<30 and positive distinct p,q; normalize q=1 by common scale. Let A have side word (p,q,p,q,p,q), directions (0,60+delta,120,180+delta,240,300+delta), and alternating angles A_H=120+delta,A_L=120-delta. Let B be a strictly convex closed hexagon with native word (p,p,p,q,q,q), native pp angles alpha=B_1,beta=B_2 and qq angles B_4,B_5.

Assume (i) no three B pp corner angles, with repetitions permitted, sum to 360, and no three B qq corner angles do; and (ii) no A–A q seam is geometrically possible in an edge-to-edge trivalent tiling by these shapes. A sufficient explicit angle test for (ii) is that neither alpha nor beta is 120 and the set {alpha,beta} does not contain both 120-2delta and 120+2delta.

If any unrestricted tiling by A and B exists, then, after choosing B's native direction of traversal, B belongs to one of these two metric families:

1. **Equal pp angles:** alpha=beta, gamma=180-alpha, 0<gamma<120-delta,
   p=2cos(delta)/(1+2cos(gamma)), with B angles
   (60+gamma-delta,180-gamma,180-gamma,60+gamma+delta,120-2delta,120+2delta).
2. **Complementary pp angles:** beta=180-alpha, 60-delta<alpha<120-delta,
   p=2cos(delta), with B angles
   (240-alpha-delta,alpha,180-alpha,60+alpha+delta,120-2delta,120+2delta).

Both families have actual doubly periodic tilings by the independently reviewed eight-face construction. Therefore a pair under these hypotheses either is untileable or has a periodic tiling. It cannot witness the unrestricted two-prototile aperiodicity target.

The necessity result is for an actual tiling admitted through the reviewed compactness theorem. It does not infer a tiling from a feasible local angle system, and it does not assume the known constructive quotient is present in the original tiling.

## 1. Actual all-A–B q limit

Use the reviewed theorem in `research/lemmas/hexagon-limit-and-periodicity.md` to pass from an unrestricted tiling to an admitted everywhere trivalent edge-to-edge tiling. In a trivalent vertex without a homogeneous star the three seam labels p/q change twice cyclically, so exactly two corners are mixed and one is homogeneous. A has six mixed corners per tile; B has two mixed and four homogeneous corners. Counts in a square of radius R have O(R) boundary error because shapes are fixed, of positive area and bounded diameter. Thus

    6N_A+2N_B=2V+O(R),    4N_B=V+O(R),    N_A=N_B+O(R).

The total tile count is Omega(R^2), so neither species can be absent. Assumption (ii) makes every A q side meet B q. The q-incidence counts give

    3N_A=E_AB,q+O(R),    3N_B=E_AB,q+2E_BB,q+O(R),

and E_BB,q=O(R). This is not pointwise absence in that tiling. To obtain actual absence, for every avoidance radius L choose R sufficiently large compared with L^2. The union of radius-L disks around O(R) bad q-seam midpoints has area O(RL^2), smaller than the available inner square area after excluding a boundary strip. Choose a remaining translation center, let L tend to infinity, and take the admitted compactness limit. Every fixed compact neighborhood in this further limit has only A–B q seams. The fixed positive sector separation from the reviewed theorem prevents vertex degeneration and preserves trivalence and whole-side matching.

The remainder uses only this first saturated limit. The later A–B p/middle-q saturations in `branching-hexagon-two-run-saturated-chain-transport.md` are unnecessary for this stronger argument.

## 2. Actual qq stars and native normalization

At either qq corner of B both q neighbors are A, so the actual vertex star is B+A+A. Its angle must be 120-2delta,120, or120+2delta. The value120 is excluded by (i), since three repeated copies of that qq corner would sum to360.

The same A tile is adjacent along the whole B middle q4 side, whose endpoints are B_4 and B_5. At each endpoint its corner belongs to an HH or LL pair. That A q side has one H and one L endpoint. Therefore one B qq angle is low and the other high, pointwise, without an additional density argument. Choose B's native traversal direction so

    B_4=120-2delta,    B_5=120+2delta.

At B_4 the two A corners are both A_H; at B_5 both are A_L.

B's p1 side has pp angles at both ends. If it met any B p side, some endpoint would have two pp corners, making the third corner pp and violating(i). Hence p1 meets A. At either endpoint of p1/A, a third A would create an A–A q seam and violate(ii). The third tile is B at a mixed corner, so both p0 and p2 of every B meet B p0 or p2. Each such seam must match mixed to pp at both endpoints: otherwise one endpoint has two pp corners and a forbidden homogeneous star. There is at least one actual B p0 seam because B occurs.

## 3. The missing double-end constraint

Consider the A tile actually adjacent to B's q3 side. At its endpoint B_4, its A corner is A_H. An A q side has exactly one A_H endpoint and one A_L endpoint. Therefore at the other endpoint B_3 the **same A tile** supplies A_L. This conclusion uses the whole q-side contact, not just the qq star at one endpoint.

Similarly the A tile adjacent to B's q5 side supplies A_L at B_5, so it supplies A_H at the other endpoint B_0.

Consequently at every B p0/p2 seam the endpoint filler at a host B_0 is fixed to A_H, and the filler at host B_3 is fixed to A_L. The offset phase alternative allowed by independent angle sums is geometrically impossible. At B_0 the B–B seam has these exact possibilities:

- A same-slot p0–p0 mate supplies native pp angle alpha. Thus B_0+alpha=240-delta.
- A cross-slot p0–p2 mate supplies native pp angle beta. Thus B_0+beta=240-delta.

Mirror choice cannot change which pp angle belongs to a given native side. It only determines the unique mixed-to-pp endpoint placement. These necessary conditions follow from actual double-ended q placement.

## 4. Native closure and the same-slot case

Set the native B first directed edge to direction0, and write

    u=180-alpha,    v=360-alpha-beta,
    S=1+exp(iu)+exp(iv).

The p-chain is pS and is nonzero because the q-chain below is nonzero. If the q3 direction is t, the fixed low/high qq angles make the q-chain directions

    t,    t+60+2delta,    t+120.

Their sum is 2cos(delta)exp(i(t+60+delta)). Closure gives a phase rho=t-120+delta for S; with this actual phase branch the mixed angles are

    B_0=60+rho-delta,
    B_3=420-rho+delta-alpha-beta.

The same-slot condition therefore forces alpha+rho=180. Multiplying the exact closure equation by exp(i alpha) gives

    p[exp(i alpha)-1+exp(-i beta)]+2cos(delta)=0.

The imaginary part is sin(alpha)-sin(beta)=0. For alpha,beta in(0,180), sine equality implies beta=alpha or beta=180-alpha.

If beta=alpha, the real equation gives p=2cos(delta)/(1-2cos(alpha)). The strict upper bound B_3=240+delta-alpha<180 gives alpha>60+delta, and strict convexity also gives alpha<180. Equivalently gamma=180-alpha belongs to(0,120-delta), giving the equal-pp cone.

If beta=180-alpha, the real equation gives p=2cos(delta). The mixed angles become B_0=240-alpha-delta and B_3=60+alpha+delta. Their strict upper bounds give exactly60-delta<alpha<120-delta; all other strict angle bounds follow. This is the complementary-pp cone.

## 5. The cross-slot case cannot add another branch

A cross-slot p0–p2 seam forces beta+rho=180. Its other endpoint also gives B_3+alpha=240+delta. Consequently B's three q directions are300-beta-delta,360-beta+delta,420-beta-delta. Multiplying exact native closure by exp(i beta) gives

    p[exp(i beta)-exp(i(beta-alpha))+exp(-i alpha)]+2cos(delta)=0.

Its imaginary part is

    sin(beta)-sin(beta-alpha)-sin(alpha).

Set s=(alpha+beta)/2 and h=(alpha-beta)/2. This expression factors exactly as

    2 sin(h) [cos(h)-cos(s)].

Because alpha,beta are strictly positive and less than180, |h|<s<180. The cosine is strictly decreasing on[0,180], and cos(h)=cos(|h|), so the bracket is strictly positive. Hence sin(h)=0. Since |h|<90, this forces h=0, or alpha=beta. With equal pp angles, the phase and real closure are those of the equal-pp cone in Section4. No extra cross-slot geometry survives.

Any actual p0 seam is either same-slot or cross-slot; these two cases exhaust the saturated tiling. Thus every admitted pair under the hypotheses belongs to the two positive cones. The already reviewed periodic constructions prove the escape without any inference about the periodicity of the original tiling or about the global assembly of its B chains.

## Review and dependencies

Positive families: `research/lemmas/branching-hexagon-new-two-run-two-parameter-periodic-cone.md` and `research/lemmas/branching-hexagon-new-two-run-complementary-pp-periodic-cone.md`. Defect-free limit: `research/lemmas/hexagon-limit-and-periodicity.md`. Earlier chain transport remains PENDING and its larger endpoint-test set is explicitly only a one-end necessary test; this manuscript supplies the stronger actual double-end test. The completed fresh hostile review reconstructs the first saturation, the same A tile along B's middle q side, exact native endpoint assignments, phase branch and factor signs. No previous artifact was modified.
