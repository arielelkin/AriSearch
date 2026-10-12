# Opposite-angle ternary A and a homogeneous endpoint palette force periodic escape

Date: 2026-10-12. Status: [fresh review VALID](../reviews/two-hexagon-ternary-propagation-and-palette-review.md).
This closes one specified ternary metric domain, not the unrestricted problem.

## Statement

Let A,B be fixed genuine strictly convex hexagons with generic angle multisets
A=2x+2y+2z and B=2r+2s+2t, where x+y+z=360,
r=360-2x,s=360-2y,t=360-2z and90<x,y,z<180. Generic has the exact meaning in
[the ternary star/balance lemma](two-hexagon-ternary-angle-star-balance.md):
the only three-angle sums are the five identity types listed there.
Assume A has cyclic native angle word012012, with colours0,1,2 denoting x,y,z.
Assume every actual A side-length class has a fixed unordered multiset of
endpoint angle colours. This includes six distinct A lengths and permits
length coincidences among sides with identical endpoint-colour pairs.
B may have any cyclic order of its two copies of each colour.

If the pair tiles the plane, it admits a periodic tiling. Original partial
contacts, reflections and omission of a type are included. In fact no
connected genuinely mixed defect-free trivalent field exists under these
hypotheses. Its original tiling can have both types; the limit can omit one.

## Reduction and analytic local contradiction

The reviewed [defect-free hexagon limit](hexagon-limit-and-periodicity.md)
supplies an admitted trivalent edge-to-edge tiling. The two propagation gates
in the ternary star/balance lemma show that a connected mixed such field has
only same-colour AAB stars: a B-B edge would force a pure B field, and an AAA
star under the A endpoint-palette hypothesis would force a pure A field.

Take a B cell and number its six corner colours b_k cyclically modulo6.
Its A neighbours are numbered k, with the standard honeycomb slots as in the
reviewed [one-B ring reduction](two-hexagon-one-b-ring-spatial-reduction.md).
Neighbour A_k has colour b_k at slot k+2 and b_(k-1) at slot k+3.
Every placement of native A012012 has period3 and three different colours
in every three consecutive slots. If b_k=b_(k-1), no such A neighbour exists.
Otherwise its colour at slot k+1 is the third colour absent from
{b_k,b_(k-1)}.

Consecutive neighbours A_k,A_(k+1) share an AA seam. At its other endpoint,
A_k contributes its corner at slot k+1 and A_(k+1) its corner at slot k+5.
The latter is the third colour absent from{b_k,b_(k+1)}. That outer vertex is
AAB, so these two colours must agree. With b_k fixed and both adjacent colours
different from it, equality of third colours gives

    b_(k-1)=b_(k+1)  for every k.

Thus the B corner word has period2 and uses at most two colours. This
contradicts the prescribed two copies of EACH of three distinct colours.
No mixed defect-free field exists. If the limit is pure, the admitted
monohedral convex hexagon belongs to a periodically tiling class by the named
unrestricted monohedral theorem imported in hexagon limits. Omission of the
other tile therefore supplies a periodic escape. This proves the statement.

## Exact finite corroboration and scope

The [small checker](../searches/two-hexagon-ternary-opposite-a-colour-rings.py)
and [retained certificate](../certificates/two-hexagon-ternary-opposite-a-colour-rings.json)
independently encode all11 B bracelets of001122 without permuting colours.
A has six distinct placed colour profiles; each ordered adjacent distinct
colour pair selects exactly one. Seven B words have no ring. The four words
010212,012012,012021,012102 each have six rings. All six full-A-profile overlap
relations are empty for every one of these four cases. All24 raw rings,
outer endpoint pairs and first deletion records are retained.
The checker also verifies that each ternary word has native colour fibres
of size at most2. No binary lifting result is needed: no mixed colour field
survives, so a periodic colour backbone is never being mistaken for a metric
witness. The analytical local proof already supplies the infinite obstruction.

Replay without overwriting the retained certificate:

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/searches/two-hexagon-ternary-opposite-a-colour-rings.py /tmp/two-hexagon-ternary-opposite-a-colour-rings-replay.json

Generic excludes extra angle-sum lines. The other ten native A bracelets,
metrics with cross-endpoint-pair length coincidences, and non-generic ternary
angle values remain outside this theorem.
