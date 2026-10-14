# Five-distinct one-private dimer: unrestricted native bridge reduction

Date:2026-10-13. Self-contained native-contact argument; fresh independent review VALID at research/reviews/contact-right-angle-one-private-native-bridge-hostile-review.md. This is the local geometric piece for the separate global frequency/limit argument, not a substitute for that argument.

Let P have cyclic native lengths(x,u,v,y,w), angles112.5,112.5,90,112.5,112.5, with the90between u,v. Assume all five lengths are pairwise distinct. Let Q have eight135angles, one private sideH, and native length multiset

    {H,u,v,w,x,x,y,y},

where H is absent from the P length set. Suppose the original shapes admit a plane tiling under unrestricted reflections and partial contacts. Then, after rotation/reflection of native labels, exactly one of the two possibilities occurs:

- x=2u and Qword(H,u,x,y,y,x,w,v);
- x=2v and Qword(H,u,y,x,x,y,w,v).

The second has no positive vector closure. The first has the exact unique positive ray already supplied with a whole-plane periodic carrier in contact-structure-one-private-x2u-periodic-carrier.md. Consequently every admitted pair satisfying this precise native length multiset has a periodic escape. No statement inferring that multiset from an arbitrary one-private pair is made here; that is the separate global counting/clean-limit gate. Relations w=2u or w=2v are allowed initially, and no edge-to-edge hypothesis is used.

Use the independently reviewed contact-right-angle-unrestricted-native-reduction.md: every native side has a constant neighbor species; all Qcontacts are whole; P has exactly the R or S binary word; only both-obtuse P sides can host a flat cap, of length2u or2v; its two acute-corner guests are S. R has PQsidesu,v,w and PPsidesx,y. S has PQsidesx,y and PPsidesu,v,w.

Because H is private its Qside must have a Qneighbor. At each endpoint its third sector is a P90corner (PQQ), so the two Qsides adjacent to H match the Pacute legsu,v. Thus root Qas(H,u,...,v), choosing reflection if needed. Any other QQside would likewise have to have BOTH neighboring native Qslots of lengths in{u,v}. Those two slots occur only once each, at1and7, and their only common adjacent slot is0. Therefore H is the unique QQslot of every Q. Its other seven neighbors are P; the u,v,w slots have Rneighbors and the x,y slots Sneighbors, since lengths are distinct. All Qcorners other than the two Hends are PPQ stars.

At an R-S PPinterface starting at one of these PPQ stars, the Rside is bevelx ory. A whole contact would require equality to one of the S PPside lengthsu,v,w, excluded by pairwise distinctness. If the Rbevel ended strictly inside an Sside, its112.5corner would be a forbidden flat corner. Thus the only possible partial interface has Rbevel as HOST and Sacute leg as GUEST, and its length is exactly2u or2v. The Swside may itself satisfy a doubling relation and host other Scorners, but it cannot host the obtuse end of this Rbevel. The Rwside is a Qcontact and cannot host Pguests because its neighbor species is constant. These points explicitly remove the possible w-double loophole.

At least one R-S transition occurs along the linear sequence of seven Pneighbors between the two Hends, because it contains three R and four S. Hence at least one of

    x=2u, x=2v, y=2u, y=2v

is necessary. At most one can hold: both equations on one bevel force u=v; equations on different bevels using the same leg force x=y. The remaining two combinations contradict Pclosure u-v=rc(y-x), where r=sqrt2,c=cos(pi/8) and rc>1: x=2u,y=2v gives (1+2rc)(x-y)=0, while x=2v,y=2u gives (1-2rc)(y-x)=0. All cases violate distinctness. By reflection it suffices to treat the sole host as x.

The R_v neighbor on Qslot7 exposes its native PPbevely at the non-H corner. Since y is not a host and an R-S whole interface is impossible, Qslot6 must have an Rneighbor exposing y. It cannot use the sole vslot already at7; among other R Qsides only middlew exposes y, so slot6 is w. Its other endpoint exposes Rbevelx. The R_u neighbor at slot1 likewise exposes x toward slot2. The remaining slots2,3,4,5 are therefore the four Sneighbors, with fixed multiset{x,x,y,y}.

Both R-S transitions at the ends of that four-S block must use the xhost. If x=2u, each Scorner at the native Qvertex is the obtuse endpoint of its aligned uleg; the adjacent native PQbevel is x. Hence slots2and5arex, forcing slots3and4toy. If x=2v, the aligned leg is v and its adjacent PQbevel is y, forcing slots2and5toy and slots3and4tox. Possible flat contacts strictly between Sneighbors cannot change these endpoint tags. This proves the two words without assuming their inner contacts whole.

For the crossed word, Pclosure and Qvertical closure imply y/x=-t/(1-1/r+t)<0, t=sin(pi/8)>0; see contact-structure-one-private-x2v-closure-obstruction.md. For the aligned word, four vector-closure rows plus x=2u have rank5 and force the retained ray. Its exact values in fact avoid every other host doubling relation, including w=2u,2v. The explicit eight-representative periodic carrier uses exactly these original P,Q shapes, with allowed Tcontacts. Thus optional initial wdouble relations create no additional closed metric in this multiset family.

Scope: a direct local reduction plus exact positive-closure and constructive escape for the specified multiset. Global density may produce a cleaner tiling of the same fixed shapes before applying this lemma; such a density/compactness step is not assumed proved by this local statement.
