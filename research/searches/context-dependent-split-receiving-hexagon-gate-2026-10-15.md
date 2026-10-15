# Changed split contexts: diagonal freedom exists, but its thick turn fails

Date: 2026-10-15. Completed analytic gate; independently hostile-reviewed VALID
([review](../reviews/context-dependent-split-receiving-hexagon-astra-hostile-2026-10-15.md)).
No metric search, source-neighbor census or periodic quotient search was run.

The new construction change relaxes mark-local splits while retaining
mark-local donor triangles. Each physical edge has one actual M, used on
both sides. A valid maximally general rule lets its unique receiver choose
M from source, parity or arbitrary neighbor context; its donor reads that
same physical point. Requiring both sides to compute a context-local rule
independently could impose additional adjacency equalities, but none is
assumed by this gate. Thus no unsupported all-neighbor condition can
artificially close the construction.

Before any convexity test, common-H unique-angle diagonal identities leave
one real split parameter: all thin receiver splits have one tail distance
D36, while all four thick receiver splits and D72 equal 1/2. The reason is
local and stronger than mark-sharing propagation: on each thick Y receiver,
BOTH original source endpoints become retained 72-degree H vertices, so
their common opposite-M distances are m and 1-m. Uniqueness of 72 forces
m=1/2. A thick X receiver's retained tail angle is also 72, so its split
inherits 1/2 through the common H diagonal. This works within each thick
rhomb and uses no assumption about its actual neighbor species.

The apparent free thin parameter does not give geometric feasibility.
At the thick X tail, internal and external donor nodes are ALREADY identical
mark-X triangles at a 72-degree source angle; no equality between X and Y
triangles is needed. In the endpoint branch Xt=Yt=beta, Xh=beta+36,
0<beta<36, put r=tan(beta),q=tan36 and A0=q(1-r²)+2r. The exact native M
turn at its compulsory midpoint is

    D= -uX*sin72/(2*A0) * [q(1-rq)+q*r²+(2+q²)*r³] < 0.

All factors have known strict signs because 0<r<q<1. Thus even the proposed
cheap identical-donor/large-thin-split feasibility experiment is impossible;
the same universal obstruction excludes every Y triangle and all context
split choices. There was no reason to choose or scan numeric split values.

The result is extracted into
[the standalone lemma](../lemmas/context-dependent-split-receiving-hexagon-obstruction-2026-10-15.md).
The [exact symbolic checker](context-dependent-split-receiving-hexagon-check-2026-10-15.py)
assembles all sixteen source-arrow endpoint contexts, verifies both thick-Y
two-72 cases and the same-X-tail thick contexts, solves the ten independent
receiver-diagonal equations (rank nine in ten variables), and proves the
universal rational turn identity over QQ(r,q). It completes with PASS:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/context-dependent-split-receiving-hexagon-check-2026-10-15.py

Finite/symbolic domain: four source/parity cases; sixteen actual endpoints;
eight independent receiving-context split variables plus D36,D72; one
bivariate rational identity. No solver, random seed, numerical angle,
parameter sample, grid, or cap congruence alias enumeration is involved.
The strict sign argument is written in the lemma and is not inferred from
special values. The proof includes arbitrary physical split contexts, so
unexamined Ammann neighbor choices cannot evade this local contradiction.

A genuinely changed next mechanism must alter mark-local donor triangles,
the retained original-endpoint/opposite-M topology, or the requirement that
all receiving hexagons share one prototype. This note establishes no
two-shape candidate, infinite unmarked cover or shape-only forcing theorem.
