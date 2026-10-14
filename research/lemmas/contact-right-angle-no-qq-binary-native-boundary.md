# Binary native octagon boundary in a global noQQ tiling

Date: 2026-10-13. Status: independently reviewed VALID; see [fresh unrestricted audit](../reviews/contact-right-angle-no-qq-hostile-review.md). Dependencies: `research/lemmas/contact-right-angle-unrestricted-native-reduction.md` and `research/lemmas/contact-right-angle-no-qq-periodic-carrier.md`.

## Exact statement and scope

Let P have native angles90,112.5,112.5,112.5,112.5and acute-adjacent lengthsu!=v. Let Qhave eight135angles. Name the cyclic P side lengths (x,u,v,y,w), with u,v incident to the90corner; x,y are the neighboring nonacute-adjacent slots and w the opposite side. In the P-Q-P-Q-P word the Q labels are precisely x,y. Suppose an entire admitted plane tiling has NOpositive-length Q-Qcontact anywhere. This is a source hypothesis, not a shape-only conclusion from one isolated Qinside a mixed tiling.

Then x!=y, Qhas exactly fourxsides and fourysides, opposite sides have equal lengths, and up to cyclic shift/reversal its binary native word is eitherxyxyxyxyorxxyyxxyy.

The alternating word is impossible even with unrestricted partial contacts and all native side-length coincidences. Thus its Q is the grouped binary octagon. The explicit carrier for that original P/grouped-Q pair supplies a legal periodic escape, irrespective of other admitted tilings. No edge-to-edge rule is assumed; doubled-leg host planes are included.

## Proof

Native reduction gives whole Qcontacts and the two Pneighbor words. Any P-Q-Qacute star contains a QQcontact, so the noQQtiling has only P-Q-P-Q-P Ptiles. Every Qside therefore matches one whole Pxoryside. Pclosure givesu-v=sqrt(2)cos(pi/8)(y-x), so u!=vimpliesx!=y.

With noQQendpoints, the y-star count in the angular ledger is0and8q=2p+O(R), hencep=4q+O(R). Counting whole native xcontacts givesn_xq=p+O(R), where n_xis the fixed number of Qslots of lengthx. Positive uniform quadraticqfollows from coverage and the ledger, so n_x=4; likewise n_y=4. No frequency assumption is used.

Rotate Qso its edge directions arei*pi/4. WriteL_i=x+(y-x)b_iwithb_iin{0,1}. Baselineequal edges sum to0, so closure withx!=ygives sum b_i d_i=0. Splitting rational andsqrt(2)coefficients yields

    b0=b4, b2=b6,
    b1+b7=b3+b5, b1+b3=b5+b7.

The last two implyb1=b5,b3=b7. Thus every binary closed word has opposite pairs equal: exactly16words before side-count filtering. With fouryslots, the first fourbits have exactly twoones. Up todihedral symmetry these are adjacentones(0011)or alternatingones(0101), giving the two words stated.

At a mixed x/y Q corner, the Px neighbor exposes either native PP side u or w, while the Py neighbor exposes v or w. Both sides start with112.5 corners at this actual PPQ vertex. Their common interface ends at the nearer native endpoint. A native112.5 endpoint cannot lie in another side interior. A native90 endpoint may do so only as a flat event; its host must be a P side with BOTH endpoints112.5, by the reviewed no-acute-adjacent-host theorem. Such a host has length exactly twice the guest acute-adjacent length.

Consequently the complete possibilities at a mixed Q corner are:

- w/w, which is a whole equal-length contact;
- u/w, possible only when w=2u, with the short u leg ending at a flat midpoint of the w host;
- w/v, possible only when w=2v, similarly.

The u/v case is impossible: u!=v would put the shorter90 endpoint inside the longer acute-adjacent host, forbidden. Equal-length u/w or v/w is also impossible because the common far endpoint would have90+112.5, belonging to no full star. A shorter w would end with112.5 in the other side interior, forbidden. These endpoint arguments remain valid with arbitrary length aliases and do not require an edge-to-edge tiling.

Since u!=v, the two relations w=2u and w=2v cannot both hold. If neither holds, every mixed corner exposes w/w. If only w=2u holds, every Py neighbor at a mixed corner must still expose w (never v). Thus in an alternating Q word its single native y side would need the same w-adjacent endpoint E at both ends, impossible. If only w=2v holds, the same contradiction applies to every native x side with its w-adjacent endpoint A. In the no-host case either contradiction applies. Hence the alternating word is impossible in every admitted global noQQ tiling.

In the edge-to-edge subbranch, the grouped word further forces u/u at xx corners and v/v at yy corners: every mixed corner is then w/w, so the same-type endpoint of each Q neighbor must expose its acute-adjacent PP side. This gives rigid four-P90 modules there. Outside that subbranch the carrier still establishes a periodic escape without assuming the original module decomposition.

## Non-consequences

The source noQQassumption is not inferred from arbitrary k=0metrics. A single isolated octagon in a mixed tiling does not imply the global ledgerp=4qor this binary length alphabet. Doubled-leg P-P partial contacts are included by the midpoint-host case split above; the proof does not claim the original tiling has no such contacts. No all-pairs or all-right-palette impossibility theorem is claimed.

## Shape-only binary-Q corollary

Suppose, without imposing any adjacency rule, that EVERY native Q side length lies in {x,y}. Then every admitted tiling automatically has noQQcontacts. Indeed a type-R Pwould need both acute-adjacent lengths u,v to match Q sides. Since u!=v and x!=y, this would force {u,v}={x,y}. If x=u,y=v, pentagon closure gives (1+rc)(u-v)=0. If x=v,y=u, it gives (1-rc)(u-v)=0. Both are impossible: rc>1 since (rc)^2=1+r/2. Thus no type-R Pcan occur. Every P is type-S, and every QQendpoint would require a type-R P90sector, contradiction. The argument admits all partial contacts through the reviewed native reduction.

Applying the preceding noQQanalysis, any tileable binary-Q pair must have the grouped word and therefore admits the explicit periodic carrier. All other closed binary words are untileable: side counting rejects those without fourx/foury, and the unrestricted mixed-corner argument rejects the alternating word. Hence no pair in this explicit binary native-length subfamily is aperiodic. This is a shape-only exclusion; it does not claim that all zero-private Qpartners use onlyx,yor have noQQcontacts.
