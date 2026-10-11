# Independent actual-phase and periodic-transfer review for reversed qq

**Verdict: VALID for both actual metric filters and positive congruence transfers.** Complete native inventories, arrangements and duals are reviewed separately. Root did not develop the reversed slices or author filters. The no-author-import checker `verify_reverse_qq_actual_phases_independent.py` reconstructs the one-variable beta half-angle factors and alpha cosine factors directly.

The raw p arcs remain those in the forward slices, but B's q chain has directions rho+120+delta,rho+180-delta,rho+240+delta. Its sum is still-2cos(delta)exp(i rho). The actual strict mixed-angle bounds change to rho+beta>120-delta in the single120 slice and alpha-rho-delta<120 in the mixed pp slice. Every other native angle is strictly in(0,180) on the stated domain. In particular these conditions cannot be replaced by the forward inequalities.

For the single120 arc, beta in(0,180) gives t=tan(beta/2)>0 finite. Its real/imaginary parts are

    Pr=(1+2t^2-sqrt3*t)/(1+t^2), Pi=(sqrt3*t^2+t)/(1+t^2).

They are positive; the chain never vanishes. The necessary imaginary factors for rho60 and rho+beta180 are respectively

    -sqrt3*(t-1/sqrt3)*(t-sqrt3)/(2*(1+t^2));
    t*(3-sqrt3*t)/(1+t^2).

All14 necessary-primal row spaces force beta120, rho60 or rho+beta180. The first and third leave beta120; rho60 has exactly beta60 and120. Both now satisfy strict convexity: at beta60 the mixed angle is180-delta, not the inadmissible180+delta from the forward slice. The arc lengths are1 and2, respectively, giving p=2cos(delta) andcos(delta).

At beta120/rho60 all14 plane constants cancel and exactly indices[3,6,11] remain active fordelta>0. At beta60/rho60 each plane becomes an affine function ofdelta. The checker retains every exact interior root; the only root isdelta15. The full active set is[3] away from15 and[3,8] at15. Thus the complete actual strata are38,39,43, matching every author filter flag. No exceptional point on either actual curve is omitted.

For the mixed pp arc P=1+2i sin(alpha),90<alpha<180, every22 necessary-primal row space forces alpha120, alpha+rho180 or rho=2alpha-180. Divide the relevant imaginary parts by the nonzero positive sin(alpha), and write c=cos(alpha) in(-1,0). Their factors are1+2c and2*(2c+1)*(c-1). Only c=-1/2 is in the domain, so alpha120/rho60. The entire active set is[4,5,12,16,17], uniquely stratum73. Every author filter condition and possibility flag was independently compared.

The positive transfers are actual native isometries, verified by the raw affine edge-direction lists. Reflect B and reorder its side indices(2,1,0,5,4,3). At reversed beta60 no further rotation is needed; its new directions are(0,120,180,240-delta,300+delta,360-delta), exactly the reviewed complementary cone at alpha60 with p=2cos(delta). At reversed beta120, or mixed alpha120, rotate the reflected presentation by-60; the new directions are(0,60,120,180-delta,240+delta,300-delta), the reviewed first curve. The reflection exchanges both pp and qq orders and preserves the pppqqq length word. The A prototype remains the same unmarked shape. Both cone domains contain their stated parameters for every0<delta<30.

Replay completed PASS:

```
conda run --no-capture-output -n arisearch python research/reviews/verify_reverse_qq_actual_phases_independent.py
```

No denominator pole, zero chain, excluded trigonometric branch or hidden identification of native orders was found. Combining this filter with accepted complete arrangement/dual audits proves the specified reversed-slice outcomes. It does not classify arbitrary qq angles or unrestricted pairs of hexagons.
