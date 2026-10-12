# Joint closure reduces the remaining alternating metric domain to57 orbits

Date: 2026-10-12. Status: [independently reviewed VALID as part of the complete ALT/ALT chain](../reviews/two-hexagon-alternating-all-metric-chain-review.md).
This component retains its stated restricted domain; the full family conclusion
is in [the all-metric theorem](../lemmas/two-hexagon-alternating-all-metric-escape.md).

Use the fixed ALT/ALT angle family and parameter t of the
[complete metric ledger](two-hexagon-alternating-metric-ledger.md).
After the [A-side stratum gate](two-hexagon-alternating-a-side-strata.md), the
[three-value joint obstruction](two-hexagon-alternating-three-length-joint-obstruction.md),
and the reviewed side-period-two metric escape, the necessary domain remaining after these gates has61 native A partitions and20970 native B words.

## Exact native symmetry and shared-value bookkeeping

The cyclic corner words of both polygons are alternating. The six native
corner relabelings preserving these colours are rotations r+j and reflections
r-j, for r=0,2,4. Their native side maps are

    rotations: j -> r+j,
    reflections: j -> r-j-1,       modulo6.

Only these D3 maps are used, not a rotation by one native corner that swaps
p with q or r with s. Relabeling the native corners of a fixed polygon by
one such map preserves its native angle word. It changes its side word by
the displayed map and describes the same unmarked polygon up to a rigid
motion or reflection. The two coordinate closure rows are consequently
changed by an invertible orthogonal transformation, so their shared-value
kernel is preserved, for every admitted angle.

Canonicalize a pair(A side partition,B side word) as follows. Apply one of
the six A side maps, then rename actual length classes in first-occurrence
order so the A word is again a restricted-growth word. Apply that **same**
class-label permutation to all B side labels. Independently apply one of
the six B side maps. Choose the lexicographically least pair over these36
possibilities. Class values remain shared between A and B; independent
class renaming of B would be invalid and is not performed.

The metric ledger domain is invariant under these actions. A reflection
swaps native even/odd side counts and changes its AB-even occupancy h to1-h;
rotations preserve h. The nine unbalanced h values and continuous balanced
interval are invariant under this swap. B reflections/rotations do not change
native value multiplicities. Hence canonicalization stays within the complete
necessary domain and loses no actual unmarked metric pair.

The [producer](../searches/two-hexagon-alternating-joint-metric-orbits.py)
enumerates every native word once from each deduplicated multiplicity vector,
checks all per-partition multinomial counts and the total20970, and records
the full orbit multiplicity of every canonical pair in
[the certificate](../certificates/two-hexagon-alternating-joint-metric-orbits.json).
There are685 canonical joint geometry orbits:399 with four A values,
244 with five,42 with six. Orbit sizes may be less than36 because of
stabilizers; no fixed orbit size is assumed.

## Joint polygon closure and actual class distinction

For a canonical pair with k actual shared A side classes, form a4-by-k matrix
M using A directions(0,0),(1,-1),(2,0),(3,-1),(4,0),(5,-1) and B directions
(0,0),(1,2),(2,0),(3,2),(4,0),(5,2). A direction(j,m) means j*60+m*theta,
theta=120-p and t=tan(theta/2). Exact entries lie in Q(sqrt(3))(t), with only
powers of1+t^2 in their denominators. A shared class may be absent from B;
its B row entries are then zero, as required by the actual native word.

The all-ones class vector is in the joint kernel for every parameter. Generic
kernel relations that force two asserted actual classes equal exclude their
partition, unless a rank drop breaks the relation. The exact gcd of all
generic-rank minor numerators isolates every admitted rank-drop parameter.
At each such algebraic parameter, calculate the exact matrix kernel and its
forced class pairs again. Constant-rank continuity extends generic forced
relations across poles of a selected normalized kernel basis.

If no pair is forced equal, a positive vector with all class values distinct
exists in that kernel: perturb the all-ones vector in a direction avoiding
the finite union of coordinate-equality hyperplanes. This is a local polygon
closure fact. It gives no infinite compatible native placement field. Generic
positive labels also do not claim that every parameter in a generic orbit
has the same actual equality stratum; further isolated class-pair relations
could still restrict its admitted metric domain.

The complete exact outcomes are

| Outcome | Joint orbits | Original native metric words |
|---|---:|---:|
| No admitted actual metric | 628 | 19764 |
| Generic actual-class kernel | 45 | 990 |
| Actual-class kernel only at isolated admitted angles | 12 | 216 |

Thus a necessary remaining native domain has at most57 joint metric orbits,
equivalently1206 original native word cases. The12 isolated-angle orbits have
four or five A classes. Six have t=+/-tan10 degrees (p=100 or140); the others
have exact algebraic parameters with minimal polynomials and roots retained
in the certificate. Their values are not discarded by numerical approximation.

No native ring enumeration or SAT solver enters this reduction. Actual
tiling compatibility, full-plane existence and periodic metric escape must
still be checked for the57 retained orbits, with their complete actual
metric freedoms and exceptional angle conditions intact.
