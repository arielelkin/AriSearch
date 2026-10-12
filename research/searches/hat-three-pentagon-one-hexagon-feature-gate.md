# Changed hat cut: convex feature exists, two-class metric gate fails

Date: 2026-10-12. Status: [independently reviewed VALID scoped exclusion](../reviews/hat-three-pentagon-one-hexagon-review.md).
This covers the specified cut and parameter domain, not arbitrary hat partitions.

This changes the previous horizontal four-pentagon cut. Normalize the hat
outline to `Tile(1,b)`, with `b>0`, and let its exact vertices `h0,...,h12`
be those retained in the companion certificate. Move the internal point
freely to `V=(u,v)` and use the four boundary words

* `P6=[h0,h1,h2,h3,h4]`;
* `P9=[h0,h4,V,h11,h12]`;
* `P48=[h4,h5,h6,h7,h8,V]`;
* `P192=[V,h8,h9,h10,h11]`.

The new feature is a genuine hexagon at P48, together with three
pentagons. At `(b,u,v)=(sqrt3,2,-sqrt3/10)` every nonincident vertex lies
strictly inside every supporting halfplane of its piece. All six pairwise
intersection areas vanish and cancellation of internal edges gives
exactly the source outline. Thus a valid strictly convex partition exists.
These strict inequalities persist in an open neighborhood. This statement
is local source geometry; it makes no unrestricted recognition claim.

For at most two congruence classes, all three pentagons must be congruent:
a strict hexagon cannot be congruent to a strict pentagon. A side inventory
already reduces the necessary metric conditions to a finite exact gate.
Write `L²=b²−3sqrt3 b+9`. The P6 side multiset is
`{b,1,2,1,L}`. P192 has two fixed sides of length b, so P6 must also contain
at least two occurrences of b. Consequently `b=1`, `b=2`, or `L=b`;
the last equation gives `b=sqrt3`. This includes all coincidences and
both orientations, without choosing a vertex correspondence.

P9 has the fixed sides L,1,b. Subtracting these occurrences from the P6
multiset leaves `{1,2}`, so its two remaining sides necessarily satisfy

    { |V−h4|², |V−h11|² } = {1,4}.

For each of the three b values this is two circle systems, six in total.
The circles are centered at

    h4=(3−sqrt3 b/2,−b/2), h11=(1,b).

Their exact real intersections number four at b=1, zero at b=2, and four
at b=sqrt3. Every intersection violates a strict supporting inequality
of at least one of the four proposed pieces. The certificate retains
every intersection, its exact algebraic minimal polynomials, and the
failed signed supporting determinants. In particular the old horizontal
point `(sqrt3,2,0)` satisfies full pentagon congruence but makes the new
hexagon flat at h8. The companion program solves the six systems over
the exact algebraic real field, checks every signed inequality, and also
checks all cyclic/reflected full squared-distance correspondences.

Therefore the changed partition has a nonempty strict convexity domain,
but **no point in that domain has at most two congruence classes**. The
weaker necessary side inventory alone suffices for this exclusion; a
larger congruence-ideal enumeration is unnecessary. This excludes this
specific four-piece source compiler, including reflections, not other
cuts, other sources, or arbitrary convex polygon pairs.

Artifacts:

* [Exact gate](hat-three-pentagon-one-hexagon-feature-gate.py).
* [Certificate](../certificates/hat-three-pentagon-one-hexagon-feature-gate.json).

Replay:

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python3 research/searches/hat-three-pentagon-one-hexagon-feature-gate.py --output /tmp/hat-three-pentagon-one-hexagon-replay.json

This failed finite compiler supplies neither a new plane tiling nor an
unrestricted forcing route. The broader construction objective remains
open and needs a different geometric feature.
