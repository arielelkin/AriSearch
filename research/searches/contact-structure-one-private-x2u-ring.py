"""Exact one-private dimer kernel ray and full Q-neighbor census with T allowed.
Replay: mise exec -- conda run --no-capture-output -n arisearch python this.py --check certificate.json
Only 32 stated full-side Q rings plus their uniquely mandatory P flat-cap guests.
No finite patch is promoted to a plane tiling.
"""
from sage.all import QQ,AA,NumberField,PolynomialRing,vector,matrix
from sage.env import SAGE_VERSION
from itertools import product
import json,sys
poly=PolynomialRing(QQ,"z");z=poly.gen()
K=NumberField(8*z**4-8*z**2+1,"c",embedding=((2+AA(2).sqrt())/4).sqrt())
c=K.gen();r=4*c*c-2;t=r/(4*c)
x=K(1);u=K(1)/2
y=(r+2*c-t-1)/(2*c+t+1/r)
v=u+r*c*(1-y)
w=1+(c+1/r)*(y-1)
H=y-(u+v-y-1)/r
assert all(AA(a)>0 for a in(x,y,u,v,w,H))
assert len(set((x,y,u,v,w,H)))==6
assert x==2*u and x!=2*v and all(a not in(2*u,2*v) for a in(y,w))
assert (u-v)/r==c*(y-x) and w==(u+v)/r-t*(x+y)
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def sub(a,b):return(a[0]-b[0],a[1]-b[1])
def scale(s,a):return(s*a[0],s*a[1])
def dot(a,b):return a[0]*b[0]+a[1]*b[1]
def det(a,b):return a[0]*b[1]-a[1]*b[0]
def edges(p):return list(zip(p,p[1:]+p[:1]))
def area(p):return sum(det(a,b) for a,b in edges(p))/2
def key(p):return frozenset(p)
def convex(p):
    for i,(a,b) in enumerate(edges(p)):
        for j,q in enumerate(p):
            if j not in(i,(i+1)%len(p)):assert AA(det(sub(b,a),sub(q,a)))>0
def disjoint(p,q):
    for a,b in edges(p)+edges(q):
        e=sub(b,a);n=(-e[1],e[0]);pp=[dot(z,n) for z in p];qq=[dot(z,n) for z in q]
        if AA(max(pp,key=AA))<=AA(min(qq,key=AA)) or AA(max(qq,key=AA))<=AA(min(pp,key=AA)):return True
    return False
A=(K(0),-w);B=(x*c,-w-x*t);C=add(B,(u/r,u/r));D=add(C,(-v/r,v/r))
E=add(D,(-y*c,-y*t));assert E==(0,0)
P=(A,B,C,D,E);convex(P)
lengths=(H,u,x,y,y,x,w,v)
directions=((1,0),(1/r,1/r),(0,1),(-1/r,1/r),(-1,0),(-1/r,-1/r),(0,-1),(1/r,-1/r))
Q=[(K(0),K(0))]
for length,direction in zip(lengths[:-1],directions[:-1]):Q.append(add(Q[-1],scale(length,direction)))
Q=tuple(Q);assert add(Q[-1],scale(lengths[-1],directions[-1]))==Q[0];convex(Q)
# Four exact closure equations plus x=2u have a unique kernel ray.
variables=("x","y","u","v","w","H");vi={name:i for i,name in enumerate(variables)}
rows=[[c,-c,1/r,-1/r,0,0],[-t,-t,1/r,1/r,-1,0]]
word=("H","u","x","y","y","x","w","v")
for coordinate in(0,1):
    row=[K(0)]*6
    for i,name in enumerate(word):row[vi[name]]+=directions[i][coordinate]
    rows.append(row)
rows.append([1,0,-2,0,0,0])
closure=matrix(K,rows)
assert closure.rank()==5 and closure*vector(K,[x,y,u,v,w,H])==vector(K,[0]*5)

def tile(species,mode,vertices):return {"species":species,"mode":mode,"vertices":vertices}
centre=tile("Q","Q",Q)
def attachments(edge_index,left,right):
    a,b=edges(P)[edge_index];source=sub(b,a);images={}
    for first,last in((left,right),(right,left)):
        target=sub(last,first);normal=(-target[1],target[0])
        assert dot(source,source)==dot(target,target)
        for sign in(-1,1):
            image=tuple(add(first,add(scale(dot(sub(z,a),source)/dot(source,source),target),
                                     scale(sign*det(source,sub(z,a))/dot(source,source),normal))) for z in P)
            if disjoint(Q,image):images.setdefault(key(image),image)
    assert len(images)==2
    return list(images.values())
options=[]
for i,(left,right) in enumerate(edges(Q)):
    if i==0:
        image=tuple(sub(add(left,right),z) for z in Q)
        assert disjoint(Q,image)
        candidates=[tile("Q","Q",image)]
    else:
        edge_index={u:1,v:2,x:0,y:3,w:4}[lengths[i]]
        raw=attachments(edge_index,left,right)
        if lengths[i] in(u,v):
            target=left if(i-1)%8==0 else right
            raw=[p for p in raw if p[2]==target]
        mode="S" if lengths[i] in(x,y) else "R"
        candidates=[tile("P",mode,p) for p in raw]
    options.append(candidates)
