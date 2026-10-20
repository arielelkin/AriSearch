# Cáceres–Márquez primary-source constructive gate

Date: 2026-10-19. Status: **Blocked as a source of an unmarked convex aperiodic pair.** This is a full-primary-text audit, not a new construction or an impossibility theorem.

## Source and bounded retrieval

José Cáceres and Alberto Márquez, *An aperiodic tiles machine*, Computational Geometry 23 (2002), 171–182, DOI [10.1016/S0925-7721(01)00060-8](https://doi.org/10.1016/S0925-7721(01)00060-8). [Open publisher-layout PDF at Universidad de Sevilla](https://idus.us.es/bitstreams/70c283bb-e95f-4d49-9891-8e0fffc01016/download).

Read research-problem.md, research-protocol.md (including §§5,13,19), current discovery-log.md, and research/literature/two-convex-primary-boundary-2026-10-19.md. This audit upgrades only that boundary's abstract-only machine entry; it does not revise other literature claims. Web search queries were `"An aperiodic tiles machine" pdf` and `"Cáceres" "Márquez" "Voronoi" aperiodic tiles machine`; claims below come from the primary PDF. The web opener returned 403, but Python urllib with User-Agent Mozilla/5.0 retrieved the complete 317238-byte PDF. SHA256: `46ac02b955d72cae8e9f3a0f12aad13218dcfe9a6aad60166fe8e7cfd2a086d2`. Text was extracted with Poppler `pdftotext -layout`; printed p178 was also rendered and visually inspected with `pdftoppm` to check Fig.8.

Replay retrieval/extraction through the prescribed environment:

```bash
mise exec -- conda run --no-capture-output -n arisearch python - <<'RETRIEVE'
import urllib.request, pathlib, hashlib
u='https://idus.us.es/bitstreams/70c283bb-e95f-4d49-9891-8e0fffc01016/download'
b=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'})).read()
assert hashlib.sha256(b).hexdigest()=='46ac02b955d72cae8e9f3a0f12aad13218dcfe9a6aad60166fe8e7cfd2a086d2'
pathlib.Path('/tmp/aperiodic-machine.pdf').write_bytes(b)
RETRIEVE
mise exec -- conda run --no-capture-output -n arisearch pdftotext -layout /tmp/aperiodic-machine.pdf /tmp/aperiodic-machine.txt
```

The temporary rendering/text are inspection aids; no exact coordinate claim depends on them. This is a literature audit, with no solver enumeration or candidate verification.

## Exact mechanism recovered

The input is **any chosen finite site template on each of Penrose's kite and dart**, transported by tile isometries to every tile of a legal Penrose tiling (§2, p173). The underlying Penrose legality includes colored-vertex matching, explicitly discussed on p173. Sites may lie on boundaries; the paper does not restrict them to centers, incenters, or one site per tile. The resulting infinite point set P is used for the ordinary, unweighted Euclidean diagram

`V(p) = intersection over q in P of {x: |x-p|^2 <= |x-q|^2}`.

Consequently the cells are convex. Lemma2 (pp174–175) asserts bounded polygonal cells and finitely many isometry classes for any fixed templates. The number depends on the chosen sites and is not universally two. Lemma9 / Theorem10 (pp178–179) assert that every relevant neighbor lies in the source tile's 3-patch; their algorithm handles all eleven 3-patches for a fixed dart and fixed kite and outputs the cells **with matching rules**. These general assertions have not been independently re-proved here and do not supply exact coordinates of a special pair.

## What is actually counted

Fig.8 and Theorem6 (p178) exhibit **five Voronoi–Penrose prototiles** and show that arbitrarily large finite cardinalities can be produced. These are decorated prototiles in the definition made on p177: congruent underlying cells with inequivalent inherited drawings are counted separately. Therefore the number five cannot silently be used as an exact count of reflection-inclusive unmarked congruence classes. Fig.8's visible cells include triangular/quadrilateral outlines, so it also supplies no all-at-least-five-sided candidate. No exact-coordinate census of its unmarked outlines is claimed here.

At p182 the authors explicitly leave open whether five is the minimum size of their collections. This is not a proof that two is impossible, and it does not exhibit a two-class specialization. Their Delaunay variant (§7) produces triangles and keeps matching rules; its four-triangle example does not meet the present objective either.

## Aperiodicity is imposed by extra rules

Theorem3 (§3, pp175–176) concerns a **generated Voronoi tiling**, not all tilings admitted by the unmarked cell shapes. Its proof appeals to reconstructing the underlying inflated Penrose tiling; this audit does not promote that reconstruction assertion to an independently checked universal recognition theorem.

Section4 (p176) explicitly separates the stronger question and observes that an obtainable rhomb cell has periodic tilings on its own (Fig.6). It then draws inherited source-tile edge portions inside each Voronoi cell. Theorem4 (p177) constructs vertex colors, edge colors and, where necessary, edge orientations. Those rules force the drawn portions to assemble into a legal Penrose tiling. Corollary5's aperiodicity conclusion is expressly conditional on these matching rules. Thus the paper's term aperiodic prototiles includes decorated placement data excluded by research-problem.md.

Section8 (pp181–182, Fig.14) considers the stronger geometric compatibility condition that the assembled cell edges should themselves be the Voronoi diagram of the associated sites. It gives a periodic escape even under that condition: one prototile is a square with its site at the center, so the square-only periodic tiling is admissible. This is exactly the omission issue in the present objective. The authors then state that the one-site-per-kite-and-dart case is unclear. They do not resolve that case by an unmarked forcing theorem or by a two-class output.

## Gate result and exact blocker

**No concrete exact two-class specialization with both classes having at least five sides and no periodic omission was found in this full source.** Convexity of ordinary Voronoi cells survives, but two-class cardinality and shape-only forcing do not follow. A generated nonperiodic source alone cannot establish the universal quantifier over all tilings of its cell shapes.

The exact missing construction is: finite exact site templates with a complete infinite-source cell census consisting of exactly two reflection-inclusive unmarked classes of at least five sides, together with an intrinsic geometric mechanism that forces every unrestricted tiling of those shapes into a nonperiodic structure and rules out each one-shape omission. The paper's labels/orientations do precisely the forcing work that has to be replaced. Its finite source-patch algorithm by itself does not replace that work.

**Stop under §5.** No new site rule, weight rule, patch enumeration or parameter sweep is licensed by this audit. In particular do not repeat existing Penrose/Ammann weighted-center gates. Reopening requires a materially changed explicit intrinsic encoding or an exact two-class specialization with a concrete recognition mechanism; then the first falsifiable gate is an exact complete cell census with infinite-tail protection and a direct periodic-omission test, before any global aperiodicity claim. The scope of this negative audit is this paper, not all Voronoi constructions or all convex pairs. The original problem remains unresolved.
