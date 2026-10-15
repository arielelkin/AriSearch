# Thick-cap splitting: exact topology and cyclic-hexagon obstruction

**Later status:** the full stated off-normal mark-local receiving-hexagon
component is excluded by the independently reviewed
[combined congruence obstruction](../lemmas/offnormal-mark-local-truncation-obstruction-2026-10-15.md).
The narrower calculations below retain their explicitly stated scope.

Date: 2026-10-15. Status: independently hostile-reviewed VALID;
[fresh review](../reviews/thick-cap-split-congruence-hostile-2026-10-15.md). This is a changed construction topology,
not a solution of research-problem.md. No novelty claim is made.

## Complete source partition and cap indexing

Use the legal unit Ammann rhomb source and native arrows from
`three-sector-fractional-construction-2026-10-15.md`. In boundary order the
marks are thin=(X,X,Y,Y), thick=(X,Y,Y,X). Opposite donor parity is0 or1.
For all four species/parity cases the two donor edges contain one X and
one Y, as do the two receivers. Shared physical edges have opposite roles.
For an edge with actual arrow T->H and mark Z, set

    M=T+a_Z(H-T), 0<a_Z<1;
    t=M+h_Z n_donor, h_Z>0,

where n_donor is the unit normal into its donor rhomb. Offsets/heights are
mark-local, so the adjacent receiver sees the same triangle and subdivision.
The split point M is the normal foot of the donor apex; this hypothesis
will be essential to the obstruction.

For a receiving edge oriented U->V in receiver boundary order, t is its
external donor apex, M its split, and p,q its internal donor nodes adjoining
U,V. Partition and assemble the precursor outputs

    L=(U,t,M,p), R=(M,t,V,q), C=(M,q,p),

as in the prior three-sector artifact. The internal sectors are triangles
(U,M,p),(M,V,q),(M,q,p), and the external pieces are (U,M,t),(M,V,t).
Assume the source-sector partition is valid and all these outputs are strict
convex quads/triangles; failure of that assumption already kills a candidate.

Each donor node t has six incident rays. To index its cap independently of
the source species and parity, take the actual donor arrow T->H. Denote by
M_T,M_H the receiving split points on the two edges adjoining T,H, and by
q the opposite donor node inside the same source rhomb. In cyclic order,
possibly clockwise depending on the arrow relative to the source boundary,
index the neighboring ray endpoints

    N0=T, N1=M_donor, N2=H, N3=M_H, N4=q, N5=M_T.

A valid embedded source partition ensures this cyclic order. Set

    c_i=t+epsilon_Z (N_i-t)/|N_i-t|, i=0,...,5,

with positive mark-local epsilon_Z small enough, or any larger admissible
value giving disjoint cuts. This is an equal-radius cap: all c_i lie on
one circle. Cap edge i joins c_i to c_(i+1 mod6). The cap is a strict convex
hexagon, regardless of whether its indexing order is clockwise or reversed.
This specifies all four source cases without imposing one source parity.

Keep every thin-source cap whole. For EACH thick-source cap choose
lambda,mu in(0,1), mark-local if desired, and put

    a=(1-lambda)c0+lambda c1,
    b=(1-mu)c3+mu c4.

The opposite-edge chord a-b cuts the cap into pentagons with exact words

    K0=(a,c1,c2,c3,b),
    K1=(b,c4,c5,c0,a).

Strict convexity of the cap and interior edge positions make both children
genuine strict convex pentagons. They partition the cap, sharing exactly
a-b. No child congruence, cap reflection symmetry, visible intrinsic chord,
or vertex correspondence has been assumed.

For any donor node d and incident ray endpoint E, write d_E for its cut
point on that ray. The other final words in EVERY source case are

    H_L=(U,t_U,t_M,M,p_M,p_U),
    H_R=(M,t_M,t_V,V,q_V,q_M),
    P_C=(M,q_M,q_p,p_q,p_M).

These result from cutting the two donor-node corners of each L,R,C. Thus
thin sources own2 pentagons and6 hexagons; thick sources own6 pentagons
and4 hexagons. The original global sector dissection and disjoint local cap
cuts make this a full-plane partition whenever all underlying metric
admissibility conditions hold. The earlier small-cut fixture supplies
nonempty admissible geometry for this incidence change, but does not meet
two-class congruence.

## Area gate is passed, not a two-class certificate

