# Historical checkpoint from the October 2 research run

**Historical record, superseded.** This preserves the overnight checkpoint,
including intermediate conclusions and instructions that were later superseded.
Use [the current discovery log](../../discovery-log.md) for research decisions.
The October 3 review falsifies the final joint pentagon–hexagon pair.

## Run metadata

The recorded deadline was 2026-10-03 00:00 UTC. The original checkpoint
reports earlier termination because of execution/context budget; the Cloud
transcript and usage telemetry were not available during the subsequent review.
This deadline does not govern future runs.

## Original checkpoint

# Discovery log

**Problem status:** Unresolved.

**Checkpoint:** 2026-10-02.  The run deadline is 2026-10-03 00:00 UTC.  The
available execution/context budget required an earlier checkpoint; no final
construction or impossibility theorem has passed the acceptance gates.

## Definitions and global invariants

### Monohedral escape -- Proved

If either member of a proposed pair has a periodic monohedral tiling, that
tiling is already a periodic tiling admitted by the pair because use of both
types is not required.  Triangles and convex quadrilaterals are therefore
excluded.  Proof and precise scope:
`research/lemmas/periodic-obstructions.md`.

### Lattice-periodic combinatorial obstruction -- Proved

For a rank-two periodic tiling with \(a\) copies of an \(m\)-gon and \(b\)
copies of an \(n\)-gon per cell,
\(a(m-6)+b(n-6)\leq0\), including T-junctions.  Edge-to-edge torus identities
and a finite angle-balance certificate are also recorded in
`research/lemmas/periodic-obstructions.md`.  This is not an obstruction to
rank-one periodicity and is not an aperiodicity proof.

### Global side-count obstruction -- Adversarially reviewed

No finite set of convex polygons all having at least seven sides can tile the
plane, even with partial-edge contacts and T-junctions.  A square-exhaustion
proof controls holes and boundary subdivisions rather than assuming
edge-to-edge structure.  Therefore every candidate pair that tiles has a
member with at most six sides.  Together with monohedral escape, at least one
member of an aperiodic pair must be a pentagon or hexagon.  See
`research/lemmas/periodic-obstructions.md` and
`research/reviews/global-side-count-review.md`.

### Hexagon plus higher-sided polygon -- Adversarially reviewed

The quantitative side-count bound makes the higher-sided tile occur only
\(O(R)\) times in a radius-\(R\) window.  A separated-grid argument produces
arbitrarily large disks containing only hexagons; compactness then yields a
monohedral tiling by that hexagon.  The 2026 unrestricted classification of
monohedral convex hexagon tilers supplies a periodic monohedral tiling, which
is admitted by the pair.  Thus an aperiodic pair must contain a pentagon or
consist of two hexagons.  See
`research/reviews/hexagon-higher-side-review.md`.

### Two-hexagon defect-free limit -- Adversarially reviewed

Every tiling admitted by two convex hexagons has square-window subdivision
and excess-valence defect only \(O(R)\).  An exact Euler slack identity plus
grid compactness produces another tiling admitted by the pair which is
edge-to-edge and everywhere 3-valent (possibly monohedral).  This does not
prove periodicity, but reduces the surviving \((6,6)\) case to a much more
rigid tiling class.  See
`research/reviews/hexagon-defect-limit-review.md`.
The limiting cell complex is necessarily combinatorially the standard
hexagonal honeycomb, by an equilateral-development argument on its dual
6-valent triangulation.  Its geometry and two-type labelling are not thereby
periodic.  See `research/reviews/hexagon-combinatorics-review.md`.
If, in addition, its full exact placement states form a finite set and each
state uniquely determines neighbour state and displacement in every global
honeycomb direction, a finite-index lattice-kernel argument makes the tiling
doubly periodic.  Therefore any aperiodic \((6,6)\) candidate must escape via
branching matches, infinitely many orientations, or failure of this
determinism.  See `research/reviews/deterministic-hexagon-review.md`.
A separate Følner argument supplies a finite exact necessary certificate for
any specified two-hexagon candidate: real frequencies of labeled corner
triples with angle sum \(2\pi\), equal-length side-pair frequencies, all
corner/side marginals, area normalization, and Euler balance.  Infeasibility
kills a candidate, while feasibility is not sufficient.  See
`research/reviews/frequency-balance-review.md`.

