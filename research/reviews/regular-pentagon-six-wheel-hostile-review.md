# Fresh hostile review: regular-pentagon wheel palette and plane family

Date: 2026-10-13. Independent reviewer: contact_structure.
Artifacts: [finite wheel and potential](../lemmas/regular-pentagon-six-wheel-potential-obstruction.md),
[full plane-family obstruction](../lemmas/regular-pentagon-six-wheel-plane-obstruction.md),
[exact producer](../searches/regular-pentagon-six-wheel-exact.py).
Verdict: VALID. The requested explicit positive square-basis orientation
assertion has been added to the producer and plane proof and independently
checked. No unresolved finding remains.

## Exact first image and finite potential

The six stated faces are convex and contained in the regular parent because
all vertices are inside it. Exact pairwise clipping disjointness and area
conservation then prove its partition. The radius identity rho*cos36=phi to
power minus2 gives the stated phi squared inflation and phi fourth area.
The producer replay passed all supports,15pair intersections, angles and
area identities. This is one native finite image, not a plane existence proof.

The palette equations in18-degree units have exactly the stated full stars
(108,126,126),(90 repeated4) and flat star(90,90). I independently checked
the complete min-angle-bounded domains. Every native star has zero score
for108->1,126->-1/2,90->0. Parent side subdivisions have90+90 zero score,
and parent native corners below180 cannot split into two child angles at
least90; they retain precisely one child corner with the parent angle.
Thus the sum of all child weights is the parent weight, giving exactly one
P child in a P image and zero P children in a Q image. This holds for every
finite dissection and any child count, not merely a proposed seven-child
wheel. The count matrix [[1,1],[5,6]] is consequently impossible regardless
of metric or seam topology; the real first image alone remains valid.

## Complete Q-only local obstruction

For0<rho<1 all five side lengths L,Rlen,C,Rlen,L are positive; angle directions
are fixed and convex. C<2L follows exactly from rho*cos36<1. Native108/126
corners cannot lie inside another side. A right-angle flat cap therefore has
whole equal perpendicular legs, since an unequal far endpoint would be a
nonright flat corner. If L!=Rlen, an L-L perpendicular cap ends in108+108,
which belongs to no full or flat star. An Rlen-Rlen cap is the sole remaining
case, with along-host length L on both sides.

A C-hosted cap would have to cover the entire C side by two complete guest
legs, because neither host126 endpoint nor a guest nonright endpoint can be
flat. It would require C=2L even at L=Rlen, contrary to C<2L. Hence each C
side matches one whole Q side. Every non-C Q side has a right endpoint,
which cannot occur together with a host126 at a full star; the match is C-C.
Its126+126 endpoints force a third108 corner and Rlen/L side contacts.
For Rlen<L, the shorter endpoint creates an L-L perpendicular cap with
forbidden108+108 far vertex. For L<Rlen, the Rlen-Rlen cap forces another108
guest and a C/L contact. Each comparison is excluded: shorter C ends126
inside a side, longer C hosts a forbidden cap, equal C/L ends126+90 in an
impossible star. This checks every length branch, including C=2Rlen; a
locally nonoverlapping swapped cap cannot escape the far endpoint rule.
Thus Q alone cannot tile when Rlen!=L.

## Transfer to unrestricted P/Q plane tilings

Grouping all native weights by geometric position in any square gives zero,
since full and flat stars all have zero total. Replacing position selection
by whole tile-centroid selection changes only O(radius) bounded-strip terms.
Q total score is zero and P score five, so P counts are uniformly O(radius).
If P were present in every disk of a fixed radius, separated disk counting
would contradict this linear count. Arbitrarily large P-free balls therefore
exist. Translating and using finite-shape compactness gives a Q-only plane
tiling, with all reflections and partial contacts still permitted. This
contradicts the Q-only obstruction. The argument is used for impossibility,
not a false extension from bounded local modules.

## Exceptional periodic carrier and scope

At Rlen=L, rho=1-tan36 lies strictly in(0,1). The exact producer checks
orthogonal equal-length square basis, midpoint-perpendicular-bisector kink
locations, four checkerboard profile identities, both final fan determinants
and the four-Q covolume. I separately executed cross(u,v)>0 exactly; adding
that assertion makes the initial homotopy orientation explicit. Each determinant
is affine in the homotopy parameter, so the positive initial/final signs
exclude flipping. The cyclic mesh winding remains one; proper bounded
displacement gives a global plane homeomorphism by the same reviewed argument
as the thin four-P fixture. Qstar and its halfturn occupy opposite sides of
their shared D-E support segment, so their local parent decomposition is
valid independently of area equality. The four-Q motif is an actual infinite
periodic tiling; no imported Type2 theorem is needed. Its Type2 relabeling
also agrees with the inspected primary-source side convention.

All0<rho<1 are thus excluded as aperiodic pairs: unequal radial/tangent lengths
are untileable; the equality point admits a periodic Q-only tiling. The stated
substitution rho=2/phi cubed has Rlen<L, checked exactly by replay.
Changed angles, endpoint data or C>=2L remain outside the proof. No original
Penrose decoder or unrestricted two-polygon impossibility is asserted.
No substantive unresolved objection remains.

The author added cross(u,v)>0 and an explicit opposite-support-halfplane
argument for the two-Q modified parent. These resolve the replay/proof
explicitness observations; the final scoped conclusions are approved.
