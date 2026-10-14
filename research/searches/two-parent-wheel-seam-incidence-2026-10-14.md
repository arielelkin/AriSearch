# One two-parent wheel/seam incidence design: exact failure

Date: 2026-10-14. Status: **falsified for the declared incidence** by a native-corner count; [independent hostile review](../reviews/two-parent-wheel-seam-independent-hostile-review-2026-10-14.md) confirms the scoped obstruction. This is one bounded design cycle, not a classification of nonconvex-parent substitutions.

## Target and notation

The atoms P,Q are compact genuine convex pentagons, and the parents H,K are intended to be simple nonconvex polygons. The base rules are H=2P+Q, K=P+2Q. The expansion is a common similarity of factor φ=(1+√5)/2 with φH=2H+K and φK=H+K. These count rules require area(P)/area(Q)=3φ+1, area(H)/area(K)=φ. The corresponding one-level atomic counts are φH=5P+4Q and φK=3P+3Q. None of these area equations proves geometric realization.

All boundary words below are counterclockwise. For an oriented pentagon T, let native edges t0,...,t4 run from vertices t0^v,...,t4^v in cyclic order, with t4 ending at t0^v. Edge symbols with different copy subscripts are distinct occurrences, even when their lengths are constrained equal. A `rev` seam pairs the indicated edges with reversed boundary direction. Native corners persist at the internal joints of every listed exposed arc; no subdivision occurs. A seam endpoint may be flat in the union unless explicitly required genuine.

## Base H and K: three-atom central wheels

For W(A,B,C), use three counterclockwise pentagon copies around one internal point z. Identify their native vertices a0^v=b0^v=c0^v=z and pair seams b0 with rev(a4), c0 with rev(b4), a0 with rev(c4). The outer seam endpoints in boundary order are a4^v=b1^v, b4^v=c1^v, c4^v=a1^v. The counterclockwise exposed boundary word is

    W(A,B,C) = (a1 a2 a3 | b1 b2 b3 | c1 c2 c3).

The bars mark precisely the three far seam endpoints. Their interior angles in the union are angle_A(a4^v)+angle_B(b1^v), angle_B(b4^v)+angle_C(c1^v), and angle_C(c4^v)+angle_A(a1^v). Central angles sum to 2π. All three radial seam lengths must agree in the cyclic pairing above. We stipulate that each far endpoint is a genuine parent corner, with at least one reflex endpoint, so W is a simple nonconvex nine-gon if the resulting sectors do not overlap. This last geometric embedding is an unproved feasibility condition; the fatal inflation count below does not use it.

Set H=W(P1,P2,Q1) and K=W(P3,Q2,Q3), retaining the displayed orientation and copy order. Their boundary words are

    h0...h8=(p11 p12 p13 | p21 p22 p23 | q11 q12 q13),
    k0...k8=(p31 p32 p33 | q21 q22 q23 | q31 q32 q33).

Here p_ij denotes edge j of P copy i (likewise q_ij), and the symbols h_i,k_i denote the actual exposed native edge occurrences in that order. The three bars in each row are genuine boundary corners. The six within-arc corners are genuine because they are native convex-pentagon corners. At the first boundary vertex, between the final and first edges, H and K both have the same corner expression angle_Q(q4^v)+angle_P(p1^v). At the other two bars, H has P/P then P/Q correlations, while K has P/Q then Q/Q correlations. Thus all far-endpoint correlations are fixed by the copy order. The central base equations are 2α_P+α_Q=2π and α_P+2α_Q=2π, where α_T is the angle at t0^v. Hence α_P=α_Q=2π/3. The radial length equations across both wheels force p0=p4=q0=q4. These are necessary conditions, not an exact coordinate solution.

## Inflation of H: three-parent central wheel

For each parent copy, choose its boundary vertex v0 between edge 8 and edge 0 as the central corner, and reuse the W seam convention with nine-sided words. With macro copies H1,H2,K1, pair h20 with rev(h18), k10 with rev(h28), and h10 with rev(k18). Their central vertices coincide at Z_H. Their three far seam endpoints are h18^v=h21^v, h28^v=k11^v, and k18^v=h11^v, in cyclic order. The oriented exposed boundary is

    B_H=(h11 h12 h13 h14 h15 h16 h17 | h21 h22 h23 h24 h25 h26 h27 | k11 k12 k13 k14 k15 k16 k17).