### Pentagon curvature backbone -- Adversarially reviewed

An exact finite-patch curvature identity relates pentagon surplus to native
side subdivisions and excess vertex valence.  A pentagon paired with an
\(n\)-gon for \(n\ge7\) is uniformly relatively dense in every tiling.  The
same must hold in every aperiodic \((5,6)\) candidate.  Such a \((5,6)\)
candidate must force positive-density contact/valence defects; a \((5,5)\)
tiling has extensive defects automatically.  See
`research/reviews/pentagon-curvature-review.md`.

## Construction mechanisms

### Convex fusion of a known aperiodic protoset -- Active, conditional

A general fusion lemma shows that if one tiling by a strongly aperiodic
source set partitions into congruent convex clusters plus one residual tile
class, fusing each cluster yields a two-tile aperiodic set.  Unique
dissection is unnecessary: a hypothetical period permits orbit-consistent
choices of the fixed dissection.  Full proof and finite search conditions:
`research/lemmas/convex-cluster-fusion.md`.

This is currently conditional for the intended Ammann application.  Required
next facts are:

1. verify from a primary proof that the classical three-convex-polygon
   Ammann set is strongly aperiodic when reflections and all contacts are
   allowed, exactly matching this problem;
2. obtain exact coordinates/parameters for its two pentagons and hexagon;
3. calculate exact tile frequencies in a specified substitution hull;
4. test the necessary frequency equation
   \(f=\lambda u+\mu e_r\) for small cluster content vectors;
5. for surviving vectors, enumerate adjacency orbits and prove a global
   partition into congruent clusters;
6. test cluster convexity exactly, and ensure the fused polygon is not
   congruent to the residual polygon.

Earlier figure-based frequency reconnaissance was withdrawn.  A more careful
conditional planar count gives total hexagon:pentagon frequency
\(H:P=1:2\tau\), not the earlier estimate: for \(t\) thin and \(T\) thick
source rhombi, the marking graph has
\(E=3t+5T+O(\partial)\), \(V=2t+3T+O(\partial)\), hence
\(F=t+2T+O(\partial)\); if every face is a nonsuppressed pentagon or hexagon,
Euler degree counting yields \(H=t\), \(P=2T\).  Splitting the two pentagon
species equally is still only a figure inference.  No cluster-frequency
claim should be used until the legal vertex stars certify these hypotheses.

For a pair fused across a whole edge, convexity is equivalent to the sums of
the incident interior angles at both seam endpoints being at most \(\pi\).
An adversarially reviewed local obstruction sharpens this: at a trivalent
source vertex a convex cluster may contain all three incident tiles or only
one, but never exactly two.  Hence a two-tile fusion across an edge fails if
either endpoint is trivalent.  See
`research/reviews/trivalent-fusion-review.md` and the fusion lemma artifact.
For a fully edge-to-edge trivalent hexagon source, the closure rule propagates
through the triangular dual: every finite convex cluster is a singleton.
Thus decorated hexagonal matching systems cannot be converted to larger
convex macrotiles by cell clustering without introducing combinatorial
defects.  See `research/reviews/no-convex-hex-cluster-review.md`.

### Naive identification in Ammann's three-tile set -- Blocked

The classical recomposition uses points \(J,K,L\) with
\(GL=DJ\), \(FL=CJ=EK\), \(HK=BJ\), and requires the four lengths
\(DJ,CJ,BJ,KL\) to be distinct to encode matching data.  Tuning parameters
to make two pieces congruent collides with those distinguishing lengths and
destroys the stated forcing mechanism.  Deleting one class also destroys
the displayed tiling.  Reopen only with an exact parameter calculation that
preserves all source forcing hypotheses.

