# Paired-repeat Cairo: exact obstruction algebra and carrier replay

Date:2026-10-10. Fixed native angle family90,120,90,120,120. Family scope
arms(a,b,b,a),e=sqrt3*b-a>0. The obstruction outside a=b or b=sqrt3*a is a
direct equality-bank/contact proof, not a solver classification.

The normalized retained shape(1,sqrt3,sqrt3,1,2) was constructed by rotating
three pentagons around their isolated120 corner. Their boundary is a regular
hexagon of side2, yielding periods(3,sqrt3),(0,2sqrt3). No search, random
seed, optimization or deadline was used to propose this carrier.

The producer uses exact Q(sqrt3) arithmetic. It verifies closure identities,
all15 native support determinants and5 edge lengths, all three rotations,
hexagon containment, area2sqrt3 per face, and area/covolume6sqrt3. Exact
inverse-lattice bounding boxes enumerate all28 potentially meeting ordered
original-face/translate pairs, maximum absolute index1; native separating
axes exclude all interior overlaps. Area plus local closedness proves
coverage of the full plane. No bounded failure-to-find claim is made.

    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-paired-repeat-periodic.py
    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-paired-repeat-periodic.py --output research/certificates/partial-contact-cairo-paired-repeat-periodic.json

PASS3 exact faces, regularhexagon,28 complete comparisons. The certificate
retains the primitive field, side lengths, every face vertex and periods.
Fresh independent review is required before promoting the obstruction or
its resulting classification.
