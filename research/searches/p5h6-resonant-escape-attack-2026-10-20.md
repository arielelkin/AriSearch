# Hostile local attack on the q=1 resonant P5/H6 metric

**Status: named split killed by forced next T contacts; no periodic witness or
global conclusion.** This is the changed metric with P sides
\((p,3/2,1,s,1/2)\), distinct from the earlier \(q=1/2\) metric whose
P-only Rao Type 2 escape is recorded elsewhere. All contacts here may be
partial and all tile images may be reflected.

## Exact metric and finite domain

In \(K=\mathbb Q(\zeta_{36})\), let \(u(d)=\zeta_{36}^{d/10}\). Solve
\(p u(0)+\tfrac32u(50)+u(150)+s u(200)+\tfrac12u(280)=0\), and set
\(L=p+1\). Solve the H closure with directions
\((0,50,100,180,230,280)\) and lengths \((L,1,1,c,1/2,e)\).
Exact replay checks the two nonsingular solves, positivity, closure and
strict convexity. Approximate values are
\((p,s,L,c,e)=(2.99292479285,3.38185574956,3.99292479285,
4.38185574956,1.38893095672)\).

For the named H0 split, the replay checks both orders and all 16
side-direction/reflection choices per order, using exact separating axes.
Exactly one nonoverlapping split exists in each order. It then checks the
two incident-edge assignments and two reflection flags for the P80 cap at
E, and the corresponding finite choices for all four P/H 100-degree
corners at the next endpoint F. This is a finite local search only.

## The next endpoint F

The P4 edge of length 1/2 ends at E inside the other P1 edge of length
3/2. The 80-degree deficit forces P vertex 2. Of its two cap images,
the one with P1 of length 3/2 along the remaining unit segment overruns
the old P1 130-degree endpoint and leaves an unfillable 50-degree gap.
The other puts P2 of length 1 exactly on that segment, reaching F with
its P vertex 3 (130 degrees) coincident with the old P vertex 1
(130 degrees). This leaves one 100-degree corner at F.

For **each** split order, eight 100-degree cap images align both exposed
rays at F and have no strict interior overlap with the existing four
tiles. Five fail at the next native endpoint by a 50-degree T gap. The
remaining three P cap images (one at P vertex 0, two at P vertex 4) each
make a 100-degree T corner on a straight P side and therefore force P80
again. The straight segment remaining after that T has length, according
to the cap image, \(s-r\), \(s-p\), or \(p-r\). Exact inequalities give

\[
s-r>3/2,\qquad 0<s-p<1,\qquad p-r>3/2.
\]

Both sides incident to P80 have lengths 1 and 3/2, with 130-degree
far corners. On a segment longer than 3/2, either P side ends in its
130-degree far corner inside the old straight side; on the segment shorter
than 1, the old 130-degree far corner lies inside the P side. Both leave
an unfillable 50-degree gap. Thus **all eight F caps fail within one more
compulsory P80 continuation**, in both split orders. The named P0+P2 H0
split cannot occur in a full plane tiling. This does not exclude other
multipiece H0 coverings.

## Whole-side H0 escapes

The exact inequalities give \(c>L\) and \(1<e<3/2\).

* For a mirrored H0/H0 full-side attachment, two H130 corners occur at
  H0 vertex 1 and leave a 100-degree cap between two length-1 H1 rays.
  Every P/H 100-degree corner has an incident side longer than 1. It
  overruns a ray's H130 far endpoint and leaves 50 degrees.
* For the half-turn H0/H0 attachment, each end leaves one 130-degree cap
  between H1 of length 1 and H5 of length e. Enumerating all 130-degree
  corners and both incident-side assignments leaves only H vertex 2,
  with H1=1 along the first ray and H2=1 along H5. Its H100 far corner
  inside H5 forces P80. The remaining H5 length e−1 is below both P80
  incident lengths 1 and 3/2, so either overrun leaves 50 degrees at H5's
  H130 far endpoint.
* H3, of length c>L, is the only different single side that can cover
  all of H0. H0 vertex 1 cannot be internal to it, since H130 plus a
  straight angle leaves 50 degrees. Aligning that vertex with an H3 end
  puts H0 vertex 0 inside H3 and forces P80 there. Its side following
  H5 has length either 1<e or 3/2>e. In the first case its P130 far
  corner ends inside H5; in the second H5's H130 far corner ends inside
  the P side. Both leave 50 degrees.

These arguments exclude the specified *single-side* H0 covers. They do
not classify arbitrary H0 partitions by multiple P/H segments, and they
do not yield a periodicity or untileability theorem for the pair.

They also exclude an H-only tiling: an H-only T contact is impossible
because every H angle is at least 100 degrees, so an H-only tiling would
be edge-to-edge; its H0 side would then need a whole-side H0/H0 mate,
already excluded in both placements.

The replay finds no P-only Rao type among all 15 imported types and ten
dihedral relabelings; this omission statement is conditional on that
classification. The full mixed problem remains open.

```text
mise exec -- conda run --no-capture-output -n arisearch sage research/searches/p5h6-resonant-escape-attack-2026-10-20.sage
```
