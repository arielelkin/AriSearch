# Fixed 6P+4Q whole-edge flat-torus CP-SAT experiment

Date: 2026-10-14. Result: INFEASIBLE in the declared fixed model.
Independent model audit VALID in
[the fresh review](../reviews/pentagon-y-no-full-edge-hostile-2026-10-14.md);
no larger domain launched.

Explicit scheme: construct a compact flat torus from six P faces and four Q
faces of the interface-Y fixture. Exactly 50 native sides must be paired,
with reversed endpoint order and equal numerical lengths. Vertex slots are
two rgg, four aad, four bbcc, four abg, and one rrrr. These are the necessary
counts from the independently reviewed full-edge incidence lemma.

Bounded model: side-pair BoolVars make an exact perfect matching within each
squared-length class. Every corner has a finite-domain vertex-slot IntVar.
Per-slot native label counts equal its specified star. Every selected pair
identifies the side's start with its mate's end, and vice versa. Reflections
are allowed: P has intrinsic reflection symmetry y=x, and Q has intrinsic
reflection symmetry x=0, so any reflected face placement is congruent to a
direct placement with native indices reversed by that symmetry.

Sound permutation symmetry fixes the six unique P R corners at slots
0,1,14,14,14,14, and the four unique Q D corners at AAD slots2,3,4,5.
There are exactly two RGG R occurrences and four RRRR R occurrences; faces
of the same species may be permuted and equal-star vertex slots relabeled.
Every Q D lies in a distinct AAD vertex, permitting the latter fixed order.

The model is a necessary relaxation until quotient links and face connectivity
are validated. Any proposed solver assignment is checked by the successor
permutation c -> next(mate(outgoing_side(c))). There must be exactly fifteen
single circular corner links with the declared actual labels, plus one
connected face graph. A rejected complete pairing gets a lazy nogood, up to
the declared cap. A valid assignment would have V=15,E=25,F=10, orientable
reversed side identifications and angle2pi at every vertex, hence a compact
flat torus and an infinite plane covering through its universal cover.
No solver assignment was found in this run, so no such implication was used.

Predeclared limits: cumulative120seconds wall from model construction,
100 rejected-pairing assignments, one worker, seed20261014. Stop at first
validated flat torus, CP-SAT INFEASIBLE, UNKNOWN/time cap, or rejection cap.
No automatic larger bound. Official status semantics were checked at
[official CP-SAT documentation](https://developers.google.com/optimization/cp/cp_solver).

Actual result: OR-Tools9.15.6755 returned INFEASIBLE in0.051064536seconds;
complete experiment elapsed0.062758132seconds. Zero branches, zero conflicts,
zero rejected assignments. Thus the relaxed fixed native-edge gluing model
already has no assignment. This is stronger than a failed quotient-link
check within this fixed count, but it is not an unrestricted-contact result.

Model/replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/pentagon-y-6p4q-flat-torus-cpsat-2026-10-14.py

Retained result: research/certificates/pentagon-y-6p4q-flat-torus-cpsat-2026-10-14.json.
The script's --check option verifies saved positive witnesses without solving.
For this negative record it verifies domain/caps/status metadata, native
incidence/chirality premises, and invokes the fresh independent Sage native-
propagation checker. It does not rerun CP-SAT or treat historical timing
fields as a formal UNSAT certificate. Replay that non-solving check with:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/pentagon-y-6p4q-flat-torus-cpsat-2026-10-14.py --check research/certificates/pentagon-y-6p4q-flat-torus-cpsat-2026-10-14.json

Independent model soundness audit and stronger proof review are recorded
separately. No claim of a formal solver proof
certificate is made; the retained JSON is a reproducible run/status record.

Stopping condition: the fixed6P4Q whole-native-edge torus scheme stops at
INFEASIBLE. Partial contacts and alternative mixed assemblies remain outside
this experiment. The subsequent [native-occurrence propagation theorem](../lemmas/pentagon-y-whole-edge-native-propagation-2026-10-14.md) independently excludes every whole-native-edge plane tiling, including infinite nonperiodic ones. Its fresh Sage checker and hostile review passed; unrestricted partial contacts remain outside. This stronger proof supersedes all larger whole-edge searches for these atoms.
