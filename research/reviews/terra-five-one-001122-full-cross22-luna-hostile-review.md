# Independent hostile review: A001122 two-ended cross22 escape

Date: 2026-10-13. Reviewer: luna. Status: VALID for the stated native spatial lemma
[reviewed theorem](../lemmas/terra-five-one-001122-full-cross-22-escape.md).
The final written theorem was inspected after independent reconstruction.
This review does not claim all-mask coverage from a local seam.

## Exact reviewed statement

A is an actual genuine convex hexagon with native angles001122, meaning
(x,x,y,y,z,z), where y=720−5x,z=4x−360 and108<x<126,x≠120.
If two A copies share the full native side4 (22) on one copy, and BOTH seam
endpoints have native AAA triples containing one corner of each colour, then
A itself has an admitted periodic monohedral tiling. Arbitrary side equalities,
reflections, and all possible native corner aliases are included. No assumption
of global tilability is required to rule out the residual closure partition.

## Completeness and metric specializations

At either endpoint, the partner A corner cannot have colour2, because the
endpoint is required to contain all three colours. Thus the partner side must
be native0(00),1(01),or2(11). Its endpoint order has two possibilities. The
third A copy has two native corners of the required colour and two choices
of incident arm order. This yields3×2×4×4=96 necessary configurations.
A third copy reused at both endpoints is included in this independent-endpoint
superset; allowing independent copies cannot discard a realizable configuration.
Fixing a central orientation loses no reflected tiling, since both partner
orders and third-copy arm orders are retained.

Each configuration imposes the shared-side equality and two ray equalities
at each endpoint. Transitive closure gives26 distinct required partitions,
with4 minimal ancestors. Independently regenerating all203 actual six-side
partitions and every coarsening retains41. Thus every further specialization
of a minimal pattern is accounted for, including coincidence of multiple
length classes. Neither positivity nor joint geometric realization was assumed
for formal partitions; the test is a necessary overapproximation.

The independent checker reconstructs equivalence relations as unordered sets
of blocks, without importing the producer or its certificate. It obtains all
counts above. It checks the settled H2 sufficient criterion under all12 native
cyclic/reflected labellings: corners0,1,3 sum360, side1=side3,side2=side5.
The possible equalities for001122 are
(a0=a2,a1=a4), (a0=a3,a2=a4), (a0=a4,a2=a5).
Forty retained actual partitions meet H2. H2 is used as a sufficient periodic
escape for an actual polygon, not as a complete classification or assertion
that every formal partition is geometrically realizable.

## Residual positive closure is impossible

The unique remaining partition is{0,3},{1,4},{2,5}, i.e. lengths(a,b,c,a,b,c)
with a,b,c>0. Put u=180−x and U=exp(iu) with angles in degrees. Then54<u<72.
Native turn recursion gives directions
(1,U,U^−4,U^−9,−U^−5,U^−1).
Closure groups their coefficients as

    a(1+U^−9)+b(U−U^−5)+c(U^−4+U^−1)=0.

Multiplying by U6/(1+U3) gives coefficient vectors
(2cos3u−1,U4−U,U2). This factor is defined throughout the interval except
u60, equivalent to the excluded x120. Each coefficient has strictly negative
real part: 3u lies in(162,216),2u in(108,144), and
cos4u−cosu=−2sin(5u/2)sin(3u/2)<0 since both sines are positive.
Consequently no strictly positive linear combination vanishes. This is an
exact separating-halfplane proof, independent of sampling or approximate roots.
The endpoint u72 is not silently included, and u60 is not divided through.

## Scope and verification

The proof does not need a complete four-star angle language to analyze an
already-existing two-ended AAA seam. A global theorem must separately show
that every relevant defect-free mixed field supplies such a seam, or a periodic
escape in its absence. The written lemma correctly derives both AAA endpoints from the supplied
complete four-star trivalent palette: neither two-A star contains z. Hence
its hypothesis of a used AA22 seam supplies the local hypothesis reviewed
here. The equivalence to unused native side4 in a nonmonohedral actual field
is sound, even with length aliases; all sides in that supplied field are whole.
No local feasible configuration is promoted to an infinite field here. Once H2 is established, omission of B produces the periodic
escape under the original permissive reflection/partial-contact conventions.

[Independent checker](verify_terra_cross22_luna.py) PASS;
the author's separate certificate checker also PASS. Replay:

```sh
mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_terra_cross22_luna.py
```

Settled H2 sufficiency was imported from
[the reviewed native001122 coverage proof](../lemmas/terra-001122-all-metric-periodic-escape.md),
not re-audited without cause. No extra computational search was undertaken.
