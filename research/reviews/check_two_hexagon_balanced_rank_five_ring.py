#!/usr/bin/env python3
"""Independent solver-free audit using canonical global triangles.
No import of author verifier, SFT, CP-SAT, Sage or census code.
"""
import argparse,hashlib,itertools,json
from fractions import Fraction as Q
from pathlib import Path
D=((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))
T={(0,1,6),(1,2,7),(0,2,8),(3,4,9),(4,5,10),(3,5,11)}
A=[(r,s) for s in (1,-1) for r in range(6)]
def add(x,y):return x[0]+y[0],x[1]+y[1]
def subtract(x,y):return x[0]-y[0],x[1]-y[1]
def native(placement,k):r,s=placement;return (r+s*k)%6
# Derive every B-centred corner incidence from just the two globally
# declared triangle orientations (anchor indices k,k+2,k+4, k=0,1).
incidences=[]
for direction in range(6):
 target={(0,0),D[direction],D[(direction+1)%6]};matches=[]
 for x,y,k in itertools.product(range(-2,3),range(-2,3),(0,1)):
  anchor=(x,y);cells=[anchor,add(anchor,D[k]),add(anchor,D[k+1])]
  if set(cells)==target:matches.append(dict(zip(cells,(k,k+2,k+4))))
 assert len(matches)==1
 incidences.append(matches[0])

def rings(B):
 constraints=[]
 for k,inc in enumerate(incidences):
  bcorner=6+native(B,inc[(0,0)]);p,q=D[k],D[(k+1)%6]
  constraints.append({(i,j) for i,a in enumerate(A) for j,c in enumerate(A) if tuple(sorted((bcorner,native(a,inc[p]),native(c,inc[q])))) in T})
 # Independent search by recursive assignments that checks all already
 # instantiated constraints, rather than traversing the producer cycle.
 answers=[]
 def assign(path):
  if len(path)==6:
   if (path[5],path[0]) in constraints[5]:answers.append(tuple(path))
   return
  for i in range(12):
   if not path or (path[-1],i) in constraints[len(path)-1]:assign(path+(i,))
 assign(())
 return constraints,answers

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output');args=ap.parse_args();stored=json.loads(Path('research/certificates/two-hexagon-balanced-minimal-covering-root.json').read_text())
 # Independent rational affine elimination, including the two720 sums.
 triples=tuple(itertools.combinations_with_replacement(range(12),3))
 def counts(t):return [t.count(i) for i in range(12)]
 def span(gs):
  rows=[[1]*6+[0]*6+[720],[0]*6+[1]*6+[720]]+[counts(t)+[360] for t in gs];B={}
  for row in rows:
   v=list(map(Q,row))
   for pivot in sorted(B):
    f=v[pivot];v=[a-f*b for a,b in zip(v,B[pivot])]
   p=next((i for i,x in enumerate(v) if x),None)
   if p is not None:
    f=v[p];B[p]=[x/f for x in v]
  return B
 def closes(gs):
  B=span(gs);out=set()
  for t in triples:
   v=list(map(Q,counts(t)+[360]))
   for p in sorted(B):
    f=v[p];v=[a-f*b for a,b in zip(v,B[p])]
   if not any(v):out.add(t)
  return out
 assert len(span(T))-2==stored['rank_mod_polygon_sums']==5
 assert closes(T)==T=={tuple(t) for t in stored['closure']}=={tuple(t) for t in stored['T']}
 assert [sum(Q(1,3)*t.count(i) for t in T) for i in range(12)]==[Q(2,3)]*6+[Q(1,3)]*6
 assert list(map(Q,stored['weights']))==[Q(1,3)]*6 and list(map(Q,stored['species_weights']))==[Q(2,3),Q(1,3)]
 assert all(sum(c in t for t in T)==1 for c in range(6,12))
 subsets=0
 for size in (1,2,3):
  for gs in itertools.combinations(sorted(T),size):
   assert {c for t in closes(gs) for c in t}!=set(range(12));subsets+=1
 assert subsets==stored['rank_le_three_generator_subsets_checked']==41
 angles=list(map(Q,stored['generic_angles_degrees']));assert len(angles)==12
 assert all(0<x<180 for x in angles) and sum(angles[:6])==sum(angles[6:])==720
 assert {t for t in triples if sum(angles[c] for c in t)==360}==T
 allrings=[]
 for i,B in enumerate(A):
  constraints,solutions=rings(B);assert len(solutions)==1
  row=stored['exact_B_star_cycle_audit'][i];assert tuple(row['B_placement'])==B
  assert [set(map(tuple,x)) for x in row['relations']]==constraints
  assert set(map(tuple,row['cycle_solutions']))==set(solutions)
  allrings.append(solutions)
 relations=[]
 for k in range(6):
  # The cell opposite the A/A edge at D[k],D[k+1] is their vector sum.
  # Derive the shared A positions in its own ring by coordinate lookup.
  opposite=add(D[k],D[(k+1)%6]);aidx=D.index(subtract(D[k],opposite));bidx=D.index(subtract(D[(k+1)%6],opposite))
  assert (aidx,bidx)==((k+4)%6,(k+3)%6)
  valid=[]
  for i,j in itertools.product(range(12),repeat=2):
   for first,second in itertools.product(allrings[i],allrings[j]):
    if first[k]==second[aidx] and first[(k+1)%6]==second[bidx]:valid.append((i,j))
  assert len(valid)==4
  assert set(map(tuple,stored['six_direction_B_pair_relations'][k]))==set(valid)
  relations.append(valid)
 assert {A[i] for i,j in relations[0]}=={(0,1),(3,1),(0,-1),(3,-1)}
 assert {A[i] for i,j in relations[1]}=={(2,1),(5,1),(1,-1),(4,-1)}
 assert {i for i,j in relations[0]}.isdisjoint({i for i,j in relations[1]})
 possible={i for i in range(12) if all(any(a==i for a,b in rel) for rel in relations)}
 assert not possible and stored['B_states_with_all_six_required_neighbors']==[]
 # Canonical triangles confirm that each shared A/A edge has exactly the
 # two opposite third cells, so every such pair really forces another B.
 for k in range(6):
  edge={D[k],D[(k+1)%6]};thirds=set()
  for x,y,o in itertools.product(range(-3,4),range(-3,4),(0,1)):
   z=(x,y);cells={z,add(z,D[o]),add(z,D[o+1])}
   if edge<=cells:thirds|=cells-edge
  assert thirds=={(0,0),add(D[k],D[(k+1)%6])}
 result={'status':'PASSED','independent_global_triangle_incidence_maps':[[[list(z),c] for z,c in inc.items()] for inc in incidences],'B_ring_solution_counts':[len(x) for x in allrings],'direction_compatibility_counts':[len(x) for x in relations],'B_placements_admitting_all_six_opposites':sorted(possible),'exact_rank':5,'exact_closure_size':6,'low_rank_generator_subsets_checked':subsets,'source_sha256':hashlib.sha256(Path('research/certificates/two-hexagon-balanced-minimal-covering-root.json').read_bytes()).hexdigest(),'scope':'Native-order SFT empty with arbitrary side classes; no solver query replay or alternate boundary-order classification'}
 if args.output:Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result))
if __name__=='__main__':main()
