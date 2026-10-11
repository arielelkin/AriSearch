"""Bounded concrete flat-surface gluing on a mixed four-face Cairo frequency witness."""
from pathlib import Path
from collections import defaultdict,Counter
from itertools import product
from fractions import Fraction
import json,argparse
prefix=Path(__file__).with_name("partial-contact-cairo-two-cross-residual-colors.py").read_text().split("ap=argparse.ArgumentParser()")[0]
ns={"__file__":str(Path(__file__).with_name("partial-contact-cairo-two-cross-residual-colors.py"))};exec(prefix,ns)
K=ns["K"];M=ns["M"]
ap=argparse.ArgumentParser();ap.add_argument("--scale",type=int,default=4);ap.add_argument("--output");ap.add_argument("--pattern",default="orbit7");ap.add_argument("--flat",type=int,default=12);ap.add_argument("--chamber",type=int,default=0);ap.add_argument("--allow-disconnected",action="store_true");ap.add_argument("--prune-closed",action="store_true");ap.add_argument("--max-nodes",type=int,default=0);ap.add_argument("--source",default="research/certificates/partial-contact-cairo-two-cross-residual-colors.json");a=ap.parse_args()
rec=next(z for z in json.loads(Path(a.source).read_text())["records"] if(z["pattern"],z["flat_id"],z["source_order_chamber_id"])==(a.pattern,a.flat,a.chamber))
flat={"arm_forms":rec["arm_forms"],"e_forms":rec["e_forms"]};ch={"sample_kernel_point":rec["sample_kernel_point"]}
raw,edges,corners,oriented,stars,*_=M(flat,ch)
faces=[];which=[];directions=(0,3,5,8,10)
for key,mass in rec["seam_balance"]["variant_frequencies"].items():
 count=Fraction(mass)*a.scale;assert count.denominator==1
 for repeat in range(count.numerator):which.append(int(key));faces.append(raw[int(key)][2])
assert len(faces)==a.scale
face_darts=[];dart_face=[];angles=[];colors=[];edge_ids=[];native_dirs=[]
for fid,cs in enumerate(faces):
 block=[]
 for c in cs:
  block.append(len(angles));angle,prev,nxt=corners[c];angles.append(angle);colors.append(edges[nxt][1]);edge_ids.append(nxt);dart_face.append(fid);native_dirs.append(directions[edges[nxt][0][1]])
 face_darts.append(block)
next_dart={i:block[(j+1)%len(block)] for block in face_darts for j,i in enumerate(block)}
groups=defaultdict(list)
for i,color in enumerate(colors):groups[color].append(i)
print("DOMAIN",len(faces),"faces",len(angles),"atomicdarts",sorted(len(z) for z in groups.values()),"variants",which,flush=True)
if any(len(z)%2 for z in groups.values()):
 result={"scope":"bounded copied exact variant frequency at fixedscale only; no global implication","source_pattern":a.pattern,"source_flat_id":a.flat,"source_order_chamber_id":a.chamber,"face_count":len(faces),"variants":which,"result":"bounded-parity-obstruction","odd_piece_classes":[{"color":[c[0],[str(t) for t in c[1]]],"darts":v} for c,v in groups.items() if len(v)%2]}
 if a.output:Path(a.output).write_text(json.dumps(result,indent=2)+"\n")
 raise SystemExit(0)
N=len(angles);nodes=0;completed=0;answer=None;cutoff=False
previous_dart={j:i for i,j in next_dart.items()}
parent=list(range(N));weight=angles[:];has120=[z==120 for z in angles];hasother=[z!=120 for z in angles]
def find(i,p):
 while p[i]!=i:i=p[i]
 return i
def union(i,j,p,w,h,t):
 i,j=find(i,p),find(j,p)
 if i==j:return True
 if w[i]+w[j]>360 or ((h[i] or h[j]) and(t[i] or t[j])):return False
 p[j]=i;w[i]+=w[j];h[i]|=h[j];t[i]|=t[j];return True
def search(unpaired,p,w,h,t,pairs):
 global nodes,completed,answer,cutoff
 nodes+=1
 if a.max_nodes and nodes>a.max_nodes:cutoff=True;return False
 if a.prune_closed:
  ports=Counter()
  for corner in range(N):ports[find(corner,p)]+=int(corner in unpaired)+int(previous_dart[corner] in unpaired)
  if any(ports[i]==0 and w[i]!=360 for i in range(N) if p[i]==i):return False
 if not unpaired:
  completed+=1
  if any(w[i]!=360 for i in range(N) if p[i]==i):return False
  graph=[set() for z in faces]
  for i,j,same in pairs:graph[dart_face[i]].add(dart_face[j]);graph[dart_face[j]].add(dart_face[i])
  seen={0};queue=[0]
  for z in queue:
   for y in graph[z]-seen:seen.add(y);queue.append(y)
  if len(seen)!=len(faces) and not a.allow_disconnected:return False
  answer=pairs;return True
 i=min(unpaired,key=lambda k:(sum(j in unpaired for j in groups[colors[k]]),k))
 for j in groups[colors[i]]:
  if cutoff:return False
  if j<=i or j not in unpaired:continue
  for same in(False,True):
   pp,ww,hh,tt=p[:],w[:],h[:],t[:]
   ends=((i,j),(next_dart[i],next_dart[j])) if same else((i,next_dart[j]),(next_dart[i],j))
   if not all(union(x,y,pp,ww,hh,tt) for x,y in ends):continue
   if search(unpaired-{i,j},pp,ww,hh,tt,pairs+[(i,j,int(same))]):return True
 return False
sat=search(set(range(N)),parent,weight,has120,hasother,[])
print("RESULT",sat,"nodes",nodes,"completepairings",completed,flush=True)
result={"scope":"bounded matching of copied exactmixed variants, all nativepart lengths and 360vertexlinks; existence not inferred fromfrequency","face_count":len(faces),"variants":which,"variant_native_types":[raw[k][0] for k in which],"native_corner_ids":faces,"dart_face":dart_face,"angles":angles,"edge_ids":edge_ids,"native_direction_labels":native_dirs,"edge_colors":[[c[0],[str(t) for t in c[1]]] for c in colors],"next_dart":[next_dart[i] for i in range(N)],"result":"witness" if sat else "resource-limit" if cutoff else "bounded-domain-exhausted","resource_node_bound":a.max_nodes,"prune_closed_vertex_links":a.prune_closed,"nodes":nodes,"complete_pairings_tested":completed,"edge_pairs":answer,"source_pattern":a.pattern,"source_flat_id":a.flat,"source_order_chamber_id":a.chamber,"arm_forms":rec["arm_forms"],"e_forms":rec["e_forms"]}
if a.output:Path(a.output).write_text(json.dumps(result,indent=2)+"\n")
