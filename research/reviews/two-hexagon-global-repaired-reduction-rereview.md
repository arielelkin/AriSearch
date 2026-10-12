# Fresh review of the repaired two-hexagon reduction

**Date:** 2026-10-11. **Verdict:** VALID for the repaired Theorem 1(d),
the metric completeness argument in Theorem 1(a), and polynomial
realisability including the distinct-shape guard. Corollary 1 and the
finite-type reduction survive these repairs. This is a mathematical
rereview by an agent who did not develop the reduction or its repair.
It is conditional on the separately reviewed defect-free-limit and
honeycomb dependencies; it is not an independent reproof of those
imported lemmas, a census-completeness certificate, a code audit, or a
review of the unrelated flux claims in Section 4.

Reviewed source:
[two-hexagon-global-sft-encoding.md](../lemmas/two-hexagon-global-sft-encoding.md).
Dependency read:
[hexagon-limit-and-periodicity.md](../lemmas/hexagon-limit-and-periodicity.md).

## Preservation of a single translation

The old inference from one period to quadratic defect replication was
invalid. The repaired proof does not use that inference. The uniform
\(O(R)\) defect estimate and the disk selection from (L1)/(L3) are applied
to the original tiling to choose defect-free disks with radii tending
to infinity. Only translations are used to recenter these disks; there
is no rescaling or rotation. Every recentered whole-plane tiling is
therefore still invariant under exactly the same nonzero vector \(t\).

This invariance is closed under local placement convergence. If a limit
tile is represented by placements \(g_n(P_q)\to g(P_q)\), then
\((g_n(P_q)+t)\to(g(P_q)+t)\). The translated tiles meet a uniformly
bounded window enlarged by \(|t|\) and the maximum tile diameter, so
placement convergence retains them as limit tiles as well. The same
argument for \(-t\) gives equality, not only inclusion, of the two limit
tile sets. Positive tile areas and bounded diameters supply the local
finiteness needed here. The separately reviewed sector-separation argument
in (L1) supplies the edge-to-edge, everywhere-trivalent limit.

The surviving physical translation induces an orientation-preserving
honeycomb automorphism. A nontranslation such automorphism has finite
order dividing six. Its sixth power would fix a geometric tile, vertex,
or edge; a nonzero physical translation cannot do so. The automorphism
is therefore translation by a nonzero lattice vector \(p\). Because
\(\langle p\rangle\) has free cell orbits, choose polygon isometries once
per orbit and extend by \(g_{z+p}=t\,g_z\). This resolves all polygon
symmetries without losing legality and produces an exactly \(p\)-periodic
symbolic labelling. Thus Theorem 1(d) holds for singly periodic original
tilings as stated. It does not assert that the original tiling had no
defects.

Together with Theorem 1(c), this gives the required equivalence for the
problem's strong quantifier: no admitted tiling has any nonzero translation
iff the nonempty SFT has no point with any nonzero symbolic period. Passing
from a one-periodic SFT point to a finite torus uses a finite-width strip
quotient and a finite one-dimensional transition graph; a legal bi-infinite
path contains a directed cycle. This does not require the original
geometric tiling to have two independent translations.

## Completeness of polygon development

The repaired proof uses finitely many tile, side, and trivalent-corner
models, with fixed positive side lengths and genuine convex corners.
Their compact prototiles have a finite collection of smaller Euclidean
charts whose closures stay inside the corresponding larger charts.
A uniform positive chart radius follows. A path taking a shortcut outside
such a chart must first cross the smaller chart boundary and hence has
length at least its Euclidean radius before exiting. Thus the chart
really contains a metric ball of uniform positive radius; local charts
alone would not have sufficed without this exit argument.

A Cauchy tail stays inside a still smaller closed disk in one chart and
converges there. This proves completeness of the glued flat surface.
Simple connectedness comes from the honeycomb topology, so applying the
complete simply connected flat-surface theorem is justified. No global
injectivity of development is assumed to prove completeness.

## Polynomial realisability and exact two classes

The strict side half-plane inequalities make the listed vertices the
actual counter-clockwise corners of a strictly convex hexagon. Positive
length variables give the exact side norms. The dot and determinant
identities therefore give the stated cosine and sine values, with
\(s>0\) selecting the interior angle in \((0,\pi)\). A triple sum lies
in \((0,3\pi)\); its complex product is \(1\) exactly when its sum is
\(2\pi\). No unwanted zero or \(4\pi\) branch occurs. Repeated corner
factors are legitimate. Boolean negations for nontriples and unequal
length classes make the type exact rather than a containment condition.

The first rereview snapshot lacked the condition that the two polygons
represent distinct congruence classes. This was a scope defect in the
word "precisely", rather than a failure of the trigonometric encoding.
It has been repaired in the source and checked in this rereview: for
each of the twelve cyclic/reversed corner matchings, at least one of
fifteen full squared distances must differ. Isometries of strictly
convex polygons preserve or reverse cyclic vertex order, and the full
squared-distance matrix determines congruence. Hence these finite
rational polynomial Boolean inequalities exclude exactly all direct
and reflected congruences. The formula now has the required
exact-two-distinct-class scope.

The finite list of types and decidable realisability formula do not
make arbitrary two-dimensional SFT emptiness decidable. Theorem 2 needs
an empty-patch or finite-torus certificate for every realisable type;
that conditional finite-certificate formulation is sound. No claim that
the current low-rank census has supplied all such certificates was
reviewed or established here.
