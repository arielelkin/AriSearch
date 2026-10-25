"""Exact fixed-domain catalogue and contact-preflight regression checks."""
from itertools import product
from sage.all import QQ
import pytest

from research.discovery.mixed_angles import (
    K, ONE, NORMALS, SQRT2, SQRT3, SQRT6, MixedTile, P_ANGLES, Q_ANGLES,
    angle_words, angle_endpoint_cycle, canonical_angles, compatible_stars, corner_states, cross,
    decode, dot, edge_lengths, encode, enumerate_catalogue, incidence_relaxation,
    normal_indices, pair_scales, place_corner, polygon_signature,
    positive_polygon_overlap, stable_content_hash, sign, star_geometry, sub, support_polygon,
)


def test_field_roundtrip_and_exact15_degree_unit_normals():
    assert SQRT2**2==2 and SQRT3**2==3 and SQRT6==SQRT2*SQRT3
    values=(K(0),ONE,SQRT2,SQRT3,SQRT6,(3+SQRT2-2*SQRT3)/7)
    for value in values:
        assert decode(encode(value))==value
    assert encode(3+2*SQRT2-4*SQRT3+SQRT6)==[[3,1],[2,1],[-4,1],[1,1]]
    assert len(set(NORMALS))==24
    assert all(dot(n,n)==1 for n in NORMALS)
    for i,n in enumerate(NORMALS):
        assert NORMALS[(i+12)%24]==(-n[0],-n[1])
        assert sign(cross(n,NORMALS[(i+1)%24]))==1
    assert sign(3-SQRT2-SQRT3)==-1
    assert sign(SQRT2+SQRT3-3)==1


def test_fixed_angle_domain_is_complete_modulo_dihedral():
    assert len(Q_ANGLES)==16
    counts=[]
    for multiset in ((120,)*3+(135,)*4,(120,)*4+(135,)*2+(150,), (120,)*5+(150,)*2):
        # Brute-force seven slots independently, then preserve the multiset.
        expected={canonical_angles(w) for w in product(sorted(set(multiset)),repeat=7)
                  if sorted(w)==sorted(multiset)}
        assert set(angle_words(multiset))==expected
        counts.append(len(expected))
    assert counts==[4,9,3]
    for a in (P_ANGLES,)+Q_ANGLES:
        assert sum(a)==(len(a)-2)*180
        assert all(90<x<180 for x in a)
        assert len(normal_indices(a))==len(a)


def test_support_geometry_and_absolute_scale_are_preserved():
    poly=support_polygon(P_ANGLES,(1,)*5)
    assert poly is not None
    twice=support_polygon(P_ANGLES,(2,)*5)
    assert twice==tuple((2*x,2*y) for x,y in poly)
    assert polygon_signature(poly)!=polygon_signature(twice)
    assert polygon_signature(poly)==polygon_signature(twice,ONE/2)
    lengths=edge_lengths(poly,P_ANGLES)
    for i,length in enumerate(lengths):
        delta=sub(poly[(i+1)%5],poly[i])
        assert length*length==dot(delta,delta)
        assert sign(length)==1
    # A support farther out than its two neighboring constraints is inactive.
    assert support_polygon((120,)*6,(2,1,1,1,1,1)) is None


def test_catalogue_fixed_domain_counts_and_all_native_edges():
    tiles,stats=enumerate_catalogue()
    assert stats["attempted"]==2080
    assert stats["inactive_or_zero"]==1535
    assert stats["P_tiles"]==20 and stats["Q_tiles"]==398
    assert len({t.signature for t in tiles})==418
    assert sum(len(t.defining_data) for t in tiles)==545
    assert {t.angles for t in tiles if t.species=="Q"}==set(Q_ANGLES)
    for tile in tiles:
        assert all(sign(length)>0 for length in tile.lengths)
        assert len(tile.polygon)==len(tile.angles)
        assert all(sign(cross(sub(tile.polygon[i],tile.polygon[i-1]),
                              sub(tile.polygon[(i+1)%len(tile.polygon)],tile.polygon[i])))>0
                   for i in range(len(tile.polygon)))


