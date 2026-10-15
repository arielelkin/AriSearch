# Six-distinct / four-distinct all-shared bounded gate

Date: 2026-10-15. Completed finite computation, with no atlas-cap skips.
This record covers a new side-multiplicity domain; no finite quotient or
periodic-placement search was run.

## Declared domain and encoding

A=(0,1,2,3,4,5). Its two private numerical side values are normalized to
{0,2} or {0,3}; B uses exactly the other four A labels. For each alphabet,
enumerate all surjective length-six words: 1,560 linear words, giving
3,120 total. Quotient only B rotations and reflections, yielding 136 words
per alphabet. Both distributions (3,1,1,1) and (2,2,1,1) are included.
A-private adjacency is excluded by the separate analytic AAA obstruction.

Every local star is encoded by a three-ray multiset, retaining repeated
rays and repeated actual corner indices. Native left/right side-slot flips
at all three corners are simultaneous microstates. A candidate star
survives only if some microstate supports all three native far-end corner
pairs, with multiplicity, in the current atlas. Iterate deletion to closure.
For every resulting atlas of at most sixteen stars, enumerate ALL its
corner-cover subsets and retain those satisfying the same simultaneous
endpoint condition. The largest actual retained atlas had twelve stars,
so the entire declared domain completed, with no skipped subsets.

The private-pair {0,2} case has sixteen feasible numerical words and
seventy-three closed supports; the {0,3} case has twenty words and ninety
supports. Thus 163 exact endpoint-closed corner covers survive. Of these,
114 directly contain a formal four-slot matching ring. Among the 49 others,
23 force a legal ring by exact rational combinations of polygon totals
and occurring-star angle equations. All twenty-three row certificates are
retained and passed an initial Fraction-only arithmetic check. The current
small checker targets the twenty-two proof-relevant certificates in the
separate narrow double-pair record.

## Stable double-pair consequence

The distribution (2,2,1,1) contributes 2,160 linear words, 192 B-cyclic
words, twenty-four endpoint-feasible numerical words and ninety-three
closed supports. Seventy-one contain a ring directly; the other twenty-two
force a ring by verified rational angle equations. A standalone stdlib-only proof producer and narrow certificate are
[hexagon-six-four-double-pair-certificate-2026-10-15.py](hexagon-six-four-double-pair-certificate-2026-10-15.py)
and [its retained record](../certificates/hexagon-six-four-double-pair-certificate-2026-10-15.json).
The complete restricted
periodic-escape theorem is extracted into
[the double-pair lemma](../lemmas/hexagon-six-four-double-pair-periodicity-2026-10-15.md).
Its independent full finite-classification and gluing review is pending.

## Triple-repeat residual and exact limitations

All 26 remaining no-span-ring supports have distribution (3,1,1,1).
Eight are four-star actual-corner partitions. Checking every endpoint-supported
native-arm microstate shows that each of those eight fixes every one of
the twenty-four corner/incident-side neighbor maps uniquely, including
any repeated B-arm ambiguity. They therefore fit the intrinsic-determinism
bridge, subject to fresh review of this application.

The other eighteen supports have ambiguous neighbor maps and contain pure-B
stars. They cannot be dismissed using corner coverage or the existing
intrinsic-determinism hypothesis alone. For a small exact obstruction,
use A-private pair {0,2}, B=(1,3,4,4,4,5), with occurring support

    {(0,5,11),(1,2,6),(3,7,9),(4,8,10),(8,8,8)}.

The angle vector in units pi

    A=(1/9,17/18,1/9,17/18,17/18,17/18),
    B=(17/18,4/9,2/3,11/18,7/18,17/18)

has all entries strictly between zero and one, each hexagon sum four,
each displayed star sum two, and no legal formal ring. The support passes
the simultaneous native-arm endpoint condition and has six ambiguous
corner-side neighbor maps. This is a countermodel to a proof using only
that endpoint condition, convex angle bounds, polygon angle totals and
full local neighbor determinism. It is NOT a convex polygon realization,
finite tiling patch, infinite tiling, or aperiodic example. The missing
geometric polygon closure and global extension have not been inferred.

The root agent is independently developing a private-AA-chain separator
mechanism for these triple-repeat metrics. This record does not claim that
periodicity of an A skeleton forces compatible periodic filling of all gaps.
That global bridge requires its own complete proof and hostile review;
no larger quotient or period bound was explored here.

## Artifacts and replay

Producer:
[hexagon-six-four-all-shared-gate-2026-10-15.py](hexagon-six-four-all-shared-gate-2026-10-15.py).
Retained data:
[certificate](../certificates/hexagon-six-four-all-shared-gate-2026-10-15.json).
Separate arithmetic verifier:
[hexagon-six-four-row-certificate-check-2026-10-15.py](hexagon-six-four-row-certificate-check-2026-10-15.py).

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-six-four-all-shared-gate-2026-10-15.py
    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-six-four-row-certificate-check-2026-10-15.py

Default producer output is JSON; --output PATH explicitly writes the same
record. The proof-relevant steps use Python finite sets, native indices,
multisets and exact rational linear algebra. The producer also retains
exploratory exact Z3 SAT angle models for at most three residual supports
per word; these models are countermodels to local angle strategies and
are not proof dependencies of the double-pair theorem. There are no
random seeds, numerical angle tolerances, period sizes, or solver UNSAT
claims. Commands completed normally.
