# Fresh root review of the single120 actual-phase filter

**Verdict: VALID for the exact nonlinear filter and its use after the separate complete arrangement/dual audit.** Root did not develop this slice or its authoring filter. The no-author-import checker `verify_single_120_actual_phase_independent.py` independently reconstructs the actual raw three-edge complex arc using a one-variable half-angle field overQ(sqrt3), rather than the author's two-variable sine-difference calculation.

For beta in(0,180), let t=tan(beta/2)>0 and w=sqrt3. The actual arc has real/imaginary parts

    Pr=(1+2t^2-wt)/(1+t^2), Pi=(wt^2+t)/(1+t^2).

Its real numerator has negative discriminant and positive leading coefficient, and Pi>0, so the principal rho is in(0,90), with no omitted zero arc. If rho60, the imaginary part after rotation by-60 is

    -w*(t-1/w)*(t-w)/(2*(1+t^2)).

All positive roots are exactly1/w andw, giving beta60 and120. Both have actual phase60 with positive rotated real part. The beta60 branch gives m3=180+delta>180 and is outside the actual strict domain. If rho+beta180, the imaginary part after rotation bybeta is

    t*(3-wt)/(1+t^2).

The only positive root isw; the zero root is outside beta's open domain. This gives beta120 and rho60. There are no denominator poles. At beta120 the arc is(1,w), length2, hence p=cos(delta); the exact B directions coincide with the previously reviewed gamma60 periodic cone.

The independent checker reconstructs row-space membership for all14 retained necessary primals. Every one implies beta120, rho60 or rho+beta180. It independently verifies every retained author filter condition and flag. At the only actual candidate(beta120,rho60), all14 planes have zero constant term and only equations1,6,9 have zero delta coefficient; all others are nonzero multiples ofdelta. Thus the full active set is exactly[1,6,9], and stratum33 is the sole actual surviving stratum. Larger generic flats cannot silently retain additional actual metric points because their omitted active equalities are compulsory at the candidate.

The first checker run failed because it compared Sage's unsorted root list to an ordered list. That implementation-only assertion was replaced by exact set equality; the repaired complete checker passed. No mathematical formula or retained author certificate was changed.

Replay:

```
conda run --no-capture-output -n arisearch python research/reviews/verify_single_120_actual_phase_independent.py
```

PASS all14 necessary-primal filters, exact positive half-angle roots, inadmissible beta60 branch and complete active-set classification. This review does not independently certify the48 star inventory,470 generators,34 duals or14 primals; those have separate fresh review. Together with that accepted audit and the reviewed periodic curve, it establishes the specified full-slice classification. It does not classify all homogeneous resonance hexagons or solve the unrestricted two-polygon problem.
