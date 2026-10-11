# Exceptional angle resonances for the binary two-run branch

Status: **independently adversarially reviewed VALID**; see [the fresh root review](../reviews/branching-hexagon-two-run-resonance-inventory-review.md). This is an exact necessary inventory and a monohedral exclusion. It does not classify tilings on the resonance loci. These loci contain continua of shapes, not a finite list of candidate geometries.

## Parameter domain and exact resonance locus

Use the preceding A(delta) with 0<delta<30, q=1,p>0,p unequal to1. B is any strictly convex closed hexagon with native side word(p,p,p,q,q,q), pp angles(alpha,beta), qq angles(chi,psi), and two mixed angles. All native angles lie strictly between0 and180. No rational-angle restriction is made.

A trivalent homogeneous ppp star can use only the pp corners alpha,beta; A has only mixed corners. Its exact necessary angle equations are the four proper affine lines

| Multiset | pp resonance | Interior interval |
| --- | --- | --- |
| 3 alpha | alpha=120 | 0<beta<180 |
| 2 alpha+beta | 2alpha+beta=360 | 90<alpha<180, beta=360-2alpha |
| alpha+2 beta | alpha+2beta=360 | 90<beta<180, alpha=360-2beta |
| 3 beta | beta=120 | 0<alpha<180 |

The qq star has the same four equations with(chi,psi) replacing(alpha,beta). Repetition is allowed because native slots from distinct tile occurrences may repeat in a star.

All four lines on a given arc intersect only at(120,120). Any two distinct equations imply that point; conversely it satisfies all four. Thus an arc has no legal homogeneous multiset off the line union, exactly one such multiset at every noncentral point of the line union, and all four at the center. This inventories angle-legal stars only; actual contact geometry may rule them out.

The exact angle locus on which an A–A q seam is not immediately excluded is

    alpha=120, or beta=120, or
    (alpha,beta)=(120-2delta,120+2delta), or its reversal.

Indeed its two A corners at either seam endpoint are H/L, H/H or L/L. The third corners are pp, so the two endpoint fillers are either120 at both ends or120-2delta and120+2delta. The paired locus is disjoint from all four pp homogeneous-star lines: for m+n=3 the homogeneous sum at the pair is360+2delta(n-m), and n-m is odd and nonzero. The reversed pair changes that coefficient's sign but never makes it zero.

Therefore, outside the eight homogeneous-angle hyperplanes and the two paired A–A q loci (the single120 A–A loci are already pp hyperplanes), the independently reviewed double-end reduction would force membership in the two constructive periodic cones if a tiling exists. The unclassified geometries in this larger branch are confined to this explicit finite union of proper affine loci, after restricting to actual closed strictly convex binary shapes. This is a dimension reduction, not an untileability decision on the loci.

## Global homogeneous-star frequency identity

In any admitted trivalent edge-to-edge tiling let Y_p,Y_q count homogeneous ppp and qqq stars whose centers lie in a square of radiusR. Let V_m count mixed stars. Fixed tile areas and diameters make all corner-incidence boundary errors O(R). There are6N_A+2N_B mixed corner occurrences and4N_B homogeneous corner occurrences. Each mixed star contributes two mixed and one homogeneous corner, while each homogeneous star contributes three homogeneous corners. Hence

    6N_A+2N_B=2V_m+O(R),
    4N_B=V_m+3(Y_p+Y_q)+O(R),
    N_B-N_A=Y_p+Y_q+O(R).

This identity allows N_A and N_B to differ when homogeneous stars are present; an equal-species ratio must not be inserted in a resonance model.

At a noncentral pp resonance the unique permitted homogeneous multiset is(m,n), m+n=3. Its native alpha and beta incidence counts each have availabilityN_B+O(R), giving

    mY_p<=N_B+O(R),    nY_p<=N_B+O(R),
    Y_p<=N_B/max(m,n)+O(R).

Thus a pure3-copy resonance gives Y_p<=N_B/3+O(R), and a mixed2+1 resonance gives Y_p<=N_B/2+O(R). At the center(alpha,beta)=(120,120) there are2N_B pp corners, so3Y_p<=2N_B+O(R). Away from the resonance lines Y_p=0. The qq arc has identical bounds.

These bounds give a useful preliminary necessary count table. Arc categories are none, pure3, mixed21, center120, with respective upper bounds0,1/3,1/2,2/3 per B tile. Add the two arc bounds to obtain c; then N_A>=(1-c)N_B+O(R). In particular a monohedral B tiling is already excluded by corner counts whenever c<1. This includes any case with a nonresonant arc and any offcenter pair except mixed21/mixed21. The center/pure3 case has c=1 and remains undecided by this count. The certificate lists all16 category pairs exactly. No nonnegative star-frequency upper bound is asserted to be attainable.

## All distinct binary two-run B shapes are nonmonohedral

In fact the imported complete convex-hexagon classification excludes B monohedral tilings throughout the binary distinct domain, including the corner-count undecided strata. The source is Zhu–Wang–Yan, [Hexagonal Tiling of the Plane, arXiv:2508.01404v2](https://arxiv.org/html/2508.01404v2), Main Theorem and Introduction's defining families.

The classification says a convex monohedral tiler satisfies one of H1,H2,H3, up to native cyclic/reflected indexing. H1 and H2 each require an equal opposite side pair. Every opposite pair of the word pppqqq is p/q and is unequal. H3 requires three equal adjacent pairs partitioning the six sides; either partition of pppqqq contains a p/q pair. Thus B satisfies none of the three families. The replay checks all12 native indexing choices. This uses the imported completeness theorem, not a new proof of that theorem.

A is also nonmonohedral. The reviewed defect-free hexagon theorem would turn any A-only tiling into a trivalent edge-to-edge one. But each A corner is mixed pq. Around a trivalent star three binary seam labels have either zero or two cyclic changes; they cannot give three mixed corners. Hence no such A-only star or tiling exists.

Consequently any tileable distinct binary pair here satisfies the hypotheses of the separately reviewed uniform-density theorem `research/lemmas/two-type-uniform-density.md`: neither species may be omitted, and both species are syndetic with positive lower tile and area density uniformly over all admitted tilings. This does not give a unique ratio or exact frequencies, and it does not prove periodicity on any remaining resonance stratum.

## Retained replay and remaining work

- `research/searches/branching-hexagon-two-run-resonance-inventory.py`;
- `research/certificates/branching-hexagon-two-run-resonance-inventory.json`.

The producer is read-only by default; an explicit `--output` is required to retain a record. It checks all exact affine line intersections, the nonzero paired A–A q homogeneous coefficients, all12 native word tests for the imported families, and all16 rational category upper bounds. It does not check imported theorem completeness or assert that an angle-legal star is geometrically attainable.

Next genuine contact problems are the noncentral mixed2+1 homogeneous lines and the single120 loci permitting A–A q seams. Actual two-ended side matching and corner balance must be tracked there, with N_A,N_B free and nonnegative. A bounded no-witness search would not classify any continuum or prove untileability. The larger unrestricted target remains unresolved.
