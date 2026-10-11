**Fresh independent status: VALID; see the corresponding root review under research/reviews.**

# Double-residual ten-face periodic carrier reproducibility

Status: completed exact high-half sufficient cone; fresh independent review pending.
Source orbit6 flat239 actual-order chamber0 full-residual-color model. Scale10
copies variant0 six times,1 twice,9 twice (8P2Q),58 formal native darts.
All equal-color perfectmatchings and both endpoint maps are admitted,
same-face pairs included. Exact360 corner-component pruning and connected
final graph yield first candidate after102808 nodes,1 completed pairing.
No exhaustive negative implication, seed, numeric solver or cutoff.

Separate model-free Euclidean development checks original native geometry,
19 true circular360 links,10 original face states, both endpoints/CCW direction
and all58 integer period shifts. Exact QQ coefficient rank2/Hermite lattice
and polynomial shoelace identity supply periods andarea=covol. Full sufficient
metric domain a>0,b>=a/sqrt3 has actual positive subdivisions (equalitymerger
explicit); lower positivity range sqrt3*a/4<b<a/sqrt3 is not covered.

Replay:

    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-mixed-quotient-native-search.py --pattern orbit6 --flat 239 --scale 10 --source research/certificates/partial-contact-cairo-remaining-eighteen-residual-colors.json --output research/certificates/partial-contact-cairo-mixed-quotient-orbit6-flat239-ten-faces.json
    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-mixed-quotient-native-development.py --input research/certificates/partial-contact-cairo-mixed-quotient-orbit6-flat239-ten-faces.json --output research/certificates/partial-contact-cairo-mixed-quotient-orbit6-flat239-development.json

Low-half bounded failures: same producer --chamber7 --scale10, output
partial-contact-cairo-mixed-quotient-orbit6-flat239-complement-ten-faces.json;
repeat --allow-disconnected outputs*-complement-components.json. Each selects
variants0*4,3*2,4*2,9*2, ten faces/58 darts, exhausts20910 nodes with189
completedmatchings andno360gluing. Scope onlythatcopiedvariantmultiset,
not low-half untileability. Alternativefrequencies/largerquotients remainopen.

Environment SageMath10.9/Python3.12.13. Deterministic exact quadratic-field,
polynomial, vertex-cycle and integer lattice arithmetic; no numerical
inference or frequency-to-surface conclusion. High-half construction is
complete; fresh independent review pending, low-half remains unresolved.
