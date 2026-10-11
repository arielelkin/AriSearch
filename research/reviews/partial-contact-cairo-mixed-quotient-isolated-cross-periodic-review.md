# Fresh full-cone review of the second mixed Cairo quotient

**Verdict: VALID for the entire positive three-parameter cone stated in the [lemma](../lemmas/partial-contact-cairo-mixed-quotient-isolated-cross-periodic.md).** Fresh reviewer root; construction author partial_contacts. No author module, solver, or necessary frequency premise is imported.

Independent native derivation starts from P=(a,b,c,d,e), its two Cairo closure equations, and Q=(e-b,a,c,D,f). Thus D=e-b+(a-c)/sqrt3 and f=sqrt3*c+D-2(e-b), reproducing every source side form. Native positivity, exact closure and directions0,90,150,240,300 prove strict convexity throughout the domain by the cyclic support-height argument. Original faces are always full pentagons, including the contact-order equality.

For D>d the actual cuts are P_e=(e-b)+b and Q_D=(D-d)+d. For D<d they are P_e=(e-b)+b and P_d=(d-D)+D, with Q whole. The independent checker reconstructs these exact atomic coordinates from the original words, compares source side forms, uses each dart once and derives all eight actual circular corner-flag links rather than trusting grouped angle totals. Every link sums360. Each domain gives eight original native face placements whose48 directed boundary transitions match both endpoints and opposite CCW orientation modulo integer period coefficients. All24 inverse pairs are checked. The integer coordinates span Z², and fresh original-face shoelace area equals minus the period determinant polynomially over Q(sqrt3)[a,b,c]. Positive original areas therefore prove independence of periods throughout each domain.

The independently checked two motifs differ only by minus the first period at state(face3,theta9,+1). At D=d the first proposal has precisely the two paired zero dart types15 and21, with four lifted occurrences. Deleting these zero boundary chains retains all cancellation identities. Original faces remain positive and strict; total area/covolume remains positive. This equality argument uses direct identities, not a limit or an assumed surface collapse. Exact interior private-arm fixtures a=1,b=2,c=16/5 and c=29/10 certify the two strict domains; the equality fixture c=2sqrt3-1/2 certifies the merger. Initial reviewer fixture guesses c=3 for the complementary order and an erroneous equality constant failed the checker; the fixtures were corrected by the exact D-d equation before any verdict, with no producer or theorem change.

The plane-coverage proof is valid: a rank-two lattice of the eight compact original polygons is locally finite; opposite CCW boundary chains cancel the multiplicity jumps across every generic segment, even when extra metric equalities make segments coincide. Generic paths avoid the locally finite endpoints and intersections, so multiplicity is constant almost everywhere. Its mean is the total area divided by covolume, exactly1. Interior overlap is open, and the locally finite closed-face union is closed, so any gap contains an open gap. Both contradict multiplicity1. Thus this is a true doubly periodic plane tiling of unmarked convex originals admitting reflections and partial contacts.

Replay both strict contact orders:

    conda run --no-capture-output -n arisearch python research/reviews/verify_partial_contact_cairo_orbit7_flat12_independent.py
    conda run --no-capture-output -n arisearch python research/reviews/verify_partial_contact_cairo_orbit7_flat12_independent.py --complementary

Both PASS full polynomial native geometry/cuts, eight circular links and placements,48 boundary transitions, primitive lattice and area/covolume. The default additionally checks the zero-piece equality case; the complementary additionally checks motif coincidence modulo the lattice.

The source orbit7flat12 is now wholly periodic for all positive native metrics, including extra equalities. The exact two-cross necessary-flat count decreases116 to115 (dimensions2/49/64 for dimensions3/2/1). Other flats and the unrestricted target remain unresolved.
