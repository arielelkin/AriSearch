# Reversed shared right pair: exact noncentral periodic fixture

Status: root-produced exact finite fixture, fresh review pending. This is
new geometry outside the zero/one-cross exclusion, not a full-cone theorem.

P=(1,z,(3sqrt3-z)/2,(sqrt3*z-1)/2,2),
Q=(z,1,(3sqrt3*z-1)/2,(sqrt3-z)/2,2z), at z=4/5.
The shared right pair is reversed: Pa=Qb and Pb=Qa. Each species has four
distinct arms. Both private cores contain four axis-reflected native faces;
the Q core is quarter-turned and translated by(0,3sqrt3).

Periods(sqrt3*z,-sqrt3),(3sqrt3*z,3sqrt3), covolume18z.
The exact eight face areas sum to18z. Inverse-lattice bounding boxes cover
every potentially overlapping translated face pair; all84 candidates pass
exact separating-axis tests. Native congruences, norms and strict supports
are independently checked inside this producer. The locally finite closed
union plus multiplicity at most1 and area/covolume equality proves coverage
at this exact fixture. A separate fresh review is still required.

The initial speculative second period(3sqrt3,3sqrt3*z) failed the area test;
it was replaced before any accepted existence claim. The corrected second
period is(3sqrt3*z,3sqrt3). Full positive-cone boundary cancellation is
being developed in a separate artifact, not inferred by deformation.

Read-only replay:

    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-reversed-right-pair-periodic-fixture.py

--output explicitly retains the finite fixture certificate. No solver,
randomness or finite lattice index cutoff is used: exact inverse projections
bound all relevant translates. This construction establishes a proposed
periodic escape at one metric, no universal periodicity or aperiodicity.
