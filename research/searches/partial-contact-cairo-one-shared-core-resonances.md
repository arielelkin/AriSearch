# Twelve core-resonance hyperplanes: exact first contact filter

Date: 2026-10-10. Python 3.12.13, SageMath 10.9. Arithmetic Q(sqrt3),
positive embedding 1<sqrt3<2. No random seed, timeout or patch search.
This exploratory computation was subsumed by the complete event-flat
intersection enumeration and is not an independently reviewed theorem.

The exact domain comprises twelve single added equations to the Cairo
closure and sole cross-arm Pa=Qd condition: b+C=2x, eP=2x or eQ=2x,
x in {Pc,Pd,Qa,Qb}. Each native slot remains distinct; only numerical
arm classes are identified. Exact positive-cone feasibility uses Sage's
field polyhedron backend. All twelve strata are positive and preserve
exact native arm privacy.

For the generic subset of each quotient kernel, side compatibility is:
equal arms or intersecting actual native event sum sets; e/arm only when
the e length is an event total at that actual bank slot; e/e only when
its lengths agree. The computation exhausts56 unordered120 corner triples
and8 choices of native reflection orientations. Cyclic order reversal is
already represented by reversing all three corners, since compatibility
is symmetric. Every hyperplane lacks at least one obligatory native120
corner. Proper deeper hyperplanes were not part of this domain and can
add contacts. No conclusion is drawn about their metrics.

Completion: PASS over all twelve exact generic strata. All positive
witnesses, native forms and allowed star lists are retained in the JSON.
A positivity witness need not be generic; nonempty generic subsets follow
from open positive cone avoidance of finite proper hyperplanes.

    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-one-shared-core-resonances.py --output research/certificates/partial-contact-cairo-one-shared-core-resonances.json
