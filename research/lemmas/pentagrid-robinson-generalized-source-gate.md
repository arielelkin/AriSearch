# Generalized pentagrid extension of the fixed U/V source compiler

**Status:** adversarially reviewed VALID with exact certificates; see the [fresh independent review](../reviews/pentagrid-robinson-generalized-window-review.md). This concerns the fixed unit Robinson-triangle source compiler, not
unrestricted U/V plane tilability or the main aperiodic-pair problem.

## Statement and exact source scope

Use the same fixed U/V shapes, source cuts, complete necessary boundary domain,
and canonical integer lifts as in the reviewed
[proper-source exclusion](pentagrid-robinson-penrose-window-exclusion.md).
Thus U has angle-after-side word(1,3,4,4,3) and lengths
(phi^3,phi^3,1,1,1); V has word(2,2,4,3,4) and lengths
(1,1+3phi,1,2phi,2phi). Thin unit rhombs are cut along their short diagonal,
fat unit rhombs along their long diagonal. The source facets are whole rhombs;
triangles used by a macro may have their paired half outside the macro.

Let E be any affine plane parallel to the physical Penrose slope in R^5,
without restricting its intercept sum to an integer. A regular generalized
source consists of all integer coordinate unit2-facets in E+[0,1]^5,
projected onto E and normalized to unit rhomb sides. This is the generalized
source construction in Section2.3, Definition2 of
[Fernique--Lutfalla, arXiv2211.08239v2](https://arxiv.org/html/2211.08239v2).
The fixed slope is spanned by(cos(2pi*j/5))_j and(sin(2pi*j/5))_j.
Regular means that the strip boundary contains no integer point.

Conditional on the reviewed upstream completeness of the fixed boundary
compiler, the exact results are:

1. None of the185 mandatory V boundaries occurs in ANY regular generalized
   source, regardless of residual filling.
2. The same exclusion holds in every source in the local matching closure of
   the union of these regular generalized source spaces.
3. Retained full U assemblies7 and8 DO occur in infinite regular generalized
   sources. Their acceptance requires a noninteger intercept sum. The other26
   retained full U assemblies fail this regular-source test.

Consequently changing only the intercept sum cannot repair the fixed U/V
compiler: its V tile still cannot occur. A global U/V repartition of such a
source therefore does not exist. Arbitrary singular all-facet selection rules
outside the stated local closure are not classified here.

## Compiler closure and reopening requirements

**Closed compiler:** the exact unit Robinson cuts and exact U/V macro data
above. Both source gates and their independent reviews are complete.

| Source space | Fixed compiler outcome | Decisive scope |
| --- | --- | --- |
| Proper Penrose sources | Excluded | All mandatory boundaries fail; proper singular cases use the reviewed common finite-pattern language. |
| All regular generalized sources at the fixed slope | Excluded | Every mandatory V boundary fails over all real internal shifts. |
| Local matching closure of the union of those regular generalized spaces | Excluded | A finite mandatory V patch in a limit would occur in an approximant. |
| Arbitrary singular closed-window selections outside that closure | Unclassified | Zero-constant strict obstructions do not exclude these selections. |

The V rejection uses mandatory exterior/paired whole rhombs before any
residual filling. The proper gate rejects177 V boundaries by its layer
condition and8 by empty closed intersections; the generalized gate rejects
145 by strict width and40 by retained positive duals. Changing only the
intercept, enumerating another residual filling, or enlarging the residual
assembly search cannot repair this fixed compiler. It is not an unrestricted
U/V untileability theorem.

No further search is assigned to this compiler. To reopen, supply all of:

1. Exact replacement data: source polygons and cuts, macro coordinates and
   relative scales, and source slope/window or an exact alternative source
   rule. Identify at least one changed assumption used by the exclusion.
2. The particular obstruction removed: show which mandatory boundary,
   integer lift, support-facet inequality, width bound or local-closure
   premise no longer applies. An intercept change alone is insufficient.
3. Cheap exact checks of positive closure, convexity, source-side incidence,
   reflections and compulsory partner halves before a new assembly search.
4. A stated global obligation and proposed proof: source occurrence in an
   infinite legal tiling, a global two-class partition, and unrestricted
   shape-only forcing. Finite assembly does not establish these obligations.

An arbitrary singular selection proposal must specify its actual selection
rule, prove that it produces a plane tiling, and establish its relation to
the stated local closure. It is an unclassified changed hypothesis, not an
existing loophole certified by a zero-margin window.

## Exact internal coordinates and source occurrence criterion

Put rho=exp(2pi*i/5), phi=(1+sqrt5)/2, and for N in Z^5 set

    I(N)=(sum N_j, sum N_j*cos(4pi*j/5),
                    sum N_j*sin(4pi*j/5)/sin(pi/5)).

I annihilates the physical slope and has rank3. Its generator lists are

    (1,1,0), (1,-phi/2,1), (1,(phi-1)/2,-phi),
    (1,(phi-1)/2,phi), (1,-phi/2,-1).

Let W=I([0,1]^5), with its20 exact support facets
h0+hk*k+ha*a+ht*t>=0. For a source shift q=(m,A,T), a lifted vertex N is
strictly inside the strip precisely when

    h0+hk*sum(N)+ha*a(N)+ht*t(N)-hk*m-ha*A-ht*T>0

for every support facet. All three coordinates of q are now free real
variables. This removes the integer four-layer restriction rather than
merely enlarging a search bound.

A whole coordinate unit2-facet lies strictly in the strip if its four
vertices satisfy these inequalities: the facet is their convex hull, and
all support inequalities are affine. Conversely every selected facet must
have all four vertices in the closed strip; regularity makes every integer
vertex strict. The graph checker verifies that the lifted rhombs are actual
coordinate unit2-facets, not only four projected points with suitable angles.

For a finite collection of these facets, a strict window witness provides an
open set of source shifts containing the collection. The set of shifts for
which ANY integer point meets ANY strip boundary facet is a countable union
of affine planes. No such plane contains an open ball. Choose a shift in the
open acceptance region outside this union; it defines a regular source
containing all the prescribed whole rhombs. The primary cut-and-project
theorem gives an infinite plane tiling by all selected facets. The prescribed
finite rhombs consequently occur in that tiling, as do the macro's retained
Robinson triangles.

The slope has no nonzero integer vector, as required by that source theorem.
Indeed an integer vector in the physical slope has zero coordinate sum and
zero Fourier coefficient at rho^2. Its degree-at-most4 integer polynomial
vanishes at this primitive fifth root, so it is a rational multiple of
1+X+X^2+X^3+X^4. Its coordinates are all equal, and their sum zero forces
all to vanish. Physical projection N -> sum N_j*rho^j is a fixed similarity
of the paper's orthogonal projection; normalization sets the source side1.

## Small exact certificates

For each of the20 normals, replace the constants from all vertices by their
minimum. This is an equivalent finite strict linear system in(m,A,T).
A failed object has a positive dependence of2,3,or4 of those normals:
weights lambda_i>0, normal sum zero, and constant sum<=0. Multiplying and
adding the selected strict inequalities would give a positive quantity
equal to a nonpositive constant, a contradiction.

The producer enumerates220 positive minimal dependencies of the20 fixed
normals. Completeness of this enumeration is not needed to trust any retained
rejection: its selected vertex rows and weights directly certify that object.
Positive objects retain their exact shift and minimum positive facet slack;
checking every original vertex against every independently reconstructed
facet directly certifies them.

The first coordinate of W is[0,5]. A strict object therefore has layer span
less than5. This supplies immediate width rejections when span>=5; equality5
would require both endpoint layers on window boundaries.

## Completed finite domain

| Objects | Count | Width rejects | Farkas strict rejects | Strict witnesses |
| --- | ---: | ---: | ---: | ---: |
| Mandatory U boundaries |28|4|20|4|
| Mandatory V boundaries |185|145|40|0|
| Retained full U assemblies |28|6|20|2|
| Retained full V assemblies |168|135|33|0|

The four positive mandatory U indices are7,8,14,18; the positive full U
indices are7,8. These are zero-based indices in the retained certificates.
For full U8 an exact shift and positive common slack are

    m=(sqrt5-17)/4,
    A=(6-3sqrt5)/8,
    T=(5-sqrt5)/8,
    slack=(3sqrt5-5)/8>0.

For full U7 they are

    m=(sqrt5-19)/5,
    A=(7-4sqrt5)/10,
    T=(7-3sqrt5)/10,
    slack=(5-sqrt5)/10>0.

Neither m is an integer. The regular shift chosen by the preceding open-set
argument need not be exactly the displayed algebraic shift; the latter only
certifies a nonempty open feasible region. Its noninteger first coordinate
can be preserved by a sufficiently small perturbation.

## Local closure and what zero constants do not prove

Every mandatory V object is a fixed finite collection of whole source
rhombs and source unit edges. If it occurred in a source which is a local
matching limit of regular generalized sources, enlarge it to a finite source
patch inside a ball. For sufficiently close approximants, that finite patch
occurs exactly after a small translation, by the definition of the local
matching topology. This would put the mandatory object in a regular source,
contradicting its strict rejection. Thus the exclusion passes to this local
closure, without assuming that all generalized sources share a common finite
language.

Some retained Farkas constants are zero. These prove lack of strict acceptance
only. They do not by themselves exclude arbitrary singular selections using
closed-window vertices. In particular this theorem must not silently identify
all such selections with the local matching closure just defined.

## Replay, dependencies, and remaining work

[Producer](../searches/pentagrid-robinson-generalized-window.py) and
[certificate](../certificates/pentagrid-robinson-generalized-window.json).
The producer reuses the independently reviewed native graph lift and zonotope
facet reconstruction. It does not modify existing source certificates.

    conda run --no-capture-output -n arisearch python research/searches/pentagrid-robinson-generalized-window.py

Normal invocation emits JSON to stdout; --output is required to write a
certificate. The [fresh independent checker](../reviews/verify_pentagrid_robinson_generalized_window_independent.py)
verifies all409 objects, six strict shifts,113 small dual certificates and290
width rejections, without importing the producer or a polyhedron backend.
The independent mathematical review validates both occurrence and exclusion. Full compiler completeness remains an explicit upstream
dependency. No unrestricted geometric forcing is imported from source
occurrence, and this does not exclude other U/V metrics, different cuts,
different macro scales, or a different source slope. No novelty claim is made.
