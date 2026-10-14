# Right-angle hosted-side necessity: native octagon lengths

Date: 2026-10-13. Status: claims1-4adversarially reviewed VALID in `research/reviews/contact-right-angle-hosted-side-necessity-hostile-review.md`. Claim5is also independently reviewed VALID. The stronger no-Q-host observation and acute-adjacent P-host exclusion below are also independently reviewed VALID in that review. No all-metric periodicity assertion.

## Exact scope

P is a genuine convex pentagon with one angle90and four angles112.5. Q is a genuine convex octagon with eight angles135. Copies may translate, rotate or reflect; contacts are unrestricted. Let u,v be the lengths of P's two sides incident to its unique90corner, and L the set of its five native side lengths.

In every admitted tiling:

1. The species of the neighbor is constant along the relative interior of each native side, although multiple P neighbors may occur.
2. A native side contains at most one flat contact vertex in its interior.
3. Each Q side is exactly one of: a whole Q-Q contact; a whole Q-P contact whose length lies in L; or the union of two whole sides of two P copies. In the last case its length is exactly2uor2v, and the P acute corners meet at its midpoint. The two P tiles share one whole acute-adjacent side perpendicular to the hosting Q side.
4. If the hosted Q side has length2u, the perpendicular shared P edge has lengthv; if it has length2v, that shared edge has lengthu. When u=v the descriptions coincide.

5. Each native Q side-neighbor word has no adjacent Q entries and no Q-P-Q cyclic substring. Thus there are at most two Q-neighbor side slots on any single Q tile. If there are two, their cyclic distances are3and5or4and4. The full labeled binary-word domain has21words: one with zero Q slots, eight with one, twelve with two.

Only the Q-hosted complete segment statement is claimed. A P host may have its own acute endpoint inside another tile side, so P-hosted endpoint analysis needs separate care.

## Proof

Measure angles in units pi/8. Genuine sectors are4,5,6. Full stars solve4a+5b+6c=16 and are precisely fourP90, twoP112.5+Q135, P90+twoQ135. A corner in another side interior leaves angle8on the other side; its only partition is4+4. Thus every flat event has one straight host and two acute P corners.

Whenever the adjacent tile changes along the interior of a native host side, a tile vertex occurs there. The previous and next adjacent sectors are both P90 by the flat-star classification. Thus a change does not change species. Local finiteness makes this a finite argument along each compact side.

Suppose a host side had two successive interior flat vertices. Between them there is one neighboring tile: otherwise another change would give an intervening flat vertex. Convexity implies its side contact is a single interval. That neighboring P would have an acute corner at both interval endpoints, contradicting that P has only one acute corner. Hence at most one flat vertex lies on a native side.

At a flat vertex T the two P90 corners each have one side along the host and one side along the common perpendicular ray. Their common interface extends to a native endpoint of at least one P side. That endpoint is P112.5 and cannot occur in the interior of the other P side, since only P90 can occur at a flat event. Thus both common sides end at the same point and have equal length. The shared side therefore uses the same native acute-adjacent length on both copies, except that u-v matching is possible when u=v. The other acute-adjacent lengths are consequently equal as well.

Now take a Q host. Its endpoint angles135cannotoccur at a flat event, so the two P sides along it end exactly at its two native endpoints: neither can stop sooner (that would be another flat event), and neither can continue past the Q endpoint (that would put a Q135corner in a side interior). Their equal lengths make T the midpoint, giving total length2uor2v and the stated perpendicular shared-edge lengths.

If no flat event lies in the Q side interior, a single neighboring tile occupies its whole side. The Q endpoints cannot occur in another side interior, so the neighboring side has precisely the same endpoints. A P neighbor therefore matches one whole P side of length in L; a Q neighbor gives a whole Q-Q contact. These exhaust all cases.

## Exact necessary metric consequence

Every Q side with length outside L union {2u,2v} must have a Q neighbor. Every Q side with length outside L but not Q-Q must host the rigid midpoint dimer above. These alternatives can be inserted into a finite periodic-escape search without assuming edge-to-edge contact.

The lemma imposes no global orientation set, no finite-model property and no existence or periodicity conclusion. In particular, it does not prove that nonsymmetric metrics force a symmetric channel. The ledger p=2q+2z+t and the separate private-side theorem remain necessary global filters, not substitutes for geometric extension.

## Additional native octagon neighbor-word proof

By claim1each native Q side has a well-defined neighbor species. Adjacent Q-labeled sides would place three Q135corners at the intervening Q vertex, impossible. Now suppose the cyclic side labels included Q-P-Q. At either endpoint of the middle P-labeled side, the Q host and neighboring Q across the outer Q-labeled side have angles135+135, so the unique remaining sector is one P90corner. If the middle side were split at a hosted T, claim3would make its endpoint P corners obtuse, a contradiction. Otherwise it has a single whole P-side neighbor, and the same P tile would have90corners at both endpoints, also impossible. Therefore any two Q-labeled slots are separated by at least two P slots, and an eight-cycle has at most two such slots. With two their distances are3/5or4/4. The exact labeled count is1+8+(8+4)=21; the eight distance3pairs and four opposite pairs give the final term. This is an unrestricted local contact constraint, not a classification of globally extendible words.

## Stronger native-pentagon parity: no Q-hosted flat event

New claim6. In fact Q-hosted flat contacts cannot occur in any admitted tiling of this palette, regardless of metric. Label each native side of one P by the constant neighbor species from claim1. At each112.5vertex the full star is PPQ, so its two adjacent side labels differ. Following the four consecutive112.5corners therefore makes four binary-label changes, implying that the two native sides incident to the unique90corner have the SAME label. Thus P's cyclic word is always P-Q-P-Q-P or Q-P-Q-P-Q (start with one acute-adjacent side), even with all permitted subdivisions.

If a Q side hosted twoP90corners, each guest P would have one acute-adjacent side labeledQalong the host and the other labeledPalong the shared perpendicular interface, contradicting the same-label conclusion. Hence t_Q=0. All Q-P contacts are then whole native sides on both tiles: their only possible subdivision event would be Q-hosted or would put a Q135corner on a P side, both forbidden. Q-Q contacts were already whole. Thus all contacts involving a Q are edge-to-edge, while P-P Tcontacts remain permitted.

This supersedes the practical application of claim3: the hypothetical rigid Q-host midpoint dimer cannot extend to a complete tiling because each guest P's other corners impose the contradictory side-label parity. Claim3itself remains a valid local conditional observation. The finiteQword constraint in claim5continues to hold, now with an even simpler proof since every P-labeled Q side has one whole Pneighbor.

## P-host refinement

If a P-host side has both endpoints112.5, neither endpoint can lie in another tile side interior. Its two neighboring guest P copies have90at the interior T and112.5at the host endpoints, so each guest uses a whole acute-adjacent side along the host. The shared perpendicular acute-adjacent sides are whole and equal by the earlier proof, forcing the host's two guest lengths equal. Therefore this P-host native side has length2uor2v. The two native P side slots incident to90retain the endpoint-partial caveat and are not assigned this length restriction.

These are necessary local metric/contact restrictions, not a proof that surviving metrics admit periodic or infinite tilings.
