# Danzer nine / Grünbaum–Shephard six convex-pentagon source boundary

Date: 2026-10-13. Status: primary lead confirmed; exact source and universal
forcing/frequency theorem not recovered. No construction or exclusion theorem.

The [primary book](https://archive.org/details/isbn_0716711931), Grünbaum and
Shephard, *Tilings and Patterns* (1987), Figure10.3.29 and Exercise4 near printed
page549, is identified by Džuklevski’s
[primary Section3.2](https://arxiv.org/html/2507.20867v1). Public Internet Archive
full-text search snippets confirm the following separate families:

* Figure10.3.29(a): nine convex pentagons, including a regular pentagon,
  recomposing Penrose kite/dart P2; credited to L.Danzer.
* Figure10.3.29(b): six convex pentagons recomposing Penrose rhombs P3.
  The caption imposes pairwise nonparallel subdivision lines.
* Exercise4(a,b) asks the reader to establish aperiodicity for suitable choices
  of parameters. The snippets do not specify those choices or supply a complete
  reconstruction proof.

This is stronger provenance than a modern figure-only mention, but insufficient
for the original problem's quantifiers. Exact pentagon coordinates, the complete
parameter inequalities, and shape-only reconstruction in every tiling admitting
reflections, partial contacts, and omission remain unverified. In particular,
no tile-frequency vector or area-rank value has been established. The separate
marked Danzer triangle sources are not substitutes for these convex-pentagon
sources. Danzer–Grünbaum–Shephard, *Tiles with5-fold symmetry*, the other primary
search hit, concerns regular-polygon patch constructions; it was not used to
supply the missing source geometry.

## Mathematical gate and next decision

Before macro enumeration, recover an exact source definition and the theorem
that every admitted source tiling reconstructs an appropriate Penrose field.
Then compute the source count vector by exact reconstruction, not solely from a
selected substitution patch. If its coordinate Q-rank is at least3 in every
admitted field, uniform two-type whole-source resection is impossible: fixed
integer content vectors u,v would force a limiting normalized source vector
f=λu+μv and hence rank at most2. If rank is2, derive its rational annihilator and
check whether any balanced content permits a convex pentagon boundary. Unlike
the Ammann source, every native source tile here has5 sides, so the prior
Ammann even-boundary conclusion cannot simply be imported.

No rank inference follows merely from the source being a Penrose recomposition;
no enumeration is justified until these obligations are discharged. Source-by-
source cuts have the separate two-target area-rank gate, again requiring exact
areas. Source access is the present blocker for this route, not an impossibility
result for convex pentagon pairs.

## Replay of the public text boundary

The public unauthenticated FTS endpoint is
`https://be-api.us.archive.org/fts/v1/search`. Query its `q` parameter with each
phrase below followed by ` AND identifier:isbn_0716711931`; inspect only
`hits.hits[].highlight.text`. This is search access, not retrieval of restricted
page images or encrypted book files.

```text
"nine convex"
"six convex pentagons"
"construction is due to L. Danzer"
"obtained by recomposition of the Penrose"
"lines of subdivision"
"Show that the recomposition"
"parameters are chosen"
```

These recovered fragments locate Figure10.3.29(a,b) and Exercise4; they do not
recover the figure or full definitions. The JSON field `page_num:[[726]]` is not
used as a printed page locator. Targeted web searches for the two family names
and figure number supplied no additional inspectable exact primary construction.

Restart: obtain an openly readable Figure10.3.29 plus its surrounding exercise
and applicable tiling conventions, or another primary exact rederivation. Then
apply the rank/annihilator gate above before geometric macro searches. Until
then this source change is an available but blocked route.

## Newly acquired author PDF: negative resource match

Subsequently inspected the complete primary author-hosted paper:
R.Ammann, B.Grünbaum and G.C.Shephard, *Aperiodic Tiles*, Discrete &
Computational Geometry8 (1992),1–25,
[author PDF](https://faculty.washington.edu/moishe/branko/BG186.Aperiodic%20tiles.pdf).
The scan has an added library cover; printed page2 is PDF page3.

Printed page2 explicitly distinguishes Ammann's convex three-tile set A1
(book p549), which it excludes from treatment, from the four proved sets
A2,A3,A4,A5. Figures1,7,13,22 define those other sets through nonconvex
shape variants or marked convex variants. No Danzer nine-pentagon or
Grünbaum–Shephard six-pentagon source definition appears in the27-page
scan. The complete figure sequence and final remarks were visually inspected;
ordinary text extraction only recovers the added library cover.

The paper's introductory convention admits direct and opposite congruence,
and its proof framework uses unique composition and inherited matching rules.
Those facts concern its own stated sets and do not discharge reconstruction
for the unprovided Figure10.3.29 pentagons. Thus this resource is not the
missing exact source. No new rank claim or enumeration follows; the restart
obligation above remains. No scan reproduction was added to the repository.
