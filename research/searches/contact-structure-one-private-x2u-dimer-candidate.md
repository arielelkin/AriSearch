# Hosted one-private dimer: exact single-ray candidate and necessary ring

Date:2026-10-13. Status: exact metric and necessary finite module retained;
now superseded as a candidate by the exact periodic carrier below.
The final global carrier is independently reviewed VALID; [complete witness review](../reviews/contact-right-angle-one-private-hosted-carrier-hostile-review.md). Earlier finite-ring and bridge stages below are retained as construction provenance.

## Native mechanism and single metric ray

P has native angles112.5,112.5,90,112.5,112.5 and cyclic side lengths
x,u,v,y,w, with90between u,v. Work on the structural host plane x=2u,
keeping the five P lengths distinct and excluding y,w=2u or2v and x=2v.
Thus the only possible partial contact is an R-type P x-side hosting two
S-type P acute corners, their along-host u legs and perpendicular v legs.
R means native word Q-P-Q-P-Q starting with an acute leg; S means P-Q-P-Q-P.

A Q with exactly one QQ side must have native public multiset
{x,x,y,y,u,v,w}. The private H side is flanked by u,v; each other Q side
has at least one neighbor length outside{u,v}. Any QQside would require
outgoing QPside lengths u/v at both ends, so H is the ONLY possible QQslot.
Its privacy forces it, giving exactly one QQneighbor intrinsically.
Distinct u,v exclude reflection HHgluing; every QQcomponent is a halfturn
dimer. This is a shape-derived property, not an imposed component rule.

At a full PPQ vertex, an R-S contact cannot match R bevel y to S acute u/v
or middle w: whole endpoint112.5/90 is illegal, y does not double, and
y!=w. Therefore the R_v neighbor immediately before H must be next to
the R_middle wneighbor. With Q rooted H,u,...,v, w must have tag slot6.
The two R-S boundary contacts use the R x=2u host and the S uleg, which
is incident to S's Qcontact bevel x. Hence the first and last of the four
Sside tags are x; the remaining two are y. The only native tagged word is

    Q=(H,u,x,y,y,x,w,v),

with the reflected/swap convention producing the equivalent orientation.

Set r=sqrt2,c=cos(pi/8),t=sin(pi/8), exactly defined by
8c^4-8c^2+1=0,9/10<c<1,r=4c^2-2,t=r/(4c). Normalize x=1. Then

    u=1/2,
    y=(r+2c-t-1)/(2c+t+1/r),
    v=1/2+r*c*(1-y),
    w=1+(c+1/r)*(y-1),
    H=y-(u+v-y-1)/r.

The two Pclosure and two Qclosure equations plus x=2u have rank5 overQ(c)
on six lengths, so this is the unique positive ray for that word. All six
lengths are positive and pairwise distinct, and only x=2u is a host equation,
checked exactly in the producer. No metric sampling is used.

Define P by A=(0,-w),B=A+(xc,-xt),C=B+(u/r,u/r),D=C+(-v/r,v/r),E=0.
Define Q starting at0with sidei of length above and directioni*pi/4.
Both close exactly and pass all strict support halfplane inequalities.

## Complete finite Qring domain

All contacts involving Q are whole by the reviewed native reduction.
Private QQneighbor H is uniquely its midpoint halfturn. Public u/v neighbors
use the unique corresponding Pacute leg and put P90at the H endpoint.
Each x,y,w public side has two full opposite-side endpoint identifications.
Thus the option counts are[1,1,2,2,2,2,2,1], giving exactly32Qrings.

The producer rejects positive-area overlaps; native angle multisets that
cannot occur in any palette star; and any corner in a side interior except
P_S90at the midpoint of an R_Pnative xside, with its uleg along that host.
That partial event's complementary Sguest is UNIQUE: reflect the first S
across its perpendicular vleg. The far endpoints112.5force the shared vleg
whole. Every such base-ring event is completed and the resulting mandatory
finite patch is checked again for overlap and forbidden contacts.

Exactly one ring survives all checks:
choices[0,0,1,1,0,0,1,0]. Its mandatory cap guests also survive.
This is necessary finite legality, not an infinite extension certificate.
A unique local ring does not supply plane existence or aperiodicity.

## Replay and certificate

Producer: research/searches/contact-structure-one-private-x2u-ring.py.
Certificate: research/certificates/contact-structure-one-private-x2u-ring.json.

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/contact-structure-one-private-x2u-ring.py --check research/certificates/contact-structure-one-private-x2u-ring.json

Exact domain: one algebraic metric ray,32full Qneighbor rings, plus the
uniquely mandatory Pcap guests at all base-ring flat events. No random seed,
timeout, periodic quotient, solver or unbounded radius is used. Software
versions and every first rejection witness are retained. Initial execution
hit a corrected Python spacing SyntaxError before computation/certificate;
the successful completed run above is the result.

## Historical cheap forcing test (completed below)

Unique Qring determines all three Qpartners of each R_Pneighbor, since
native Q u/v/wpublic slots are unique and P has no nonidentity symmetry.
These bridges and the HHhalfturn generate mandatory Qplacement isometries.
Check their translation rank/finite linear group before any large patch:
a nondiscrete translation group forces Qoverlap, while a discrete rank-two
group may supply a small exact periodic carrier. QQdimers alone give no
infinite-chain barrier proof. At this intermediate stage no successful construction had been asserted; the final periodic carrier below closes this exact candidate.

The exact Rbridge computation now gives pointgroup{I,-I} and only a
rank-one translation subgroup. The u-v bridge equals the existing HH
halfturn; the second apparent translation is identically zero. Therefore
this cheap group gate neither excludes the candidate nor yields a plane
carrier. The remaining Sbridges have two candidate partner-Q slots each;
the subsequent check transported the entire unique Qring across each, as recorded in the final escape below.

## Final escape for this exact metric ray

All8 possible second-Q contacts through the four Sneighbors also survive
a necessary two-Qring check, retained in
contact-structure-one-private-x2u-ring-extension.py. Their two actual
geometries are halfturn and reflection. Choosing compatible halfturns gives
a rank-two lattice and a direct exact carrier with2Qand6Prepresentatives.
All56 atomic boundary segments pair oppositely modulo the lattice and the
total tile area equals its covolume. Distributional multiplicity therefore
proves a legal periodic whole-plane cover. See the standalone stable proof
research/lemmas/contact-structure-one-private-x2u-periodic-carrier.md and
producer contact-structure-one-private-x2u-periodic-carrier.py.
This periodic construction kills this exact single-ray candidate. It does
not settle all one-private/hosted metrics or force every possible filling
to be periodic.
