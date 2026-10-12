# Ternary complementary hexagons: pure stars break the one-B reduction

Date: 2026-10-12. Status: [fresh review VALID](../reviews/two-hexagon-ternary-propagation-and-palette-review.md). This introduces a mechanism outside the completed
unique-B-star and complementary two-angle families. It is not an aperiodic
candidate or an impossibility theorem.

## Exact angle family and generic scope

Let A have two copies of each angle x,y,z, and B two copies of each angle
r=360-2x,s=360-2y,t=360-2z, where x+y+z=360 and90<x,y,z<180.
Both angle multisets sum to720 and all angles are strictly between0 and180.
A generic point means that no three-angle multiset whose equation is not an
identity on this two-dimensional family sums to360. This removes finitely
many proper affine lines, not any identity stars. Six distinct angle values
can additionally be required; that also removes only proper affine lines.
For example x=120+sqrt2,y=120+sqrt3,z=120-sqrt2-sqrt3 degrees satisfies both
requirements: rational independence of1,sqrt2,sqrt3 rules out nonidentities.
This example specifies angles, not a geometrically realized tile pair.

For defect-free trivalent edge-to-edge tilings, the complete generic star
language, at the angle-type level, is

    (x,x,r), (y,y,s), (z,z,t), (x,y,z), (r,s,t).

The final two stars are pure AAA and pure BBB. Therefore the completed
one-B-per-star ring theorem cannot be applied: the B cells need not form its
forced index-three species coset. In particular this family is not obtained
by relabelling the complementary two-angle family.

## Complete identity derivation

Let a_i,b_i count the three A and three B angle types in a triple. Substituting
B_i=360-2A_i and x+y+z=360, the star equation is an identity exactly when

    a_i-2b_i=k for all i,  k+sum_i b_i=1.

Since sum_i(a_i+b_i)=3, put n=sum_i b_i, so k=1-n.
For n=0, all a_i=1: pure AAA. For n=1, a_i=2b_i: one of the three mixed
stars. For n=2, a_i=2b_i-1>=0 would require all three b_i>=1, impossible.
For n=3, all a_i=0 and b_i=1: pure BBB. This is exhaustive.
At native-corner level each angle has two slots. Each mixed type admits three
unordered A-slot pairs with repetition, and two B-slot choices, giving18
mixed native triples. Pure AAA and BBB each have2^3=8 native triples.
There are therefore34 unordered native triples; cyclic star orders remain a
separate placement requirement. This does not assert that every triple is
realized spatially.

## Corner balance and what it fails to force

For any periodic tiling let N_A,N_B be the tile counts on its torus, Y_i the
counts of mixed colour-i stars, U the pure AAA count and V the pure BBB count.
Counting the two corners of each angle per tile gives, for each i,

    2N_A=2Y_i+U,  2N_B=Y_i+V.

Hence Y_i=Y independently of colour and

    U=2N_A-2Y,  V=2N_B-Y,
    0<=Y<=min(N_A,2N_B).

These equations impose no fixed species ratio. They allow Y=0 with either
species omitted, or with both species present. A tiling with every star mixed
has U=V=0 and N_A=2N_B, recovering the old species ratio only under that extra
hypothesis. More generally the same equations hold for invariant-mean corner
counts when the existing averaging theorem applies; no empirical density is
assumed. Local finite-window counting instead has boundary-error terms.
Positive angle balance alone neither proves plane tilability nor excludes it.

## Spatial gate: a B-B edge propagates to a pure B field

In a connected defect-free hexagon cell field, any B-B edge forces every cell
to be B. Around a B cell, consecutive neighbours participate with its centre
in a trivalent star. The generic star language contains no ABB star, so those
neighbours cannot have different species. If any neighbour is B, the whole
cyclic neighbour list is B. Apply the same conclusion at every such neighbour,
and connectedness propagates it to the entire field.

