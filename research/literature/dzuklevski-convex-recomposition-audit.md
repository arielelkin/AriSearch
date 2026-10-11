# Džuklevski convex recomposition: source audit and exact scaffold

**Date:** 2026-10-09. **Status:** primary-source lead; one exact geometric
scaffold checked, no inherited forcing theorem accepted for our parameters.
Independent review pending.

## Source claim and scope

Aleksa Džuklevski, *A σ-morphic convex protoset*,
[arXiv:2507.20867v1](https://arxiv.org/abs/2507.20867), submitted 2025-07-28.
The PDF/HTML title is *A convex σ-morphic protoset*.
Theorem 3.2 and Figure 7 construct six convex congruence classes by dividing
Schmitt's two coarse tiles: four hexagons and two pentagons. Eight drawn
pieces include three rotated congruent hexagons. The argument uses unique
angle sums at internal trivalent nodes, unequal incident side lengths, and
exclusion of complementary-angle fillings to force relative orientation,
including reflected copies. It aims to reconstruct every admitted tiling.
No chosen exact parameter or finite angle-star certificate is supplied.

The updated six-page contribution 71 in the
[EuroCG 2026 booklet](https://eurocg26.fernuni-hagen.de/booklet-contributions.pdf),
*A set of convex prototiles that allows only countably many different
tilings*, states the same result as Theorem 2.1/Figure 4 and explicitly
labels itself a preprint rather than a formally reviewed paper.

Neither construction is an aperiodic source: σ-morphic means countably
infinitely many tilings up to isometry. The associated periodicity
obstruction is discussed below. Six is the count of this construction,
not a theorem that fewer convex shapes cannot encode matching rules.

## Our algebraic diagram reconstruction

The following coordinates are our reconstruction of the geometric scaffold
in Figure 7, not coordinates specified by the author. In particular, the
original EPS contains rounded drawing coordinates; those are not a proof
certificate. This reconstruction separates the polygon geometry from the
unverified generic-angle selection.

Put \(h=\sqrt3/2\) and let \(J(x,y)=(-y,x)\). Use free parameters
\(0<t<1,d>0\). For a clockwise directed unit edge from \(u\) to \(v\),
replace it by a two-segment inward nick through
\(u+t(v-u)-dJ(v-u)\), or an outward bump through
\(u+(1-t)(v-u)+dJ(v-u)\). Reversing the edge exchanges a bump with
a congruent nick. All coordinates are algebraic when the parameters are.

The right coarse skeleton has clockwise vertices

\[
\begin{array}{lll}
v_0=W'=(0,0),&v_1=Z'=(h,1/2),&v_2=Z''=(2h,0),\\
v_3=(2h+1/2,-h),&v_4=T=(2h,-2h),&v_5=(h,-2h-1/2),\\
v_6=(0,-2h),&v_7=W=(1/2,-h).&
\end{array}
\]

Decorate successive edges with signs
\(s=(+1,-1,-1,+1,+1,-1,-1,+1)\), where +1 is outward.
Thus \(a_i=v_i+\lambda_i(v_{i+1}-v_i)+s_i dJ(v_{i+1}-v_i)\),
with \(\lambda_i=1-t\) for +1 and \(t\) for -1, and indices modulo 8.
In the source notation, \(Z=a_1,V=a_2,S=a_5,U=a_6\).
Let \(Q,R\) be internal free points.
Five cyclic polygon lists are

\[
\begin{array}{ll}
4:&(Q,v_4,a_4,v_5,a_5),\\
5:&(Q,a_5,v_6,a_6,R),\\
6:&(R,a_2,v_3,a_3,v_4,Q),\\
7:&(v_7,a_1,v_2,a_2,R,a_6),\\
8:&(v_7,a_7,v_0,a_0,v_1,a_1).
\end{array}
\]

For the left coarse regular-hexagon skeleton set
\(C=(0,0), A=(-1/2,h),B=(1/2,h),D=(1,0)\),
\(P=A+t(B-A)-dJ(B-A)=(-1/2+t,h-d)\), and
\(X=B+(1-t)(D-B)+dJ(D-B)\).
Write \(\rho\) for rotation through -120 degrees about C. The sixth
congruence class has clockwise list
\(1=(C,P,B,X,D,\rho P)\). The other two left pieces are \(\rho1\)
and \(\rho^21\). This gives threefold symmetry without an extra shape.

## One exact fixed instance and reproducible scope

Take

\[
t=7/10,\quad d=4/15,\quad Q=(3/4,-4/3),\quad R=(37/50,-5/4).
\]

All coordinates lie in \(\mathbb Q(\sqrt3)\), with the positive square
root specifying the embedding. The exact verifier
[verify_dzuklevski_scaffold.py](../reviews/verify_dzuklevski_scaffold.py)
checks this one fixed instance, with no search, random seed, or denominator
cutoff:

    conda run --no-capture-output -n arisearch python3 research/reviews/verify_dzuklevski_scaffold.py

It checks strict clockwise convexity, actual hull vertex counts and areas,
six distinct congruence classes using different squared-side multisets,
empty interior intersections of the five right pieces, and their exact
area sum. It also checks the threefold left pieces have disjoint interiors
and total area \(3h\). Arithmetic uses Sage AA with exact algebraic
comparisons and no floating-point predicates. These are finite geometric
checks. They do not certify generic angle exclusions, Schmitt matching-rule
forcing, infinite tilability, or aperiodicity.

## Gaps before this mechanism can be imported

A reconstruction proof must enumerate all native-corner sums and sums
containing a straight sector. Requiring no combination to equal a tile
angle must explicitly exclude its unavoidable singleton realization;
the source's literal wording does not do this. A generic choice argument
must prove the forbidden analytic relations are nonidentities on an open
convexity domain, rather than merely note infinitely many parameter choices.
Congruence identifications must not create new corner stars. For every
internal shared edge, one must rule out unequal-length partial contacts
and certify the intended order/orientation using endpoint stars. Finally,
the clusters must partition every plane tiling and produce the intended
coarse matching data; no finite local check alone establishes this global
step. Our fixed instance has not passed any of these obligations.

Preserving the periodic coarse tilings while specializing or fusing pieces
preserves a periodic plane tiling. Therefore this family cannot become an
aperiodic source just by reducing congruence classes while retaining all
its inherited coarse tilings. Its useful contribution is a concrete convex
geometry mechanism to audit, not an aperiodic candidate.

## Countability theorem audit boundary

N. Dolbilin, *The countability of a tiling family and the periodicity of a
tiling*, DCG 13 (1995), 405–414,
[publisher abstract](https://link.springer.com/article/10.1007/BF02574052),
states that a finite protoset with a finite matching rule and at most
countably many different tilings of d-dimensional space has a periodic
tiling. The full text was subscription-restricted in this audit; therefore
its precise definition of periodicity and matching-rule hypotheses have
not been independently checked. It is a primary theorem lead, not a
new proved lemma in this repository. Independently, the source Schmitt
family itself has periodic coarse tilings, so the proposed convex
recomposition was not intended to force aperiodicity.
