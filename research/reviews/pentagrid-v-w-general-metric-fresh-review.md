# Fresh hostile review of the full V/W metric construction

**Verdict: VALID for the stated cone and universal selected-partner consequence.**
Reviewer: `/root/penrose_extension_gate`, 2026-10-10. The reviewer authored neither
this construction nor its producer. This is an additional independent review;
it does not replace the earlier root review or claim literature priority.

Reviewed [the lemma](../lemmas/pentagrid-v-w-general-metric.md) and
[producer](../searches/pentagrid-v-w-general-metric.py) in full. No theorem defect
or omitted positive-metric case was found. The new
[reviewer checker](verify_pentagrid_v_w_general_metric_independent.py) imports no
author producer, retained certificate, or earlier partner checker. It builds
native directed walks, derives every reversed side twin and its integer period
displacement, verifies the actual circular corner links including accumulated
shift zero, and independently checks the full cone and fixture overlaps.

## Full parameter domain and genuine polygons

The two V closure equations uniquely determine r,e from x,y,f, and the two W
closure equations uniquely determine H,E. This really gives three parameters;
there is no missing mirror condition. The seven positive native lengths are
exactly the stated domain. The claimed five irredundant inequalities are
equivalent: E+e=2f and r=x/phi+f+(x+f/phi-y) remove the other two. Independent
exact enumeration of all 21 rank-two active pairs gives the five stated rays;
for each of the five alleged facets the on-facet rays span a plane and their
sum satisfies the other four facet inequalities strictly.

Positive closure and directions turning counterclockwise exactly once prove
global strict convexity. For any fixed edge, subsequent cross increments have
one positive block and one negative block; every nonincident partial sum is
positive by closure, including when one increment is zero at the opposite
direction. Thus the argument establishes supporting edges and simplicity,
not only positive local turns. V has native angles (4,2,2,4,3)pi/5 and W has
five 3pi/5 angles. Their angle multisets distinguish the two congruence classes
under reflections as well as direct isometries.

Repeated side lengths inside either polygon, and incidental equalities among
otherwise private values, are included. None of the construction's identities
requires a length to identify a unique native side. Designated side pairings
remain legal at every point of the strict cone.

## Local quotient and complete plane coverage

The checker derives 20 mutually inverse directed side twins, or ten seams,
from the walks. Their links are four 3-corner cycles and two 4-corner cycles.
Each is one actual circle, its corner angles sum to 2pi, and its accumulated
integer shift is (0,0). The four-face graph is connected. Each reference face
is counterclockwise and each identification reverses endpoint order, so the
positive sectors concatenate without changing orientation or leaving a local
gap at edges or vertices.

The abstract polygon quotient is therefore a compact oriented surface with
a local Euclidean map to the displayed lattice torus. The independent formal
identities give

    cross(u,v)/sin(pi/5)=2phi*f*(phi*(x+y)+f)>0,
    cross(u,v)=2area(V)+2area(W).

Compactness makes the local map a finite covering, and the second identity
makes its degree one. This justifies every lattice translate, disjoint
interiors, and full-plane coverage throughout the entire positive domain.
Possible accidental metric coincidences cannot invalidate this degree-one
argument. The fixture check is corroboration, not the extension proof.

## Quantifiers and replay

For any given positive equiangular pentagon W, choose a shortest side as native
side 0. Then x>=y, and the closure equations force the displayed H,E. This
guarantees r,e>0 without any strict shortest-side uniqueness. Cyclic numbering
and reflection of a supplied W cause no difficulty. The conclusion is that
**some explicitly selected V partner** admits a periodic pair tiling with W.
It does not establish periodicity for every other polygon paired with that W,
classify independently specified V/W metrics, or prove every tiling periodic.

Replayed successfully:

```text
conda run --no-capture-output -n arisearch python research/searches/pentagrid-v-w-general-metric.py
conda run --no-capture-output -n arisearch python research/reviews/verify_pentagrid_v_w_general_metric_independent.py
```

The independent replay passes all symbolic native walks, 20 derived twins,
six closed links, five cone rays and facets, formal covolume, strict supporting
sides of x=2,y=1,f=3, and all 32 possible nontrivial ordered-pair lattice overlaps.
The overlap domain is derived from exact inverse-lattice bounding intervals,
and separation uses exact algebraic supporting lines. No author import,
bounded period search, solver timeout, or random seed is involved. The script
requires assertions. This review creates no additional research mechanism.
