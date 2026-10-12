# Matched-endpoint P2 attachment exclusion: independent review

Date: 2026-10-12. Verdict: **VALID within the two recorded bounded domains**, subject to the marked substitution source and Z3 trust stated below. The global problem remains unresolved.

## Scope and census

The source is the primitive marked alternating Lang–Hayes P2 substitution-language hull used by the first kite/dart audit. Each labelled source type carries one repeated strictly interior centre. A selected long/short edge-role orbit carries one strictly interior matched endpoint, with its two owner-centre spokes. Corner spokes are arbitrary, with centre degree at least three. All source edges are erased. The star domain has 706 recipes: 15² for each single active orbit and 16² for both. The chord extension adds at most one endpoint-to-nonadjacent-source-corner chord per type inside one abstract fan face. There are 35 local types per single orbit, hence 35²−15²=1000 new ordered pairs per orbit. With both orbits active no such chord fits, so the extension adds 2000 recipes in total.

This is exhaustive for those normalized graph domains, not for all boundary attachments. Empty orbit activation belongs to the previously audited no-endpoint domain. Multiple endpoints per edge, multiple centres, more chords, neighbour-dependent rules, preserved source edges, changed graph incidence and arbitrary bare unmarked kite/dart sources are outside scope. The abstract noncrossing fan census allows unrealizable dart embeddings; exclusion of this geometric superset is sound.

## Independent checks

[The retained checker](kite-dart-edge-attachment-audit.py) constructs its own boundary fan cycles and split-chord cycles. It does not call producer tables, analyze routines, union/find or congruence canonicalization. It independently verifies recipe equality and uniqueness, patch digests, source-owner orientation/parity matching, local boundary interval coverage and opposite pairs of internal darts.

Every recorded negative witness is independently proved to be a connected **full** dual component avoiding the source-patch boundary. Direct graph traversal replaces the producer's component union. The checker rebuilds all decoration darts, checks slit or multiple-cycle certificates, and counts corners after conditional degree-two deletion. All 704 rejected star rows and all 2000 chord rows pass. Counts are:

| Screen | Triangle/quadrilateral | Slit | Multiple cycles | Degenerate | Retained |
| --- | ---: | ---: | ---: | ---: | ---: |
| Stars | 522 | 181 | 1 | 0 | 2 |
| Chords | 1262 | 604 | 34 | 100 | 0 |

No additional affine identically-flat simplification is needed for any rejected corner-count witness: the independent unsimplified counts after graph-degree deletion already equal the recorded counts. Thus the producer's formal polynomial straightness test and artificial complex endpoint-variable indices are not needed for this exclusion.

For stars `(kite_mask,dart_mask)=(4,2)` and `(4,8)`, the checker reconstructs every bounded component: 136 faces per recipe. It rebuilds complex affine vertex coordinates directly from source vertices and orientations and verifies each of the six stored coordinate representatives is an actual interior face, up to cyclic start. The independent real-coordinate encoder from [the earlier full audit](kite-dart-exclusion-audit.py) then produces weak-turn, positive-area, nonzero-edge and strictly interior centre constraints. Removing all six at-least-five-positive-turn constraints gives the larger minimum-zero-corner domain. Both independently encoded queries are UNSAT. Endpoint-alignment equations are omitted, so these exclusions also apply to the aligned subset. Retained SMT files and [controls](kite-dart-edge-attachment-audit-controls.json) record the result.

## Why these witnesses exclude the route

At an interior graph vertex of degree two, two convex complementary sectors sum to 2π and each has angle at most π. Both are therefore flat and the two incident rays are opposite. Deletion is a necessary consequence of convexity, not an assertion that arbitrary sample centres align. Source-boundary corners are exempt when outside incident tiles are missing. A nonzero bridge/slit cannot occur on a simple convex polygon boundary; a full component with multiple boundary cycles cannot be a convex tile. A cycle collapsing to fewer than three corners cannot retain positive area. Strict interior centres/endpoints and valid noncrossing embeddings keep the retained decoration segments nonzero; an incidence-changing degeneration is not a rescue within this graph domain.

Any convex triangle or quadrilateral among the final shapes admits a periodic tiling using that shape alone. The target allows this, so that single witnessed small face kills forced aperiodicity without congruence-class analysis. The only remaining star recipes fail even weaker necessary convexity. This excludes isolated parameters as well as continuous varying-angle families **inside these valid domains**.

## Source-language transfer

[The prior source audit](kite-dart-exclusion-audit-source.py) independently proves the ten-triangle sun occurs strictly inside a single acute half-tile supertile after four deflations and checks exact containment/area partitions of each subdivision. The same retained source seed and subdivision rule produce patch4 by four additional deflations, followed by removal of unmatched boundary halves. Continuing a legal strictly interior patch preserves legality; unlike an arbitrary finite assembled patch, this patch therefore occurs inside a legal supertile. The positive square of the two-halfstep substitution matrix gives primitivity, and the prior audit's bounded-gap argument transfers this finite witnessed pattern to every tiling of that substitution-language hull. No claim transfers to all tilings by unmarked kite/dart geometry.

Source reflection reverses corner labels and permutes corner masks/chord choices within the census; it preserves long/short roles and sends directed endpoint fractions to their complements where needed. The reflected source hull consequently does not open a missing uniform recipe case.

## Limitations and next mathematical path

No mathematical defect was found. The prior manifest's outstanding-review and finite-source-transfer caveats can now be replaced by this precise audit provenance. Producer scripts and retained certificates were not changed. The checker shares source parsing/field setup with the alignment module, explicitly checks its owner/parity outputs, and shares the independent real-coordinate encoder and Z3 engine with the prior audit. These are executable exact encodings, not formally checked UNSAT certificates.

Do not enlarge this enumeration on the strength of these negatives. A useful changed mechanism must first invalidate a used assumption: for example, a proposed higher-valence attachment should specify two final boundary words and give an exact local realization in which an endpoint has at least three distinct rays. First test that the new local rule survives source-edge matching, positive source containment and convex turns while avoiding every forced degree-two collapse and small-face periodic escape. Only a surviving exact realization justifies its two-class metric and angle-variation gates; unrestricted shape-only forcing would remain a separate obligation. The prescribed-boundary-word route already has its own bounded Ammann H-to-two-pentagon exclusion, so changing only its enumeration cap is not a new mechanism.

Replay:

```bash
MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/reviews/kite-dart-edge-attachment-audit.py
```

`MISE_AUTO_INSTALL=0` skips installation of an unrelated missing Netlify tool whose provenance check currently fails; it does not bypass that check or change the workspace configuration.
