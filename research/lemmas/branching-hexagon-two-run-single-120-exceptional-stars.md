# Complete exceptional-star locus on the single-120 / qq-low-high slice

Status: **VALID after fresh independent hostile review.** This is a complete necessary reduction of one two-parameter homogeneous resonance slice. Outside an explicit14-relation locus, the separately reviewed five-type native-slot dual proves untileability. It does not claim outcomes for the14 relations, or a classification of all homogeneous resonance strata.

## Actual metric slice and positivity

Let0<delta<30, alpha120, beta in(0,180), chi=120-2delta, psi=120+2delta. Setq=1 and

    P_beta=1+exp(i60)+exp(i(240-beta)),
    rho=arg(P_beta),    p=2cos(delta)/|P_beta|.

Here rho is the principal phase. P_beta has positive real and imaginary parts for beta in(0,180): its real part is3/2+cos(240-beta)>=1/2, and its imaginary part is sqrt3/2+sin(240-beta)>0 on that open interval. Thus0<rho<90. Also P_beta never vanishes since the sum of its first two terms has magnitude sqrt3 and the last has magnitude1.

Take A(delta) as usual. Take B's native directions

    (0,60,240-beta,rho+120-delta,rho+180+delta,rho+240-delta).

Its p-chain has phase rho and magnitude2cos(delta); its q-chain has the opposite phase and the same magnitude. Closure is exact. Its six angles are

    m0=60+rho-delta, alpha120, beta,
    m3=300-rho+delta-beta, chi120-2delta, psi120+2delta.

All are strictly between0 and180 exactly when

    rho+beta>120+delta.

Indeed m0 lies in(30,150), m3 is strictly greater than30, and the displayed inequality is exactly m3<180; the other four angle bounds follow from the stipulated delta/beta intervals. Ordered positive turns, exact closure and the previously established side-support argument then give actual strict convexity. Restrict further to p unequal to1; this is essential for the binary label argument. This defines the exact actual geometric slice, rather than merely independently specified angles.

## Complete named length-legal star domain

A trivalent binary-label star has either three homogeneous corners of the same label, or two mixed corners and one homogeneous corner. Thus its named angle type is in this full pre-stated48-element domain:

- four pp multisets of three corners from{alpha,beta};
- four qq multisets of three corners from{chi,psi};
- ten unordered mixed pairs from{AH,AL,m0,m3}, each with one of the four indexed homogeneous choices alpha,beta,chi,psi, giving40 types.

Reflections make both cyclic orientations available, but this inventory concerns angle types only; native slot/circular orientation expansion is handled by the80-star dual. Repetition means different tile occurrences. Angle equality does not imply placement or global extension.

On the whole slice five types identically sum360:

    (alpha,alpha,alpha), (AH,AH,chi), (AL,AL,psi),
    (AH,AL,alpha), (m0,m3,beta).

These are precisely the five types in the single-120 native-slot obstruction. Every other one of the48 types gives a proper affine equation in(delta,beta,rho). Exact canonicalization of all43 remaining equations gives15 equation classes. One is delta0, outside the domain. The other14 are exactly:

    beta=120, 120-2delta, 120+2delta;                         (3)
    rho=60+k delta,          k in{-2,0,1,2,4};              (5)
    rho+beta=180+k delta,    k in{-2,0,1,2,4};              (5)
    2rho+beta=240+2delta.                                    (1)

The14 are distinct affine equations in the auxiliary coordinate space(delta,beta,rho). They need not be distinct curves after imposing rho=arg(P_beta); some can coincide on the actual metric slice, some may have several branches or none in part of the strict domain. No curve pruning or outcome classification is hidden in the14 count.

## Derivation of the phase relations

For another mixed pair involving A and B, angle sums give the following equations with r in{alpha,beta,chi,psi}:

| Mixed pair | Extra angle equality |
| --- | --- |
| AH,m0 | rho+r=180 |
| AL,m0 | rho+r=180+2delta |
| AH,m3 | rho+beta-r=60+2delta |
| AL,m3 | rho+beta-r=60 |
| m0,m0 | 2rho+r=240+2delta |
| m3,m3 | 2rho+2beta-r=240+2delta |

Substituting the four homogeneous values yields exactly the11 listed phase relations. A/A corner pairs with the extra homogeneous choice beta and opposite B mixed pairs with r unequal tobeta add the three beta relations. Homogeneous pp triples add only beta120; qq triples add only delta0. This exhausts the48-domain without sampling beta/delta, metric approximation or a bounded assembly search.

Therefore outside all14 relations the full legal oriented native-star set is contained in the five identity types. The strong integer W/Y dual from `branching-hexagon-two-run-single-120-slot-obstruction.md` then excludes every trivalent admitted tiling and, by the reviewed defect-free limit, any unrestricted plane tiling. This is a complete complement exclusion with independently reviewed inventory and dual dependency.

At beta120, rho60 and p=cos(delta); this is the known periodic first curve and supplies an actual periodic escape. The other relations remain to be tested with every additional native star admitted by their exact intersections. The assertion of a complete complement exclusion must not be read as an outcome for those remaining strata.

## Retained exact replay

- `research/searches/branching-hexagon-two-run-single-120-exceptional-stars.py`;
- `research/certificates/branching-hexagon-two-run-single-120-exceptional-stars.json`.

The coefficient order is(constant,delta,beta,rho). The producer retains all48 original named types and each full unnormalized angle-sum-minus360 vector. It retains all15 proper canonical equation classes with every raw index and the explicit delta0 boundary label, then lists the14 remaining classes. It independently compares the latter with the explicit equations above. All5 identity types are checked exactly. Normal replay is read-only; explicit`--output` writes the record. The replay passed48types,5identities,43rawexceptions,15properclasses and14in-domainrelations.

Fresh review must reconstruct label legality and the48-domain, exact coefficient expansion, phase normalization, all-real strict convexity criterion and the80-star dual dependency. No previous artifact was modified. The homogeneous resonance branch and unrestricted target remain unresolved.
