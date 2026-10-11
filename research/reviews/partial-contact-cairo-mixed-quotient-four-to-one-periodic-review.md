# Fresh full positive-cone review of the ten-face Cairo carrier

**Verdict: VALID for the entire two-parameter positive cone in the [lemma](../lemmas/partial-contact-cairo-mixed-quotient-four-to-one-periodic.md).** Fresh reviewer root; author partial_contacts. No author module, solver or native frequency encoding is imported.

Independent native equations reproduce P=(a,b,(3sqrt3*a+b)/4,(a+sqrt3*b)/4,(a+sqrt3*b)/2) and Q=((3sqrt3*a-b)/2,a,(11a-3sqrt3*b)/2,b,5(sqrt3*a-b)/2), both exact Cairo closures. All ten side lengths are positive exactly when a>0 and0<b<sqrt3*a: these conditions are necessary from Pa,Pb,Qe, and suffice directly for all remaining sides. Strict convexity throughout the cone follows from the original positive closed cyclic directions0,90,150,240,300. The P_c and Q_a cuts have identical positive residual3(sqrt3*a-b)/4; Q_c-a=3sqrt3(sqrt3*a-b)/2 is positive; Pe=2Pd. Thus all original subdivisions are strictly interior throughout the complete metric domain, without additional arm-order restrictions.

The independent checker reconstructs all58 actual atomic coordinates from original native vertices and compares every source native row. It uses each paired dart once, derives19 connected circular corner-flag links of total360 (including the four90 link), and checks the ten original placements directly as affine formulas over Q(sqrt3)[a,b]. All58 directed transitions match both endpoints, reverse CCW boundary orientation after reflections, use integer period shifts and occur in29 inverse pairs. Integer period coordinates generate Z². Fresh native-face shoelace area equals the positive period determinant identically; its explicit polynomial81sqrt3*a²/8+27ab/4+3sqrt3*b²/8 confirms independence everywhere.

The multiplicity coverage proof survives independently: lattice translates of the ten bounded native originals are locally finite, paired opposite CCW boundary chains give zero multiplicity jumps, generic paths avoid locally finite intersection points and endpoints, and average multiplicity is total area/covolume1. Hence multiplicity1 almost everywhere, disallowing open interior overlaps and any gap because the locally finite closed-face union is closed. This proves actual doubly periodic plane coverage by the unmarked convex originals, including reflections and partial contacts. No local-balance or finite-patch extension is assumed.

The exact interior fixture a=1,b=6/5 has positive originals, four distinct arms on each species and precisely sharedPa=Qb,Pb=Qd. Original support inequalities are checked exactly. Additional native equalities/event resonances elsewhere in the cone do not harm the polynomial construction. The bounded search proposes only the retained witness; none of its search decisions are needed for sufficiency.

Replay:

    conda run --no-capture-output -n arisearch python research/reviews/verify_partial_contact_cairo_orbit6_flat142_independent.py

PASS all native polynomial closures/cuts,19 actual circular links, ten placements,58 reverse boundary transitions, primitive lattice, full area/covolume and exact private-arm fixture. An initial reviewer variable-name collision between nativeQa and a face-area list failed the checker; renaming the area list corrected it before acceptance, without changing any producer or theorem.

The full source orbit6flat142 is periodically realized. Descendant containment is a separate exact matrix audit; neither it nor unrelated positive/negative claims are inferred from a fixture. The unrestricted target remains unresolved.
