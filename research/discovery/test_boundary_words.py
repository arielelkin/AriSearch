"""Independent finite-word and exact-coordinate checks for the M<=6 library."""
from itertools import product
import pytest

from research.discovery.boundary_words import (
    DIRECTIONS, canonical_word, closure_parameter, closure_vector,
    compatibility_metadata, edge_compatible, enumerate_words, is_closed,
    library_metadata, orientations, prior_fixture_overlap, states, vertices,
)


def _cross(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])


def _distance(a,b):
    return (a[0]-b[0])**2+3*(a[1]-b[1])**2


def _metric_signature(poly):
    # Independent complete polygon congruence check, preserving absolute scale.
    return min(tuple(_distance(a,b) for a in seq[i:]+seq[:i]
                     for b in seq[i:]+seq[:i])
               for seq in (poly,poly[::-1]) for i in range(6))


def test_four_free_enumerator_matches_unpruned_sixfold_product_m3():
    expected=set()
    raw_count=0
    for w in product(range(1,4),repeat=6):
        # Direct coordinate closure, independent of the four-free formula.
        sx=sum(w[i]*DIRECTIONS[i][0] for i in range(6))
        sy=sum(w[i]*DIRECTIONS[i][1] for i in range(6))
        if (sx,sy)==(0,0):
            raw_count+=1
            expected.add(min(seq[i:]+seq[:i] for seq in (w,w[::-1]) for i in range(6)))
    actual=enumerate_words(3)
    assert {t.word for t in actual}==expected
    assert raw_count==len(states(actual))==45
    assert len(actual)==15


def test_m6_counts_and_metric_diversity():
    tiles=enumerate_words(6)
    meta=library_metadata(tiles)
    assert meta["tile_count"]==126
    assert meta["central_count"]==56
    assert meta["noncentral_count"]==70
    assert meta["distinct_length_count_histogram"]=={1:6,2:45,3:32,4:31,5:10,6:2}
    assert meta["integer_similarity_family_count"]==106
    assert len(states(tiles))==666
    assert len({t.id for t in tiles})==126
    assert len({_metric_signature(t.polygon) for t in tiles})==126
    assert [t.word for t in tiles]==sorted(t.word for t in tiles)


def test_all_m6_polygons_are_exact_strictly_convex_and_equiangular():
    for tile in enumerate_words(6):
        w,p=tile.word,tile.polygon
        assert p==vertices(w)
        assert closure_vector(w)==(0,0)
        assert is_closed(w)
        k=closure_parameter(w)
        assert k==w[0]-w[3]==w[2]-w[5]==w[4]-w[1]
        assert tile.centrally_symmetric==(w[:3]==w[3:])
        for i,(a,b) in enumerate(zip(p,p[1:]+p[:1])):
            assert _distance(a,b)==4*w[i]**2
            # Every nonincident vertex is strictly left of every directed side.
            assert all(_cross(a,b,c)>0 for j,c in enumerate(p) if j not in (i,(i+1)%6))
            previous=p[i-1]
            u=(previous[0]-a[0],previous[1]-a[1])
            v=(b[0]-a[0],b[1]-a[1])
            dot=u[0]*v[0]+3*u[1]*v[1]
            assert dot==-2*w[i-1]*w[i]
            assert 4*dot*dot==_distance(previous,a)*_distance(b,a)
        center_sum=(p[0][0]+p[3][0],p[0][1]+p[3][1])
        central_geometry=all((p[i][0]+p[i+3][0],p[i][1]+p[i+3][1])==center_sum for i in range(3))
        assert central_geometry==tile.centrally_symmetric


def test_states_preserve_absolute_scale_and_all_dihedral_readings():
    tiles=enumerate_words(6)
    for tile in tiles:
        readings=orientations(tile.word)
        assert len(readings)<=12
        assert all(canonical_word(w)==tile.word for w in readings)
        signature=_metric_signature(tile.polygon)
        assert all(_metric_signature(vertices(w))==signature for w in readings)
        actual=states((tile,))
        assert {s["word"] for s in actual}==set(readings)
        assert all(s["polygon"][0]==(0,0) for s in actual)
        assert states((tile.to_dict(),))==actual
    regulars=[t for t in tiles if len(set(t.word))==1]
    assert len(regulars)==6
    assert len({t.id for t in regulars})==6
    assert len({_metric_signature(t.polygon) for t in regulars})==6


def test_exact_edge_and_corner_metadata_retains_loops():
    tiles=enumerate_words(3)
    seed=next(t for t in tiles if t.word==(1,2,2,2,1,3))
    partner=next(t for t in tiles if t.word==(1,3,2,2,2,3))
    own_pairs={tuple(p["lengths"]) for p in compatibility_metadata((seed,))["corner_pairs"]}
    assert own_pairs=={(1,2),(2,2),(1,3)}
    meta=compatibility_metadata((seed,partner))
    pairs={tuple(p["lengths"]) for p in meta["corner_pairs"]}
    assert pairs=={(1,2),(2,2),(2,3),(1,3)}
    stars={tuple(t) for t in meta["locally_compatible_ray_length_triples"]}
    assert (1,2,3) in stars
    assert (2,2,2) in stars
    assert (1,1,1) not in stars
    ss=states((seed,))
    for a,b in product(ss,repeat=2):
        for heading in range(6):
            assert edge_compatible(a,b,heading)==(a["word"][heading]==b["word"][(heading+3)%6])
            assert edge_compatible(a,b,heading)==edge_compatible(b,a,heading+3)


def test_prior_fixture_overlap_is_explicit_and_common_scale_only():
    fixtures=prior_fixture_overlap(enumerate_words(6))
    assert all(f["all_members_present"] for f in fixtures)
    assert len(fixtures)==2
    assert all(len(f["tile_ids"])==2 and all(f["tile_ids"]) for f in fixtures)
    small=prior_fixture_overlap(enumerate_words(3))
    assert small[0]["all_members_present"]
    assert not small[1]["all_members_present"]


def test_invalid_lengths_and_nonclosure_are_rejected():
    for w in ((1,)*5,(0,1,1,1,1,1),(1,1,1,1,1,1.0)):
        with pytest.raises(ValueError): vertices(w)
    bad=(1,1,1,1,1,2)
    assert not is_closed(bad)
    with pytest.raises(ValueError): vertices(bad)
    for bound in (0,-1,2.5):
        with pytest.raises(ValueError): enumerate_words(bound)
