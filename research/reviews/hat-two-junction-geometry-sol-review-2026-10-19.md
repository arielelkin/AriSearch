# Independent Sol hostile review: repaired Hat two-junction geometry gate

Date: 2026-10-19

Verdict: PASS for the stated restricted-topology exclusion. No material defect found. This supersedes the original incidence review's failure only for the corrected boundary-flat enumeration and its geometric follow-up; the earlier FAIL remains an accurate review of the original artifact.

## Scope and evidence

Inspected the corrected incidence and geometry reports and Python producers, both retained certificates, the prior `hat-two-junction-incidence-sol-review-2026-10-19.md`, and the exact `hat_outline` source certificate. Independently recomputed outline turns using Fraction arithmetic, recovering reflex indices 0,4,8,11. Built the two tree adjacency graphs independently, recursively recovered the four leaf-to-leaf face paths, and enumerated all 2592 flat assignments from those paths. The resulting survivor sets exactly equal the incidence certificate: 32 and zero. Replayed the exact geometry producer with its certificate write replaced by an equality assertion, normalizing Python tuples through JSON. The full output matched the retained certificate: 11 SAT base systems, 21 UNSAT base systems, and UNSAT congruence extensions for all 11 SAT systems. No author certificate was overwritten.

## Completeness attacks

A four-leaf tree with two interior trivalent vertices has a central edge and two leaves attached to each junction. Alternating pairing 02|13 cannot embed in the disk. The other two pairings are exhaustive up to names of junctions. Face walks follow the boundary arc and unique tree path. This independently yields nominal counts (6,7,5,5) and (7,6,6,4). The latter cannot supply four pentagons/hexagons because its four-sided face cannot gain corners through flat deletion.

Boundary leaves now have all three permitted states: no flat, or flat in either incident face. Interior junctions have all four states. Positive face angles and the angle sum allow at most one flat at each node. Every original convex boundary corner remains a genuine corner. Consecutive flats do not invalidate the count: in a genuine convex polygon each deleted collinear intermediate vertex reduces the side count by one. Geometry rules out unrealizable assignments. No omitted boundary-flat mechanism was found.

## Geometry and congruence attacks

The outline parser retains exact rational coefficients in coordinates (x,sqrt(3)y); its assertion verifies the other quadratic-field coefficients vanish. Positive vertical scaling preserves orientation. The four walks and their junction labels match the graph paths. Each actual dissection satisfies every encoded halfplane, turn and nonzero-edge condition. These constraints may admit relaxed configurations without explicitly requiring the junctions to lie inside the Hat, but that enlarges the feasible set and does not weaken an UNSAT exclusion. Their necessity is sufficient for the conclusion. All assigned flat turns are equalities; every other turn is strict. The flat constraints therefore do not silently discard boundary-flat cases or reverse-ray ambiguities in actual convex sectors.

After deleting precisely the assigned flats, a polygon congruence must map extreme vertices in cyclic order or reverse cyclic order. All shifts and both directions are present. Equality of every pairwise distance is sufficient for an isometry, and the metric uses the required factor 3 on the scaled y difference. There is no restriction to translations, direct isometries, equal orientation, or a chosen first vertex. Unequal vertex counts cannot be congruent. The six masks 1 through 6 plus the separately included zero mask give all seven unordered nonempty bipartitions with sector zero anchoring one class. Pairwise congruence inside each part expresses at most two classes and includes the all-congruent case.

## Solver status and limits

The retained certificate has no unknown result. The reviewed final producer also explicitly asserts each base result belongs to SAT/UNSAT before emitting COMPLETE; it already requires every SAT branch's congruence result to equal UNSAT. The calculation is exact polynomial real arithmetic with no finite coordinate grid or timeout. The strict-boundary witnesses use rational scaled y coordinates, consistently with the metric and certificate.

This is a solver-backed finite exclusion, not an independently extracted algebraic UNSAT proof. The replay shares the producer's constraint implementation and Z3; the independent parts are the graph/flat enumeration and mathematical audit of constraint necessity and congruence completeness. No claim is established about other endpoint choices, additional junctions, arbitrary cuts, plane tilings, or aperiodicity. Within the explicit domain, the exclusion is supported and the branch can close.
