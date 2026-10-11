# Complete Pa=Qd sole-cross event-flat enumeration and sixteen remaining ratio families

Date: 2026-10-10. Python 3.12.13, SageMath 10.9. Arithmetic Q(sqrt3),
positive embedding 1<sqrt3<2. No random seed, numerical decisions, timeout,
patch search, symmetry quotient or maximum-codimension truncation.

The mathematical question is which exact event-contact strata remain
locally possible for two internally distinct Cairo shapes sharing only
Pa=Qd. The finite domain is the entire intersection lattice of 22 relevant
homogeneous event/e hyperplanes within the five-dimensional closure kernel.
Canonical keys are the exact RREF rows in eight native arm coordinates.
All unactivated forms define proper excluded hyperplanes of each open
stratum. Extra arm equalities are outside this exact cross pattern.

Every positive privacy-preserving flat is expanded even if its generic
stratum has a contact obstruction. Only forced extra-arm identities and
empty positive cones prune descendants. The latter have retained exact
Gordan dual weights: nonnegative sum1 weights on eight arms and two e
linear forms annihilate every kernel coordinate. Thus positivity pruning
has direct algebraic certificates. Dimension1 flats need no expansion:
every proper further equation would leave only the zero metric.

The native120-star filter uses actual native-slot arm/arm compatibility,
e/arm bank-host compatibility and whole e/e equality. It exhausts 56
unordered corner triples with 8 native reflection choices. A sorted triple
covers both cyclic orientations because global reversal swaps all native
corner choices and compatibility is symmetric. A missing mandatory corner
is an unrestricted obstruction, not a failed patch extension. The reviewed
forced-core theorem kills a flat when none of its twelve core resonance
forms is an identity; all its proper forms are excluded in that stratum.

Completion: all 1639 visited flats processed. Counts: 1270 forced extra arm equality,
34 exact empty positive cones, 318 generic missing120 corner, 1 reviewed
core obstruction, and 16 generic local survivors. All 16 survivors have metric dimension2, including
scale. Each stores an exact normalized affine sideword, full strict
positivity ratio interval, every privacy and proper-event exclusion,
and every resulting open arm-order chamber with an actual generic positive
sample. No claim of tiling existence or periodicity is made for a survivor.
All positive flats retain cone witnesses; these witnesses alone need not
be generic. Open-cone finite proper-hyperplane avoidance proves each
specified stratum nonempty.

    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-one-shared-event-flats.py --output research/certificates/partial-contact-cairo-one-shared-event-flats.json

Fresh independent hostile review is VALID; its no-author-import five-
coordinate checker verifies all 1639 flats, 34 Gordan duals, sixteen
normalized ratio families and their 102 generic arm-order chambers. The reduction is stated in
[the lemma](../lemmas/partial-contact-cairo-one-shared-event-flat-reduction.md).
The sixteen exact ratio families below are restart data, not proved tilers.
Native arm indices0..7 are Pa,Pb,Pc,Pd,Qa,Qb,Qc,Qd.

### Flat 223

Parameter u=arm[1]/Pa. Positivity interval: (1/3*w, 2).

Normalized P: (1, u, -1/2*u + 3/2*w, 1/2*w*u - 1/2, 2).

Normalized Q: (-1/4*w*u + 1/2*w + 1/4, -1/4*u + 3/4*w + 1/2, -u + 2, 1, -1/2*w*u + w + 1/2).

Identical event hyperplanes: cross=2arm0, eP=event0, eP=event7, eQ=event4.

Excluded privacy or proper-event ratio values: -1/13*w + 22/13, -5*w + 10, 1, 1/3*w + 2/3, 3/5*w + 2/5, 7/13*w - 2/13, w.

Exact open arm-order chambers retained: 8.



### Flat 259

Parameter u=arm[1]/Pa. Positivity interval: (0, -1/3*w + 2).

Normalized P: (1, u, 1/4*u + 3/4*w, 1/4*w*u + 1/4, 1/2*w*u + 1/2).

Normalized Q: (-1/2*w*u + w - 1/2, 1/2*u + 3/2*w - 1, -u + 2, 1, 2).

Identical event hyperplanes: cross=2arm0, eP=event3, eQ=event0, eQ=event7.

Excluded privacy or proper-event ratio values: -1/3*w + 4/3, -3/5*w + 8/5, -7/13*w + 28/13, -w + 2, 1, 1/13*w + 4/13, 5*w - 8.

Exact open arm-order chambers retained: 8.



### Flat 347

Parameter u=arm[1]/Pa. Positivity interval: (1/3*w, 17/11*w - 8/11).

Normalized P: (1, u, -1/2*u + 3/2*w, 1/2*w*u - 1/2, 2).

Normalized Q: ((-w + 1/2)*u - 3/2*w + 5, (-1/2*w + 1)*u - w + 9/2, -2*u + 3*w, 1, -u + 3*w).

Identical event hyperplanes: cross=2arm2, eP=event0, eQ=event2, eQ=event7.

Excluded privacy or proper-event ratio values: 1, 13/11*w - 10/11, 15/13*w - 8/13, 23/11*w - 28/11, w.

