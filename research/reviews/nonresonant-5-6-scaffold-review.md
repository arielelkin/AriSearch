# Hostile review: nonresonant (5,6) angle scaffold

**Artifact reviewed:** [nonresonant-5-6-angle-scaffold.md](../searches/nonresonant-5-6-angle-scaffold.md).

**Verdict:** valid as a local necessary-condition certificate; not a tiling
and not an aperiodic candidate.  The later side-compatibility audit actually
falsifies the displayed exact shapes.

## Checks

* The pentagon and hexagon angle totals are 180 and 240 units of
  $\pi/60$, respectively.
* The minimum angle is 22 units.  Therefore at most two angles can sum to 60
  units, and exhaustive integer enumeration finds no such pair.  The
  edge-to-edge theorem applies to any realized polygons with these angles.
* Each of the six selected vertex rows sums to 120 units.  Weighted corner
  marginals are exactly 2 for each pentagon label and 1 for each hexagon
  label.  Four units of trivalent stars and one unit of 4-valent stars give
  excess valence 1, so $2D=N_5=2$.
* The edge directions are the cumulative exterior turns from the listed
  cyclic angles.  Solving two vector equations produces the displayed sine
  lengths.  All are positive; in particular the exact inequalities in the
  report show $h_1>1$.
* Against Zhu--Wang--Yan's three Reinhardt systems, the hexagon fails H1's
  angle equation, fails H2's required side equality despite meeting its
  angle equation, and fails H3's alternating-angle equation.  Under that
  unrestricted classification it cannot tile monohedrally.
* The pentagon fails a necessary angle equation for each of the fifteen
  known families: there is no three-corner or double-plus-one $360^\circ$
  sum and no $90^\circ$ or $120^\circ$ corner.  This check is insensitive to
  cyclic relabeling and reflection.  Because completeness remains
  unconfirmed, it is evidence rather than a monohedral impossibility proof.
* A classification-free argument nevertheless closes the pentagon gate.
  Nonresonance forces edge-to-edge contact, and the minimum angle bounds
  valence by five.  Exhaustion of all pentagon-only 3--5-sector sums shows
  that the $150^\circ$ corner occurs in none, so it cannot occur in any
  monohedral tiling.  Every pentagon copy contains that corner.
* A full-edge star is a connected Eulerian cycle of adjacent-side length
  symbols.  Exhaustion of all 52 partitions of the five symbols shows that
  the six weighted rows can coexist only if $u=a=b=c$.  For the displayed
  distinct values, only rows `(0,4,10)` and `(0,8,8)` are compatible, which
  omit seven labelled corners and preclude any tiling.  Coarsening to the
  required equality makes the pentagon equilateral, whose unit edge-vector
  sum has the strictly negative imaginary part proved in the report.

## Attacks that remain fatal

The certificate is only a fractional incidence solution, and the displayed
lengths prove it cannot be upgraded to a tiling.  A replacement must jointly
solve the planar map, compatible edge pairing, polygon closure, and
compactness/existence obligations.
The geometry admits additional $360^\circ$ rows recorded in the JSON, so
one may not impose only the six selected stars.  Most importantly, neither
local incidence balance nor one nonperiodic realization would prove that every
admitted tiling is nonperiodic.  Promotion to an exact candidate would be a
category error at the current stage.
