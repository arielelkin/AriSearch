# Double-acute pentagon monohedral escape gate

Verdict: the exact test against the fifteen listed convex pentagon families is valid. This is a gate on a construction family, not a proof of tiling existence or mixed aperiodicity.

The native angles are `(60,60,150,120,150)`. With positive `c,d,e`, the closure equations give

`a=e+(c+2d)/sqrt(3)`, `b=e+(d-c)/sqrt(3)`.

The strict domain is `c<d+sqrt(3)e`. Within it, `a` is strictly larger than every other side: comparisons with `c,d` follow by substituting the strict domain inequality; comparisons with `b,e` follow directly from positivity.

The checker transcribes Table 2 of [Rao's primary classification paper](https://arxiv.org/pdf/1708.00274#page=14), and checks all ten cyclic/reflected native labelings for each of the fifteen families. A reflection maps a side by its two endpoints, so that its offset differs by one from the corner offset. Only Types 2, 5, and 8 have matching angle equations. The Type 5 and Type 8 matches require the largest edge to equal a smaller one. Two Type 2 matches fail for the same reason. The two remaining Type 2 matches are exactly `c=e` or `b=d`. Those loci must be rejected before trying an unmarked aperiodic pair, since a periodic monohedral tiling can omit the other species.

The sample used by the construction agent avoids both loci for both species. Passing this test supplies no global tiling and no restriction on mixed periodic tilings. The source transcription, exact arithmetic, ten dihedral maps, and output are retained in `check_pentagon_two_acute_monotile_gate.py` and `pentagon-two-acute-monotile-gate.json`.
