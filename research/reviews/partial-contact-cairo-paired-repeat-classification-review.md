# Fresh hostile audit of paired-repeat Cairo monohedral classification

**Reviewer:** branching_hexagons, freshly assigned by root. The reviewer did not develop the classification or carrier and independently reconstructed its native positive geometry before author extraction. The actual extracted lemma, producer and certificate were then read. No author code was executed or imported.

**Artifact:** [paired-repeat classification](../lemmas/partial-contact-cairo-paired-repeat-classification.md).
**Verdict:** **VALID** for the stated strictly convex Cairo monohedral stratum, all isometries and original arbitrary contacts. The iff statement and both positive branches are supported; no substantive flaw or required repair was found. This is not an arbitrary two-species theorem.

## Generic obstruction under unrestricted contacts

For arms(a,b,b,a) with a!=b there are exactly four native90-corner slots. Every equal-perpendicular pairing is one of six unordered pairs with repetition. A perpendicular arm of length a always has its other bank arm b, whether native slot a or d is used; a perpendicular b always has bank a, whether slot b or c is used. Thus every right-corner event has equal banks and total2b or2a. Reflection, rotation, intrinsic symmetries and using different equal-length native slots add no unequal-bank event.

The reviewed two-T invariant applies to every unequal arm/arm contact from a120 star, not merely edge-to-edge contacts. An arm hosting a T would create such an unequal opposing native arm at its120 endpoint: the opposing bank's120 endpoint must coincide with that endpoint, since a120 corner cannot occur in a side interior. The two switch events would have different bank values a,b but equal totals2a,2b, impossible for a!=b. Consequently native arms cannot host T points. Equal arm/arm contacts are full native matches, since both endpoints have types90,120.

An e-hosted T must have its length equal to one of the complete event totals2a,2b. Since e=wb-a and a,b>0,w<2, e-2b=(w-2)b-a<0. Away from e=2a there is no T anywhere. Cairo angles have only native full stars90^4 or120^3 and half stars90^2, so all remaining contacts are full native seams. Any e side is therefore whole-matched to another e: a native arm cannot mate e even if their lengths happen to agree, because its90 endpoint would coincide with an e120 endpoint.

At both endpoints of an e/e seam, regardless of its two physical placements, the two remaining exposed arms are native a or d, both length a. The third sector is120. It cannot use an e-adjacent corner because that would require the prohibited full e/arm match. Its isolated corner has two arms b,b, so it cannot fill the two whole a rays when a!=b. This proves untileability at every metric outside the two stated cases. There is no omitted monohedral species case, contact subdivision, special e=arm metric, or chirality restriction.

## Both positive branches

For a=b all four arms agree and e=(w-1)a>0. The separately reviewed swapped-arm cone allows its shapes to coincide; substituting a=c=d=D in that cone gives both words(a,a,a,a,(w-1)a). Its constructive full-plane proof remains valid on the equality boundaries, and thus directly supplies a monohedral periodic witness. No imported pentagon classification is needed.

For e=2a, positive Cairo closure gives b=wa. Normalize a=1. The reviewer reconstructs P's native vertices and all five lengths(1,w,w,1,2), checking every nonincident support determinant. Its area is2w. The three rotations about its isolated120 corner are exact whole P copies. Every vertex lies in the stated centered regular hexagon of side2; all three polygons have total area6w, equal to the hexagon. Interior disjointness is independently verified below, proving an actual dissection rather than relying on a drawing or corner sums.

The lattice vectors(3,w),(0,2w) have determinant6w. To avoid relying on the author's inverse-lattice pruning, the reviewer uses a different complete overlap bound. The full three-face motif has x span4 and y span2w. An overlap after translation m*(3,w)+n*(0,2w) requires |3m|<=4 and |m+2n|<=2. Hence integer indices satisfy |m|<=1,|n|<=1. This rectangle contains every possible overlap, including motif contacts and self translations.

All nine lattice indices and nine ordered primitive-face pairs are independently tested, excluding only the three identical zero-shift occurrences:78 complete comparisons. Exact convex half-plane clipping gives intersection area zero in every case. Thus every original polygon occurrence has interior disjoint from every other lattice occurrence. The author's narrower28-pair inverse-lattice bounding ranges are also mathematically complete and are contained in this independently checked larger domain.

Area per motif equals lattice covolume6w, so periodic multiplicity at most1 has mean1 and is1 almost everywhere. The full closed polygon union is locally finite because the lattice is discrete. A missing point would therefore have a missing open neighborhood of positive area, impossible. This supplies a whole-plane tiling and two actual nonzero independent translational periods. Scaling gives all b=wa metrics.

## Independent exact replay and certificate

[Independent checker](verify_partial_contact_cairo_symmetric_monohedral_independent.py) uses Q(sqrt3) with an explicit positive algebraic embedding, no author imports, no solver, and no numerical tolerance. It independently checks the six generic native events, closure/e inequalities, all-equal cone substitution, the positive native pentagon, exact threefold rotations, regular-hexagon containment/area, all78 complete lattice-pair intersections, and exact coordinate/period/native-length agreement with the retained author certificate.

    conda run --no-capture-output -n arisearch python research/reviews/verify_partial_contact_cairo_symmetric_monohedral_independent.py

Completed output: PASS. The verification does not rely on finite extension, failed searches or a polygon classification theorem.

## Scope

The reviewed result is precisely that a strictly convex Cairo pentagon with arms(a,b,b,a) admits an unrestricted monohedral tiling iff a=b or b=sqrt3*a, with a periodic witness in either case. It does not classify pairs containing individually untileable members and does not resolve the original two-convex-polygon problem. The separate master monohedral equality-pattern extraction was not assigned for this audit and is not silently certified by it.
