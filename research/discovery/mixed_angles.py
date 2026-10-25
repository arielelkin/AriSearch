"""Exact bounded strictly-obtuse pentagon/heptagon support catalogue.

The field is Q(sqrt(2),sqrt(3)), with exact coefficients in that order.
Supporting normals occupy 24 directions. No integer-edge restriction is used.
This module performs catalogue/contact preflight only, not patch growth.
"""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
from time import perf_counter, process_time

from sage.all import AA, NumberField, PolynomialRing, QQ

R=PolynomialRing(QQ,"z")
z=R.gen()
K=NumberField(z**4-10*z**2+1,"t",embedding=AA(2).sqrt()+AA(3).sqrt())
t=K.gen()
SQRT2=(t**3-9*t)/2
SQRT3=(11*t-t**3)/2
SQRT6=(t*t-5)/2
ZERO=K(0)
ONE=K(1)


def encode(value):
    """Four rational coefficient pairs in basis(1,sqrt2,sqrt3,sqrt6)."""
    cs=list(K(value).list())+[QQ(0)]*4
    coefficients=(cs[0]+5*cs[2],cs[1]+11*cs[3],cs[1]+9*cs[3],2*cs[2])
    return [[int(c.numerator()),int(c.denominator())] for c in coefficients]


def decode(data):
    if len(data)!=4:
        raise ValueError("field data needs four rational coefficients")
    return sum((QQ(a)/QQ(b))*u for (a,b),u in zip(data,(ONE,SQRT2,SQRT3,SQRT6)))


def field_key(value):
    return tuple(tuple(c) for c in encode(value))


@lru_cache(None)
def sign(value):
    value=K(value)
    return 0 if value==0 else (1 if AA(value)>0 else -1)


C15=(SQRT6+SQRT2)/4
S15=(SQRT6-SQRT2)/4
NORMALS=[(ONE,ZERO)]
for _ in range(23):
    x,y=NORMALS[-1]
    NORMALS.append((x*C15-y*S15,x*S15+y*C15))
NORMALS=tuple(NORMALS)


def dot(a,b):
    return a[0]*b[0]+a[1]*b[1]


def cross(a,b):
    return a[0]*b[1]-a[1]*b[0]


def sub(a,b):
    return (a[0]-b[0],a[1]-b[1])


def cyclic_words(word):
    word=tuple(word)
    return tuple(sorted({s[i:]+s[:i] for s in (word,word[::-1]) for i in range(len(word))}))


def canonical_angles(word):
    return min(cyclic_words(word))


def angle_words(multiset):
    """Unique multiset permutations modulo cyclic rotation and reflection."""
    counts={a:multiset.count(a) for a in set(multiset)}
    found=set()
    def visit(prefix):
        if len(prefix)==len(multiset):
            found.add(canonical_angles(prefix))
            return
        for a in sorted(counts):
            if counts[a]:
                counts[a]-=1
                visit(prefix+(a,))
                counts[a]+=1
    visit(())
    return tuple(sorted(found))


P_ANGLES=(105,105,105,105,120)
Q_MULTISETS=((120,120,120,135,135,135,135),
             (120,120,120,120,135,135,150),
             (120,120,120,120,120,150,150))
Q_ANGLES=tuple(sorted({w for m in Q_MULTISETS for w in angle_words(m)}))


