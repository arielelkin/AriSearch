# Mixed QQ heptagons: two parameter-wide closure obstructions

Date: 2026-10-19. Status: proved internally; independent hostile review pending.
The four remaining mixed words are blocked. No plane existence, periodicity,
or aperiodicity claim is made for those four.

## Scope

Let P be a regular unit pentagon and Q any fixed strictly convex heptagon
whose angles are A=144 degrees, B=alpha, C=252−alpha, with
108<alpha<126 degrees. Of the six balanced rooted reversal words whose
forced QQ sides have types BB, CC, BC, **ABBBCCC and ABBCBCC cannot tile
together with P**, with arbitrary metrics, rotations, reflections and
unrestricted contacts. This extends their earlier fixed-alpha124 metric
failures to the entire open parameter interval, including alpha120.
The four remaining mixed words are ABBCCBC, ABBCCCB, ABCBBCC, ACBBBCC.

Dependencies: the reviewed complementary-angle necessary theorem
`research/lemmas/complementary-angle-flow-necessary-theorem-2026-10-19.md`,
and the balanced-defect purification argument in
`research/searches/heptagon-all-bc-qdimer-sol-2026-10-19.md`.
The proof below supplies the needed purification reasoning explicitly.

## Exhaustion of the six mixed classes and indexing convention

Root each cyclic Q word at its unique A corner, numbered vertex0, and
write the following six B/C corners as vertices1 through6. Side i joins
vertex i to vertex i+1 modulo7. Reversal of the rooted word reverses
that six-letter string. There are binomial(6,3)=20 rooted balanced strings.
None is reversal-fixed: a reversal-fixed even string has even counts of
each letter, whereas both counts here are three. Thus there are exactly
ten rooted reversal classes, as in the reviewed necessary theorem.
The unique perfect matching on the six non-A vertices is
(1,2),(3,4),(5,6). The three corresponding QQ side types either are all
BC/CB or comprise one BB, one CC, one BC/CB: equality of total B and C
counts proves this dichotomy. The all-BC case has 2^3=8 ordered strings,
or four reversal classes. The other twelve strings give exactly six
mixed classes, represented by ABBBCCC, ABBCBCC, ABBCCBC, ABBCCCB,
ABCBBCC, ACBBBCC. All representatives are distinct under reversal;
together they exhaust the six classes. The two excluded representatives
are therefore exactly two of the six mixed classes.

## Necessary intrinsic metric conditions, including resonance

In any tiling the angle theorem forces full-edge trivalent contacts.
Away from alpha120 the only stars are PPA and PBC. Thus sides 0,2,4,6
of Q face P and have length one; sides 1,3,5 face Q. Their types are the
consecutive pairs of non-A corners (1,2), (3,4), (5,6). At a QQ endpoint,
B must meet C, independently of reflection parity. Consequently a BB side
can only meet a CC side, and their intrinsic lengths are equal, say x>0.
Write z>0 for the length of the remaining BC or CB side.

At alpha120 the extra BBB vertices need not be absent in the original
tiling. However the balanced B/C square-window count gives O(R) such
vertices in a square of side R. A defective Q has at least one such vertex,
so there are also O(R) defective Q copies. For each fixed r, the union of
radius-r neighborhoods of those copies has area O_r(R). It cannot cover
a square with area of order R squared. There are therefore defect-free
disks of arbitrarily large radius. Translate their centers to the origin
and pass to a locally convergent subsequence of tilings by the same fixed
compact polygons. Local compactness follows from positive minimum tile
area, bounded diameter, and compactness of rigid motions meeting a fixed
window. No BBB vertex survives in the limit. Q cannot be omitted because
regular pentagons alone have no allowed vertex stars. In this purified
tiling the preceding unit-side and equal-BB/CC conclusions hold. They are
intrinsic facts about the original fixed Q metric. Thus the closure
obstruction applies to the original tile pair even when its hypothetical
original tiling had sparse resonant defects.

