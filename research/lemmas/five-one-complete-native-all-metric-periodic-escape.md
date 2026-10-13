# Complete B5+1 resonance line: no aperiodic pair at any native order or metric

Date: 2026-10-13. Status: [independent whole-synthesis review VALID](../reviews/five-one-complete-native-all-metric-synthesis-review.md). Restricted-family theorem, not the unrestricted two-convex-tile
problem.

## Theorem

Let 108 < x < 126, x != 120, in degrees, and define

    y=720-5x, z=4x-360, r=360-2x, s=360-2y.

Let A and B be actual strictly convex hexagons with angle multisets

    A: two copies each of x,y,z;
    B: five copies of r and one copy of s.

All cyclic native orders, positive actual closed polygon metrics, side-length
equalities, rotations and reflections are permitted. If the pair admits any
plane tiling with unrestricted contacts, then it admits a plane tiling with
a nonzero translational symmetry. Either species may be omitted.

Thus no pair in this entire angle-line family is aperiodic. This is an
existential periodic escape; it does not say that every admitted tiling is
periodic. Other angle multiplicities, lines, and general pentagon pairs are
outside the theorem. The equal-angle point x=120 and degenerate endpoints
are excluded.

## Domain and complete native split

The five angles have slopes (1,-5,4,-2,10) and all equal 120 at x=120.
Their simultaneous strict convexity interval is exactly (108,126).
For x!=120 their complete trivalent star language is

    AAA(x,y,z), AAB(x,x,r), AAB(y,y,s), ABB(z,r,r).

The [full-domain review](../reviews/five-one-full-strict-convex-angle-line-extension-review.md)
checks these identities and the applicability of the nine earlier native
coverage proofs, including the part of the interval with acute A angles.
It does not claim original tilings are trivalent: the defect-free limit
is used first.

B has one cyclic order up to rotation/reflection. A has exactly eleven
fixed-colour native bracelets. The complete palette enumeration in
[the saturation theorem](terra-five-one-b-saturated-chain-reduction.md)
and its [exact checker](../reviews/verify_terra_five_one_b_chain_palette.py)
includes precisely the following disjoint cases.

| Native A orders | Result used |
| --- | --- |
| 001221, 011022 | No saturated B mask is compatible; pure-A periodic escape |
| 002112, 012012, 012102 | All-metric boundary interface forces alternating rows; binary periodic lift |
| 001212, 011202 | Boundary resource contradiction excludes every saturated mixed field |
| 010212, 012021 | Empty boundary interface and compulsory AAA contradict every saturated mixed field |
| 001122 | Used AA22 forces H2 or impossible positive closure; unused AA22 has support-based periodic lift |
| 010122 | Every used AA22 case forces H1/H2; unused AA22 has the same support-based lift |

Colours are fixed by the displayed parameterization. No arbitrary permutation
of x,y,z is applied to claim coverage on the same B5+1 line.

## Proof for original unrestricted tilings

Suppose a tiling exists. The reviewed
[hexagon limit](hexagon-limit-and-periodicity.md) supplies a whole-side
trivalent field of the same fixed actual polygons. The reviewed
[saturation extraction](terra-five-one-b-saturated-chain-reduction.md),
with its full-interval scope extension, then supplies either a pure-A
field or a mixed field T in which every B has exactly two B neighbours.
A pure-B trivalent field is impossible because BBB is absent. A pure-A
field admits a periodic monohedral tiling by the named unrestricted
convex-hexagon classification imported in the limit theorem. It remains
to treat mixed T.

The first nine orders are covered by the following separately reviewed
theorems, using the full-interval scope review above:

- The two palette exclusions in the saturation theorem.
- [Three native interface escapes](five-one-three-native-word-all-metric-interface-escape.md).
- [A001212 resource exclusion](terra-five-one-001212-universal-boundary-exclusion.md)
  and [its independent review](../reviews/terra-five-one-001212-universal-boundary-fresh-hostile-review.md).
- [A011202 resource exclusion](terra-five-one-011202-universal-boundary-exclusion.md)
  and [its independent review](../reviews/terra-five-one-011202-universal-boundary-fresh-hostile-review.md).
- [A010212 interface exclusion](five-one-010212-all-metric-interface-escape.md)
  and [A012021 interface exclusion](five-one-012021-all-metric-interface-escape.md),
  with [their independent review](../reviews/terra-five-one-010212-012021-fresh-hostile-review.md).

For either of the two remaining words, native A side 4 has endpoints z,z.
Use a dichotomy in the ACTUAL saturated field T.

If even one such side meets A, both endpoints must be AAAxyz, since neither
two-A star contains z. For
[A001122](terra-five-one-001122-full-cross-22-escape.md), the complete
two-ended native classification and exact positive-closure separator give
a sufficient H2 monohedral periodic escape. For
[A010122](terra-five-one-010122-full-cross-22-escape.md), all two-ended
patterns already imply sufficient H1 or H2. Reflections and all actual
side-equality partitions are retained in both classifications. The mixed
field need not be extended from these local patterns: it already exists,
and the sufficient monohedral criterion constructs the escape separately.

Otherwise every A side 4 meets B. The
[unused-AA22 support theorem](five-one-all-mask-no-cross-periodic-escape.md)
applies without any metric noncollision assumption. It counts unused
resources to obtain U+2M=O(R), where U counts AAA stars and M middle-mask
B tiles, and takes a support-preserving limit containing neither. Opposite
marked AB seams force a periodic species pattern. Actual B closure reduces
every residual native fibre to at most two states; all constraints become
equalities of maps of bits. The reviewed binary finite-cover theorem and
actual polygon development then construct a periodic plane tiling.

The dichotomy is exhaustive even when side lengths permit a cross match
which T never uses. It is not a split into open metric strata. Consequently
the two residual orders also admit a periodic escape whenever tileable,
and all eleven orders are covered. QED.

## Evidence, review, and limits

The proof imports the reviewed sparse extraction, saturation, binary
finite-cover, and actual development theorems; it does not silently replace
them with finite experiments. New proof-relevant finite domains are:

- A001122 used seam: 96 two-ended cases and all 203 six-side partitions;
  the sole non-H2 partition has no positive closure.
- A010122 used seam: 96 two-ended cases and all 203 partitions; all 71
  compatible partitions satisfy H1/H2.
- Unused support: two native words, two species phases, eight representative
  cells each, with all twelve native placements and the exact B closure
  identity.

Independent component reviews and the linked whole-synthesis review are
VALID; this is reviewed coverage of the stated family. The full replay validates its
registered finite evidence, not mathematical completeness by itself.
No radius, timeout, numerical sample, unproved chain-periodicity principle,
or inferred global extension enters this synthesis.

No novelty claim is made; the periodic monohedral criteria and unrestricted
monohedral classification are imported dependencies. The original research
problem remains unresolved.