There are 21 exposed native macro-edge occurrences. The far angles are θ(H1,v8)+θ(H2,v1), θ(H2,v8)+θ(K1,v1), and θ(K1,v8)+θ(H1,v1). The central equation is 2θ(H,v0)+θ(K,v0)=2π. Since the base definitions make both v0 angles the same, this specializes to θ(H,v0)=θ(K,v0)=2π/3. Seam length equations require |h0|=|h8|=|k0|=|k8|. The intended identification is B_H with the oriented boundary of φH, up to one plane isometry and cyclic shift or reversal.

## Inflation of K: two-parent whole-edge seam

Take H3 and K2. Pair h30 with rev(k28), identifying h30^v=k20^v and h31^v=k28^v. The exposed counterclockwise boundary is

    B_K=(h31 h32 h33 h34 h35 h36 h37 h38 | k20 k21 k22 k23 k24 k25 k26 k27).

The first bar lies at h30^v=k20^v, with union angle θ(H3,v0)+θ(K2,v0). The closing joint lies at h31^v=k28^v, with union angle θ(H3,v1)+θ(K2,v8). These are the complete far-endpoint correlations. Seam length requires |h0|=|k8|. The intended identification is B_K with the oriented boundary of φK, up to one plane isometry and cyclic shift or reversal.

This specifies every positive-length seam and every exposed boundary edge for all four dissections. It imposes whole-native-edge contacts and excludes T contacts inside the declared template; no claim is made about what arbitrary P/Q tilings can do.

## Fatal boundary-corner invariant

A simple polygon similar to H or K has exactly nine genuine corners. In B_H, each macro-child contributes the interior six vertices of its exposed seven-edge arc. Those vertices remain on the union boundary with their original nonstraight child angles, whether convex or reflex. Hence B_H has at least 3×6=18 genuine corners. The three far endpoints can add corners or flatten, but cannot remove these 18. Thus B_H cannot be the boundary of φH.

In B_K, each macro-child contributes the interior seven vertices of its exposed eight-edge arc. These 14 genuine corners persist on the union boundary regardless of the two far endpoint angle sums. Thus B_K cannot be the boundary of φK. This is an incidence contradiction; metric equations, area, overlap and exact placement cannot repair it. It remains true if one or all **inflation** far endpoints are flat.

The contradiction is robust even if the declaration that all three **base** far endpoints are genuine is relaxed. A base three-pentagon wheel has nine exposed atomic edge occurrences. Only its three joins can flatten, so each simple parent has at least six genuine sides: write p_H,p_K≥6. Keep the same macro topology with one whole genuine parent edge per radial seam and no other positive-length contacts. The H,H,K wheel removes six parent-edge occurrences, and at most its three far joins can flatten. Therefore its union has at least 2p_H+p_K−9 genuine sides. Similarity to H would require p_H+p_K≤9, contrary to p_H+p_K≥12. The H,K one-edge join removes two parent-edge occurrences and has at most two flattenable far joins. Its union has at least p_H+p_K−4 genuine sides. Similarity to K would require p_H≤4, contrary to p_H≥6. If a selected radial segment ceases to be a whole genuine parent side after a base flat merger, the stipulated macro whole-edge rule is already undefined there; it does not rescue this template. These inequalities use only the declared seam topology and no metric hypotheses.

## Scope and recognition gate

The obstruction applies exactly to the displayed base three-atom wheels, the displayed macro three-parent wheel, and the displayed macro one-edge join. It does not exclude inflation rules with partial contacts, several seams per pair, internal macro children, or a different base boundary. The six-child convex-parent wheel theorem does not apply because H,K are nonconvex parents, and the all-hexagon perimeter theorem does not apply because the atoms are pentagons. The positive-conjugate small-substitution obstruction addresses convex pentagon parents, not these H,K. No structural recognition map for arbitrary atomic P/Q tilings has been supplied, and no repeatable parent interface survives this template. Even a geometrically valid four-rule template would still need exact expanding plane extension and a universal shape-only decoder.