Exact open arm-order chambers retained: 6.



### Flat 366

Parameter u=arm[1]/Pa. Positivity interval: (7/3*w + 4, 5*w + 12).

Normalized P: (1, u, (1/4*w + 1/4)*u - 1/4*w - 3/4, (1/4*w - 1/4)*u + 1/4*w + 5/4, (1/2*w + 1/2)*u - 1/2*w - 3/2).

Normalized Q: ((-1/4*w + 3/4)*u - 3/4*w - 5/4, (-1/4*w + 1/4)*u + 7/4*w + 3/4, (1/2*w - 1/2)*u - 1/2*w - 3/2, 1, 2).

Identical event hyperplanes: cross=2arm2, eP=event2, eP=event7, eQ=event0.

Excluded privacy or proper-event ratio values: 3*w + 10, 3*w + 4, 3*w + 6, 5*w + 4.

Exact open arm-order chambers retained: 5.



### Flat 370

Parameter u=arm[1]/Pa. Positivity interval: (2*w + 3, infinity).

Normalized P: (1, u, (1/4*w + 1/4)*u - 1/4*w - 3/4, (1/4*w - 1/4)*u + 1/4*w + 5/4, (1/2*w + 1/2)*u - 1/2*w - 3/2).

Normalized Q: ((-1/8*w + 3/8)*u - 3/8*w - 1/8, (1/8*w - 1/8)*u + 5/8*w - 3/8, (1/2*w - 1/2)*u - 1/2*w - 3/2, 1, (-1/4*w + 3/4)*u - 3/4*w - 1/4).

Identical event hyperplanes: cross=2arm2, eP=event2, eP=event7, eQ=event4.

Excluded privacy or proper-event ratio values: 3*w + 4, 3*w + 6, 31/13*w + 46/13, 7*w + 10.

Exact open arm-order chambers retained: 5.



### Flat 379

Parameter u=arm[1]/Pa. Positivity interval: (0, 7*w - 10).

Normalized P: (1, u, 1/4*u + 3/4*w, 1/4*w*u + 1/4, 1/2*w*u + 1/2).

Normalized Q: ((-1/4*w - 1/4)*u - 3/4*w + 11/4, (1/4*w + 1/4)*u - 1/4*w + 9/4, -1/2*u + 3/2*w, 1, 1/2*u + 3/2*w).

Identical event hyperplanes: cross=2arm2, eP=event3, eQ=event2, eQ=event7.

Excluded privacy or proper-event ratio values: -13/11*w + 32/11, -23*w + 40, 1, 1/13*w + 4/13, 23/11*w - 28/11, 5*w - 8, w.

Exact open arm-order chambers retained: 8.



### Flat 381

Parameter u=arm[1]/Pa. Positivity interval: (0, 3*w).

Normalized P: (1, u, 1/4*u + 3/4*w, 1/4*w*u + 1/4, 1/2*w*u + 1/2).

Normalized Q: (-1/8*w*u + 11/8, -1/8*u + 9/8*w, -1/2*u + 3/2*w, 1, -1/4*w*u + 11/4).

Identical event hyperplanes: cross=2arm2, eP=event3, eQ=event4.

Excluded privacy or proper-event ratio values: -11/61*w + 88/61, -13/11*w + 56/11, -23*w + 40, 1, 1/13*w + 4/13, 13*w - 20, 3*w - 2, 37/13*w - 8/13, w.

Exact open arm-order chambers retained: 10.



### Flat 484

Parameter u=arm[1]/Pa. Positivity interval: (0, 1/3*w + 2/3).

Normalized P: (1, u, 1/4*u + 3/4*w, 1/4*w*u + 1/4, 1/2*w*u + 1/2).

Normalized Q: ((-3/4*w + 3/4)*u + 1/4*w + 1/4, (-1/4*w + 5/4)*u + 3/4*w - 1/4, (1/2*w - 1)*u + 1/2, 1, 1/2*w*u + 1/2).

Identical event hyperplanes: cross=2arm3, eP=event3, eP=event7, eQ=event3, eQ=event7, eP=eQ.

Excluded privacy or proper-event ratio values: 1, 1/13*w + 4/13.

Exact open arm-order chambers retained: 3.



### Flat 485

Parameter u=arm[1]/Pa. Positivity interval: (0, w + 2).

Normalized P: (1, u, 1/4*u + 3/4*w, 1/4*w*u + 1/4, 1/2*w*u + 1/2).

Normalized Q: ((-1/4*w + 3/8)*u + 1/8*w + 1/4, (1/8*w - 1/4)*u + 3/4*w + 1/8, (1/2*w - 1)*u + 1/2, 1, (-1/2*w + 3/4)*u + 1/4*w + 1/2).

Identical event hyperplanes: cross=2arm3, eP=event3, eP=event7, eQ=event4.

Excluded privacy or proper-event ratio values: 1, 1/13*w + 4/13, 13*w - 20, 61/97*w + 28/97, w.

Exact open arm-order chambers retained: 6.



### Flat 584

Parameter u=arm[1]/Pa. Positivity interval: (0, 1/2).

