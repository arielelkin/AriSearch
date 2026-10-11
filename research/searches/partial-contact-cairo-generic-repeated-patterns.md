# Generic repeated-arm Cairo patterns: exact exhaustive record

Date: 2026-10-10. Python 3.12.13, SageMath 10.9. Field: Q(sqrt3), positive embedding 1<sqrt3<2. No floating-point
choices, optimizer, random seed, deadline or finite patch search. No
symmetry reduction. This is an exact algebraic enumeration of 738 complete
cross equality patterns over the four allowed internal partitions D, R01,
R23, S, followed by necessary contact tests and sufficient cone containment.

Per ordered type count: D/D has 209; D/R01, D/R23, R01/D and R23/D
have 73 each; D/S and S/D have 21 each; each ordered R/R pair has 34;
each ordered R/S or S/R pair has 13; S/S has 7.
Cross matchings are injective between collapsed internal length labels, but
all geometric native bank slots remain 0..7. Exact kernel comparisons detect
any extra forced arm equality. Exact Polyhedron over the field backend checks
positivity >=1 and retains actual eight-arm/two-e/kernel-coordinate witnesses.

Of 738 patterns, 70 force extra equality, 668 have positive exact strata,
517 give generic beta obstructions, and 151 are local survivors, all mapped
to reviewed periodic cones. No empty positive cone, forced e/event identity
or uncovered local survivor occurs.
The D/D count22/155/32 reproduces the prior independent classification.
Genericity means removal of finite proper event/event,e/event,and nonforced
eP/eQ hyperplanes. It is certified by open positive cone avoidance, not by
claiming every retained positivity witness is itself generic.

The necessary test uses S_i intersections for ACTUAL native slots with
complements (1,0,3,2,5,4,7,6), no transitive closure. It checks both e seam
orientation signs and both 120 endpoints, and requires an allowed seam for
each species because the monohedral classification excludes either species
alone in the generic subset. Surviving native equalities are mapped to the
swapped or general-Y cone under exact native reflections/species swap.
Certificate retains the full positive witnesses, quotient forms, allowed
seams, native compatibility and periodic mapping for each survivor.

    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-generic-repeated-patterns.py
    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-generic-repeated-patterns.py --output research/certificates/partial-contact-cairo-generic-repeated-patterns.json

Output: 70/517/151 as above. This has received fresh independent hostile review as VALID and closes
only the explicitly generic strata; proper exceptional metric hyperplanes
remain unclassified. No nonperiodicity or failed-extension inference is made.
