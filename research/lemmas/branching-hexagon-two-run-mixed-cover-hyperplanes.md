# A complete 72-hyperplane mixed-corner obstruction

Status: **VALID after fresh independent hostile review.** This is a necessary condition for the entire distinct binary alternating/two-run family. It is not sufficient for local star coverage or a plane tiling; membership on a hyperplane is not an outcome classification. The complement of the union is untileable, by the independently reviewed proof and exact complete inventory.

## Domain and theorem

Let q=1,p>0,p unequal toq. A is the preceding threefold hexagon A(delta), with0<delta<30, side word(p,q,p,q,p,q) and angles A_H=120+delta,A_L=120-delta. Let B be any fixed strictly convex closed hexagon with side word(p,p,p,q,q,q), and write

    alpha=B_1, beta=B_2, chi=B_4, psi=B_5,
    m0=B_0, m3=B_3, S=alpha+beta+chi+psi.

All six native B angles lie in(0,180), and

    m0+m3=720-S.

**Necessary theorem.** If any unrestricted plane tiling by this pair exists, then its homogeneous-angle tuple(delta,alpha,beta,chi,psi) lies on at least one of the following72 distinct proper affine hyperplanes. Let r,s range over the four **indexed** coordinates alpha,beta,chi,psi, permitting repetition.

| Family | Exact necessary hyperplanes | Index domain | Count |
| --- | --- | --- | ---: |
| A/A partners | S-r-s=240+k delta | unordered indexed pair{r,s}; k in{-2,0,2} |30 |
| A/self partners | S-r-s/2=300+epsilon delta | ordered indexed pair(r,s); epsilon in{-1,1} |32 |
| self/self partners | S-(r+s)/2=360 | unordered indexed pair{r,s} |10 |

The72 hyperplanes are distinct as affine subsets of the five-dimensional angle-coordinate space. Different actual parameter subdomains or native equalities may cause some restrictions of these hyperplanes to coincide; this does not change the original exact domain or claim. The theorem allows all homogeneous pp/qq stars and all A–A q seams. No fixed quotient, species ratio, or rational-angle assumption is imposed.

## Proof from actual stars

An unrestricted tiling admits an everywhere trivalent edge-to-edge tiling by the reviewed hexagon defect-free limit theorem. In a trivalent star the three seam length labels are p or q. They change cyclically zero or two times. Thus there are either zero mixed corners (a homogeneous ppp/qqq star), or exactly two mixed corners and one homogeneous corner. There cannot be three mixed corners.

Every A corner is mixed. An A-only trivalent tiling is therefore impossible, so B occurs in the admitted limit even if a type vanished during extraction. Fix an actual B occurrence. Its corner m0 lies in a mixed star. The other mixed corner is either A_H, A_L, m0 from another B occurrence, or m3 from another B occurrence. The homogeneous corner is some indexed r from(alpha,beta,chi,psi), since A has no homogeneous corners. The same list applies at m3. This argument does not assert that every enumerated corner combination has a valid cyclic label ordering; retaining some impossible combinations only makes the necessary condition weaker.

If either of these actual stars pairs m0 with m3, its angle sum is

    m0+m3+r=360,

so S-r=360. This is already in the self/self family with the indexed repeated pair r=s. Hence no additional hyperplane is required for this case.

Otherwise both corners separately have a partner in{A_H,A_L,self}. Covering m0 with A_H/A_L gives

    m0=240-r-epsilon delta,    epsilon in{1,-1},

and covering it with another m0 gives m0=180-r/2. At m3 the identical alternatives hold with another indexed s. The twelve alternatives for each mixed corner (four indexed homogeneous choices times three partner choices) give a complete pre-stated domain of12×12 separate-cover pairs. Eliminate m0+m3=720-S:

- Two A partners give S-r-s=240+(epsilon+eta)delta, yielding the30 hyperplanes.
- An A partner and a self partner give S-r-s/2=300+epsilon delta. Here r denotes the A-partner star's homogeneous corner and s the self-partner star's homogeneous corner, regardless of which mixed corner is which. This yields32 hyperplanes.
- Two self partners give S-(r+s)/2=360, yielding10 hyperplanes.

Every actual B occurrence supplies a covered m0 and m3 and therefore one of these relations. All hyperplanes are proper: in the A/A family at least two indexed homogeneous coordinates have coefficient1; in A/self at least two do; in self/self at least two do. No relation reduces identically to0. Exact canonical coefficient enumeration checks both properness and all claimed counts.

The absence of all72 relations therefore excludes every possible trivalent limit and hence every original unrestricted tiling. On the union, many corners may still be uncovered, cyclic label order may fail, actual double-end geometry may fail, or global assembly may fail. No positive tiling claim follows from a relation.

## Relation to homogeneous-star resonance inventory

The pp/qq homogeneous-star loci in `branching-hexagon-two-run-resonance-inventory.md` are four proper lines on each of their native two-angle arcs. None of the eight resulting hyperplanes equals any of these72 hyperplanes. The only members of the72 supported on just two homogeneous coordinates have equal coefficients and constant240 (with a possible delta term), whereas the two-coordinate homogeneous resonances have coefficient ratio2:1 and constant360. The one-coordinate homogeneous resonances also differ. The replay explicitly compares all eight canonical resonance vectors against the72 and records their disjointness. Thus each homogeneous-star resonance stratum is further restricted to finitely many proper affine intersections by this necessary mixed-corner theorem. This is still a finite union of continua, not a finite geometric catalog.

The paired A–A q locus alpha,beta=120±2delta has alpha+beta=240. It is already contained in the k=0 A/A hyperplane with r=chi,s=psi, so the new condition alone does not reduce that exceptional locus. A genuine double-ended contact or global count invariant is still needed there.

As an example of the mechanism rather than a retained classification, atdelta15, homogeneous angles(alpha,beta,chi,psi)=(135,90,90,150) have mixed-angle sum255. A joint m0/m3 star would require a homogeneous105 corner, which is absent; independent separate-cover constraints must therefore be tested. An irrational mixed angle cannot be dismissed merely for being irrational; only failure of the exact complete finite cover conditions justifies an exclusion.

## Complete retained replay domain

The producer retains4 opposite-mixed joint-cover equations plus all144 separate-cover equations before any deduplication. It canonicalizes rational coefficient vectors by clearing denominators, dividing by the integer gcd and fixing the sign of the first nonzero coefficient. All148 raw equations map to exactly72 canonical proper hyperplanes; the four joint equations are already among the self/self hyperplanes. Every raw record is retained with its index, and each canonical hyperplane records its raw indices.

- Producer: `research/searches/branching-hexagon-two-run-mixed-cover-hyperplanes.py`.
- Certificate: `research/certificates/branching-hexagon-two-run-mixed-cover-hyperplanes.json`.

Normal replay is read-only; explicit `--output` is required for retained writes. The exact coordinate order is(constant,delta,alpha,beta,chi,psi); the hyperplane is the dot product with(1,delta,alpha,beta,chi,psi) equal tozero. Replay passed all148 eliminations and the exact72 distinct/proper count. No solver, timeout, geometric patch search or frequency assumption is involved.

Dependency: the reviewed `research/lemmas/hexagon-limit-and-periodicity.md`. Fresh hostile review must independently reconstruct the mixed-corner parity, B-presence argument, full alternative domain, all rational eliminations, indexed versus numerically equal coordinates, and the infinite compactness implication. The larger target remains unresolved on the remaining loci.
