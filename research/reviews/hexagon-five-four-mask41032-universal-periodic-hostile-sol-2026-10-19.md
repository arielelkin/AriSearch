# Hostile Sol review: mask41032 universal periodic carrier

Date: 2026-10-19. Reviewer: fresh Sol review (not Astra).

**Verdict: PASS.** The conditional theorem holds for every closed simple strictly convex pair with the stated common native side lengths and four stated angle equations, allowing reflected copies. No further metric equality, fixed-coordinate period formula, or genericity assumption is needed.

Reviewed author artifact: `research/lemmas/hexagon-five-four-mask41032-universal-periodic-sol-2026-10-19.md`.
Reviewed producer: `research/searches/hexagon-five-four-open-metric-gate-sol-2026-10-19.py`.

## Replay and independent finite reconstruction

Ran `mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-five-four-open-metric-gate-sol-2026-10-19.py`; exit 0. The exact fixture closure, strict convexity, determinant -1/4, angle row-space checks, and standalone carrier incidence checks passed. Replay regenerates the named certificate. The author artifact was not edited.

Independently transcribed the twelve literal side pairs into a plain Python involution alpha, without importing the producer or its certificate. Walking from corner (f,j) across its preceding side gives the next corner alpha(f,j-1). This produces the cycles:

    [(0,0),(1,5),(3,5)]
    [(0,1),(3,4),(2,3)]
    [(0,2),(2,2),(1,3)]
    [(0,3),(1,2),(3,2)]
    [(0,4),(3,1),(2,0)]
    [(0,5),(2,5),(1,0)]
    [(1,1),(2,4),(3,3)]
    [(1,4),(2,1),(3,0)]

These agree with the artifact as unoriented cycles. Independently checked all 24 sides occur once and every paired native color agrees. The four native corner multisets are (a0,b0,b1), (a1,a2,b2), (a3,b3,b4), (a4,a5,b5), each occurring twice. Thus none of the eight vertices imposes a fifth angle relation. The independent reconstruction uses neither stored lattice offsets nor numerical coordinates.

## Geometry and topology audit

The reflected B indexing is consistent: stored vertex j is native vertex 5-j, stored side j is native side 4-j, and its starting corner is b_(4-j). For A, the starting corner is a_(j-1). After orienting native polygons counterclockwise, reflection plus reversing the stored order gives counterclockwise face discs. Reverse boundary identifications therefore give an orientable quotient. The connected face graph, eight circular links, twelve edges and four faces prove a closed connected orientable surface of Euler characteristic zero, hence a torus. The circular links were independently checked by an actual corner permutation, not inferred solely from Euler characteristic.

For each allowed metric, paired sides have equal positive length, so their endpoint reversing interval maps exist. Gluing Euclidean discs by these maps supplies ordinary Euclidean charts across edges. Each vertex has one circular link and total angle exactly 2pi, so its cone is an ordinary Euclidean disc. Strict convexity supplies positive sectors and valid polygon discs. The hypotheses already assume the individual polygons close; no fixture closure calculation is promoted to a universal claim.

The resulting compact length surface is complete. Its simply connected complete flat cover develops isometrically onto the whole Euclidean plane: a local isometry from a complete connected Riemannian manifold to the Euclidean plane is a covering, and the target is simply connected. This standard completeness step rules out incomplete development, overlap, and missing regions. Each lifted polygon interior is a distinct cell interior; the global isometry therefore gives disjoint tile interiors and coverage. In particular, a possible quotient-boundary identification cannot cause self-overlap of a lifted polygon: its development agrees with a rigid Euclidean copy of the original convex polygon.

Deck transformations preserve orientation and act freely, so every nonidentity one is a translation. The torus deck group is Z^2 and its action is discrete and cocompact; the translation vectors form a full rank lattice. A fundamental cell has the four original face interiors, with total area 2 area(A)+2 area(B). This proves two independent periods and the claimed multiplicities. No separate translation-holonomy constraint is needed: compact nonsingular flat torus geometry supplies it.

## Scope and limitations

The producer finite checks alone are not a universal geometry proof; the development argument in the artifact supplies that proof. The exact fixture and its determinant are ancillary and are not required for the universal implication. The mask row-space replay identifies precisely the four required triple identities. A larger support containing those identities inherits this conditional conclusion. Nothing reviewed proves realizability of arbitrary formal angle data, a classification of mask33416, or a solution of the unrestricted two-convex-tile problem. No blocking defect found.
