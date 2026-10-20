# Sugimoto concave pair: convex exchange entry gate

Status: blocked at the missing exchange topology; no candidate pair and no aperiodicity claim. Checked 2026-10-19 against arXiv:2609.09603v1, HTML, TeX source archive, and Figures 1.4 and 2.1. No finite cluster search was performed. [Sol primary-source review](../reviews/sugimoto-concave-pair-convex-exchange-sol-review-2026-10-19.md): pass with wording clarifications incorporated.

Primary links: [paper](https://arxiv.org/html/2609.09603v1), [source archive](https://arxiv.org/src/2609.09603v1), [Figure 2.1](https://arxiv.org/html/2609.09603v1/Fig02-01_AMT.png).

## Source facts and first blocker

Section 2 gives actual unmarked plane tilings by each concave pair AH/BH and AT/BT, using the hat/turtle H7/H8 substitution. Each concave tile is a union of respectively eight or ten congruent Type-5 pentagons. Section 5.3 leaves unrestricted aperiodicity of these two pairs unknown. Sections 4–5 show reflected periodic escapes for other combinations, including AH/AT and BH/BT. These are not counterexamples to AH/BH or AT/BT.

The archive contains one TeX file, 57 PNG figures, and `00README.json`; it contains no coordinate or tiling-generator code. Figure 2.1 shows the pentagon-union incidence and correspondence, but no cross-boundary exchange into two convex classes. The local Mystic replacement in Section 4 reflects a nonconvex region while preserving the surrounding cluster boundary and changing its internal hat/turtle tiling; it is not a convexification rule.

**First missing datum:** a specified finite incidence topology, with exact cut endpoints and a globally compatible choice of seam neighborhoods, whose replacement cells form exactly two convex congruence classes. Neither a universal decoder nor aperiodicity needs to be attempted before this datum exists. There is no source-specified exchange topology to test here. This observation is restricted to the examined source package, not a nonexistence theorem for exchanges.

## Exact reusable carrier, and why it is not a candidate

The native pentagon in Figure 1.4 can be normalized, in boundary order E,A,B,C,D, as

    (0,0), (0,sqrt(3)/3), (-1/2,sqrt(3)/2),
    (-3/2,sqrt(3)/2), (-1,0).

Successive turns are 90, 60, 30, 120, 60 degrees. Hence its interior angles at E,A,B,C,D are respectively 90,120,150,60,120 degrees, and its lengths satisfy EA=AB=1/sqrt(3), BC=CD=DE=1. This exactly reproduces the figure without estimating pixels.

Splitting the concave unions back into these native cells yields one convex class, a periodic Type-5 carrier. Counting the reflected pentagon as a second class is invalid under the repository congruence convention. Adding any second shape while retaining this pentagon also fails, because the pentagon-only periodic tiling remains admitted. Thus the one exact convexification directly supplied by the source is eliminated immediately.

## Gates for any genuinely new exchange

Any output containing a triangle, quadrilateral, or centrally symmetric convex hexagon is immediately eliminated by that member's periodic monohedral tiling. A native Type-5 pentagon output is eliminated as above. A proposed rule must also be tested on reflected source configurations: if a periodic legal source is covered by a translation-equivariant finite-radius exchange with no added labels, translating by its periods translates every output cell, so the output is periodic. A rule whose applicability requires choosing a globally aperiodic phase does not itself provide shape-only forcing.

Even an exact two-class plane repartition would prove only existence. The remaining intrinsic-decoder lemma must assert that every unrestricted output tiling, including reflections, partial-edge contacts, omissions, and unintended assemblies, reconstructs an appropriate nonperiodic source in a translation-equivariant manner. The paper's unknown pair aperiodicity cannot fill that lemma. One could instead decode directly to a hat hierarchy, but that would require a new proof.

Stop condition: no blind enlargement of pentagon clusters. Resume only with an explicit new seam exchange or dual-cell incidence rule and exact endpoint formulas. No discovery-log edit was made by this worker.
