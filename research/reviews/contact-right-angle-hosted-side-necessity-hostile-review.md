# Fresh hostile review: one-right-angle hosted-side rigidity

Date: 2026-10-13. Independent reviewer: contact_structure.
Artifact: [local lemma](../searches/contact-right-angle-hosted-side-necessity.md).
Verdict: VALID, including arbitrary reflections and partial contacts.

The complete angle equations give only flat host plus two P90 corners.
Neighbor changes on a host side therefore preserve P species; Q corners
cannot occur in such changes. A contact component with one convex neighbor
is an interval, and between consecutive changes the same P tile would have
acute corners at both endpoints. Since P has only one acute corner, two
interior changes on a single native host side are impossible. Native host
endpoints are not included in this statement.

At a flat event the two right sectors meet along a perpendicular ray. Their
shared acute-adjacent P edges cannot have unequal lengths: the shorter
endpoint is P112.5, and lying in the longer side interior would violate the
flat language. Equal matched acute-adjacent lengths give equal remaining
acute-adjacent lengths, even for reflected placements; if u!=v only same-slot
length matches are possible. If u=v the two descriptions agree.

For a Q host, the P sides on the host terminate at its native endpoints:
terminating inside would require a second flat event or a P112.5 flat corner;
extending past would put Q135 in a side interior. Thus both P sides are
whole, their equal lengths force the midpoint, and the host has length 2u or
2v. The perpendicular shared edge uses the other length. A Q side with no
flat event is a whole contact with one neighbor, because neither Q endpoint
can lie in the neighbor side interior.

I attempted to transfer this Q-host claim to P hosts. It would fail without
additional endpoint analysis because a P90 endpoint can be flat in another
side. The artifact expressly excludes that strengthening. Neither finite
orientations, edge-to-edge global forcing, nor periodicity is concluded.
No unresolved objection or computation remains.

## Fresh review of added claim 5

Claim 5 is VALID. Adjacent Q-neighbor slots would give three 135 corners,
since a convex neighbor cannot share two noncollinear whole sides. A Q-P-Q
substring forces the middle P-side contact to contribute P90 at both native
Q endpoints. A Q-hosted split has P112.5 at these endpoints, so is impossible;
a whole P neighbor would require two acute corners on one P, also impossible.
Thus QQ slots have cyclic spacing at least three and there are at most two
per octagon. The labeled count is one empty word, eight singletons, eight
unordered pairs at cyclic distance three, and four opposite pairs: 21 total.
All 256 binary eight-cycle words are covered by this elementary classification;
no computer search or extension assertion is needed. No unresolved finding.

## Fresh review of added claim 6 and P-host refinement

Both are VALID. Every P112.5 corner is a full PPQ star, and its two incident
side-neighbor species differ. No such corner can lie inside a side, because
flat stars have only P90 native sectors. Species is constant along each native
side, including any allowed interior subdivision. Four consecutive obtuse
corners therefore enforce four flips and equal neighbor species on the two
acute legs. At a hypothetical Q-host T each guest acute corner instead has
Q along the host and P along its perpendicular common interface. These are
positive initial contact intervals on genuine native legs, so an endpoint or
later subdivision cannot avoid the contradiction. Thus t_Q=0 in every actual
plane tiling. Every Q-P contact is whole on both tiles; extending beyond an
endpoint or ending inside would require forbidden Q135 flat incidence or a
Q-hosted T. P-P partial contacts remain explicitly allowed.

For a P host whose native side has two obtuse endpoints, those endpoints
cannot be flat in another tile. A side with an interior T has two guests,
whose acute corners are at T and whose other ends are obtuse. The two
along-host guest legs therefore end exactly at the host endpoints. Their
shared perpendicular legs match whole and have equal lengths; consequently
the other acute legs also have equal lengths, even allowing reflections.
The host side length is 2u or 2v. Hosts incident to the native P90 corner
retain the expressly stated endpoint caveat. No hidden edge-to-edge global
assumption or iteration/extension claim is present.

## Fresh review of the stable unrestricted reduction and no acute host

Reviewed [stable lemma](../lemmas/contact-right-angle-unrestricted-native-reduction.md).
Verdict: VALID, including new claim 6 excluding an acute-adjacent P host.
The reciprocal-cap proof closes the endpoint loophole explicitly: a guest
P112.5 endpoint cannot coincide with the host P90 endpoint because no allowed
full star contains both angles. It must extend across that endpoint, creating
a reciprocal flat event. Whole perpendicular cap matching at the original
T makes the right guest leg length L_B; matching its far obtuse endpoint to
the host far obtuse endpoint forces L_A=d+L_B. At the reciprocal T the left
guest leg is L_A, and its far endpoint must match B, forcing L_B=d+L_A.
Reflections may exchange native acute legs but do not alter equality of the
other legs, since either matched u/v are equal or same-length native slots
match. Thus d>0 is impossible. All hosts are both-obtuse P sides and have
length 2u or 2v. The stated generic metric condition really excludes every
flat star, while retaining full four-right stars.

The stronger local private-mask conclusion follows because all Q-P contacts
are whole: private slots must be Q-neighbor slots, of which there are at most
two, at cyclic distances three or four. Exactly two private slots fix the QQ
mask. The uniform O(R) consequence for four-right/flat defects is correctly
stated only as zero quadratic density, not their absence or an edge-to-edge
trivalent reduction of every tiling. No new gap was found in the extracted
stable statement.
