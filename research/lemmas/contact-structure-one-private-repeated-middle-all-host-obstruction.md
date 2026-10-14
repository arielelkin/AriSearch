# One-private repeated middle/bevel palettes are untileable, including all hosts

Date:2026-10-13. Adversarially reviewed VALID, including all host planes.
Fresh complete audit: `research/reviews/contact-structure-one-private-repeated-middle-all-host-hostile-review.md`.

Let P have right-palette indexed lengths(x,u,v,y,w), angles112.5,112.5,90,112.5,112.5, with w=x and the four values x,y,u,v pairwise distinct. Let Q have eight135angles and exactly one native side slot whose length occurs nowhere among Pside lengths. Then no unrestricted plane tiling by the original P,Qexists. All host doubling planes, reflections, partial contacts and initial prototile omission are allowed. Reflection gives the w=y dual. This is a new repeated-side family obstruction, not an unrestricted all-pairs result.

## Uniform actual-contact counts, without a frequency assumption

The reviewed native reduction applies independently of length aliases: all Qcontacts are whole; P has wordsR orS; Qhas at most two QQslots; every flat guest is a P90corner; only both-obtuse Pside hosts are possible. Rhas PQside lengthsu,v,w=x and PPbevelsx,y. Shas PQbevelsx,y and PPside lengthsu,v,w=x. The four distinct values make these classifications unambiguous at each native Pslot even though x is repeated.

Write H for the unique private Qslot. It must be QQ, so every Qhas degree one or two. Let q,p,p_R,p_S count centered tiles in any translated square of side2R. Let e count native extra QQincidences beyond each Qs mandatory Hslot, anchored at Qcenters; exactly0<=e<=q. Let f_i count those incidences of valuei in{i=u,v,x,y}. Thus sum f_i=e exactly. Let n_i be the fixed number of native Qslots of valuei, so sum n_i=7. Whole contact incidence errors are uniformO(R) by positive tile areas, bounded diameters and boundary-strip packing.

Each R90star is PQQ and conversely every PQQstar is R. The number of QQnative incidences equals the number of their endpoint PQQstars, up to uniform boundary errors, so

    p_R=q+e+O(R).

The native angular ledger gives p+p_R=4q+O(R). Therefore

    p=3q-e+O(R), p_S=2q-2e+O(R).

Native PQcontacts of each value give

    n_u*q-f_u=p_R+O(R),
    n_v*q-f_v=p_R+O(R),
    n_y*q-f_y=p_S+O(R),
    n_x*q-f_x=p_R+p_S+O(R)=p+O(R).

The last identity counts BOTH Rmiddlesw=x and Sbevelsx. Uniform quadraticq is available: every Phas at least two whole Qneighbors, so p<=4q+O(R); plane coverage with positive fixed areas gives p+q>=cR^2-O(R). Thus q>=cprime*R^2-O(R), uniformly in square center.

Since f_x<=e and p=3q-e+O(R), n_x<=3. Since f_x>=0 and p>=2q+O(R), n_x>=2. Hence n_x is2or3. If n_x=2, f_x=e-q+O(R)>=0 forces q-e=O(R). If n_x=3, f_x=e+O(R), so f_u+f_v+f_y=O(R). Each is nonnegative; in particular f_u=O(R), and the uidentity gives

    e=(n_u-1)q+O(R).

As0<=e<=q and n_u is an integer, n_u is1or2. Thus either e=O(R), or q-e=O(R), uniformly. This is a shape-dependent integer dichotomy, not an assumed infinite frequency.

In the e=O(R) branch, n_x=3 and the same identities force n_u=n_v=1,n_y=2. Qhas native multiset{H,u,v,x,x,x,y,y}. A unique Hside can only have its midpoint-halfturn mate: support-line reflection would expose equal outgoing lengths at the P90seam endpoint, contradicting u!=v. The Hflanks are therefore u,v in opposite order. The other five sides are binaryx/y. The independently reviewed contact-structure-one-private-aliased-binary-middle-closure-obstruction.md proves that shape word cannot close when x!=y: Qvertical closure puts c=cos(pi/8) inQ(sqrt2), while Norm(c^2)=1/8 is not a rational square. This branch is impossible without a limiting argument or an extra-middle-R assumption.

