# Independent hostile review of the skew-flat closure obstruction

Date: 2026-10-15. **Verdict: VALID** for the exact conditional metric statement in [the lemma](../lemmas/hexagon-changed-word-skew-flat-metric-obstruction-2026-10-15.md). This is an optional branch result, not a dependency of the complete five-length periodicity classification.

I independently checked the complex closure identity, including its possible zero denominators. Set alpha=a0=2pi-u0-v0 and delta=p+q0-u0-v0. Then the two angle words give

    a1=b0=alpha-delta, b1=alpha, a2=p-delta, b2=p,
    a3=b3=q0, a4=b4=u0, a5-b5=delta.

After independently rotating both polygons to put side 0 in direction 1, let U=-exp(-i alpha) and Q=exp(i delta). Accumulating exterior turns pi minus the listed angles gives side 1 directions U,QU and a common side 2 direction QU^2. The first three interior-angle sums differ by -delta, so the A-side 3 direction is Q times the B-side 3 direction. The same holds for side 5, because the next two interior angles agree. For B-side 4 the accumulated angle is 2alpha-delta+p+q0=alpha+2pi, so its direction is -U and A-side 4 has direction -QU. These calculations verify every directional premise of the two displayed polygon closure equations, with the length words in their stated native order.

Subtracting Q times the B equation from the A equation eliminates both y and t and gives

    r(1-Q)(1+QU^2)+(1+Q)U(x-Qz)=0.

Strict convexity places a5,b5 in (0,pi), so |delta|<pi. Consequently H=exp(i delta/2) is nonzero, 1+Q is nonzero, and cos(delta/2)>0. Division by (1+Q)UH is therefore legitimate at every allowed metric, including delta=0. The r coefficient becomes

    -i tan(delta/2) * ((HU)^(-1)+HU),

which is purely imaginary because |HU|=1. The other term is xH^(-1)-zH, whose real part is (x-z)cos(delta/2). Its vanishing proves x=z without generic-rank assumptions.

I specifically checked delta=0, reflected reference orientations, independent initial rotations, and the possibility of coincident numerical lengths. A polygon may always be read in a positively oriented reference before this calculation; the conditional angle/length statement itself fixes its cyclic reading. No tiling hypothesis or realization of an abstract angle flat is used. Positivity and strict convexity rule out the only denominator failure at delta=+/-pi.

No defect or repair is needed. The identification of this angle word with a named support-certificate flat remains a separate finite provenance claim; this review establishes the standalone implication for precisely the displayed angle words. It neither excludes other flats nor resolves the unrestricted two-convex-polygon problem.
