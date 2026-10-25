"""Independent exact arithmetic and geometry audit for mixed obtuse preflight.

Coordinates are actual Euclidean coordinates in Q(sqrt2,sqrt3), serialized
as four rational pairs in the basis (1,sqrt2,sqrt3,sqrt6). No Sage arithmetic
is used here. Local stars and rational incidence are necessary conditions;
they do not certify a planar extension, a substitution, or aperiodicity.
"""
from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
import hashlib
import gzip
from itertools import permutations, product
import json
import tempfile
from math import isqrt
from pathlib import Path

from .verify import VerificationError, digest, require


@dataclass(frozen=True,slots=True)
class F:
    c: tuple

    def __init__(self,value=0):
        if isinstance(value,F):
            coeffs = value.c
        elif isinstance(value,(int,Fraction)):
            coeffs = (Fraction(value),Fraction(0),Fraction(0),Fraction(0))
        else:
            require(len(value) == 4,'field requires four coefficients')
            coeffs = tuple(Fraction(x) for x in value)
        object.__setattr__(self,'c',coeffs)

    def __add__(self,other):
        other = F(other)
        if not self:
            return other
        if not other:
            return self
        return F(tuple(a+b for a,b in zip(self.c,other.c)))
    __radd__ = __add__

    def __neg__(self):
        return F(tuple(-a for a in self.c))

    def __sub__(self,other):
        return self+-F(other)

    def __rsub__(self,other):
        return F(other)+-self

    def __mul__(self,other):
        other = F(other)
        if not self or not other:
            return ZERO
        if self == ONE:
            return other
        if other == ONE:
            return self
        result = [Fraction(0) for _ in range(4)]
        for i,a in enumerate(self.c):
            if not a:
                continue
            for j,b in enumerate(other.c):
                if not b:
                    continue
                common = i&j
                factor = (2 if common&1 else 1)*(3 if common&2 else 1)
                result[i^j] += factor*a*b
        return F(tuple(result))
    __rmul__ = __mul__

    @lru_cache(None)
    def inverse(self):
        require(self != ZERO,'division by zero in exact field')
        a,b,c,d = self.c
        conjugate3 = F((a,b,-c,-d))
        norm3 = self*conjugate3
        require(norm3.c[2:] == (0,0),'field norm arithmetic failure')
        aa,bb = norm3.c[:2]
        return conjugate3*F((aa,-bb,0,0))/Fraction(aa*aa-2*bb*bb)

    def __truediv__(self,other):
        if isinstance(other,(int,Fraction)):
            require(other != 0,'division by zero rational')
            return F(tuple(a/other for a in self.c))
        return self*F(other).inverse()

    def __rtruediv__(self,other):
        return F(other)*self.inverse()

    def __pow__(self,power):
        require(type(power) is int,'integer field exponent required')
        if power < 0:
            return self.inverse()**(-power)
        result,base = ONE,self
        while power:
            if power&1:
                result *= base
            base *= base
            power >>= 1
        return result

    def __bool__(self):
        return any(self.c)

    @lru_cache(None)
    def sign(self):
        if not self:
            return 0
        bits = 8
        while True:
            denominator = 1<<bits
            bounds = [(Fraction(1),Fraction(1))]
            for radicand in (2,3,6):
                root = isqrt(radicand << (2*bits))
                bounds.append((Fraction(root,denominator),Fraction(root+1,denominator)))
            lower = sum(a*(lo if a >= 0 else hi) for a,(lo,hi) in zip(self.c,bounds))
            upper = sum(a*(hi if a >= 0 else lo) for a,(lo,hi) in zip(self.c,bounds))
            if lower > 0:
                return 1
            if upper < 0:
                return -1
            bits *= 2

    def wire(self):
        return [[a.numerator,a.denominator] for a in self.c]


ZERO,ONE = F(0),F(1)
SQRT2,SQRT3,SQRT6 = F((0,1,0,0)),F((0,0,1,0)),F((0,0,0,1))


