# Fresh hostile review of the regular-dodecagon classification

**Verdict: valid.** The general necessity proof, full strict parameter
domain, and periodic construction for every admitted parameter pass
fresh adversarial review. The independent fixture and universal-gluing
checker also pass. This is a restricted regular-polygon classification,
not a resolution of the unrestricted main research problem.

The reviewer did not develop the n=12 theorem, parameter family, or
seven-motif witness. The artifacts reviewed are the
[classification lemma](../lemmas/all-obtuse-pentagon-regular-dodecagon-classification.md),
[producer](../searches/obtuse_pentagon_regular_dodecagon_witness.py), and
[certificate](../certificates/obtuse-pentagon-regular-dodecagon-witness.json).
The new checker is
[verify_regular_dodecagon_independent.py](verify_regular_dodecagon_independent.py).
It imports no author module, uses separating axes instead of clipping,
and independently reconstructs the complete abstract side/corner gluing.

## Necessity and the saturation step

Strict obtuseness gives full native contacts and trivalence by the explicit
reviewed forcing dependency. For n>=8, two regular-Q sectors would leave
at most90 degrees, incompatible with a P corner. Three Q sectors also
fail the angle sum. Thus there are no QQ sides, every Q side meets P,
and Q-neighbor slots on a P are nonadjacent. A five-cycle has at most
two such slots.

Uniform corner and angle window counts give N_P=(n-6)N_Q+O(R), with
quadratic counts of both types. Counting PQ contacts then forces
nN_Q<=2N_P+O(R), so n>=12. This excludes8<=n<=11 independently of
P's angle word and lengths. It also excludes omitted and subquadratic
types; boundary errors cannot account for a quadratic contact deficit.

For n=12, d(P)=2 minus its Q-neighbor count is nonnegative pointwise.
The total is2N_P-12N_Q+O(R)=O(R). Consequently bad centroids have
uniformly linear counts and arbitrarily large translated disks contain
none. The positive-area/O(2) local compactness argument applies to the
fixed original shapes. Full-side neighbors and native stars persist by
the uniform separation of vertices in a strictly obtuse tiling, as
proved in the already reviewed heptagon argument. All neighboring
centroids of a selected bounded tile lie in the growing good disk.
The admitted limit therefore has exactly two nonadjacent Q sides on
every P. The proof correctly confines this pointwise conclusion to
the limit, rather than asserting it for the original tiling.

## Forced angle and metric words

Every QPP star has complementary P angles summing to210 degrees.
Each is strictly below120 because the other is strictly above90.
With exactly two nonadjacent Q sides, a P has four QPP corners and
one PPP corner. It therefore has at most one angle at least120. If all
five were below120, no PPP star could exist. Hence there is exactly
one large angle, and it is the PPP corner on every copy. The three
PPP sectors are copies of that same angle, forcing it to equal120.

Labeling that corner0 leaves only native sides1,2,3 eligible for Q
neighbors. The two nonadjacent slots are necessarily1 and3, hence
both have unit length. The remaining sides0,2,4 meet P. Side2 has
two small-angle endpoints and cannot match sides0 or4: a120-degree
endpoint plus a strictly obtuse small P endpoint and Q150 would exceed
360 degrees. It cannot match1 or3 because those are already Q contacts.
Thus side2 matches side2. Reversed endpoint correspondence gives b+d=210;
preserved correspondence gives b=d=105, which also has this sum.
The P angle sum then gives a+e=210. This argument includes reflected
placements and accidental equal side lengths.

The lengths at the120-degree corner are equal. If ell0 and ell4 differ,
whole-side matching forces the three rays at a PPP star to carry those
two distinct numerical labels. Each of its three sectors supplies one
of each label. This would alternate two labels around an odd cycle.
Reflection may interchange the native indices but preserves the one-of-each
condition, so it cannot repair the contradiction. Equality yields the
side word (ell,1,t,1,ell) and angle word
(120,a,b,210-b,210-a).

## Exact parameter completeness and convexity

With vertex0 at0 and side0 on the positive real axis, vertex4 is
ell*omega. Writing a=7h+p forces -h<p<h. The exterior turns give
unit side directions5h-p and15h-p. Thus the source's five coordinates
follow without an extra orientation or length assumption.

The middle vector has the exact factorization

    exp(10hi)*(sqrt(3)*ell-2sin(h)*exp(-ip)).

Its compatible convex direction lies between120 and180 degrees, so the
argument of the bracket lies between -30 and30 degrees. The native angle
equation is q=b-7h=-p-arg(w). The bracket's imaginary part has the sign
of p. Hence |q|<h is exactly the strict bound
|arg(w)|<h-|p|, with positive real part. For p=0 the compatible middle
vector requires w>0, not the negative real branch.

The positive-real tangent inequality is equivalently

    sqrt(3)*ell > 2s*(cos(p)+sin(|p|)*cot(h-|p|))
                    = 2s^2/sin(h-|p|).

