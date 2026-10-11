# Complete classification of one alternate four-shared-arm Cairo family

**Status:** all proof dependencies independently hostile-reviewed VALID;
exact negative certificates and a positive flat-torus witness independently
reconstructed. This is a restricted family theorem, not a classification
of arbitrary Cairo pairs or the main two-convex-tile result. No novelty claim.

Let w=sqrt3, w squared=3 and1<w<2. Choose a>0 and k with

    (5-w)/(1+3w)<k<3+2w.

Define b=ka and

    c=((3+w)a+(1-w)b)/4,
    d=((3-w)a+(1+w)b)/4,
    e=(w-1)(a+b)/2,
    f=((w-5)a+(1+3w)b)/4.

P=(a,b,c,d,e) and Q=(a,d,b,c,f) denote strictly convex pentagons
with directed native side directions0,90,150,240,300 degrees and first
vertex0. For a word(A,B,C,D,E), their exact vertices are

    (0,0),(A,0),(A,B),(A-w*C/2,B+C/2),(-E/2,w*E/2).

The displayed positive cone is precisely where all native lengths are
positive. Their native angles after sides are90,120,90,120,120. If k!=1,
the four arms are distinct and e!=f, so these are two distinct congruence
classes. At k=1 the two shapes coincide.

**Theorem.** For k!=1, this pair tiles the plane if and only if

    k=1+4w/3.

At that ratio it has a doubly periodic plane tiling using four P and four
Q copies per lattice cell, with native partial contacts and reflections.
The lattice generators at a=1 are

    U=(2+w,2+w), V=(4w/3,-4-10w/3).

General a scales both periods by a. Therefore no pair in this exact
family is aperiodic. The congruent k=1 case also has a periodic monohedral
escape by the reviewed swapped-arm cone specialized to a=c=d=D.

## Exhaustive parameter proof

The reviewed [resonance-domain reduction](partial-contact-cairo-alternate-resonance-reduction.md)
solves both vector closure relations and checks all15 event-sum collisions
and12 fifth-side host equalities. For k!=1 all six event sums are distinct.
If neither fifth side is a bank sum, the two-T compatibility components
{a,c},{b,d} and whole Q f seam give an impossible isolated120 third corner.
This is an unrestricted contact argument, not a bounded torus search.
Exactly six positive ratios escape it:

| Ratio | Necessary host equality | Final exact result |
|---|---|---|
| (28w+13)/37 |f=2c|untileable by whole/hosted corner charge|
| w |f=a+c|untileable by actual-slot two-ended seam charge|
| (20w-11)/13 |f=2a|untileable by actual-slot two-ended seam charge|
|1+w|e=2c|untileable by actual-slot two-ended seam charge|
|1+4w/3|e=a+c|periodic eight-face flat-torus tiling|
|1+2w|e=2a|untileable by whole/hosted corner charge|

The first and last exclusions are in the reduction and its
[independent no-solver review](../reviews/partial-contact-cairo-alternate-resonance-review.md).
The three stronger exclusions are self-contained with individual reviews:
[f2a](partial-contact-cairo-alternate-f2a-seam-obstruction.md),
[e2c](partial-contact-cairo-alternate-e2c-seam-obstruction.md),
[fac](partial-contact-cairo-alternate-fac-seam-obstruction.md).
Each preserves every whole/T occurrence choice, optional native long-arm
cut and reflection. Complete star charges are nonnegative; native tile
charges are negative; canonical edge-end potentials cancel. Uniform O(R)
boundary error contradicts Omega(R squared) coverage. This supplies the
unbounded implication of every finite rational obstruction certificate.

The sole positive case is the independently reviewed
[eac construction](partial-contact-cairo-alternate-eac-periodic-escape.md).
Its24 edge pairs exhaust all eight augmented face boundaries, and16 actual
circular vertex links have angle360. The connected orientable quotient
is a flat torus, with Euclidean universal cover giving the entire plane.
The independently developed exact lattice is primitive and its covolume
22+40w/3 equals4area(P)+4area(Q). This establishes existence, rather than
inferring it from feasible numerical frequencies.

All six exceptional ratios and the generic complement are thus settled.
The theorem permits reflections, partial contacts and omitted species
exactly as the main problem does. Its restriction is the displayed side
ordering and metric family, not a weaker tiling convention.

## Exact evidence and restart boundary

[Resolved-strata record](../searches/partial-contact-cairo-alternate-resolved-strata.md)
indexes the explicit negative domains, primal-to-positive quotient search,
retained certificates and all replay commands. Independent root checkers:

    conda run --no-capture-output -n arisearch python research/reviews/verify_cairo_alternate_endpoint_marginals_independent.py
    conda run --no-capture-output -n arisearch python research/reviews/verify_cairo_alternate_f2a_slot_edge_independent.py
    conda run --no-capture-output -n arisearch python research/reviews/verify_cairo_alternate_f2a_slot_edge_independent.py --kind e2c
    conda run --no-capture-output -n arisearch python research/reviews/verify_cairo_alternate_f2a_slot_edge_independent.py --kind fac
    conda run --no-capture-output -n arisearch python research/reviews/verify_cairo_alternate_eac_periodic_independent.py

The independent obstruction checkers import no producer or solver. Fac's
numeric optimizer only proposed a vector; every final proof inequality
is exact rational arithmetic. Canceled redundant solver runs remain
UNKNOWN and are no part of this theorem.

No remaining geometric obligation exists inside this family. Reopen only
changed arm order, internal length coincidences, or other exact hypotheses.
Other internally distinct Cairo metrics on exceptional contact hyperplanes,
repeated-arm pairs, other pentagon angles and broader hexagon pairs remain
unclassified. This theorem is not a final mathematical report for the task.