assert [len(o) for o in options]==[1,1,2,2,2,2,2,1]

full_stars=((4,4,4,4),(5,5,6),(4,6,6))
def partial_events(tiles):
    events=[]
    for gi,guest in enumerate(tiles):
        for hi,host in enumerate(tiles):
            if gi==hi:continue
            for ci,point in enumerate(guest["vertices"]):
                for si,(left,right) in enumerate(edges(host["vertices"])):
                    if det(sub(point,left),sub(right,left))!=0 or AA(dot(sub(point,left),sub(point,right)))>=0:continue
                    valid=(guest["species"]=="P" and guest["mode"]=="S" and ci==2 and
                           host["species"]=="P" and host["mode"]=="R" and si==0 and
                           point==scale(K(1)/2,add(left,right)) and
                           det(sub(guest["vertices"][1],point),sub(right,left))==0)
                    if not valid:return None,{"kind":"forbidden_partial","guest":gi,"host":hi,"corner":ci,"host_side":si}
                    events.append((gi,hi,ci,si))
    return events,None
def patch_check(tiles):
    for i,a in enumerate(tiles):
        for j,b in enumerate(tiles[:i]):
            if not disjoint(a["vertices"],b["vertices"]):return None,{"kind":"overlap","pair":[j,i]}
    events,failure=partial_events(tiles)
    if failure:return None,failure
    groups={}
    for i,a in enumerate(tiles):
        for j,point in enumerate(a["vertices"]):
            angle=6 if a["species"]=="Q" else(4 if j==2 else 5)
            groups.setdefault(point,[]).append(angle)
    for point,angles in groups.items():
        if not any(all(angles.count(a)<=star.count(a) for a in(4,5,6)) for star in full_stars):
            return None,{"kind":"impossible_native_star","angles":angles,"position":[str(z) for z in point]}
    return events,None
def complete_cap(guest):
    p=guest["vertices"];origin=p[2];axis=sub(p[3],origin)
    reflected=tuple(add(origin,sub(scale(2*dot(sub(z,origin),axis)/dot(axis,axis),axis),sub(z,origin))) for z in p)
    assert disjoint(p,reflected)
    return tile("P","S",reflected)
records=[];raw_valid=[];cap_valid=[]
for choices in product(*(range(len(o)) for o in options)):
    tiles=[centre]+[options[i][choices[i]] for i in range(8)]
    events,failure=patch_check(tiles)
    record={"choices":list(choices)}
    if failure:record.update({"status":"RING_REJECTED","failure":failure})
    else:
        raw_valid.append(list(choices))
        extended=list(tiles);seen={key(a["vertices"]):a["mode"] for a in tiles}
        collision=None
        for guest,host,corner,side in events:
            extra=complete_cap(tiles[guest]);extra_key=key(extra["vertices"])
            if extra_key in seen:
                if seen[extra_key]!="S":collision={"kind":"cap_mode_collision","mode":seen[extra_key]}
            else:
                seen[extra_key]="S";extended.append(extra)
        extra_events,extra_failure=patch_check(extended) if not collision else(None,collision)
        record["ring_T_events"]=[list(e) for e in events]
        record["mandatory_cap_added_tiles"]=len(extended)-len(tiles)
        if extra_failure:record.update({"status":"MANDATORY_CAP_REJECTED","failure":extra_failure})
        else:
            record["status"]="NECESSARY_PATCH_SURVIVES"
            cap_valid.append(list(choices))
    records.append(record)
assert len(records)==32
result={"domain":"one exact x=2u hosted-dimer kernel ray, all32fullQside-neighbor rings; all mandatory P cap guests for base-ring flat events",
        "field":"c root8c^4-8c^2+1,9/10<c<1,r=4c^2-2,t=r/(4c)",
        "software":{"sage":SAGE_VERSION,"python":sys.version.split()[0]},
        "word":list(word),"lengths":{name:str(a) for name,a in zip(variables,(x,y,u,v,w,H))},
        "closure_rank":5,"only_permitted_host_equation":"x=2u",
        "option_counts":[len(o) for o in options],"rings_tested":32,
        "raw_valid_rings":raw_valid,"mandatory_cap_valid_rings":cap_valid,"records":records,
        "scope":"necessary finite patches only; no plane existence or aperiodicity inferred from survival"}
if len(sys.argv)==3 and sys.argv[1]=="--output":
    with open(sys.argv[2],"x") as out:json.dump(result,out,indent=2)
elif len(sys.argv)==3 and sys.argv[1]=="--check":
    with open(sys.argv[2]) as inp:assert json.load(inp)==result
elif len(sys.argv)!=1:raise SystemExit("use --output newpath or --check retainedpath")
summary={"status":"COMPLETE","rings_tested":32,"raw_valid_rings":raw_valid,"mandatory_cap_valid_rings":cap_valid,"lengths":result["lengths"]}
print(json.dumps(result if len(sys.argv)==1 else summary))
