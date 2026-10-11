# Fresh hostile review: the complete U/V area family has no ETE tiling

**Verdict: VALID without repair.** This applies to every positive real b,c,
all rotations and reflections, and omission of either tile type. It excludes
edge-to-edge plane tilings only. It does not exclude partial contacts or give
a mixed plane tiling. No monohedral classification is used in this result.

Reviewed [the analytic proof](../lemmas/pentagrid-area-family-edge-obstruction.md)
independently of its producer. The reviewer developed the earlier different
two-length fixture obstruction, but did not develop this general b,c theorem.
The check below derives the native corner table again from side/angle incidence
and uses a different enumeration: angle-compatible multisets followed by
explicit circular endpoint-length assignments. It imports no author code.

## Metric reduction and the full-star condition

For A=phi^2 b+phi c, D=2phi b+phi^2 c and E=phi(b+c), direct simplification
using phi^2=phi+1 gives

    D-A=(phi-1)b+c, A-E=b,
    E-b=(phi-1)b+phi c, E-c=phi b+(phi-1)c.

All are strictly positive for b,c>0 and phi>1. Thus D>A>E>max(b,c),
and b=c is the only remaining possible coincidence. No assumption of
algebraicity, rational independence of b,c, or generic metric is needed.

Using angles after sides, the genuine corner classes are exactly

    U36: A/A, U108: A/b, U144: b/c,
    V72: b/D, V144: b/E, V108: E/E,

with weights1,3,4,2,4,3 respectively. A full vertex in an edge-to-edge
tiling consists only of genuine native tile corners: a tile side interior
containing another native vertex would be a partial contact. The surrounding
sector angles sum to10 units pi/5, and whole-side matching forces successive
length labels to agree. Native-angle minima bound the number of sectors by10.
Reflections reverse corner traversal; the graph and independent check allow
both traversal directions. These facts justify the complete closed-walk
necessary condition without an assumed valence or orientation restriction.

## Independent enumeration

[The independent checker](verify_pentagrid_area_family_edge_obstruction.py)
first lists all55 nonnegative integer corner multisets of total angle10.
For each of the two length cases, it attempts every circular ordering and
every relevant native-corner traversal direction by backtracking. Fixing the
first occupied corner class loses no circle: every candidate circle can be
rotated to put that class first. It then checks every endpoint match including
the last-to-first closure. The search allows arbitrarily many tile copies;
native multiplicities on one tile are not mistaken for a bound on a full star.

The complete feasible signatures in class order
(U36,U108,U144,V72,V144,V108) are

    b!=c: (10,0,0,0,0,0), (4,2,0,0,0,0), (0,2,0,2,0,0);
    b=c:  the preceding three, plus (0,2,1,0,0,0).

The retained [review certificate](../certificates/pentagrid-area-family-edge-review.json)
gives actual circular links for every signature and exact independent
coefficient checks for the strict length order. These signatures agree with
the author's certificate, inspected only after running the independent
enumeration. The author's11/14 rooted walks are also consistent: there is
one all-U36 walk; the four-U36/two-U108 signature gives five walks starting
at A and one at b; the two-U108/two-V72 signature gives one at A, one at D
and two at b. At b=c the additional star gives one at A and two at b.

Every feasible full star lacks V144. In the b!=c case every feasible star
also lacks U144. In the b=c case the only star containing U144 is one U144
plus two U108. These are necessary length-linked stars, not claimed realizable
large patches, which is sufficient for the exclusions below.

## The analytic exclusion survives the hostile checks

The b--E bridge must occur an even positive number of times in any closed
walk containing V144. Weight10 allows only two traversals, costing8.
The remaining weight2 cannot be an E-loop of weight3. A nonempty b-to-b
excursion costs at least4 (two V72, or the U144 loop at b=c), while accessing
A and returning costs6. A's weight1 loop cannot be used without that access
cost. Thus the proposed V144 star is impossible. Every actual V tile has
two V144 vertices, so V cannot occur anywhere in an ETE tiling. This is a
pointwise exclusion, requiring no density or frequency argument.

With V absent and b!=c, the U144 bridge similarly requires8 units and has
no available residual weight2. Every U tile has U144 vertices, so this case
has no tiles at all.

With V absent and b=c, each U144 vertex is forced to meet two U108 corners.
U's side3 (numbered from0) has two144 endpoints. Its unique whole-side
neighbor must contribute108 at each endpoint because those are the only
remaining sectors in the forced stars. The U side endpoint pairs are

    (108,36), (36,108), (108,144), (144,144), (144,108).

There is no side with two108 endpoints, in either orientation or reflection.
The required neighbor cannot exist. The argument uses the same neighboring
tile across the whole side, justified by the ETE assumption. It would fail
with partial neighbors and is correctly not applied to that domain.

## Scope and replay

    conda run --no-capture-output -n arisearch python research/reviews/verify_pentagrid_area_family_edge_obstruction.py

Replay completed successfully, with55 multisets checked in each case and
3/4 surviving signatures. Ordinary invocation prints JSON nondestructively;
artifact writing requires an explicit --output.

The final pentagons must use partial contacts in any plane tiling. An underlying
ETE source triangulation may still produce partial pentagon boundaries after
regrouping its triangles, so this proof does not exclude triangle recomposition.
The positive geometry and area ratio of the family are separate hypotheses;
this review establishes no source markings, substitution, global extension,
periodicity or aperiodicity.
