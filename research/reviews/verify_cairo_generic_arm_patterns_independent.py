#!/usr/bin/env python3
"""Independently reconstruct the209 generic partial-contact Cairo patterns."""
import json
from collections import Counter
from itertools import combinations, permutations, combinations_with_replacement
from pathlib import Path
from sage.all import QuadraticField, matrix, vector
K=QuadraticField(3,'w');w=K.gen()
root=Path(__file__).resolve().parents[2]
data=json.loads((root/'research/certificates/partial-contact-cairo-generic-arm-patterns.json').read_text())
records={tuple(map(tuple,r['cross_matches'])):r for r in data['records']}
assert len(records)==len(data['records'])==209
counts=Counter();seen=set(); anchored_counts=Counter(); anchored_survivors=set()
for k in range(5):
 for first in combinations(range(4),k):
  for second in combinations(range(4),k):
   for order in permutations(second):
    matches=tuple(zip(first,order));assert matches not in seen;seen.add(matches)
    # Collapse declared shared labels before closure, unlike the producer's8-slot system.
    labels=list(range(4));reverse={b:a for a,b in matches};unused=4
    for b in range(4):
     if b in reverse:labels.append(reverse[b])
     else:labels.append(unused);unused+=1
    U=[vector(K,[int(j==labels[i]) for j in range(unused)]) for i in range(8)]
    rows=[w*U[0]+U[1]-U[2]-w*U[3],w*U[4]+U[5]-U[6]-w*U[7]]
    kernel=matrix(K,rows).right_kernel().basis()
    form=lambda v:tuple(v.dot_product(t) for t in kernel)
    arms=[form(x) for x in U]
    bad=any((arms[i]==arms[j])!=(labels[i]==labels[j]) for i,j in combinations(range(8),2))
    rec=records[matches]
    if bad:
     status='forced-extra-arm-equality'
     assert rec['anchored_status']==status
    else:
     # Verify the producer's retained positive point in its published basis,
     # independently of any polyhedral solver or feasible/empty verdict.
     I=[vector(K,[int(i==j) for j in range(8)]) for i in range(8)]
     fullrows=[w*I[0]+I[1]-I[2]-w*I[3],w*I[4]+I[5]-I[6]-w*I[7]]+[I[a]-I[b+4] for a,b in matches]
     fullkernel=matrix(K,fullrows).right_kernel().basis()
     assert len(fullkernel)==rec['dimension']==len(kernel)
     coeffs=vector(K,[K(x) for x in rec['positive_parameter_point']])
     values=sum((coeffs[i]*t for i,t in enumerate(fullkernel)),vector(K,[0]*8))
     E=-2*values[0]+w*values[2]+values[3]
     F=-2*values[4]+w*values[6]+values[7]
     assert all(t>=1 for t in list(values)+[E,F])
     assert list(values)==[K(t) for t in rec['positive_arm_values']]
     assert [E,F]==[K(t) for t in rec['positive_e_values']]
     e=[form(-2*U[0]+w*U[2]+U[3]),form(-2*U[4]+w*U[6]+U[7])]
     other=[1,0,3,2,5,4,7,6]
     banks={}
     for i,j in combinations_with_replacement(range(8),2):
      if arms[i]!=arms[j]:continue
      u,v=other[i],other[j];key=form(U[u]+U[v])
      banks.setdefault(key,set()).update([arms[u],arms[v]])
     assert not any(x in banks for x in e)
     relation={(x,x) for x in arms}
     for group in banks.values():
      relation.update((x,y) for x in group for y in group)
     isolated=[(arms[1],arms[2]),(arms[5],arms[6])]
     legal=[]
     for H in (0,1):
      for G in (0,1):
       if e[H]!=e[G]:continue
       for flip in (0,1):
        ends=[(arms[4*H],arms[4*G+(3 if flip else 0)]),
              (arms[4*H+3],arms[4*G+(0 if flip else 3)])]
        if all(any(((x,a) in relation and(y,b) in relation) or
                   ((x,b) in relation and(y,a) in relation) for a,b in isolated)
               for x,y in ends):legal.append([H,G,flip])
     assert sorted(legal)==sorted(rec['allowed_e_seams'])
     # Stronger necessary relation: the first/second bank events must involve
     # the actual arm slots on the ray, not arbitrary equal-length bank slots.
     sums_by_slot=[]
     for i in range(8):
      sums_by_slot.append({form(U[i]+U[j]) for j in range(8)
                           if arms[other[i]]==arms[other[j]]})
     allowed_actual=[]
     for H in (0,1):
      for G in (0,1):
       if e[H]!=e[G]:continue
       for flip in (0,1):
        ends=[(4*H,4*G+(3 if flip else 0)),(4*H+3,4*G+(0 if flip else 3))]
        def permits(i,j):
         return arms[i]==arms[j] or bool(sums_by_slot[i]&sums_by_slot[j])
        if all(any((permits(i,u) and permits(j,v)) or(permits(i,v) and permits(j,u))
                   for u,v in ((1,2),(5,6))) for i,j in ends):
         allowed_actual.append((H,G,flip))
     outcome='survivor' if all(any(t[0]==H for t in allowed_actual) for H in(0,1)) else 'obstruction'
     assert rec['anchored_status']==('local-survivor' if outcome=='survivor' else 'generic-beta-obstruction')
     assert sorted(map(list,allowed_actual))==sorted(rec['anchored_allowed_e_seams'])
     actual_compat={(i,j) for i in range(8) for j in range(8) if permits(i,j)}
     assert actual_compat==set(map(tuple,rec['anchored_slot_compatibility']))
     anchored_counts[outcome]+=1
     if outcome=='survivor':anchored_survivors.add(frozenset(matches))
     status='local-survivor' if all(any(t[0]==H for t in legal) for H in(0,1)) else 'generic-beta-obstruction'
    assert status==rec['status'];counts[status]+=1
