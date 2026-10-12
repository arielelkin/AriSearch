#!/usr/bin/env python3
"""Exact native support, seam tables and explicit orientable four-face torus.

No producer import, solver or polygon parameter enumeration. Matched actual
length assumptions are A0=B1,A2=B0,A3=B3; all other pairs are private.
"""
import argparse,itertools,json
from pathlib import Path
A=[130,281,150,295,224];B=[80,289,272,94,345]
def stars(angles,target):
 if target<0:return []
 return [tuple(c) for k in range(1,target//min(angles)+1) for c in itertools.combinations_with_replacement(angles,k) if sum(c)==target]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
 joint=A+B;flat=stars(joint,360);full=stars(joint,720)
 assert flat==[(130,150,80)]
 assert len(full)==9
 def has(a,b):return any(a in s and b in s and (a!=b or s.count(a)>=2) for s in full)
 # Every alpha/beta seam has ineligible far ends and an absent far star.
 assert all(not has(a,b) for a,b in itertools.product((281,224),(281,295)))
 # An x-side A3 cannot face gamma: its far y would meet delta or w.
 assert not has(224,289) and not has(224,345)
 # Angular support for hosts when flat-fan outer far endpoints are y,x.
 host_candidates=[]
 for n,angles in [('A',A),('B',B)]:
  for j in range(5):
   a,b=angles[j],angles[(j+1)%5]
   if (has(a,224) and has(b,295)) or (has(b,224) and has(a,295)):host_candidates.append((n,j))
 assert host_candidates==[('A',3),('A',4),('B',3)]
 eligible={130,150,80}
 potential_hosts=[]
 for n,angles in [('A',A),('B',B)]:
  for j in range(5):
   a,b=angles[j],angles[(j+1)%5]
   fits=lambda h,f:h in eligible or has(h,f)
   if (fits(a,224) and fits(b,295)) or (fits(b,224) and fits(a,295)):potential_hosts.append((n,j))
 assert potential_hosts==[('A',2),('A',3),('A',4),('B',3),('B',4)]
 # Remaining continuation support used after T exclusion.
 assert has(224,224) and not has(224,281) and has(150,281) and not has(150,224)
 assert has(150,289) and not has(150,345)
 assert has(224,94) and not has(224,80)
 assert has(130,272)
 # Two copies of each native CCW face, all paired by reversed boundaries.
 faces=[A,A,B,B]
 pairs=[((0,1),(1,1)),((0,4),(1,4)),((2,2),(3,2)),((2,4),(3,4)),
        ((0,0),(2,1)),((1,0),(3,1)),((0,2),(3,0)),((1,2),(2,0)),
        ((0,3),(2,3)),((1,3),(3,3))]
 assert sorted(e for pair in pairs for e in pair)==[(f,i) for f in range(4) for i in range(5)]
 parent=list(range(20));links={i:[] for i in range(20)}
 def find(i):
  while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
  return i
 def link(i,j):parent[find(i)]=find(j);links[i].append(j);links[j].append(i)
 for (f,i),(h,j) in pairs:
  link(5*f+i,5*h+(j+1)%5);link(5*f+(i+1)%5,5*h+j)
 groups={}
 for i in range(20):groups.setdefault(find(i),[]).append(i)
 assert len(groups)==6 and all(len(v)==2 for v in links.values())
 vertices=[]
 for group in groups.values():
  seen=[];previous=None;current=group[0]
  while current not in seen:
   seen.append(current);nxt=links[current][0] if links[current][0]!=previous else links[current][1]
   previous,current=current,nxt
  assert current==seen[0] and sorted(seen)==sorted(group)
  angles=[faces[i//5][i%5] for i in seen];assert sum(angles)==720
  vertices.append({'corners':[[i//5,i%5] for i in seen],'angles_doubled_degrees':angles})
 expected=sorted([sorted(x) for x in [(281,150,289),(281,150,289),(295,80,345),(295,80,345),(130,224,272,94),(130,224,272,94)]])
 assert sorted(sorted(v['angles_doubled_degrees']) for v in vertices)==expected
 graph={f:set() for f in range(4)}
 for (f,i),(h,j) in pairs:graph[f].add(h);graph[h].add(f)
 reached={0}
 while True:
  nxt=reached|set().union(*(graph[f] for f in reached))
  if nxt==reached:break
  reached=nxt
 assert len(reached)==4 and 6-10+4==0
 aliases={('A',0):('B',1),('A',2):('B',0),('A',3):('B',3)}
 for (f,i),(h,j) in pairs:
  if f//2!=h//2:assert aliases[('A',i)]==('B',j)
  else:assert i==j
 out={'status':'PASSED','scope':'Exact support/continuation tables and explicit four-face orientable flat torus; no metric search. For actual strictly convex polygons, length aliases make every pairing isometric and flat universal cover is a periodic plane tiling.','native_angles_doubled_degrees':{'A':A,'B':B},'flat_native_stars':flat,'full_native_stars':full,'full_endpoint_coincidence_hosts_for_y_x_fan':host_candidates,'possible_hosts_including_eligible_endpoint_overrun':potential_hosts,'actual_length_aliases':['A0=B1','A2=B0','A3=B3'],'faces':['A0copy','A1copy','B0copy','B1copy'],'edge_pairs_reversed_boundary':pairs,'vertices':vertices,'topology':{'connected':True,'orientable':True,'vertex_links_single_cycles':True,'faces':4,'edges':10,'vertices':6,'Euler_characteristic':0},'all_vertex_angle_sums_doubled_degrees':720,'periodic_tiles_per_fundamental_domain':{'A':2,'B':2},'strict_scope':'Pointwise T exclusion and alias necessity require the accompanying local proof. This checker validates all finite support and carrier tables used there.'}
 Path(args.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':'PASS','vertices':6,'actual_length_aliases':out['actual_length_aliases'],'periodic_domain':'2A+2B'}))
if __name__=='__main__':main()
