# Independent hostile review: interface-first pentagon Y partition

Date: 2026-10-14. Reviewer: sol_hexagons, independent of the author.
Verdict: VALID for the scoped claims in the construction record. Mixed
infinite existence and universal recognition remain unresolved. This review
certifies no aperiodic pair and no mixed-pair exclusion.

Reviewed: research/searches/pentagon-y-interface-2026-10-14.md and .py.
Independent verifier: pentagon-y-interface-2026-10-14-independent.py in this
directory. It imports no author module or certificate and derives its arm
records from the supplied polygon coordinates.

The verifier checks each strict turn, squared side length, exact interior
angle using complex numbers (1+i)/sqrt(2) and (1+2i)/sqrt(5), and areas.
The parent native word at the displayed coordinate order is a,a,b,g,g,b.
Exact rational convex clipping proves that all three children lie in H,
all pairwise intersection areas are zero, and their areas sum to H's area.
The finite closed union therefore covers H: any missing interior point
would provide a missing open region of positive area, and boundary coverage
follows by closedness. This establishes a local partition, not an extension.

The irrationality proof is valid: if theta/pi were rational, exp(2i theta)
would be a root of unity, so its sum with its inverse would be an algebraic
integer. That sum is the rational noninteger -6/5. A rational algebraic
integer must be an integer. Thus comparison in (pi/4,theta) is exact.

Omission arguments survive arbitrary partial contacts. At any native tile
vertex, the other sectors are actual corners or flat pi sectors. At most
one flat sector occurs with any actual corner. Independent enumeration finds
P-only full stars rrrr and flat corner sums rr; neither contains any a or b
corner. Every P has a and b corners, so a P-only plane covering is impossible.
Q has neither a full native star nor a native sum pi; Q-only covering is
impossible. Reflections, valence changes, and side-interior contacts do not
alter these native angle equations.

The full mixed star domain and flat domain agree independently:
rgg, aad, abg, rrrr, rrbc, rccd, bbcc; and flat+rr, flat+bc.
Reconstructed indexed arm/orientation enumeration reproduces respectively
6/6, 6/6, 6/6, 16/16, 0/0, 0/0, 12/8 length/far-end survivors. The far
c+c completion includes both bb and r+d. Omitting the latter would have
made a recognition argument unsound. The author explicitly retains it.

The intact H obstruction also survives arbitrary initial contacts. All H
angles exceed pi/2, so four native sectors exceed 2pi. A flat pi sector
cannot be completed: two native sectors already exceed the remaining pi,
and a single native sector is less than pi. Hence an H tiling would be
whole-edge and trivalent. Its only angle-legal native star is abg. The three
corner arm pairs have squared lengths (16,5),(5,8),(8,4); the unmatched 16
and 4 cannot be repaired by any orientation or reflection. Independent
indexed arm enumeration finds zero matches. Therefore no full-plane intact
H assembly exists.

Hostile alternatives: surviving child stars abg and rgg show that local Y
recognition is not forced by these tests. They do not prove any alternative
infinite assembly, and the author correctly says so. The existing general-Y
periodic-partner carrier does not directly apply: this Q has a different
native angle word. The root is independently testing a first 2P+2Q
whole-edge torus; its result is separate from this review. No large-bound
search, absence-of-small-torus extrapolation, or parent-recognition premise
is used here.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/pentagon-y-interface-2026-10-14-independent.py

Completed successfully with exact Fractions and SymPy algebra. The meaningful
stopping condition for the proposed intact-parent scheme is already met:
no intact-H plane assembly exists. Restarting requires changed cross-parent
boundaries or another parent type, rather than more copies of H. The atomic
pair may still admit a mixed covering; no conclusion about that is supplied.
