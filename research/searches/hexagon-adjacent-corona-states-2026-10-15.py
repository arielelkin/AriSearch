#!/usr/bin/env python3
"""Exact necessary indexed tile-corona states for FOUR explicit supports.
All 8 native arm choices per star, full-side endpoint consistency, reciprocal
state pruning. No angle or coordinate solve. JSON stdout; --output writes.
"""
from itertools import product
from pathlib import Path
import json,argparse
A=(0,0,1,2,3,4)
CASES=(
 ((2,2,1,3,0,4),((0,1,1),(0,5,10),(2,2,6),(3,4,11),(3,7,8),(4,5,9))),
 ((2,2,1,3,0,4),((0,10,10),(1,8,9),(2,6,7),(3,7,8),(4,5,9),(6,11,11))),
 ((0,1,3,0,4,2),((0,1,6),(0,5,9),(1,2,11),(2,3,7),(3,4,10),(4,5,8))),
)
def compatible(f,host,i,guest):
 j,dl,dr=host[i];g=j//6;k=j%6
 hs,gl,gr=guest[k]
 if hs!=6*f+i:return False
 nativehostends=(6*f+(i-1)%6,6*f+i)
 expected=dict(zip((dl,dr),nativehostends))
 return (gl,gr)==(expected[6*g+(k-1)%6],expected[6*g+k])
def analyze(B,S):
 W=(A,B);corner=[set() for _ in range(12)]
 for cs in S:
  for bits in product((0,1),repeat=3):
   sides=[(6*(c//6)+c%6,6*(c//6)+(c%6+1)%6) for c in cs]
   left=[side[b] for side,b in zip(sides,bits)];right=[side[1-b] for side,b in zip(sides,bits)]
   if any(W[right[i]//6][right[i]%6]!=W[left[(i+1)%3]//6][left[(i+1)%3]%6] for i in range(3)):continue
   for k,c in enumerate(cs):
    prev=(k-1)%3;nex=(k+1)%3
    records={left[k]:(right[prev],cs[prev]),right[k]:(left[nex],cs[nex])}
    own=sides[k];corner[c].add((records[own[0]],records[own[1]]))
 states=[[],[]]
 for f in (0,1):
  for ch in product(*(sorted(corner[6*f+i]) for i in range(6))):
   maps=[]
   for i in range(6):
    l=ch[(i-1)%6][1];r=ch[i][0]
    if l[0]!=r[0] or l[1]==r[1]:break
    j=l[0];ends={j,(j//6)*6+(j%6-1)%6}
    if {l[1],r[1]}!=ends:break
    maps.append((j,l[1],r[1]))
   else:states[f].append(tuple(maps))
 initial=states
 rounds=[]
 while True:
  nxt=[[],[]]
  for f in (0,1):
   for h in states[f]:
    if all(any(compatible(f,h,i,z) for z in states[h[i][0]//6]) for i in range(6)):nxt[f].append(h)
  if nxt==states:break
  rounds.append({'input':states,'output':nxt});states=nxt
 choices=[[[[j for j,z in enumerate(states[h[i][0]//6]) if compatible(f,h,i,z)] for i in range(6)] for h in states[f]] for f in (0,1)]
 return {'B':B,'support':S,'corner_port_options':[sorted(x) for x in corner],'initial_tile_states':initial,'reciprocal_pruning_rounds':rounds,'fixed_tile_states':states,'neighbor_state_choices':choices}
def build():
 return {'schema':'ADJACENT_REPEAT_CORONA_STATE_V1','A':A,'records':[analyze(B,S) for B,S in CASES],
 'scope':'Necessary finite local states only; uniqueness and connected deterministic-edge propagation are separate written proofs.'}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output');a=p.parse_args();encoded=json.dumps(build(),sort_keys=True,indent=2)+'\n'
 if a.output:Path(a.output).write_text(encoded)
 print(encoded,end='')
