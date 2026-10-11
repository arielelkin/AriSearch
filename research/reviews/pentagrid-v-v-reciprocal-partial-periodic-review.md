# Fresh hostile review: reciprocal mirror-V partial-contact periodic theorem

Reviewed 2026-10-10 by an agent who developed neither this reciprocal family,
its placements, its producer, nor the boundary-jump proof. The reviewer had
worked on separate whole-side constructions and repeated-length hexagons.
Root supplied an earlier no-author-import fixture checker, which this fresh
review extended independently to the entire formal positive cone. Neither
checker version imports the reciprocal producer or author geometry code.

**Source reviewed:**
[pentagrid-v-v-reciprocal-partial-periodic.md](../lemmas/pentagrid-v-v-reciprocal-partial-periodic.md),
[producer](../searches/pentagrid-v-v-reciprocal-partial-periodic.py), and
[certificate](../certificates/pentagrid-v-v-reciprocal-partial-periodic.json).

**Verdict: valid for every a,k>0.** The explicit construction is a doubly
periodic tiling with two copies of each metric per lattice cell. For a!=k
it has exactly two congruence classes. The positive family is therefore
excluded as a universal-aperiodicity source. The theorem asserts existence
of this periodic tiling, not periodicity of every admitted tiling. At a=k
the two classes coincide and the same construction is monohedral.

The separate assertion that neither member has a monohedral escape when
a!=k is valid **conditional on the explicitly imported, separately reviewed
Rao classification/filter**. That external completeness theorem is not
needed for the reciprocal tiling proof, and this review does not recertify
Rao's full classification search.

## Whole-cone native geometry and all parameter strata

I reconstructed the four walks and checked all twenty native edge vectors
against their positive native lengths and direction powers. Each walk closes.
The actual before-side angles are (4,2,2,4,3)pi/5; they are not the displayed
after-side word without an index shift. Their normalized adjacent dot products
agree exactly with the cosines of those angles throughout the formal cone.

For every native side and each of its three nonincident native vertices,
the normalized supporting determinant has real positive nonzero coefficients
in a,k. The independent checker verifies all sixty such polynomials under
the explicitly selected positive-imaginary embedding of z. This proves strict
convexity, simplicity and genuine positive corners for all a,k>0, rather than
just at the author's fixtures. A1 and B1 are half-turns, so they retain positive
boundary orientation. No reflected tile is required by the displayed tiling.

The threshold identities are exactly

    r-a=phi*k-a/phi^2,
    k-f=k/phi^2-phi*a.

Thus r=a at k/a=phi^-3 and k=f at k/a=phi^3. These distinct thresholds give
all three open cases and both boundary rays. The source's positive
parameterizations cover their entire cases. In the middle case, explicitly,

    s=(phi^3*a-k)/(phi^3-phi^-3),
    t=(k-phi^-3*a)/(phi^3-phi^-3),

are positive precisely in the stated open ratio interval and recover
(a,k)=(s+t,phi^-3*s+phi^3*t). The other two open parameterizations invert
by subtracting the corresponding threshold multiple. Boundary parameters
are a>0. No real-length branch is being restricted to an algebraic fixture.

The independent checker substitutes each parameterization into every listed
positive segment length. All resulting coefficients are positive; each boundary
middle interval is exactly zero and is omitted. Consequently the ordering
and the segment pairing do not change inside an unsampled chamber.

## Boundary contacts: neither a missing side nor a forced full-D match

I checked the six full seams by both reversed endpoint equalities, with the
specified lattice shift. Their twelve native-side occurrences are all different.
The other eight occurrences were checked independently by their actual
start and end coordinates on q z^2 and J+q z^3. Together these account for
all twenty native-side occurrences once modulo the lattice.

On the first line, the two negative intervals concatenate to [0,r+a], and
the two positive intervals concatenate to exactly [0,r+a]. On the second,
both orientations concatenate to [-k-f,0]. These are identities for arbitrary
positive a,k; they do not rely on the ordering r<a versus r>a or k<f versus
k>f. The five cases determine only the physical subdivision into contacts.
Thus the boundary-chain cancellation is valid also at each coalescence ray.
The unequal D edges are not incorrectly equated as whole native sides.

Every full or partial segment has opposite supporting interior half-planes:
all native walks are counterclockwise and the matched directed segments are
opposite. Straight subdivision points have angle pi and are subdivisions
of actual unmarked polygon sides. No new prototile boundary is introduced.

The exact retained links were audited in all five strata. In each open case
there are four (2,4,4) native links and four (2,3,5) T links, in units pi/5;
the quotient counts are F=4,E=12,V=8. At either boundary there are four
(2,4,4), two (2,3,5), and one (2,2,3,3) link, with F=4,E=11,V=7.
Every circular link sums to ten units and has zero lattice holonomy.
This audit is supplementary: the global proof below does not assume that
an abstract side-pairing surface already embeds.

