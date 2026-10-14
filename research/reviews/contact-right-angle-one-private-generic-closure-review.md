# Independent review of the 60 one-private dimer closure cones

Date:2026-10-13. Verdict: **valid finite closure computation**. No plane-tiling conclusion follows from the48positive records.

Reviewed producer `research/searches/contact-structure-one-private-dimer-words.py` and certificate `research/certificates/contact-structure-one-private-dimer-words.json`. Independent verifier `research/reviews/contact-right-angle-one-private-generic-closure-check.py` imports no producer and passed all60records.

The exact domain is two endpoint orders(H,u,...,v)/(H,v,...,u)and all30distinct permutations of(x,x,y,y,w), giving60rooted native words. Each record adds the two Pclosure equations and two octagon vector equations in the quartic fieldc,8c^4-8c^2+1=0,9/10<c<1. Sum of the six lengths=1normalizes the homogeneous positive cone. The21forbidden hyperplanes are15pairwise length equalities and6host doublingsx,y,w=2uor2v.

All normalized systems have rank5and dimension1. I independently solve each as an affine line p+s*k, intersect its six coordinate halfspaces to obtain the exact closed parameter interval, and reconstruct its endpoint vertices. This is independent of the author's active-zero-subset enumeration. Endpoint sets, closure ranks, dimensions, forced-zero coordinates and all forced forbidden equalities agree. The interval construction proves full normalized polytope completeness.

All48positive records have independently checked strictly positive witnesses, closure and normalization identities, nonzero values for every forbidden hyperplane, and the recorded weighted-vertex construction. All12negative records force at least one forbidden equality or zero coordinate throughout the full interval. Their metadata and60-wordcoverage agree exactly. Algebraic signs use the specified positive exact embedding, without tolerance or solver.

The producer's vertex-enumeration rationale is also correct: every vertex of a bounded normalized nonnegative affine polytope has enough independent active-zero coordinate equations; choosing all subsets of its affine dimension exhausts them. Its finite polynomial hyperplane-avoidance bound is valid when no forbidden hyperplane contains the whole polytope. The independent interval and actual witness checks avoid relying solely on this generation argument.

Critical scope: exactly one private native side does NOT itself imply every Qhas one QQneighbor. The60words are a dimer-source algebraic domain, expressly stated by the producer; possible degree2QQfields are outside this computation. The separate stronger generic analytic obstruction treats them. Positive closed polygons do not establish extension or tileability. No substantive defect found in this exact finite computation.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/contact-right-angle-one-private-generic-closure-check.py
