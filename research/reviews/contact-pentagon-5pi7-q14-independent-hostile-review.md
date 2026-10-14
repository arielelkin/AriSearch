# Fresh independent hostile review: exact P5/Q14 candidate and one-Q adversary

Date: 2026-10-14. Reviewer: construction-adversary agent, independent of the author. Verdict: VALID for the exact native-ring and geometric mandatory-dimer counts, and for exclusion of the fixed one-Q translation-orbit periodic model. Plane tileability and unrestricted aperiodicity remain UNRESOLVED. The same-patch native-palette audit excludes336 of364 geometrically disjoint completions;28 pass its two necessary checks.

## Reviewed claims and independent implementation

Reviewed [the exact experiment](../searches/contact-pentagon-5pi7-q14-exact.md), [producer](../searches/contact-pentagon-5pi7-q14-exact.py) and [frozen certificate](../certificates/contact-pentagon-5pi7-q14-exact.json). The [independent checker](construction-adversary-2026-10-14-p5q14-independent.py) imports no author module, guest list, patch geometry or producer verdict. It reconstructs cyclotomic coordinates, native-side isometries, endpoint transition cycles, alpha reflection mates, and exact separating axes directly. Its [certificate](../certificates/construction-adversary-2026-10-14-p5q14-independent.json) retains every cycle and result.

Take z=exp(i*pi/14), i=z^7 and s=(z-z^-1)/(2i). The exact ordered P lengths are (1,1,1,v,y), y=2s+4s^2, v=1+2s(1-y), with edge exponents (-5,1,7,13,19). Their turn increments are (4,6,6,6,6) units pi/14, giving one alpha=5pi/7 and four beta=4pi/7 corners. The independent reconstruction verifies exact closure, 0<y<1<v and every strict supporting halfplane. Q edges have exponents2k and lengths1 or v; convexity and closure are checked for every retained word.

## Source deductions and completeness audited

All angles exceed pi/2 and are less than pi. No flat-host star is possible, and four native corners cannot meet. Consequently actual plane contacts are whole and trivalent. The complete integer equation5A+4B+6C=14 has only PPP=(2,1,0) and PPQ=(0,2,1); no QQ contact is possible.

At a PPP star its two alpha copies share one whole alpha-alpha edge. If that edge uses one bevel value, the other two incident bevels have equal other value; the beta guest must have an equal pair (x,x) or (y,y). The six necessary equality planes in the candidate note follow by exhausting its four beta native pairs. For this fixed P, only beta corners1 and2 have equal eligible pairs, both(1,1), so the alpha-alpha edge must be native y. Matching alpha to alpha fixes endpoints; the unique opposite-side mate is reflection in y. Its beta-beta endpoint requires Qgamma, forcing every native v side to meet Q. Its adjacent w side must meet P. The x side has an alpha endpoint and cannot meet Q. Only u and v can be Q contacts, even though x=u=w numerically.

The independent raw native-attachment control retains all six unit-side aliases/reflections and both v-side hands before applying those source deductions. Thus the reduction does not silently replace native side identities by numerical equality classes.

Uniform boundary-strip errors give PPP=p/2+O(R), PPQ=14q+O(R), and4p=PPP+2PPQ+O(R), hence p=8q+O(R). Exactly one v-Q side per P gives p=kq+O(R), where k is the fixed number of v sides of the one Q congruence class. Area coverage and p=8q+O(R) imply q=Theta(R^2), so k=8. The other six Q sides have unit length. Reflections preserve these native multiplicities; no absolute frequency or favored source tiling is assumed.

The complete binary closure check exhausts C(14,8)=3003 words and finds35. Independently, with t=z^2, D(T)=sum_(j=0)^6(epsilon_j-epsilon_(j+7))T^j vanishes at t, so D=c Phi14. Its coefficients in {-1,0,1} imply c=0,+1,-1. A nonzero c gives one v per opposite pair, totaling7 rather than8. Hence opposite lengths agree and the35 seven-bit3u/4v words are complete for this fixed P and the derived palette/count domain.

## Exact computational outcomes and repairs

The independent checker reproduces all35 closed words,14 with native cycles,896 pairwise-disjoint Q/guest cycles,364 disjoint mandatory-dimer21-face patches and532 forced positive-area overlaps. Per-word cycle sets and per-cycle completion/rejection identities agree exactly with the author certificate after accounting for the opposite ordering of reflection hands. The displayed word has64 native cycles and36 disjoint completions. A nonoverlapping finite patch is not an extension proof.