### Direct marked-edge encoding -- Locally obstructed

Convexity gives no jigsaw freedom while preserving square or rhomb carriers,
and every convex polygon edge admits a legal reflected self-match.  Thus a
faithful edge-local encoding of forbidden arrow/colour contacts is
impossible; any viable mechanism must enforce matching nonlocally through
complete vertex coronas and must survive reflection closure.  Exact scope and
non-consequences are in
`research/lemmas/convex-mark-encoding-obstructions.md`.

### Two obtuse hexagons as a rule compiler -- Active

A new positive mechanism survives the unrestricted-contact objection.  If
all twelve angles lie in \((\pi/2,\pi)\), every admitted tiling is
automatically edge-to-edge and trivalent.  Side-length equality classes and
angle-sum triples can then compile a finite reflection-closed honeycomb rule
language.  Exact closure equations, generic-separation conditions, and fast
obstructions are recorded in
`research/searches/two-obtuse-hexagon-encoding.md`; the forcing theorem and
its review are in `research/lemmas/obtuse-edge-forcing.md` and
`research/reviews/obtuse-edge-forcing-review.md`.

The next finite question is to transcribe the Walton--Whittaker R1/R2 system
into side slots and vertex triples and test whether its reflection closure is
representable by two cyclic hexagon words.  No solver should be written until
that incidence table is explicit.

The natural tile/mirror transcription has now been enumerated exactly.  Its 1,056
legal ordered vertex triples force the twelve corner angles to be exactly
\(2\pi/3\) (rank 12), while 240 allowed edge-flag pairs force all twelve side
lengths equal and thereby admit 336 forbidden contacts.  Thus this compiler
collapses to congruent regular hexagons and is falsified.  Source-state
identification and scope caveats are recorded at
`research/searches/walton-encoding-reconnaissance.md`, with certificate and
independent verifier.

A broader state-assignment exhaustion now checks all 4,094 nonconstant maps
from the twelve Walton rotation/reflection states to two geometric types,
retaining all compatible source vertices.  Exactly four maps leave an angular
degree of freedom; all four force every side of both hexagons equal, and the
remaining one-parameter equilateral hexagon fails polygonal closure unless
the parameter is zero.  Hence every map in this finite compiler family
collapses to regular hexagons.  The search, certificate, and hostile review
are `research/searches/walton_state_assignment_rank.py`,
`research/searches/walton_state_assignment_rank_certificate.json`, and
`research/reviews/walton-state-assignment-review.md`.  This closes the former
"alternative state assignment" branch, but not arbitrary strict sublanguages
or different matching-rule sources.

## Exact candidate falsification

No explicit two-polygon candidate with exact coordinates was selected.
Accordingly, the candidate-falsification machinery was not activated and no
generic geometry framework was built.

The exact Penrose-rhomb counterexample to merely forgetting decorations is
preserved at `research/counterexamples/forgetting-penrose-arrows.md`.

## Literature equivalences and novelty boundary

The current search is recorded at
`research/literature/2026-10-02-search.md`.  Relative to those arXiv and
OpenAlex queries, the closest source still explicitly reports the two-convex
question open.  Recent proposed three-type families prohibit reflections and
do not satisfy the present problem.  Even completeness of the fifteen
convex-pentagon monotile families is described in 2026 literature as not
definitively established.

A dedicated audit of the classical Ammann three-convex-polygon benchmark is
at `research/reviews/ammann-convex-source-audit.md`.  It recovers exact
Penrose-rhomb coordinates and the stated length relations, but finds no
accessible proof covering reflections, T-junctions, or partial-edge contacts.
The similarly named rigorous 1992 Ammann A2--A5 paper treats different
marked/concave systems and cannot discharge this obligation.

