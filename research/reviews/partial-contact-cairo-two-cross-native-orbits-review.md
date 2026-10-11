# Independent review: complete two-cross native symmetry orbits

Verdict: **VALID for the retained72-pattern/13-orbit enumeration and the two named periodic-orbit representative maps.** This audit does not certify the remaining event-flat enumeration or claim any local survivor tiles.

`research/reviews/verify_partial_contact_cairo_two_cross_orbits_independent.py` independently generates the72 injective matchings by choosing two distinct P arms, two distinct Q arms, and either bijection. It forms group orbits by repeated application of the actual native reflections i->3-i on either prototype and species transpose. Every retained matching and canonical representative in `research/certificates/partial-contact-cairo-two-cross-native-orbits.json` agrees exactly. Orbit sizes are4,8,8,4,8,2,4,8,8,8,4,4,2, totaling72.

The two native reflections commute. Species swap conjugates P reflection to Q reflection and does not commute with an individual reflection. The originally extracted native reduction text's phrase "three commuting involutions" was therefore inaccurate; it was reported promptly to root and the actual extraction now uses the corrected wording. The enumeration itself uses the correct generated action, and this wording does not affect its mathematical coverage. The group has eight transformations, including both possible native reflection choices and species swap.

The swapped periodic representative P0=Q2,P2=Q0 maps to canonical(01,23). The Y representative P1=Q3,P2=Q0 maps to canonical(01,32). All points on those full positive partner cones transfer under the native congruences/species presentation changes; the actual periodic construction dependencies are separately reviewed. This audit checks the orbit assignments, not their imported geometric constructions.

Replay: `conda run --no-capture-output -n arisearch python research/reviews/verify_partial_contact_cairo_two_cross_orbits_independent.py` — PASS all72 matchings in13 complete orbits and both periodic representative mappings. The global aperiodicity target remains unresolved.
