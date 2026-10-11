# Penrose source membership of the retained Robinson rhomb clusters

**Status:** adversarially reviewed exact proper-Penrose membership
exclusion. The [fresh hostile review](../reviews/pentagrid-robinson-penrose-window-review.md)
found no unresolved source-convention, singular-transfer, or computational
defect; an independent resume audit on 2026-10-10 rechecked the primary
source and replayed the independent verifier. This excludes the stated
unit-Robinson source compiler. It does not establish an aperiodic U/V
tiling or exclude every other geometric construction.

## Exact objects and bounded source scope

The fixed U,V shapes have angle-after-side words(1,3,4,4,3) and
(2,2,4,3,4) in pi/5 units, with respective lengths
(phi^3,phi^3,1,1,1) and(1,1+3phi,1,2phi,2phi).
The unit source rhombs are thin36/144 and fat72/108. Thin rhombs are
cut along their short diagonal and fat rhombs along their long diagonal;
the resulting unit Robinson triangles have nonunit edge lengths
s=phi-1 and l=phi.

The inputs are all retained SAT assemblies in
`research/certificates/pentagrid-robinson-residual-rhombs.json`, together
with every compulsory boundary parent rhomb. This is28 retained U
assemblies and168 retained V assemblies; the geometric producer kept
one SAT assembly per successful boundary word, not all residual fillings.

A separate, stronger boundary-only test uses ALL28 U and185 V boundary
words retained by the necessary exact height/diagonal/completion screens
in `research/certificates/pentagrid-robinson-boundary-completion.json`.
Every such boundary includes its compulsory full rhomb parents, including
their halves outside the macro. Unit boundary steps are also source edges
and connect the height graph. These boundary-only objects are independent
of the choice of residual filling. The result below is conditional on the
separate completeness and necessity of those upstream fixed-boundary
screens; their fresh reviews are independent dependencies.

Every one of these retained boundary objects has no occurrence in a
regular proper Penrose rhomb source. Under the stated common finite-pattern
language of proper Penrose tilings, the same exclusion applies to singular
proper Penrose tilings. It does not apply to every generalized Penrose
cut-and-project tiling with noninteger intercept sum, nor to arbitrary
unit-rhomb tilings without Penrose arrows. It does not exclude U/V tilings
whose macro tiles are not these prescribed whole-source-triangle fusions.

## Primary source and why a regular strip test is appropriate

