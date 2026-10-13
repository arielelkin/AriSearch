# Exact search record: two-size negative-conjugate counts


**Superseded for U candidate coverage:** the previously reviewed
[unrestricted at-most-two-U theorem](../lemmas/pentagrid-two-asymmetric-u-obstruction.md)
already excludes every pair of these cyclic angles at arbitrary metrics,
including fullquartic lengths and partial contacts. The U-specific boundary
application below is retained as an exact audit, not a new construction route.
The general count reduction and non-U statements remain unaffected.
Date: 2026-10-13. Status: exact105/94/67 count domain; independently reviewed
VALID. The complete count theorem, d=0 qualification and U metric obstruction
are extracted to [the lemma](../lemmas/two-size-pentagon-small-inflation-and-boundary-module.md).
The [independent review](../reviews/resumed-two-size-negative-conjugate-review.md)
checks the quartic field and whole-side boundary arguments separately.

## Exact domain and encoding

An ordinary substitution on two genuine convex pentagons with irrational
area inflation1<mu<6 must have the one-child cross-species parent rule.
Its count matrix is [[0,b],[1,d]], with mu²=dmu+b and negative conjugate.
The complete finite domain is

    d=0,...,5;
    max(1,6-d)<=b<=35-6d;
    d²+4b not a square.

Counts are105 before the square test,94 after,67 with d>0. Nonnegative
integer b,d are the only search variables. No metric positions, orientations,
contact graphs or finite patches are enumerated; there is no symmetry
reduction, solver, numerical tolerance, seed or timeout.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python -c 'from math import isqrt; c=[(b,d) for d in range(6) for b in range(max(1,6-d),36-6*d)]; a=[(b,d) for b,d in c if isqrt(d*d+4*b)**2!=d*d+4*b]; assert len(c)==105 and len(a)==94 and sum(d>0 for b,d in a)==67; print("PASS:105 integer,94 irrational,67 d-positive counts")'

This exact complete test passed. No separate certificate is needed for the
small explicit integer domain; the command contains the full enumeration
and deterministic arithmetic membership test.

## Mechanism state

All94 counts are impossible for the exact U fixture with native side lengths
(phi³,phi³,1,1,1), by the proved boundary-module theorem. That geometric
exclusion uses no pentagon-classification dependency. The statements that U
is monohedrally untileable and d=0 yields a periodic omission are explicitly
conditional on the imported complete pentagon classification.

Other metric pentagons remain outside this exclusion. A concrete escape
must change the length module and give a pointwise actual parent dissection;
a new arbitrary pentagon is not a candidate. The separate
[six-piece-wheel test](resumed-two-size-six-wheel.md) examines one explicit
changed contact scheme at mu=1+sqrt5. No larger generic point search or
closed enumeration was reopened.
