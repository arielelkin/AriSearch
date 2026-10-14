# Exact rooted one-private dimer closure cones

Date:2026-10-13. Completed exact finite-domain closure enumeration; independently checked VALID/PASS by affine agent. This records necessary metric domains, not tileability.

With five distinct P native lengths x,u,v,y,w, a whole-contact one-private Q dimer would have public multiset x,x,y,y,u,v,w and private H, with H flanked by u,v. Up to reflection the rooted words are H,u,permutation(x,x,y,y,w),v: precisely30 distinct permutations and their swapped u/v convention,60 words. The producer contact-structure-one-private-dimer-words.py retains every word and exact closure/positivity/degeneracy outcome in research/certificates/contact-structure-one-private-dimer-words.json. It solves two P vector-closure and two Q vector-closure equations over Q(cos22.5), normalized by sum(lengths)=1. Every vertex of the resulting nonnegative polytope is recovered by enumerating active zero-coordinate sets. Their barycenter has all coordinates positive exactly when strict-positive closure exists. Rational weighted combinations then avoid the finite forbidden equality planes, giving exact witnesses where permissible. This is a complete60-word closure domain, without a numerical cutoff or sampling.

Result:48 words have admissible positive generic cones;12 are degenerate. Nonetheless the entire five-distinct/no-host-doubling domain fails local extension, analytically: both P_R and P_S neighbors occur around every Q. Some consecutive Q neighbors must therefore form an R-S PP interface. A whole R-side bevel x/y has two112.5 endpoints; an S acute leg u/v has one90 endpoint, making the far full star impossible. An S middle leg w would require w=x or w=y. Those identities are excluded in this domain. Thus none of the48 positive closure cones supplies a tiling. This stronger local obstruction supersedes any attempted downstream ring or large-radius search; the closure certificate remains a useful necessary-domain record.

The genuinely changed hosted mechanism x=2u is recorded separately in contact-structure-one-private-x2u-dimer-candidate.md. Its partial interface escapes the whole-interface obstruction; it is not an enlargement of the killed generic-cone search.

Replay (retained certificate unchanged):

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/contact-structure-one-private-dimer-words.py --check research/certificates/contact-structure-one-private-dimer-words.json

Default stdout now emits the full result JSON; --check emits a concise replay summary. No certificate mutation occurs on replay.
