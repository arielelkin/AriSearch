"""Exact necessary neighboring-Q-ring extension of the hosted dimer ray."""
from sage.all import matrix,vector
import runpy,sys,io,contextlib,json
argv=sys.argv[:];sys.argv=["research/searches/contact-structure-one-private-x2u-ring.py"]
with contextlib.redirect_stdout(io.StringIO()):d=runpy.run_path(sys.argv[0])
sys.argv=argv
K=d["K"];P=d["P"];Q=d["Q"];options=d["options"];choice=d["cap_valid"][0]
base=[d["centre"]]+[options[i][choice[i]] for i in range(8)]
basis=matrix(K,[[P[1][j]-P[0][j],P[2][j]-P[0][j]] for j in(0,1)])
maps={}
for i in range(1,8):
 p=options[i][choice[i]]["vertices"]
 M=matrix(K,[[p[1][j]-p[0][j],p[2][j]-p[0][j]] for j in(0,1)])*basis.inverse()
 assert M.transpose()*M==matrix.identity(K,2)
 maps[i]=(M,vector(K,p[0])-M*vector(K,P[0]))
def serialize(v):return [str(z) for z in v]
records=[]
for i in(2,3,4,5):
 for j in((3,4) if i in(2,5) else(2,5)):
  M,b=maps[i];N,a=maps[j];G=M*N.inverse();s=b-G*a
  image=[{"species":T["species"],"mode":T["mode"],"vertices":tuple(tuple(G*vector(K,z)+s) for z in T["vertices"])} for T in base]
  seen={d["key"](T["vertices"]):T for T in base};patch=list(base)
  for T in image:
   key=d["key"](T["vertices"])
   if key not in seen:seen[key]=T;patch.append(T)
   else:assert seen[key]["species"]==T["species"] and seen[key]["mode"]==T["mode"]
  events,failure=d["patch_check"](patch)
  if not failure:
   for guest,host,corner,side in events:
    extra=d["complete_cap"](patch[guest]);key=d["key"](extra["vertices"])
    if key not in seen:seen[key]=extra;patch.append(extra)
   events,failure=d["patch_check"](patch)
  records.append({"S_source_slot":i,"other_Q_native_slot":j,"linear":[serialize(row) for row in G.rows()],"offset":serialize(s),"patch_tiles":len(patch),"status":"REJECTED" if failure else "NECESSARY_PATCH_SURVIVES","failure":failure})
result={"scope":"all8 possible second-Q contacts through the four S neighbors of the unique hosted Q ring, with mandatory caps; no plane existence inferred","records":records}
print(json.dumps(result,indent=2))
