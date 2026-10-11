# The two extra-sharing roots of the exceptional Cairo family are also untileable

**Status:** freshly independently hostile-reviewed **VALID**; see [review](../reviews/partial-contact-cairo-single-shared-roots-review.md). This is a new
native-slot proof at two exact previously excluded metrics. It must receive
its own audit before combining it with the open-interval obstruction.

## Exact root and conventions

Let w=sqrt3,r=5w-8=(2w-1)/(w+2),t=10-5w=2-r. The two Cairo shapes are

    P=(1,r,4-w,7-4w,2),
    Q=(r,4w-5,t,1,2).

Besides Pa=Qd=1, the extra arm equality is Pb=Qa=r. Each shape remains
internally four-distinct. Put B=Qb=4w-5. The result below proves this pair
admits no unrestricted plane tiling. The reflected parameter2-r has the
same conclusion by the explicit native-label symmetry at the end.

The angle convention and two-T contact invariant are as in the previous
Cairo artifacts. Denote the eight native arm slots by

    0=Pa,1=Pb,2=Pc,3=Pd,4=Qa,5=Qb,6=Qc,7=Qd,

with perpendicular complements(1,0,3,2,5,4,7,6).

## Exact necessary contact ledger, with native slots retained

The ten equal-perpendicular bank events, including self pairings, are

    (0,0):2; (0,5):B+1;
    (1,1):2r; (1,6):2;
    (2,2):2Pc; (3,3):2Pd;
    (4,4):2r; (5,5):2B; (6,6):2t; (7,7):2.

All displayed totals except the stated repetitions are mutually distinct.
For each actual arm i let S_i be the totals of events that contain that
slot. The exact two-T switch makes unequal opposing native arms i,j possible
only if S_i intersects S_j. Equal arm lengths may whole-match. This is a
necessary overapproximation that drops strict switch inequalities; it adds
no transitive closure. It is derived from the reviewed contact invariant
and is valid at these collisions, without a genericity assumption.

In particular actual Qb slot5 can oppose only native slots0 or5, of lengths
1 or B. An e2 side can oppose a native bank from a120 endpoint only if
that very bank slot belongs to an event totaling2. The only such slots are
0,1,6,7. Thus e2 cannot face Qb, nor Qa even though Qa and Pb have equal
numerical length r. This distinction is essential.

## A full Qc seam is impossible

A full native Qc seam can only mate the same globally private Qc slot.
Its90/120 endpoints force reflection preserving the native endpoint labels.
At its120 endpoint this places two isolated Q corners(Qb,Qc), each of120
degrees. The third120 sector would have to offer two rays compatible with
actual Qb slot5.

The six native120 corners are

    P:(Pa,e),(Pb,Pc),(Pd,e),
    Q:(Qa,e),(Qb,Qc),(Qd,e).

No e ray can face Qb, and neither native pair(Pb,Pc) nor(Qb,Qc) has both
arms among its compatible slots{0,5}. Therefore there is no third corner.
The full Qc seam is impossible in any admitted tiling, regardless of its
other contacts.

## P still has a forced fourfold cluster

Pc and Pd are globally private. Their bank-event totals2Pc and2Pd are
singleton and differ from e2. The same reviewed contact proof as in the
canonical cluster reduction makes every Pc/Pd seam whole and forces the
four reflected P copies around its private(c,d)90 corner. Thus every P
belongs to the same canonical macrotile S(r). This does not assume any
corresponding Q cluster; that previous conclusion is invalid at this root
and is deliberately not used.

A hypothetical tiling contains P, since Q alone has four distinct arms
and is monohedrally untileable by the reviewed private-arm theorem. Fix an
S(r) at the origin and its right-axis240 notch(d_r,0). Two original P120
sectors form that notch, whose two boundary rays are native e2 sides.
The missing120 sector must be one original tile's native120 corner.

Use the actual e2 bank slots0,1,6,7 above. Among the six native120 corners,
only P(Pa,e) and Q(Qd,e) can face those two e2 rays. P's isolated corner
has private Pc; Q's isolated corner has excluded Qb; the Pd corner is
excluded; Q(Qa,e) is excluded because actual Qa slot4 cannot bank e2.
Thus only these two filler types exist, with two physical orientation
choices each. Their unit and double edges fix their placements exactly as
in the earlier right-notch geometry. No Q macrotile is assumed.

For a Q(Qd,e) filler, the unit tip lies inside the host e2 side and forms a
T. Its perpendicular full native arm is Qc=t, forcing the full Qc seam
just proved impossible. Both orientation signs are excluded.

For a P(Pa,e) filler the unit tip similarly forms a T with perpendicular
Pb=r. Its possible full mate slots are Pb and Qa. A Qa mate has bank Qb=B,
so this event's total would be1+B rather than the host's2; it is excluded
by the e-host bank sum. Only a Pb mate, with bank Pa=1, remains. It is the
same-slot reflected P mate, whose canonical P cluster is reflection of
the filler P cluster across its bank line.

The universal reflected-cluster witness in the
[open-interval proof](partial-contact-cairo-single-shared-family-obstruction.md)
requires only z=r in(1/w,2-1/w), not the absence of other arm equalities.
It gives a strict overlap of two actual P constituent interiors. Since
both P clusters are canonically forced and distinct, that is impossible.
The lower orientation is its horizontal reflection. Every filler of the
one P notch is excluded, proving no plane tiling exists at r.

## Reflected root, exact replay and scope

Native Cairo reflection reverses arm labels by

    M(a,b,c,d,e)=(d,c,b,a,e).

The family identities are M(P(r))=Q(2-r), M(Q(r))=P(2-r). Reflection followed
by species swap therefore identifies the two tiling problems, including
all isometries and contacts. Hence parameter2-r=5/(w+2) is also untileable.

[Exact checker](../searches/partial-contact-cairo-single-shared-exceptional-roots.py)
reconstructs the two shapes, verifies every native equality, all ten events,
exact collision classes, native slot compatibilities and the six third
corner exclusions. It checks the e2 bank inventory, the T mate selection,
the reflection identities and a strict actual P overlap witness at this
root. Geometry and exhaustive angle-sector arguments are written above;
no extension search, solver or numerical angle decision is used.

Combined with the independently reviewed open-interval theorem, these proofs leave only r=1 in this family. The present file
asserts neither tiling nor periodicity at r=1 and is not an unrestricted
classification of Cairo pairs.
