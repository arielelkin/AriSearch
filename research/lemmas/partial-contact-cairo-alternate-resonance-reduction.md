# Alternate four-shared-arm Cairo pairs reduce to two exact ratios

**Status:** independently hostile-reviewed **VALID** with a no-solver,
no-producer-import exact checker; see [fresh review](../reviews/partial-contact-cairo-alternate-resonance-review.md). This is an unrestricted necessary-condition theorem
for one exact two-parameter metric family, not the main two-tile result.

## Family and statement

Let w=sqrt3 with1<w<2. Choose a>0 and set b=ka. Define

    c=((3+w)a+(1-w)b)/4,
    d=((3-w)a+(1+w)b)/4,
    e=(w-1)(a+b)/2,
    f=((w-5)a+(1+3w)b)/4.

Let P have ordered native lengths(a,b,c,d,e), and Q have ordered native
lengths(a,d,b,c,f). Both have side directions0,90,150,240,300degrees and
angles after successive native sides(90,120,90,120,120). The positive
metric cone is exactly

    (5-w)/(1+3w) < k < 3+2w.

Assume k!=1. All four arm values a,b,c,d are then distinct; e and f may
coincide with arms. The pair comprises distinct congruence classes because
its side-length multisets differ by e!=f. Its exact native coordinates
for a word(A,B,C,D,E) are

    (0,0), (A,0), (A,B),
    (A-wC/2,B+C/2), (-E/2,wE/2).

**Theorem.** If this pair tiles the plane under unrestricted contacts and
all isometries, its ratio k belongs to

    { w, 1+4w/3 }.

No existence or periodicity conclusion is asserted at these two remaining
ratios. The certificate-weight exclusions below and the generic argument
exclude all other positive ratios except k=1, where arm distinctness fails.

## Closure and exact finite resonance domain

P closure says b-c=w(d-a), e=wc+d-2a. Q closure says
d-b=w(c-a), f=wb+c-2a. Solving gives the displayed family. Positivity
of f and c gives the two endpoints of the cone; d,e are automatically
positive there. The native side directions turn once around the circle
with positive exterior turns, so positive closed words are genuine strictly
convex polygons. The exact domain checker also verifies all supporting
incidences for each retained resonant shape.

Differences among a,b,c,d are nonzero multiples of k-1. For k>1 their
order is c<a<d<b; for k<1 the order reverses. Also

    f-e=(3+w)(b-a)/4.

The right-corner pair graph is the four-cycle with P pairs{a,b},{c,d}
and Q pairs{a,d},{b,c}. The native right-corner event list consists of
self-bank sums2a,2b,2c,2d and cross-bank sums a+c,b+d. This is the
complete list from the eight oriented right-corner slots; identical slots
from different occurrences are allowed.

Every sum is affine linear in k after setting a=1. All six equal2 at k=1
and their slopes are pairwise distinct. Thus all six sums are distinct
whenever k!=1. The two-T switch invariant in
[partial-contact-cairo-two-t-switch.md](partial-contact-cairo-two-t-switch.md)
then restricts unequal native arm-ray matches to the two components

    {a,c}, {b,d}.

Exhausting all twelve equalities between e/f and these six bank sums gives
exactly six roots in the positive cone other than1:

| Ratio k | Unique host equality | Complete endpoint-marginal result |
|---|---|---|
| (28w+13)/37 | f=2c | Infeasible; exact rational dual retained |
| w | f=a+c | Feasible; not a tiling witness |
| (20w-11)/13 | f=2a | Feasible; not a tiling witness |
| 1+w | e=2c | Feasible; not a tiling witness |
| 1+4w/3 | e=a+c | Feasible; not a tiling witness |
| 1+2w | e=2a | Infeasible; exact rational dual retained |

The pairwise event-sum and host-root comparisons are exact computations in
Q(w), not sampled ratios or numerical coincidences. The full root-domain
certificate records all comparisons, including roots outside the cone.

## Generic unrestricted obstruction

Outside the six roots, neither e nor f can host a T, since such a host's
length must equal its two right-corner event bank lengths. An unsubdivided
native120-to120 side must whole-match another120-to120 side. Since e!=f,
each Q f side is therefore a whole same-species f seam.

At either endpoint the two Q copies each expose an a or c arm. The third
120 tile cannot expose an e/f side on an arm ray: a whole e/arm match
would identify90 with120, while a longer e counterpart would have to host
a T, excluded here. It must consequently have two arm rays in the component
{a,c}. Both incident arms at a120 corner force the isolated120 corner.
P's isolated pair is{b,c}, while Q's is{d,b}; neither lies wholly in
{a,c}. This contradiction eliminates Q. If only P occurs, its four arms
are internally distinct and the reviewed private-arm Cairo untileability
proof applies. Thus no tiling exists outside the six ratios.

This step needs **both** e and f to avoid event sums. A T-hosted e/f side
at a resonant ratio can complete a whole-seam endpoint and is not silently
discarded in the following finite models.

## Complete augmented contact domain at each resonance

All six roots satisfy k>1, so c<a<d<b. An arm T is the long-arm endpoint
switch derived in the two-T lemma. The only possible unequal pairs are
(c,a) and(d,b); hence only native a,b can be subdivided. A subdivided a
has its T at distance c from its120 endpoint, giving pieces c and a-c.
A subdivided b has its T at distance d from its120 endpoint, giving
pieces d and b-d. The pieces appear in the appropriate reversed order
when the native side runs90-to120. The c,d sides stay whole.

