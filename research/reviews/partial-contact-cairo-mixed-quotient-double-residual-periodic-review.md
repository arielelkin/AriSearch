# Fresh scoped review of the Cairo double-residual periodic subcone

**Verdict: VALID for a>0,b>=a/sqrt3 in the [lemma](../lemmas/partial-contact-cairo-mixed-quotient-double-residual-periodic.md).** Fresh root review; author partial_contacts. This is a sufficient closed subcone, explicitly excluding the lower positive interval. No bounded negative search is promoted to untileability.

Independently derive P=(a,b,(3sqrt3*a+b)/4,(a+sqrt3*b)/4,(a+sqrt3*b)/2), Q=(4b-sqrt3*a,a,3sqrt3*b-2a,b,2b) and both original Cairo closures. With a>0 their full positive native cone is b>sqrt3*a/4. The actual sufficient domain is b>=a/sqrt3, which is stronger. In its strict interior the Q_a and Q_c subdivision residuals3b-sqrt3*a and3sqrt3*b-3a are positive and proportional; P_e=2Pd,Q_e=2b. Original positive closed cyclic directions give strict convexity throughout, not just at a fixture.

The independent no-author-import checker reconstructs every atomic coordinate from original native vertices, source side rows and actual cuts. All58 dart occurrences are paired once with equal native linear lengths, and their corner-flag graph consists of19 connected circular links of total360. Direct affine placement checks verify all ten original native faces and58 directed transitions, both actual endpoints, opposite CCW orientations with reflections and integer period coefficients. All29 inverse pairs are checked, the coefficient span is primitive Z², and fresh original shoelace area equals minus the determinant polynomially over Q(sqrt3)[a,b]. The displayed positive area polynomial proves the two periods independent throughout the accepted subcone.

At b=a/sqrt3 the two native Q residuals vanish. Exactly darts43,46,51,54 have zero length, each paired with a zero partner. Deleting their four zero boundary chains leaves every original polygon strictly convex with positive sides, all surviving opposite boundary identities and the unchanged positive area/covolume. An exact boundary fixture confirms these facts. The coverage argument is direct: local finiteness, zero generic boundary jumps, total area/covolume1 imply generic multiplicity1, which excludes both open interior overlap and open gaps; the locally finite closed-face union is closed. Thus the entire plane is covered by the original unmarked convex shapes with both independent translations, even at the equality merger.

The strict interior private-arm fixture a=1,b=6/5 is exactly checked, including original supports and precisely the native cross matches. Added resonances are allowed by the positive theorem. The complementary b interval remains unclassified; its selected10-face multiset exhaustion has only its recorded bounded scope. Necessary frequencies merely proposed face counts and never established surface existence.

Replay:

    conda run --no-capture-output -n arisearch python research/reviews/verify_partial_contact_cairo_orbit6_flat239_independent.py

PASS native polynomial closures/cuts,19 circular links,10 placements,58 reversed transitions, primitive periods/full area and interior/equality fixtures. Other metric domains and the unrestricted target remain unresolved.
