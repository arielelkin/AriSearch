# Repeated middle/bevel length: binary-middle vector obstruction

Date:2026-10-13. Direct analytic proof; fresh independent review VALID at research/reviews/contact-right-angle-one-private-binary-middle-hostile-review.md.

Let P have the right-palette side lengths(x,u,v,y,w), with w=x and x!=y. Let an equiangular135 octagon Qhave native length word

    (H,u,L2,L3,L4,L5,L6,v),

where every Lj is x or y. Then P and Qcannot both close with positive native lengths, regardless of H, any host doubling relation, or any contact assumptions. The reversed u/v endpoint convention has the same obstruction. Thus every rooted one-private dimer word(H,u,permutation(x,x,x,y,y),v) is killed before a ring test. Reflection supplies the w=y dual. This is an exact necessary-metric obstruction, not a statement classifying every one-private pair.

Put r=sqrt2 and c=cos(pi/8). Pentagon closure gives

    (u-v)/r=c(y-x).

Orient Qsidei at i*pi/4, so Hside0 contributes no vertical component. The five directions2,...,6 have vertical components1,1/r,0,-1/r,-1, whose total is0. Writing Lj=x+(y-x)bj for bj in{0,1}, Qvertical closure is

    (u-v)/r+(y-x)A=0,
    A=sum_(j=2,...,6) bj*sin(j*pi/4) in Q(r).

Consequently (y-x)(c+A)=0. As x!=y, this would put c=-A in Q(r). That is impossible: c^2=(2+r)/4, whose quadratic-field norm is1/8. If c belonged to Q(r), that norm would equal the square of the rational numberNorm(c);1/8 is not a rational square. The endpoint-swapped convention yields c=A and the same contradiction.

This proof treats all32 binary-middle words analytically, not by metric sampling. The important one-private frequency branch has three x and two y middle slots, a10-word subdomain; no expansion of a killed numerical family is required. All partial contacts remain allowed because the obstruction concerns the original shape vectors before tiling.

Application gate: in an actual right-palette field a private Hslot is QQ. A unique Hside has only the midpoint halfturn mate, since support-line reflection forces u=v at the P90seam endpoint. Hence its two neighboring native Qlengths are u,v in opposite order. If those are the only native u/vslots and all remaining public values lie in{x,y=w}, the word above follows pointwise, independent of extra R_middle neighbors. This repairs that alias loophole without invoking a clean-limit/FLC argument. A separate public-frequency proof is required to infer those native multiplicities from an arbitrary one-private prototype.
