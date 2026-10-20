# Adjacent 150-degree heptagon seam: exact local construction and omission failure

**Status: falsified for aperiodicity (2026-10-20).** This is a shape-first P5/Q7 trial, not a plane-tiling construction. Replay the exact Sage arithmetic and separating-axis checks with

```text
mise exec -- conda run --no-capture-output -n arisearch python research/searches/p5q7-adjacent-150-caps-2026-10-20.py
```

## Distinction from recorded work

P has angle word `(60,105,120,120,135)` and Q has `(150,150,120,120,120,120,120)`. This differs under cyclic shift and reversal from the earlier P5/Q7 `(115,115,100,110,100)`/`(130,130,130,125,125,125,135)` torus pair, `(95,105,110,115,115)`/`(125,125,125,125,130,130,140)` disconnected-side pair, regular-P5/126–144 heptagon families, and square-lattice power cells. The mechanism is a Q/Q seam across the side between two adjacent 150-degree Q corners, capped by a 60-degree P corner at both ends. The earlier long-edge P/P5 and contact-right constructions have different angle words and topology. This comparison is repository deduplication only.

## Exact definition and local checks

Work in the positive real embedding of `K=Q(sqrt(2),sqrt(3))`. Write `r=sqrt(2)`, `s=sqrt(3)`, `c=s-1`, and `t=1+3r/2-s-rs/2`, all with `r,s,c,t>0`. Starting at `(0,0)`, P has directed edges at angles `(0,75,135,195,240)` degrees and lengths `(1,t,c,t,c)`. Q has directed edges at `(0,30,90,150,210,270,330)` degrees and lengths `(s,c,c+2-t,t,c-t+3,c,1)`. Both vector sums are exactly zero. Every successive edge cross product is positive; thus both polygons are strictly convex. The full vertices are emitted by the replay script. The exact numerical side-equality classes are `P: 1 | t,t | c,c` and `Q: s | c,c | c+2-t | t | c-t+3 | 1`; all six listed values are pairwise distinct.

Let Q0 be the native Q and Q1 its half-turn about the midpoint of side 0, of length `s`. This gives a Q/Q seam with a 60-degree vacant wedge at both endpoints, since both incident Q corners are 150 degrees. Place a P at each endpoint by matching its length-1 and length-c arms at its 60-degree corner to the adjacent Q sides. The resulting 2P+2Q patch is exact and pairwise interior-disjoint, including both orientations of the Q dimer; the script checks it by exact separating axes. The two Q 120-degree private sides have lengths `c+2-t` and `c-t+3`; a half-turn Q mate across either side, taken in isolation, has endpoint rays of lengths `c,t`, so a P 120-degree corner with those lengths caps each endpoint without overlap. The length-`c-t+3` half-turn mate remains legal beside the 2P+2Q base patch. The length-`c+2-t` mate **overlaps** that base patch; local seam compatibility does not imply simultaneous extension.

Q alone cannot tile: at any interior point of a Q side, two Q corners would need angles summing to 180 degrees, impossible for the Q palette `{120,150}`; at a full vertex containing a 150-degree corner, no multiset of these angles sums to 360 degrees. In any Q-only plane tiling a 150-degree corner must nevertheless occur. This is a direct obstruction for unrestricted partial contacts.

## Fatal P-only escape

The P metric exactly satisfies Rao monohedral pentagon **type 2**. In the repository's reviewed Table 2 transcription, choose reversed indexing with offset 2: the type-2 angle equation is `105+135+120=360`, and its side equation compares native side 4 with native side 2, both `c`. The script independently applies every cyclic and reversed indexing and prints hit `(2,-1,2)`. The standard type-2 construction yields a periodic P-only tiling, so the pair fails the universal aperiodicity quantifier irrespective of whether mixed patches extend.

This failure is structural for this local cap design. For P's angle word `(60,105,120,120,135)`, Rao type 2 is triggered if the length-c arm at the P 60-degree corner (native side 4) equals either native side 1 or 2. Forcing a P 120-degree cap on Q's private Q/Q seam by equating the Q outer length c to one of those P sides therefore creates the P-only escape. The earlier parameterization `P=(1,c,t,c,c)` gave the same type-2 failure, with reversed offset 4 (native sides 1 and 4 equal). This route should not be extended by larger patches of either fixed metric. A materially changed P angle word or a Q-side cap using Q rather than P is required.

The script performs exact finite checks of closure, convexity, equality pattern, legal displayed patches, and the Rao filter. It does not classify all mixed tilings or prove plane existence. No novelty claim beyond the repository comparison is made.
