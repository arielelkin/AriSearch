# Oppositely ordered mixed homogeneous arcs: exact phase and singleton slots

Status: **VALID after fresh independent analytic hostile review.** This is an exact phase classification and necessary contact/count theorem, not a positive construction. The two exceptional curves below remain outside the off-curve obstruction in the separate manuscript.

## Scope

Fix 0<delta<30 and distinct positive p,q. A is the threefold alternating convex hexagon with native lengths(p,q,p,q,p,q), native angles H=120+delta at even slots and L=120-delta at odd slots. B is a strictly convex binary two-run hexagon with lengths(p,p,p,q,q,q), angles

    (u,alpha,beta,v,chi,eta),
    2alpha+beta=360, chi+2eta=360,
    alpha!=120, eta!=120.

Thus 90<alpha,eta<180, beta=360-2alpha and chi=360-2eta are the singleton homogeneous slots. This is the singly reversed relative ordering of the two mixed homogeneous arcs. Reflections, repeated native corners, omission of a species and unrestricted contacts are admitted. Angles are in degrees; derivative formulas below use radians.

## Exact native metric phase

Common-scale q=1 and rotate side0 of B to direction0. The first three unit p edges have directions0,180-alpha,alpha and sum

    P_alpha=1+2i sin(alpha).

If its first q edge has direction phi, the three q unit edges have directions phi,phi+2eta-180,phi+eta. Their sum is exp(i(phi+eta))*conjugate(P_eta). Let

    rho(x)=arg(1+2i sin x), 0<rho(x)<atan(2),
    u=rho(alpha)+rho(eta), v=alpha+eta-u.

Native closure, with the positive length ratio, is equivalent to

    p/q=|P_eta|/|P_alpha|,
    phi=180+rho(alpha)+rho(eta)-eta.

The actual mixed angles are exactly the displayed u,v. There is no lift ambiguity: 0<u<2atan(2)<180, and the displayed directions finish at180+u<360. The six positive strict turn conditions are exactly alpha,eta in(90,180) and v<180. The two pp turns are180-alpha,2alpha-180; the two qq turns are2eta-180,180-eta; the mixed turns are180-v,180-u. Closure and these positive ordered increments give a strictly convex native polygon. Thus this phase describes all actual geometries on the scoped arc relations, not a linear-angle envelope.

On90<x<180,

    rho'(x)=2cos x/(1+4sin²x)<0,
    rho''(x)=-2sin x*(5+4cos²x)/(1+4sin²x)²<0.

Consequently rho strictly decreases and is strictly concave; f(x)=x-rho(x) strictly increases and is strictly convex. Since sin strictly decreases here, p!=q is equivalent to alpha!=eta.

## Exact exceptional curves for B-only singleton stars

A binary trivalent star has either zero or two mixed corners. A B-only nonhomogeneous beta-star therefore uses two corners from u,v with repetition. Its three residuals are

    2u+beta-360=2(u-alpha),
    u+v+beta-360=eta-alpha,
    2v+beta-360=2(eta-u).

The chi residuals are, respectively, 2(u-eta),alpha-eta,2(alpha-u). Because alpha!=eta, a B-only nonhomogeneous star containing either singleton is angle-legal only on the two curves

    u=alpha or u=eta.

Conversely these equalities really permit both singleton B-only angle patterns: on u=alpha,v=eta one has2u+beta=2v+chi=360, while on u=eta,v=alpha the roles of the two mixed corners interchange. This is a local angle/length-pattern assertion only. It gives neither planar extension nor a tiling; native side incidence remains a separate constraint.

Here is a complete exact parametrization of u=alpha, including all denominator cases. Put t=tan(alpha/2)>1 and

    D=1+8t²-t⁴, N=t(3t²-1),
    F(t)=t⁴+3t³-8t²-t-1.

Let t0 be the unique real root of F above1. It lies strictly between sqrt(3) and2. The curve is exactly

    1<t<t0, t!=sqrt(3),
    alpha=2arctan(t),
    eta=180-arcsin(N/D).

The other curve swaps alpha and eta. The curve formulas always have0<N<D, so the displayed inverse sine is its principal value in(0,90), and v=eta lies strictly between90 and180. There is no further convexity restriction on these curves.

To prove completeness, the imaginary part of exp(-i alpha)*P_alpha*P_eta is

    sin(alpha)*(2cos(alpha)-1)
      +(2cos(alpha)+4sin²(alpha))*sin(eta).

