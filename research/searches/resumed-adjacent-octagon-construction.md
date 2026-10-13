# Exact search record: adjacent-alpha equality covering

Date:2026-10-13. Status: independently reviewed VALID periodic escape;
falsified as an aperiodic construction. Full exact definitions and plane
covering proof: [counterexample](../counterexamples/resumed-adjacent-octagon-periodic-equality-pair.md).
Independent [review](../reviews/resumed-adjacent-octagon-construction-review.md)
and [separating-axis verifier](../reviews/resumed_higher_adjacent_octagon_verify.py).

## Replay and finite-domain record


Command:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/resumed-adjacent-octagon-check.py

Observed result: PASS: exact strict 2Q+4P motif, angle words, area identity, and44 complete bounding-box overlap checks.

Question: does this one exact pair admit the stated infinite covering? Domain: six exact motif polygons and every bbox-eligible relative lattice translate (44 tests), plus the exact angle/closure identities. Encoding: Sage AA vectors; deterministic Sutherland–Hodgman convex clipping. Transformations allowed: all translations by ZS+ZT and the explicitly stated half-turn/reflection motif copies. Seeds, solver, timeout and external enumeration: none. Completion: PASS; all domain cases exhausted. Trusted arithmetic: Sage real algebraic field; overlap code is separate from the geometric identities used to build the motif. The retained coordinates are the witness, and the small clipping procedure is its checker.

An earlier diagnostic assertion failed because reflected polygon lists were clockwise; reversing their order repaired that computational convention, with no geometric change. The completed run above is the evidence. No failed run is labelled UNSAT.

## Restart condition

The necessary AA=BB equality admits this exact periodic pair. The general
equality-locus tilability/periodicity classification remains unproved. A new
construction must change the metric geometry and avoid this or another
periodic carrier; no enlargement of this singleton overlap check is needed.
