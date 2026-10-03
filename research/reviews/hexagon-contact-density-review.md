# Hostile review: same-type contact density

**Artifact reviewed:** [hexagon-limit-and-periodicity.md](../lemmas/hexagon-limit-and-periodicity.md).

**Claim:** in an edge-to-edge, trivalent tiling by two convex hexagon types,
same-type contacts have lower Følner density (1/3).

**Verdict:** valid as a combinatorial density bound.

The dual is the triangular tessellation by the preceding combinatorial
rigidity theorem.  A two-coloring of a triangle has a monochromatic edge.
Charging one such edge from every dual face gives at least (F/2) distinct
monochromatic edges because an edge is incident to at most two faces.  In a
van Hove patch, (F=2V+O(\partial)) and (E=3V+O(\partial)), so the ratio is
at least (1/3-o(1)).  Boundary triangles only change the count by
(O(\partial)).

The conclusion concerns prototile-type labels, not placement orientations or
individual side labels.  It does not say which of the two types supplies the
contacts, does not force an infinite monochromatic component, and does not
imply periodicity.  Its sound use is to reject a compiler whose geometric
contact language permits only unlike types.
