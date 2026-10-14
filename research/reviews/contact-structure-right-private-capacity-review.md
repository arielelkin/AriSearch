# Fresh hostile review: unrestricted right-palette private-side capacity

Date: 2026-10-13. Verdict: **valid**. Reviewer: affine-construction agent, independent of author.

Reviewed `research/lemmas/contact-structure-right-palette-private-octagon-capacity.md`. The exact domain is arbitrary metrics for P=(90,112.5,112.5,112.5,112.5) and Q=(135 repeated eight times), with all isometries and unrestricted partial contacts. The claim is at most two native Q side slots may have lengths absent from all five P lengths.

I independently enumerated the complete angle equations over 0<=a<=N/4,0<=b<=N/5,0<=c<=N/6 for N=8,16. They give only flat2P90 and full4P90,2P112.5+Q135,P90+2Q135. Strict convexity and local finiteness justify this angular classification without contact assumptions. In particular Q135and P112.5cannot occur in a side interior.

The native balances check: x=2p+O(R), y=4q-p+O(R), p=y+4z+2t+O(R), hence p=2q+2z+t+O(R). The four-right stars and all hosted stars are retained with correct multiplicity. A Q-Q contact must be whole on both sides, since a terminating Q corner cannot lie on another side interior. Each Q-Q endpoint has precisely a y star, and conversely a y star has exactly one Q-Q side incident, yielding2e=y+O(R).

For a private Q side not QQ, all adjacent positive-length intervals are P contacts. If there were one interval only, Q's two endpoint corners cannot lie within the P side, so both sides would match whole with equal length, contradicting privacy. There is therefore a Q-hosted flat vertex in that side interior. Choosing one such event per side is injective: a flat event has one host and lies in one native side interior. A Q-hosted flat event cannot pay for two private side slots or two Q copies. Thus kq<=2e+tQ+O(R)<=y+t+O(R)=2q-2z+O(R) is valid. Charging private sides to all QQ slots can only overcount capacity, never undercount it.

Uniform boundary errors hold because tile diameters and corner counts are bounded and minimum areas are positive. Chosen host anchors versus tile/edge anchors only differ within a fixed-width boundary strip. If k>=3, q=O(R); y>=0 then p<=4q+O(R), contradicting quadratic area coverage. This handles zero-density and omitted-type cases without assuming a frequency limit.

The distinct-Q-length corollary uses slots correctly: eight distinct lengths can coincide with at most five P values, so k>=3. Repeated Q lengths must still count separately as native side slots, and the proof does.

No substantive defect found. The theorem does not assert existence, periodicity or classify all metrics surviving k<=2. The separate stronger local midpoint lemma is not needed by this capacity proof.
