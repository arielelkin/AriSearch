# Exact exceptional Cairo family with one shared native arm

**Status:** exact positive candidate family and local arithmetic, not a plane
tiling claim. No periodic or aperiodic conclusion. This family lies outside
the generic arm classification because e equals a collided right-corner
event sum. Global extension and all periodic escapes remain unproved.

Let w=sqrt3 and 1/w<r<2-1/w. Fix s=1,t=2-r. Impose the sole proposed cross
arm equality Pa=Qd=s, the bank-sum collision Pb+Qc=2s, and eP=eQ=2s. Exact
Cairo closure then uniquely gives

    P=(1,r,(3w-r)/2,(wr-1)/2,2),
    Q=((w*(2-r)-1)/2,(3w-2+r)/2,2-r,1,2).

All ten sides are positive throughout the stated interval; the fixed cyclic
directions give genuine strictly convex pentagons. Further arm equalities
can occur on finitely many exceptional r values and are not declared absent
throughout that whole interval. The retained exact r=4/5 fixture has four
internally distinct arms per species and exactly one cross arm equality,
Pa=Qd=1. It is outside both sufficient two-equality cones and every generic
stratum because eP=eQ=Pb+Qc=2Pa=2Qd.

The shared perpendicular arm1 can create a T with banks r,t; its private
perpendicular alternatives generate banks1,1. These events have the same
total2, and both e sides can host them. The exact two-T switch can exchange
r with1 using r+t=1+1=2 (since r<1<t at the fixture), or exchange1 witht.
Unlike the generic event classes, this collision makes actual native slots
with different perpendicular labels compatible. One must keep those slot
labels, not add an unrestricted transitive closure.

The private Pc arm forces two isolated P120 corners together along their c
ray. Their remaining r rays need a third outer120 corner. Such a third
corner can offer native arm1 and e2; both are locally compatible with r via
the exhibited switches and split-e event. The private Qb arm similarly
forces two isolated Q120 corners and a third outer corner offering1 and e2
against their t rays. This explains why the simple private-arm obstruction
and the generic no-e-T filter no longer settle the family. This is only
necessary local incidence; both endpoints, complete tile separation, and
global continuation have not been supplied.

[Exact checker](partial-contact-cairo-single-shared-exception.py) verifies the
fixture closure, positivity, strict convexity, native side lengths, all
cross arm equalities, the event inventory, the declared exact collision and
strict switch inequalities. There is no bounded tiling search, optimization
or numerical decision.