def _regular(species):
    angles=(120,)*6
    poly=support_polygon(angles,(1,)*6)
    lengths=edge_lengths(poly,angles)
    return MixedTile(species,species,angles,(1,)*6,poly,lengths,polygon_signature(poly),())


def test_corner_states_keep_reflections_and_geometry_matches_full_edges():
    p,q=_regular("P"),_regular("Q")
    assert pair_scales(p,q)==(ONE,)
    stars=compatible_stars(p,q,ONE)
    assert {c for key in stars for c in key}==set(range(12))
    for key in ((0,0,0),(0,6,6),(6,6,6)):
        geometry=star_geometry(p,q,ONE,stars[key])
        assert geometry["pairwise_interior_disjoint"]
        assert geometry["radial_native_edges_matched"]
    source=support_polygon(P_ANGLES,(1,2,1,1,1))
    tile=MixedTile("p","P",P_ANGLES,(1,2,1,1,1),source,edge_lengths(source,P_ANGLES),polygon_signature(source),())
    for index in range(5):
        for reflected in (False,True):
            placed=place_corner(tile,index,reflected,0)
            assert polygon_signature(placed)==tile.signature
            assert (K(0),K(0)) in placed
    assert positive_polygon_overlap(p.polygon,p.polygon)
    assert not positive_polygon_overlap(p.polygon,tuple((x+100,y) for x,y in p.polygon))


def test_incidence_is_exact_frequency_relaxation_and_catches_coverage_falsepositive():
    feasible={key:None for key in ((0,1,2),(3,4,5),(6,7,8),(9,10,11))}
    answer=incidence_relaxation(feasible)
    assert answer["feasible"] and not answer["actual_patch"]
    assert answer["Euler"]=={"V":4,"E":6,"F":2}
    assert sum(QQ(r["weight"][0])/QQ(r["weight"][1]) for r in answer["weights"])==4
    bad={key:None for key in ((0,0,1),(1,2,3),(4,5,6),(7,8,9),(10,10,11))}
    assert {c for key in bad for c in key}==set(range(12))
    negative=incidence_relaxation(bad)
    assert not negative["feasible"]
    y=[QQ(a)/QQ(b) for a,b in negative["farkas"]["native_corner_weights"]]
    assert sum(y)==-1
    assert all(sum(y[c] for c in key)>=0 for key in bad)


def test_angle_endpoint_cycle_exhausts_both_reflections_and_exactly_two_q_words_fail():
    failing=[]
    for word in Q_ANGLES:
        p=angle_endpoint_cycle(P_ANGLES,P_ANGLES,word)
        q=angle_endpoint_cycle(word,P_ANGLES,word)
        assert q["feasible"]
        if not p["feasible"]:
            failing.append(word)
            assert p["angle_state_cycle_count"]==0
            assert all(not trial["closing_states"] for trial in p["trials"])
        else:
            witness=p["witness_cycle"]
            assert len(witness)==5
            assert all(witness[i-1][1]+P_ANGLES[i]+witness[i][0]==360 for i in range(5))
        for option in p["endpoint_options"]:
            assert all(isinstance(source["reflected"],bool) for source in option["native_sources"])
    assert failing==[(120,120,120,120,150,120,150),(120,120,120,150,120,120,150)]


def test_content_hash_excludes_elapsed_timing_but_preserves_math():
    a={"counts":[20,398],"stats":{"elapsed_seconds":1},"cpu_seconds":3}
    b={"counts":[20,398],"stats":{"elapsed_seconds":200},"cpu_seconds":900}
    assert stable_content_hash(a)==stable_content_hash(b)
    b["counts"][0]=21
    assert stable_content_hash(a)!=stable_content_hash(b)