Consequently every genuinely mixed field has no B-B edge and no pure BBB
star. Each B is isolated with six A neighbours, but its locations need not
form the old index-three coset: pure AAA stars are allowed. For periodic mixed
fields the previous equations therefore sharpen to

    V=0, Y=2N_B, U=2N_A-4N_B, N_A>=2N_B.

The corner-balance cone allowing both V>0 and N_A>0 is locally unrealizable;
its failure shows why balance must precede rather than replace spatial gates.
A pure B field or pure A field, if geometrically realized, gives a monohedral
plane tiling and therefore a periodic escape by the existing [monohedral
convex-hexagon theorem](hexagon-limit-and-periodicity.md). The unresolved mechanism is the genuinely mixed
isolated-B field with possible AAA holes. Equal species balance would remove
all AAA holes only at N_A=2N_B; no such equality has been proved in general.

## Metric gate: fixed endpoint-pair classes remove AAA holes

Suppose every actual A side-length class has one fixed unordered pair of
endpoint angle colours. In particular this holds if all six A sides have
distinct lengths; it also permits repeated lengths among sides with the same
endpoint pair. Along an AA seam the two matched native sides then have the
same unordered endpoint-colour multiset. Their A colours at one endpoint
agree if and only if they agree at the other endpoint. This follows by the
two possible bijections of equal two-element multisets; repeated-colour pairs
make both endpoints agree automatically.

At a mixed AAB vertex the two A colours agree; at a pure AAA vertex they are
different. Therefore an AA seam joins two mixed vertices or two pure AAA
vertices. Every edge incident to a pure AAA vertex is AA, so propagation along
the connected edge graph makes every vertex AAA. It follows that a genuinely
mixed field on this metric locus has no AAA star. The preceding B-B gate
already removed BBB stars. Thus every star is AAB, and the reviewed exact
one-B species-coset reduction applies again.

This does not discharge that new one-B family: each native B corner still
allows three A-slot pairs, and the three colour types replace the former two
colour types. It does establish a necessary feature for a genuinely mixed
field with AAA holes: at least one A length coincidence must join sides with
different unordered endpoint-colour pairs. Such a coincidence can now be
screened against exact polygon closure before spatial enumeration. A pure
field still gives the monohedral periodic escape. The argument concerns a
connected defect-free field supplied by the reviewed hexagon limit theorem;
it does not assume the original admitted tiling is edge-to-edge.

## Cheap periodic escapes before any enumeration

There are11 native bracelets of the multiset001122 under geometric dihedral
symmetry without permuting the three angle names:

    001122,001212,001221,002112,010122,010212,
    011022,011202,012012,012021,012102.

The bracelet012012 has opposite equal angles. If its actual opposite side
lengths also agree, the polygon is centrally symmetric. Indeed its first
three exterior turns sum to180, so opposite edge directions are opposite;
equal opposite lengths make the corresponding boundary vectors negatives.
The half-turn pairs opposite vertices. Every convex centrally symmetric
hexagon tiles periodically by translations, as in the standard reviewed
[monohedral hexagon result](new-angle-two-equilateral-hexagons.md). Because omission is allowed, either such A or such
B immediately kills the pair as an aperiodic candidate, independently of the
other tile. This is a metric-locus escape, not an all-metric claim for012012.
Actual convex examples exist for every admitted angle triple: choose the
three edge vectors in cyclic order with prescribed exterior turns, then their
negatives, all with length1. Consecutive exterior turns lie strictly between0
and180 and total360, so the resulting closed polygon is strictly convex.

The exact small checker below retains the five symbolic triples,34 native
triples and11 bracelets. No spatial state enumeration is justified yet.
Concrete next gate: screen cross-endpoint A length coincidences by exact
closure; for the remaining mixed-only fields derive a local metric identity
or an explicit small periodic carrier. The global existence and nonperiodicity
obligations remain entirely open.

Supporting checker:
[ternary exact star ledger](../searches/two-hexagon-ternary-angle-star-ledger.py).
