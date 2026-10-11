# Equal-private scaffold: exact closure classification and universal escape

**Question.** Does repeating H's only private length at sides0,2 allow
cross-slot matching to evade the distinct-private periodic mechanisms?

**New result.** Same-slot seams are half-turns; allowed cross-slot seams
are glide reflections fixing the private chord direction. Four linear
chain states exist, so straight chords alone do not prove tile periodicity.
Nevertheless native endpoint constraints leave exactly six P order/beta
cases. Three are untileable, one forces repeated P lengths, and the two
mirror-equivalent survivors form a complete2D positive metric cone. Every
positive metric embeds in the earlier four-orbit continuum after side
renumbering, yielding an explicit periodic escape.

**Finite exact domain.** H=(L,a,L,b,c,d,e), P five distinct shared values
and angles beta=5pi/7 once,alpha=4pi/7 four times, L absent P. Six local
cases, three rank4 real closure systems over Q(t), t=2cos(pi/7), fifteen
collision equations, two cone ray tests, and one exact continuum parameter
substitution. No period bound, search grid, numerical geometry branch,
solver or random seed.

**Artifacts.** The lemma, producer and certificate use the common basename
`two-angle-5-7-equal-private-scaffold` under lemmas/searches/certificates.
An exact generic fixture is L=1,a=11/10. The producer prints JSON by default
and writes only with explicit --output.

```text
conda run --no-capture-output -n arisearch python research/searches/two-angle-5-7-equal-private-scaffold.py
```

Complete execution passed in the arisearch Sage environment. Its universal
proof depends on the full positive-cone existence theorem, which permits
repeated lengths; it does not import that theorem's generic rigidity claim.
Fresh review is pending. The possibility of mixed-glide nonperiodic tilings
is immaterial to this pair's aperiodicity because every feasible metric
already has an explicit periodic tiling.
