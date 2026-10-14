# Independent hostile review: high-partner PPP density

Date: 2026-10-13. Reviewer: affine-construction agent, independent of the author.
Verdict: **valid** for the stated all-obtuse pentagon/n-gon domain.

## Exact claim

Reviewed `research/lemmas/contact-structure-high-partner-ppp-density.md`: for P a convex pentagon, Q a convex n-gon, n>=7, all angles strictly between pi/2 and pi, every admitted tiling has uniform-window bounds 6u>=4p-nq-O(R) and u>=(n-8)q/2-O(R). Consequently n>=9 forces uniform positive quadratic PPP incidence and excludes P with no native three-angle sum 2pi.

## Hypotheses and contact audit

I read the reviewed obtuse forcing and pentagon curvature dependencies. Strict obtuseness excludes both a corner in another side interior and four or more genuine corner sectors. Interior angles below pi exclude two sectors. Hence edge-to-edge trivalence is valid without initially imposing any contact rule. Reflections do not change these facts. A mixed vertex always has exactly two mixed edges. Convex tiles cannot have multiple sectors at a point. Two neighboring tiles cannot occupy the same side twice, and no such neighbor uniqueness is actually needed by the count.

At each P corner the two consecutive side neighbors determine precisely the other two incident tiles. Adjacent P entries are therefore exactly PPP incidences. A finite exhaustive check of all 32 cyclic binary words returned possible r-values indexed by m: m=0:{5}, 1:{3}, 2:{1,2}, 3:{0,1}, 4:{0}, 5:{0}. Every word satisfies m+r>=3, with equality at (2,1) and (3,0). This is also proved by the author's cycle-edge argument; enumeration is not needed for the theorem.

## Global and boundary audit

Finite prototiles have maximum diameter D and positive minimum area a. Every tile whose centroid, corner or side-midpoint anchors disagree about square inclusion meets a fixed-width boundary strip. Such tiles lie in a slightly enlarged strip of area O(R), and disjoint interiors imply their number is O(R)/a. Each has boundedly many corners and sides, so every displayed incidence discrepancy is O(R), uniformly over center and admitted tiling. There is no frequency-existence or ergodicity assumption.

The identities are correct: e=x+y+O(R), 5p=3u+2x+y+O(R), nq=x+2y+3z+O(R). Summed m+r>=3 gives e>=3p-3u-O(R), hence y>=p-3u-O(R), and nq>=(5p-3u+3y)/2-O(R)>=4p-6u-O(R). Trivalent curvature gives p=(n-6)q+O(R), and substitution yields the second bound with coefficient (n-8)/2.

Area coverage implies p+q>=cR^2-O(R). Together with the uniform ratio this implies q>=c1R^2-C1R. For n>=9 the PPP lower bound is also c2R^2-C2R. Thus neither sparse higher tiles nor sparse PPP vertices invalidate the argument. It actually implies syndeticity of both Q tiles and PPP vertices (take a fixed sufficiently large R). Repetition of a native P angle at different copies is allowed; excluding all native multisets of size three is the right angle hypothesis.

## Defects and scope

No defect in the reviewed theorem or proof was found. At n=8 the derived coefficient is zero and yields no PPP obstruction. Acute or right angles invalidate the contact reduction and remain outside scope. This is a necessary structural theorem, not an existence or periodicity theorem.

The existing dependency `obtuse-edge-forcing.md` says its uniform quadratic-count consequence does not force bounded gaps. That sentence is inaccurate: a uniform lower bound cR^2-CR does force bounded gaps for sufficiently large fixed R. This does not undermine the dependency's main contact theorem or the current PPP proof. The author and root were notified; correction is separate from the validity verdict.
