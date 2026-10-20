# Negative Hat weight: finite pentagon congruence chamber

2026-10-19. Exact finite obstruction with [independent Sol hostile review](../reviews/hat-negative-weight-congruence-chamber-hostile-sol-2026-10-19.md) PASS. Scope is the closed interval I=[-62437/17000,-62403/17000], centered at -3121/850=-249/68-1/100 with half-width 1/1000. No parameter survives in I.

The genuine infinite source, native full-size frames, intrinsic site, chirality convention and actual-support radius-10 completeness are inherited from `hat-chiral-weighted-power-gate-2026-10-19.md` and its replay. This report does not assume all source sites have nonempty power cells.

## Exact cell certification

The cyclic edge-neighbor lists throughout I are:

* 509: 480,523,507,510,516.
* 519: 508,511,513,517,516.
* 516: 480,509,510,508,519,517,518,520.

The replay intersects consecutive support lines exactly over Q(sqrt(3)). Each vertex is affine in lambda. At both endpoints it checks strict positivity of every nonincident finite-neighbor slack and every oriented edge length. Affineness certifies these inequalities throughout I, so these are genuine five-, five-, and eight-sided polygons. Every endpoint vertex has squared radius less than 365/16; convexity of squared norm gives that bound throughout I. The resulting cyclic intersections form convex polygons with the asserted supports: the strictly positive edge orientation and all halfplane checks exclude collapsed edges or omitted constraints.

All weights have spread less than 4. At distance d>=10 an omitted site's slack at any such vertex is at least d^2-2d sqrt(365/16)-4>0, since 96^2>400(365/16); this lower bound increases for d>=10. Convexity extends the slack bound to the whole finite polygon. Radius-10 disks are strictly inside the actual finite support, so no omitted infinite-source site is closer than 10. Thus these polygons equal the actual three infinite-source power cells, without any global nonemptiness assumption.

## Congruence invariants and solution

Areas are

    A509(lambda)=sqrt(3)*(401407/70144 - 11 lambda/48 - 5 lambda^2/882),
    A519(lambda)=sqrt(3)*23484642059/3199878312.

For the cyclic edges listed above, squared side lengths of 509 are

    75/64,
    3715779/300304,
    70756/18769 - 304 lambda/411 + 16 lambda^2/441,
    5929/1024 + 55 lambda/96 + 25 lambda^2/1764,
    13689/1024 - 39 lambda/32 + lambda^2/36.

The five squared side lengths of 519 are constant:

    1076269417/82498608, 55127331/108409744,
    6042978459/322094809, 32181744/4959529, 38272753/4127787.

The certificate also retains exact affine vertices and all invariants for 516. Congruence of the two pentagons requires equal areas and equality of cyclic squared-side lists under one of the ten rotations/reversals. Area equality already fails everywhere in I. Explicitly,

    (A519-A509)/sqrt(3) = 331070418797/204792211968 + 11 lambda/48 + 5 lambda^2/882.

Its degree-two Bernstein coefficients on I are the strictly positive rationals

    1361659956656491139/1599299180337600000,
    453986621928198797/533099726779200000,
    454086603725996393/533099726779200000.

The Bernstein basis is nonnegative and sums to one on the interval. Therefore A519>A509 throughout I. Since the third cell has eight sides, these witnesses give at least three congruence classes, allowing reflection, for every parameter in I. This stops only this chamber.

For a possible future restart, the *formal fixed-cycle* area quadratic has roots

    -1617/80 +/- 7 sqrt(71613048630830285211)/5333130520,

isolated exactly in (-32,-31) and (-10,-9), respectively (approximately -31.319887 and -9.105113). Its leading coefficient is positive; it is positive outside the two roots and negative between them. These are algebraic hints only: no remote cell combinatorics or cutoff is asserted at those values. The first possible formal area equality when decreasing lambda from this chamber is the root in (-10,-9). Reaching it would require a new event partition and finite exclusion proof before applying the formula there; this report makes no claim about the next actual transition.

## Replay and limits

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hat-negative-weight-congruence-chamber-2026-10-19.py

Certificate: `research/certificates/hat-negative-weight-congruence-chamber-2026-10-19.json`. All proof predicates use rational Q(sqrt(3)) signs. The imported producer also replays and deterministically rewrites its original certificate. No candidate, global palette census, universal cell-survival theorem or decoder is produced or implied.
