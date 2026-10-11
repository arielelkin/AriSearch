# Fresh hostile review: internally distinct Cairo edge-to-edge obstruction

Reviewer: `primary_literature`, 2026-10-09. The reviewer did not develop or
modify the proof. Reviewed
[the edge-to-edge theorem](../lemmas/cairo-distinct-side-edge-obstruction.md),
[the author's exact verifier](verify_cairo_distinct_side_ete.py), and
[its finite execution record](../searches/cairo-distinct-side-edge-obstruction.md).
A separate reviewer checker is retained at
[verify_cairo_distinct_side_independent.py](verify_cairo_distinct_side_independent.py).
It does not import author code or use the author's eliminated residuals.

## Exact claim and hypotheses

Each of two convex pentagons has the corner-after-native-side angle word
(90,120,90,120,120) degrees and has five pairwise distinct **internal** side
lengths. The theorem excludes edge-to-edge plane tilings by the two types,
including rotated and reflected copies. It permits arbitrary numerical
cross-type equalities, and does not presuppose that both types occur.

The word edge-to-edge is essential: the theorem does not exclude plane
tilings with partial contacts or right-angle T-junctions. No claim about
periodicity, defect density, or unrestricted aperiodicity follows from it.

## Corner repetition and graph completeness attacks

At an edge-to-edge vertex containing a120-degree corner, the equation
90a+120b=360 with b>=1 has only a=0,b=3. Thus it has three genuine
120-degree sectors. Matching complete native sides labels its three rays
by whole numerical lengths. The labels are distinct: equal labels on two
rays would give the intervening tile adjacent equal side lengths, violating
that tile's internal distinctness.

Consequently its three unordered corner pairs are the three different
edges of a triangle. Two congruent copies using the **same actual corner
slot** cannot create a missing triangle: they would contribute the same
edge twice. More generally, two corners with the same unordered length
pair cannot both occur at this star. This resolves the main potential gap
in identifying the majority corners.

For A=(a,b,c,d,e), the120-degree corner edges are {b,c},{d,e},{e,a}:
an isolated edge plus a two-edge path, with all five labels different.
The same is true for B. Neither graph has a triangle, excluding a
monochromatic120-degree star and therefore an edge-to-edge monohedral
tiling by either member. Both types must occur in a hypothetical tiling.
Every actual120-degree slot of each occurring shape appears in a vertex
star, since each copy has that slot.

A's isolated corner cannot belong to a star with another A corner: a
different A corner has disjoint labels, while a second instance of the
isolated corner would repeat its graph edge. It is therefore the sole A
sector of a star with two B sectors. The B corners must be the two
different path edges, the only B pair sharing a label. Their external
labels match A's isolated pair. Applying the same reasoning to B's
isolated corner gives the other equality. This derives exactly

    {a,d}={B1,B2}, {b,c}={B0,B3}.

The two independent unordered bijections give the four displayed B words.
B's fifth side f may equal e or may be a new numerical length. It cannot
equal a,b,c,d, because those lengths already occupy the other four B
slots and B is internally distinct. No additional cross-type equality is
silently excluded or assumed. Positivity of f is unnecessary for the
contradiction below; the closure obstruction holds even without it.

## Independent exhaustive cross-equality check

The reviewer checker exhausts every equivalence pattern of five A slots
and five internally distinct B slots. Choose k B slots to match an
injectively chosen k-tuple of A labels, and assign private distinct symbols
to the others. This is the complete finite domain

    sum_(k=0)^5 binomial(5,k)*5!/(5-k)! = 1546.

For every pattern it enumerates mixed three-corner multisets **with
replacement**, so duplicate instances of one actual slot are included in
the adversarial domain. It retains a star only when its corner edges
are exactly the three different pairs of three different ray labels.
It then requires every actual120-degree slot of both types to occur in
some allowed star. Exactly8 equivalence patterns survive: the four
claimed B words, each with f=e or with f new. This is a necessary local
coverage check, not an inference that any surviving language tiles globally.
It independently confirms the proof's equality-case completeness.

## Vector closure and reflecting references

With side0 at direction0, the angle word gives successive side directions
0,90,150,240,300 degrees. The five unit vectors are

    (1,0), (0,1), (-w/2,1/2), (-1/2,-w/2), (1/2,-w/2),

where w is the positive square root of3. Their weighted sum is zero
precisely when

    2a=w*c+d-e, 2b=w*(d+e)-c.

These equations use the **corner after** side convention correctly.
Arbitrary rotation only rotates the zero vector equation. Reflecting the
reference changes all direction signs coherently (or reverses their
orientation), giving the same two closure constraints up to an invertible
orthogonal map. The corner graph itself uses unordered pairs. Thus there
is no missing reflected-copy case in either the equality argument or the
algebra.

The author's verifier checks all four residual identities, with factors
2,-4,4,-2 multiplying L=d+e-w*c. Every factor is nonzero. L=0 then
implies a=d and b=c, violating internal distinctness.

The reviewer checker independently constructs the four closure matrices
directly from the five unit direction vectors for A and B, in the six
length variables (a,b,c,d,e,f). In each case the exact4-by6 matrix has
rank4 and a two-dimensional kernel. Both vectors representing a-d and
b-c lie in its row space; equivalently every kernel vector satisfies
a=d and b=c. This proves the contradiction for every exactly closed
length vector without using the author's elimination or residual table.
An extra equality f=e only restricts that kernel further and cannot evade
the contradiction.

## Unrestricted-contact counterexample boundary

The already retained
[three-copy Cairo diagnostic](../counterexamples/cairo-partial-beta-length-graph.md)
shows precisely why native ray-length labeling fails without full-side
matching: three120-degree native corners can meet while one whole
length-q edge matches only the initial length-p segment of its neighbor.
The shorter edge ends at a right corner on the longer edge's interior.
The present theorem explicitly assumes edge-to-edge contact, so that
diagnostic is not a counterexample to it. It does refute any attempted
upgrade of this proof to unrestricted no-tiling.

In particular, the fact that the central120-degree vertex is trivalent
does not establish full matching farther along its rays. The proof uses
the global edge-to-edge hypothesis to obtain that matching and keeps it
throughout. No lower bound on the number, density, or spacing of necessary
right-angle junctions in an unrestricted tiling is established here.

## Reproduction, defects, repairs, and verdict

Freshly executed with assertions enabled:

```text
conda run --no-capture-output -n arisearch python3 research/reviews/verify_cairo_distinct_side_ete.py
conda run --no-capture-output -n arisearch python3 research/reviews/verify_cairo_distinct_side_independent.py
```

Independent result:

```text
PASS independent ETE-only audit: all1546 internally-injective cross-equality patterns; exactly8 beta-covering supports (four words, private side new or equal e); all four direct vector-closure kernels force a=d and b=c.
```

No counterexample or proof defect was found within the stated edge-to-edge
hypotheses. No proof repair was made by the reviewer. All cross-type length
patterns, repeated-corner attempts, and reflected-copy conventions have
been checked. No sampling, approximate arithmetic, bounded global tiling
search, or imported pentagon classification is used. Unrestricted tilings
with partial contacts remain unresolved. No novelty claim is audited.

**Verdict: VALID edge-to-edge obstruction exactly as stated.**
