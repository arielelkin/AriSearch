# Fresh hostile review: thin-point deformation omission gate

Date: 2026-10-13. Independent reviewer: sol. **Verdict: VALID** for the exact
t=1/100 local pentagon and its nonmonohedral exclusion. The two-shape
construction/global covering problem remains unresolved.

## Exact claim and geometry checked

The reviewed objects are the retained producer and certificate
penrose-dual-fusion-thin-deformation, not a universal Penrose compiler.
Thick rhomb points remain centres; thin rhomb points shift by t times their
retained marked unit frame. All coordinates lie in Q(zeta10) with the
specified positive standard complex embedding. The independent checker
reconstructs the source data and the five vertices from scratch, checks every
source point strictly inside its own rhomb, and verifies strict crossing of
every internal source edge by its two point-connection segments using both
orientation-product tests. These tests imply nonzero denominators and interior
intersection parameters, without relying on the producer's rational formulas.
The two specified triangle/quadrilateral modules, the fused pentagon and the
retained untouched quadrilateral have every strict nonincident support.
This checks finite actual geometry; it does not certify a uniform marked
point rule on every legal source neighbourhood or the entire plane.

## Complete omission test and primary conditions

[Rao, Exhaustive search of convex pentagons which tile the plane,
arXiv1708.00274v1](https://arxiv.org/pdf/1708.00274), refreshed13 October2026,
was checked directly, including Table2 on PDF page14 and its following
classification discussion. The source permits rotations, reflections and
partial contacts. Its fifteen genuine families are necessary; the additional
listed cases reduce to those families or have no positive nondegenerate
geometric solution. Strict convexity of this pentagon excludes degeneracy.
This is an imported computer-assisted classification, not newly reproduced.

The independent checker re-enters all fifteen necessary ANGLE systems from
the primary table, with no import from the producer or its family filter.
For each family all five cyclic offsets and both cyclic directions are tested,
covering all10 geometric dihedral reindexings. Every one of the150 tests
fails at least one angle equation. In particular no side-equation transcription
or side-indexing ambiguity can restore a monohedral family in this fixture.
The producer's reflected side map k-i-1 is nevertheless the correct map for
sides connecting native vertices i and i+1.

For a counterclockwise convex polygon, (previous-current)/(next-current)
has argument equal to the interior angle in(0,pi). Dividing by its positive
algebraic modulus gives its exact unit phase. All required angle sums in the
primary table involve at most three angles, or twice an angle for targetpi;
phase comparison has no harmful branch choice. In any event a failed phase
is a rigorous failed exact angle equality, even without a converse. All150
failures match the retained certificate. Length square roots are exact AA
objects, but no successful angle row proceeds to a length test here.

Thus the local pentagon cannot tile monohedrally under the named theorem.
This closes a necessary omission gate for THAT shape and fixes the undeformed
Type1 escape; it does not prove that a second shape lacks an omission escape.

## Scope and continuation

The shift uses retained marked frames from an input source. Those frames are
construction bookkeeping, not allowed final matching rules. A full candidate
must establish a globally legal finite-family geometric rule and prove
shape-only forcing after forgetting markings, including reflections,
unintended contacts and omission. The source patch and local convex fusion
supply no infinite covering proof and no finite two-congruence-class reduction.
An untouched quadrilateral survives in the retained geometry; if it remains
as a final prototile it permits a periodic monohedral escape. It must be removed
or recomposed through an exact mechanism before accepting a two-shape candidate.
Other deformation parameters are not classified by the one exact sample.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/penrose-dual-fusion-thin-deformation.py --check research/certificates/penrose-dual-fusion-thin-deformation.json
    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_penrose_thin_deformation_omission_independent.py

Both outcomes: PASS. Finite domain is the retained source patch, its exact
specified modules and15 families times10 reindexings; no solver, seed,
timeout, numerical acceptance or inference of infinite extension.

## Full lemma review: incidence and density qualifications

The subsequently extracted lemma
[penrose-dual-single-fusion-deformation-gate.md](../lemmas/penrose-dual-single-fusion-deformation-gate.md)
was reviewed as a whole. The degree-two straightness statement is correct:
two complementary convex face sectors must both have anglepi. However the
claim that no opposite surviving rays forces deleted edges to form a matching
requires every source rhomb point to remain an intrinsic network vertex.
Deleting all four incident edges removes a vertex entirely, evading the
degree-two argument. Such disappearance is not excluded by convexity alone.
Retaining every point, as expressly assumed by the density calculation,
excludes degrees0/1 and therefore gives the matching condition. This precise
hypothesis must also accompany the earlier matching claim.

Under the stated degree3/4 retained-point condition, with N source rhombs
and M deleted edges, E=2N-M+O(R), V=N+O(R), F=N-M+O(R). Solving the face
incidence equations gives exactly F5=2N-4M+O(R), F6=3M-N+O(R), and the
number of degree4 vertices N-2M+O(R)=F5/2+O(R). These calculations are
correct. Nonnegativity gives N/3-O(R)<=M<=N/2+O(R); the originally displayed
exact finite lower bound N/3<=M drops its boundary error and must be corrected.
Equivalently any limiting deletion ratio lies in[1/3,1/2]. Positive lower
pentagon density keeps the upper ratio bounded away from1/2. These statements
remain conditional on a globally valid deletion rule and retained points;
they do not apply to collapsed degree2 points or deleted source vertices.

The centered-v10 and v11 producer replays are nondestructive checks of their
finite local records. The centered Type1 escape is a valid sufficient family
application. It does not promote the surviving deformed local polygon into
a global construction. After the two stated qualification repairs, the
extracted artifact's local geometry, monohedral gate and conditional density
requirements are VALID; global simultaneous deletion/finite-class/forcing
obligations remain explicitly unresolved.
