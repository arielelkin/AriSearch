# Fresh hostile review: the 108/144 pentagon–nonagon obstruction

**Claim reviewed:** [obtuse-pentagon-nonagon-neighbour-obstruction.md](../lemmas/obtuse-pentagon-nonagon-neighbour-obstruction.md):
any convex P5 with five108-degree corners and convex Q9 with one108-degree
corner and eight144-degree corners admit no unrestricted plane tiling,
independently of lengths, rotations, reflections, and possible omitted types.

**Verdict: valid.** No mathematical defect or proof repair was found.
This review is independent of the proof's developer.

## Hypotheses and angle forcing

The Q angle sum is108+8*144=1260=(9-2)*180degrees, so the statement does not
hide an impossible polygon-angle sum. Every native angle is strictly between
90 and180. The previously independently reviewed all-obtuse lemma therefore
forces full-edge contacts and exactly three genuine corner sectors at every
vertex, including under the originally unrestricted contact convention.
Three sectors sum360 only with two108 and one144; neither all108 nor two144
works. Reflections do not change these angle facts.

No whole-native-side equality is inferred merely from a beta angle: here
full-side equality comes from the strict-all-obtuse forcing theorem. This
avoids the right-angle Cairo T-junction defect audited separately.

## Local neighbour bounds

At a P corner, if both of its side neighbours were P, the three sectors would
all be108, total324. Thus the positions of P side neighbours on the P five-cycle
are nonconsecutive. Any independent set of C5 has at most two positions, so P
has at least three Q full-edge contacts. This conclusion counts side incidences;
it does not require an unproved global simple-graph assumption.

At Q's unique108 corner, the other sectors are108 and144. A144 corner is
available only in Q. Because three sectors meet and contacts are edge-to-edge,
that144-sector Q is one of the two tiles adjacent across Q's incident full
sides. A merely point-touching Q cannot replace that full-side neighbour at a
trivalent regular polygonal vertex. Thus every Q has at least one Q side
contact and at most eight P side contacts. A single Q cannot contribute two
native corners at the same point because the polygon is simple and nondegenerate.

The extra distinct-neighbour observation is valid: if two convex interior-
disjoint tiles shared two different genuine whole sides, the convex hull of
those two segments would have positive area. Distinct supporting sides of a
genuine convex polygon do not lie on the same line, even when parallel.
The double counting itself remains valid even without this observation.

## Boundary and frequency audit

For tile-centre windows W_R, bounded diameter D and positive minimum area a
bound the number of tiles with centres in a fixed-width boundary strip byO(R):
their full tiles lie in a larger strip of areaO(R) and have disjoint interiors.
Selected centres areO(R^2) by the same area bound, and areOmega(R^2) because
their tiles cover W_(R-D). These estimates do not presuppose either type's density.

A P-Q contact counted on one selected type but not the other has a centre
within2D of the boundary. Each tile has at most nine sides, so the contact
count error isO(R), giving3N_P<=8N_Q+O(R).

For native angle counts, compare the corners on selected-centre tiles with
all vertices inside W_R: only tiles withinD of the square boundary differ.
There areO(R) such tiles and at most nine corners each. Every complete star
has two alpha and one beta. Hence5N_P+N_Q=2*(8N_Q)+O(R), or
N_P=3N_Q+O(R). This step is a tile/corner incidence count, not a claim about
convergent frequencies or positive density.

Combining gives9N_Q<=8N_Q+O(R), thenN_Q=O(R) andN_P=O(R), contradicting the
quadratic total. If either type is omitted, or hypothetically sparse, the same
identities still apply and give the same contradiction. No periodicity,
compactness, torus quotient, or exact side-length assumption is used.

## Counterexamples and scope tested

Attempted escape cases: Q neighbour only touching at a point; the same Q
counted twice around P; parallel shared side segments; non-edge-to-edge contacts;
Q sparse/absent; P absent; disconnected window patches; boundary-only alpha
corners; infinitely many orientations and reflected tiles. The existing
hypotheses and explicitO(R) errors exclude these cases as described above.
The window argument does not require a simply connected patch or Euler formula.

No defect was found. No repairs were made. The result excludes this exact
angle signature for all side lengths; it does not establish an unrestricted
convex two-tile impossibility theorem or exclude the nearby n7/n8 signatures.
