# Independent hostile review: hexagon strip cycle

Date: 2026-10-14. Verdict: **VALID on the stated conditional strip domain**.
Reviewed [the theorem](../lemmas/two-hexagon-repeatable-strip-cycle-2026-10-14.md) and [the author's checker](../searches/two-hexagon-sawtooth-strip-cycle.py). The independent checker imports neither author's code nor certificate data.

The explicit hexagon has positive six-turn determinants. Horizontal translates occupy exactly the vertical fibers from `-p*tau(x)` to `h+q*tau(x)`, since each polygon has two affine lower segments, two affine upper segments, and vertical sides. These fibers have gap `h+(p+q)*tau(x)>0`; adjacent horizontal translates meet only on their vertical boundary. The identity `tau(x-1/2)=1-tau(x)` matches the entire piecewise-linear seam, including both endpoints and its apex. The halfturn map `(x,y)->(1-x,h-y)` takes the ordered polygon to the reverse strip polygon exactly.

Stacking A and B therefore gives a direct full-plane cover. Its rows advance by positive vertical amounts, and their joint boundary graphs are bounded fluctuations about increasing row offsets, so neither holes at infinity nor hidden finite-patch extension assumptions occur. The mixed fixture has independent periods `(1,0)` and `(1,23/8)`. The A-only and B-only fixtures use a polygon and its allowed halfturned copy and have periods `(1,0)` together with `(1,19/8)` or `(1,27/8)`. The area checks agree with these exact fundamental-domain determinants. Thus omission is established even if arbitrary other tilings of these polygons have no intrinsic rows.

For the general finite-state theorem, follow a chosen directed cycle and translate every succeeding independently usable strip by the accumulated previous displacement. Each upper boundary equals the next lower boundary as a complete graph. Let the cumulative cycle displacement be `(Delta,D)`. Averaging the strict pointwise strip gaps gives `d_e+mean(f_t)-mean(f_s)>0`, because translation does not change a continuous periodic function's mean. Summing along the cycle gives `D>0`; this works unchanged for irrational horizontal phases. The cycle boundary translated by `n*(Delta,D)` is `nD+f_s(x-nDelta)`, which diverges uniformly in both vertical directions because f_s is bounded. Hence all cycle copies cover the plane. The two period vectors are independent since their determinant is `uD>0`.

I specifically attacked the possibility that a horizontal period or arbitrary finite transition graph alone implies the theorem. It does not; the statement expressly requires complete geometric states, independently reusable strips, bounded periodic graph boundaries and positive pointwise gap. These hypotheses exclude the hidden dependence on adjacent rows that would invalidate choosing and repeating a graph cycle. A finite bi-infinite path indeed has a repeated state on its forward half, giving a directed cycle. No theorem about arbitrary two-hexagon pairs follows, and the artifact correctly preserves that limitation.

The independent bounded checker additionally tests a very thin rational strip fixture and a phase-independent irrational example: boundary functions tau and 2*tau, edge vertical shifts 3, and arbitrary real horizontal phases. Both gaps are bounded below by 1; their mean gaps telescope to cycle height 6. This checks the claimed mechanism for irrational phases without numerical approximation or a larger census.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/two-hexagon-strip-cycle-independent-2026-10-14.py

No mathematical defect found. The stopping condition is decisive: independent finite-state row reuse must change before restarting this mechanism; selecting a nonperiodic row word does not remove its periodic cycle escape.
