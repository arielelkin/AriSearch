#!/usr/bin/env python3
"""Independent exhaustive endpoint census/witness controls, fixed domain only.
Producer tables, analyze, union/find and congruence routines are not called.
"""
import argparse,hashlib,importlib.util,json,time
import z3
from collections import Counter,defaultdict
from pathlib import Path
S=Path(__file__).resolve().parents[1]/'searches'
s=importlib.util.spec_from_file_location('audit_align',S/'penrose-kite-dart-edge-alignment.py');align=importlib.util.module_from_spec(s);s.loader.exec_module(align)
K,w=align.K,align.w
patch_path=Path('research/certificates/penrose-kite-dart-patch4.json')
P,V,owners,components,roles,pairs=align.source(str(patch_path))
# Independently verify the role/parity transfer and every source edge owner.
assert set(roles)=={(k,i) for k in ('kite','dart') for i in range(4)}
for edge,os in owners.items():
 assert len(os) in (1,2)
 if len(os)==2:
  (ri,i),(rj,j)=os;A,B=P['tiles'][ri],P['tiles'][rj]
  assert A[1][i]==B[1][(j+1)%4] and A[1][(i+1)%4]==B[1][j]
  ca,pa=roles[A[0],i];cb,pb=roles[B[0],j]
  assert ca==cb and pa+pb==1
for (kind,i),(ci,parity) in roles.items():assert components[ci]['name']==('long' if i in (0,3) else 'short')

def local(mask,active,kind,chord):
 selected=sorted([2*i for i in range(4) if mask>>i&1]+[2*i+1 for i in range(4) if roles[kind,i][0] in active])
 if len(selected)<3:return None
 faces=[['P']+[(a+t)%8 for t in range((b-a)%8+1)] for a,b in zip(selected,selected[1:]+selected[:1])]
 if chord:
  e,c=2*chord[0]+1,2*chord[1];matches=[i for i,C in enumerate(faces) if e in C and c in C]
  if len(matches)!=1:return None
  C=faces.pop(matches[0]);u,v=sorted((C.index(e),C.index(c)))
  if v-u in (1,len(C)-1):return None
  faces += [C[u:v+1],C[v:]+C[:u+1]]
 boundary={};segments=[]
 for i,C in enumerate(faces):
  seg=[]
  for a,b in zip(C,C[1:]+C[:1]):
   if a!='P' and b!='P' and b==(a+1)%8:boundary[a]=i
   else:seg.append((a,b))
  segments.append(seg)
 assert set(boundary)==set(range(8))
 counts=Counter(e for seg in segments for e in seg);assert all(counts[b,a]==n==1 for (a,b),n in counts.items())
 return boundary,segments
def key(r):return tuple(r['active_orbits']),r['kite_mask'],r['dart_mask'],tuple(r.get('kite_chord') or ()) or None,tuple(r.get('dart_chord') or ()) or None
def expected(chords):
 result=set();sizes={}
 for active in ((0,),(1,),(0,1)):
  bykind={}
  for kind in ('kite','dart'):
   rows=[]
   for mask in range(16):
    choices=[None]+([(side,c) for side in range(4) if roles[kind,side][0] in active for c in range(4) if c not in (side,(side+1)%4)] if chords else [])
    for chord in choices:
     if local(mask,active,kind,chord) is not None:rows.append((mask,chord))
   bykind[kind]=rows
  sizes[str(active)]={k:len(v) for k,v in bykind.items()}
  for mk,ck in bykind['kite']:
   for md,cd in bykind['dart']:
    if not chords or ck or cd:result.add((active,mk,md,ck,cd))
 return result,sizes