The inspected primary source is Fernique and Lutfalla,
[arXiv2211.08239v2](https://arxiv.org/html/2211.08239v2), Section2.3,
Definition2 and its subsequent Penrose specialization. It selects whole
integer unit2-facets in E+[0,1]^5 and projects them onto the physical
plane. Its physical slope has cosine/sine directions2pi*j/5. Proper
Penrose tilings specialize to an affine intercept whose coordinate sum
is an integer. Definition2 assumes that the strip boundary contains no
integer point; it is a regular construction.

The Introduction states that Penrose tilings share their finite patterns.
Therefore an alleged finite patch in a singular proper Penrose tiling
must also occur in a regular proper Penrose tiling. This uses the proper
Penrose finite-pattern language, not an unrestricted all-facets rule at
an arbitrary singular generalized intercept. No four-layer conclusion is
asserted directly for such arbitrary singular selections.

There exist regular integer-sum intercepts: in the two-dimensional internal
star-coordinate space, the integer-point boundary conditions form
countably many nontrivial affine lines. Choose an intercept outside their
union. The normals are nonzero in these two coordinates (also checked for
all20 window facets by the exact producer), so no boundary condition is
identically imposed by the integer sum. Such a source is a proper Penrose
source by the cited specialization.

## Canonical lift, coordinate conversion, and finite four-layer gate

Let z=exp(pi*i/5). Give a unit edge of physical direction z^k lift E_k
in Z^5, where E_i=e_i for0<=i<5 and E_(i+5)=-E_i. Rhomb loops lift to
zero. The imported plane-source height lemma proves path independence;
the retained finite graphs are independently traversed and every repeated
vertex height is checked for agreement. The lift is unique up to an
integer constant. No choice of physical kernel gauge at individual
vertices is permitted, because every unit edge has this fixed lift and
the graphs are connected.

The paper uses rho=z^2 directions. Convert H into its native rho basis by

    N_(3i mod5)=(-1)^i*H_i.

Then sum_i H_i*z^i=sum_j N_j*rho^j, and

    kappa=sum_j N_j=sum_i(-1)^i*H_i.

In these coordinates define the internal projection

    I(N)=(kappa, a, t),
    a=sum_j N_j*cos(4pi*j/5),
    t=sum_j N_j*sin(4pi*j/5)/sin(pi/5).

These three functionals annihilate the physical slope and are independent.
They are an invertible coordinate representation of its internal space;
they need not be an orthonormal projection. Their values lie in Q(sqrt5)
for integer N.

For an affine physical plane with coordinate sum m integer, a selected
integer vertex is in E+[0,1]^5, so0<=kappa-m<=5. Equality at0 or5
forces all five cube coordinates to0 or1, respectively; the point then
lies on the strip boundary. Regularity excludes equality. Consequently
all vertices of a finite proper Penrose patch have kappa in the four
consecutive layers m+1,...,m+4, and its layer span is at most3.

Adding a constant height shifts all kappas equally. Rotating or reflecting
the physical source direction frame changes kappa by an overall sign plus
constant, so the span gate respects all allowed isometries. The subsequent
full window test likewise covers all internal translations, and the cube
is preserved up to an integer translation by signed-basis/permutation
frame conversion; that translation is absorbed in the intercept shift.

The first retained full U object (six residual plus four boundary parents)
has18 vertices with layer interval[-3,1], span4. The first retained full V
object (nine residual plus seven boundary parents) has27 vertices with
interval[-4,3], span7. Both fail already at this gate; V even exceeds the
width5 closed-strip bound for an arbitrary intercept.

## Exact full window gate and small rejection certificates

The internal window is the zonotope

    W=I([0,1]^5)
     =conv{I(n):n in{0,1}^5}.

It has20 support facets, computed in the exact real field Q(sqrt5).
For a candidate fixed integer intercept sum m and internal shift(A,T),
every selected vertex N must satisfy

    I(N)-(m,A,T) in W.

In the regular source these are all strict support inequalities. If a
facet is h0+hk*kappa+ha*a+ht*t>=0, its constraint at vertex N is

    C-ha*A-ht*T>0,
    C=h0+hk*(kappa(N)-m)+ha*a(N)+ht*t(N).              (1)

The possible integer m values are exactly

    max(kappa)-4 <= m <= min(kappa)-1.

Every four-layer survivor here has span3 and hence exactly one possible m.

The producer maximizes a common margin delta, with0<=delta<=1, in the
closed inequalities corresponding to(1). It performs exact field-backed
polyhedron arithmetic; no numeric tolerance determines membership.
For every failed window test it also emits a two- or three-row Farkas
certificate. Its nonnegative weights, not all zero, satisfy

    sum lambda*(-ha,-ht)=(0,0),
    sum lambda*C<=0.

Thus simultaneous strict inequalities(1) would imply a positive sum with
left side equal to a nonpositive constant, an immediate contradiction.
A negative sum excludes even the closed window; a zero sum excludes the
regular source without by itself deciding closed-window feasibility. These small
certificates permit checking the decisive rejection without trusting the
polyhedron backend. Their exact selected rows and positive weights are
stored alongside the corresponding vertex lifts and facet data.

All vertices of each compulsory completed boundary rhomb are included.
The completion apex layers equal the midpoint of a diagonal's two endpoint
layers, so this inclusion does not silently change the earlier layer rule;
it can strengthen the other two internal-coordinate constraints.

## Completed finite results

| Object domain | Count | Layer-span histogram | Four-layer passes | Strict-window passes |
| --- | ---: | --- | ---: | ---: |
| retained full U assemblies |28|3:3,4:19,5:6|3|0|
| retained full V assemblies |168|3:6,4:27,5:33,6:39,7:42,10:21|6|0|
| compulsory U boundaries |28|3:4,4:20,5:4|4|0|
| compulsory V boundaries |185|3:8,4:32,5:44,6:36,7:42,10:23|8|0|

The boundary-only test rejects every retained boundary before any residual
filling is chosen. Therefore an alternate filling of one of these SAME
words cannot repair proper Penrose membership. This is stronger than the
retained-assembly test but still depends on the completeness of the
upstream necessary boundary screens; it is not an enumeration of every
geometrically conceivable pentagon construction.

Among full retained assemblies, only U row8 has nonempty closed-window
acceptance. Its words are

    (l,u,l), (u,s,l,u), (u), (u), (u),

and its reported feasible shift is on the window boundary:

    m=-4, A=1-sqrt5/2, T=(sqrt5-1)/2, delta=0.

It has a zero-constant Farkas certificate and hence no regular proper
Penrose occurrence. This borderline case is the essential reason not to
replace the source argument by a blanket statement about arbitrary singular
closed-window choices. Singular proper-Penrose exclusion uses finite-pattern
transfer as stated above. The mandatory-only domain additionally has U
boundary row14 on the closed window boundary. Both zero-margin boundary
objects fail strict membership, so neither an alternate residual filling
nor a singular proper-Penrose source supplies an escape.

## Reproducibility and non-consequences

Producer:
`research/searches/pentagrid-robinson-penrose-window.py`.
Certificate:
`research/certificates/pentagrid-robinson-penrose-window.json`.
Small same-author verifier, importing neither producer nor polyhedron
backend:
`research/searches/verify_pentagrid_robinson_penrose_window_certificate.py`.
It independently reconstructs the20 zonotope facets from generator-pair
cross products, all213 boundary layer intervals, and all21 retained
small strict-window dual obstructions (nine full and twelve boundary-only).
This mechanical replay does not count as a fresh hostile mathematical review.
The separate [independent verifier](../reviews/verify_pentagrid_robinson_penrose_window_independent.py)
reconstructs the complete mandatory and full-rhomb graphs directly,
traverses native rho-basis unit lifts, independently clips every surviving
window intersection, and checks the retained duals. Its successful replay
and the source-language audit are recorded in the fresh hostile review.

```text
conda run --no-capture-output -n arisearch python research/searches/pentagrid-robinson-penrose-window.py
conda run --no-capture-output -n arisearch python research/searches/verify_pentagrid_robinson_penrose_window_certificate.py
conda run --no-capture-output -n arisearch python research/reviews/verify_pentagrid_robinson_penrose_window_independent.py
```

The domain is exactly the retained fixed-boundary objects and retained
SAT witnesses from the named input certificates. No solver period bound,
random seed, timeout extrapolation, arrow-only sufficiency claim, or global
macro tiling is used. The inspected primary source explicitly discusses
finite arrow-legal deceptions, so local arrow compatibility would not
replace this membership test.

No global source witness survived this test. These failures do not prove
that U,V fail unrestricted plane tilability, nor that any admitted tiling
would be aperiodic. They reject this unit-Penrose Robinson-source compiler,
with independently reviewed upstream necessary-boundary completeness
and the cited primary source-language theorem as explicit dependencies. No novelty claim is made.
