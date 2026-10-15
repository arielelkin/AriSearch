# Independent hostile review: off-normal mark-local receiving hexagons

Date: 2026-10-15. **Final verdict: VALID.** I independently attacked the proposed proof, then reread the complete final [root-authored lemma](../lemmas/offnormal-mark-local-truncation-obstruction-2026-10-15.md) after its replacement of common-pair uniqueness by the simpler tangent-wedge argument. No unresolved mathematical defect remains. This is a construction-component obstruction, not an unrestricted impossibility theorem for two convex polygons.

## Exact scope and assumption ledger

The source consists of the specified unit thin/thick Ammann rhombs, with the actual native arrow table. For each mark Z a donor triangle has parameters 0<u_Z<1 and h_Z>0, and a split 0<m_Z<1, both independent of source species and parity. Internal donor apices are strictly inside their source rhombs. All source-sector geometry is embedded and strict. Crucially, all sixteen receiving PRECURSOR quads are explicitly assumed strict convex. Each is truncated at its two donor-node vertices to a genuine convex six-corner polygon. External tail cuts are mark-local on their two role-indexed rays. Other cuts need not be mark-local.

The contradiction assumes all receiving hexagons are congruent to one unmarked H, with arbitrary rotations and reflections. It does not use congruence of pentagons or caps, cyclicity of caps, equal radial distances, or a normal-foot relation between split and apex. These are exact hypotheses of the reviewed claim, not derived universal properties of every fractional surgery. The explicit strict-precursor condition matters to the head-angle geometry below.

## Actual endpoint angles and the acute branch

I previously independently reconstructed all sixteen arrow endpoint forms for the preceding construction review. They remain valid after moving M off the normal foot: they depend on the donor triangle base angles and retained source vertex, not on the position of the split along the edge. The thin endpoint values are a=36+Xt-Yt, b=36+Yt-Xt,144,144; the thick values are c=108+Yt-Xh, d=108+Xh-Yt,72,72. Every one persists as a native H corner.

Since a,b>0 and a+b=72, unequal a,b would give four distinct H angle values a,b,72,144 totaling 288. The remaining two angles are each less than 180 and cannot give total 720. Hence a=b=36 and Xt=Yt=beta. With values 36,72,144 in H, the other three angles sum 468 and are individually greater than 108. Therefore H has a unique 36, a unique 72, and four other angles all above 108.

The values c,d are H angles with sum 216. They cannot both exceed 108. An available smaller value 36 would force its companion to be 180, so the pair is exactly {72,144}. Thus Xh=beta+36 or beta-36. The actual thin arrow table places each tail at an acute 36 source vertex. An internal donor apex strictly inside that source wedge has tail base angle strictly between 0 and 36. This is enough to exclude beta-36. Consequently Xh=beta+36, c=72 and d=144. Both marks have endpoint 36 in thin tail contexts and 72 in thick tail contexts. No normal-foot assumption has entered.

## Same-mark head bound

The needed head contexts really exist in the native source table: the thin vertex B has two X arrows ending there and source angle 144; the thick vertex C has two Y arrows ending there and source angle 72. Choosing either donor parity provides the corresponding receiving quad and internal donor node.

In such a quad U,t,M,p, the distances Ut and Up are equal because both are head-to-apex distances of the same mark-local unit-base triangle. Equality does not require the two apex vectors to have the same direction. Incoming and outgoing head-base-angle transfers cancel at U, leaving exactly the source angle sigma. Hence triangle Utp is isosceles with each base angle (180-sigma)/2.

Strict convexity of the native ordered quad places its opposite vertices U and M on opposite sides of diagonal tp. At t the ray tp lies strictly inside the quad angle between tU and tM. The external donor half-angle at t is therefore strictly larger than angle Utp. It follows that theta_Xhead>18 and theta_Yhead>54. This is an ordinary convex-quadrilateral diagonal argument; a mere positive ray angle or an angle-SAT assignment would not establish it.

Since M lies strictly between the two unit base endpoints, its ray divides the full donor apex angle into positive tail/head parts. The full X apex is 144-2beta. Thus theta_Xtail<126-2beta. These geometric inequalities do not alone produce a contradiction, and are not claimed to. Existing angle-only and strict-precursor examples remain compatible with this stage.

## Exhaustive cyclic lower bound, without uniqueness assumptions

I independently checked the final weaker cyclic lemma: if H has angles 36,72,144 and the same ordered pair (s,t) follows its unique 36 and unique 72 in possibly different directions, then s+t>=288.

Neither pair entry is 36, because its occurrence after the unique 36 would duplicate that vertex; neither is 72, because its occurrence after the unique 72 would duplicate that vertex. Thus both entries lie among the four angles above 108. Remove the two small vertices from the cycle. Its two intervening large-angle runs have lengths 0/4,1/3 or2/2, up to exchange, exhausting every orientation and cyclic alias.