This is precisely the strict domain (A). It excludes a zero middle edge
at p=0 and all right/120-degree small-corner boundary cases. Conversely,
that domain makes w's real part positive and gives the desired argument
bound. All four small angles are strictly between90 and120, t=|w|>0,
and the closing positive side directions turn exactly once. Their
supporting heights first increase and then decrease to zero, so all
nonincident vertices are strictly on the interior side. Thus the
coordinates give a genuine convex pentagon and no missing parameter
branch is needed.

Reflection in the bisector of the120-degree corner has complex form
z -> omega*conjugate(z); reversing the vertex traversal sends the family
parameter p to -p. It leaves ell unchanged and gives exactly the source's
reflected family member. The parameterization need not identify this
symmetry to establish the if-and-only-if statement.

## Universal gluing checked independently

The checker represents every vertex as a complex affine form in the
independent symbols ell and rho=exp(-ip). It checks each endpoint
identity coefficientwise, so this part is not parameter sampling.
It reconstructs all21 undirected edge pairs: the A and B triple-center
pairings, the three side2 A/B pairings with their period offsets, and
all twelve Q-side pairings from the source table. Each native edge occurs
once and every endpoint map reverses the boundary direction.

From this edge involution it independently walks corner cycles by crossing
the incoming paired edge. All42 corners fall into exactly14 ordered
cycles of length3: two PPP cycles consisting of120-degree corners and
twelve QPP cycles. Formal angle coefficients verify total360 degrees
for every cycle, with a and b left symbolic. The face adjacency graph is
connected, its gluing is orientable, and V-E+F=14-21+7=0. This directly
checks the finite abstract surface needed for the universal proof.

For the strictly convex family faces, reversed common edge directions
put the neighboring polygons on opposite local half-planes. At a vertex,
the checked corner-cycle order and positive angles summing to360 make
the face wedges cover a neighborhood once. The resulting map of the
compact glued surface into C/(Z*u+Z*v) is therefore locally an
orientation-preserving Euclidean isometry. It is not assumed globally
injective at this stage.

The claimed area identity is also checked coefficientwise. Before imposing
rho=x-iy with x^2+y^2=1, exact shoelace gives

    area(P)=sqrt(3)*ell^2/4
             +sqrt(3)*ell*R*x/2-(x^2+y^2)/4,
    area(Q)=3cot(h)*(x^2+y^2).

The sum over all seven faces equals the determinant polynomial

    (3sqrt(3)/2)*((ell+R*x)^2+(R*y)^2).

Restricting to the unit circle yields exactly (F),(G),(H). Since
Re(q0)>0 in the strict domain, the lattice determinant is positive.

A compact local homeomorphism onto the connected target torus is a
finite covering: its image is open and closed, compactness makes fibers
finite, and local inverse neighborhoods make the fiber cardinality locally
constant. The checked total face area equals the torus area, forcing degree1.
Thus the map is globally a homeomorphism and its lifted faces give the
claimed plane tiling with disjoint interiors. Accidental coordinate
coincidences would increase fiber multiplicity and are excluded by this
same degree argument. Area equality is used after local completeness,
not to justify an arbitrary packing.

## Independent asymmetric fixture

The checker also decodes and verifies every retained coordinate of the
fixed member ell=2, sin(p)=1/8, cos(p)=sqrt(63)/8. It verifies the strict
parameter inequality by exact multiplication with sin(h-p)>0, so no
floating argument computation is required. All seven polygons satisfy
strict support inequalities. Exact squared lengths and angle cosines
check a regular unit Q12, the prescribed P side word, the unique120-degree
corner, and four strictly obtuse complementary small angles. All rotations,
half-turns, period vectors, and fixture area formulas match the source.

The lattice-coordinate projection bounds are derived independently for
all ordered motif pairs. They give exactly the retained62 nontrivial
integer-shift comparisons. Every one passes the separating-axis test.
Any omitted shift has disjoint coordinate projections. The motif areas
sum to the exact positive lattice covolume. Local finiteness and closedness
of the periodic union then prove whole-plane coverage from full cell area.
This is a direct finite-to-infinite proof for the fixture, independent of
the general covering construction.

## Replay and scope

```text
conda run --no-capture-output -n arisearch python research/reviews/verify_regular_dodecagon_independent.py
```

The checker passed all universal gluing/corner/area checks and the complete
fixture replay. It imports no producer, makes no numerical decisions, and
uses no stochastic seed, solver, geometric cutoff, period bound, or finite
orientation assumption for the classification. The existing reviewed
all-obtuse forcing and good-limit arguments are explicit dependencies.

The result excludes8<=n<=11 and classifies n=12 for an all-obtuse pentagon
and regular unit Q_n. It supplies a periodic escape for every tileable
n=12 member. It does not establish that all tilings of a member are
periodic, nor classify n>=13, nonregular Q, or right/acute P corners.
No primary-literature priority or novelty claim is made. No substantive
defect was found.