The unique resonant e/f side may be either whole or T-hosted **for each
individual occurrence**. No argument forces every resonant side to host
a T. A hosted side has bank pieces(c,c), (a,a), or(a,c)/(c,a) according
to the equality. The nonresonant e/f side remains whole. Thus the complete
finite list consists of all four independent a/b subdivision flags for
each native species, with every whole/hosted choice and both orders when
banks differ. Doubled-bank strata have12 augmented variants; mixed-bank
strata have16. Actual polygon shapes are not marked: these are bookkeeping
states of actual contacts admitted by the two original unmarked shapes.

Each native subdivision contributes a straight180 corner. Every actual
augmented star is120^3,90^4, or180+90+90. Two180 corners alone are excluded
because no native corner would be present. A numerical ray symbol records
its whole shared piece length and how many of its endpoints are120
corners. A120 corner cannot meet90 or180, so both sides of an actual piece
have the same endpoint count. This keeps an e side distinct from an equal
numerical arm value when their endpoint roles differ.

An augmented corner kind consists of its angle and unordered pair of
incident ray symbols. Reflection is allowed. A multiset of corner kinds
can form a ray-matched cyclic star only if the multigraph whose edges are
those incident-symbol pairs has a connected Eulerian circuit, counting
loops twice toward degrees. Enumerating all3- and4-corner multisets with
angle sum360 and this circuit condition gives a necessary **superset**
of actual stars. It is not asserted that all retained stars or their
finite configurations extend.

## Exact weighted boundary exclusions at f=2c and e=2a

For every augmented variant s record its corner-kind multiplicity vector
m_s. For each legal numerical star t record its corner-kind vector m_t.
The finite normalized necessary count system is

    sum_t m_t x_t = sum_s m_s F_s,
    x_t>=0, F_s>=0, sum_s F_s=1.

For f=2c its complete domain has12 variants,23 corner kinds and59 stars.
For e=2a it has12 variants,24 corner kinds and61 stars. Each retained
rational dual w satisfies

    w dot m_t >= 0 for every star,
    w dot m_s <= -1 for every augmented variant.

These are exact finite certificates requiring no trust in Z3. They apply
to whole and hosted occurrences, species omission, and every reflection.

To obtain an infinite-plane contradiction, select native tiles whose
interiors meet int Q_R and assign each its actual augmented contact variant.
Their total weighted corner charge is at most-N. All complete interior
stars have nonnegative charge. Every incomplete star touches a selected
tile meeting partial Q_R: otherwise its missing tile has interior inside
the square and would have been selected. Selected boundary tiles lie in
a fixed-diameter strip with O(R) area; minimum tile area and disjoint
interiors bound them by O(R). The variant list has a uniform finite number
of corners and its rational weights are bounded. Thus the incomplete-star
charge is at least-O(R), implying N<=O(R). Coverage requires
N>=4R^2/Amax, contradiction. No frequencies, periods, densities of both
types, or lattice hypotheses are assumed. This excludes these two
resonances. Two further exclusions use the separate reviewed two-ended seam
theorems linked below.

## Reproduction and remaining gaps

[Complete domain producer](../searches/partial-contact-cairo-alternate-resonances.py),
[domain certificate](../certificates/partial-contact-cairo-alternate-resonances.json),
[complete endpoint-marginal producer](../searches/partial-contact-cairo-alternate-endpoint-marginals.py),
and its six certificates named
`research/certificates/partial-contact-cairo-alternate-<ratio>-endpoint-marginals.json`.
Exact ratio names are f2c,fac,f2a,e2c,eac,e2a in the table order.

Normal replay is read-only:

    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-alternate-resonances.py
    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-alternate-endpoint-marginals.py

Explicit --output/--output-dir writes retain certificates. Every system
retains a rational primal or dual. The [independent checker](../reviews/verify_cairo_alternate_endpoint_marginals_independent.py)
reconstructs every augmented variant and circular star, and verifies all
rational primals and duals without a solver.
No timeout, randomized search, bounded period assumption or floating-point
proof decision enters the theorem.

The simpler complete endpoint marginals leave four ratios. The freshly
reviewed [two-ended f2a seam obstruction](partial-contact-cairo-alternate-f2a-seam-obstruction.md)
excludes (20w-11)/13 using an actual-slot seam potential, reducing the
initial four-ratio necessary set to three. Its independent no-solver
reconstruction and infinite boundary proof are separate dependencies.

The freshly reviewed [e2c seam obstruction](partial-contact-cairo-alternate-e2c-seam-obstruction.md)
also excludes1+w, with separate independent domain reconstruction.

The two surviving ratios remain exact candidates, not established tilers.
Their feasible necessary marginals do not provide existence. Restricted
four-face quotient searches found no witnesses; their finite failures do
not prove nonexistence of larger periodic quotients or plane tilings.
The earlier angle-marginal producer that forced every resonant side to
host a T is only a conditional experiment, superseded for theorem purposes
by the complete whole-or-hosted endpoint model above.


The later independently verified [complete alternate-family classification](partial-contact-cairo-alternate-classification.md)
settles every remaining ratio described above: all except1+4sqrt3/3 are
untileable, and that ratio has a periodic tiling. Earlier remaining-gap
phrasing records this intermediate theorem's original scope.
