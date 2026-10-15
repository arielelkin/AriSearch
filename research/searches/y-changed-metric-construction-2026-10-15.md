# Changed metric Y pentagons: exact closure and stopped construction gates

Date: 2026-10-15. Status: internally derived geometry and two failed
whole-edge construction gates. No new tiling candidate with existence.
No solver or finite patch census was run for this investigation.

## Complete reflection-symmetric metric parameterization

Fix theta=atan(t), with 1<t<1+sqrt(2), and assume theta/pi irrational
when using the seven-star atlas. Let x,y,R,z be positive and require

    R>(t-1)x, 0<z<ty.

The most general pentagons with the stated reflection axes and the
specified directed angle words, up to common Euclidean placement, are

    P=((0,0),(R,0),(R+x,tx),(tx,R+x),(0,R)),
    Q=((ty,y),(ty-z,y+z),(-ty+z,y+z),(-ty,y),(0,0)).

Their native metric words are

    P: RA=R, AB=L=x sqrt(1+t^2), BB=S=sqrt(2)[R-(t-1)x],
    Q: CG=U=sqrt(2)z, GG=H=2(ty-z), CD=V=y sqrt(1+t^2).

These formulas follow directly from the edge vectors: the P AB vector
is x(1,t), its BB vector is a positive multiple of (-1,1), and Q's
CD and CG vectors are positive multiples of (t,1) and (-1,1).
Reflection gives the second half of each boundary. The resulting interior
angles are exactly rabba and cggcd; positivity of the displayed edge
parameters and these angles strictly between zero and pi give strict
convexity. Conversely, those directions and reflection symmetry force
the displayed coordinate expressions.

For irrational theta/pi in this interval, both omission exclusions hold
independently of all these lengths. An A corner admits only native stars
aad or abg, requiring Q. It cannot lie against a flat side because its
flat residual theta is smaller than the least angle c. A G corner admits
only native stars rgg or abg, requiring P; its flat residual pi/4 is too
small. Therefore no P-only and no Q-only tiling exists. This is not an
existence proof for the pair.

The parent's newly excluded family is the special locus x=y=1,
z=(t+1)/3,R=(4t-2)/3, giving U=S,H=R,V=L. The general coordinates
above leave U,H,V independent subject to the one linear closure relation
H+sqrt(2)U=2t V/sqrt(1+t^2).

## Gate 1: equal long sides and short GG

The resonance R=L=V, U=H=S changes the original far-endpoint correlation:
Q GG has the short length S, so in principle it can match P BB.
But it cannot support a whole-edge tiling. Here P's R and A corners have
only length-R arms and Q's G has only length-S arms. The only stars
containing G are rgg and abg. Both would put a G across a native ray from
an R or A, impossible when R!=S. Thus no full-edge G is completable.
This is a local metric obstruction, not a plane-tiling search. It does
not exclude partial contacts in this metric locus. No independent partial
extension mechanism was found, so this construction gate is stopped.

## Gate 2: move CD to the right-arm length

Fix t=2,x=1 and put

    L=sqrt(5), R=1/(3/2-2/sqrt(5)), S=sqrt(2)(R-1),
    y=R/sqrt(5), z=R-1.

Then V=H=R and U=S. These are positive and S<R<L, with the exact
parameterization above. This changes Q CD from the old long L to R.
It makes the old whole-edge-disallowed rccd star metrically possible,
so it was a genuine change to the native contact atlas.

Nevertheless this branch has no whole-edge tiling. Its allowed G stars
are rgg and abg. Any rgg forces both actual A corners of its incident P
into abg because both RA arms match GG. Each corresponding AB length L
can match only another P AB. At its A endpoint that neighbor is B;
at the far endpoint the original B meets A and hence G. Both original
B corners therefore need G across their BB side, impossible because
there is no native length-S GG side. Thus rgg cannot occur.

Every P R is then in rrrr, as follows. The rrbc star would put
an R-length arm across a B, whose lengths L,S are both unequal to R.
For rccd, the two C corners each have arms (S,R). If the Cs are not
adjacent, each C would need R arms on both sides, impossible. Thus the
Cs are adjacent on their S arms, and R is adjacent to D across a
length-R ray. But that full RA/CD match identifies their far endpoints
A and C. No native angle star contains both A and C. A cannot lie against
a flat side either. This excludes rccd, using far endpoints rather than
merely its superficially compatible ray lengths.

At every rrrr star, all four RA sides are fully paired to other RA sides;
the far ends of each such pair put A next to A, hence in aad. Thus every
actual A corner of every P is aad. No abg can occur. Since rgg has already
been excluded, no Q G corner can occur either. Both species are
indispensable by the omission exclusions, yielding a contradiction.

Consequently Gate 2 also has no whole-edge tiling. This is not an
unrestricted-contact impossibility proof: a partial RA/CD contact could
avoid the A/C far-endpoint identification. An actual infinite assembly
using such partial contacts was not found, and that missing existence
step is theorem-strength without an explicit extension mechanism.
The gate is stopped rather than promoted as a construction or searched
in enlarging quotient sizes.

## Restart information

The concrete new object is Gate 2's exact pair, with both omission
exclusions and a changed local native endpoint atlas. Its whole-edge
assembly is now excluded by far-endpoint propagation. A useful restart
requires an explicit repeatable partial RA/CD contact mechanism. Neither gate is an aperiodic
pair, and this note does not claim a substantial construction result.
