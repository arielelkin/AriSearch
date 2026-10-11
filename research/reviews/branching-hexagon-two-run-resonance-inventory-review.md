# Fresh root review: binary two-run resonances and omission exclusions

**Verdict: VALID as the stated necessary inventory, capacity bounds and imported monohedral exclusion.**

Reviewed [the actual lemma](../lemmas/branching-hexagon-two-run-resonance-inventory.md). The [independent checker](verify_two_run_resonance_inventory_independent.py) derives all four repeated-angle homogeneous equations on each arc, their six pairwise intersections, all actual A-Aq endpoint patterns, the sixteen rational capacity bounds and all twelve native length-word exclusions without author imports.

A homogeneous trivalent star has only Bpp or only Bqq corners, because each A corner is mixed. Thus exactly four repeated-angle equations exist per arc. Pairwise solving any two of their independent rows gives only(120,120); on a noncentral line just one multiset can occur. Every whole Aq has one H and one L endpoint, so the A-Aq endpoint fillers must either both be120 or be the ordered opposite pair120−2delta,120+2delta. The paired locus has no homogeneous pp multiset: the nonzero odd coefficient of2delta excludes every three-corner sum. These are necessary angle conditions, not geometry sufficiency.

The incidence identity NB−NA=Yp+Yq+O(R) is correct with both species counts free. A mixed star has two mixed and one homogeneous corner, while a homogeneous star has three homogeneous corners. Bounding each native corner's supply by NB+O(R) gives1/3 for a pure3-copy line and1/2 for a mixed2+1 line; a center arc has2NB corners giving2/3. All16 pairwise upper bounds are valid, and none is asserted attainable. Boundaries are O(R) for fixed positive-area bounded-diameter shapes. No equal-species constraint is inserted on resonances.

The root separately opened the primary source [Zhu–Wang–Yan, arXiv2508.01404v2](https://arxiv.org/html/2508.01404v2), Introduction's H1/H2/H3 conditions and Main Theorem. The paper's complete classification applies to compact convex hexagons with unrestricted contacts. Both H1/H2 require the specified opposite equality; all opposite pairs in pppqqq are unequal when p!=q. H3 requires three adjacent equal pairs, and every native cyclic/reflected indexing has a p/q crossing among those pairs. The independent checker verifies all12 indexings. The imported complete theorem, already used in reviewed repository work, is necessary to deduce B cannot tile monohedrally. No new elementary completeness result is claimed.

A-only tiling is excluded by the reviewed trivalent edge-to-edge admitted-limit theorem: three binary ray labels have zero or two changes, whereas three A corners would need three mixed changes. Both nonmonotiles then meet the hypotheses of the reviewed uniform-density theorem. This supplies positive lower densities in admitted tilings without specifying frequency limits or a ratio.

Completed replay:

    conda run --no-capture-output -n arisearch python research/reviews/verify_two_run_resonance_inventory_independent.py

All independent finite checks pass. No substantive defect was found. No tiling on any exceptional locus is classified by this inventory; the complete no-homogeneous reduction has a separate review, and all homogeneous resonance loci still require geometric work.