Exact multibranch formulas for the Ammann diagram's points \(K,L\) in terms
of the free interior point \(J\), together with the corrected conditional
aggregate face count, are preserved at
`research/searches/ammann-coordinate-parameterization.md`.  They do not yet
select prototiles: the exact \(J\), circle-intersection branches, cyclic
polygon vertices, and legal vertex-star data remain missing.

## Assumption ledger

* Reflections, rotations, translations, and non-edge-to-edge contacts are
  permitted: problem definition, never relaxed.
* A tiling may omit one prototile: problem definition; drives monohedral
  escape.
* Classical Ammann three-tile strong aperiodicity under allowed reflections
  and non-edge-to-edge contacts: **unverified imported claim**, and a blocker
  for fusion.  The rigorous 1992 Ammann--Gruenbaum--Shephard paper treats
  different marked/concave A2--A5 families and does not fill this gap.
* Existence of a convex global cluster partition in an Ammann tiling:
  **conjectural**.
* Completeness of known convex-pentagon monohedral families: **not assumed**.

## Portfolio reset and restart state

* **Proved structural theorem:** monohedral escape and elementary exclusions.
* **Adversarially reviewed structural theorem:** every tileable finite
  protoset has a member with at most six sides.
* **Adversarially reviewed structural theorem:** side types \((6,n)\) with
  \(n>6\) cannot be aperiodic.
* **Adversarially reviewed reduction:** every tileable \((6,6)\) pair admits
  an edge-to-edge, trivalent limit tiling.
* **Proved rank-two obstruction:** torus side-count and angle accounting.
* **Active construction mechanism:** conditional convex-cluster fusion.
* **Blocked shortcut:** identify or delete an Ammann tile class.
* **Literature status:** no resolution found within documented boundary.
* **Exact candidate:** none yet.

The highest-information next action is to retrieve the primary Ammann proof
and exact diagram data, audit its reflection convention, and compute the
three tile frequencies.  If the source set survives and a content vector
passes the frequency equation, enumerate only those convex connected
clusters.  In parallel, seek a different rigorously established convex
source set under unrestricted reflections; do not invest in a verifier until
an exact finite candidate question exists.

The relative decoration freedom in that no-go has also been exhausted: all 24
relative cyclic-shift/chirality/global-charge choices for the two compiled
Walton words give the same 1,056-triple, rank-12, single-length-class collapse.
See `research/searches/walton_relative_relabeling_rank.py` and its JSON
certificate.  The Walton route now requires a genuinely strict hierarchical
sublanguage or a non-word-based geometric encoding, not a relabeling.

The 24-case computation admits a group-theoretic upgrade: every bijective,
one-block, Euclidean-equivariant compiler from the two global-charge orbits of
the asymmetric Walton hexagon to the placement orbits of two labelled
geometric hexagons is, up to common relabelling, one of those 24 cases.  The
result is now isolated as `research/lemmas/walton-one-block-obstruction.md`.
This rules out the complete natural one-block compiler class, while explicitly
leaving neighbourhood-dependent, hierarchical, non-bijective, or strict
sublanguage compilers open.

The convex-fusion obstruction has been strengthened: hexagonal combinatorial
rigidity was unnecessary.  In any connected edge-to-edge tiling with exactly
three genuine convex tile sectors at each vertex, a finite convex cluster
cannot contain more than one tile.  The dual is a connected triangulation;
once a cluster contains a dual edge, convexity selects both incident
triangles and propagates across every dual face.  Consequently the all-obtuse
mechanism (which forces edge-to-edge trivalence) and finite convex-cluster
fusion are mutually incompatible for every side-count pair, not only
$(6,6)$.  The revised proof is in
`research/lemmas/convex-cluster-fusion.md` and its hostile review.

