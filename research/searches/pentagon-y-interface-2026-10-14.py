"""Bounded exact Y-interface geometry and native/flat endpoint gate. No cover claim."""
import itertools,json
from fractions import Fraction as F
from pathlib import Path
T={"r":(2,0),"a":(4,-1),"b":(1,1),"c":(3,-1),"g":(3,0),"d":(0,2)}
# Each arm: squared length, far-corner type. Reflection reverses arms.
ARM={"r":((4,"a"),(4,"a")),"a":((4,"r"),(5,"b")),"b":((5,"a"),(2,"b")),"c":((2,"g"),(5,"d")),"g":((2,"c"),(4,"g")),"d":((5,"c"),(5,"c"))}
P=[(0,0),(2,0),(3,2),(2,3),(0,2)]
Q=[(2,3),(1,4),(-1,4),(-2,3),(0,2)]
H=[(-2,0),(2,0),(3,2),(1,4),(-1,4),(-3,2)]
def cross(a,b,c):return (b[0]-a[0])*(c[1]-b[1])-(b[1]-a[1])*(c[0]-b[0])
def area(v):return F(sum(v[i][0]*v[(i+1)%len(v)][1]-v[i][1]*v[(i+1)%len(v)][0] for i in range(len(v))),2)
def add(word):return tuple(sum(T[t][j] for t in word) for j in range(2))
def completions(target):
 out=[]
 for k in range(6):
  for w in itertools.combinations_with_replacement(T,k):
   if add(w)==target:out.append(list(w))
 # At most one flat sector can fit a nonempty corner completion.
 if target==(4,0):out.append(["flat"])
 return out
stars=[]
for k in range(2,6):
 for word in itertools.combinations_with_replacement(T,k):
  if add(word)==(8,0):stars.append(word)
flatstars=[]
for k in range(1,4):
 for word in itertools.combinations_with_replacement(T,k):
  if add(word)==(4,0):flatstars.append(word)
records=[]
for star in stars:
 orders=sorted(set(itertools.permutations(star)))
 raw=passed=0; survivors=[]
 for w in orders:
  for flips in itertools.product((0,1),repeat=len(w)):
   arms=[ARM[t][::(-1 if f else 1)] for t,f in zip(w,flips)]
   if any(arms[i][1][0]!=arms[(i+1)%len(w)][0][0] for i in range(len(w))):continue
   raw+=1; ends=[]; valid=True
   for i in range(len(w)):
    x,y=arms[i][1][1],arms[(i+1)%len(w)][0][1]
    sx,sy=add((x,y)); co=completions((8-sx,-sy))
    ends.append({"length_squared":arms[i][1][0],"far_types":[x,y],"completions":co})
    if not co:valid=False
   if valid:
    passed+=1
    if len(survivors)<2:survivors.append({"cyclic_word":w,"flips":flips,"endpoints":ends})
 records.append({"star":star,"oriented_length_matches":raw,"endpoint_survivors":passed,"examples":survivors})
assert all(cross(v[i],v[(i+1)%len(v)],v[(i+2)%len(v)])>0 for v in (P,Q,H) for i in range(len(v)))
assert 2*area(P)+area(Q)==area(H)
# Parent corner alpha,beta,gamma: (4,-1),(1,1),(3,0).
parent_stars=[w for w in stars if set(w)<=set("abg")]
assert parent_stars==[("a","b","g")]
# H alpha arms lengths 4,sqrt5; beta sqrt5,sqrt8; gamma sqrt8,2.
parent_arm={"a":(16,5),"b":(5,8),"g":(8,4)}
parent_matches=0
for w in itertools.permutations("abg"):
 for f in itertools.product((0,1),repeat=3):
  arm=[parent_arm[t][::(-1 if z else 1)] for t,z in zip(w,f)]
  if all(arm[i][1]==arm[(i+1)%3][0] for i in range(3)):parent_matches+=1
assert parent_matches==0
report={"status":"LOCAL_TWO_SHAPE_PARTITION; BOTH_OMISSIONS_EXCLUDED; INTACT_PARENT_ASSEMBLY_EXCLUDED; INFINITE_COVER_UNPROVED", "angle_basis":"(pi/4, theta), theta=atan(2); theta/pi irrational", "P":P,"Q":Q,"H":H,"areas":{"P":str(area(P)),"Q":str(area(Q)),"H":str(area(H))},"native_stars":records,"flat_stars":flatstars,"parent_native_stars":parent_stars,"parent_whole_edge_matches":parent_matches,"scope":"Stars exhaustive by exact irrational angle coefficients; endpoint checks necessary only, no infinite extension or universal decoder."}
print(json.dumps(report,indent=2))
if __name__=="__main__":
 import argparse
 ap=argparse.ArgumentParser();ap.add_argument("--output");args=ap.parse_args()
 if args.output:Path(args.output).write_text(json.dumps(report,indent=2)+"\n")
