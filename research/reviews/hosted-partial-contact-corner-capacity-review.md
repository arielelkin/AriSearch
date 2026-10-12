# Independent review: hosted partial-contact corner capacity

Reviewed: [root general theorem](../lemmas/hosted-partial-contact-corner-capacity-obstruction.md).
Verdict: valid as stated, including arbitrary isometries, partial contacts
and the finite-window argument. No invariant-measure assumption is needed.

For two fixed compact convex polygons, positive inscribed radii and bounded
diameter imply local finiteness by disk packing. They also give a uniform
bound on neighbours and contact vertices per tile: any contacting tile's
inscribed-disk centre lies in a fixed-radius neighbourhood of the first
tile. Thus the stated O(R) annular error remains valid without finite local
complexity, and arbitrary choices of one host point per tile suffice.

A single convex neighbour covering the full relative interior of the
longest side must supply a collinear straight side of at least that length.
Strict convexity prevents replacing it by a bent chain of native sides.
The strict maximum leaves only the equal designated side, whose full
pairing is excluded. Hence an interior contact junction really exists.
If a single neighbour continued across that junction as a flat sector,
the host and neighbour already fill360 and no positive native corner
could occur; the selected native junction cannot have that form.

Each selected flat host has a distinct native c and d resource. Selected
hosts cannot coincide, because two flat sectors exhaust360. The B-f stars
are distinct under the at-most-one-f condition, cannot be flat, and use
additional c corners disjoint from the hosted resources. Consequently all
three finite-window resource inequalities are genuine injections with
bounded displacement, not just formal angle balances.

Combining them gives b_R=O(R), then a_R=O(R), contradicting area coverage
Omega(R²). The proof excludes sparse exceptional species as well. For the
application, the complete joint census independently contains only the
stated native180 star and only the stated B144.5 full star. The metric
maximum is essential: replacing the sample by a longer B side would remove
the argument that every A designated side hosts an interior junction.
The root states this limitation explicitly. No correction needed.
