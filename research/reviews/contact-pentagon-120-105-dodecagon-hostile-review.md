# Fresh whole-family review: P120/105 and equiangular Q12

Date:2026-10-13. Reviewer:source_recovery. Verdict:VALID.
Reviewed research/lemmas/contact-pentagon-120-105-dodecagon-periodic-escape.md,
research/searches/contact-pentagon-120-105-dodecagon-symbolic-carrier.py,
its retained certificate, and the root's independent alternate-embedding
checker research/reviews/contact-pentagon-120-105-dodecagon-independent.py.

All native angles exceed90, so any flat host leaves180 for native corners;
one available corner is not180 and two exceed180. Thus no corner lies
inside a side, and every contact is whole, without imposing ETE. The full
integer equation8A+7B+10C=24 has only3P120 or2P105+Q150. Species omission
therefore fails atP105 orQ150. Native counting gives p=6q, PPPcount2q,
PPQcount12q up to uniform boundary errors; this matches the carrier.

At every P105 star its two adjacent neighbor species differ, while atP120
both areP. The indexed word P,Q,P,Q,P follows pointwise. Thus Qcontacts
use only nativeu/v even if other lengths coincide. At the threeP120 star,
every full mate edge is incident to a nativeP120 on both tiles, so only
bevel slotsx/y participate. Ifx!=y each Psector requires its two incident
edge labels to differ, impossible on the odd3-cycle. Reflections do not
change this numeric two-colour contradiction. Other aliases cannot create
a P105 corner in thatPPP120 star. Hence x=y necessarily at all metrics.

With the given fixed turn directions, horizontal closure now forcesu=v;
vertical closure givesw=sqrt3*x-2u*sin15. Every Qside then has lengthu,
so its equal-angle polygon is regular. After common scalingu=1, the only
remaining freedom isw>0 andx=(w+2sin15)/sqrt3. This necessity proof is
not an assumption restricting the original source and includes all
positive coincidences x=1,w=1,x=w and other aliases.

The carrier's exact field embedding selectsR=sqrt(2+sqrt3)>1 and
sqrt3=R^2-2>0. Its regular dodecagon radiusR=1/(2sin15), unit chord
identities and its six60-degree rotations are exact. The proposedP* has
native word(x,1,w,1,x), signed angles120/105 and strict support inequalities
for ALLw>0. Producer positivity tests verify nonnegative polynomial
coefficients and at least one positive coefficient in the selected real
embedding, a sufficient whole-domain strict inequality, not a sample.
The bevel identity(2-sqrt3)R=1/R is exact. Native ordered lengths/angles
identify P* with every original normalized P, up to an allowed isometry.

The independent checker uses the SMALL quartic root h=2sin15 rather than
authorR, reconstructs P by its native edge directions and rotates it-90
to the carrier. It builds explicitQ coordinates, independently solves
unrestricted integral lattice coordinates for every reverse partner,
checks the42-edge partner involution and area=covolume. Replay PASS:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/contact-pentagon-120-105-dodecagon-independent.py

I additionally executed the complete author producer with captured JSON
and compared every field/coordinate/period/partner entry to
research/certificates/contact-pentagon-120-105-dodecagon-symbolic-carrier.json;
full dictionary equality passed. Its42 directed partners form a complete
involution (21 pairs), with no unpaired boundary edge. No producer or
retained table was imported by the independent checker.

The period determinant sqrt3*(2R+w)^2/2 is strictly positive. Locally finite
closed lattice translates have multiplicity N with distributional gradient
zero by complete oriented cancellation. Exact area/covolume1 forcesN=1
almost everywhere; open interior overlaps/gaps are impossible and local
finiteness makes the union closed, ensuring every point covered. This is
actual full-plane existence at every positive metric, not finite-patch
extension or source-language forcing. The conclusion supplies SOME periodic
tiling and never claims every original filling periodic. The specific
P120/105,Q150 palette, all its positive metrics and all reflections/contacts
are correctly covered. No objection or remaining gate in this family proof.
