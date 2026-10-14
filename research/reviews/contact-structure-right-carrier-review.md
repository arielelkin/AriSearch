# Independent hostile review: right-angle pentagon/octagon carrier

Date: 2026-10-13. Verdict: **valid** for the explicit shapes and placements.

Reviewed `research/lemmas/contact-structure-right-pentagon-octagon-periodic-carrier.md`. Independent verifier: `research/reviews/contact-structure-right-carrier-independent-check.py`; no author imports.

## Exact geometry

The checker uses the exact quadratic field Q(r), r^2=2, with its explicitly positive real embedding into Sage's exact algebraic real field. It verifies all convex turns, Q squared edge length 4, Q turning angles 45 degrees, P right turn at indexed corner2, and its remaining turning-angle squared cosine (2-r)/4. Thus Q has angles135 and P has90,112.5,112.5,112.5,112.5. Areas Q=8+8r and P=3+r agree exactly.

## Independent packing and entire-plane covering

I independently normalize the three fundamental representatives Q, P+(a,0), J(P)+(a+1,a), with lattice vectors v=(2a+1,a), w=(0,2a). Their total area is exactly det(v,w)=14+10r.

For each ordered pair of representatives, transform all vertices into the lattice coordinate basis. If interiors of one polygon and an integer lattice translate of the other intersect, each integer translation coefficient lies within the coordinate ranges of their difference polygon. Exact algebraic ceil/floor gives a finite, exhaustive set of potentially intersecting translations. The verifier checks all22nonidentity candidates by exact separating axes; all are interior-disjoint. This establishes packing of all three infinite lattice orbits, including cross-column and reflected-P contacts.

On the fundamental lattice torus, this locally finite closed packing has total area equal to the torus area. A missing point would have an open neighborhood outside the packing and hence positive missing area, a contradiction. Thus the verified infinite packing covers the whole plane. This independently establishes the author's global covering assertion without relying only on numerical area agreement or finite-patch extension.

## Native contact and monohedral audit

The stated seam ordering and exact channel polygons are consistent with the coordinates; no additional congruence classes appear. The angle palette in units22.5 is P90=4,P112.5=5,Q135=6. Integer solutions summing16are exactly4+4+4+4,5+5+6,4+6+6; the flat-side sum8is exactly4+4. Consequently no P112.5 corner can be covered in a monohedral P tiling (full or hosted-flat). Q cannot tile monohedrally by the reviewed convex side-count theorem. Reflections are allowed by the target, so J(P) is legal.

No defect was found. The metric-specific periodic carrier does not classify arbitrary polygons with this angle palette or imply periodicity for their admitted tilings.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/contact-structure-right-carrier-independent-check.py