The audit targeted reflected winding, the x=u=w aliases, a missing alpha/dimer case, noncentral Q closure words, omitted native endpoint matches, false finite-patch existence inference, and count/frequency assumptions. An initial transmitted sine formula used the wrong cyclotomic exponent; the frozen producer uses the corrected expression above and independent closure passes. An earlier working summary conflated all896 native cycles with dimer-completed cycles. The final producer and note distinguish364 completions from532 overlap rejections; the independent check confirms the repair. No defect remains in those scoped geometric counts.

P alone is excluded analytically: its only full native star has2alpha/1beta. Native weights(alpha,beta)=(1,-2) make that star score0 but each P tile score-7; whole-plane counts would force positive quadratic tile count to be O(R). Q alone has neither a full nor flat-host star. These omission exclusions are not inferred from the separate unsuccessful thirty-case P periodic-motif search.

## Actual periodic counterexample search within the loop

The agreed finite model is one Q orbit under translations, with a primitive periodic cell containing1Q/8P. Intrinsic Q symmetries representing the same translated polygon set are included. For each of364 disjoint mandatory-dimer states, every Q-u guest has its distinct native P-v side obligatorily meeting another Q. For a reflected P guest, that edge's native orientation is clockwise; the checker reverses the required Q direction accordingly. It tries every native v side of Q and solves the exact endpoint translation. Each of364 states lacks such a translated-Q match for at least one mandatory v contact.

Therefore no candidate in this one-Q model supplies a periodic escape. Every retained state requires some differently oriented Q, so the model fails before any lattice search. No Hermite-normal-form, lattice-index, larger torus or strip search was run after that failure. This is a complete negative for the stated one-Q orbit model, not a proof of aperiodicity, untileability, or failure of larger periodic motifs.

## Remaining local and global gates

The [same-patch native-palette checker](construction-adversary-2026-10-14-p5q14-palette.py) separately tests all364 geometrically disjoint completions for forbidden corner-in-edge contacts and native corner multisets that cannot extend to PPP or PPQ. These tests add no patch depth or metric domain. Its [certificate](../certificates/construction-adversary-2026-10-14-p5q14-palette.json) records all364 exact word/cycle outcomes. There are336 forbidden corner-in-edge contacts and28 states with neither a T contact nor an unextendable native-corner multiset. No extra star-only rejection occurs. Exactly the seven cyclic rotations of vvuvvuu retain four states each (28 total). The other seven native-ring words, with one four-v run, retain none. An earlier inferred two-per-word summary was wrong; the correction is checked directly from the retained pass records. Every rejected state records the exact offending native corner, host segment and face indices in the cyclotomic basis. A corner inside another side is impossible in the all-obtuse palette: the host contributes pi, leaving less than the minimum available corner after the positive native corner has been placed. All coincident corner occurrences are counted with reflected native indexing preserved. The separate author reconstruction and [fresh palette review](contact-pentagon-5pi7-q14-exact-palette-review.md) validate all336 pointed T witnesses and all28 pass records without importing this checker. The28 passes certify only absence of these two tested obstructions; they do not prove arbitrary missing sectors can be filled or that the patch extends to the plane.

Even a surviving locally extendable patch does not establish a plane tiling. No candidate has an intrinsic expanding decoder or a proved infinite cover. Moreover the no-pi native-star relation prevents boundary subdivision in a finite polygonal parent dissection: each genuine straight parent side lies in one bounded native atomic edge. A fixed finite polygonal-parent similarity hierarchy cannot iterate expansively with these fixed atoms. This strategy obstruction does not classify all admitted plane tilings.

## Replay

```text
mise exec -- conda run --no-capture-output -n arisearch python research/reviews/construction-adversary-2026-10-14-p5q14-independent.py --check research/certificates/construction-adversary-2026-10-14-p5q14-independent.json
mise exec -- conda run --no-capture-output -n arisearch python research/reviews/construction-adversary-2026-10-14-p5q14-palette.py --check research/certificates/construction-adversary-2026-10-14-p5q14-palette.json
```

No numerical tolerance, solver seed, timeout inference or quotient-size increase is used. The unrestricted mathematical target remains unresolved.
