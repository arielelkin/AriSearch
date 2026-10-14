# Independent equal-private symbolic geometry and collision audit

Date: 2026-10-13. Verdict: **valid conditional on an actual clean type-R tiling**, with the central-case core repair below. Zero-density defect removal and clean-limit existence are separately reviewed obligations.

## Scope

P has one90corner and four112.5corners, acute-adjacent lengths u,v withu!=v. Qhas eight135corners and exactly two private native side slots. In the equal-private branch let their common length beH. A clean type-R tiling means every P's native word isQ-P-Q-P-Q; no four-right or flat events occur. No assumptions of five distinct Pside lengths, distinctu/v/wor general neighborhood uniqueness are made.

## Native tags survive length aliases

A Qpublic side adjacent to one QQslot has one P90endpoint and one P112.5endpoint. It must match one acute-adjacent native Psideuorv, with its acute endpoint prescribed. A Qpublic side not adjacent to any QQslot has two P112.5endpoints and, in typeR, must match the middle opposite native Q-labeled Psidew. Although the other two Pnative sidesx,yalso have two obtuse endpoints, their type-R labels areP, so they cannot match Qeven if their lengths happen to equalw,uorv. Thus angle and neighbor-species tags distinguishwfromu/vwhenw=uorw=v.

Tagged native incidences give oneu,onevandonewQcontact per P. With fixed two-slot QQmask, clean corner balances givep=2q+O(R), so the six public Qslots contain exactly two tagged u,two tagged v,two tagged wby lettingRgrow. Slot tags are fixed by endpoints;u!=vthen fixes each acute tag by its length.

## Distance-three mask

Normalize private indices0,3. The two short-gap slots are tagged acutea,b; the four long-gap slots arec,w,w,d. All four acute tags comprise two uand two v. Mixed shortu/vputs PPnative sidesxandyagainst one another at their common PPQvertex. Their far endpoints are112.5, so neither can end within the other side; whole equality forcesx=y. Pentagon closure givesu-v=sqrt(2)cos(pi/8)(y-x), contradictingu!=v. Hence the short gap isuuorvvand the long acute endslots are respectivelyvv oruu.

Foruu the word is[H0,u,u,H3,v,w,w,v]. Exact vector closure with edge directionsi*pi/4gives

    H3=v+(1+sqrt(2))(w-u),
    H0=H3.

The vvcase swapsu,v. This conclusion is unaffected by any wlength alias. Reversing the word maps sidei to3-i, producing an actual reflection symmetryFexchanging the private sides0,3. Its private slots are nonopposite, so the polygon cannot be centrally symmetric.

## Distance-four mask

The word is[H,a,w,b,H,c,w,d]. The private andwopposite edge vectors cancel. The remaining coordinate sums are proportional to

    a-b-c+d=0,  a+b-c-d=0,

so a=candb=d. Tagged counts then make(a,b)=(u,v)or(v,u). The whole Qword repeats after four edges and Qis centrally symmetric. A reversed second gap would forcea=b, henceu=v, excluded. This check does not requirew!=uorw!=v.

## Geometric quotient and forced QQplacements

In the distance-three case the actual reflection symmetry exchanges the two private side slots; in distancefour central symmetry exchanges them. Composing with that symmetry identifies the two native-Hmatching choices as actual polygon sets. Thus each private contact has only two geometric placements on its unoccupied side: support-line reflection or midpoint half-turn. The former fixes endpoints and gives equal outgoing QPside lengths at each endpoint. Those are the two acute native Plegs at the intervening90sector, contradictingu!=v. Therefore actual QQneighbor placement is uniquely the midpoint half-turn in both masks. Length aliases ofwdo not change this endpoint argument. No full Q/Pneighbor-ring uniqueness is asserted or needed here.

## Essential central-case core repair

The reviewed distinct-private Qcore used absence of central symmetry to exclude odd closed QQcomponents. That argument cannot be copied into distancefour. Instead, ifQhas centerzand opposite private midpointsm0,m4, thenm4=2z-m0and the midpoint half-turnH0acts on the polygon set as translation by2(m0-z)=m0-m4. H4acts by its negative. This is a nonzero vector. Every QQcomponent is therefore a two-sided translation orbit and cannot close. Its two-step period remains2(m0-m4). This supplies the same finite-motif core, proper-line barrier, common-period and complementary-band conclusions with a corrected infinite-chain proof.

For distance-three reflection-symmetric Q, the old noncentral odd-cycle exclusion remains valid; its two-step vector is2(m0-m3). The ordinary core/bands/anchored-completion synthesis can then construct a periodic completion of the clean tiling. It does not prove every original dirty filling or even every clean Pcompletion periodic.

No other collision defect was found in this symbolic geometry. The remaining global gate is the separately supplied existence of a clean plane tiling from the zero-core count, not a metric sweep or an imposed type-R rule.
