# Changed fractional mechanism: X/Y-dependent triangle heights

Date: 2026-10-14. One bounded second cycle changes the common-triangle
assumption of the two-node rule, preserving the known infinite source.
Verdict: independently hostile-reviewed VALID ([review](../reviews/ammann-mark-altitude-independent-2026-10-14.md)); an exact compatible pentagonal rule
exists, but every unequal X/Y height version requires at least three
output congruence classes. Equal heights return the reviewed periodic escape.
No contact census, whole-source fusion, or quadrilateral fan is reopened.

## Explicit scheme and source-grounded boundary

Use the known infinite legal marked unit thin/thick rhomb source from
[the source proof](../lemmas/ammann-forcing-aperiodicity.md), Lemmas 5 and 7.
The edge marks are read directly from Lemma 5, item 4:

| Counterclockwise source | Edge marks | Arrows |
|---|---|---|
| Thin A,B,C,D | X,X,Y,Y | A→B,C→B,A→D,C→D |
| Thick E,F,G,H | X,Y,Y,X | E→F,F→G,H→G,E→H |

The two triangle edges selected by vertex bipartition are opposite. Hence
each rhomb has one X triangle edge and one Y triangle edge. Across every
source edge one side supplies a triangle, the other a quad. Replace each
X-edge triangle by a unit-base isosceles triangle of physical altitude hX,
and each Y-edge triangle by one of altitude hY. Receiving quads are glued
to triangles with their own edge's mark. Adjacent source rhombs read the
same mark, so the incoming triangle has exactly the required shape.

This specifies the repeatable interface before solving geometry. Unlike
the preceding cycle, X and Y triangles differ. Keep the same two-node
interior tree topology; no source edge directions, arrow rules, or source
frequency hypotheses are changed. The bipartition remains auxiliary data.
The arrow direction is not used by this particular height-only surgery.

## Exact coordinates and finite genuine-pentagon witness

Write a source rhomb A=0,B=1,C=1+c+i s,D=c+i s, where theta is 36 or
72 degrees and c=cos(theta),s=sin(theta). Suppose AB/CD are triangle
edges, respectively X/Y. Choose

    p=1/2+i hX, q=1/2+c+i(s-hY).

The four sectors are ABp, BCqp, CDq, DApq. On each receiving quad's
source edge of mark Z, attach the outside unit-base isosceles triangle of
altitude hZ. The output has five boundary vertices.

The explicit small-height fixture is

    hX=sin(36 degrees)/10, hY=sin(36 degrees)/20.

The producer uses exact Q(sqrt(5)) coordinates scaled by sin(36 degrees).
It checks both source types and both possible opposite-edge role choices:
four local cases total. Every sector passes strict support-line inequalities
against every nonincident vertex; every pair of sectors has an exact
separating supporting axis; their areas sum exactly to the rhomb area.
The sector boundary coordinates are strictly within the rhomb at interior
nodes; convexity of the source then places the entire tree inside it.
Each glued output pentagon passes all strict support inequalities, including
both far endpoints of the removed base. The receiving quad and outside
triangle are interior-disjoint, and their areas add exactly.

These four exact cases establish genuine convex pentagons, not triangles
or quads. Strict inequalities also persist in a small open neighborhood
of this fixture. No claim is made that all positive heights are convex.

Applying the same rule to each source rhomb gives a plane partition, since
the source sectors partition before gluing and each matched source edge
uses exactly one triangle and one quad. This certifies global compatibility
of the fractional rule; it does NOT certify exactly two output classes.

## Analytic area gate for every admissible unequal-height rule

Let delta=hX-hY. The BC quad has area

    s/2 - (hX+hY)/4 + c*delta/2.

The skew term c*delta/2 is essential; unequal-height nodes cannot be
treated as the equal-height tree. For thin source BC is X and DA is Y.
After attaching the marked incoming triangles, its two output areas are

    sin(36)/2 ± (cos(36)+1/2)*delta/2.

For thick source BC is Y and DA is X, giving

    sin(72)/2 ± (cos(72)-1/2)*delta/2.

Selecting the other pair of triangle edges reverses the sign assignments
but leaves each unordered pair unchanged. The four-case producer checks
this independently at the exact unequal-height fixture. Direct shoelace
expansion supplies the displayed formulas for arbitrary heights.

Both coefficients of delta are nonzero: cos(36)>1/2 and cos(72)<1/2.
Therefore delta≠0 makes each source's two output areas distinct. If only
two distinct areas existed over both source types, the two unordered pairs
would have to be equal. Taking pair means would force sin(36)=sin(72),
which is false. Thus at least three distinct areas, and hence at least
three congruence classes, are unavoidable whenever the rule is admissible
and hX≠hY. Both source types occur in the reviewed infinite source; the
argument does not depend on their frequencies or local contact catalogue.
The small exact fixture has four distinct output areas.

If delta=0, the surgery is exactly the preceding two-class common-triangle
rule. Each class then has an explicit homogeneous-rhomb periodic monohedral
carrier, so the target still fails. This exhausts this height-only scheme.

## Bounded experiment, stop, and changed assumption

The bounded experiment is four exact local geometries plus the parameter
area invariant. The stopping condition is more than two area values or an
explicit periodic omission. Unequal heights trigger the first for the full
admissible parameter domain; equal heights trigger the second. The
height-only X/Y variant is closed, with no larger patch run.

The assumption that must change before restarting is a midpoint-based
isosceles triangle interface carrying source information only in altitude.
Changing heights or source depth cannot restore two classes. A later
explicit scheme could change lateral apex offsets or the tree/quad
boundary simultaneously, but it must solve exact receiving-class equality
and global compatibility before any source enumeration. No such later
scheme is claimed or tested here.

Successful global partition and universal decoding remain separate. This
cycle fails the two-shape gate, so no decoder argument is needed or
asserted for its unequal-height outputs. The equal-height decoder
obstruction remains the previous cycle's result.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/ammann-mark-altitude-gate-2026-10-14.py

Frozen certificate: ../certificates/ammann-mark-altitude-gate-2026-10-14.json.
[Independent hostile review](../reviews/ammann-mark-altitude-independent-2026-10-14.md):
VALID. Its fresh symbolic-height checker reconstructs actual marks, both
opposite-edge role choices, all eight strict pentagons at the fixture, and
the full-parameter pair-mean obstruction.
