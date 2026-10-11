"""Exact geometric development of a copied-face gluing, no frequency-to-surface inference."""
from sage.all import *
from pathlib import Path
from collections import deque
import json,argparse
ap=argparse.ArgumentParser();ap.add_argument("--input",required=True);ap.add_argument("--output",required=True);args=ap.parse_args()
K=QuadraticField(3,'w');w=K.gen();R=PolynomialRing(K,names=('x','y','z'));x,y,z=R.gens()
c=json.loads(Path(args.input).read_text())
def form(a):return sum(K(t)*v for t,v in zip(a,(x,y,z)))
half=QQ(1)/2
cos=(1,w/2,half,0,-half,-w/2,-1,-w/2,-half,0,half,w/2)
sin=(0,half,w/2,1,w/2,half,0,-half,-w/2,-1,-w/2,-half)
# exact algebraic trigonometric constants
cos=tuple(K(t) for t in cos);sin=tuple(K(t) for t in sin)
def F(theta,s):return matrix(K,[[cos[theta],-s*sin[theta]],[sin[theta],s*cos[theta]]])
N=len(c['angles']);nxt=c['next_dart'];df=c['dart_face'];dirs=c['native_direction_labels']
blocks=[[i for i in range(N) if df[i]==f] for f in range(c['face_count'])]
local={};localareas=[]
for fid,block in enumerate(blocks):
 v=vector(R,[0,0]);points=[]
 for i in block:
  local[i]=v;points.append(v);v=v+form(c['edge_colors'][i][1])*vector(K,[cos[dirs[i]],sin[dirs[i]]])
 assert v==vector(R,[0,0]),('nonclosedface',block,v)
 localareas.append(sum(matrix(R,[points[k],points[(k+1)%len(points)]]).det() for k in range(len(points)))/2)
 # remove subdivision vertices and compare original native geometry
 native=[local[i] for i in block if c['angles'][i]!=180]
 arms=[form(t) for t in c['arm_forms'][(0 if fid<2 else 4):(4 if fid<2 else 8)]]
 aa,bb,cc,dd=arms;ee=form(c['e_forms'][0 if fid<2 else 1])
 assert native==[vector(R,v) for v in [(0,0),(aa,0),(aa,bb),(aa-w*cc/2,bb+cc/2),(-ee/2,w*ee/2)]]
 assert bb-cc==w*(dd-aa) and ee==w*cc+dd-2*aa
# independently check every vertex link as one cycle of individual corner arcs
pair={};endmap={}
for i,j,same in c['edge_pairs']:
 pair[i]=(j,same);pair[j]=(i,same)
# arc flags(corner,0 incoming /1 outgoing), tile arc plus glued endpoint transitions
link={};corneredges={i:[] for i in range(N)}
for i,j,same in c['edge_pairs']:
 connections=[((i,1),(j,1)),((nxt[i],0),(nxt[j],0))] if same else [((i,1),(nxt[j],0)),((nxt[i],0),(j,1))]
 for a,b in connections:link[a]=b;link[b]=a
seen=set();links=[]
for flag in link:
 if flag in seen:continue
 route=[];at=flag
 while at not in seen:
  seen.add(at);other=(at[0],1-at[1]);seen.add(other);route.append(at[0]);at=link[other]
 assert at==flag,('noncircularlink',flag,at)
 assert sum(c['angles'][i] for i in route)==360
 links.append(route)
# lift finite direction/sign frames and develop by exact affine maps
start=(0,0,1);positions={start:vector(R,[0,0])};todo=deque([start]);transitions=[]
while todo:
 state=todo.popleft();face,theta,s=state;frame=F(theta,s);origin=positions[state]
 for i in blocks[face]:
  j,same=pair[i];ss=s*(-1 if same else 1);tt=(theta+s*dirs[i]-ss*dirs[j]+(0 if same else 6))%12
  target=(df[j],tt,ss);otherframe=F(tt,ss)
  endpoint=local[i if same else nxt[i]]
  location=origin+frame*endpoint-otherframe*local[j]
  if target not in positions:positions[target]=location;todo.append(target)
  shift=location-positions[target]
  # both endpoints, with opposite CCW orientation after a reflection
  A0=origin+frame*local[i];A1=origin+frame*local[nxt[i]]
  B0=positions[target]+otherframe*local[j]+shift;B1=positions[target]+otherframe*local[nxt[j]]+shift
  assert (A0==B0 and A1==B1) if same else (A0==B1 and A1==B0)
  Avec=s*(A1-A0);Bvec=ss*(B1-B0);assert Avec==-Bvec
  transitions.append((state,i,target,j,shift))
nonzero=[t[4] for t in transitions if t[4]!=vector(R,[0,0])]
def flatten(v):
 out=[]
 for q in v:
  assert q.degree()<=1 and q.constant_coefficient()==0
  for parameter in (x,y,z):
   coef=K(q.monomial_coefficient(parameter));out.extend([QQ(coef[0]),QQ(coef[1])])
 return vector(QQ,out)
H=matrix(QQ,[flatten(v) for v in nonzero]);rank=H.rank()
print('LINKS',len(links),links,'LIFT_STATES',len(positions),'HOLONOMY_RANK',rank,flush=True)
assert rank==2
basis=[]
for v in nonzero:
 if matrix(QQ,[flatten(t) for t in basis+[v]]).rank()>len(basis):basis.append(v)
 if len(basis)==2:break
B=matrix(QQ,[flatten(v) for v in basis]);coords=[B.solve_left(flatten(v)) for v in nonzero]
den=lcm([q.denominator() for v in coords for q in v]);G=matrix(ZZ,[[den*q for q in v] for v in coords]).hermite_form();G=matrix(QQ,[r for r in G.rows() if r!=0])/den
assert G.nrows()==2
periods=[sum((G[k,j]*basis[j] for j in range(2)),vector(R,[0,0])) for k in range(2)]
P=matrix(R,periods);covol=P.det();total=sum(localareas[state[0]] for state in positions)
assert covol==total or -covol==total,('areaindex',covol,total)
periodcoords=[]
periodflat=matrix(QQ,[flatten(v) for v in periods])
for a,i,b,j,shift in transitions:
 q=periodflat.solve_left(flatten(shift));assert all(t in ZZ for t in q);periodcoords.append([int(t) for t in q])
print('PERIODS',periods,'COVOLUME',covol,'SUM_AREA',total,flush=True)
def sv(v):return [str(t) for t in v]
result={'status':'exact_geometric_candidate_pending_review','source':args.input,'vertex_links':links,'lift_states':[list(s) for s in positions],'positions':[sv(v) for v in positions.values()],'local_atomic_vertices':{str(i):sv(v) for i,v in local.items()},'local_face_areas':[str(t) for t in localareas],'periods':[sv(v) for v in periods],'covolume_signed':str(covol),'total_lift_face_area':str(total),'transitions':[{'state':list(a),'dart':i,'target':list(b),'target_dart':j,'shift':sv(shift),'period_coordinates':pc} for (a,i,b,j,shift),pc in zip(transitions,periodcoords)]}
Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