Normalized P: (1, u, 1/4*u + 3/4*w, 1/4*w*u + 1/4, 1/2*w*u + 1/2).

Normalized Q: ((-w - 3/2)*u + 1/2*w + 1, (-1/2*w - 1)*u + w + 1/2, (-2*w - 4)*u + w + 2, 1, (-2*w - 3)*u + w + 2).

Identical event hyperplanes: cross=2arm4, eP=event3, eQ=event4, eQ=event7.

Excluded privacy or proper-event ratio values: -23*w + 40, -47/97*w + 112/97, -w + 2, 1/13*w + 4/13, 1/2*w - 1/2.

Exact open arm-order chambers retained: 6.



### Flat 591

Parameter u=arm[1]/Pa. Positivity interval: (1/3, 1/2).

Normalized P: (1, u, (-3/2*w - 7/2)*u + 3/2*w + 3/2, (3/2*w + 3/2)*u - 1/2*w - 1/2, (-2*w - 3)*u + w + 2).

Normalized Q: ((-w - 3/2)*u + 1/2*w + 1, (-1/2*w - 1)*u + w + 1/2, (-2*w - 4)*u + w + 2, 1, (-2*w - 3)*u + w + 2).

Identical event hyperplanes: cross=2arm4, eP=event4, eP=event7, eQ=event4, eQ=event7, eP=eQ.

Excluded privacy or proper-event ratio values: 1/13*w + 4/13, 1/2*w - 1/2.

Exact open arm-order chambers retained: 3.



### Flat 638

Parameter u=arm[1]/Pa. Positivity interval: (1/3*w, 3*w).

Normalized P: (1, u, -1/2*u + 3/2*w, 1/2*w*u - 1/2, 2).

Normalized Q: (1/2*u + 1/2*w + 2, (1/2*w + 1)*u + w + 3/2, (w + 1)*u + 2*w + 3, 1, (w + 2)*u + 2*w + 3).

Identical event hyperplanes: cross=2arm5, eP=event0, eQ=event5, eQ=event7.

Excluded privacy or proper-event ratio values: -w + 4, 1, 3*w - 2, w.

Exact open arm-order chambers retained: 5.



### Flat 664

Parameter u=arm[1]/Pa. Positivity interval: (0, 3/2*w).

Normalized P: (1, u, 1/4*u + 3/4*w, 1/4*w*u + 1/4, 1/2*w*u + 1/2).

Normalized Q: (-1/2*w*u + 5/2, -1/2*u + 3/2*w, -2*u + 3*w, 1, -w*u + 5).

Identical event hyperplanes: cross=2arm5, eP=event3, eQ=event4.

Excluded privacy or proper-event ratio values: -5*w + 10, 1, 1/13*w + 4/13, 13*w - 20, 19/13*w - 2/13, 23/11*w - 28/11, 3/2*w - 1/2, 97/61*w - 44/61, w.

Exact open arm-order chambers retained: 10.



### Flat 665

Parameter u=arm[1]/Pa. Positivity interval: (0, infinity).

Normalized P: (1, u, 1/4*u + 3/4*w, 1/4*w*u + 1/4, 1/2*w*u + 1/2).

Normalized Q: (1/2*u + 1/2*w + 2, (1/2*w + 1)*u + w + 3/2, (w + 1)*u + 2*w + 3, 1, (w + 2)*u + 2*w + 3).

Identical event hyperplanes: cross=2arm5, eP=event3, eQ=event5, eQ=event7.

Excluded privacy or proper-event ratio values: 1, 1/13*w + 4/13, w, w + 4.

Exact open arm-order chambers retained: 5.



### Flat 674

Parameter u=arm[1]/Pa. Positivity interval: (-1/11*w + 16/11, 7/3*w).

Normalized P: (1, u, (1/4*w - 1/2)*u + 1/2*w + 9/4, (1/2*w - 1/4)*u - 3/4*w + 1/2, 1/2*u + 3/2*w).

Normalized Q: (-1/4*w*u + 7/4, 1/4*u + 3/4*w, -1/2*u + 3/2*w, 1, 2).

Identical event hyperplanes: cross=2arm5, eP=event5, eP=event7, eQ=event0.

Excluded privacy or proper-event ratio values: -13/11*w + 56/11, 3*w - 2, 7/11*w + 20/11, 9/13*w + 16/13, w.

Exact open arm-order chambers retained: 6.



### Flat 678

Parameter u=arm[1]/Pa. Positivity interval: (-2*w + 5, 3/2*w).

Normalized P: (1, u, (-1/2*w - 1/2)*u + 1/2*w + 9/2, (1/2*w + 1/2)*u - 3/2*w + 1/2, -u + 3*w).

Normalized Q: (-1/2*w*u + 5/2, -1/2*u + 3/2*w, -2*u + 3*w, 1, -w*u + 5).

Identical event hyperplanes: cross=2arm5, eP=event5, eP=event7, eQ=event4.

Excluded privacy or proper-event ratio values: -w + 4, 13*w - 20, 19/13*w - 2/13, 23/11*w - 16/11, 3/2*w - 1/2, 5/11*w + 14/11, w.

Exact open arm-order chambers retained: 8.

