# Exact adjacent-alpha pentagon/octagon periodic covering

Date:2026-10-13. Status: **exact periodic covering; independently reviewed VALID.** This is an existence and periodic-escape result for one pair, not aperiodicity or a universal classification. No old nonadjacent-alpha enumeration was resumed.

## New mechanism and concrete scheme

A Q side joining its two adjacent108° corners matches its opposite144–144 side. Repetition across those two parallel equal sides produces a translative vertical QQ chain. Alternate these chains with half-turned copies, then fill each intervening gap by two congruent equi108° pentagons. The pentagon pairs alternate their two PP joins vertically. This is a concrete six-face motif (2Q+4P), obtained by solving the edge-vector closure equations; no torus gluing enumeration was performed.

Let φ=(1+√5)/2, c=(1+√5)/4 and s=√(10−2√5)/4, where the square roots are positive. Define the rotation matrix

    R=[[c,−s],[s,c]], u_k=R^k(1,0), k=0,...,9.

This specifies exact real algebraic coordinates; R rotates36°. Define Q's edge lengths and direction exponents by

    lengths=(1,φ+2,1,1,1,1,1,φ+2),
    exponents=(0,2,3,4,5,6,7,8).

Starting q0=(0,0), let q(i+1)=qi+length_i*u(exponent_i). The exact sum is zero, so q8=q0. Put Q=conv(q0,...,q7) in that boundary order. The turns are72° at q0,q1 and36° at the other six corners, so Q has angle word(108,108,144,144,144,144,144,144). All lengths are positive and the script independently checks strict convexity. Its AA side q0q1 and opposite BB side q4q5 both have length1, as required by the reviewed necessary equality gate.

Write a=φ+2, x=2φ² and T=q5−q0. Exact closure yields T=(0,h), h>0. Define

    B=q4, D=q3, X=D+x*u1, Y=X+u3, Z=Y−a*u0,
    P=[B,D,X,Y,Z].

The identities Z=q2+T and B=Z+a*u7 close P. Its side directions are(324,36,108,180,252) degrees, with lengths(1,2φ²,1,φ+2,φ+2); hence all five interior angles are108°. Again strict convexity and actual angle cosines are independently checked.

The closure arose from a mirror-symmetric Q family with lengths(d,a,b,c,d,c,b,a). Q closure requires a−b=φ²c. A pentagon at a QQ chain joint with its third PQ side matching a rotated-chain side requires x=c+φ(a−b), y=φ³c−b/φ. Choosing b=c=d=1 gives x=2φ² and y=a=φ+2. These equations explain the parameter choice. No assertion of covering for all other parameters is made.

## Exact infinite motif

Set L=D+X and S=(2(L_x−1),0), whose x coordinate is positive. Let F(v)=(1−v_x,v_y), the reflection in Q's vertical symmetry axis. A finite motif consists of the following six closed polygons:

    Q,
    L−Q,
    P,
    L−P,
    S+F(P),
    S+F(L−P).

Here minus denotes pointwise half-turn, not set complement; reflected polygon boundary orders are reversed for counterclockwise computation. Repeat the motif by every mS+nT, m,n in Z. This uses exactly the two congruence classes P and Q, since all copies above are isometric. The pair has distinct side counts5 and8.

## Complete coverage certificate and proof

The retained exact Sage witness research/searches/resumed-adjacent-octagon-check.py defines every coordinate above and performs the following finite checks over exact real algebraic arithmetic:

1. All six motif polygons are strictly convex and have positive oriented area.
2. Independently computed angle cosines are exactly cos108°=(1−√5)/4 on P and the specified108/144 word on Q.
3. The sum of the six areas equals det(S,T)>0 exactly.
4. For every ordered pair of motif polygons, enumerate all lattice translates whose closed axis-aligned bounding boxes can meet. Because S is horizontal and T vertical, the complete integer ranges are

       ceil((A_xmin−B_xmax)/S_x) <= m <= floor((A_xmax−B_xmin)/S_x),
       ceil((A_ymin−B_ymax)/T_y) <= n <= floor((A_ymax−B_ymin)/T_y).

   Skip only a polygon compared with its own zero translate. There are44 remaining tests. Exact convex clipping verifies that every intersection has area zero. This includes all potentially overlapping copies in the entire infinite tiling; translations outside these ranges have disjoint bounding boxes. No symmetry quotient is used.

For completeness, these checks imply plane coverage as follows. Let U be the union of all motif translates. Bounded motifs and a nondegenerate lattice make the family locally finite, so U is closed. Check4 implies pairwise interior-disjointness. Integrating the multiplicity over one fundamental rectangle, translation invariance and finite summation give covered area equal to the sum of motif areas. Check3 therefore leaves zero uncovered area per rectangle. If any point were absent from U, its open complement would contain a positive-radius disk and therefore positive uncovered area in some fundamental rectangle, contradiction. Thus U is the whole plane. This proves a genuine infinite covering, not merely locally legal patches.

Both S and T are nonzero independent translational symmetries of the resulting tiling. Consequently the pair fails aperiodicity. The construction supplies an exact mixed periodic escape inside the adjacent-AA=BB equality locus.

Neither individual type alone can cover: all-obtuse stars must be108+108+144; P alone has no144 sector, while Q alone has alpha:beta native counts2:6 rather than the required2:1. Finite-window counting excludes either singleton without assuming periodicity. The mixed periodic witness remains decisive for the original target.

## Scope and review


The [independent hostile review](../reviews/resumed-adjacent-octagon-construction-review.md) validates translate-domain completeness, overlap separation, area-to-covering and algebraic geometry; its checker uses separating axes independently of clipping. For the global target this candidate is already rejected by its periodic symmetry. Equality by itself therefore does not force aperiodicity. A viable next mechanism needs a geometry that prevents these or other periodic chain assemblies; no broader adjacent-alpha tilability or periodicity classification follows from this one witness.

The finite domain and replay commands are in the [search record](../searches/resumed-adjacent-octagon-construction.md).
