# Angular-first ordering comparison

Date: 2026-10-24. Completed optimization experiment on the unchanged finite
mixed-angle domain. **Final leads remain zero.** The global convex-pair problem
remains unresolved.

## Measured outcome

Separate fresh Python processes ran the complete original pipeline and the
angular-first pipeline with the same exact arithmetic and metric-screen code.
The fresh full baseline reproduced the previous catalogue, preflight and
compressed-audit hashes before comparison.

| Phase, process CPU seconds | Original order | Angular first |
|---|---:|---:|
| Exact-engine import | 1.49 | 1.52 |
| Early angular check | — | 0.02 |
| Support catalogue | 7.90 | 6.76 |
| Metric preflight | 56.71 | 41.15 |
| Total | 66.09 | 49.46 |

Total CPU time fell by 25.17%, about 25% in this paired run. Total wall time
was 65.54 versus 48.79 seconds. This is one measurement on this machine;
the removed work and exact-domain equivalence are independently reproducible.

## Same domain, earlier rejection

The nominal domain remains P5 angles`(105,105,105,105,120)` and all 16 Q7 cyclic
angle words from`(120^3,135^4)`, `(120^4,135^2,150)`, `(120^5,150^2)`, with exact
unit-normal support offsets`{1,2}` and every possible mixed-edge relative
scale. Reflections and relative size are preserved. Nothing was added to
or silently dropped from that nominal domain.

The new wrapper checks both root species' angle-only endpoint cycles before
constructing support polygons. It rejects exactly the two Q words
`(120,120,120,120,150,120,150)` and
`(120,120,120,150,120,120,150)`. The necessary first-surround obstruction and
complete reflected cycle traces were independently checked in the
[preceding experiment](astra-followup-report-2026-10-24.md).

| Work | Original order | Angular first |
|---|---:|---:|
| Nominal support assignments covered | 2,080 | 2,080 |
| Support polygon constructions | 2,080 | 1,824 |
| Active support definitions | 545 | 502 |
| Catalogue classes used by metric screen | 418 | 391 |
| Pentagon / heptagon shape pairs | 7,960 | 7,420 |
| Raw pair-and-scale cases | 158,264 | 150,102 |
| Inequivalent metric cases | 150,226 | 142,576 |
| Exact three-polygon star checks | 357 | 0 |
| Rational incidence solves | 14 | 0 |
| Final leads | 0 | 0 |

The early proofs cover 256 support assignments without constructing their
polygons. The reduced catalogue has 20 pentagons and 371 heptagons from 14 Q words;
it is explicitly labelled a filtered catalogue, not a new full-domain census.
Of its 150,102 raw scale rows, 7,526 are common-scale duplicates and 142,576 fail
a native-corner support requirement. The cases formerly reaching expensive
star geometry or incidence belong to the two early-rejected patterns.

## Exact comparison and verification

The independent checker revalidates all 16 early angle certificates and the
complete 2080 = 1824 + 256 domain partition. It requires every reduced polygon,
identity and defining support assignment to equal the accepted-angle subset
of the previously audited full catalogue. It then streams both metric audits
and requires exact equality of every retained 150,102 rows, including its
relative scale, rejected-corner data and common-scale reference. This compares
complete finite records rather than relying on unchanged empty lead totals.

A fresh optimized-only replay reproduces all scientific hashes. Timings are
excluded from those hashes. Prior source files and retained evidence remain
unchanged; the original pipeline is kept as the replay baseline. New tests
also check that rejected words never call support geometry, that an existing
output is refused before launching the expensive baseline, and that omitted
or altered catalogue/audit/manifest data are rejected.

**84 discovery tests passed.** Independent full nominal-coverage, angle-proof,
catalogue-subset, metric-row and manifest checks passed. One fresh optimized
replay matched the retained catalogue, prefilter, preflight, gzip and worker
hashes. The full cold baseline had separately matched the original scientific
fingerprints. The historical replay registry is unchanged.

## Inspect or reproduce

The [comparison manifest](runs/mixed-angular-first-2026-10-24/manifest.json)
contains the full phase timings, source hashes, old-baseline bindings and work
counters. The [early angle proofs](runs/mixed-angular-first-2026-10-24/angle-prefilter.json),
[filtered catalogue](runs/mixed-angular-first-2026-10-24/catalogue.json),
[metric preflight](runs/mixed-angular-first-2026-10-24/preflight.json), and
[compressed scale audit](runs/mixed-angular-first-2026-10-24/scale-audit.jsonl.gz)
are retained alongside it.

Read-only verification, with one fresh optimized pass:

```bash
mise exec -- conda run --no-capture-output -n arisearch python -m research.discovery.angular_first_verify --replay
```

Repeat the full cold-process comparison in a new directory:

```bash
mise exec -- conda run --no-capture-output -n arisearch python -m research.discovery.angular_first --output /tmp/arisearch-angular-comparison
```

Run only a fresh angular-first pass:

```bash
mise exec -- conda run --no-capture-output -n arisearch python -m research.discovery.angular_first --replay --output /tmp/arisearch-angular-only
```

Comparison hash:`946d590e4283d02f23e6ec6106e1b768632ec5caea6514ec0d611524bf12e9b7`.
Optimized worker hash:`fe648da72d1007036138c29e19bc42f5e3e71da2745e13aa49a1280ed37a2487`.

The new entry point changes ordering and bypasses certified impossible angle
patterns. It does not widen the candidate family, provide a growth engine,
or establish a global impossibility theorem.
