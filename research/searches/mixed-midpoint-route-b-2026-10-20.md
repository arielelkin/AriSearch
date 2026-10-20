# Mixed P/Q host split: exact first gate, 2026-10-20

**Status: stopped fixed metric; no aperiodic-pair claim.** This is route B of the [13:49 Astra assessment](astra-shape-first-assessment-2026-10-20-1349.md). The pair is distinct in angle word and contact mechanism from the stopped fixtures in the [deduplication audit](shape-first-dedup-audit-2026-10-20.md). The exact first gate succeeds as a local patch, but it fails to distinguish the mixed split from two Q/Q whole-host attachments. Plane tilability and global periodicity are unproved.

## Exact pair

Let \(z=\exp(2\pi i/60)\) and \(u(d)=z^{d/6}\) for the degree arguments below. Set

\[
 p_0u(0)+p_4u(252)=-u(144)-[u(84)+u(192)]/5,\qquad
 q_1u(96)+q_2u(132)=-2u(0)-3u(240)-u(204)/5.
\]

Define P by successive directed edges with directions \((0,84,144,192,252)\) degrees and lengths \((p_0,1/5,1,1/5,p_4)\); define Q by directions \((0,96,132,204,240)\) and lengths \((2,q_1,q_2,1/5,3)\). Vertices are indexed from zero, starting at the origin. Their angle words are respectively \((72,96,120,132,120)\) and \((60,84,144,108,144)\). The two-by-two systems are nonsingular. Exact Sage AA checks give \(p_0=1.2258408572\ldots\), \(p_4=0.7834521718\ldots\), \(q_1=2.6490817779\ldots\), \(q_2=0.0603566191\ldots\), all positive. Algebraic closure and all strictly positive turns are asserted in the replay script.

## Local first gate

Take host Q side 4, from \(A=Q_4=3z^{10}\) to \(B=Q_0=0\), length 3. Split it into guest P side 2 (length 1) and guest Q side 0 (length 2), putting P vertex 2 (120 degrees) against Q vertex 0 (60 degrees) at the split. For each of the two orders and both reflections of each guest, the script checks exact strict-interior nonoverlap using separating axes over the real algebraic field. In each order exactly one of the four reflection choices is nonoverlapping: flags \((0,1)\). The other three overlap the host or another guest. Both legal choices have collinear outgoing P side 1 and Q side 4. The P side has length \(1/5\), so its far endpoint \(E\) is in the relative interior of the guest Q side 4.

At E, the P corner is 96 degrees and the Q edge supplies a flat 180-degree sector. The gap is 84 degrees. Every tile corner is at least 60 degrees, so the gap takes exactly one corner; Q vertex 1 is the only 84-degree corner. The script checks both neighboring-side assignments and both reflection flags. In **each split order**, exactly two Q1 placements align the two boundary rays and have no overlap with the three initial tiles. Thus the explicit short outgoing offset is locally completable but does not have a unique completion.

Both host endpoints can also complete simultaneously with E. The first split order has an 84-degree gap at A and a 216-degree gap at B. An exact nonoverlapping witness uses Q1 at A, Q3+Q3 at B, and one of the Q1 placements at E. The second order has gaps 132 and 168 degrees; a witness uses P3 at A, Q1+Q1 at B, and Q1 at E. The script prints exact placement indices and reflection flags for these patches, then checks every pair of placed polygons for strict-interior nonoverlap. Its host-endpoint sequence list is a **selected witness domain**, not an exhaustive classification of every angular partition.

## Competing whole-host contacts and omission check

The host Q side 4 also takes another Q side 4 across its entire length. Both the mirror identification and reversed, half-turn identification are nonoverlapping. Their endpoint gaps admit simultaneous exact completions: mirror uses P0 at A and P2+P2 at B; half-turn uses P0+Q1 at each endpoint. Hence this metric has a concrete local Q/Q alternative at the same host side, even after its endpoints are completed. No observed successor rule distinguishes the mixed split from these whole-host arrangements. The prescribed first gate therefore **stops this metric**; further fixed-patch growth would need a new mechanism rather than the split itself.

The script also tests both pentagons against all fifteen Rao monohedral types, including dihedral relabelings and exact metric equalities, and reports no hits. Conditional on that imported classification and its hypotheses, this excludes either species tiling alone. This is the immediate omission attack, not a new proof of the classification. No translational torus enumeration was run after the local forcing test failed; no periodic tiling or aperiodicity conclusion is drawn.

## Replay and scope

Run from repository root:

```bash
mise exec -- conda run --no-capture-output -n arisearch sage research/searches/mixed-midpoint-route-b-2026-10-20.sage
```

The script uses exact cyclotomic arithmetic for coordinates and incidences and AA for all proof-relevant inequalities. It enumerates the eight prescribed split/reflection cases, all four Q1 placements at each short endpoint, and explicit selected host-endpoint and Q/Q witness sequences. It produces local existence witnesses only. It does not prove a full-plane tiling, a forced global split, or absence of periods.
