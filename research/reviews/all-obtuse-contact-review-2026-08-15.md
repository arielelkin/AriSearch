# Hostile review: all-obtuse hexagon contact reduction

**Reviewer:** independent subagent `review_obtuse`

**Artifact reviewed:** `research/lemmas/all-obtuse-hexagon-contact-reduction.md`
as initially extracted on 2026-08-15.

## Exact claim reviewed

Every unrestricted tiling by a finite set of strictly convex hexagons whose
angles lie in `(pi/2,pi)` is full-edge-to-full-edge, trivalent, and abstractly
the standard `{6,3}` honeycomb.

## Assumptions checked and attacks attempted

The review checked reflections, T-junctions, shorter or longer neighboring
sides, accumulating neighbor changes, multiple contacts, nonstandard planar
hexangulations, quotient surfaces, and finite-length paths grazing vertices
while crossing infinitely many cells.

## Defects found

Claims excluding T-junctions, forcing full-side pairing, and forcing exactly
three corners survived. The original completeness inference did not:
crossing infinitely many triangles does not impose a uniform positive length
cost because a path may cross arbitrarily close to vertices. Local finiteness
also needed an explicit packing argument using both minimum inradius and
maximum diameter.

## Repair proposed

Use the uniform regular triangulation and prove that a fixed-radius
neighborhood of a triangle lies in a finite closed star. A Cauchy tail then
lies in a compact finite subcomplex, proving completeness. Expand the
local-finiteness packing argument.

## Remaining uncertainty

The repaired uniform-neighborhood argument and the developing-map conclusion
require fresh independent review. “Standard honeycomb” must mean cell-complex
isomorphism induced by the developed regular-hexagon tiling.

## Verdict

**Unresolved as initially written.** Claims 1–3 appeared valid; claim 4 had a
repairable proof gap. No counterexample to the theorem itself was found.
