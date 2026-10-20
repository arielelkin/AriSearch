#!/usr/bin/env sage-python
"""Exact affine nonresonance gate and an all-obtuse type-I periodic escape."""
import importlib.util,json
from pathlib import Path
from sage.all import QQ,QQbar,AA,matrix,vector
base=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('atlas',base/'research/searches/hexagon-five-four-forced-dimer-2026-10-19.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
stars=m.build((0,1,1,0,2,3))['fixed_stars']
masks=[33416,41032,1118212,2625540,20774,22550,3543044]
records=[]
for mask in masks:
 rows=[[int(i//6==f) for i in range(12)]+[4] for f in range(2)]
 ids=[k for k in range(len(stars)) if mask>>k&1]
 rows += [[sum(p[0]==i for p in stars[k]) for i in range(12)]+[2] for k in ids]
 aug=matrix(QQ,rows);equ=vector(QQ,[QQ(2)/3]*12)
 assert aug[:,:12]*equ==vector(QQ,aug.column(12))
 # On [3/5,4/5]^12 a nonempty pi-sum has <=floor(5/3)=1 entries.
 candidates=[[int(i==j) for i in range(12)] for j in range(12)]
 assert all(sum(QQ(c)*equ[i] for i,c in enumerate(v))!=1 for v in candidates)
 records.append(dict(mask=mask,star_indices=ids,affine_dimension=12-aug[:,:12].rank(),augmented_rref=[[str(v) for v in row] for row in aug.echelon_form()],pi_multiset_candidates_under_positive_bound=candidates,pi_sum_feasible_count=0,identity_count_all_finite_multisets=0))
D=AA(3).sqrt();lengths=list(map(QQ,[2,1,QQ(101)/100,QQ(102)/100,QQ(103)/100]))
def triangle(a,b):
 y=(D*D+a*a-b*b)/(2*D);h=(a*a-y*y).sqrt()
 assert 0<y<D and h>0
 return h,y

def cross(u,v):return u[0]*v[1]-u[1]*v[0]
def polygon(word):
 l=[lengths[i] for i in word];ht,yt=triangle(l[1],l[2]);hb,yb=triangle(l[5],l[4]);z=AA(0)
 P=[vector(AA,(-l[0],z)),vector(AA,(z,z)),vector(AA,(ht,yt)),vector(AA,(z,D)),vector(AA,(-l[0],D)),vector(AA,(-l[0]-hb,yb))]
 for j in range(6):
  u=P[(j+1)%6]-P[j]
  assert u.dot_product(u)==l[j]**2
  for k in range(6):
   if k not in (j,(j+1)%6): assert cross(u,P[k]-P[j])>0
  # At vertex j+1 the two inward rays have negative scalar product.
  v=P[(j+2)%6]-P[(j+1)%6]
  assert (-u).dot_product(v)<0
 assert P[1]-P[0]==-(P[4]-P[3])
 # Each pair of chains is a graph over 0<=y<=D; side-midpoint
 # halfturns preserve each entire two-segment periodic boundary.
 center_right=(P[1]+P[2])/2;center_left=(P[4]+P[5])/2
 w=2*(center_right-center_left);v=vector(AA,(0,D))
 area=sum(cross(P[j],P[(j+1)%6]) for j in range(6))/2
 assert cross(w,v)==2*area and w[0]>0
 # Verify the halfturn sends both vertices of each periodic boundary
 # to vertices of that same boundary modulo the vertical period.
 for chain,c in [([P[1],P[2],P[3]],center_right),([P[4],P[5],P[0]],center_left)]:
  for q in chain:
   image=2*c-q
   assert any(image[0]==r[0] and (image[1]-r[1])/D in QQ and QQ((image[1]-r[1])/D).denominator()==1 for r in chain)
 return dict(word=word,coordinates_approx=[[float(x) for x in p] for p in P],coordinate_recipe='D=sqrt(3); triangle(a,b): y=(3+a^2-b^2)/(2D), h=sqrt(a^2-y^2); top=triangle(l1,l2); bottom=triangle(l5,l4); vertices=(-l0,0),(0,0),(ht,yt),(0,D),(-l0,D),(-l0-hb,yb)',all_angles_strictly_obtuse=True,strict_convexity_full_halfplane_checks=True,lengths_verified=True,periodic_tile_orbits=2,lattice_recipe='v=(0,D), w=2*(midpoint(side1)-midpoint(side4)); representatives P and halfturn_about_midpoint(side1)(P)',lattice_approx=[[float(x) for x in w],[0,float(D)]],twice_area_equals_lattice_determinant=True)
metrics=[polygon(list(m.A)),polygon([0,1,1,0,2,3])]
# Parallel opposite sides imply each consecutive block of three turns sums pi.
# Thus interior angle sums in each block are 2pi; check these rows imply all
# rows of the three indicated supports, using exact rational row containment.
block=matrix(QQ,[[int(i//3==j) for i in range(12)]+[2] for j in range(4)])
compatible=[]
for record in records:
 aug=matrix(QQ,record['augmented_rref'])
 if block.stack(aug).rank()==block.rank():
  assert aug.rank()==block.rank()==4
  record['equals_four_block_angle_space']=True
  record['block_augmented_rank']=4
  record['support_augmented_rank']=4
  record['stacked_augmented_rank']=4
  compatible.append(record['mask'])
 else:record['equals_four_block_angle_space']=False
assert compatible==[1118212,2625540,3543044]
out=dict(schema='FIVE_FOUR_NONRESONANT_SUPPORT_V1',angle_units='pi',compact_domain=['3/5','4/5'],relative_open_domain=['3/5','4/5'],uniform_positive_lower_bound='3/5',max_pi_sum_cardinality=1,equiangular_point=['2/3']*12,supports=records,lengths=[str(x) for x in lengths],exact_metric_support_masks=compatible,universal_periodic_omission_support_masks=compatible,metrics=metrics,status='three_entire_support_angle_families_have_conditional_monohedral_periodic_escapes',scope='For each of three block-angle supports every strictly convex common-length metric has a monohedral periodic escape; four other supports and unrestricted problem remain unresolved. Formal star realization is not asserted.')
path=base/'research/certificates/hexagon-five-four-nonresonant-support-2026-10-19.json';path.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['status','exact_metric_support_masks','lengths']},indent=2))
