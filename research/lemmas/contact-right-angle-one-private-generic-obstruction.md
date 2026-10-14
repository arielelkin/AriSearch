# Fully distinct nondoubled pentagons cannot tile with a one-private octagon

Date:2026-10-13. Status: independently reviewed VALID; [fresh complete audit](../reviews/contact-right-angle-one-private-generic-hostile-review.md). This is an unrestricted necessary obstruction in one exact angle palette, not a general two-convex impossibility theorem.

## Exact hypotheses

Let P be a genuine convex pentagon with cyclic native side lengths(x,u,v,y,w) and angles112.5,112.5,90,112.5,112.5at the corresponding vertices, so u,vmeet at90. Let Q be a genuine convex octagon with eight135angles. Assume all five Pside lengths are pairwise distinct, and none ofx,y,weis2uor2v. Suppose exactly one native Qside slot has a length absent from all Pside lengths.

**Theorem.** There is no plane tiling by unmarked isometric copies of P,Q, allowing reflections, arbitrary contacts and prototile omission initially.

Dependencies: the reviewed `contact-right-angle-unrestricted-native-reduction.md` supplies native side-neighbor words, allQcontacts whole, at most two QQslots separated by3/4, and every possible flat host is a both-obtuse Pside of length2uor2v. The no-doubling hypotheses therefore force every admitted tiling to be edge-to-edge, without imposing that rule. Four-right stars are initially retained.

## All tiles are typeR, without a dimer assumption

TypeR P has Qneighbor slotsu,v,w and PPslotsx,y. TypeS P has Qslotsx,y and PPslotsu,v,w. A whole R-S PPcontact would match one of{x,y}to one of{u,v,w}, impossible under pairwise distinctness. Thus no R-S PPinterface exists.

Each Qhas its private side matched to Q, so it has at least one QQgap in its cyclic neighbor word. At each QQendpoint the guest P90is typeR. Along any consecutive run of Pneighbors around Q, adjacent guests meet at a PPQvertex and share a whole PPside. Their types cannot change by the preceding R-Sobstruction. Each run starts and ends next to a QQgap, hence every guest in every run isR. Every P has at least two Qneighbors by native alternation, so all Ptiles in the whole tiling areR. In particular no flat or four-right star remains.

The private length Hoccurs on exactly one Qside (another occurrence would be a second private slot). Normalize it as side0. Its QQmate must use the same native side. The two opposite-side isometric placements are support-line reflection or midpoint half-turn. Reflection gives equal outgoing QPside lengths at each fixed endpoint, contradicting the two distinct P90acute legsu,v. Thus the Hmate is uniquely its midpoint half-turn. It follows that the two outgoing public native lengthsL1,L7are u,v in opposite order: the half-turn switches the endpoints and those outgoing lengths are precisely the two legs of the intervening P90.

## A Qcannot have only one QQside

If its only QQside isH, sides1,7are taggedu/v. All five remaining public sides2,...,6have two obtuse P endpoints; in typeR the only such Q-labeled side isw. Orient native sidei at i*pi/4. The vertical closure of

    (H,u,w,w,w,w,w,v)

is(u-v)/sqrt(2)=0, since the five wdirections have zero total vertical component. Swappingu,vchanges only the sign. This contradictsu!=v. Therefore every Qhas exactly two QQslots.

## The second native QQslot is fixed geometrically

It lies at j=3,4or5by native mask spacing. With all guestsRthe two middle public wslots are:

    j=3: positions5,6, with position2acute;
    j=4: positions2,6;
    j=5: positions2,3, with position6acute.

Since wdiffers fromu,v, no fixed Qshape can support two of these masks. Thus all Qcopies have the same native second QQslotj. This is an intrinsic mask conclusion, not a presumed one-private dimer field or a frequency limit.

Whole tagged contact counts now show each Qhas two publicu,two publicv,two publicwslots. Indeed all P areR, corner balance givesp=2q+O(R), and each Pcontributes one Qcontact of each tag. For a fixed native mask and distinctu,v,w,the tag countsN_iq=p+O(R)and quadratic coverage forceN_i=2.

## Closure forces a second private length: contradiction

Write Jfor the length of native QQsidej. Every non-H Qslot has a Pnative length, soJ!=H.

Forj=3the public word is(H,a,b,J,c,w,w,d). Mixed short-gap acute tagsa!=bwould require the two neighboring PPedgesx,yto match whole, contradictingx!=y. Thusa=b, and the two-each counts forcec=dto be the other acute tag. Forword(H,u,u,J,v,w,w,v), exact coordinate closure gives

    J=v+(1+sqrt(2))(w-u), H=J.

The swapped case has the same equality. Reversal reducesj=5to this case. Both contradictJ!=H.

Forj=4the word is(H,a,w,b,J,c,w,d), where acute tags are two u,two v and the unique Hseam requiresa!=d. Thus{a,d}={u,v}and{b,c}={u,v}. Vertical closure givesa+b=c+d. The optionb=a,c=dwould give2(a-d)=0, impossible. Henceb=d,c=a. Horizontal closure then reduces toH-J=0, again contradictingJ!=H.

All possible masks are exhausted. No admitted tiling exists.

## Relation to the 60-word closure computation

The retained computation `contact-structure-one-private-dimer-words.py` studies the conditional one-QQ dimer word alphabetH,u,perm(x,x,y,y,w),v(and the acute swap). It finds48positive generic closure cones among60rooted words. Those are exact polygon metrics, not plane tilings. This theorem does not assume a one-private side forces dimer degree: it explicitly treats and excludes degree2as well. Its proof is analytic and independent of those cone records.

Side collisions, doubled acute-leg host planes, symmetric P, zero/two private slots and other angle palettes remain outside this obstruction. No novelty claim or unrestricted final result is made.