## Exact closure obstruction

Angles in this section are in degrees. Put d=126−alpha, so 0<d<18,
and let e(theta)=(cos(theta),sin(theta)). Orient side0 of Q with heading
zero. The side headings obtained by adding exterior turns are:

| word | headings of sides 0 through 6 |
|---|---|
| ABBBCCC | 0,54+d,108+2d,162+3d,216+2d,270+d,324 |
| ABBCBCC | 0,54+d,108+2d,162+d,216+2d,270+d,324 |

For both words the unit public-side sum is

S=e(0)+e(108+2d)+e(216+2d)+e(324)
 =2 cos18 e(−18)+2 cos54 e(162+2d).

The BB and CC sides are sides1 and5, with common length x. Their unit
direction sum is

V=e(54+d)+e(270+d)=2 cos108 e(162+d).

Put U=e(162+d), and define cross(u,v)=u_x v_y−u_y v_x. Then

cross(U,V)=0,
cross(U,S)=2(cos18+cos54) sin d>0.

For ABBCBCC the BC/CB side3 has direction U. Closure would require
S+xV+zU=0, whose cross product with U gives cross(U,S)=0, a
contradiction. This is inconsistency of closure irrespective of positivity.

For ABBBCCC the BC side3 has direction e(162+3d). Closure instead gives

0=cross(U,S)+z sin(2d),

and hence

z=−(cos18+cos54)/cos d<0.

The divisions are valid because 0<d<18 implies sin d>0 and cos d>0.
This contradicts a positive polygon side. Thus neither word admits a
plane tiling with P. Reflection of Q conjugates all vectors and changes
cross-product signs consistently, leaving both contradictions intact.

## Exact replay

The adjacent Sage script checks all four vector identities as exact
Laurent-polynomial identities in t over CyclotomicField(20), with
w=exp(i*pi/10) and t formally representing exp(i*d). It performs no angle
sampling, metric enumeration, quotient search, or numerical sign test.
The strict signs are the elementary interval inequalities written above.

```
mise exec -- conda run --no-capture-output -n arisearch sage research/searches/heptagon-mixed-qq-mechanism-sol-2026-10-19.sage
```

## Global mechanism attempted and stopping state

For every remaining mixed word, deleting the BC/CB seams from the QQ
adjacency graph gives a directed degree-(1,1) graph: direct each BB-to-CC
seam from the tile supplying BB to the tile supplying CC. Each component
is a directed cycle or doubly infinite directed strand; the remaining
BC/CB seams give a perfect matching on the Q copies. Distinct physical
Q copies cannot share two full sides because their strictly convex
interiors would then overlap, so these incidence statements have their
usual geometric meaning. This is an exact combinatorial consequence,
but it is not an embedded-axis, monotonicity, or translation invariant.

The obstruction to promoting it is explicit: each BB/CC contact permits
both endpoint assignments under allowed reflections. Their compositions
can have different rotational holonomies. Degree-(1,1) alone controls
neither the sequence of reflection choices nor transverse matching of
strands by BC seams. The earlier fixed-alpha124 strand atlas already
found both parities locally feasible. No new argument here eliminates
one parity or makes successive holonomies commute. Therefore it would
be unjustified to assert periodic strands, parallel axes, a finite
quotient property, or plane existence for the four surviving words.

**Blocked under protocol section5:** the missing statement is a global
extension/return theorem or contradiction for the four remaining fixed
metrics at arbitrary alpha, with all reflection sequences included.
The BB/CC equal-length condition fixes their metric through two planar
closure equations when the resulting two direction columns are
independent, but metric uniqueness does not imply plane extension.
No larger torus, patch search, or alpha grid was run. Reopening requires
a new parity/holonomy restriction derived from the BC matching or an
explicit universal flat carrier. The two excluded words require no
further search. This artifact makes no novelty claim and does not solve
the unrestricted two-convex-polygon problem.
