# Independent hostile review: right-angle pentagon / symmetric octagon carrier

Date:2026-10-13. Reviewer: source_recovery, independent of contact_structure.
Claim reviewed: research/lemmas/contact-structure-right-pentagon-octagon-periodic-carrier.md,
including its arbitrary positive b,g,c family. Verdict: VALID under its explicit
hypotheses. No generic-angle-palette classification is inferred.

## Exact shapes and field checked

Let t=sqrt2-1>0, s=b+tg, a=c+s, d=b+s, W=2a+g, with b,g,c>0.
The octagon consecutive vertices are
(a,b),(c,d),(-c,d),(-a,b),(-a,-b),(-c,-d),(c,-d),(a,-b).
Its side vectors alternate axial vectors and diagonal vectors with equal
absolute components s. The axial lengths are2b and2c and the diagonal
lengths sqrt2*s; all eight interior angles are135 degrees.

The pentagon is (0,-b),(g,-s),(g+s,0),(g,s),(0,b).
Its edge directions in cyclic order are -pi/8,pi/4,3pi/4,9pi/8,3pi/2.
The corresponding positive turns are3pi/8,pi/2,3pi/8,3pi/8,3pi/8,
so its one90 corner and four112.5 corners are genuine. Positivity excludes
zero sides. All rational b,g,c produce exact Q(sqrt2) coordinates.
Reflections used by the construction are allowed by the original problem.

## Attempted defect: seams may not exhaust widened banks

This is the main potential omission in the column proof: a seam graph only
has x-domain[a,a+g], whereas the channel extends beyond that strip. I checked
coverage by horizontal slices instead of presuming the band description.

Take column0 centres (0,2kd), column1 centres (W,d+2kd). Let L(y),R(y)
be their respective right and left banks. On the full halfperiod0<=y<=d,

    L(y)=a                        for0<=y<=b,
         a+b-y                    forb<=y<=d;
    R(y)=a+g+s-y                  for0<=y<=s,
         a+g                      fors<=y<=d.

This follows directly from the axial and45-degree octagon sides and uses
s>b, d=b+s. The channel is exactly[L(y),R(y)]. Its width is positive.

Write P0=P+(a,0) and Pd=J(P)+(a+g,d), J(x,y)=(-x,y).
Their horizontal sections are:

    0<=y<=b: P0=[a,R(y)]; Pd empty (except boundary at y=b).
    b<=y<=s: P0=[a+(y-b)/t,R(y)],
              Pd=[L(y),a+(y-b)/t].
    s<=y<=d: P0 empty (except boundary at y=s), Pd=[L(y),a+g].

The intermediate intervals have correct endpoint order: the right endpoint
of P0 minus its left is linear in y, positive at y=b and zero at y=s,
since s-b=tg. The Pd interval is positive for interior heights. Consequently
the two polygons cover the entire channel slice and share no interior
points. At endpoints they meet only in boundary segments or points.
The banks are even in y; reflection y->-y sends Pd to the corresponding
P centred at-d and fixes P0. Thus these checks cover[-d,d]. Translation
by(0,2d) covers the whole channel. Translation by(W,d) covers every channel.

Each octagon column fills its own region between banks; successive members
touch on horizontal sides. Different columns are disjoint becauseW>2a.
Every plane point either lies in an octagon column or a channel. This proves
allplane coverage and disjoint interiors, including widened channel portions.

## Area, period and angle inventories checked

Direct shoelace gives area(Q)=4ad-2s^2 and area(P)=g(b+s)+s^2.
Their sum area(Q)+2area(P)=2dW is the lattice covolume. This check is
supplementary to the complete slice proof.
The two period vectors(W,d),(0,2d) have positive determinant2dW.
The regular specialization b=g=c=1 gives s=sqrt2,a=d=1+sqrt2,
Qside2, area(Q)=8+8sqrt2, area(P)=3+sqrt2.

For the angle inventory write units of22.5degrees. The angles are4,5,6.
The full-star equation4x+5y+6z=16 has exactly
(x,y,z)=(4,0,0),(1,0,2),(0,2,1).
The flat-star equation4x+5y+6z=8 has only(2,0,0).
These establish the stated full and partial-contact stars without relying
on an edge-to-edge assumption for arbitrary admitted tilings. Each P112.5
corner cannot be surrounded by P-only sectors, nor lie opposite a flat
sector with P-only sectors. Thus P cannot tile alone. Q alone cannot tile
because every local corner star would require an integer multiple of135
equal to360 or180, neither possible. This directly verifies the monohedral
nonexistence claims here without importing a convex n>=7 theorem.

## Scope and remaining uncertainty

The construction proves periodicity for this explicit three-positive-parameter
metric family, regardless of other tilings the same shapes admit. It does not
prove any arbitrary-metric pair with the same angle palette periodic. It uses
reflections, which are expressly admitted. No limit argument, finite patch
extension or area-only plane covering is assumed. No unresolved defect remains
in the reviewed family.
