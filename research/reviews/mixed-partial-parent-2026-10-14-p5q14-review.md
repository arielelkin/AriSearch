# Fresh hostile review of the forced neighboring-Q P5/Q14 obstruction

Date: 2026-10-14. Reviewer: mixed-partial-parent construction agent, which
did not develop the P5/Q14 transition proof. **Verdict: VALID** for the
fixed exact pair and the stated equiangular-Q14 corollary, with the explicitly
reviewed earlier ring/palette reductions as dependencies. The unrestricted
two-convex-tile problem remains unresolved.

## Exact claim reviewed

[Proof](../proofs/p5q14-orientation-transition-2026-10-14-untileability.md),
[producer](../searches/p5q14-orientation-transition-2026-10-14.py),
[compact64-case certificate](../certificates/p5q14-orientation-transition-2026-10-14-compact.json), and
[author's separately coded NumberField verifier](p5q14-orientation-transition-2026-10-14-verifier.py).
The claim is that the exact P with edges(z^-5,z,z^7,v*z^13,y*z^19) cannot
tile together with the equiangular Q14 having native length word(v,v,1,v,v,1,1)^2,
under all isometries and unrestricted contacts. Here z=exp(i*pi/14),
y=2sin(pi/14)+4sin(pi/14)^2, and v=1+2sin(pi/14)(1-y).
The extended corollary treats arbitrary strictly convex equiangular Q14
partners through the earlier proved side-length/count and35-word reduction.

## Fresh reconstruction, separate from raw placement generation

I wrote a [fresh checker](mixed-partial-parent-2026-10-14-p5q14-review.py) that
imports neither the transition author module nor an earlier adversary module.
It reconstructs P and displayed Q from their exact edge vectors in
CyclotomicField(28), then generates the permitted native P1/P3 guests itself.
For each side it tries both isometry hands and both endpoint maps and selects
the outside placement by an exact half-plane test. It constructs actual
14-cycles by equality of the neighboring PP-edge far endpoints, reflects
all mandatory native-y mates, identifies duplicate actual faces, and checks
interior separation and all strict corner-in-side incidences.

Its fresh canonical domain is exactly64 native ring cycles. The results are:

- 28 mandatory-dimer positive-area overlap rejections;
- 32 mandatory-patch forbidden T-contact rejections;
- 4 surviving21-face patches, each satisfying the native-star submultiset test.

The four freshly generated actual patch sets equal the four canonical frozen
sets. Frozen raw guest placement data enter only this comparison, after the
entire canonical domain and all rejection geometry were generated independently.
The remaining earlier seven-word normalization is checked by the separately
replayed NumberField verifier: every one of28 indexed positives has an exact
face-preserving isometry to one of the four canonical states, including ordered
native P labels. Thus this is not a loose count agreement or an unordered-only
native-label match.

In the fresh four states, unit-slot5 guest F, unit-slot6 guest G, and F's native-y
reflection mate M agree exactly across all states. The checker generates every
Q isometry sharing F's obligatory native-v side: eight native Q-v indices,
both hands, and both endpoint maps, with one outside endpoint order per index
and hand. This is16 indexed attachments and four physical Q polygons per state.
All64 indexed cases have a Q corner strictly inside G's or M's native-v side.
The independently computed exact parameters are1/v or(v-1)/v, strictly inside
(0,1) since v>1. The retained [fresh certificate](../certificates/mixed-partial-parent-2026-10-14-p5q14-review.json)
records the64 native indices and pointed witnesses.

## Necessity and attempted defects

The complete angle palette is checked analytically: 5A+4B+6C=14 has only
(2,1,0) and(0,2,1), while all native angles exceed pi/2. Hence genuine T
contacts cannot occur and all contacts must be whole native edges. This
justifies the finite attachment domain rather than imposing it.

The earlier native-dimer argument forces every native-v side to Q. F's native-v
edge is outside the central Q and is not one of its edges; therefore it requires
a different Q, with exactly one of the enumerated eight native-v side indices.
No unit/v alias is omitted because0<y<1<v. The native-y mate is mandatory
regardless of which hand F has. The two other host faces used in the witnesses
are actual distinct tiles in each mandatory patch; the fresh21-face identity
census confirms this.

I checked reflected winding by ordering polygons according to exact signed area
before supporting-line separation. I retained both hands and both endpoint
maps until the outside half-plane selection, so reflection symmetries of Q
cannot silently remove an index case. Four physical Q placements are only a
reported deduplication; all16 indexed cases remain tested for every central
state. I checked strict rather than weak segment containment, and every
parameter lies in the open interval. A zero-length touch or a coincident native
endpoint therefore cannot rescue any witness.

The proof's Q-presence deduction handles omission: P alone conflicts with
its one-alpha/four-beta corner supply, with only linear boundary error in a
large square. Q alone is locally forbidden by the full-star palette. For the
arbitrary-equiangular-Q14 corollary, the earlier counting argument forces
8v/6u, exact closure forces equal antipodal lengths, and the complete35-word
classification/palette audit supplies the28 positives. Those earlier complete
reductions have their own independent reviews and remain explicit dependencies.
This new review independently regenerates the displayed canonical domain and
all mandatory extension placements; it does not claim to newly rerun all3003
binary masks or all896 original cycles.

No defect was found in the new fixed-contact proof. The full1536 exploratory
neighbor-ring domain is not needed to infer untileability: a required next Q
already fails before its own ring is considered. Accordingly possible alternative
ring states, periodic quotients, transition holonomy and further radii cannot
repair this exact local obstruction. No assumption of a particular hierarchy,
orientation class, chirality rule or bounded periodic motif enters the theorem.

## Replay and verification evidence

Both the NumberField verifier and the fresh geometry checker completed without
solver limits, randomness or numeric tolerances. The fresh checker prints:

    PASS fresh geometry generation:64 canonical cycles,28 overlap+32 T+4 survivors; all64 required Q placements have T at1/v or(v-1)/v.

Replay (default is a readonly comparison with frozen fresh evidence):

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/mixed-partial-parent-2026-10-14-p5q14-review.py
    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/p5q14-orientation-transition-2026-10-14-verifier.py

The new mathematical theorem is VALID on its stated candidate-family scope.
This does not supply an aperiodic pair or classify all possible convex pairs.