A fresh primary-source pass over Sugimoto v5 found that its own two-type
congruence specializations have already been tested and fail in both relevant
ways: at 105°/150° a convex hexagon is a periodic monotile, while at 165° and
one 180° specialization the surviving convex classes have displayed mixed
periodic tilings despite reportedly not tiling alone.  Moreover all of the
paper's positive Tile(1,1) divisions become periodic when reflections are
allowed.  The negative parameter map is recorded at
`research/searches/sugimoto-two-type-degeneracies.md`.  This closes simple
parameter collision in that family and reinforces that non-monotility of the
individual pieces is insufficient.

A further honeycomb constraint is proved and reviewed: in every defect-free
edge-to-edge trivalent two-hexagon tiling, at least one third of contacts are
same-type in Følner density.  It is the elementary fact that every triangular
dual face has a monochromatic edge, double-counted by at most two faces.  A
geometric compiler permitting only A--B contacts is therefore impossible;
the result is in `research/lemmas/periodic-obstructions.md` with review
`research/reviews/hexagon-contact-density-review.md`.

For the remaining all-obtuse $(5,n)$ branch, $n\ge7$, the curvature identity
now gives the exact Følner ratio $f_5:f_n=(n-6):1$ and uniform positive
quadratic counts of both types.  The higher polygon cannot be a sparse defect.
This is recorded and reviewed in the obtuse-edge-forcing artifacts; it remains
a necessary condition rather than a construction.

A newly audited near miss converts the two Penrose rhombs directly into two
convex pentagons for $54^\circ<\theta<90^\circ$ (Sugimoto,
arXiv:2203.04457v3).  It is not a candidate: both pentagons belong to the
Type-2 monohedral family and therefore admit periodic tilings alone.  The
source only converts a chosen rhomb pattern and supplies no converse forcing
argument.  The audit is at
`research/searches/penrose-to-two-pentagons-audit.md` and has been added to
the literature boundary.

The T-junction strategy has been generalized beyond all-obtuse polygons.  If
no finite multiset of labelled prototile angles sums exactly to $\pi$, every
otherwise-unrestricted tiling is automatically edge-to-edge: a vertex in a
side interior would partition the opposite half-disk into precisely such a
sum.  This is a finite exact check (bounded by the smallest angle) and leaves
higher-valence $2\pi$ sums available, unlike the all-obtuse condition.  It is
therefore the preferred forcing mechanism for future $(5,6)$ candidates,
which require positive-density excess valence.  The proof and hostile review
are `research/lemmas/angle-nonresonance-edge-forcing.md` and
`research/reviews/angle-nonresonance-review.md`.

Combining angle nonresonance with curvature sharpens the prospective $(5,6)$
mechanism: with subdivision defect eliminated,
$2\sum(\deg v-3)=N_5+O(R)$.  If only trivalent and 4-valent vertices occur,
4-valent stars must have asymptotic count one half of the pentagon count.  A
future compiler should target this exact incidence balance rather than an
all-trivalent language.

An exact rational-angle $(5,6)$ scaffold now demonstrates that the new route
is not arithmetically empty.  The cyclic angles
$P=(66,162,66,96,150)^\circ$ and
$H=(102,111,99,147,117,144)^\circ$ have no multiset sum of $180^\circ$, yet
admit an exact nonnegative mixture of trivalent and 4-valent $360^\circ$
stars with every labelled corner balanced at tile-frequency ratio $2:1$ and
with $2D=N_5$.  Explicit positive cyclotomic side lengths close both strictly
convex polygons; the chosen hexagon violates all three Reinhardt systems and
cannot tile monohedrally.  This remains only a local scaffold: edge pairing,
global extension, extra admitted stars, pentagon monohedral escape, and
aperiodicity are open.  Artifacts are
`research/searches/nonresonant-5-6-angle-scaffold.md`, the exact script/JSON,
and `research/reviews/nonresonant-5-6-scaffold-review.md`.

