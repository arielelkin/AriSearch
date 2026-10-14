# Fresh hostile review: native-occurrence propagation and fixed torus model

Date: 2026-10-14. Verdict: **VALID** for [the no-full-edge theorem](../lemmas/pentagon-y-whole-edge-native-propagation-2026-10-14.md). The unrestricted partial-contact problem remains open.

The checker derives corner cosines and arm lengths from the integer P/Q coordinates independently. It verifies the exact angle labels, all seven angle-only stars and all reflected arm choices, giving exactly five length-compatible stars. In particular it proves the complete ray signatures of rgg and abg. The contradiction does not rely on CP-SAT, finite counts, a flat torus, a chosen handedness, or a patch fixture.

I attacked each far-endpoint inference. A Q GG side has squared length 4 and cannot meet another Q GG side: the only star with adjacent G corners is rgg, and its G-G ray has squared length 2. It therefore meets P RA. The particular P's R belongs to rgg, so both its RA sides meet G corners. Every native squared-length-4 side incident to G has G at its other end. Hence both actual A corners of this same P lie in abg stars. At each A, the squared-length-5 ray meets a B corner, and every native squared-length-5 side incident to B ends at A. Both actual B corners of the original P therefore lie in abg stars too. Their connecting BB side has squared length 2; its mate would need G at both endpoints. The side inventory has no GG side of that length. All steps are forced by complete native sides and follow actual occurrences within one P, rather than just aggregate corner counts.

The remaining P-only case is excluded locally: there is no completion of an A or B corner using only r,a,b in the five-star atlas. Reflections preserve all native side/corner incidences used in the contradiction. The independent checker explicitly verifies P's reflection `(x,y)->(y,x)` as native index reversal `i->-i`, and Q's reflection `(x,y)->(-x,y)` as reversal `i->3-i`, with indices modulo five.

The conclusion is no full-native-edge plane covering by this pair. At a subdivided side the far-endpoint neighbor can change along the side, so the final BB mate need not be one tile having GG endpoints. The manuscript correctly leaves that unrestricted possibility open. Enlarging full-edge quotients cannot repair the obstruction.

I also reviewed [the fixed 6P+4Q CP-SAT model](../searches/pentagon-y-6p4q-flat-torus-cpsat-2026-10-14.py). Every side is paired exactly once with equal squared length and reversed endpoint identifications. The corner variables have precisely the label-permitted star domains; their reified assignments and per-label capacities enforce the necessary star counts. Fixing P's unique R corners at the two rgg vertices and four occurrences at rrrr is a sound permutation of identical P faces. Fixing Q's unique D corners at the four aad vertices is likewise a face/vertex relabeling. The explicit reflection automorphisms above justify its canonical face handedness without losing any possible gluing.

Its corner successor `c->next(mate(c))` is the correct cyclic link traversal after reversed full-edge gluing. The postcheck requires fifteen complete star links and a connected dual face graph. Its no-good cut removes a selected edge matching only when those combinatorial links or connectivity fail; these properties depend on the edge matching itself. In this actual run no lazy rejection occurred. The frozen [certificate](../certificates/pentagon-y-6p4q-flat-torus-cpsat-2026-10-14.json) records INFEASIBLE, 0.051 seconds of solver time, zero branches and no witness. The fresh native propagation proof independently excludes its entire domain, so the negative conclusion does not require trusting solver presolve.

Independent exact replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/pentagon-y-no-full-edge-independent-2026-10-14.py

The Sage checker passed. No mathematical defect found in the new propagation theorem or the reviewed fixed-domain model. No developed polygon placements or period lattice are asserted, because there is no witness.
