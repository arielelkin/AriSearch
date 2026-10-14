# Fresh hostile review: irrational three-triangle fan angle obstruction

Date:2026-10-13. Claim reviewed:
research/lemmas/three-triangle-irrational-fan-angle-obstruction.md.
Reviewer source_recovery did not develop this theorem. Verdict: VALID.

## Quantifiers and pointwise contradiction

The theorem assumes a FINITE protoset and fixed irrational theta/pi, with
positive rational ri and0<ri theta<pi/3. Finiteness ensures a maximum ri
among classes ACTUALLY USED. At a central corner of such a maximum tile,
local finiteness makes the incident sectors finite. Each incident tile has
either a genuine angle sector or a straight pi sector. An interior tile
sector is impossible at a native corner of another tile because it would
intersect that tile's positive interior sector. Two straight sectors likewise
leave no room for the selected native corner. Thus the native angle sum is
h*pi for h=1 or2. This does not assume edge-to-edge contacts.

In the angle equation the pi coefficient is sum(bi/2+ci) and the theta
coefficient is sum(3ri ai-ri bi/2-ri ci), both rational. Irrationality forces
both coefficients separately. The second gives

    3r <= sum(3ri ai) = sum ri(bi/2+ci) <= r*h <=2r,

where the first inequality uses the selected maximum-species central corner.
All corners present at this star belong to species occurring in the tiling,
so ri<=r is justified. r>0 yields a strict contradiction. No frequency,
limiting measure, hierarchy or extension assumption occurs. Missing species
and reflected copies are explicitly covered. Equal angles could be labelled
by occurrence instead of magnitude; no hidden distinction assumption is needed.

## Attempts to break the theorem

- A T-junction gives h=1 and strengthens the contradiction.
- A tiling omitting the species with globally largest parameter still has
  a largest parameter among used species; the same proof applies.
- Species with the same parameter add no exception to3r<=2r.
- A central angle coinciding with another category would imply theta/pi
  rational; occurrence labels would suffice even without this observation.
- A corner supported by a long side with interior vertices is still a flat
  sector, not an omitted angle.
- Local finiteness follows from the uniform diameter and positive minimum
  area of finitely many prototiles; tiles meeting a compact region all fit
  in a fixed enlargement and have disjoint positive-area interiors.

No defect found.

## Exact example independently checked

Let u=(2+i)/sqrt5, theta=arg u=arctan(1/2). Then0<theta<pi/6 because
1/2<1/sqrt3. Therefore both ri=1 andri=2 satisfy ri theta<pi/3.
All six radial fan triangles have unit equal radial sides, with central angles
theta or2theta in their respective fans. The three-triangle union is the
cyclic pentagon(0,1,u,u^2,u^3), or(0,1,u^2,u^4,u^6).
Its central corner is3ri theta; the two endpoints have(pi-ri theta)/2;
the two intermediate arc vertices have pi-ri theta. Since3ri theta<pi,
all are genuine convex corners.

Independent exact support inequalities confirmed both cyclic polygons are
strictly convex. Their areas are respectively

    area(P1)=3 sin(theta)/2=3/(2sqrt5),
    area(P2)=3 sin(2theta)/2=6/5.

These are unequal, so the classes are distinct without relying on angle-set
permutation arguments. The original proof's angle distinction is also valid:
equality of central3theta with either other P2 category would make theta/pi
rational.

If theta/pi were rational then exp(2i theta) is a root of unity; its sum
with its inverse,2cos(2theta)=6/5, must be an algebraic integer. A rational
algebraic integer is an integer, contradiction. This proves exactly the
irrationality needed; numerical arctangents do not enter it.

## Replayed finite check

Domain: the two exact displayed polygons, all30 nonincident-vertex support
inequalities and two exact areas. It is verification of example geometry,
not a finite search for plane tilings. Replayed command:

```bash
mise exec -- conda run --no-capture-output -n arisearch sage -c '
from sage.all import *
r=AA(5).sqrt(); u=QQbar(2+I)/r
polygons=[[vector(AA,[z.real(),z.imag()]) for z in zs] for zs in
 [[QQbar(0),QQbar(1),u,u**2,u**3],
  [QQbar(0),QQbar(1),u**2,u**4,u**6]]]
cross=lambda a,b:a[0]*b[1]-a[1]*b[0]
areas=[]
for P in polygons:
 for i,a in enumerate(P):
  b=P[(i+1)%5]
  for j,c in enumerate(P):
   if j not in (i,(i+1)%5): assert cross(b-a,c-a)>0
 areas.append(sum(cross(a,b) for a,b in zip(P,P[1:]+P[:1]))/2)
assert areas==[AA(3)/(2*r),AA(6)/5]
assert areas[0]!=areas[1]
print("Independent exact allsupport inequalities and distinct fan areas passed")
'
```

Result exit0. The general untileability proof is analytic and does not depend
on this finite example verification.

## Scope

This is a genuine restricted untileability theorem for the specified angular
family. It does not prove impossibility for arbitrary pairs, and its exact
example has no plane tiling, hence is no aperiodic construction. No unresolved
qualification remains in the reviewed statement.