The highest-information next action for this branch is no longer random angle
search.  It is to find a globally extendible planar substitution or matching
system using the certified incidence proportions, then choose side-length
classes to exclude every extra vertex/contact while retaining that system.
Until such a source language exists, the scaffold must not enter exact
candidate falsification.

The scaffold pentagon has now passed the strongest currently available
monohedral filter: under every cyclic/reflected labeling it fails an angle
condition for each of the fifteen known convex-pentagon tiler families.  The
exact checker verifies absence of three-corner and double-plus-one
$360^\circ$ relations and of $90^\circ$/$120^\circ$ corners.  Because the
fifteen-family completeness claim remains unconfirmed, this is explicitly not
promoted to a proof of monohedral escape.

A stronger exact check closes the scaffold pentagon's monohedral gate without
assuming completeness of the fifteen families.  Nonresonance forces any
hypothetical monohedral tiling edge-to-edge; the minimum angle bounds valence
by five; exhaustive enumeration shows that the pentagon's $150^\circ$ corner
belongs to no pentagon-only 3--5-sector $360^\circ$ sum.  Every copy contains
that unusable corner, so the pentagon cannot tile alone.  Together with the
Reinhardt exclusion for the hexagon, **both scaffold members now provably
avoid monohedral escape**.  The remaining blockers are existence of a global
mixed tiling and universal nonperiodicity, not the one-tile gate.

The full-edge audit now **falsifies the displayed exact $(5,6)$ shapes**.
At a vertex, adjacent side-length pairs must form a connected Eulerian cycle.
With the exact five distinct length values, only two of all angle-legal stars
are side-compatible, and they omit seven corner labels, so no tiling exists.
Exhausting all 52 partitions of those five symbols shows that supporting the
six balanced rows would force four symbols equal and make the pentagon
equilateral; its unit edge-vector sum has nonzero imaginary part and cannot
close.  The angle/nonresonance and monohedral results remain valid as a
relaxation, but future search must synthesize angle rows, side equalities, and
closure jointly.  The search script, JSON, report, and hostile review have
been updated rather than hiding this negative result.

A joint follow-up search repaired the specific sequencing mistake at the
relaxation level.  For the same rational angles it found side classes
`[0,2,0,1,2 | 2,3,1,4,0,1]` with a positive numerical closure kernel and a
nine-row angle-and-full-edge-compatible local language containing the
balanced six-row support.  Both types are locally incapable of monohedral
tilings.  This is not yet exact geometry or existence: face chirality must be
consistent globally.  The precise restart data and next finite torus-map
question (12 pentagons, 6 hexagons, 30 vertices) are preserved at
`research/searches/joint-5-6-restart.md`.  Exact kernel certification and
periodic-witness machinery are deferred until that embedded-map question has
a YES instance.

The repaired side partition now has an **exact**, not merely numerical,
positive closure certificate.  With class 4 normalized to 1, the other four
lengths are the unique Cramer solution of a $4\times4$ real-cyclotomic system.
A pure-`Fraction` verifier uses rational sine/cosine Taylor intervals to prove
the determinant nonzero and isolate all four positive lengths in disjoint
rational intervals.  The same verifier exhausts the nine compatible vertex
rows and certifies a chirality-balanced 12-pentagon/6-hexagon incidence
mixture.  What remains before existence is a globally consistent two-ended
edge pairing/embedded plane map; local flip marginals alone are insufficient.

The repaired local language already forces a strong periodic subsystem.
Hexagon side classes 3 and 4 occur only on hexagon sides 1 and 3, so every
hexagon has exactly two H--H neighbors.  Endpoint rows force same-chirality
same-slot contacts, hence half-turns.  Each H-component alternates the two
sides, and every two steps are a fixed nonzero translation: the H tiles form
bi-infinite periodic chains.  A full contradiction now reduces to whether
the intervening pentagon contacts synchronize chain orientations/phases.
This new restart lemma is recorded in `joint-5-6-restart.md`; it is not yet a
period of the entire tiling.
