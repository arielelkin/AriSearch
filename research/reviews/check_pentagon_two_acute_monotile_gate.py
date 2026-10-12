#!/usr/bin/env python3
"""Exact D5 matching against RaoTable2's15 known pentagonal families.
No geometry enumeration or search solver. The generic survivor is not a
positive tiling candidate; mixed periodic escapes remain a separate gate.
"""
import argparse,json
from pathlib import Path
from sage.all import QuadraticField,PolynomialRing,AA
K=QuadraticField(3,'sqrt_three',embedding=AA(3).sqrt());r=K.gen();R=PolynomialRing(K,'c,d,e');c,d,e=R.gens()
a=e+(c+2*d)/r;b=e+(d-c)/r;L=(a,b,c,d,e);ANGLES=(60,60,150,120,150)
def relation(terms,total=360):return terms,total
# Lowercaseangles, uppercaseedgesi->i+1 perprimaryTable2.
ANGLE={1:[([(0,1),(1,1),(2,1)],360)],2:[([(0,1),(1,1),(3,1)],360)],3:[([(4,3)],360),([(3,1),(4,2)],360),([(1,1),(4,2)],360)],4:[([(0,1),(1,1),(3,1)],360),([(4,2)],180)],5:[([(4,3)],360),([(0,1),(1,1),(3,1)],360)],6:[([(3,1),(4,2)],360),([(0,1),(2,1),(3,1)],360)],7:[([(3,1),(4,2)],360),([(0,1),(2,2)],360)],8:[([(3,1),(4,2)],360),([(1,2),(2,1)],360)],9:[([(3,1),(4,2)],360),([(0,2),(2,1)],360)],10:[([(2,2),(3,1)],360),([(1,1),(2,1),(4,1)],360),([(0,1),(1,2)],360)],11:[([(2,1),(3,2)],360),([(1,1),(3,1),(4,1)],360),([(0,1),(1,2)],360)],12:[([(2,1),(3,2)],360),([(1,1),(3,1),(4,1)],360),([(0,1),(1,2)],360)],13:[([(1,1),(3,2)],360),([(0,1),(1,1),(3,1)],360),([(4,2)],180)],14:[([(2,1),(3,2)],360),([(1,1),(3,1),(4,1)],360),([(0,1),(1,2)],360)],15:[([(2,1),(3,2)],360),([(1,2),(4,1)],360),([(0,2),(3,1)],360),([(4,2)],180)]}
def eq(i,j):return [(i,1),(j,-1)]
LENGTH={1:[],2:[eq(2,4)],3:[[(2,1),(4,1),(3,-1)],eq(0,1)],4:[eq(3,4),eq(1,2)],5:[eq(3,4),eq(1,2)],6:[eq(2,3),eq(3,4),eq(0,1)],7:[eq(0,2),eq(2,3),eq(3,4)],8:[eq(0,1),eq(1,2),eq(2,3)],9:[eq(0,1),eq(1,2),eq(2,3)],10:[[(0,1),(2,1),(3,-1)],eq(3,4)],11:[eq(0,1),[(1,1),(2,-1),(4,-2)]],12:[[(0,1),(2,1),(1,-1)],[(1,1),(4,-2)]],13:[[(0,1),(1,-2)],eq(1,2)],14:[eq(0,1),[(1,1),(2,-2)],eq(2,4)],15:[eq(1,3),eq(3,4),[(2,1),(1,-2)]]}
def proportional(p,q):
 for i in range(3):
  pc,qc=p.monomial_coefficient(R.gen(i)),q.monomial_coefficient(R.gen(i))
  if qc:return p==(pc/qc)*q and pc!=0
 return False

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output');args=ap.parse_args()
 # Allothernativeedges are strictly smaller than a on the given domain.
 h=R.gen(0);bound_rewrite=(r-1)*d+(2-r)*e+(1-1/r)*h
 assert (a-c).subs({c:d+r*e-h})==bound_rewrite
 assert all(K(x)>0 for x in (r-1,2-r,1-1/r))
 assert a-b==(2*c+d)/r and a-d==e+c/r+(2/r-1)*d and a-e==(c+2*d)/r
 records=[];counts={};feasible=[]
 for kind in range(1,16):
  count=0
  for start in range(5):
   for direction in (1,-1):
    cm=[(start+direction*i)%5 for i in range(5)];angles=[ANGLES[i] for i in cm]
    if not all(sum(angles[i]*n for i,n in terms)==target for terms,target in ANGLE[kind]):continue
    count+=1;sm=[cm[i] if direction==1 else cm[(i+1)%5] for i in range(5)]
    equations=[sum((n*L[sm[i]] for i,n in terms),R(0)) for terms in LENGTH[kind]]
    if any(proportional(p,a-L[j]) for p in equations for j in range(1,5)):
     verdict='IMPOSSIBLE_LARGEST_EDGE'
    else:
     assert kind==2 and len(equations)==1
     if proportional(equations[0],c-e):locus='c=e'
     else:assert proportional(equations[0],b-d);locus='b=d'
     verdict='MONOHEDRAL_PERIODIC_LOCUS';feasible.append(locus)
    records.append({'type':kind,'vertex_start':start,'direction':direction,'side_map':sm,'length_equations':[str(p) for p in equations],'verdict':verdict})
  if count:counts[kind]=count
 assert counts=={2:4,5:2,8:2} and set(feasible)=={'c=e','b=d'}
 result={'status':'PASSED','angle_word':ANGLES,'domain':'c,d,e>0;c<d+sqrt(3)e','a':str(a),'b':str(b),'known_types_checked':15,'dihedral_labelings_per_type':10,'angle_matches':counts,'feasible_periodic_loci':sorted(set(feasible)),'records':records,'primary_source':'https://arxiv.org/pdf/1708.00274#page=14','scope':'All15knownmonohedralfamiliesgate; no mixedtiling existence, periodic exclusion or aperiodicity conclusion'}
 if args.output:Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result))
if __name__=='__main__':main()
