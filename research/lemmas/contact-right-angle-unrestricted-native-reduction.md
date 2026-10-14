# Unrestricted native reduction for one-right pentagons and equiangular octagons

Date: 2026-10-13. Status: adversarially reviewed VALID, including the final no-acute-host refinement. Review: `research/reviews/contact-right-angle-hosted-side-necessity-hostile-review.md`.

## Exact hypotheses and conclusions

P is a genuine compact convex pentagon with exactly one90-degree corner and four112.5-degree corners. Q is a genuine compact convex octagon with eight135-degree corners. All metrics, translations, rotations, reflections and contacts are unrestricted. Let u,v be the lengths of P's two acute-adjacent sides and L its set of five side lengths.

Every admitted plane tiling has these properties:

1. Each native side has constant neighbor species, even if subdivided, and contains at most one interior flat event.
2. The cyclic native P neighbor word, starting with one acute-adjacent side, is exactly P-Q-P-Q-P or Q-P-Q-P-Q.
3. No Q side hosts a flat event. Every contact involving Q is a whole native side of both incident tiles. P-P partial contacts are not excluded by this step.
4. Q's cyclic native neighbor word has no adjacent Q entries and no Q-P-Q substring. Each individual Q has at most two Q-neighbor slots; if two, their cyclic distances are3/5or4/4. There are21labeled words: one with no Q slots, eight with one, twelve with two.
5. A P-hosted flat event on a side whose two endpoints are112.5requires that side's length to be2uor2v. The two guest P tiles share a whole perpendicular acute-adjacent side, lengthv oru respectively.
6. New refinement: a P side incident to its90corner cannot host a flat event at all. Hence every flat host side is one of the three nonacute-adjacent P side slots and has length2uor2v. If none of those three lengths equals2uor2v, every tiling is edge-to-edge (four-right vertices remain permitted).

A Q native side length absent from L is called private. Every private Q slot must have a Q neighbor. At most two can exist; if two their native cyclic distance is3or4. With exactly two, every Q's Q-neighbor mask is exactly those private slots. This alone does not exclude isolated four-right or flat defects.

## Complete angular language and side species

In units pi/8 the angles are4,5,6. The nonnegative solutions of4a+5b+6c=16are exactly(4,0,0),(0,2,1),(1,0,2): fourP90; twoP112.5+Q135; P90+twoQ135. The only solution with sum8is(2,0,0), so every corner in another native side interior has one straight host and twoP90corners. Neither P112.5norQ135can lie in a side interior.

Along a native side, any change of neighboring tile occurs at an interior vertex of that side. At such a flat event both preceding and succeeding neighbors are P, so their species agrees. Local finiteness makes the number of changes finite. If two successive flat events occurred on one native side, the intervening neighboring tile would be one P with a90corner at each endpoint of its side interval. This contradicts P's unique90corner. Thus the native side has at most one flat event.

At each P112.5corner, the adjacent side-neighbor species are one P and one Q. Following the four consecutive obtuse corners flips the labels four times, so the acute-adjacent labels are equal. This proves the two stated P words. A P guest at a Q-hosted flat event would instead have one Q-labeled acute leg and one P-labeled perpendicular leg, a contradiction. Thus Q cannot host a flat event. Q135corners cannot lie in side interiors, and P corners in Q-side interiors are now excluded; every positive-length Q-P or Q-Q contact consequently matches whole native sides.

## Native octagon word

Two adjacent Q-labeled sides would put threeQ135sectors at their common vertex, impossible. For Q-P-Q, the single P neighbor across the middle whole side would have90corners at both its endpoints, because each endpoint already contains twoQ135sectors. This contradicts its unique90corner. Thus Q-labeled slots have cyclic spacing at least3; an eight-cycle admits at most two. For two slots the spacings are3/5or4/4. Exactly eight unordered pairs have distance3and four have distance4, giving the21labeled words. This is a necessary word census, not a global extension theorem.

## Rigid flat cap and both-obtuse host sides

At any flat event, the two P90guests share a perpendicular ray. Their shared interface ends at a native endpoint of at least one acute-adjacent P side. That endpoint is112.5and cannot lie in the other P side interior, so the two sides are whole and equal. Their other acute-adjacent lengths are therefore equal too: sharedu/u gives otherv/v; sharedv/v gives otheru/u; sharedu/vis possible only ifu=v.

If the host P side has two112.5endpoints, neither endpoint can lie in the guest's side interior. Its two guest side intervals therefore extend exactly to those endpoints, so they are equal whole acute-adjacent legs. The host length is2uor2v, and the shared perpendicular edge has complementary lengthv oru.

## New refinement: no acute-adjacent host side

Suppose A's acute-adjacent side hosts a flat event T. Place its acute endpoint O at coordinate0on the side line and T at coordinate d>0. A's native side extends from0toL_A, with0<d<L_A. Let B be the guest along the interval just left of T; B has its unique90corner at T and its host-aligned side extends left by lengthL_B.

B's other endpoint is112.5. It cannot end within(0,d), because that would put112.5inside A's native side. It cannot end at0either, because A90+B112.5cannot be completed by any allowed full star, and neither corner can be straight there. Thus L_B>dand B's side passes through O. At O, B is the flat host and A is one90guest. This is a reciprocal flat event.

At T, the other guest C has host-aligned acute leg lengthL_Bby the perpendicular-cap equality. It extends right fromd tod+L_B. Its112.5endpoint and A's112.5endpoint cannot lie in each other's side interior, so L_A=d+L_B. At O, the other guest D analogously has leg lengthL_Aand extends left to-L_A. B's112.5endpoint is atd-L_Band must coincide with D's112.5endpoint, so L_B=d+L_A. Combining gives2d=0, contradiction. Therefore no acute-adjacent host exists. All possible flat hosts satisfy the preceding both-obtuse length condition.

## Private masks and sparse-defect limit

Whole Q-P contacts force every private Q slot to be Q-labeled. The local word theorem bounds the number by two and their distances by3/4. For exactly two private slots the two-slot local maximum fixes the Q mask in every copy.

For uniform square counts p,q and star counts y=P90+2Q135, z=4P90, t=flat+2P90, native corner balance gives y=4q-p+O(R), p=2q+2z+t+O(R). A fixed two-Q-slot mask has2eQQ=2q+O(R), and2eQQ=y+O(R), so z+t=O(R). Errors are uniform in square center: finite tile diameters, positive minimum areas and finite native vertex counts bound every fixed-width boundary strip byO(R). This is a zero quadratic density consequence. It does not prove the defects absent or permit replacing unrestricted tilings with the trivalent model.

## Scope and dependencies

Elementary angular enumeration, convexity, local finiteness and exact incidence counts suffice. No finite computational model, metric classification, periodicity, plane extension or recognizability is assumed. The reduction constrains arbitrary metrics for this exact palette; other angle words are outside scope. A surviving fixed-mask pair still needs a concrete existence construction and a universal periodic-escape or aperiodicity proof.