def decode(raw):
    require(len(raw) == 4 and all(len(p) == 2 and all(type(x) is int for x in p) and p[1] > 0 for p in raw),
            'invalid field serialization')
    result = F(tuple(Fraction(a,b) for a,b in raw))
    require(result.wire() == raw,'noncanonical field rational serialization')
    return result


def point(raw):
    require(len(raw) == 2,'point requires two coordinates')
    return tuple(decode(x) for x in raw)


def encode_points(poly):
    return [[x.wire(),y.wire()] for x,y in poly]


def add(a,b):
    return a[0]+b[0],a[1]+b[1]


def sub(a,b):
    return a[0]-b[0],a[1]-b[1]


def dot(a,b):
    return a[0]*b[0]+a[1]*b[1]


def cross(a,b):
    return a[0]*b[1]-a[1]*b[0]


@lru_cache(None)
def direction(index):
    # Repeated exact complex multiplication, with independent coefficient algebra.
    c,s = (SQRT6+SQRT2)/4,(SQRT6-SQRT2)/4
    x,y = ONE,ZERO
    for _ in range(index%24):
        x,y = x*c-y*s,x*s+y*c
    return x,y


def canonical_angles(angles):
    angles = tuple(angles)
    return min(seq[i:]+seq[:i] for seq in (angles,angles[::-1]) for i in range(len(angles)))


def independent_angle_words():
    palettes = ((120,)*3+(135,)*4,(120,)*4+(135,)*2+(150,),(120,)*5+(150,)*2)
    return sorted({canonical_angles(w) for palette in palettes for w in set(permutations(palette))})


