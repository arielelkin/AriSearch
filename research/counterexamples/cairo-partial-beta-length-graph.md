# A beta vertex does not equate whole native side lengths

**Status:** exact finite patch diagnostic, internally checked. It refutes a
local inference; no global monohedral plane-tiling extension is claimed.

Use the exact pentagon A from
[cairo-two-scalene-periodic.md](../lemmas/cairo-two-scalene-periodic.md), with
p=1,r=1/2,q=sqrt3-1/2. Let v4=(-r/2,sqrt3*r/2), and let R90(x,y)=(-y,x).
Take the three congruent placements

    T1=A,
    T2=v4-A,
    T3=(p,-q)+R90(A).

All three have a120-degree native corner at the origin: T1 uses corner after
side4, T2 uses corner after side3, T3 uses corner after side1. By convexity T1
lies in the closed120-degree cone with rays at0 and120 degrees; T2 lies in the
cone with rays120 and240; T3 lies in the cone with rays240 and360. Hence their
interiors are pairwise disjoint. Their sectors cover a neighborhood of the
origin, so this is a locally valid three-beta-corner star.

T1 and T2 share their whole length-r fifth sides from0 to v4. On the ray at0
degrees, T1 has a whole native side of lengthq while T3 has a whole native side
of lengthp. They share the initial lengthp segment only, since q>p. The same
partial length-p contact occurs on the ray at240 degrees between T2 and T3.
At the end of either length-p contact, T3 has a right corner, while the other
pentagon's native length-q side continues. This is the local geometric origin
of a possible90+90 T-junction when another tile fills the remaining gap.

Therefore the fact that the initial vertex has three120-degree native corners
does not force its incident full native side lengths to agree. In particular,
one cannot use numerical native lengths as the three ray labels of a local
corner graph unless full-side matching has been established separately.

For the concrete A, the private fifth side r cannot be split into two full
opposite sides because r is shorter than twice the minimum native length.
That observation still does not force the two outgoing length-q sides at its
beta endpoints to match full length-q sides: the patch above uses length-p
opposite edges and terminates them at right corners. The analogous issue
arises for B's private fifth side. The proposed unrestricted monohedral
exclusion from a beta-length graph is therefore unproved.

The exact verifier of the parent object checks the algebraic geometry; the
cone placements and native side lengths above give a direct proof of this
finite patch. No picture or numerical approximation is needed.