Assign each cap (or its two children) to its donor rhomb and receiving
outputs to their receiver. Mark-local transferred cap slices cancel between
one X+one Y donation and receipt in each source. Opposite-edge splitting
preserves the total cap area. Hence, writing a for thin-rhomb area and
phi=(1+sqrt(5))/2, two congruence classes would require

    2P+6H=a, 6P+4H=phi*a,
    P=(3phi-2)a/14, H=(3-phi)a/14.

These areas are positive. The old equal-count area contradiction is indeed
removed. The next geometric gate nevertheless excludes this entire
equal-radius component, without solving any child-matching equations.

## The sharp cyclic congruence obstruction

**Theorem.** No admissible realization of the specified mark-local,
normal-foot, equal-radius cap topology has only two global polygon
congruence classes. This holds for every admissible lambda,mu, every
reflection/rotation in a proposed congruence, and all cyclic pentagon or
hexagon vertex aliases.

Proof. Pentagons and strict hexagons cannot be congruent. Thus two classes
would mean ONE class P for all pentagons and ONE class H for all hexagons.
A whole thin cap is cyclic, so every receiving hexagon must be cyclic.
Only cyclicity, an isometry invariant, is used; no preferred correspondence
between its corners and cap corners is required.

Consider a receiving precursor quad (U,t,M,p), with original interior
angles alpha_U,alpha_t,alpha_M,alpha_p. Cutting each donor-node corner at
equal radial distances along its two incident rays creates two equal new
angles beta_t=(pi+alpha_t)/2 and two equal new angles
beta_p=(pi+alpha_p)/2. This follows from the removed isosceles triangle.
The receiving hexagon's cyclic angle sequence is therefore

    alpha_U, beta_t, beta_t, alpha_M, beta_p, beta_p.

In any cyclic convex hexagon the sum of alternate interior angles is2pi:
write each angle as pi minus half the sum of its two adjacent central arc
angles, then sum over alternate indices. Subtracting these two alternating
sums for the displayed sequence gives alpha_U-alpha_M. Consequently

    alpha_U=alpha_M.

At M the two rays of this quad point toward t and p. The first is the
outward normal times h_Z; p lies strictly inside the receiver half-plane.
Their dot product is h_Z times the negative inward signed distance of p,
so is STRICTLY NEGATIVE. Since the precursor quad is strict convex,

    alpha_M>pi/2, hence alpha_U>pi/2.

The same argument for (M,t,V,q) forces its original endpoint angle
alpha_V>pi/2. Thus all FOUR original-source-vertex angles belonging to the
two receiving L/R pairs of any thin rhomb must be strictly obtuse.

Their sum is exactly2pi. To see this without numerical angle evaluation,
start with the four interior angles of the source rhomb, totaling2pi.
Removing its two donor triangles subtracts their four base angles from
the receiver sectors. Adding the two external incoming donor half-triangle
pairs adds the corresponding four base angles. For an edge mark Z their
sum is

    b_Z=atan(h_Z/a_Z)+atan(h_Z/(1-a_Z)).

This sum is independent of the donor source species, the donor's parity,
and the direction of its arrow in the chosen cyclic boundary order. Every
rhomb donates one X and one Y and receives one X and one Y. The net change
is therefore -b_X-b_Y+b_X+b_Y=0. The four receiving quad endpoint angles
sum to2pi. Their all being greater than pi/2 contradicts this identity.

The contradiction arises among hexagons alone, before any congruence test
of the thick-cap pentagonal children. Thus every D5 alias for either child,
all chord parameters, and all reflected child congruences are automatically
covered; there is no hidden assumption that the cap chord is intrinsic or
that congruent children imply a reflected whole cap. QED.

## Changed hypotheses required to escape

The argument specifically uses a cyclic thin H cap, paired equal-radius
cuts at each receiving donor corner, the normal-foot relation t-M, and
mark-local cancellation of base-angle sums. Unequal radial distances can
make the cap noncyclic and the two new angles unequal. Moving M away from
the apex's normal foot can remove the compulsory obtuse angle at M.
Source-context-dependent base-angle transfer can break the local2pi sum.
Each is a genuine changed geometric rule requiring a new exact partition
and forcing proof; the present theorem makes no claim about those variants.
The old metric census and D5 child matching are unwarranted within the
closed component.

Replay, finite scope:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/thick-cap-split-congruence-check-2026-10-15.py

The checker uses only the standard library and exact fractions. It verifies
the cap-split boundary incidence, all four mark-balanced source cases,
the formal alternating-angle identity, and the exact area-vector inversion.
A rational dot-product fixture is a sanity check only; the universal
obtuse-angle sign and unbounded geometric contradiction are proved above.
There are no solver calls, metric parameter samples, period bounds or
floating-point angle decisions. Fresh independent review is pending.
