# Independent actual-phase review for the mixed homogeneous pp slice

**Verdict: VALID for the exact metric filter.** The complete arrangement, native stars and strong duals require their separate independent review. Root did not develop this slice. The independent checker `verify_mixed_pp_actual_phase_independent.py` imports no author modules and uses cosine polynomial factors instead of the author's tangent expressions.

The specified native p arc has unit resultant

    P_alpha=1+exp(i(180-alpha))+exp(i alpha)=1+2i sin(alpha).

For90<alpha<180 its real part is1 and its imaginary part is positive. It never vanishes and its principal phase rho is in(0,90). Put c=cos(alpha), so -1<c<0 and sin(alpha)>0. If alpha+rho180, the necessary imaginary part after rotating byalpha, divided by the nonzero sine, is1+2c. Its only root is c=-1/2. If rho=2alpha-180, the necessary imaginary part after rotating by-2alpha, divided by the sine, is

    2*(2c^2-1-c)=2*(2c+1)*(c-1).

The root c1 is outside the stipulated interval. Both phase conditions therefore force c=-1/2, giving alpha120 because cosine is one-to-one on that interval. The alternative condition alpha120 already gives that result directly. At this angle P=(1,sqrt3), rho60 and its magnitude2, so p=cos(delta). Direct evaluation supplies the principal phase and real-ray signs; necessary imaginary tests are not treated as converses on arbitrary complex rays. No zero sine, chain zero, denominator pole or extra cosine root is discarded.

The checker independently reconstructs each of the22 necessary-primal row spaces and finds at least one of alpha120, alpha+rho180 or rho=2alpha-180 in it. Every authoring metric-filter condition and possible/impossible flag matches. At alpha120/rho60 all21 exceptional plane constants cancel. Exactly indices[4,5,12,16,17] have zero delta coefficient; the rest are nonzero multiples ofdelta and cannot vanish fordelta>0. Stratum73 alone has that complete active set and contains the actual metric candidate. Larger generic strata omitting a compulsory equation do not create further survivors.

The raw B directions at the candidate are(0,60,120,180-delta,240+delta,300-delta), equal to the previously reviewed gamma60 periodic cone. The strict domain alpha-rho+delta<120 holds for the entire0<delta<30 interval, and p differs from1 there. Thus the metric filter leaves the actual known periodic curve. The two phase implications and complete active-set treatment are valid on the entire stated slice, including all exceptional intersections.

Replay completed PASS:

```
conda run --no-capture-output -n arisearch python research/reviews/verify_mixed_pp_actual_phase_independent.py
```

This review does not claim that the opposite native qq ordering or every homogeneous resonance is equivalent to this slice. Native reflection swaps both pp and qq corner orders, so transferring a result without tracking both orders would omit cases. The unrestricted target remains unresolved.