- In 0/4, both occurrences enter the long run from opposite ends, giving (s,t,t,s). Its angle sum gives s+t=306.
- In 1/3, both enter the three-vertex run, giving (s,t,s) and one isolated angle v, with 2s+t+v=612. If 144=s then t+v=324 forces t>144. If 144=t then 2s+v=468 forces s>144. If 144=v then 2s+t=468 and s<180 force s+t>288. Thus every case gives a strict lower bound above 288.
- In 2/2, occurrences using different runs again give sum 306. Occurrences using the same run read it in opposite directions, forcing s=t=q. The other entries u,v satisfy 2q+u+v=612. If q=144 the pair sum is 288. Otherwise one of u,v is 144 and the other is less than 180, forcing 2q>288. This argument includes equal angles on both runs and needs no hypothesis that the ordered pair or its orientation is unique.

This is a complete finite case proof on a six-cycle, not an unrecorded numerical search. Mark-local X tail triangle/split/cuts give the same ordered external cut pair in thin and thick X-tail contexts. Its sum is 180+theta_Xtail by the elementary corner-truncation triangle identity, valid for unequal cut distances. The cyclic lemma yields theta_Xtail>=108. Combining with theta_Xhead>18 gives 108<126-2beta, hence beta<9.

## Metric congruence forces a common donor, including reflections

The final replacement is sound and avoids the earlier, more elaborate pair-uniqueness argument. In a thin-tail receiving hexagon the native vertex sequence is T,external-cut0,external-cut1,M,internal-cut0,internal-cut1. Unique angle 36 forces every congruence to map T to T. Isometries of genuine convex polygons preserve their six-cycle of vertices up to reversal, so the opposite native vertex M, three steps from T, maps to M independently of all other angle coincidences. Their distance is therefore common. As each original source edge is unit and its split lies internally, |TM|=m_Z, giving m_X=m_Y=m>0.

Normalize a thin X-tail and a thin Y-tail H to T=0, M=(m,0), placing the source interior above the base. Their external donor rays point at angle -beta, whereas their internal donor rays point at 36-beta: both source tail base angles equal beta. Proper corner cuts preserve these tangent rays. Thus the unordered tangent wedge at T is the same pair {-beta,36-beta} in both normalized polygons.

Every Euclidean isometry fixing the two distinct points T and M is identity or reflection in their line. The reflection gives tangent pair {beta,beta-36}. For 0<beta<36 it equals the original pair only if beta=18; direct matching of the two unordered rays proves this, with no orientation convention suppressed. Since beta<9, reflection is impossible. The normalized congruence is the identity.

The two external cut vertices are now fixed individually. They lie below the base, while the internal cuts lie above it; alternatively they are the first two boundary vertices reached along the lower tangent ray. The proper cut on tT and the proper cut on tM determine the lines T-cut0 and M-cut1. Both contain the external apex t, and they are distinct nonparallel lines because h>0 and T,M,t are not collinear. Thus their intersection recovers the same external apex for both marks. It follows that u_X=u_Y and h_X=h_Y. With their common original unit base, their head base angles coincide, so gamma_Y=gamma_X=beta+36. With their common split m the tail and head apex parts also agree.

Consequently theta_Yhead=144-2beta-theta_Xtail<=36-2beta<36. This contradicts the proven thick Y-head bound theta_Yhead>54. This final step uses actual METRIC congruence of H, not just equality of its angle word; it is exactly the missing coupling between the separate relaxed angle and precursor-convexity gates.

## Defects attacked, final status and limits

I attacked the source tail/head roles, whether apex-in-wedge really bounds beta, the full-side counterpart of head radial equality, both diagonal half-planes, arbitrary repeated large angles, every cyclic arc configuration, a hidden assumption of unique pair orientation, possible reflection symmetry fixing T and M, recovery of an apex outside the original edge projection, properness of the cut rays, and an unjustified inference from angle compatibility to coordinate congruence. The final exact artifact explicitly supplies the needed strict precursor, proper-cut and interior-apex assumptions. Every bridge survives.

The proof needs no new computation: its inequalities and cyclic enumeration are complete written arguments, so no solver/certificate is being used to replace a universal geometric step. The old exact SAT-angle witness and independent strict-precursor fixture are not counterexamples to the combined claim; neither satisfies the common receiving-H congruence hypothesis. They remain valid within their own declared scopes.

I made no author edits. The final written theorem is VALID for its exact unit-source, mark-local donor/split/external-tail-cut component, even with off-normal splits, unequal cuts, arbitrary inner cuts, reflections and arbitrary prototype aliases. It does not cover context-dependent external cuts, donor projections outside (0,1), changed source incidences, nonconvex precursors, or arbitrary two-polygon constructions. The original unrestricted objective remains unresolved.