Its vanishing yields sin(eta)=N/D. At D=0 the first summand is strictly negative, so no solution is lost by division. With t>1, N>0, and0<sin eta<1 requires D>N, equivalent to F(t)<0. F(1)=-6, F(sqrt(3))=8sqrt(3)-16<0, F(2)=5. Moreover F''=12t²+18t-16>0 on t>1, F'(1)=-4; hence F first decreases then strictly increases to infinity and has exactly one root t0 above1. Conversely1<t<t0 makes0<N<D and the imaginary part zero. Both u and alpha lie strictly between0 and180, so zero sine of u-alpha forces equality, not the antipodal ray. Finally alpha=eta would give2rho(alpha)=alpha, equivalent to tan(alpha/2)=2sin(alpha), or t²=3. The two curves meet only at the excluded center alpha=eta=120; a centered arc on either curve similarly forces that same point by strict monotonicity of f.

## Actual side exclusions and count ledger

Use the reviewed defect-free trivalent ETE limit for arbitrary admitted tilings of fixed convex hexagons. At each radial star both possible AA whole-side tests require the opposite B homogeneous arc to contain120 or the unordered pair{120-2delta,120+2delta}. Neither scoped noncentral mixed homogeneous arc has120. Such an arc cannot be that pair either: substituting the two distinct paired values into2alpha+beta=360 or chi+2eta=360 forces delta=0. Thus AAp and AAq are impossible. Every star with A has precisely one A, one B mixed corner and one B homogeneous corner. Injection of A's six corners into B's two mixed native slots gives

    6N_A<=2N_B+O(R).

The only pure pp and qq native multisets are2alpha+beta and chi+2eta, respectively. Indeed the four possible pure resonance planes meet pairwise only at a centered arc. Let Yp,Yq denote the corresponding pure stars and M_alpha,M_beta,M_chi,M_eta their nonpure native-corner counts. Direct inventories and mixed-corner counts give

    M_alpha=N_B-2Yp+O(R), M_beta=N_B-Yp+O(R),
    M_chi=N_B-Yq+O(R), M_eta=N_B-2Yq+O(R),
    Yp,Yq<=N_B/2+O(R),
    N_A=N_B-Yp-Yq+O(R).

The last equality follows by counting mixed corners: each nonpure star has two; equivalently6N_A+2N_B=2(4N_B-3Yp-3Yq)+O(R).

Away from both exceptional curves every M_beta and M_chi star contains one A. Therefore

    M_beta+M_chi=N_B+N_A+O(R)<=6N_A+O(R),
    N_B/5-O(R)<=N_A<=N_B/3+O(R).

All discrepancies are uniform O(R) for the two fixed shapes: changing vertex/tile-window selection changes counts only in a bounded-width boundary band, whose tiles have bounded diameter and positive minimum area. Total tile count is Omega(R²), so these inequalities force both species at quadratic count without presuming a frequency or prior species density. On the exceptional curves the upper bound and pure-slot ledger remain valid; the lower bound and forced-singleton conclusion are not asserted.

## Opposite-sign necessary singleton covers off the curves

Define

    Aform=2alpha-u, Bform=alpha-eta+u,
    Cform=2eta-u, Dform=eta-alpha+u.

An A/beta star is legal only if Aform or Bform equals H or L; an A/chi star requires Cform or Dform equals H or L. These are exactly360-(Bmixed+singleton). Both singleton types have positive quadratic count. They cannot both be restricted to the same A sign: then their N_B+N_A+O(R) corner occurrences would fit into only3N_A A corners, requiring N_B<=2N_A+O(R), inconsistent with N_A<=N_B/3+O(R). Therefore there is a legal beta cover and chi cover with opposite A signs. Adding that pair gives the necessary finite union

    u=120 or v=120 or alpha+eta=240.

For the first two, delta=|alpha-eta|. On alpha+eta=240 the possible delta values are|2alpha-u-120| or|2eta-u-120|. These remain necessary conditions until the separately stated corner-inventory obstruction is reviewed.

No B-only plane tiling is inferred from the exceptional curves. The distinct pppqqq word fails every native cyclic/reflected convex monohexagonal periodicity side condition, as recorded in the existing reviewed monohex inventory; this fact by itself does not exclude a tiling using both species on either curve.

Exact computation ledger: `research/searches/two-homogeneous-opposite-mixed-arcs-phase.py`. Dependencies: reviewed unrestricted hexagon ETE-limit theorem and fixed-shape boundary estimates. The full unrestricted two-prototile problem remains unresolved.

Fresh independent whole-proof analytic [review](../reviews/two-homogeneous-opposite-mixed-arcs-phase-review.md) is VALID.