def check(r,chords):
 active,mk,md,ck,cd=key(r);tabs={k:local(m,active,k,c) for k,m,c in [('kite',mk,ck),('dart',md,cd)]}
 adjacency=defaultdict(set);segments={};neighbours=defaultdict(set)
 boundary_corners={v for edge,os in owners.items() if len(os)==1 for v in edge}
 def node(ri,q):
  gv=P['tiles'][ri][1]
  if q=='P':return ('p',ri)
  if q%2==0:return ('v',gv[q//2])
  return ('e',*sorted((gv[q//2],gv[(q//2+1)%4])))
 for ri,(kind,gv,a) in enumerate(P['tiles']):
  for pi,seg in enumerate(tabs[kind][1]):
   D=[(node(ri,u),node(ri,v)) for u,v in seg];segments[ri,pi]=D
   for u,v in D:neighbours[u].add(v);neighbours[v].add(u)
 boundary=set()
 for edge,os in owners.items():
  for half in (0,1):
   pieces=[]
   for ri,side in os:
    kind,gv,a=P['tiles'][ri];h=half if gv[side]==min(edge) else 1-half;pieces.append((ri,tabs[kind][0][2*side+h]))
   if len(pieces)==1:boundary.update(pieces)
   else:
    a,b=pieces;adjacency[a].add(b);adjacency[b].add(a)
 if r['dead'] is None:
  available=set(segments);verified=set();allforms=[]
  while available:
   start=next(iter(available));M={start};todo=[start]
   while todo:
    for b in adjacency[todo.pop()]:
     if b not in M:M.add(b);todo.append(b)
   available-=M
   if M&boundary:continue
   D=[e for m in M for e in segments[m]];nxt=dict(D);assert len(nxt)==len(D)
   a=next(iter(nxt));start=a;C=[]
   while not C or a!=start:C.append(a);a=nxt[a];assert len(C)<=len(D)
   assert len(C)==len(D)
   C=[u for u in C if u[0]!='e'];ri=min(q[0] for q in M);origin=V[P['tiles'][ri][1][0]];rotation=w**(-P['tiles'][ri][2]);forms=[]
   for u in C:
    if u[0]=='v':f={'c':(V[u[1]]-origin)*rotation}
    else:
     j=u[1];kind,gv,orientation=P['tiles'][j];f={'c':(V[gv[0]]-origin)*rotation,0 if kind=='kite' else 2:w**orientation*rotation}
    forms.append({str(k):tuple(v) for k,v in f.items() if v})
   allforms.append(forms)
  for cl in r['classes']:
   stored=[{k:tuple(v) for k,v in f.items()} for f in cl['forms']]
   assert any(len(f)==len(stored) and any(f[i:]+f[:i]==stored for i in range(len(f))) for f in allforms),'Stored coordinate representative is not a reconstructed interior face'
  return len(allforms),len(r['classes'])
 M={tuple(q) for q in r['witness']['pieces']};start=next(iter(M));reached={start};todo=[start]
 while todo:
  for b in adjacency[todo.pop()]:
   if b not in reached:reached.add(b);todo.append(b)
 assert reached==M and not M&boundary
 D=[e for m in M for e in segments[m]];counts=Counter(D);status=r['dead']
 if status=='slit':assert any((b,a) in counts for a,b in counts);return
 assert len(counts)==len(D);nxt={}
 for a,b in D:assert a not in nxt;nxt[a]=b
 cycles=[];unvisited=set(nxt)
 while unvisited:
  s=next(iter(unvisited));C=[];a=s
  while a in unvisited:unvisited.remove(a);C.append(a);a=nxt[a]
  assert a==s;cycles.append(C)
 if status=='multiple-boundary-cycles':assert len(cycles)>1;return
 assert len(cycles)==1
 flat={u for u,N in neighbours.items() if len(N)==2 and (u[0]=='p' or u[0]=='e' and len(owners[frozenset(u[1:])])==2 or u[0]=='v' and u[1] not in boundary_corners)} if chords else {u for u in neighbours if u[0]=='e'}
 C=[u for u in cycles[0] if u not in flat]
 if status=='degenerate-face':assert len(C)<3;return
 assert status=='triangle-or-quadrilateral-escape',status
 assert 3<=len(C)<=4 and r['corners']==len(C),(key(r),len(C),r.get('corners'))
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output-dir',default='research/reviews');args=ap.parse_args();output_dir=Path(args.output_dir);output_dir.mkdir(parents=True,exist_ok=True)
 result={'scope':'Fixed census; conditional degree-two straightness; marked P2 source hull','audits':[]}
 for stem,chords in [('stars',False),('chords',True)]:
  path=Path(f'research/certificates/penrose-kite-dart-edge-{stem}-patch4.jsonl');rows=[json.loads(l) for l in path.read_text().splitlines()];census,sizes=expected(chords)
  assert {key(r) for r in rows}==census and len(rows)==len(census)
  assert all(r['patch_sha256']==hashlib.sha256(patch_path.read_bytes()).hexdigest() for r in rows)
  dead=[r for r in rows if r['dead']]
  for r in dead:check(r,chords)
  retained_controls=[check(r,chords) for r in rows if r['dead'] is None]
  result['audits'].append({'kind':stem,'recipes':len(rows),'witnesses_checked':len(dead),'stats':dict(Counter(r['dead'] or 'retained' for r in rows)),'local_types':sizes,'retained_face_coordinate_controls':retained_controls,'checkpoint_sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
 spec=importlib.util.spec_from_file_location('independent_real_encoder',Path(__file__).with_name('kite-dart-exclusion-audit.py'));independent=importlib.util.module_from_spec(spec);spec.loader.exec_module(independent)
 stars=[json.loads(l) for l in Path('research/certificates/penrose-kite-dart-edge-stars-patch4.jsonl').read_text().splitlines()]
 result['independent_weak_convexity']=[]
 for row in stars:
  if row['dead'] is not None:continue
  row['kite'],row['dart']=row['kite_mask'],row['dart_mask']
  previous,smt=independent.weak_check(row,15000)
  # Remove the at-least-five-positive-turn constraints to reproduce the
  # deliberately larger zero-minimum-corner domain. All other independent
  # constraints remain: weak turns, positive area, nonzero edges, interior.
  parsed=z3.parse_smt2_string(smt);kept=[];removed=0
  for assertion in parsed:
   if z3.is_ge(assertion) and str(assertion.arg(1))=='5':removed+=1
   else:kept.append(assertion)
  assert removed==len(row['classes'])
  solver=z3.SolverFor('QF_NRA');solver.set(timeout=15000);solver.add(*kept);t=time.monotonic();answer=solver.check()
  assert answer==z3.unsat,answer
  result['independent_weak_convexity'].append({'masks':[row['kite'],row['dart']],'status':str(answer),'minimum_genuine_corners':0,'seconds':round(time.monotonic()-t,3),'five_corner_constraints_removed':removed})
  (output_dir/f'kite-dart-edge-attachment-{row["kite"]}-{row["dart"]}-weak.smt2').write_text(solver.sexpr()+'\n(check-sat)\n')
 (output_dir/'kite-dart-edge-attachment-audit-controls.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
if __name__=='__main__':main()