def normal_indices(angles):
    angles=tuple(angles)
    if sum(angles)!=(len(angles)-2)*180 or any(a<=90 or a>=180 or a%15 for a in angles):
        raise ValueError("invalid strictly-obtuse15-degree angle word")
    result=[0]
    for angle in angles[1:]:
        result.append((result[-1]+(180-angle)//15)%24)
    return tuple(result)


def support_polygon(angles, offsets):
    """Return exact CCW native vertices, or None when a side is inactive/zero."""
    angles,offsets=tuple(angles),tuple(map(K,offsets))
    if len(angles)!=len(offsets) or any(sign(h)<=0 for h in offsets):
        raise ValueError("positive support offset required for each side")
    ns=tuple(NORMALS[i] for i in normal_indices(angles))
    vertices=[]
    for i,b in enumerate(ns):
        a=ns[i-1]
        det=cross(a,b)
        if sign(det)<=0:
            return None
        ha,hb=offsets[i-1],offsets[i]
        vertices.append(((ha*b[1]-a[1]*hb)/det,(a[0]*hb-ha*b[0])/det))
    for i,n in enumerate(ns):
        for j,v in enumerate(vertices):
            slack=offsets[i]-dot(n,v)
            if j in (i,(i+1)%len(vertices)):
                assert slack==0
            elif sign(slack)<=0:
                return None
    return tuple(vertices)


def edge_lengths(poly, angles):
    return tuple(dot(sub(poly[(i+1)%len(poly)],poly[i]),(-NORMALS[j][1],NORMALS[j][0]))
                 for i,j in enumerate(normal_indices(angles)))


def polygon_signature(poly, scale=ONE):
    n=len(poly)
    words=[]
    for seq in (tuple(poly),tuple(poly)[::-1]):
        for start in range(n):
            ordered=seq[start:]+seq[:start]
            words.append(tuple(field_key(dot(sub(a,b),sub(a,b))*scale*scale)
                               for a in ordered for b in ordered))
    return (n,min(words))


def encode_points(poly):
    return [[encode(x),encode(y)] for x,y in poly]


@dataclass(frozen=True)
class MixedTile:
    id: str
    species: str
    angles: tuple
    offsets: tuple
    polygon: tuple
    lengths: tuple
    signature: tuple
    defining_data: tuple

    def to_dict(self):
        return {"id":self.id,"species":self.species,"angles":list(self.angles),
                "offsets":list(self.offsets),"normal_indices":list(normal_indices(self.angles)),
                "polygon":encode_points(self.polygon),"lengths":[encode(x) for x in self.lengths],
                "signature":self.signature,
                "defining_data":[{"angles":list(a),"offsets":list(h)} for a,h in self.defining_data]}


def enumerate_catalogue():
    """Complete fixed offset domain; preserve actual scales and all definitions."""
    started=perf_counter()
    grouped={}
    stats={"P_angle_words":1,"Q_angle_words":len(Q_ANGLES),"attempted":0,"inactive_or_zero":0,
           "by_angle_word":[]}
    for species,angle_list in (("P",(P_ANGLES,)),("Q",Q_ANGLES)):
        for angles in angle_list:
            attempted=valid=0
            signatures=set()
            for offsets in product((1,2),repeat=len(angles)):
                attempted+=1
                poly=support_polygon(angles,offsets)
                if poly is None:
                    continue
                valid+=1
                lengths=edge_lengths(poly,angles)
                assert all(sign(x)>0 for x in lengths)
                signature=polygon_signature(poly)
                signatures.add(signature)
                if signature not in grouped:
                    grouped[signature]=[species,angles,offsets,poly,lengths,[]]
                grouped[signature][-1].append((angles,offsets))
            stats["attempted"]+=attempted
            stats["inactive_or_zero"]+=attempted-valid
            stats["by_angle_word"].append({"species":species,"angles":list(angles),
                "attempted":attempted,"valid_definitions":valid,"congruence_classes":len(signatures)})
    tiles=[]
    for signature,(species,angles,offsets,poly,lengths,defs) in grouped.items():
        digest=sha256(json.dumps(signature,separators=(",",":")).encode()).hexdigest()[:16]
        tiles.append(MixedTile(species.lower()+str(len(angles))+"-"+digest,species,angles,offsets,poly,lengths,signature,tuple(defs)))
    tiles=tuple(sorted(tiles,key=lambda tile:(tile.species,tile.angles,tile.id)))
    stats.update({"P_tiles":sum(t.species=="P" for t in tiles),
                  "Q_tiles":sum(t.species=="Q" for t in tiles),"elapsed_seconds":perf_counter()-started})
    return tiles,stats


def stable_content_hash(value):
    """Hash mathematical/configuration content, excluding elapsed timing."""
    def scrub(obj):
        if isinstance(obj,dict):
            return {k:scrub(v) for k,v in obj.items()
                    if k not in ("elapsed_seconds","cpu_seconds","wall_seconds","content_sha256")}
        if isinstance(obj,(list,tuple)):
            return [scrub(v) for v in obj]
        return obj
    return sha256(json.dumps(scrub(value),sort_keys=True,separators=(",",":")).encode()).hexdigest()


def write_catalogue(destination):
    tiles,stats=enumerate_catalogue()
    destination=Path(destination)
    destination.mkdir(parents=True,exist_ok=True)
    data={"schema":"mixed-obtuse-support-v1",
        "field_basis":["1","sqrt(2)","sqrt(3)","sqrt(6)"],
        "support_domain":[1,2],"tiles":[t.to_dict() for t in tiles],"stats":stats}
    data["content_sha256"]=stable_content_hash(data)
    (destination/"catalogue.json").write_text(json.dumps(data,indent=2)+"\n")
    return tiles,stats


@dataclass(frozen=True)
class CornerState:
    native_index: int
    angle: int
    start_length: object
    end_length: object
    reflected: bool


def corner_states(p, q, q_scale):
    result=[]
    for tile,scale,base in ((p,ONE,0),(q,q_scale,len(p.angles))):
        for i,angle in enumerate(tile.angles):
            outgoing,previous=tile.lengths[i]*scale,tile.lengths[i-1]*scale
            result.append(CornerState(base+i,angle,outgoing,previous,False))
            if outgoing!=previous:
                result.append(CornerState(base+i,angle,previous,outgoing,True))
    return tuple(result)


def compatible_stars(p,q,q_scale):
    """Every exact matched three-corner star, modulo incidence multiplicity.

    Each value retains an ordered geometric realization; keys are multisets
    of native corner identities. Equal incident lengths retain loop corners.
    Reflections exchange the start/end rays and are always permitted.
    """
    cs=corner_states(p,q,q_scale)
    by_start={}
    by_pattern={}
    for c in cs:
        by_start.setdefault(c.start_length,[]).append(c)
        by_pattern.setdefault((c.angle,c.start_length,c.end_length),[]).append(c)
    found={}
    for a in cs:
        for b in by_start.get(a.end_length,()):
            target=360-a.angle-b.angle
            if target<=90 or target>=180:
                continue
            for c in by_pattern.get((target,b.end_length,a.start_length),()):
                key=tuple(sorted((a.native_index,b.native_index,c.native_index)))
                found.setdefault(key,(a,b,c))
    return found


def place_corner(tile,index,reflected,heading,scale=ONE):
    """Place a corner at0 with its interior in a CCW sector of given heading."""
    origin=tile.polygon[index]
    chosen=tile.polygon[(index-1 if reflected else index+1)%len(tile.polygon)]
    ray=sub(chosen,origin)
    ray_length=tile.lengths[index-1 if reflected else index]
    if reflected:
        ray=(ray[0],-ray[1])
    unit=(ray[0]/ray_length,ray[1]/ray_length)
    target=NORMALS[heading%24]
    co,si=dot(unit,target),cross(unit,target)
    placed=[]
    for v in tile.polygon:
        x,y=sub(v,origin)
        if reflected:
            y=-y
        placed.append((scale*(co*x-si*y),scale*(si*x+co*y)))
    return tuple(placed)


def positive_polygon_overlap(a,b):
    """Exact separating-axis test: contacts on boundary have zero area."""
    for poly in (a,b):
        for i,p in enumerate(poly):
            edge=sub(poly[(i+1)%len(poly)],p)
            normal=(-edge[1],edge[0])
            av=[dot(normal,v) for v in a]
            bv=[dot(normal,v) for v in b]
            amin=min(av,key=AA); amax=max(av,key=AA)
            bmin=min(bv,key=AA); bmax=max(bv,key=AA)
            if sign(amax-bmin)<=0 or sign(bmax-amin)<=0:
                return False
    return True


def star_geometry(p,q,q_scale,star):
    heading=0
    polys=[]
    sectors=[]
    for c in star:
        tile,index,scale=(p,c.native_index,ONE) if c.native_index<len(p.angles) else (q,c.native_index-len(p.angles),q_scale)
        poly=place_corner(tile,index,c.reflected,heading,scale)
        polys.append(poly)
        chosen=tile.polygon[(index-1 if c.reflected else index+1)%len(tile.polygon)]
        ray=sub(chosen,tile.polygon[index])
        ray_length=tile.lengths[index-1 if c.reflected else index]
        if c.reflected:
            ray=(ray[0],-ray[1])
        unit=(ray[0]/ray_length,ray[1]/ray_length)
        target=NORMALS[heading%24]
        rotation=(dot(unit,target),cross(unit,target))
        rotation_index=NORMALS.index(rotation)
        ox,oy=tile.polygon[index]
        if c.reflected:
            oy=-oy
        co,si=rotation
        translation=(-scale*(co*ox-si*oy),-scale*(si*ox+co*oy))
        sectors.append({"tile_id":tile.id,"species":tile.species,"native_corner":index,
                        "reflected":c.reflected,"scale":encode(scale),
                        "rotation_index_15deg":rotation_index,
                        "translation":[encode(x) for x in translation],
                        "start_heading_15deg":heading,"angle":c.angle})
        heading+=c.angle//15
    assert heading==24
    assert not any(positive_polygon_overlap(polys[i],polys[j]) for i in range(3) for j in range(i+1,3))
    # All shared radial edges have exactly equal endpoints, not merely lines.
    for i,c in enumerate(star):
        end_heading=sum(s.angle for s in star[:i+1])//15
        target=NORMALS[end_heading%24]
        endpoint=(target[0]*c.end_length,target[1]*c.end_length)
        assert endpoint in polys[i] and endpoint in polys[(i+1)%3]
    return {"corners":sectors,"polygons":[encode_points(poly) for poly in polys],
            "pairwise_interior_disjoint":True,"radial_native_edges_matched":True}


def incidence_relaxation(stars,p_corners=5,q_corners=7):
    """Exact rational necessary frequency relaxation; never an actual patch.

    Every native corner has demand1 per P copy and1 per Q copy. Equality
    nP=nQ follows both Euler/trivalence and the total angle equations.
    Here F=2,E=6,V=4 in normalized frequency units. Nonnegative rational
    star counts must supply all12 demands. Exact PPL solves this LP.
    """
    from sage.all import MixedIntegerLinearProgram
    from sage.numerical.mip import MIPSolverException
    keys=tuple(sorted(stars))
    lp=MixedIntegerLinearProgram(maximization=False,solver="PPL")
    x=lp.new_variable(nonnegative=True)
    for c in range(p_corners+q_corners):
        lp.add_constraint(sum(key.count(c)*x[i] for i,key in enumerate(keys))==1)
    lp.set_objective(0)
    try:
        lp.solve()
    except MIPSolverException:
        # Farkas: A^T*y>=0, 1^T*y=-1 contradicts any x>=0 with A*x=1.
        dual=MixedIntegerLinearProgram(maximization=False,solver="PPL")
        y=dual.new_variable(nonnegative=False)
        for key in keys:
            dual.add_constraint(sum(key.count(c)*y[c] for c in range(p_corners+q_corners))>=0)
        dual.add_constraint(sum(y[c] for c in range(p_corners+q_corners))==-1)
        dual.set_objective(0)
        dual.solve()
        vals=dual.get_values(y)
        witness=tuple(QQ(vals.get(c,0)) for c in range(p_corners+q_corners))
        assert sum(witness)==-1
        assert all(sum(witness[c] for c in key)>=0 for key in keys)
        return {"feasible":False,"method":"exact-rational-PPL","actual_patch":False,
                "farkas":{"native_corner_weights":[[int(v.numerator()),int(v.denominator())] for v in witness],
                          "demand_dot":-1,"all_star_column_dots_nonnegative":True}}
    values=lp.get_values(x)
    weights={i:QQ(v) for i,v in values.items() if v}
    assert all(v>=0 for v in weights.values())
    assert all(sum(keys[i].count(c)*v for i,v in weights.items())==1
               for c in range(p_corners+q_corners))
    assert sum(weights.values())==4
    return {"feasible":True,"method":"exact-rational-PPL","actual_patch":False,
            "normalized_tile_counts":{"P":1,"Q":1},"Euler":{"V":4,"E":6,"F":2},
            "weights":[{"star":list(keys[i]),"weight":[int(v.numerator()),int(v.denominator())]}
                       for i,v in sorted(weights.items())]}


def pair_scales(p,q):
    """All positive relative Q/P scales induced by any possible mixed edge."""
    return tuple(sorted({a/b for a in p.lengths for b in q.lengths},key=field_key))


def _load_tile(record):
    poly=tuple((decode(x),decode(y)) for x,y in record["polygon"])
    return MixedTile(record["id"],record["species"],tuple(record["angles"]),tuple(record["offsets"]),
                     poly,tuple(decode(x) for x in record["lengths"]),polygon_signature(poly),
                     tuple((tuple(d["angles"]),tuple(d["offsets"])) for d in record["defining_data"]))


def load_catalogue(destination):
    data=json.loads((Path(destination)/"catalogue.json").read_text())
    return tuple(_load_tile(t) for t in data["tiles"]),data["stats"]


def angle_endpoint_cycle(root_angles,p_angles,q_angles):
    """Necessary finite ANGLE-only endpoint cycle; no surrounding patch search.

    One neighboring tile occupies each root side. Its two endpoint angles
    therefore come from one native side, in either reflected reading. At
    root corner i, previous-neighbor end + root[i] + next-neighbor start
    must equal360. Edge lengths and nonlocal collisions are relaxed here.
    """
    sources={}
    for species,angles in (("P",tuple(p_angles)),("Q",tuple(q_angles))):
        for i,a in enumerate(angles):
            b=angles[(i+1)%len(angles)]
            for reflected,pair in ((False,(b,a)),(True,(a,b))):
                sources.setdefault(pair,[]).append({"species":species,"edge":i,"reflected":reflected})
    options=tuple(sorted(sources))
    trials=[]
    total=0
    witness=None
    for first in options:
        reachable={first:1}
        paths={first:(first,)}
        layers=[[[*first],1]]
        layer_records=[{"edge":0,"states_and_counts":layers}]
        for i in range(1,len(root_angles)):
            following={}
            following_paths={}
            for previous,count in reachable.items():
                for current in options:
                    if previous[1]+root_angles[i]+current[0]==360:
                        following[current]=following.get(current,0)+count
                        following_paths.setdefault(current,paths[previous]+(current,))
            reachable,paths=following,following_paths
            layer_records.append({"edge":i,"states_and_counts":[[list(k),v] for k,v in sorted(reachable.items())]})
        closing=[state for state in reachable if state[1]+root_angles[0]+first[0]==360]
        cycle_count=sum(reachable[state] for state in closing)
        total+=cycle_count
        if closing and witness is None:
            witness=[list(pair) for pair in paths[closing[0]]]
        trials.append({"first_state":list(first),"layers":layer_records,
                       "closing_states":[list(state) for state in closing],"cycle_count":cycle_count})
    return {"feasible":total>0,"angle_state_cycle_count":total,"root_angles":list(root_angles),
            "endpoint_options":[{"angles":list(pair),"native_sources":sources[pair]} for pair in options],
            "trials":trials,"witness_cycle":witness,
            "necessary_only":True,"edge_lengths_relaxed":True,"actual_patch":False}


def run_preflight(destination, cpu_cap=540):
    """Exhaust the fixed library/scales, or explicitly retain a capped prefix.

    Scale audit rows retain every native pair/scale and any common-scaling
    mapping to a representative. Only complete contact, incidence and angular
    endpoint-cycle survivors count toward the heuristic10pair/3Q-word gate.
    """
    import gzip
    destination=Path(destination)
    destination.mkdir(parents=True,exist_ok=True)
    cpu_started=process_time(); wall_started=perf_counter()
    if (destination/"catalogue.json").exists():
        tiles,catalogue_stats=load_catalogue(destination)
    else:
        tiles,catalogue_stats=write_catalogue(destination)
    ps=[t for t in tiles if t.species=="P"]
    qs=[t for t in tiles if t.species=="Q"]
    bases={t.id:min(t.lengths,key=AA) for t in tiles}
    normalized={t.id:polygon_signature(t.polygon,1/bases[t.id]) for t in tiles}
    seen={}
    counts={"native_tile_pairs":len(ps)*len(qs),"native_pair_scales":0,
            "common_scale_duplicates":0,"unique_pair_scales":0,
            "missing_native_corner_support":0,"geometry_checked_pair_scales":0,
            "geometry_checked_stars":0,"incidence_infeasible":0,"incidence_feasible":0,
            "angular_endpoint_cycle_infeasible":0,"strong_survivors":0}
    survivors=[]
    incidence_survivors=[]
    corner_supported=[]
    angle_cycles={angles:{"P":angle_endpoint_cycle(P_ANGLES,P_ANGLES,angles),
                          "Q":angle_endpoint_cycle(angles,P_ANGLES,angles)} for angles in Q_ANGLES}
    complete=True
    import io
    with (destination/"scale-audit.jsonl.gz").open("wb") as compressed, io.TextIOWrapper(gzip.GzipFile(filename="",fileobj=compressed,mode="wb",mtime=0)) as audit:
        for p in ps:
            if not complete:
                break
            for q in qs:
                if not complete:
                    break
                for ratio in pair_scales(p,q):
                    if process_time()-cpu_started>cpu_cap:
                        complete=False
                        break
                    counts["native_pair_scales"]+=1
                    key=(normalized[p.id],normalized[q.id],field_key(ratio*bases[q.id]/bases[p.id]))
                    row={"P":p.id,"Q":q.id,"Q_scale":encode(ratio)}
                    if key in seen:
                        rep=seen[key]
                        counts["common_scale_duplicates"]+=1
                        row.update({"status":"common-scaling-duplicate","representative":rep["id"],
                                    "common_scale_to_representative":encode(rep["P_base"]/bases[p.id])})
                        audit.write(json.dumps(row,separators=(",",":"))+"\n")
                        continue
                    counts["unique_pair_scales"]+=1
                    identifier="mix-"+sha256(json.dumps((p.id,q.id,encode(ratio)),separators=(",",":")).encode()).hexdigest()[:16]
                    seen[key]={"id":identifier,"P_base":bases[p.id]}
                    row["id"]=identifier
                    stars=compatible_stars(p,q,ratio)
                    covered={c for key in stars for c in key}
                    if len(covered)!=12:
                        counts["missing_native_corner_support"]+=1
                        row.update({"status":"missing-native-corner-support","missing_corners":sorted(set(range(12))-covered),
                                    "incidence_star_count":len(stars)})
                        audit.write(json.dumps(row,separators=(",",":"))+"\n")
                        continue
                    geometries=[]
                    for star_key in sorted(stars):
                        geometries.append({"native_corner_multiset":list(star_key),
                                           **star_geometry(p,q,ratio,stars[star_key])})
                    counts["geometry_checked_pair_scales"]+=1
                    counts["geometry_checked_stars"]+=len(geometries)
                    relaxation=incidence_relaxation(stars)
                    row.update({"status":"strong-survivor" if relaxation["feasible"] else "incidence-infeasible",
                                "incidence_star_count":len(stars)})
                    supported_record={**row,"Q_angle_word":list(q.angles),"native_corner_support_complete":True,
                                      "stars":geometries,"incidence_relaxation":relaxation}
                    corner_supported.append(supported_record)
                    if not relaxation["feasible"]:
                        counts["incidence_infeasible"]+=1
                    else:
                        counts["incidence_feasible"]+=1
                        cycle=angle_cycles[q.angles]
                        supported_record["angular_endpoint_cycle"]={"P_feasible":cycle["P"]["feasible"],
                            "Q_feasible":cycle["Q"]["feasible"],"proof_Q_angle_word":list(q.angles)}
                        incidence_survivors.append(supported_record)
                        if not (cycle["P"]["feasible"] and cycle["Q"]["feasible"]):
                            counts["angular_endpoint_cycle_infeasible"]+=1
                            row["status"]="angular-endpoint-cycle-infeasible"
                            supported_record["status"]=row["status"]
                        else:
                            counts["strong_survivors"]+=1
                            survivors.append(supported_record)
                    audit.write(json.dumps(row,separators=(",",":"))+"\n")
    q_words={tuple(row["Q_angle_word"]) for row in survivors}
    passed=complete and len(survivors)>=10 and len(q_words)>=3
    result={"schema":"mixed-obtuse-preflight-v1","complete":complete,"cpu_cap_seconds":cpu_cap,
            "cpu_seconds":process_time()-cpu_started,"wall_seconds":perf_counter()-wall_started,
            "catalogue_stats":catalogue_stats,"funnel":counts,"strong_survivors":survivors,
            "corner_supported_pairs":corner_supported,"incidence_survivors":incidence_survivors,
            "angle_endpoint_cycle_audit":[{"Q_angle_word":list(word),**angle_cycles[word]} for word in Q_ANGLES],
            "allocation_gate":{"minimum_pairs":10,"minimum_Q_angle_words":3,
                "actual_pairs":len(survivors),"actual_Q_angle_words":len(q_words),"passed":passed,
                "heuristic_only":True},
            "source_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
            "scale_audit_sha256":sha256((destination/"scale-audit.jsonl.gz").read_bytes()).hexdigest(),
            "catalogue_content_sha256":stable_content_hash(json.loads((destination/"catalogue.json").read_text())),
            "scope":"Exact finite support/relative-scale/contact/incidence preflight; no global tileability or novelty claim; no growth engine."}
    result["content_sha256"]=stable_content_hash(result)
    (destination/"preflight.json").write_text(json.dumps(result,indent=2)+"\n")
    write_gallery(destination,tiles,survivors)
    return result


def write_gallery(destination,tiles,survivors):
    """Static SVG catalogue sample with exact identities in embedded labels."""
    selected=[]
    ids={r[k] for r in survivors for k in ("P","Q")}
    if ids:
        selected=[t for t in tiles if t.id in ids][:24]
    else:
        ptiles=[t for t in tiles if t.species=="P"]
        selected=ptiles[:3]
        for word in Q_ANGLES:
            candidate=next((t for t in tiles if t.species=="Q" and t.angles==word),None)
            if candidate:
                selected.append(candidate)
    import html
    cols=4; rows=(len(selected)+cols-1)//cols
    out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="{60+rows*230}" viewBox="0 0 1000 {60+rows*230}">',
         '<rect width="100%" height="100%" fill="#f8f8f4"/>',
         '<text x="20" y="28" font-family="sans-serif" font-size="18">Mixed obtuse catalogue: exact finite support preflight</text>',
         f'<text x="20" y="49" font-family="sans-serif" font-size="12">{len(survivors)} strong contact/incidence survivors; drawings approximate exact retained coordinates</text>']
    for i,tile in enumerate(selected):
        coords=[(float(AA(x)),float(AA(y))) for x,y in tile.polygon]
        xs=[x for x,y in coords]; ys=[y for x,y in coords]
        factor=min(170/(max(xs)-min(xs)),150/(max(ys)-min(ys)))
        cx=(max(xs)+min(xs))/2; cy=(max(ys)+min(ys))/2
        x0=125+(i%cols)*250; y0=150+(i//cols)*230
        points=" ".join(f"{x0+(x-cx)*factor:.3f},{y0-(y-cy)*factor:.3f}" for x,y in coords)
        out.append(f'<polygon points="{points}" fill="{"#c4dae8" if tile.species=="P" else "#ead4b3"}" stroke="#253342" stroke-width="1.5"/>')
        out.append(f'<text x="{x0-115}" y="{y0+95}" font-family="monospace" font-size="10">{html.escape(tile.id)}</text>')
        out.append(f'<text x="{x0-115}" y="{y0+111}" font-family="sans-serif" font-size="9">{",".join(map(str,tile.angles))}</text>')
    out.append('</svg>')
    (Path(destination)/"gallery.svg").write_text("\n".join(out)+"\n")


if __name__=="__main__":
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",default="research/discovery/runs/mixed-obtuse-2026-10-24")
    parser.add_argument("--cpu-cap",type=float,default=540)
    parser.add_argument("--catalogue-only",action="store_true")
    args=parser.parse_args()
    if args.catalogue_only:
        _,stats=write_catalogue(args.output)
        print(json.dumps(stats,indent=2))
    else:
        answer=run_preflight(args.output,args.cpu_cap)
        print(json.dumps({k:answer[k] for k in ("complete","cpu_seconds","funnel","allocation_gate")},indent=2))
