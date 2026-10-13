# Exact decision: repeated-angle U wheel with unrestricted quartic metric

Date:2026-10-13. Status: complete7680-case nonsingularity certificate, independently reviewed
VALID; superseded for U candidate coverage by the prior unrestricted
[at-most-two-U theorem](../lemmas/pentagrid-two-asymmetric-u-obstruction.md).
Pre-execution status was NOT YET RUN. This finite contract was
written before computation. No generic point search or other-angle family is
included. The previous fixedU length module is NOT imposed.

## Exact native index and geometric scheme

Take mu=1+sqrt5, lambda=sqrt(mu), and native pentagon edge directions

    (1,z⁴,z⁶,z⁷,z⁸),

where z=exp(pi*i/5), specified by z⁴-z³+z²-z+1=0, Im(z)>0,
4/5<Re(z)<81/100. The angle AFTER sideword is(1,3,4,4,3)*pi/5.
Therefore the vertex BEFORE outgoing sideword is

    m=(3,1,3,4,4).

The exact object sought is a positive length vector l_0,...,l_4 whose
edge-vector sum vanishes. No golden fixedlength relation, metric parameter
ratio or individual-monohedral exclusion is assumed.

Retain the explicit onecentral/fivecorner sixpiecewheel scheme of
[the earlier wheel record](resumed-two-size-six-wheel.md): each parentcorner
has one full childcorner, each parentside exactly two whole native childside
segments, and reflections unrestricted. Parent muP contains4P+2lambdaP.
This is NOT a classification of every sixpiecepartition.

For parent corneri, choose native childvertex j_i with m_(j_i)=m_i.
Choices: j_0,j_2 in{0,2}; j_1=1; j_3,j_4 in{3,4}.
These16 independent assignments need not be permutations: distinct children
may use the same native vertex index. Reflectionbit r_i swaps the two rays.
For parentsidei, startchild contributes

    t_i l_(j_i) if unreflected, else t_i l_(j_i-1),

and endchild atvertex i+1 contributes

    t_(i+1) l_(j_(i+1)-1) if unreflected,
    else t_(i+1) l_(j_(i+1)).

Indices modulo5; t_i in{1,lambda}. Central small implies2large corners,
central large implies1large corner, as previously. The16assignments times
480scale/reflection choices give exactly7680cases, without symmetry reduction.

## Exact closure and arithmetic field

Let phi=(1+sqrt5)/2=mu/2. The complex edge closure is equivalent to these
two equations, obtained by twice the real part and imaginary part divided
by sin(pi/5)>0:

    2l_0-phi(l_1+l_2)-(phi-1)l_3+(phi-1)l_4=0,
    l_1-l_2-phi(l_3+l_4)=0.

These coefficients lie in F=Q(lambda), lambda⁴-2lambda²-4=0. Thus no larger
composite field calculation is necessary, although the equations are exact
projections of closure in Q(z,lambda). Native lengths may be arbitrary
positive real numbers; in particular fullquarticmetric is permitted.

## Finite primary question and certificate decision

For eachcase, construct boundary M=lambda²I-C over F. If nonsingular, there
is no nonzero native length solution; closure need not be tested. If singular,
retain exactboundary rank and a kernel basis, append both closure rows,
and retain augmentedrank/kernel. If an augmentedkernel survives, test exact
positive-length feasibility with normalization sum(l)=1 and l_i>=delta,
delta>=0. A compact exactpolyhedral maximum delta>0 is necessary/sufficient
for all five lengths positive. Numerical feasibility is not accepted.

Retain casekeys, determinantcoefficients, singular kernel/rank data and all
positive feasibility witnesses or exactnegative results. A positive algebraic
length vector is only a closure/boundary solution, NOT a geometricdissection:
innercontacts, supportingconvexity and exactcovering still require proof.
No singular matrix or localclosure result will be called a candidate.

Deterministic SageMath exactnumberfield arithmetic; positive embedding chosen
by exactreal root isolation if feasibility is needed. No solver, randomseed,
floating branch or globaltiling query. If computation is interrupted, preserve
actual partialcounts and never report incompletion as UNSAT.

## Completed exact result and angular scope audit

All7680 boundary matrices are NONSINGULAR in Q(lambda). There are0singular
cases,0boundary kernels and0positive closure/boundary solutions. Consequently
no closure or positive-feasibility branch was needed. This is a complete
negative result over precisely the stated native-assignment/scale/reflection
domain, valid even for arbitrary real side lengths.

The necessary boundary schema allows additional children to touch the
parent-side two-segment joints at isolated native corners. It does not assume
exactly two interior sectors at such a joint or require the central child to
avoid boundary points. Thus this algebraic exclusion covers a larger set of
necessary boundary data than a strict interior-center/ring wheel.

The strict two-sector version is already killed cheaply by angles. Native
vertex1 is the unique36corner, with native108neighbors at vertices0and2.
Its corner child uses this native36corner, so both its fullboundary sides
end at108corners strictly inside parent sides. A two-sector flat junction
would require108+beta=180 with beta in{36,108,144}; none works. If a third
child touches the junction, the only possible sum is108+36+36=180.
Both adjacent parent-side joints require such a three-corner event. Therefore
point contacts could evade the strict two-sector angular argument, although
no actual compatible point-contact dissection is asserted. The broader7680
boundary test above permits them and still has no nonzero length solution.

The computation was launched immediately before this angular attack was
received. Its broader point-contact-allowing contract was already written;
the domain finished before the next status poll. The audit does not pretend
that running this test was needed to kill the strict wheel.

Producer:[resumed_intrinsic_repeated_u.py](resumed_intrinsic_repeated_u.py).
Certificate:[resumed_intrinsic_repeated_u.json](../certificates/resumed_intrinsic_repeated_u.json).
All7680case labels and exactdeterminant coefficientvectors are retained.
The certificate has empty singular/positive lists, exactly matching the
complete domain. No kernel data or feasibility witness was omitted.

Read-only replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/resumed_intrinsic_repeated_u.py --check research/certificates/resumed_intrinsic_repeated_u.json

## Prior-result match and definitive route state

After this computation, repository inspection recovered the already reviewed
[maximum-side two-U obstruction](../lemmas/pentagrid-two-asymmetric-u-obstruction.md).
Its hypotheses are at mosttwo genuine convex pentagons with cyclic angleword
(36,108,144,144,108), arbitrary positive metrics, all isometries, omission and
unrestricted partial contacts. Our before-sideword(108,36,108,144,144) is a
cyclic rotation of exactly that word. The theorem has no equal-long-side,
common-scale, algebraic-length or edge-to-edge assumption, and uses no
monohedral classification. Its native-measure dependency and maximum-side
argument have separately reviewed VALID records.

Therefore EVERY proposed U two-size pair is already untileable, irrespective
of this wheel or metric module. A repeatable ordinary substitution would
imply a plane tiling by iterated growing convex parents and compactness,
contradicting that theorem. This7680 computation is **superseded for candidate
coverage** and carries no new novelty claim. It is retained only as exact
finite audit evidence. Stop U construction: neither arbitrary quarticmetrics,
newwheel contacts nor more boundary-point variants justify reopening it.
The distinct-angle generalwheel theorem and the general105/94count reduction
are unaffected. A materially new route must change the angular hypotheses
or use a genuinely different source compiler with exact two-shape output.
