# Independent hostile review: pentagon/heptagon first gate

Reviewed 2026-10-19: `research-problem.md`, the first-gate Markdown report,
Python producer, and JSON coefficient certificate. Verdict: **passes within
its explicitly restricted scope; no solution of the research problem**.
No substantive mathematical error found.

## Independent replay

Command (run successfully):

```
mise exec -- conda run --no-capture-output -n arisearch python research/reviews/pentagon-heptagon-first-gate-sol-independent-2026-10-19.py
```

The independent verifier reads the certificate without importing or executing
the producer. It regenerates the full angle census using combinations with
replacement, checks exact support incidences and edge vectors in the stated
cyclotomic field, checks normal gaps and angle words, and enumerates all
10,395 pairings with a bitmask recurrence for both relative chiralities.
Output: `PASS: 12 stars, exact support incidences and edge vectors,
strict-convex support gaps, 10395 pairings in both chiralities`.
The verifier does not certify plane existence, motif extension, or larger
period domains. Positivity follows analytically from the angle gaps and
support construction; polynomial residues alone would not certify signs.

## Attacks checked

* **Full contacts:** at most six genuine corners can meet because their
  minimum angle is 60. One flat host leaves angle 180 and produces precisely
  AF or AAA. Two flats exhaust the full angle and cannot have genuine corners.
  The ten full stars and two flat-host stars in the report are exhaustive.
  Indexed expansion permits repetitions from different tile copies, arbitrary
  cyclic orders and reversals. This is angular feasibility only. Every finite
  star embeds near its center because each convex tile lies in its own corner
  sector (and a host in its half-plane). Endpoint compatibility is unproved.
* **Exact shapes:** the normal gaps are the exterior angles, strictly between
  zero and 180, with total 360. The consecutive tangent-line intersections
  therefore define bounded strictly convex polygons circumscribing the unit
  disk. Independent exact checks confirm both endpoints of every native edge
  lie on its support and have the certified directed edge vector. The positive
  tangent-sum formula gives the lengths. The three-sector motif follows from
  convexity; it is not evidence of an infinite tiling.
* **Monohedral P:** among stars using only P, a C corner occurs only in AACD;
  it cannot meet a flat host. Distinct C stars demand two A incidences each,
  and each tile supplies only one A. The incidence deficit is linear in the
  number of tiles and hence quadratic in disk radius, while crossing tiles
  lie in a bounded-width annulus and contribute only O(R). Reflections and
  partial contacts do not evade this count. Q is excluded because a G corner
  has no Q-only full or flat star.
* **Frequencies:** checked each coefficient against the census. Subtracting
  the B and E equations gives 2d=0, hence e=q. The A equation gives p>=q.
  Writing S=p-q, one has g+h<=S/2 and
  5q>=2p-(g+h)>=3p/2+q/2, so p<=3q. The reported p=2,q=1
  nonnegative vector satisfies all six equations. At p=q the extra densities
  vanish and a=b=c=e=q follows. The report correctly does not infer literal
  absence from zero density in arbitrary tilings. In a periodic tiling any
  occurrence repeats with positive density. Subsequence densities exist
  because bounded area and diameter bound all incidence counts per area;
  disk boundary errors are O(R). No density assumption beyond taking such a
  subsequence is needed.
* **One-P/one-Q torus:** in a translational quotient a P-P seam would join
  different sides of the same representative by translation, requiring
  antiparallel directed sides. P has none; mirroring or rotating the whole
  representative preserves that fact. Thus every P side must join Q. All Q
  side directions lie in a single residue modulo 30 after any isometry;
  the 75-degree difference between the first two P directions prevents this.
  Reflecting Q changes sign and can reverse boundary convention, with the
  latter absorbed by a common 180-degree phase. Independent exhaustive
  pairings confirm zero survivors for both signs. A translation cannot
  modify direction. The argument excludes whole native edge pairings with
  exactly one representative of each type; subdivisions and larger domains
  remain completely outside its conclusion.

## Remaining research gap

There is no infinite mixed tiling certificate and no exclusion of arbitrary
mixed tilings. These are local exact shapes and a small-period exclusion.
Neither aperiodicity nor impossibility of the pair follows. The report
states this limitation correctly and makes no novelty claim requiring a
literature audit. No discovery-log changes were made by this reviewer.
