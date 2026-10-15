# Native-occurrence propagation excludes whole-edge Y-pair coverings

**Later status (2026-10-15):** [unrestricted untileability](pentagon-y-unrestricted-2026-10-15.md)
now closes the former partial-contact gap for the fixed pair. This record
retains its original scoped proof; historical existence questions below are superseded.

Date: 2026-10-14. Status: fresh independent hostile review VALID; see
[review](../reviews/pentagon-y-no-full-edge-hostile-2026-10-14.md).
No conclusion for unrestricted partial contacts is asserted.

Let

    P=((0,0),(2,0),(3,2),(2,3),(0,2)),
    Q=((2,3),(1,4),(-1,4),(-2,3),(0,2)).

Theorem: no edge-to-edge plane covering by isometric copies of P and Q
exists, even with all reflections permitted. Here edge-to-edge means every
contact across a native side matches an entire native side, with no native
corner in another side's interior. This is stronger than the fixed6P4Q
flat-torus solver result and is proved independently of that solver.

## Exact local premises

Use theta=atan(2) and the exact corner
labels r=pi/2, a=pi-theta, b=pi/4+theta, c=3pi/4-theta,
g=3pi/4, d=2theta. Native words are P=r,a,b,b,a and Q=c,g,g,c,d.
Squared native lengths are P=4,5,2,5,4 and Q=2,4,2,5,5.
These geometry and irrational theta/pi premises passed the independent
interface-Y review. In particular theta coefficients may be compared
separately from pi/4 coefficients.

Every actual corner exceeds pi/3. Hence at most five native corners meet
at an edge-to-edge vertex. Exact angle enumeration gives seven possible
multisets: rgg,aad,abg,rrrr,rrbc,rccd,bbcc. Whole-side arm matching removes
rrbc and rccd. The remaining five-star atlas is therefore a necessary
length-compatible atlas, not an angle-only assertion. Each cyclic order
and both arm orientations are included in that gate.

In every length-compatible rgg star, the gg ray has squared length2 and
the two rg rays have squared length4. In every abg star, ab has squared
length5, ag has squared length4, and bg has squared length2. This follows
from r arms(4,4), a arms(4,5), b arms(5,2), g arms(2,4). The only atlas
star containing a+g or a+b is abg; the only one containing r+g is rgg.
All these assertions were independently checked in the full-edge torus
balance review. They remain valid for each actual native occurrence.

## Propagation contradiction

Suppose a whole-edge plane covering contains a Q. Its unique native GG
side has squared length4. The only native sides of that length in the pair
are Q's GG and P's RA sides. A Q-Q match would require a gg adjacency on a
length4 ray. Only rgg can contain the two g corners, but its gg ray has
length-squared2. Thus the Q side must match a P RA side.

At the R-G endpoint, the incident P R corner lies in an rgg star. Consider
this particular P tile, retaining its actual native vertices. Both sides
incident to its R have squared length4. In the rgg star both neighboring
corners across these sides are G. Since the only native length4 side at a
G is Q's GG, both P RA sides match Q GG sides. At their far endpoints this
same P's two actual A corners consequently meet G corners. Each such A
corner must lie in an abg star.

Now follow each of those two A corners along this P's incident length5
side. At an abg star the length5 ray is AB, so the neighboring corner is B.
The only native length5 side incident to B is a P AB side. The opposite
endpoint therefore identifies the original P's B with its neighbor's A.
Only abg can contain A+B, so both actual B corners of the original P lie
in abg stars. This uses whole-side far endpoints and the native A-B-B-A
arrangement; it cannot be inferred from the angle word's counts alone.

The side connecting the original P's two B corners has squared length2.
At each endpoint, an abg B's length2 ray must meet G. A full native-side
mate for this particular BB side would thus have to be a GG side of squared
length2. No such side exists: P's length2 side is BB, Q's length2 sides are
CG, and Q's GG side has squared length4. This is a contradiction.

Hence no Q can occur. A P-only whole-edge covering is also impossible:
within the five-star atlas the only P-only star is rrrr, so no actual A or B
corner of P can be completed. Alternatively the already reviewed omission
proof excludes P-only tilings even with partial contacts. Thus no whole-edge
plane covering exists.

Reflections reverse the cyclic native words while preserving the two RA
sides, the two AB sides, and the BB side of the particular P. The propagation
uses actual indexed occurrences and far endpoints, so it does not assume a
preferred handedness, global orientation, periodicity, or a finite quotient.
No flat-torus development or speculative global geometry is needed.

## Scope and stopping condition

This theorem stops the entire full-native-edge track for this pair, not
merely the minimal6P4Q torus. It does not exclude a mixed plane covering
with side subdivision or T contacts. There the BB side may meet several
different sides and its two G requirements need not belong to one tile;
the final native-side contradiction can fail. Therefore the atomic pair's
unrestricted existence and universal recognition remain unresolved.

Restarting must change the whole-native-edge assumption or the actual
polygons' native endpoint correlations. Increasing the number of whole-edge
faces cannot repair this contradiction. The fixed CP-SAT run and its bounded
INFEASIBLE status remain separately recorded and are not used as a theorem
about infinite coverings.

Independent exact Sage replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/pentagon-y-no-full-edge-independent-2026-10-14.py

Completed successfully; the checker independently reconstructs actual native
angles, all reflected ray records, and the far-endpoint propagation.
