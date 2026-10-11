# Unequal three-angle pentagon multiplicities force rational angles

**Status:** adversarially reviewed; [fresh hostile review](../reviews/three-angle-pentagon-multiplicity-rationality-review.md) valid.
This is a necessary angle reduction, not a tiling construction or a complete
impossibility result.

## Theorem

Let P,Q be genuine compact convex pentagons. Suppose their combined set of
interior angle values is exactly {alpha,beta,gamma}. Write the vectors of
multiplicities as c_P,c_Q in Z_(>=0)^3, each with coordinate sum5. If
c_P != c_Q and the pair admits any unrestricted plane tiling, then
alpha/pi,beta/pi,gamma/pi are all rational numbers.

Consequently any tileable two-pentagon pair with exactly three combined
angle values, at least one irrational multiple of pi, must have identical
angle multiplicities in its two members. Cyclic orders and lengths can differ.
This theorem includes rotations, reflections, partial-edge contacts, and a
tiling omitting either member. No angle-denominator bound is asserted.

## Proof

Let x=(alpha/pi,beta/pi,gamma/pi). The shape angle sums give

    c_P dot x = 3,    c_Q dot x = 3.                  (1)

The rows c_P,c_Q are linearly independent over Q. Otherwise they would be
proportional, but both have coordinate sum5, so proportionality would make
them equal.

Choose any native tile vertex in an admitted plane tiling. Fixed positive
areas and bounded diameters give local finiteness. At this point each incident
tile contributes a genuine corner sector, or a straight sector of angle pi.
Two straight sectors would leave no room for the chosen positive corner.
Hence the genuine corner sectors sum pi or2pi, with at most one straight
sector. Let s be their nonnegative integer count vector and h in {1,2} their
sum divided by pi. Thus

    s dot x = h,    s dot (1,1,1) is an integer.       (2)

The sum of the coordinates is finite, since the fixed shapes have a positive
minimum native angle. There is no imposed valence cutoff.

If s belonged to the Q-span of c_P,c_Q, write s=a*c_P+b*c_Q for rational a,b.
By (1),(2), 3(a+b)=h. But its coordinate sum would be5(a+b)=5h/3, which is
not an integer for h=1 or2. This is impossible. Therefore the three rows
c_P,c_Q,s form an invertible integer3-by3 matrix. Equations (1),(2) have
rational right-hand side (3,3,h), so their unique solution x is rational.

Both shape rows are available even if a tiling omits one shape. The corner
row can come from any present tile. Thus omission and hypothetical rare-type
frequencies cannot evade the argument. No full-edge assumption is used.

## Dependencies and scope

Only the convex-pentagon angle sum, local corner/straight-sector dichotomy,
and rational linear algebra are used. This is not a rational-angle
classification and uses no monohedral pentagon theorem. There is no finite
search or numerical evidence.

If the multiplicity rows agree, the argument supplies only two independent
rows; one angle can remain an irrational multiple of pi. For example a
formal angle list (pi/2,theta,pi/2,theta,2pi-2theta), with pi/2<theta<3pi/4,
has the star equations four right angles and theta+theta+(2pi-2theta)=2pi.
This observation alone asserts neither polygon closure nor plane tilability.
The three-angle periodic trial at theta=7pi/12 belongs to this equal-row
branch and does not contradict the theorem.

Four or more combined angle values also leave this argument insufficient
for rationality. Rationality itself does not imply a periodic escape.