def normal_indices(angles):
    require(sum(angles) == (len(angles)-2)*180 and all(90 < a < 180 and a%15 == 0 for a in angles),
            'invalid obtuse angle word')
    return tuple(sum(180-a for a in angles[1:i+1])//15 % 24 for i in range(len(angles)))


def support_polygon(angles,offsets):
    require(len(angles) == len(offsets) and all(h in (1,2) for h in offsets),'outside fixed support-offset domain')
    normals = [direction(i) for i in normal_indices(angles)]
    poly = []
    for i,n in enumerate(normals):
        prev = normals[i-1]
        determinant = cross(prev,n)
        require(determinant.sign() > 0,'invalid normal order')
        poly.append(((offsets[i-1]*n[1]-offsets[i]*prev[1])/determinant,
                     (offsets[i]*prev[0]-offsets[i-1]*n[0])/determinant))
    for i,n in enumerate(normals):
        for j,p in enumerate(poly):
            slack = F(offsets[i])-dot(n,p)
            if j in (i,(i+1)%len(poly)):
                require(not slack,'incident support equation violated')
            elif slack.sign() <= 0:
                return None
    return tuple(poly)


def edge_lengths(poly,angles):
    return tuple(dot(sub(poly[(i+1)%len(poly)],poly[i]),(-direction(k)[1],direction(k)[0]))
                 for i,k in enumerate(normal_indices(angles)))


def polygon_signature(poly,scale=ONE):
    n = len(poly)
    distances = [[None]*n for _ in poly]
    factor = scale*scale
    for i,a in enumerate(poly):
        for j in range(i+1):
            delta = sub(a,poly[j])
            value = tuple(tuple(pair) for pair in (dot(delta,delta)*factor).wire())
            distances[i][j] = distances[j][i] = value
    words = []
    for direction in (1,-1):
        for start in range(n):
            indices = [(start+direction*i)%n for i in range(n)]
            words.append(tuple(distances[i][j] for i in indices for j in indices))
    return n,min(words)


def strict_convex(poly):
    require(len(poly) >= 3,'degenerate polygon')
    turns = [cross(sub(poly[(i+1)%len(poly)],p),sub(poly[(i+2)%len(poly)],poly[(i+1)%len(poly)])).sign()
             for i,p in enumerate(poly)]
    require(all(s == 1 for s in turns) or all(s == -1 for s in turns),'polygon is not strictly convex')
    orientation = turns[0]
    require(all(cross(sub(q,p),sub(r,p)).sign()*orientation >= 0
                for p,q in zip(poly,poly[1:]+poly[:1]) for r in poly),'polygon crosses its support sides')
    return orientation


def interiors_overlap(a,b):
    for poly in (a,b):
        for p,q in zip(poly,poly[1:]+poly[:1]):
            edge = sub(q,p)
            aa,bb = [cross(edge,v) for v in a],[cross(edge,v) for v in b]
            maximum = lambda xs: max(xs,key=lambda x: _Ordered(x))
            minimum = lambda xs: min(xs,key=lambda x: _Ordered(x))
            if (maximum(aa)-minimum(bb)).sign() <= 0 or (maximum(bb)-minimum(aa)).sign() <= 0:
                return False
    return True


class _Ordered:
    def __init__(self,value):
        self.value = value
    def __lt__(self,other):
        return (self.value-other.value).sign() < 0


def verify_catalogue(data):
    require(data['schema'] == 'mixed-obtuse-support-v1','unknown mixed catalogue schema')
    require(data['support_domain'] == [1,2] and data['field_basis'] == ['1','sqrt(2)','sqrt(3)','sqrt(6)'], 'mixed field/domain mismatch')
    expected = {}
    statistics = []
    for species,words in (('P',[(105,105,105,105,120)]),('Q',independent_angle_words())):
        for angles in words:
            valid = 0
            signatures = set()
            for offsets in product((1,2),repeat=len(angles)):
                poly = support_polygon(angles,offsets)
                if poly is None:
                    continue
                valid += 1
                signature = polygon_signature(poly)
                signatures.add(signature)
                expected.setdefault(signature,[]).append((tuple(angles),offsets))
            statistics.append({'species':species,'angles':list(angles),'attempted':2**len(angles),
                               'valid_definitions':valid,'congruence_classes':len(signatures)})
    actual = {}
    for tile in data['tiles']:
        angles,offsets = tuple(tile['angles']),tuple(tile['offsets'])
        species = 'P' if len(angles) == 5 else 'Q'
        require(tile['species'] == species,'catalogue species disagrees with polygon family')
        poly = support_polygon(angles,offsets)
        require(poly is not None,'retained polygon has inactive side')
        require(encode_points(poly) == tile['polygon'],'retained support polygon differs from independent reconstruction')
        require(list(normal_indices(angles)) == tile['normal_indices'],'normal turn-index mismatch')
        lengths = edge_lengths(poly,angles)
        require(all(x.sign() > 0 for x in lengths),'nonpositive native side')
        require([x.wire() for x in lengths] == tile['lengths'],'native side length mismatch')
        signature = polygon_signature(poly)
        require(json.loads(json.dumps(signature)) == tile['signature'],'congruence signature mismatch')
        require(signature not in actual,'duplicate congruent retained tile')
        definitions = [(tuple(d['angles']),tuple(d['offsets'])) for d in tile['defining_data']]
        require(len(definitions) == len(set(definitions))
                and set(definitions) == set(expected[signature]),'lost or duplicate support definitions or grid phases')
        expected_id = tile['species'].lower()+str(len(angles))+'-'+hashlib.sha256(json.dumps(signature,separators=(',',':')).encode()).hexdigest()[:16]
        require(tile['id'] == expected_id,'tile identity does not bind exact geometry')
        actual[signature] = tile
    require(set(actual) == set(expected),'fixed support domain not completely covered')
    expected_stats = {
        'P_angle_words':1,'Q_angle_words':len(independent_angle_words()),
        'attempted':sum(row['attempted'] for row in statistics),
        'inactive_or_zero':sum(row['attempted']-row['valid_definitions'] for row in statistics),
        'by_angle_word':statistics,
        'P_tiles':sum(tile['species'] == 'P' for tile in actual.values()),
        'Q_tiles':sum(tile['species'] == 'Q' for tile in actual.values()),
    }
    require(all(data['stats'].get(key) == value for key,value in expected_stats.items()),
            'support enumeration counters disagree')
    return {'valid':True,'kind':'mixed_catalogue','tiles':len(actual),
            'P_tiles':sum(t['species'] == 'P' for t in actual.values()),
            'Q_tiles':sum(t['species'] == 'Q' for t in actual.values()),
            'Q_angle_words':len(independent_angle_words()),
            'scope':'complete specified binary support-offset domain only'}


def angular_ring_possible(root_angles,p_angles,q_angles):
    """Exact endpoint-angle cycle, including both reflection parities."""
    options = {(word[i],word[(i+1)%len(word)]) for word in (p_angles,q_angles) for i in range(len(word))}
    options |= {(b,a) for a,b in tuple(options)}
    for first in options:
        reachable = {first}
        for i in range(1,len(root_angles)):
            reachable = {following for previous in reachable for following in options
                         if previous[1]+following[0]+root_angles[i] == 360}
        if any(last[1]+first[0]+root_angles[0] == 360 for last in reachable):
            return True
    return False


def verify_star(star,p,q,ratio):
    tiles = {p['id']:p,q['id']:q}
    require(len(star['corners']) == len(star['polygons']) == 3,'star needs three polygons')
    heading,indices,polys,endpoints = 0,[],[],[]
    for item,raw_poly in zip(star['corners'],star['polygons']):
        require(item['tile_id'] in tiles,'star references unrelated species')
        tile = tiles[item['tile_id']]
        native = tuple(point(raw) for raw in tile['polygon'])
        lengths = tuple(decode(x) for x in tile['lengths'])
        index,reflected = item['native_corner'],item['reflected']
        require(type(index) is int and 0 <= index < len(native) and type(reflected) is bool,'invalid native corner state')
        require(item['angle'] == tile['angles'][index] and item['start_heading_15deg'] == heading,'star sector angles/headings disagree')
        require(item['species'] == tile['species'],'star species annotation mismatch')
        scale = ONE if tile['species'] == 'P' else ratio
        require(decode(item['scale']) == scale,'star uses an independent per-tile scale')
        rotation = item['rotation_index_15deg']
        require(type(rotation) is int and 0 <= rotation < 24,'star rotation not in native frame')
        co,si = direction(rotation)
        translation = point(item['translation'])
        expected = []
        for x,y in native:
            if reflected:
                y = -y
            expected.append(add((scale*(co*x-si*y),scale*(si*x+co*y)),translation))
        poly = tuple(point(raw) for raw in raw_poly)
        require(poly == tuple(expected),'star polygons differ from exact isometries')
        strict_convex(poly)
        require(poly[index] == (ZERO,ZERO),'star native corner is not at the common vertex')
        start_index,end_index = ((index-1)%len(poly),(index+1)%len(poly)) if reflected else ((index+1)%len(poly),(index-1)%len(poly))
        start_length = lengths[index-1 if reflected else index]*scale
        end_length = lengths[index if reflected else index-1]*scale
        target = direction(heading)
        require(poly[start_index] == (target[0]*start_length,target[1]*start_length),'star start side does not follow its sector ray')
        heading += item['angle']//15
        target = direction(heading)
        require(poly[end_index] == (target[0]*end_length,target[1]*end_length),'star end side does not follow its sector ray')
        endpoints.append((poly[start_index],poly[end_index]))
        indices.append(index+(0 if tile['species'] == 'P' else 5))
        polys.append(poly)
    require(heading == 24 and sorted(indices) == star['native_corner_multiset'],'star does not form the asserted360 incidence')
    require(all(endpoints[i][1] == endpoints[(i+1)%3][0] for i in range(3)),'radial native sides have different full endpoints')
    require(all(not interiors_overlap(polys[i],polys[j]) for i in range(3) for j in range(i)), 'star polygons overlap')
    require(star['pairwise_interior_disjoint'] is True and star['radial_native_edges_matched'] is True,'star geometry summary mismatch')
    return tuple(sorted(indices))


def verify_incidence(record,star_keys):
    require(record['actual_patch'] is False,'incidence relaxation incorrectly claims actual patch')
    if record['feasible']:
        require(record['normalized_tile_counts'] == {'P':1,'Q':1} and record['Euler'] == {'V':4,'E':6,'F':2},'incorrect5/7trivalent density normalization')
        demand = [Fraction(0) for _ in range(12)]
        total = Fraction(0)
        seen = set()
        for item in record['weights']:
            key = tuple(item['star'])
            require(key in star_keys and key not in seen,'incidence weights reference absent/duplicated star')
            seen.add(key)
            value = Fraction(*item['weight'])
            require(value >= 0,'negative primal incidence weight')
            total += value
            for corner in key:
                demand[corner] += value
        require(demand == [1]*12 and total == 4,'species-aware native corner frequency equations fail')
    else:
        cert = record['farkas']
        weights = [Fraction(*v) for v in cert['native_corner_weights']]
        require(len(weights) == 12 and sum(weights) == -1,'Farkas demand pairing is not negative')
        require(all(sum(weights[i] for i in key) >= 0 for key in star_keys),'Farkas star column has negative pairing')
        require(cert['demand_dot'] == -1 and cert['all_star_column_dots_nonnegative'] is True,'Farkas summary mismatch')
    return record['feasible']


@lru_cache(None)
def _ratio(a,b):
    return a/b


def _wire_key(value):
    return tuple(tuple(v) for v in value.wire())


def _pair_star_keys(p,q,ratios):
    """Enumerate stars with integer length IDs before assigning any scale.

    A same-species seam compares unscaled lengths. A mixed seam forces one
    exact relative ratio, looked up in the precomputed complete edge table.
    This avoids rescaling every corner for each of150k candidate pairs.
    """
    lengths = {}
    states = []
    for species,tile,base in ((0,p,0),(1,q,5)):
        ls = [decode(v) for v in tile['lengths']]
        for length in ls:
            if length not in lengths:
                lengths[length] = len(lengths)
        for i,angle in enumerate(tile['angles']):
            a,b = lengths[ls[i]],lengths[ls[i-1]]
            states.append((base+i,angle,species,a,b))
            if a != b:
                states.append((base+i,angle,species,b,a))
    ids_to_length = {v:k for k,v in lengths.items()}
    def seam(a,b):
        if a[2] == b[2]:
            return None if a[4] == b[3] else False
        pl,ql = (a[4],b[3]) if a[2] == 0 else (b[3],a[4])
        return ratios[(ids_to_length[pl],ids_to_length[ql])]
    by_angle = {}
    for state in states:
        by_angle.setdefault(state[1],[]).append(state)
    found = {}
    for a in states:
        for b in states:
            ab = seam(a,b)
            if ab is False:
                continue
            for c in by_angle.get(360-a[1]-b[1],()):
                bc,ca = seam(b,c),seam(c,a)
                if bc is False or ca is False:
                    continue
                forced = [r for r in (ab,bc,ca) if r is not None]
                if forced and any(r != forced[0] for r in forced[1:]):
                    continue
                scale = forced[0] if forced else None
                found.setdefault(scale,set()).add(tuple(sorted((a[0],b[0],c[0]))))
    return found


def stable_content_hash(value):
    def scrub(item):
        if isinstance(item,dict):
            return {k:scrub(v) for k,v in item.items() if k not in ('elapsed_seconds','cpu_seconds','wall_seconds','content_sha256')}
        if isinstance(item,(list,tuple)):
            return [scrub(v) for v in item]
        return item
    return digest(scrub(value))


def verify_angle_cycle(record,p_angles,q_angles):
    root = tuple(record['root_angles'])
    source_options = {}
    for species,angles in (('P',p_angles),('Q',q_angles)):
        for i in range(len(angles)):
            for reflected in (False,True):
                pair = (angles[i],angles[(i+1)%len(angles)]) if reflected else (angles[(i+1)%len(angles)],angles[i])
                source_options.setdefault(pair,[]).append({'species':species,'edge':i,'reflected':reflected})
    options = sorted(source_options)
    require(record['endpoint_options'] == [{'angles':list(pair),'native_sources':source_options[pair]} for pair in options],
            'angular cycle omitted an edge endpoint state or reflection')
    trials,total = [],0
    for first in options:
        counts = {first:1}
        layers = [{'edge':0,'states_and_counts':[[list(first),1]]}]
        for i in range(1,len(root)):
            counts = {following:sum(value for previous,value in counts.items() if previous[1]+following[0]+root[i] == 360)
                      for following in options}
            counts = {key:value for key,value in counts.items() if value}
            layers.append({'edge':i,'states_and_counts':[[list(key),value] for key,value in sorted(counts.items())]})
        closing = sorted(key for key in counts if key[1]+first[0]+root[0] == 360)
        count = sum(counts[key] for key in closing)
        total += count
        trials.append({'first_state':list(first),'layers':layers,'closing_states':[list(key) for key in closing],'cycle_count':count})
    retained_trials = [{**trial,'closing_states':sorted(trial['closing_states'])} for trial in record['trials']]
    require(retained_trials == trials and record['angle_state_cycle_count'] == total and record['feasible'] is (total > 0),
            'angular cycle reachability/count proof failed')
    require(record['necessary_only'] is True and record['edge_lengths_relaxed'] is True and record['actual_patch'] is False,
            'angular relaxation overclaims actual geometry')
    witness = record.get('witness_cycle')
    if total:
        require(witness and len(witness) == len(root) and all(tuple(pair) in options for pair in witness), 'angular positive cycle missing')
        require(all(witness[i-1][1]+witness[i][0]+root[i] == 360 for i in range(len(root))), 'angular cycle witness does not close')
    else:
        require(not witness,'impossible angular cycle has a positive witness')
    return total > 0


def verify_preflight(directory,*,check_catalogue=True):
    directory = Path(directory)
    catalogue = json.loads((directory/'catalogue.json').read_text())
    data = json.loads((directory/'preflight.json').read_text())
    require(data['schema'] == 'mixed-obtuse-preflight-v1' and data['complete'] is True,'incomplete or unknown mixed preflight')
    require(data['cpu_cap_seconds'] <= 600,'preflight exceeds authorized CPU bound')
    require(stable_content_hash(catalogue) == catalogue['content_sha256'] == data['catalogue_content_sha256'],'mixed catalogue content hash mismatch')
    require(stable_content_hash(data) == data['content_sha256'],'mixed preflight content hash mismatch')
    require(hashlib.sha256((Path(__file__).parent/'mixed_angles.py').read_bytes()).hexdigest() == data['source_sha256'],'mixed source hash mismatch')
    audit_path = directory/'scale-audit.jsonl.gz'
    require(hashlib.sha256(audit_path.read_bytes()).hexdigest() == data['scale_audit_sha256'],'scale audit hash mismatch')
    catalogue_result = verify_catalogue(catalogue) if check_catalogue else None
    tiles = {tile['id']:tile for tile in catalogue['tiles']}
    require(data['catalogue_stats'] == catalogue['stats'],'preflight catalogue counters mismatch')
    ps = [t for t in catalogue['tiles'] if t['species'] == 'P']
    qs = [t for t in catalogue['tiles'] if t['species'] == 'Q']
    lengths = {t['id']:tuple(decode(v) for v in t['lengths']) for t in catalogue['tiles']}
    bases = {identifier:min(values,key=lambda x:_Ordered(x)) for identifier,values in lengths.items()}
    normalized = {t['id']:polygon_signature(tuple(point(p) for p in t['polygon']),ONE/bases[t['id']]) for t in catalogue['tiles']}
    normalized_lengths = {identifier:tuple(_ratio(v,bases[identifier]) for v in values) for identifier,values in lengths.items()}
    supported = {row['id']:row for row in data['corner_supported_pairs']}
    require(len(supported) == len(data['corner_supported_pairs']),'duplicate corner-supported pair')
    cycles = {}
    require([tuple(row['Q_angle_word']) for row in data['angle_endpoint_cycle_audit']] == independent_angle_words(),'angular cycle audit omits a Q word')
    p_angles = (105,105,105,105,120)
    for row in data['angle_endpoint_cycle_audit']:
        q_angles = tuple(row['Q_angle_word'])
        require(tuple(row['P']['root_angles']) == p_angles and tuple(row['Q']['root_angles']) == q_angles,'angular root word mismatch')
        cycles[q_angles] = (verify_angle_cycle(row['P'],p_angles,q_angles),verify_angle_cycle(row['Q'],p_angles,q_angles))
    counts = Counter({'native_tile_pairs':len(ps)*len(qs)})
    seen,checked_records = {},set()
    feasible_records,strong_records = [],[]
    with gzip.open(audit_path,'rt') as stream:
        rows = iter(stream)
        for p in ps:
            for q in qs:
                ratios = {(a,b):_ratio(a,b) for a in lengths[p['id']] for b in lengths[q['id']]}
                normalized_ratios = {_ratio(a,b):_ratio(na,nb)
                                     for a,na in zip(lengths[p['id']],normalized_lengths[p['id']])
                                     for b,nb in zip(lengths[q['id']],normalized_lengths[q['id']])}
                stars_by_scale = _pair_star_keys(p,q,ratios)
                for scale in sorted(set(ratios.values()),key=_wire_key):
                    try:
                        row = json.loads(next(rows))
                    except StopIteration:
                        raise VerificationError('scale audit omits part of the exact edge-ratio domain')
                    require(row['P'] == p['id'] and row['Q'] == q['id'] and decode(row['Q_scale']) == scale,'scale audit domain/order mismatch')
                    counts['native_pair_scales'] += 1
                    key = (normalized[p['id']],normalized[q['id']],normalized_ratios[scale])
                    if key in seen:
                        representative,base = seen[key]
                        require(row['status'] == 'common-scaling-duplicate' and row['representative'] == representative
                                and decode(row['common_scale_to_representative']) == _ratio(base,bases[p['id']]),'invalid common scaling quotient or representative')
                        counts['common_scale_duplicates'] += 1
                        continue
                    counts['unique_pair_scales'] += 1
                    identifier = 'mix-'+hashlib.sha256(json.dumps((p['id'],q['id'],scale.wire()),separators=(',',':')).encode()).hexdigest()[:16]
                    require(row['id'] == identifier,'pair scale identity mismatch')
                    seen[key] = identifier,bases[p['id']]
                    star_keys = stars_by_scale.get(None,set())|stars_by_scale.get(scale,set())
                    require(row['incidence_star_count'] == len(star_keys),'complete reflected native star count mismatch')
                    covered = {c for key in star_keys for c in key}
                    if len(covered) < 12:
                        require(row['status'] == 'missing-native-corner-support' and row['missing_corners'] == sorted(set(range(12))-covered),
                                'native corner omission is not a valid necessary exclusion')
                        counts['missing_native_corner_support'] += 1
                        continue
                    require(identifier in supported,'corner-supported scale lacks retained star/incidence evidence')
                    record = supported[identifier]
                    require(all(record[k] == row[k] for k in ('P','Q','Q_scale','id','status','incidence_star_count')),'supported record differs from scale audit')
                    require(record['Q_angle_word'] == q['angles'] and record['native_corner_support_complete'] is True,'supported pair word/coverage annotation mismatch')
                    require({tuple(star['native_corner_multiset']) for star in record['stars']} == star_keys
                            and len(record['stars']) == len(star_keys),'retained geometric stars omit a native incidence type')
                    for star in record['stars']:
                        verify_star(star,p,q,scale)
                    counts['geometry_checked_pair_scales'] += 1
                    counts['geometry_checked_stars'] += len(star_keys)
                    feasible = verify_incidence(record['incidence_relaxation'],star_keys)
                    if feasible:
                        counts['incidence_feasible'] += 1
                        feasible_records.append(record)
                        p_cycle,q_cycle = cycles[tuple(q['angles'])]
                        require(record['angular_endpoint_cycle'] == {'P_feasible':p_cycle,'Q_feasible':q_cycle,'proof_Q_angle_word':q['angles']},'pair angular cycle binding mismatch')
                        if p_cycle and q_cycle:
                            require(row['status'] == 'strong-survivor','feasible pair classified as excluded')
                            counts['strong_survivors'] += 1
                            strong_records.append(record)
                        else:
                            require(row['status'] == 'angular-endpoint-cycle-infeasible','impossible angular root classified as a survivor')
                            counts['angular_endpoint_cycle_infeasible'] += 1
                    else:
                        require(row['status'] == 'incidence-infeasible','Farkas excluded pair classified as feasible')
                        counts['incidence_infeasible'] += 1
                    checked_records.add(identifier)
        require(next(rows,None) is None,'scale audit contains unexpected extra pair/scales')
    require(checked_records == set(supported),'unsupported extra pair certificates')
    require(data['incidence_survivors'] == feasible_records and data['strong_survivors'] == strong_records,'survivor lists differ from verified stage filters')
    require(data['funnel'] == {key:counts[key] for key in data['funnel']} and set(data['funnel']) ==
            {'native_tile_pairs','native_pair_scales','common_scale_duplicates','unique_pair_scales','missing_native_corner_support','geometry_checked_pair_scales','geometry_checked_stars','incidence_infeasible','incidence_feasible','angular_endpoint_cycle_infeasible','strong_survivors'},'mixed candidate funnel mismatch')
    q_words = {tuple(r['Q_angle_word']) for r in strong_records}
    gate = {'minimum_pairs':10,'minimum_Q_angle_words':3,'actual_pairs':len(strong_records),
            'actual_Q_angle_words':len(q_words),'passed':len(strong_records)>=10 and len(q_words)>=3,'heuristic_only':True}
    require(data['allocation_gate'] == gate,'heuristic allocation gate mismatch')
    return {'valid':True,'kind':'mixed_preflight','catalogue':catalogue_result,'funnel':data['funnel'],
            'allocation_gate':gate,'content_sha256':data['content_sha256'],
            'scope':'complete fixed support/edge-ratio domain; local stars, exact rational incidence and necessary angle cycles only'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source',nargs='?',type=Path,default=Path(__file__).parent/'runs/mixed-obtuse-2026-10-24',help='catalogue JSON or preflight run directory')
    parser.add_argument('--replay',action='store_true',help='regenerate into a temporary directory and compare stable hashes')
    args = parser.parse_args()
    result = verify_preflight(args.source) if args.source.is_dir() else verify_catalogue(json.loads(args.source.read_text()))
    if args.replay:
        require(args.source.is_dir(),'preflight replay requires a run directory')
        from .mixed_angles import run_preflight
        retained = json.loads((args.source/'preflight.json').read_text())
        with tempfile.TemporaryDirectory(prefix='arisearch-mixed-replay-') as directory:
            replayed = run_preflight(directory,cpu_cap=retained['cpu_cap_seconds'])
            require(replayed['content_sha256'] == retained['content_sha256'],'fresh mixed replay content differs')
            require(replayed['scale_audit_sha256'] == retained['scale_audit_sha256'],'fresh exact scale audit differs')
            require(replayed['catalogue_content_sha256'] == retained['catalogue_content_sha256'],'fresh support catalogue differs')
        result['fresh_replay'] = True
    print(json.dumps(result,sort_keys=True))


if __name__ == '__main__':
    main()
