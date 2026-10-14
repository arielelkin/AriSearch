# Symbolic equal-private distance-three glide family

Date: 2026-10-13. Status: independently reviewed VALID throughout the declared positive parameter domain; [hostile review](../reviews/contact-right-angle-symbolic-glide-hostile-review.md). This broadens the exact metric by symbolic necessary geometry, not by sampling or enlarging a search bound.

## Exact parameter domain

Put r=sqrt(2),c=cos(pi/8),t=sin(pi/8), with the degree-four defining data8c^4-8c^2+1=0,9/10<c<1,r=4c^2-2,t=r/(4c). Choose positive real x,y,u,v,w satisfying

    (u-v)/r=c(y-x),
    w=(u+v)/r-t(x+y).

Require u!=v, pairwise distinct u,v,w, and x,y absent from{u,v,w}. Define

    H=v+(1+r)(w-u)=2(v-cy).

Require H>0 and H absent from{x,y,u,v,w}. These hypotheses imply x!=y and all five Pside lengths distinct.

Define PbyA=(0,-w),B=(xc,-w-xt),C=B+(u/r,u/r),D=C+(-v/r,v/r),E=0, cyclic orderA,B,C,D,E. The constraints close the edge vectors and positivity makes Pstrictly convex with angles112.5,112.5,90,112.5,112.5.

Define Qby cyclic positive lengths[H,u,u,H,v,w,w,v]and edge directionsi*pi/4fori=0,...,7, starting at0. The chosen H closes both coordinate sums. Positivity makes it a genuine135equiangular octagon. Its only private slots are0,3.

**Claim:** Every admitted plane tiling by this pair has a nonzero translation period. Plane existence is not asserted for arbitrary parameters; a forced ring may fail remotely to pack, which simply makes that metric untileable.

## Intrinsic defect-free native language

The reviewed native reduction gives whole Qcontacts and native PwordsPQPQPorQPQPQ. The P-Q-P-Q-P word would require itsx,ysides matched to Q, impossible becausex,yare absent from Q's length set. Thus every P hasQPQPQ, three Qneighbors and no acute P-Pstar. Every90corner is PQQ; there are no four-right or flat events anywhere. Every tiling is therefore edge-to-edge without imposing that rule.

Every Q has the two private QQslots0,3and no further QQslots. Itsu/vpublic neighbor edges identify unique native Pacute legs, and widentifies P's unique opposite side. At every Qendpoint next to a private edge, the incident Pcorner is90; elsewhere the Pcorner is112.5.

## Symbolic removal of all four binary branches

The Qside word has an exact reflection symmetryFexchanging native sides0and3,1and2,4and7,5and6. It fixes vertices2and6; its axis is the line through them. This follows by reversing the cyclic word and its uniform angle sequence, or by reflecting the edge vectors. It is an actual unmarked polygon symmetry.

Across a private Qside, matching either private native Hside gives, after quotienting F, exactly two geometric opposite-side placements: reflection across the shared support line or half-turn about its midpoint. In the reflected placement, outgoing QPsides at each fixed endpoint have the same length. They would be the two acute legs of the unique intervening P90, contradictingu!=v. Thus the QQplacement is uniquely its midpoint half-turn. This excludes one branch independently at each private side. No endpoint-index marking is used.

The Pneighbor on native Qside4has lengthv and its acute endpoint next to QQside3. At its other endpoint, adjacent PPside is nativey, becausev=PedgeC-Dand its obtuse endpointDmeets edgeD-Eof lengthy. At the common Qvertex with side5, the wneighbor's incident PPedge must therefore also be y. Its two possible endpoint correspondences expose eitherxory there. Sincex!=y, exactly the ychoice survives. This fixes side5. The symmetric argument at side7fixes side6. At their shared Qvertex, the two chosen wneighbors exposex/x, consistent. These are the remaining two branches.

The acuteu/u short-gap neighbors exposex/xat their common obtuse Qvertex. Thus all16formal branch combinations reduce to one candidate ring up to an isometry fixing Q. This is necessary uniqueness: possible remote overlap in that candidate does not produce another ring and may invalidate existence, but cannot produce an aperiodic tiling. Rejected QQbranches requireu=v; rejected wbranches requirex=y. No additional metric equality is silently discarded within the declared domain.

## Glide transport and universal period

LetH0,H3be half-turns about the private side midpointsm0,m3. SinceFswaps the sides,FH0F=H3. The isometryS=H0Fhas determinant-1and

    S^2=H0H3=translation by d=2(m0-m3)!=0.

AlsoSQ=H0QandS^(-1)Q=H3Q. Thus the unique ring's QQcomponent isS^nQ,ninZ, with a two-tile translation motif. It and all forced Prings are periodic underd. No finite chain can occur: any repeated even placement would imply a nonzero translation symmetry of a bounded Qpolygon; an odd glide repetition squares to such a translation.

The exact-pair chain-barrier proof now applies without numerical ring data. Centroid/seam-midpoint paths form disjoint proper embedded lines within bounded slabs parallel to the respective isometric images ofd. Nonparallel lines would cross by proper-line Jordan separation. All chain periods therefore have parallel directions and equal lengths, hence one common vector up to sign. Every Pbelongs to a forced Qring, so the whole admitted tiling has that period.

## Declared exceptions and scope

This proof does not coveru=v(and hencex=y), collisions amongu,v,w, xorycoinciding withu,v,w, Hcoinciding with any Pside length, H<=0, or a different Qnative word. Such cases may admit additional native neighbors, reflected QQplacements, or ambiguous endpoint choices and require separate arguments. No metric sweep is proposed. The proof establishes a restricted all-tilings periodicity theorem, not all-metric plane tileability or an unrestricted two-convex impossibility result. The linked independent review found no unresolved objection within this declared domain.
