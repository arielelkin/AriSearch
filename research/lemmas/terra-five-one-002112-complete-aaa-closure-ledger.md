# A002112 on the five-plus-one resonance: complete AAA equality/closure gate

Status: exact finite computational certificate with an independently authored checker; fresh hostile mathematical review pending. This is a necessary-condition ledger, not an infinite-tilability or periodicity theorem. The reviewed paired-stratum separator is a separate stable analytic result.

## Domain and decision rule, stated before computation

The A angle word is (x,x,z,y,y,z), where x in (112.5,126), x!=120, y=720-5x, z=4x-360. The saturated B word is (s,r,r,r,r,r), r=360-2x, s=360-2y. Only native BB mask {1,4} survives the endpoint palette for this A word. Reflections and all native A/B length aliases are included.

Finite domain: 8 native corner choices times 8 independent arm reversals for AAA; all 203 partitions of six A sides, retaining every coarsening of each resulting equality relation and excluding a0=a3 (reviewed H1 escape). There are 26 distinct non-H1 formal required partitions, whose full upward closure contains 42 actual partitions. “26” does not mean an inclusion-minimal antichain.

For each actual partition, the mathematical questions are: does positive closed A exist at some exact allowed angle, and can its sixteen native saturated B fan choices close with positive BB lengths? For surviving three-class closures, can both BB sides join an identical or reflected B while identifying the entire shared A at both endpoints? Empty positive closure excludes that stratum. A surviving closure demands a spatial or extension mechanism; it does not authorize a larger torus search. Four-class positive cones remain a separate obligation.

## Exact geometry and positivity

Set u=180-x in (54,67.5), u!=60, t=cos(u). The exact t interval is

    sqrt(2-sqrt(2))/2 < t < sqrt(10-2sqrt(5))/4, t!=1/2.

Writing U=exp(iu), the six A unit directions are (1,U,-U^5,-1,-U^-5,U^-1). Divide the imaginary closure row by positive sin(u). With P=T5(t)=16t^5-20t^3+5t and Q=U4(t)=16t^4-12t^2+1, the ungrouped closure matrix is

    [1, t, -P, -1, -P, t]
    [0, 1, -Q, 0, Q, -1].

Group columns by the actual length partition. All grouped matrices have rank two at every allowed t: the checker independently computes common minors and excludes every common-minor root in the interval, including isolated roots rather than testing only generic rank. Counts are:

| Actual classes | Matrix rank | Kernel dimension | Partitions |
|---|---:|---:|---:|
| 2 | 2 | 0 | 12 |
| 3 | 2 | 1 | 26 |
| 4 | 2 | 2 | 4 |

Thus the twelve two-class cases have no nonzero closed A, throughout the entire allowed interval. Three-class kernels are primitive cross products of the grouped columns. Strict positivity requires all components to have one strict sign. Distinct actual classes require pairwise unequal components; merged cases belong to their separate coarsened partition, and zero components are inadmissible. All component, difference, B-length and BB-length-equality roots are isolated over real algebraic numbers; every open cell and every interior critical point is checked. A positive closed edge cycle with strictly increasing native edge directions through one turn is a strictly convex polygon: its projection onto each inward edge normal first increases and then decreases to zero, with every nonincident vertex strictly inside that supporting half-plane. This establishes actual polygon closure; it does not establish spatial compatibility of a ring.

## B closure and full shared-A link gate

Central AB sides (0,2,3,5) choose native A sides from (2 or4, 1 or5, 1 or5, 2 or4), respectively. These sixteen choices precede any assumption of distinct lengths. B directions have R=180-2u and are exp(ijR), j=0,...,5. Its two unknown BB columns j=1,4 are independent in the allowed interval; det/sin(u)=32t^5-32t^3+6t has its only interior zero at excluded t=1/2. The independent checker obtains both BB numerators by Cramer's rule from Chebyshev recurrences for cos(jR), sin(jR)/sin(u).

For BB partners, the complete canonical B side tuple must agree either in forward order or in reverse order, side j mapping to 5-j under reflection fixing its unique s corner. Both BB sides and both endpoint maps are tested. At a shared ABB vertex, the exposed second native A side is 2→1,4→5,1→2,5→4. The partner must use that exact native side so the entire A polygon is identified, rather than only its two arm lengths. The sole alternative color-preserving native A automorphism is corner i→1-i, side j→-j; it is available only when a1=a5 and a2=a4. The gate includes that alternative when present. Additional aliases never license an angle-profile mismatch.

These are necessary shared-edge links; they do not verify disjointness of an entire four-A B fan or consistency of successive full chains.

## Exact result and residual ledger

Of the 26 three-class partitions, ten have no positive distinct A closure anywhere in the interval. Six more admit A closure but never positive saturated B closure:

    000112, 001122, 001222, 011120, 011220, 012200.

The remaining ten admit positive A and B closure on at least one exact interval, and each retains full shared-A BB links:

    001102, 001121, 001202, 010112, 010120,
    010122, 010220, 011202, 012110, 012202.

The certificate stores all exact angle cells and native choices. Counts of split cells are bookkeeping, not geometric invariants: 112 A-positive cells and 92 B-positive cells, with critical singleton cells included. The BB gate narrows native fan assignments but does not remove one of these ten families. Several survivors are palindromic B profiles (m,p,n,n,p,m), with reflected same-side BB matches; their presence explains why arm constraints alone cannot supply a blanket obstruction.

The four-class actual partitions remain open:

    001232, 010223, 012130, 012203.

Their grouped kernels have dimension two; no inference from the three-class classification covers these necessary ancestors. Every further specialization has nevertheless been included among the 42 actual partitions already classified or retained. The no-AAA branch is handled independently by root's periodic binary-fibre lift, whose fresh review is not a dependency audited here.

Next justified obligation: combine the surviving native BB states with the straight parallel B-row geometry of the opposite {1,4} mask. Check an exact obstruction to full-chain shared-A placement, or derive a periodic-extension mechanism for bounded A strips. Do not assume that arbitrary reversible chains or bounded strip widths force periodicity. For the four-class cases, use a two-dimensional positive-cone separator and native BB states before any patch growth.

## Certificate, replay, and implementation repairs

Producer: `research/searches/terra-five-one-002112-chebyshev-gate.py`.
Certificate: `research/certificates/terra-five-one-002112-chebyshev-gate.json`.
Independent checker: `research/reviews/verify_terra_five_one_002112_chebyshev_gate.py`.

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/searches/terra-five-one-002112-chebyshev-gate.py
    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_terra_five_one_002112_chebyshev_gate.py

The retained workaround skips installation of unrelated Puppeteer and does not bypass its provenance policy or mutate configuration. A first runner stalled because using ceil to sample strictly above dyadic lower endpoint1/2 repeatedly selected the endpoint itself; it was interrupted and repaired to floor+1. No mathematical result was inferred from that stalled run. Exact critical cuts and samples are retained by minimal polynomial and rational isolating interval; printed decimal endpoints are display only. The checker imports no producer code and reconstructs native directions, AAA connectivity, all partitions, ranks, roots, closure signs and shared-A BB links independently.

## Subsequent stronger result

The fresh independent native interface review `research/reviews/terra-five-one-002112-universal-interface-fresh-review.md` verifies root's all-metric obstruction: a boundary A row cannot have another A row on its inward side. Combined with opposite saturated B seams, this forces alternating A/B rows and removes every AAA-used branch, including the residual three- and four-class cases above. The earlier computational returns are retained as necessary-condition evidence and exact counterexamples; they are no longer the active extension blocker for A002112. The separately reviewed no-AAA binary lift then supplies periodic escape for the actual pair.
