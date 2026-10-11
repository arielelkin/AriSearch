# No strictly obtuse pentagon can tile with a regular tridecagon

**Status:** adversarially reviewed; the fresh reviewer independently read this
standalone text and found it valid without repair. See the explicit follow-up
in the [large-polygon review](../reviews/all-obtuse-pentagon-regular-large-polygon-review.md).
This is an analytic restricted untileability theorem, not a global solution.

## Theorem

Let P be any genuine convex pentagon all of whose angles lie strictly
between pi/2 and pi. Let Q be the regular unit-side 13-gon, whose angle is
11pi/13. Then {P,Q} has no admitted tiling under the unrestricted problem
definition. Arbitrary rotations and reflections, unrestricted contacts,
and omission are initially allowed.

## Proof

The reviewed [all-obtuse forcing theorem](obtuse-edge-forcing.md) makes any
hypothetical tiling full native-edge and trivalent. A star with two Q
sectors would leave angle4pi/13<pi/2, so it is impossible; three Q sectors
are impossible as well. Every Q side neighbor is P, and P has at most two
Q side neighbors, in nonadjacent positions.

Use centroid counts N_P,N_Q in a translated square W_R and star counts
by vertex location. Fixed positive areas and bounded diameters give only
O(R) boundary discrepancies, uniformly in translation, and total count
Theta(R^2). Corner and angle counting give N_P=7N_Q+O(R), so both types
have positive quadratic counts. Let Z be the number of P,P,P stars and Y
the number of P,P,Q stars. Q sector count is Y=13N_Q+O(R). Hence P sector
count gives

    5N_P=2Y+3Z+O(R),
    Z=3N_Q+O(R).                                         (1)

Every P,P,Q P sector has angle strictly below

    H=2pi-11pi/13-pi/2=17pi/26 < 2pi/3,

because its fellow P sector is strictly obtuse. Call a native P corner
high if its angle is at least H. Every occurrence of a high corner must
be P,P,P. If k is the number of native high corners, then

    kN_P <= 3Z+O(R) = 9N_Q+O(R).

Since N_P=7N_Q+O(R)=Theta(R^2), this gives k<=1.

There is a native P angle at least2pi/3. Otherwise no P,P,P star could
exist, contrary to (1). Thus k=1, and let theta>=2pi/3 be this unique
high angle. All four remaining P angles are strictly below H<2pi/3.
If theta=2pi/3, the only P,P,P star would be three theta sectors; any
star containing a smaller sector would sum below2pi. Its incidence count
would require N_P=3Z+O(R), whereas (1) gives N_P=7N_Q+O(R) and
3Z=9N_Q+O(R), a quadratic contradiction. Therefore theta>2pi/3.

A P,P,P star has at least one high sector, since three remaining angles
are below2pi/3. It has at most two high sectors, since3theta>2pi. Counting
all high occurrences therefore gives

    N_P <= 2Z+O(R)=6N_Q+O(R).

This contradicts N_P=7N_Q+O(R) and N_Q=Theta(R^2), proving untileability.
No limit tiling, finite computational search, or rational-angle hypothesis
on P was used.

## Scope and dependencies

The only imported geometric theorem is all-obtuse forcing. Boundary counts
are explicitly derived from fixed positive areas, bounded diameters, and
finite side counts, as in the reviewed
[regular-heptagon classification](all-obtuse-pentagon-regular-heptagon-classification.md).
Regularity is used only for Q's common angle; side lengths play no role.
The same argument excludes a convex equiangular13-gon with arbitrary
positive side lengths. Acute/right P corners are outside the proof.

This artifact supplies no aperiodic pair and does not classify n>=14.
No current primary-literature novelty audit was performed for this exact
obstruction, so no novelty is claimed. No code or finite certificate is
needed for the displayed analytic inequalities.
