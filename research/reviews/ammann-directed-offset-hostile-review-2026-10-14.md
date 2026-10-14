# Independent hostile review: directed X/Y offset gate

**Later status:** the subsequent [exact residual review](ammann-directed-offset-residual-hostile-review-2026-10-14.md) closes all four three-plus-one assignments. This record preserves the earlier UNKNOWN-stage review and its then-unresolved full gate; it is not the current restart state.

Date: 2026-10-14. Reviewer: independent adversary. Verdict: **UNRESOLVED for the full two-class gate**. The coordinate construction, reflection reduction, area formulas, and exclusion of the within-type 2+2 branch are valid under the stated strict interior and convexity hypotheses. Four 3+1 partitions remain unsolved. This is not a two-tile aperiodicity result.

## Claim and independent reconstruction

The claim reviewed is the local four-parameter gate in `../searches/ammann-directed-offset-gate-2026-10-14.md` and its producer script. I reconstructed the arrows and coordinates before reading that producer. Lemma 5 of `../lemmas/ammann-forcing-aperiodicity.md` gives the thin CCW edge list `AB:X A→B`, `BC:X C→B`, `CD:Y C→D`, `DA:Y A→D`; the thick list is `EF:X E→F`, `FG:Y F→G`, `GH:Y H→G`, `HE:X E→H`. The quadrilateral vertex graph is bipartite, so donor edges occur as an opposite pair and each shared edge has a donor on precisely one side. For a legal marked source, the same actual directed edge and parameters are seen on both sides; therefore a source partition can glue globally whenever every local sector passes the strict geometry checks.

For a normalized rhomb `A=(0,0), B=(1,0), C=(1+c,s), D=(c,s)`, write the donor nodes `p=(u,h_1)` and `q=(c+v,s-h_2)`. If the directed arrow on `AB` agrees with `A→B`, then `u=a_Z`; otherwise `u=1-a_Z`. If the arrow on `CD` agrees with `C→D`, then `v=1-a_Z`; otherwise `v=a_Z`. This is measured from the arrow tail, with the donor side selected independently. For the exterior apex on a receiving CCW edge `W→W+e`, use `W+f e+h_Z(e_y,-e_x)`, where `f=a_Z` for a forward arrow and `1-a_Z` for a reversed arrow. The receiving pentagons have cycles `(B,t_{BC},C,q,p)` and `(D,t_{DA},A,p,q)`. This reconstructs all eight indexed outputs without importing the producer.

In each rhomb, the two donated and two received triangles contain one X and one Y, so the two output areas sum to `s`. Independent shoelace expansion gives, for the base roles,

```
D_T = (aY-aX) sin36 + (cos36+1-aY) hX + (aX-1-cos36) hY,
D_K = (1-aX-aY) sin72 + (cos72+aY-1) hX + (aX-cos72) hY.
```

The alternate thin role has difference `-D_T`; the alternate thick role has `D_K`. A thin reflection across `BD` exchanges `A↔C`, preserves the X/Y arrows, and exchanges its two output indices. A thick reflection across `EG` exchanges `F↔H`, preserves X/Y arrows, and preserves output indices. Consequently the eight outputs reduce to four indexed congruence types even if a chosen infinite source happens to realize only one role of a rhomb type. This reduction uses permitted reflections and the inward normal selected from the actual donor side. It does not assume an arrow-tail parity shared by all rhombs.

## The analytic branch obstruction

Let `E_T` and `E_K` be

```
E_T = (aX-aY)(aX+aY-2) + hX^2-hY^2,
E_K = aX^2-aY^2+2aY+hX^2-hY^2-1.
```

My independent coordinate expansion gives `2 E_T` for the difference in the sums of squared pentagon edge lengths `T_0−T_1`, and `−2 E_K` for `K_0−K_1`. Thus internal congruence of both pairs implies `E_T=E_K=0`, whence `E_T−E_K=1−2aX=0` and `aX=1/2`. With `aY=1/2+d`, `hX=sin36·x`, `hY=sin36·y`, `δ=x−y`, and `φ=sin72/sin36`, the necessary area equalities become

```
d(1-x)+(cos36+1/2)δ=0,
d(x-φ)+(cos72-1/2)δ=0.
```

For `d≠0`, addition yields `δ/d=(φ−1)/(φ−1/2)>0`; the first equation gives `x=1+(cos36+1/2)(φ−1)/(φ−1/2)>1`. The donor node at thin `AB` then lies beyond the opposite support line, contradicting strict donor interior `hX<sin36`. Hence `d=0`, then `δ=0`: the only within-type 2+2 assignment has `aX=aY=1/2` and `hX=hY`. The already reviewed homogeneous-rhomb periodic omission applies when that old component has valid local geometry.

The two crosswise 2+2 assignments fail earlier: if `T_0≅K_0` and `T_1≅K_1`, or the crossed version, summing matched areas would give `sin36=sin72`. The four 3+1 partitions are not covered by either argument. In particular, unequal pair means alone do not rule out two area classes: one rhomb type can have two equal-area outputs while the other has one matching and one different output.

## Checks, defects, and residual scope

The independent script `ammann-directed-offset-independent-2026-10-14.py` uses its own case table and geometry functions. It symbolically checks all four source/role sector-area totals, output-area totals, signed differences, and squared-edge-sum invariants. At the exact asymmetric fixture `aX=2/5, aY=3/5, hX=sin36/10, hY=sin36/20`, it checks every nonincident support-line determinant of all sixteen sectors and all eight output pentagons is strictly positive, and verifies both role reflections by all ten squared vertex distances over cyclic shifts and reversal. The command is:

```
mise exec -- conda run --no-capture-output -n arisearch python research/reviews/ammann-directed-offset-independent-2026-10-14.py --fixture
```

The producer's initial Z3 run compared all ten squared distances under the ten dihedral correspondences for each required congruence. It encoded donor support inequalities and consecutive turns, but omitted nonincident pentagon support inequalities. For this layout the omission appears equivalent to the stronger domain: all four positive turns of a receiving quadrilateral give its strict convex cyclic order; its vertices lie in the source rhomb. The incoming apex lies in the exterior halfplane of the receiving base, so its two new edges cannot cross the quad's other edges. The resulting pentagon is simple, and five positive turns make it strictly convex. Nevertheless, the producer subsequently updated the script to encode **all nonincident strict support inequalities** for every sector and output, plus separating-axis conditions for every sector pair. I checked the form of those added constraints independently. The historical `UNKNOWN` result is from the earlier, weaker encoding; the updated strict encoding has not been solved and must not inherit that run as a solver result.

The historical finite search returned `UNKNOWN` (timeout) on the first 3+1 branch; its next branch was interrupted before any status. The current script is set to stop at the first `UNKNOWN`. Neither event is a satisfiable witness or an exclusion certificate. I did not rerun or enlarge NLSAT after the declared cap. The remaining 3+1 systems require a new analytic argument or a separately justified exact procedure before the local gate can be classified. The partitions nominally require two nonempty classes; equality of all four representatives is impossible anyway, since a thin output pair sums to `sin36` while a thick pair sums to `sin72`. Even an exact two-class local survivor would still require periodic omission and wrong-arrow attacks, and a geometric decoder valid for **all** unmarked tilings, including reflections, T contacts, alternate chords, and single-species tilings. No such decoder is currently established.

No claim of full validity is made for the constructor's unresolved solver branches. A repair or later exact survivor needs a fresh hostile review.