assert seen==set(records)
assert dict(counts)==data['counts']=={'forced-extra-arm-equality':22,'generic-beta-obstruction':147,'local-survivor':40}
assert Counter(len(x['cross_matches']) for x in data['records'] if x['status']=='local-survivor')=={2:8,3:32}
# Reconstruct every actual reflected/swap sufficient subset independently.
bases={'swapped-arm-cone':((0,2),(2,0)), 'reviewed-Y-cone':((1,3),(2,0))}
orbits={}
for name,base in bases.items():
 for mask in range(8):
  rp,rq,sw=(mask>>j&1 for j in range(3))
  transformed={(3-i if rp else i,3-j if rq else j) for i,j in base}
  if sw:transformed={(j,i) for i,j in transformed}
  orbits.setdefault(frozenset(transformed),set()).add(name)
assert len(orbits)==8
open_patterns=set();covered=Counter()
for pattern,rec in records.items():
 if rec['status']!='local-survivor':continue
 options={s for s in orbits if s.issubset(pattern)}
 if not options:
  assert rec['periodic_family']=='anchored-beta-obstruction'
  open_patterns.add(frozenset(pattern));continue
 family=rec['periodic_family'];subset=frozenset(map(tuple,rec['sufficient_periodic_pattern']))
 assert subset in options and family in orbits[subset]
 rp,rq,sw=rec['native_reflection_and_swap']
 mapped={(3-i if rp else i,3-j if rq else j) for i,j in bases[family]}
 if sw:mapped={(j,i) for i,j in mapped}
 assert frozenset(mapped)==subset
 covered[len(pattern)]+=1
expected=set()
for mask in range(8):
 rp,rq,sw=(mask>>j&1 for j in range(3))
 mapped={(3-i if rp else i,3-j if rq else j) for i,j in ((0,3),(1,0),(2,1))}
 if sw:mapped={(j,i) for i,j in mapped}
 expected.add(frozenset(mapped))
assert open_patterns==expected and len(expected)==8
assert covered=={2:8,3:24}
assert anchored_counts=={'obstruction':155,'survivor':32}
assert data['anchored_counts']=={'forced-extra-arm-equality':22,'generic-beta-obstruction':155,'local-survivor':32}
assert anchored_survivors=={frozenset(p) for p,r in records.items() if r.get('periodic_family') in bases}
print('PASS:actual-slot two-T necessities give155 generic obstructions and32 sufficient periodic survivors')
print('PASS:32 sufficient periodic subset maps;8 additionally rejected patterns form one actual reflection/species orbit')
print('PASS:209 independently reconstructed patterns;187 exact positive witnesses;22 equality rejects;147 generic necessary obstructions;40 local survivors')