## The high-QQ branch has a clean allR ETE limit

Now q-e=O(R). The ledger gives p=2q+O(R). Let z count four-P90stars and t count flat-host plus two-P90stars. Native corner balance gives

    p=2q+2z+t+O(R), hence2z+t=O(R).

Assign native corner weights P112.5→1,P90→4,Q135→-2; side-interior hosts contribute zero. The complete angle palette has scores0forPPQ,0forPQQ,16forquadP90,8forflatcaps. Thus positive-score vertices are precisely the uniformly linearly bounded z/t defects. Prototile totals are P8,Q-16; no theorem requiring individually zero prototile scores is invoked.

Choose growing disks free of positive-score vertices by a separated-grid count: quadratically many disjoint disks in a sufficiently large window cannot all meetO(R) defects. Translate their centers to0and take a diagonal indexed-isometry placement limit, retaining every native corner occurrence, tile species and symmetry-resolving label. Fixed diameters/positive areas bound tile counts in compact windows; bounded translation parts and compact orthogonal parts give subsequences. Interior disjointness and coverage persist, producing a legal tiling of the same fixed shapes.

For each limiting native vertexv, choose a small disk containing no other limiting native-corner position. Late approximants have exactly the complete multiset of native corner OCCURRENCES converging tovinside that disk; all other occurrences stay outside, and the local tile bound excludes untracked tiles. Group approximating occurrences by their geometric positions. Each group is an ENTIRE zero-score source star, including every indexed native corner there; any flat host contributes zero. Summing those groups and retaining all occurrences shows the limiting score atv is zero even if several source zero stars coalesce. The only zero-score stars in this fixed angle palette are PPQ/PQQ. Thus the limit is trivalent ETE and every P90isPQQ, so every P is R. This explicitly reuses the additive cluster proof of contact-structure-two-private-octagon-clean-r-limit.md after replacing its two-private count premise by the direct2z+t=O(R) derivation above. It does not invoke that lemmas statement outside its scope.

## Conditional allR unique-H closure contradiction

The clean limit still has the original single private Hslot. Its Hmate is the midpoint halfturn as above, forcing opposite outgoing acute tagsu,v. A degree-one Qwould have word(H,u,w,w,w,w,w,v), whose vertical closure is(u-v)/sqrt2=0, impossible. Hence every Qhas degree two.

The second QQslot is atj=3,4or5. It is fixed natively: the compulsory middle-w public slots are5,6forj3;2,6forj4;2,3forj5. Since w=x is distinct from bothu,v, no fixed Qshape can support two such masks. The clean allR degree-two ledger gives p=2q+O(R), and each Pcontributes one PQside of each tagged valueu,v,w. Therefore each Qhas exactly two public slots of each tag. This uses public tags, not the total native multiplicities including QQslots.

Forj3the public short gap has acute tagsa,b. Mixedtags would expose PPbevelsx,ywhich cannot match whole sincex!=y; hencea=b. The two-each count forces the other two acute tags equal the other value. The word is(H,u,u,J,v,w,w,v), orswapped. Exact closure givesH=J. Reversal treatsj5. Forj4the word is(H,a,w,b,J,c,w,d), with Hforcinga!=dand two occurrences of each acute tag. Vertical closure forcesb=d,c=a; horizontal closure thenH=J.

But Hoccurs on exactly one private native slot, while every other slot has one of the four Pvalues; J!=H. Contradiction. These are the conditional steps of contact-right-angle-one-private-generic-obstruction.md, reproved here with their needed hypotheses: publicu/v/w pairwise distinct, PPbevelsx!=y, allR ETE, unique privateH. Its original five-distinct/nodoubling hypotheses are NOT substituted, since w=x and hosts were allowed initially.

Both uniform count branches are impossible. Therefore no original unrestricted tiling exists in the stated repeated-side one-private family. There is no proposed finite patch, numerical metric domain or candidate-radius search in this proof.
