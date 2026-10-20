# Tangential 110/140 first construction gate

Status: internally checked analytic exclusion; [independent Sol hostile review](../reviews/tangential-110-140-scale-hostile-sol-2026-10-19.md) PASS.
Scope: one new one-parameter P5/Q7 pair, not arbitrary pairs.

## Exact shapes
Let t_a=cot(a*pi/360), with a an integer number of degrees. P is the
circumscribed unit-inradius pentagon with outward normals at
0,90,160,230,300 degrees. Q_r is the circumscribed radius-r heptagon
with outward normals 0,80,160,200,240,280,320 degrees, r>0.
Equivalently intersect the halfplanes x*cos(theta)+y*sin(theta)<=1
for P and <=r for Q. All coordinates lie in the real part of Q(zeta_36)
and its imaginary-coordinate companion: cos(k*pi/18)=(zeta^k+zeta^-k)/2,
sin(k*pi/18)=(zeta^k-zeta^-k)/(2*zeta^9), zeta=exp(2*pi*i/36).
Intersections of adjacent lines give finite exact vertices.
P angles cyclically are 120,90,110,110,110; Q angles are
140,100,100,140,140,140,140 (cyclic shift allowed).

Write u=t_110, v=t_120, w=t_100, z=t_140. P sides at its
110 corners have lengths a=1+u, b=2u, c=u+v; a occurs once,
b twice, c once. Q sides have lengths r*f,r*d,r*e where
f=2w,d=w+z,e=2z. Exact inequalities are c<b<a,
f>d>e, and c<b<h=1+v. A retained Sage checker verifies these.

## Unrestricted contacts
The complete angle stars are 90^4, (90,90,flat180),
(110,110,140), (100,120,140), and (120,120,120).
Every T-junction therefore has two P90 corners and one flat sector.
In particular an edge that first ends at an obtuse corner cannot terminate
in the interior of an opposite native side: the remaining angle would
be less than 90 degrees and no tile can fill it.

## Counting gate
For counts in a radius-R disk, all boundary errors below are O(R),
because fixed compact tiles have positive inradius and bounded diameter.
Let p,q count P,Q tiles and x,y count stars (110,110,140),(100,120,140).
Then 3p=2x+O(R), 2q=y+O(R), 5q=x+y+O(R), so
p=2q+O(R), x=3q+O(R).
At every Q100 the ray shared with Q140 must pair two full equal sides:
all far endpoints are obtuse. The only shared numerical length between
a Q100 side (rf or rd) and a Q140 side (rd or re) is rd.
Thus each Q100 pairs along its 100--140 side with another Q's 140--100
side. This consumes precisely the two boundary140 corners per Q at y
stars. The other three Q140 corners, whose incident sides are both re,
are x stars. There are therefore 6q+O(R) rays from such corners to P110.

If re is not b, each such ray either uses a full equal P side of length
a or c, with only one 110 endpoint per occurrence (at most p rays),
or has a shorter P side ending90, possible only when re>a.
The latter consumes P90 endpoint rays, at most 2p in total.
The cases are mutually exclusive: re=a, re=c, re>a, or no permitted ray.
Hence in all non-b cases 6q<=2p+O(R)=4q+O(R), giving q=O(R),
then p=O(R), contradicting coverage area Theta(R^2).
Therefore tileability requires re=b.

At re=b, look at a Q boundary140 in its forced (100,120,140) star.
Its Q--Q ray uses rd, so its Q--P120 ray uses re=b.
A P120 has incident lengths c and h. Since c<b<h, either the
P side ends first at its obtuse110 corner or the Q side ends first
at its obtuse140 corner. Both are forbidden T-junctions.
Contradiction. Thus no r>0 tiles the plane with this pair.

## Scope and stop
This is a killed construction family, not an impossibility theorem.
No bounded patch extrapolation, source aperiodicity, solver or novelty
claim is used. A changed angle word or unequal support distances would
be required to reopen; increasing patch searches cannot help.

Replay: mise exec -- conda run --no-capture-output -n arisearch sage
research/searches/tangential-110-140-scale-gate-sol-2026-10-19.sage
