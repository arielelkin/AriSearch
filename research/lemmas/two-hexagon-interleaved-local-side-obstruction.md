# Interleaved angle hexagons cannot have side period two

Date: 2026-10-12. Status: [independently reviewed VALID local necessary gate](../reviews/two-hexagon-interleaved-local-side-gate-review.md).
The later geometric and transport theorems separately handle the surviving rings.

Let A have native angle word (p,p,q,p,q,q), with p+q=240 degrees and
90<p<150, p!=120. Such a genuine strictly convex hexagon cannot have native
side lengths (E,O,E,O,E,O) for positive E,O.

To see this, orient side zero along angle zero and put alpha=180-p and
beta=180-q=p-60. The six native side directions, using the exterior turn at
the next corner, are

    0, alpha, 120, 120+alpha, 240, 240+beta.

The even-index side vectors of length E sum to zero. If omega=exp(2pi*i/3),
the sum of the odd-index side vectors of length O is

    O [exp(i alpha)(1+omega)+omega^2 exp(i beta)]
      = O omega^2 [exp(i beta)-exp(i alpha)].

Here angles in the exponent are interpreted in radians. Closure would require
alpha=beta modulo 360 degrees. Both lie between 30 and 90 degrees, so this
requires p=120, contrary to the hypothesis. Cyclic changes of the start and
reflections preserve the obstruction.

## Exhaustive local side-equality gate

In a legal full B ring, let A_k denote the A cell at direction D_k from B.
At B side slot k its neighbour is A_(k+1), whose matched side slot is k+3.
Consecutive A_k and A_(k+1) share side slots k+1 and k+4 respectively. Thus the
ring has exactly these twelve local whole-side seam equalities:

    B[k] = A_(k+1)[k+3],
    A_k[k+1] = A_(k+1)[k+4],       k=0,...,5.

Convert every side slot to its actual native index: r+k for placement (r,+1)
and r-k-1 for placement (r,-1). Take the exact equivalence closure of these
twelve equalities on the twelve native side variables of A and B. If that
closure identifies A0,A2,A4 and identifies A1,A3,A5, the local ring cannot
occur in any metric tiling of this family, by the closure argument above.
The two equivalence classes may coincide; that case is also impossible.

The [producer](../searches/two-hexagon-interleaved-local-side-gate.py) enumerates
each of the twelve native B placements. Its six independently chosen A
placements must have corner colours b[k],b[k-1] at slots k+2,k+3. Since A=I
has twelve distinct placed colour words, each is an actual unique native
placement. This finite Cartesian product is the complete full native ring
domain, including every reflected placement and repeated B colour word.
No global compatibility pruning or solver enters this census.

| Native A,B words | All native rings | Forbidden side-period-two rings | Remaining local rings | Distinct seam closures |
|---|---:|---:|---:|---:|
| I,C | 3072 | 384 | 2688 | 67 |
| I,I | 12288 | 6264 | 6024 | 105 |
| I,ALT | 49152 | 0 | 49152 | 1628 |

The [certificate](../certificates/two-hexagon-interleaved-local-side-gate.json)
retains every distinct closure, its exact multiplicity, the rejection flag,
and a full native B/A-ring representative. The ring counts independently
agree with the colour Cartesian-product counts multiplied by the native B
colour fibre sizes: 1536*2, 12288*1, and 8192*6.

The rejected counts give exact local geometric impossibilities. Remaining
rings are merely not excluded by this one test. In particular the zero count
of rejections for I,ALT supplies no positive global existence or periodicity
claim. A colour torus, a nonempty local ring set, or the absence of a period-two
forced closure does not solve the metric tiling problem.
