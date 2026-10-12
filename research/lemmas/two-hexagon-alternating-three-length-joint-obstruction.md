# Alternating/alternating pairs cannot use three actual A side lengths

Date: 2026-10-12. Status: [independently reviewed VALID as part of the complete ALT/ALT chain](../reviews/two-hexagon-alternating-all-metric-chain-review.md).
This component retains its stated restricted domain; the full family conclusion
is in [the all-metric theorem](../lemmas/two-hexagon-alternating-all-metric-escape.md).

Fix the same-colour AAB hexagon angle family with A=ALT=(p,q,p,q,p,q),
B=ALT=(r,s,r,s,r,s), q=240-p, r=360-2p, s=2p-120,
90<p<150, p!=120. If A has exactly three actual positive native side lengths,
the pair admits no plane tiling under the unrestricted problem conventions.

The [A-only side stratum gate](two-hexagon-alternating-a-side-strata.md)
excludes87 of90 three-class native partitions universally. Thus A's actual
partition must be001221,011022, or012210. Each block has one even and one odd
native index. The complete [AB seam ledger](two-hexagon-alternating-metric-ledger.md)
then forces every actual B side into this same three-value alphabet, with
exactly two occurrences of each value. There are90 labeled native B words,
giving precisely270 pairs before dihedral quotient. Reflections are retained
through native words and the unmarked defect-free limit theorem.

For each pair, assign three variables to the shared actual side values and
form the4-by-3 joint polygon closure matrix M. Its two A rows use directions

    (0,0),(1,-1),(2,0),(3,-1),(4,0),(5,-1),

and its two B rows use

    (0,0),(1,2),(2,0),(3,2),(4,0),(5,2),

where(j,m) means j*60+m*theta, theta=120-p. In particular B's odd directions
have the same+2theta term, derived from alternating r,s exterior turns.
Use t=tan(theta/2) with sqrt(3)-2<t<2-sqrt(3), t!=0, and exact entries over
Q(sqrt(3))(t). All denominators are powers of1+t^2 and have no real poles.

Each polygon's six unit directions sum to zero, so the all-ones vector is in
the joint kernel. The [producer](../searches/two-hexagon-alternating-three-length-joint-closure.py)
and [certificate](../certificates/two-hexagon-alternating-three-length-joint-closure.json)
show that **every one of the270 matrices has generic rank2**, with kernel
exactly the span of(1,1,1). The gcd of every matrix's2-by-2 minor numerators has
no admitted real root. Therefore rank2 and that kernel persist for every
admitted angle, not just a generic or sampled angle.

Both polygons can close with these identifications only if all three class
lengths are equal, contradicting the hypothesis of three actual classes.
Thus no polygon pair in the necessary seam domain can have these side data.
Any original plane tiling would supply an admitted trivalent limit and hence
one of these270 cases, proving the claimed impossibility.

Combining this gate with the reviewed side-period-two periodic escape and
the A-only137-partition exclusion leaves a necessary ALT/ALT domain remaining after this gate
of61 native A partitions:45 with four classes,15 with five, one with six.
Their complete AB ledger contains20970 native B word cases. This count is a
remaining necessary domain, not evidence that any case extends to a plane
tiling or forces aperiodicity.
