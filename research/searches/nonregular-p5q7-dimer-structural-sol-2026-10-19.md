# Nonregular P5/Q7: exact dimer reduction and a failed curvature-return test

Date: 2026-10-19. Status: independently hostile-reviewed conditional reduction; see [review](../reviews/nonregular-p5q7-structural-hostile-sol-review-2026-10-19.md). One theoretical cycle, no patch or torus enumeration and no metric existence assumption. Conditional on genuine convex polygons with angle multisets P=(100,100,110,115,115), Q=(125,125,125,130,130,130,135), in degrees. Cyclic corner orders and lengths are unspecified. Reflections are allowed. No tilability or periodicity result is claimed.

## Unrestricted contacts and complete star list

The reviewed obtuse edge-forcing lemma applies: every admitted plane tiling is edge-to-edge and trivalent. The complete unordered angle triples summing to 360 are

A=(100,125,135), B=(100,130,130), C=(110,115,135), D=(110,125,125), E=(115,115,130).

This follows by taking the smallest angle in the six-element support and testing the remaining pair; triples with all Q angles exceed 360, and triples with all P angles are below 360. These stars have species PQQ except C,E, which have species PPQ.

At any P tile, a corner meets a P neighbor precisely at its PPQ corners. Each PP edge contributes its two endpoint corners, and at a trivalent vertex there is at most one P neighbor of the selected P. Thus the number of PPQ corners on P is even. Its two 115 corners necessarily are PPQ. Its 100 corners never are. Consequently its 110 corner cannot be C. There are no C stars anywhere, and every P has exactly one PP edge, whose endpoints are its two 115 corners. In particular these corners must be consecutive in the chosen cyclic order; otherwise no tiling exists. The PP graph is a perfect matching, giving canonical P dimers.

## Pointwise Q alternatives: a sparse defect cannot be silently excluded

Let k(Q) be the number of PPQ corners of one Q. They are all E and use its 130 corners, so 0<=k<=3. At its other corners exactly one of its two incident side neighbors is Q; at E neither is Q. There are no QQQ stars. Counting QQ-side endpoints gives 2 deg_QQ(Q)=7-k. Therefore k is odd, and exactly the alternatives

k=1, deg_QQ=3; or k=3, deg_QQ=2

survive. Calling the second alternative a defect, no argument here excludes an individual defect in an arbitrary plane tiling. The frequently stronger statement “every Q has exactly one PPQ130” is not established.

## Window estimates and exact frequencies

Use square windows of side R and count tiles by any fixed interior marked point. All discrepancy constants below are uniform in window centre. A finite polygon set has bounded diameter and positive areas, so only O(R) tiles or stars intersect a fixed-width boundary strip. This follows by putting the disjoint interiors of those tiles into a slightly wider strip and dividing its area by the least tile area. The reviewed curvature identity gives N_P-N_Q=O(R).

For completeness all star counts can be recovered directly. Write a,b,d,e for A,B,D,E counts with any consistent local anchor convention; differing conventions cost O(R). Counting P110, P115, P100 and Q135 gives respectively

d=N_P+O(R), e=N_P+O(R), a+b=2N_P+O(R), a=N_Q+O(R).

Counting Q125 gives a+2d=3N_Q+O(R), hence again N_P-N_Q=O(R). Thus a,b,d,e each equal N_P+O(R), and V=4N_P+O(R). Every Følner subsequential frequency has P:Q=1:1 and A:B:D:E=1:1:1:1. These are relative counts, not an assertion that the absolute density has a unique limit.

If Z(R) counts k=3 Q tiles, counting E incidences on Q gives

e=N_Q+2Z(R)+O(R).

Therefore Z(R)=O(R), uniformly in window centre. This proves zero upper square density of defects, not their absence. Boundary terms have uncontrolled sign and cannot justify pointwise equality.

There is nevertheless a defect-free admitted tiling whenever any admitted tiling exists. For every L there is a square of side L containing no defect: otherwise each square in a disjoint grid of that fixed size contains a defect, yielding quadratic defect counts, contradicting the linear bound. Choose such squares with L tending to infinity and translate their centres to the origin. Finite local complexity follows here from edge-to-edge contacts: fix one tile frame; each adjacent tile has finitely many side-role/isometry choices, and bounded regions contain uniformly boundedly many tiles. The connected adjacency graph and the usual diagonal compactness argument therefore give a whole-plane limiting tiling. Alternatively use compactness of locally finite closed tile configurations, anchoring a tile meeting the origin and passing to subsequences. Every bounded region eventually lies inside a defect-free square, so the limit has no k=3 tile. No periodicity is supplied by this purification.

## One specific global return/curvature test

Test whether the canonical dimer network forces nonzero rotational return or Euler curvature on a periodic quotient. Fuse each matched PP pair. A dimer has eight boundary sides, six convex corners (100,100,110 twice) and two reflex corners 230. Its exterior-turn sum is

2(80+80+70)+2(-50)=360.

At each reflex corner an E Q130 corner exactly fills the complement. Thus fusing does not create a curvature excess that could obstruct a closed return. For the original trivalent network on any hypothetical torus quotient (enlarge the period lattice if necessary so its cells contain full dimers), boundary errors vanish. The identities force

N_P=N_Q=N; a=b=d=e=N; V=4N; E_edges=6N; F=2N.

Hence V-E_edges+F=0 identically. Dimer matching only forces N even. The smallest arithmetic choice N=2 satisfies all these integer equations. This is an arithmetic consistency check, not a realizable quotient or a finite-map enumeration. It falsifies the hoped-for contradiction from this particular Euler/turn/parity invariant. All side directions also lie in one finite set modulo 5 degrees, because every exterior turn is a multiple of 5 degrees and adjacent tiles share sides; this finite rotational condition gives no translational return.

In a defect-free limit each Q has three QQ sides and four PQ sides, and is incident at exactly one E cap. Each dimer has two E caps. A Q cap occupies two consecutive P-boundary sides, one from each member of a dimer; the remaining incidences and side-role choices are not determined by the angle inventory. The counts and the signed turn sum supply no deterministic path whose displacement repeats.

## Exact stopping gap

The missing lemma for a periodic escape is: every geometrically realizable defect-free tiling by the specified polygons, with canonical P dimers and Q QQ-degree three, admits a nonzero translationally periodic tiling by those same polygons (not necessarily the same tiling). No strip decomposition, finite return map with a proved repeatable displacement, or extension theorem for that assertion has been established. The corresponding construction route would instead require an exact metric realization and a global invariant excluding every periodic return. The current angle/count invariant supplies neither. Stop this mechanism after this one cycle under protocol section 5; section 19 leaves other mechanisms to the root portfolio.

Dependencies: research-problem.md; research-protocol.md sections 5 and 19; research/lemmas/obtuse-edge-forcing.md and its hostile review. No novelty claim, literature theorem, or computation-dependent conclusion is used.
