# Crossed acute-leg host: direct positive-closure obstruction

Date:2026-10-13. Exact standalone replay PASS; fresh independent review VALID at research/reviews/contact-right-angle-one-private-native-bridge-hostile-review.md.

For the right-angle pentagon/equiangular135-octagon palette, the rooted Qword

    (H,u,y,x,x,y,w,v)

cannot coexist with positive P lengths(x,u,v,y,w) satisfying Pclosure and x=2v. This is a direct vector-closure obstruction, valid without any distinctness assumption. It kills the necessary word of the changed crossed-host one-private dimer mechanism; it does not exclude arbitrary hosted or one-private palettes. Its reflection dual is y=2u.

In the motivating mechanism all five P lengths are distinct, H is private, public Qmultiset is{x,x,y,y,u,v,w}, and only the R xside can host a flat cap, now using two S vlegs because x=2v. Exclude x=2u and y,w=2u or2v. At a Qcorner an Rbevely cannot meet an Sneighbor through an unequal acute-leg interface or a whole middle-leg interface; hence R_v next to the private Hside must neighbor R_middle on Qslot6. Both remaining R-S interfaces run along R xhosts, and the Sguest vleg is incident to its native Qbevely. The first and last of the four Sslots are therefore y; the remaining two are x, giving the word above. This is a changed incidence mechanism from x=2u, whose word was(H,u,x,y,y,x,w,v). It is not a parameter enlargement of that completed ray.

Set r=sqrt2,c=cos(pi/8),t=sin(pi/8)>0. Pentagon vector closure gives

    u-v=rc(y-x),
    w=(u+v)/r-t(x+y).

As x=2v, these imply

    w=x/r+c(y-x)-t(x+y).

The vertical component of Qclosure for the stated word is

    (u-v+x-y)/r+y-w=0,

and therefore

    w=y+(c-1/r)(y-x).

Equating the two expressions for w and cancelling common terms yields

    -t(x+y)=y(1-1/r),
    y/x=-t/(1-1/r+t)<0.

Because r>1 and t>0, the denominator is strictly positive. Thus x,y cannot both be positive. No inequality based on numerical sampling or a finite search is used, and horizontal Qclosure need not even be consulted for this obstruction.

The standalone exact producer research/searches/contact-structure-one-private-x2v-closure.py also retains all five linear rows over Q(c), proves rank5, and verifies the unique normalized kernel

    (x,y,u,v,w,H)=(1,1+2c-4c^2,-8c^3+4c^2+2c-1/2,
                  1/2,-8c^3+2c^2+4c,8c^3-4c^2-2c+1).

Its sign pattern is(+,-,-,+,-,+), consistent with the direct proof. There is no positive metric to pass to a ring enumeration.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/contact-structure-one-private-x2v-closure.py
