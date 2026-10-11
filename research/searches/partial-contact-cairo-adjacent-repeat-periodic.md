# Adjacent-repeat periodic witness: proposal and exact replay record

Date:2026-10-10. Arithmetic:Q(sqrt3) for every geometric comparison and the
retained witness. Scope:a=b=1,e=2 Cairo pentagon, not arbitrary shapes.

An exploratory SciPy MILP proposal used S(1) cluster centers on sqrt3 times
the integer grid, with two orientations0 and90 degrees. Candidate rectangular
period cells had integers3<=M<=8,M<=N<=9,M*N divisible by3, sorted by cell
area. Each cell had up to2MN placement states; one orientation0 cluster at
origin was fixed. Pair conflicts were precomputed by exact convex separating
axes on the four constituent pentagons, with integer coordinate differences
-3..3 in each dimension. Farther coordinate differences cannot overlap
because the whole macro extents are at most3sqrt3. Each MILP imposed exact
binary placement and pair-conflict constraints and required MN/3 clusters
(the area budget). The solver was numerical and had a10-second per-cell
time limit. No randomization was used. No numerical infeasibility is a
mathematical obstruction or used elsewhere in this proof.

Eleven cells were attempted in order:3x3,3x4,3x5,3x6,3x7,3x8,4x6,3x9,5x6,
4x9,6x6. The6x6 cell supplied twelve clusters:orientation0 at(i,-i mod6),
orientation90 at(i,3-i mod6), i=0..5. This proposal reduces exactly to the
lattice(w,-w),(3w,3w), with two macrofaces0 andquarter-turn+(0,3w). Hence
the retained motif has eight original P pentagons per lattice cell.

The definitive producer performs no MILP and imports no proposal state.
It reconstructs the native P, the exact P/Q reflection, the eight faces and
periods directly. Exact inverse-lattice bounding boxes enumerate ALL84
potentially meeting ordered face/translate pairs, max absolute index2,
and exact edge-normal projection comparisons exclude interior overlap.
Every face has area9/4 and covolume18, proving coverage as in the lemma.
This is a completed positive witness; no failure-to-find inference is made.

Exact commands:

    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-adjacent-repeat-periodic.py
    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-adjacent-repeat-periodic.py --output research/certificates/partial-contact-cairo-adjacent-repeat-periodic.json

Result:PASS8 exactfaces;area18;84 complete comparisons;max index2. Certificate
retains every face vertex, both periods, native side lengths and field.
Independent hostile review is required before promoting the new witness.
