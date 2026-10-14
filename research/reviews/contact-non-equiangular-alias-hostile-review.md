# Independent hostile review: support-pivot alias candidate

Date: 2026-10-13. Verdict: VALID exact pair untileability.

Reviewed `contact-non-equiangular-octagon-alias-candidate-obstruction.md` and its producer. Independently wrote `contact-non-equiangular-alias-independent.py`, importing no author module or retained witness list. It reconstructs both exact AA polygons, verifies closure, positivity, strict support convexity, the sole x=w alias, H privacy and absence of every native 2u/2v length. It enumerates ordinary/reflected native-side isometries directly. For interior overlap it uses the separating-axis theorem with exact projections, independently of the author's convex-clipping algorithm. Its complete 4^5 domain yields exactly XXXXW, XXWWW, WWXXW, WWWWW, and independently reconstructs a missing native Q135 pair at a far endpoint for every ring. Replay PASSED.

The Q-only whole-contact proof survives the changed alias and angle palette. The full-star census and sole flat180+2P90 star exclude every obtuse native corner in a side interior. Perpendicular cap legs cannot differ because the shorter far P112.5 corner would lie inside the longer side; matching perpendicular legs force matching along-host legs. Both Q host endpoints and guest far112.5 endpoints prohibit a truncated cap, so a Q host would have native length2u or2v, absent. Q cannot host or have a native corner inside another side. All Q contacts therefore whole on both sides. This does not assert global native ETE.

H is the unique matching Q slot. Reflection would make157.5+157.5 at a seam endpoint, impossible in the enumerated angle census, so the H mate is the half-turn. The u/v acute P guests are uniquely fixed. The five length-one Q sides cannot be QQ: at one endpoint the adjoining outgoing own-Q side also has length one, whereas the forced P90 guest has no acute leg of length one. Thus each matches P x or w, and the independent placement domain has four choices on each.

At each central Q135 corner, the exposed consecutive P edges have values1,u,y. A shorter edge ending at an obtuse112.5 corner is forbidden inside its longer mate. The only potentially partial unequal interface is short u with far90 against a native length-one Px/Pw host (y<u<1 in this exact metric). These host sides have two obtuse endpoints, and completing its flat cap forces two along-host u legs, so its native length would be2u. This is absent. Hence these PARTICULAR interfaces are whole. No unrelated PP contact is claimed whole. This is the crucial finite-domain completeness argument; omitting it would make the 4^5 whole-interface filter insufficient.

At a reconstructed far endpoint with two P112.5 corners, only one Q135 can complete360. Its two outgoing native sides must match the outgoing P sides, by Q-whole contact. The six actual Q135 native pairs are (u,1),(1,1),(1,v); none includes y and neither (u,u) nor(v,v) occurs. Each of the four independently verified first rings has such a forbidden pair, so no Q occurrence can extend to a plane. A P-only tiling is impossible by its obtuse corner angle census. This proves the original exact pair untileable, without a global patch-extension assumption, blanket exclusion of PP flats, or a numerical tolerance.

Scope remains one exact pivot-c alias pair and its similarities. No obstruction for arbitrary support pivots, aliases, non-equiangular Q shapes, or the original general two-convex problem follows.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/contact-non-equiangular-alias-independent.py

## Exact producer orientation repair

Author normalized both clipper inputs to CCW after review, covering reflected native-index lists. Parent received all repaired replays, unchanged PASS outputs. The alias review's independent separating-axis checker does not depend on cyclic orientation and already verifies the same four rings. Final mathematical claims and verdicts are unchanged; the repaired clipper is the replay implementation supporting the finite patch checks.