The wording has been clarified to state that partial native-side contacts
occur throughout **this displayed construction**. There are still two T links
at each boundary, so its genuine partial contacts persist there. No claim
that every possible tiling must contain these T contacts has been established.

## Hostile audit of the infinite-coverage argument

The independent formal checker recovers both individual area formulas and

    det(U,V)/sin(pi/5)=phi^2(a^2+4ak+k^2)
                    =(2area(A)+2area(B))/sin(pi/5)>0.

Therefore the lattice has rank two everywhere in the open positive cone.
This fact, together with finite bounded native motifs, proves local finiteness
before any plane-covering assumption is made.

The ordinary geometric torus multiplicity proof is sound. Its N is the sum
of interior indicators of all translated faces, so overlaps are counted
rather than silently identified. Oriented polygon-boundary cancellation on
the torus means the distributional derivative of N is zero. Equivalently,
a finite boundary arrangement has zero jump on every open boundary atom.
The torus is connected, and paths between complementary cells may avoid the
finite endpoints/intersections while crossing atoms transversely. Thus N is
constant almost everywhere, even if hypothetical unlisted crossings or
coincident segments occur in the initial geometric placement. The proof
never assumes their absence.

Integrating N over the torus gives the sum of the four native polygon areas,
regardless of hypothetical overlaps. Its average is one by the exact identity,
so its almost-everywhere constant is one. Any interior overlap would provide
an open set with N>=2 and is impossible. The locally finite union of closed
tile copies is closed; a hole would be open with N=0 and is likewise impossible.
This establishes disjoint interiors and full infinite plane coverage.
Boundary points are covered by the closed copies. The translates U,V preserve
the resulting tile set. No finite-patch extension inference is involved.

The zero-jump argument is stronger than sample nonoverlap evidence and is the
reason the result applies to every real positive metric in the family.

## Congruence classes, reflections and monohedral preflight

The two 72-degree corners are joined by exactly one native side. Its length
is r in A and f in B. Every isometry, including reflections, preserves that
side. Since r-f=k-a, no A/B congruence is possible if a!=k. Conversely at a=k
the native lengths agree, B's direction powers are A's powers plus one,
and the walks differ by a 36-degree rotation and translation. The half-turn
motifs do not create additional classes.

For the imported monohedral filter, rotate the before-side angle word
(4,2,2,4,3) to the filter's V=(2,2,4,3,4). If li is the outgoing side in
that filter convention, then li=L_(i+1) for these after-side native data.
Consequently the reviewed gates l1=l3 or l2=l4 become

    L2=L4 or L3=L0.

Both A gates reduce to a=k; both B gates reduce to k=a. The incoming-side
shift for reflected labels is already included in the separately reviewed
filter; it is not discarded here. The independent reciprocal checker verifies
these four exact differences, and the reviewed filter's no-producer-import
checker was replayed successfully on all450 angle-family gates.

Hence a!=k passes the conditional individual monohedral-exclusion preflight.
At a=k the monohedral escape is real and is already witnessed by this
construction. Neither a local gate calculation nor this review establishes
a new unconditional classification of monohedral pentagons. The existence
of the mixed periodic witness is independent of that imported classification.

## Actual execution and retained verification

The nondestructive producer was replayed, its standard output parsed, and
compared exactly with the retained JSON. All five strata and their links
agree. Author fixture overlap counts are 38,40,56,68,74, totaling276.

The independent checker is
[verify_reciprocal_v_partial_periodic_independent.py](verify_reciprocal_v_partial_periodic_independent.py).
The root-authored coordinate/clip checks were extended in this fresh review
with whole-cone angle/support identities, all six full seams, all eight remaining
directed line occurrences, all five interval-sign cases, individual areas and
the after-side monohedral gate differences. It imports only exact utilities
from an independently reviewed checker, never reciprocal producer code.

```text
conda run --no-capture-output -n arisearch python3 research/reviews/verify_reciprocal_v_partial_periodic_independent.py
conda run --no-capture-output -n arisearch python3 research/reviews/verify_pentagrid_monohedral_filter.py
```

Both commands pass. The independent reciprocal fixtures use a=1 and ratios
phi^-4,phi^-3,3/2,phi^3,phi^4,1. These cover all five ratio strata and the
congruent interior ratio. Their complete overlap counts are respectively
34,40,44,68,62,44, totaling292. Each count is derived from exhaustive
inverse-lattice closed-box bounds, followed by exact convex clipping;
no arbitrary translate neighborhood or floating tolerance is used.

No theorem defect was found. Arbitrary independently chosen mirror metrics,
arbitrary V/V pairs, and forcing every admitted tiling periodic remain
outside the claim.
