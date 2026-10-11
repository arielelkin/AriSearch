# Exact two-run hexagon angle and frequency gate

**Status:** completed finite exact computation; independent audit pending. Fifty-two necessary-frequency witnesses are retained. These are not infinite tilings, periodic quotients, or aperiodicity candidates with an existence proof.

## Question and finite domain

A has edge lengths (p,1,p,1,p,1) and edge directions (0,75,120,195,240,315) degrees. Thus delta=15 and its alternating angles are135,105. B has side word (p,p,p,1,1,1). Enumerate all81 ordered tuples (beta1,beta2,beta4,beta5) in {90,120,150}^4. These are all values that a homogeneous B corner may need at a two-A star. The search asks which exact closed convex B geometries with p!=1 admit nonnegative native-corner frequencies with both species positive.

Set z=exp(i*pi/12), the primitive24th root with real part between96/100 and97/100 and imaginary part between25/100 and26/100. It satisfies z^8-z^4+1=0. For tuple (a,b,c,d), let

    P=(1,z^((180-a)/15),z^((360-a-b)/15)),
    Q=(1,z^((180-c)/15),z^((360-c-d)/15)),
    Psum=sum(P), Qsum=sum(Q),
    p=sqrt((Qsum*conjugate(Qsum))/(Psum*conjugate(Psum)))>0,
    R=-p*Psum/Qsum.

The B directed edges are p*P followed by R*Q. Their exact sum is zero and R is a unit complex number. The first directed edge fixes the native orientation; no symmetry reduction is used. Exact support half-plane inequalities against every nonincident vertex check strict convexity. Equal p=1 cases are outside the distinct-length question.

For a unit incoming/outgoing directed-edge ratio w, the unit internal-angle complex number is -conjugate(w). A corner triple sums360 exactly when the product of its three unit internal-angle numbers equals1, since each strict convex angle lies in (0,180). Candidate triples use combinations with replacement of the12 native corners, retaining repeated slots from distinct occurrences. The allowed binary length-star multiplicities are (3pp), (pp,pq,pq), (qq,pq,pq), or (3qq). No orientation or endpoint-pairing condition is added at this necessary gate.

For each retained legal triple t use a nonnegative rational variable v_t and species variables f_A,f_B>0 with f_A+f_B=1. Every native corner i has the equation sum_t multiplicity_i(t)*v_t=f_species(i). These equations are necessary only. They omit edge matching, pair endpoint consistency, overlap and global extension.

## Complete result and retained evidence

All81 ordered tuples completed:

* 15 have p=1 and are excluded by the exact distinctness condition;
* 14 are infeasible; in every one, B native corners0 and3 appear in no legal triple, providing a direct exact infeasibility witness;
* 52 have retained rational positive-species corner-frequency solutions.

All66 distinct-length reconstructed geometries pass strict convexity. There is no timeout or floating-point proof decision.

Producer: [exact search](branching-hexagon-new-two-run-angle-search.py).
Retained finite record: [certificate](../certificates/branching-hexagon-new-two-run-angle-search.json).
Replay without rewriting the certificate:

    conda run --no-capture-output -n arisearch python research/searches/branching-hexagon-new-two-run-angle-search.py

The producer uses Sage QQbar/AA exact algebraic arithmetic and Z3 rational linear arithmetic. Versions: Python3.12.13, Sage10.9, Z3 4.16.0. The deterministic ordered domain has no random seed or symmetry reduction. No timeout is configured; the original complete run finished without resource exhaustion. A consequential witness can be verified from rational corner marginals without trusting the solver, and each infeasible case has its explicit absent-corner obstruction. The certificate records exact tuple/formula data and p's minimal polynomial; the positive root is fixed by the construction, not by the minimal polynomial alone.

## A small exact surviving geometry

Tuple (120,120,90,150) gives

    q=1, p=cos15=(sqrt6+sqrt2)/4,
    A directions: 0,75,120,195,240,315;
    B directions: 0,60,120,165,255,285;
    B angles: 105,120,120,135,90,150.

The geometry is exact over Q(zeta24). A's and B's opposite side pairs all have different lengths, and B's three p then three q word cannot be partitioned cyclically into three equal adjacent pairs. Hence the recorded Reinhardt monohedral families supply no monohedral escape for either tile; A also directly has no trivalent monohedral star by its all-pq corners. This monohedral exclusion uses the recorded imported classification, not merely a failure to find a single-tile patch. The [primary source](https://arxiv.org/html/2508.01404v2) was rechecked on2026-10-10: H1 and H2 each require an equal opposite side pair, while H3 requires a cyclic partition into three equal adjacent side pairs (Introduction, displayed H1/H2/H3 conditions).

An explicit symmetric frequency certificate has f_A=f_B=1/2 and12 vertex types of frequency1/6 each:

* (B4,A0,A2), (B4,A2,A4), (B4,A4,A0);
* (B5,A1,A3), (B5,A3,A5), (B5,A5,A1);
* (B1,B0,A0), (B1,B0,A2), (B1,B0,A4);
* (B2,B3,A1), (B2,B3,A3), (B2,B3,A5).

Each native corner marginal equals1/2; every triple is length-legal and has angle sum360. The producer's Z3 certificate may choose a different feasible frequency vector, which is retained separately.

The live next obligation is geometric: pair full native edges at both endpoints, obtain an admitted whole-plane tiling, and establish either a complete periodic escape or actual global aperiodic forcing. No such tiling is established here. Frequency feasibility alone cannot decide this obligation; bounded failure to find a periodic quotient would not be sufficient either.
