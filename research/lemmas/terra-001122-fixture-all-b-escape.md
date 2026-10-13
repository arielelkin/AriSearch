# Superseded duplicate fixed-fixture extraction

This parallel extraction has the same mathematical scope as the canonical
[reviewed fixed-fixture lemma](terra-001122-fixed-fixture-periodic-escape.md).
Use that canonical artifact for dependencies. The original extraction below
is retained as provenance; it is not a second independent mathematical result.

# The exact nonmonohedral AAA fixture nevertheless forces a periodic B escape

Date: 2026-10-13. Status: proved internally with separate exact checker;
independent hostile review pending. Fixed-angle/fixed-A result only.

## Statement

Take the exact actual A001122 with angles(113,113,121,121,126,126), positive
sideword(a,a,b,b,c,c) and cyclotomic coordinates defined in
[the AAA counterexample](../counterexamples/terra-generic-aaa-does-not-force-monohedral.md).
Let B be any actual convex hexagon with two copies of each complementary
angle(134,118,108), in arbitrary native order and arbitrary side metric.
If the pair tiles, it admits a periodic tiling, including reflections, original
partial contacts, and omission of either species. This is not an all-angle
A001122 theorem and does not infer mixed infinite existence.

## Necessary neighbourhood before exact closure

The generic five-star language and reviewed defect-free-limit theorem apply.
In a connected genuinely mixed defect-free field no B-B edge or BBB star can
occur, by the reviewed no-ABB propagation gate. Every B vertex is AAB with
two A corners of the same colour. AAA elsewhere is allowed and not removed.

A corner arms by colour are

    colour0:(c,a),(a,a), colour1:(a,b),(b,b), colour2:(b,c),(c,c).

Match either arm of either native A corner to either arm of a same-colour A
corner, allowing reflections. The necessary ordered B arm pairs are exactly

    colour0:aa,cc,ac,ca;
    colour1:aa,bb,ab,ba;
    colour2:bb,cc,bc,cb.

An AB edge has at each endpoint the same A colour as its B colour, because
that vertex is a same-colour AAB star. Native A endpoint-palette classes are

    a:00 or01, b:11 or12, c:22 or02.

These six unordered endpoint-colour pairs are distinct. Consequently each
native B edge has exactly one necessary length: its endpoint pair selects a,
b or c. Every B bracelet thereby determines one side word, rather than3^6
independent assignments. All11 required words pass the B fan-pair necessity;
this alone is not a whole compatible ring or extension theorem.

## Exact eleven-word closure gate

The finite domain is all11 bracelets of001122 under cyclic rotation and
reflection, without permuting angle names. For each, assign its uniquely
forced sides, derive unit edge directions from exterior angles, and compute
its closure residue in CyclotomicField360 using the exact a,b,c definitions.
The [certificate](../certificates/terra-001122-b-neighbourhood.json) retains
all nativewords, necessarysides, directions and exact nonzero residue
polynomials. Ten residues are nonzero. The only closed necessary B is

    nativeword012012, sideword(a,b,c,a,b,c).

The checker also proves strict positivity and every strict supporting-halfplane
inequality of this B. Its equal opposite angles and lengths make it centrally
symmetric, so it has a monohedral periodic translation tiling. Omission of A
therefore gives a periodic admitted tiling, regardless of whether a mixed
field using this B actually extends infinitely.

If a defect-free limit is pure B instead, the imported unrestricted monohedral
convex-hexagon theorem gives a periodic escape. A pure A field is excluded by
the exact failure of all Reinhardt monohedral criteria in the counterexample.
This exhausts the cases supplied by any original tiling and proves the claim.

## Evidence, scope and next obligation

[Producer](../searches/terra-001122-b-neighbourhood.py),
[separate no-import checker](../reviews/verify_terra_001122_b_neighbourhood.py).
Replay is nondestructive:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_terra_001122_b_neighbourhood.py

The query exhausted11 exact necessary fixed-metric closure cases. No bounded
patch/torus search, timeout, random seed or numerical acceptance was used.
The preceding same-colour-fan and endpoint-palette arguments explain why this
small domain contains every possible B in a genuinely mixed defect-free field
for THIS exact A. Arbitrary actual B metrics were eliminated by necessity
before computation; arbitrary A angles and metrics were not classified.

The next justified extension is symbolic A001122 closure with three paired
side lengths, followed by analytic factor/sign classification of the ten B
closure residues over its admitted angle domain. More angle samples or larger
mixed patches would not prove that coverage and are not authorized by this
artifact. The nonmonohedralAAA counterexample remains valid; the fixture pair
family now has a different B-closure/omission mechanism.
