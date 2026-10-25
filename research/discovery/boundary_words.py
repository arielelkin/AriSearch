"""Finite exact library of equiangular 120-degree convex hexagons.

Words give positive native lengths at headings 0,60,...,300 degrees.
Coordinate (x,y) denotes Euclidean (x,sqrt(3)*y); native length l has
physical length 2*l. This ONE common scale is never normalized per tile.
D6 words capture rigid congruence, including reflections, while preserving
size. The finite library is not a new angle family or a tileability result.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from itertools import combinations_with_replacement, product
from math import gcd
from functools import reduce
from typing import Iterable, Mapping

Word = tuple[int, int, int, int, int, int]
Point = tuple[int, int]
DIRECTIONS = ((2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1))


def _word(word: Iterable[int]) -> Word:
    word=tuple(word)
    if len(word)!=6 or any(type(x) is not int or x<=0 for x in word):
        raise ValueError("a boundary word needs six positive integer lengths")
    return word


def closure_vector(word: Iterable[int]) -> Point:
    w=_word(word)
    return (sum(s*d[0] for s,d in zip(w,DIRECTIONS)),
            sum(s*d[1] for s,d in zip(w,DIRECTIONS)))


def is_closed(word: Iterable[int]) -> bool:
    return closure_vector(word)==(0,0)


def closure_parameter(word: Iterable[int]) -> int:
    w=_word(word)
    k=w[0]-w[3]
    if k != w[2]-w[5] or k != w[4]-w[1]:
        raise ValueError("boundary word does not close")
    return k


def vertices(word: Iterable[int]) -> tuple[Point,...]:
    """CCW strict corners, with vertex0=(0,0); reject nonclosing words."""
    w=_word(word)
    closure_parameter(w)
    points=[]
    x=y=0
    for s,(dx,dy) in zip(w,DIRECTIONS):
        points.append((x,y))
        x+=s*dx
        y+=s*dy
    assert (x,y)==(0,0)
    return tuple(points)


def orientations(word: Iterable[int]) -> tuple[Word,...]:
    """Distinct directed length states under rotations and reflections.

    In each returned word, entry k belongs to the globally fixed heading k.
    All polygons begin at vertex0=(0,0). Reflection reverses cyclic order.
    """
    w=_word(word)
    closure_parameter(w)
    return tuple(sorted({seq[i:]+seq[:i] for seq in (w,w[::-1]) for i in range(6)}))


def canonical_word(word: Iterable[int]) -> Word:
    return min(orientations(word))


def tile_id(word: Iterable[int]) -> str:
    return "bw120-"+"-".join(map(str,canonical_word(word)))


def _double_area(poly: tuple[Point,...]) -> int:
    return sum(x*v-y*u for (x,y),(u,v) in zip(poly,poly[1:]+poly[:1]))


@dataclass(frozen=True)
class BoundaryTile:
    id: str
    word: Word
    polygon: tuple[Point,...]
    centrally_symmetric: bool

    @property
    def side_count(self) -> int:
        return 6

    def to_dict(self) -> dict:
        w=self.word
        return {"id":self.id,"word":list(w),"polygon":[list(p) for p in self.polygon],
                "centrally_symmetric":self.centrally_symmetric,
                "closure_parameter":closure_parameter(w),
                "side_count":6,"angles_degrees":[120]*6,
                "edge_squared_lengths":[4*x*x for x in w],
                "double_area_coefficient_sqrt3":_double_area(self.polygon),
                "corner_length_pairs":[[w[i-1],w[i]] for i in range(6)],
                "angle_cos_data":[{"dot":-2*w[i-1]*w[i],
                                   "norm_product_squared":16*w[i-1]**2*w[i]**2}
                                  for i in range(6)],
                "orientation_words":[list(s) for s in orientations(w)]}


def enumerate_words(max_length: int=6) -> tuple[BoundaryTile,...]:
    """Exactly exhaust words in {1,...,M}^6 satisfying closure, modulo D6.

    Four free lengths s0,s1,s2,s3 give k=s0-s3, s4=s1+k,
    s5=s2-k. Bounds on the last two are checked exactly. Positive closed
    edges in strictly increasing directions form a strictly convex hexagon.
    No gcd division or per-shape scaling is performed.
    """
    if type(max_length) is not int or max_length<1:
        raise ValueError("max_length must be a positive integer")
    found=set()
    for a,b,c,d in product(range(1,max_length+1),repeat=4):
        k=a-d
        e,f=b+k,c-k
        if 1<=e<=max_length and 1<=f<=max_length:
            found.add(canonical_word((a,b,c,d,e,f)))
    return tuple(BoundaryTile(tile_id(w),w,vertices(w),closure_parameter(w)==0)
                 for w in sorted(found))


def _tile_fields(tile):
    if isinstance(tile,BoundaryTile):
        return tile.id,tile.word
    return tile["id"],_word(tile["word"])


def states(tiles: Iterable[BoundaryTile | Mapping]) -> tuple[dict,...]:
    """All distinct directed states with exact edge slots and corner geometry."""
    result=[]
    for tile in sorted(tiles,key=lambda t:_tile_fields(t)[0]):
        identifier,word=_tile_fields(tile)
        for index,w in enumerate(orientations(word)):
            result.append({"state_id":f"{identifier}:o{index:02d}","tile_id":identifier,
                           "word":w,"polygon":vertices(w),"orientation":index})
    return tuple(result)


def edge_compatible(left: Mapping, right: Mapping, heading: int) -> bool:
    """Native full-edge matching in fixed global headings."""
    return left["word"][heading%6]==right["word"][(heading+3)%6]


def compatibility_metadata(tiles: Iterable[BoundaryTile | Mapping]) -> dict:
    """Exact local length compatibility; no assertion of patch extension.

    At each vertex three 120-degree corners meet. With reflected copies
    allowed, ray lengths a,b,c are locally possible exactly when each of
    their three unordered adjacent pairs occurs as a native tile corner.
    Loops (a,a) are retained. Edge matches require equal actual lengths.
    """
    tiles=tuple(tiles)
    pair_sources={}
    edge_sources={}
    for tile in tiles:
        identifier,w=_tile_fields(tile)
        for i,length in enumerate(w):
            edge_sources.setdefault(length,[]).append([identifier,i])
            pair=tuple(sorted((w[i-1],length)))
            pair_sources.setdefault(pair,[]).append([identifier,i])
    palette=sorted(edge_sources)
    stars=[(a,b,c) for a,b,c in combinations_with_replacement(palette,3)
           if all(tuple(sorted(p)) in pair_sources for p in ((a,b),(b,c),(c,a)))]
    return {"angle_degrees":120,"corner_count_at_vertex":3,
            "edge_rule":"state[k] == neighbor[(k+3)%6]",
            "edge_lengths":[{"native_length":length,"physical_squared_length":4*length*length,
                             "sources":sorted(edge_sources[length])} for length in palette],
            "corner_pairs":[{"lengths":list(pair),"sources":sorted(pair_sources[pair])}
                            for pair in sorted(pair_sources)],
            "locally_compatible_ray_length_triples":[list(s) for s in stars]}


def library_metadata(tiles: Iterable[BoundaryTile | Mapping]) -> dict:
    tiles=tuple(tiles)
    words=[_tile_fields(t)[1] for t in tiles]
    central=sum(closure_parameter(w)==0 for w in words)
    distinct_lengths=Counter(len(set(w)) for w in words)
    # Gcd reduction is used ONLY to count similarity families as audit metadata.
    # It never changes catalogue identities, geometry, states, or compatibility.
    similarity={canonical_word(tuple(x//reduce(gcd,w) for x in w)) for w in words}
    return {"tile_count":len(words),"central_count":central,
            "noncentral_count":len(words)-central,
            "distinct_length_count_histogram":dict(sorted(distinct_lengths.items())),
            "integer_similarity_family_count":len(similarity),
            "common_physical_length_scale":2,
            "coordinate_convention":"(x,y) represents Euclidean (x,sqrt(3)*y)",
            "scope":"finite integer side-length library; all six angles120; no new angle family"}


# Explicit native fixtures already present in this repository; this is an
# overlap audit, not a literature review or a novelty assertion.
PRIOR_FIXTURES = (
    {"name":"three-length seed", "source":"research/searches/two-equiangular-three-length-seed-sol-2026-10-19.md",
     "words":((1,2,2,2,1,3),(3,2,2,2,3,1)),
     "common_scale_from_prior_to_library":"2",
     "audit_note":"Prior note assigns all four corner-pair types to either word; exactly they occur in the union. A lacks(2,3), B lacks(1,2)."},
    {"name":"power-cell periodic mixed pair", "source":"research/searches/two-equiangular-hexagons-sol-2026-10-19.md",
     "words":((2,5,2,5,2,5),(5,5,5,5,5,5)),
     "common_scale_from_prior_to_library":"4*sqrt(3)"},
)


def prior_fixture_overlap(tiles: Iterable[BoundaryTile | Mapping]) -> list[dict]:
    available={canonical_word(_tile_fields(t)[1]):_tile_fields(t)[0] for t in tiles}
    return [{"name":fixture["name"],"source":fixture["source"],
             "common_scale_from_prior_to_library":fixture["common_scale_from_prior_to_library"],
             "audit_note":fixture.get("audit_note","Explicit known periodic mixed fixture; central member permits omission escape."),
             "tile_ids":[available.get(canonical_word(w)) for w in fixture["words"]],
             "all_members_present":all(canonical_word(w) in available for w in fixture["words"])}
            for fixture in PRIOR_FIXTURES]
