# Independent H0 escape attack on the offset P5/H6 pair

**Status: named split killed; no periodic witness or global verdict.**
This reviews the replacement metric in
`astra-shape-first-assessment-2026-10-20-1419.py`, including the
constructor's named P0/P2 split and its outgoing endpoint. All tilings
here allow reflections and arbitrary partial contacts. The exact replay is
`p5h6-offset-escape-attack-2026-10-20.sage`.

## Metric and angle data

Take the cyclotomic field \(K=\mathbb Q(\zeta_{36})\),
\(u(d)=\zeta_{36}^{d/10}\), and solve the two vector closures exactly as
in the assessment. The P side word is \((p,1,q,3/2,1/2)\), with angles
\((100,130,80,130,100)\); H has sides \((L,1,1,c,1/2,e)\), with angles
\((100,130,130,100,130,130)\), and \(L=p+q\). The verified strict order
needed below is

\[
0<q<1/2<1<p<e<3/2<L<c,
\]

except that the script checks the equivalent partial inequalities separately.
Numerically \((p,q,L,c,e)\approx(1.0945623,0.4787793,1.5733416,
1.9622725,1.3889310)\). In particular, **H3 is longer than H0**; it
must be considered as a possible full cover. This corrects my initial
message to the root, which overlooked it.

## Exact local exclusions

**No mirrored whole-side H0/H0 mate.** Reflect H across its H0 side while
matching the corresponding H0 endpoints. At its vertex 1,
two H corners of 130 degrees leave one 100-degree corner. The two outward
H1 rays both have length 1 and end in 130-degree H corners. Every native
100-degree corner has an incident side longer than 1: P vertex 0 has p,
P vertex 4 has 3/2, H vertex 0 has e and L, and H vertex 3 has c. That
longer side must follow one of the H1 rays. At the ray's far end, the
130-degree H corner meets a straight point of the longer side, leaving
only 50 degrees. No tile corner fits, since the minimum is 80 degrees.
This excludes this placement in any full plane tiling, without assuming
edge-to-edge contacts elsewhere.

**No half-turned whole-side H0/H0 mate.** The other opposite-interior
placement swaps the endpoints. At either seam endpoint, the H angles are
100 and 130 degrees, so the 130-degree deficit takes exactly one cap
corner between outward H1 (length 1) and H5 (length e) rays. A cap side
longer than either ray would overrun its 130-degree far H corner and leave
50 degrees; a shorter cap side with a 130-degree far corner would also
leave 50 degrees at its T contact. The exact enumeration of all P/H
130-degree corners and both incident-side assignments leaves only two
cap germs: P vertex 1 with P1=1 along H1 and P0=p along H5, or H vertex 2
with H1=1 along H1 and H2=1 along H5. The latter sides end at 100-degree
corners inside H5, forcing P vertex 2 (80 degrees) at that T contact.
The remaining H5 lengths are e-p or e-1 respectively, and exact
inequalities give \(0<e-p<q\), \(0<e-1<q\). Both sides incident to P
vertex 2 have lengths q and 1. Whichever follows the remaining H5 ray
therefore overruns H's 130-degree terminal corner, leaving 50 degrees.
Thus the half-turn placement is impossible as well. Together these cases
exclude a full H0/H0 side attachment.

**No H3 single-side full cover of H0.** The only other native side at least
as long as H0 is H3, of length c>L. If an H3 side covers H0, H0 vertex 1
cannot lie in its relative interior: H's 130-degree corner plus a straight
angle leaves 50 degrees. Thus H0 vertex 1 coincides with one H3 endpoint,
and H0 vertex 0 lies inside H3. At H0 vertex 0 the 100-degree H corner
plus a straight angle leaves exactly 80 degrees, forcing P vertex 2.
One incident side of that P corner must follow H5, whose length is e;
the two choices have lengths 1 and q, both below e. At the end of either
P side, a P 130-degree corner lies inside H5, again leaving an impossible
50-degree gap. This excludes *complete* H0 coverage by one tile side.

**The named P0+P2 split cannot extend to a plane tiling.** In either split
order, P4 of length 1/2 ends at E, the midpoint of the other P1 side of
length 1. There E is a T vertex: the old P1 edge is straight and the P4
tile contributes its 100-degree vertex 4, leaving a unique 80-degree cap,
P vertex 2. Its incident sides are P1 of length 1 and P2 of length q.
Whichever reflected or unreflected cap image fits the wedge, one of those
two sides follows the remaining length-1/2 portion of the old P1 edge.
If it is P2, exact \(q<1/2\) puts cap vertex 3 (130 degrees) inside that
straight old edge. If it is P1, \(1>1/2\) puts the old P1 endpoint,
vertex 1 (130 degrees), inside the straight cap edge. Either contact
leaves \(360-180-130=50\) degrees, below the minimum 80-degree tile
angle. Thus the two collision-free cap images in the constructor's
bounded first-step search are **dead ends at the next T vertex**. Their
initial nonoverlap cannot provide an infinite extension. This excludes
the *named split*, not every possible multipiece H0 covering.

At an interior endpoint of a side contact along H0, a terminating
130-degree corner is impossible, whereas 100 and 80 degrees can be
completed by 80 and 100 degrees respectively. The script enumerates eight
angle-and-length eligible short-side germs at H0 vertex 1 (six P, two H),
before checking their other geometry. The named P0 option is present.
These local exclusions therefore **do not force** the named P0/P2 split;
other partial attachments remain. My initial claim that P4 was forced was
wrong because a 130-degree corner may *start* a short side at H0 vertex 1
and end in a 100- or 80-degree corner inside H0.

## Monohedral omission checks

H-only tilings have no T contacts: every H angle is at least 100 degrees,
so a straight angle plus one H corner leaves less than 100 degrees for the
next corner. In an H-only edge-to-edge tiling, H vertex 0 (100 degrees)
needs two 130-degree corners linking its adjacent side lengths e and L.
The possible 130-degree incident pairs are \((L,1),(1,1),(c,1/2),
(1/2,e)\); no two form an e-to-L chain. Hence **H cannot tile alone**.

The replay also checks all 15 Rao convex-pentagon monohedral types under
dihedral relabeling and exact side equations, finding no P hit. Conditional
on the completeness and applicability of that imported classification,
P cannot tile alone. This is not an independent proof of the classification.

## Scope and replay

No mixed periodic carrier was found or excluded. No bounded negative search
is offered as evidence for aperiodicity. H0 can be partitioned by multiple
guest side segments, and the eligible short-side germs above require full
nonoverlap and continuation analysis. Plane tilability is also unproved.

```text
mise exec -- conda run --no-capture-output -n arisearch sage research/searches/p5h6-offset-escape-attack-2026-10-20.sage
```
