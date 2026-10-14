"""Exact periodic carrier attempt using only half-turn S bridges."""
from sage.all import matrix,vector,QQ,AA
import runpy,sys,io,contextlib,json
argv=sys.argv[:];sys.argv=["research/searches/contact-structure-one-private-x2u-ring-extension.py"]
with contextlib.redirect_stdout(io.StringIO()):d=runpy.run_path(sys.argv[0])
sys.argv=argv
raw=d["d"];K=d["K"];base=d["base"];maps=d["maps"];H=vector(K,[raw["H"],0])
U=maps[1][1]-maps[6][1]
M,b=maps[2];N,a=maps[3];G=M*N.inverse();assert G==-matrix.identity(K,2)
V=b-G*a-H
L=matrix(K,[[U[0],V[0]],[U[1],V[1]]]);assert L.det()!=0
def integral(v):return all(z in QQ and z.denominator()==1 for z in v)
def equivalent(F,G):
 for p in F:
  shift=vector(K,p)-vector(K,G[0])
  if integral(L.inverse()*shift) and frozenset(F)==frozenset(tuple(vector(K,q)+shift) for q in G):return True
 return False
seed=list(base)+[{"species":T["species"],"mode":T["mode"],"vertices":tuple(tuple(H-vector(K,z)) for z in T["vertices"])} for T in base]
events,failure=raw["patch_check"](base);assert not failure
for guest,host,corner,side in events:seed.append(raw["complete_cap"](base[guest]))
reps=[]
for T in seed:
 if not any(equivalent(T["vertices"],S["vertices"]) for S in reps):reps.append(T)
assert [T["species"] for T in reps].count("Q")==2 and len(reps)==8
segments={}
for i,T in enumerate(reps):
 F=list(T["vertices"]);F=F if AA(raw["area"](tuple(F)))>0 else list(reversed(F))
 k=0
 for p,q in raw["edges"](tuple(F)):
  diff=raw["sub"](q,p)
  points=[p,q] if raw["dot"](diff,diff)!=1 else[p,raw["scale"](K(1)/2,raw["add"](p,q)),q]
  for first,last in zip(points,points[1:]):segments[i,k]=(first,last);k+=1
partners={};unpaired=[]
for name,(p,q) in segments.items():
 candidates=[]
 for other,(s,t) in segments.items():
  shift=vector(K,p)-vector(K,t)
  if vector(K,q)-vector(K,s)==shift and integral(L.inverse()*shift):candidates.append((other,tuple(L.inverse()*shift)))
 if len(candidates)!=1:unpaired.append((name,candidates))
 else:partners[name]=candidates[0]
assert len(segments)==56
total=sum(abs(raw["area"](T["vertices"])) for T in reps)
assert AA(L.det())!=0
assert not unpaired and total==abs(L.det())
for name,(other,shift) in partners.items():assert partners[other]==(name,tuple(-z for z in shift))
result={"status":"PASS","scope":"one exact hosted x=2u metric ray; genuine entire-plane periodic carrier, sixP/twoQ, allowed partial contacts","field":raw["result"]["field"],"software":raw["result"]["software"],"field_polynomial_coefficients":[1,0,-8,0,8],"field_isolating_interval":["9/10","1"],"native_lengths":raw["result"]["lengths"],"canonical_polygons":{"P":[[str(z) for z in p] for p in raw["P"]],"Q":[[str(z) for z in p] for p in raw["Q"]]},"U":[str(z) for z in U],"V":[str(z) for z in V],"signed_covolume":str(L.det()),"representatives":[{"species":T["species"],"mode":T["mode"],"vertices":[[str(z) for z in p] for p in T["vertices"]]} for T in reps],"atomic_segment_count":len(segments),"segment_pairs":[{"segment":list(name),"partner":list(other),"lattice_shift":[int(z) for z in shift]} for name,(other,shift) in sorted(partners.items())],"area_difference":str(total-abs(L.det()))}
if len(sys.argv)==3 and sys.argv[1]=="--output":
 with open(sys.argv[2],"x") as out:json.dump(result,out,indent=2)
elif len(sys.argv)==3 and sys.argv[1]=="--check":
 with open(sys.argv[2]) as inp:assert json.load(inp)==result
elif len(sys.argv)!=1:raise SystemExit("use --output newpath or --check retainedpath")
print(json.dumps(result if len(sys.argv)==1 else {"status":"PASS","representatives":8,"atomic_segments":56,"area_difference":"0"}))
