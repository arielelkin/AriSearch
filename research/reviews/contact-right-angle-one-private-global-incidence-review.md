# Independent audit: one-private distinct-side global reduction

Date: 2026-10-13. Verdict: VALID global incidence dichotomy and pointwise dimer reduction, with the strengthened arguments below. This is not yet a review of the remaining sixty-word host classification or an all-metric periodic-escape theorem.

Assumptions: P has native lengths (x,u,v,y,w), all five pairwise distinct, and the right-angle palette 90,112.5^4. Q is equiangular135^8 with exactly ONE private native side SLOT H. PP partial contacts and all x/y/w=2u/2v host planes are retained. The reviewed unrestricted native reduction applies without excluding host planes: Q contacts are whole; QQ degree is one or two; P species words R and S persist along subdivided sides; all flats are midpoint two-acute caps on x,y,w; acute-adjacent native P sides never host.

## Incidence ledger

In translated squares let q,p_R,p_S count anchored tiles, and D count QQ native incidences. Boundary errors below are uniform O(R). Every P90+2Q135 vertex belongs to an R P, and every R P has exactly that acute star. Counting QQ edge endpoints gives p_R=D+O(R). Counting all native P112.5 and Q135 corners gives p_R+p_S=4q-D+O(R), hence p_S=4q-2D+O(R). Let n_i be a fixed Q native multiplicity, and e_i its QQ native incidence count in the square. Whole Q contacts and distinct P values imply

    n_i*q-e_i=p_R+O(R), i=u,v,w;
    n_i*q-e_i=p_S+O(R), i=x,y.

H contributes exactly q private QQ incidences. Therefore public n_i sum to seven and public e_i sum to D-q+O(R). These identities count whole Q contacts and remain valid at all PP flats and quad-right vertices.

Uniform positive Q density follows because every P has at least two Q neighbors and each Q has at most eight P neighbors, while fixed positive areas and diameters force quadratic total tile density. Thus q>=cR^2-O(R), uniformly in square position. Extracting any frequency subsequence gives a=D/q in [1,2], b=p_S/q=4-2a, and nonnegative e_i/q. If 1<a<2, all three u/v/w multiplicities are at least two and both x/y multiplicities at least one. Their sum would be at least eight, contradicting seven. Hence only endpoints a=1 or a=2 can occur. No ergodicity, invariant measure, or individual positive P-mode frequency was assumed.

## Endpoint a=2 is pointwise all-R and needs no defect limit

At a=2, the public counts must be either: u/v/w=(3,2,2), x=y=0; or u/v/w=(2,2,2) and precisely one x/y slot. In either case Q lacks at least one of the distinct values x,y. Every S P requires Q on BOTH native x and y sides. Thus no S can occur. This is a direct shape-alphabet argument; disjoint R/S native PP palettes alone would not exclude subdivided R/S contacts on host planes.

All-R excludes quad-right and flat vertices because their P90 occurrences have P on acute legs and hence are S. The field is intrinsically ETE even when its metric lies on a host plane. H is the unique native slot of its value; a full H contact uses that slot on both Q copies. The mirrored mate gives equal acute legs, impossible; the half-turn requires distinct u/v end tags. A degree-one Q then has word (H,u,w,w,w,w,w,v), up to swapping u/v; vertical closure forces u=v. Thus every Q has degree two pointwise. The earlier one-private generic mask proof now applies with its no-host-plane assumption replaced by already proved all-R/ETE. Its sole second QQ slot is public, and fixed-mask closure forces its length equal H, contradicting privacy. This transfer does not require a separate sparse-defect compactness argument.

## Endpoint a=1 gives pointwise dimers without a limit

At a=1, the seven public counts are forced to be n_u=n_v=n_w=1 and n_x=n_y=2. H is QQ at every Q. Its two neighboring native slots must have lengths u or v, because their P90 endpoint guest contacts Q along an acute leg. Since u and v each occur once, H is flanked by those two different values, at slots1 and7 after rooting H at0. Any second QQ slot must be separated from H by distance3 or4. Its two flanking slots are distinct from1 and7 and must again carry u/v. No such native occurrences remain. Thus every Q has degree one pointwise. This depends only on whole Q contacts and the fixed native multiset, and retains all PP partial contacts.

No frequency clean limit, atomic refinement, contact-persistence lemma, or deletion of sparse public QQ edges is needed for the theorem. The incidence argument merely obtains a subsequence endpoint and thereby fixes the exact integer multiplicities of the original shapes. The rooted Q word then belongs intrinsically to the sixty-word domain. Host-specific word forcing and the exact positive carrier/negative ray are separately reviewed below/in the native bridge review.

## Ancillary contact-limit check, unnecessary for this reduction

The following independently checked refinement remains useful for other sparse-defect arguments, but is NOT a dependency of the pointwise dimer theorem.

Define D_lengths={x,y,w} intersect {2u,2v}. Insert a marked midpoint on every native P or Q side whose length belongs to D_lengths. Do NOT indiscriminately cut all sides of length2u/2v: an acute leg u=2v could otherwise introduce unwanted recursive quarter cuts. Distinctness ensures u and v are not in D_lengths. Every actual T is a midpoint cap on one of these host sides. Whole native contacts receive identical midpoint marks on both sides; split host contacts become whole atomic contacts with uncut u/v guest edges. The resulting finite list of fixed marked polygons therefore forms an ETE cell complex. Artificial midpoint angles180 are permitted and pose no problem.

Choose rho>0 below every atomic edge length and every marked-corner distance to a nonincident boundary segment. At each marked vertex the incident polygons fill a rho disk by their fixed corner wedges, including180 wedges. A second marked vertex cannot lie in a wedge interior, and cannot lie along a wedge ray because atomic ETE edges are whole and exceed rho. Thus marked vertices are uniformly separated. This gives actual incidence persistence under indexed placement convergence: neither native stars nor marked midpoint caps can merge or produce an untracked intervening vertex.

Translate growing clean disks and extract fixed marked-polygon placements. Coverage and nonoverlap persist; the uniformly separated marked stars preserve whole atomic contacts and original native identities. The limit has no public QQ contact, while its H contacts are whole and survive. It is an admitted tiling by the original polygons, with PP flats retained and Q degree one everywhere. This proves the required actual dimer reduction without falsely claiming the limit is native ETE.

The refinement argument supplies an optional incidence-preserving compactness tool. The theorem above uses the direct two-flank pigeonhole obstruction instead. No conclusion about all admitted original tilings being periodic is made.
