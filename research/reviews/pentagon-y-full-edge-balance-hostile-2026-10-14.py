"""Independent full-edge local atlas, ray incidence, and torus balance audit."""
import itertools,json
import sympy as s
polys=[[(0,0),(2,0),(3,2),(2,3),(0,2)],[(2,3),(1,4),(-1,4),(-2,3),(0,2)]]
words=['rabba','cggcd']
angles={'r':(2,0),'a':(4,-1),'b':(1,1),'c':(3,-1),'g':(3,0),'d':(0,2)}
def sq(a,b):return sum((x-y)**2 for x,y in zip(a,b))
arms={}
edges4=[]
for poly,word in zip(polys,words):
 e=[]
 for i,t in enumerate(word):
  arm=(sq(poly[i],poly[i-1]),sq(poly[i],poly[(i+1)%5]))
  if t in arms:assert arm==arms[t] or arm[::-1]==arms[t]
  else:arms[t]=arm
  if sq(poly[i],poly[(i+1)%5])==4:e.append(''.join(sorted(t+word[(i+1)%5])))
 edges4.append(e)
assert edges4==[['ar','ar'],['gg']]
allstars=[];viable={};raysets={}
for n in range(2,6):
 for star in itertools.combinations_with_replacement(sorted(angles),n):
  if tuple(sum(angles[t][j] for t in star) for j in [0,1])!=(8,0):continue
  key=''.join(star);allstars.append(key);records=[]
  for order in set(itertools.permutations(star)):
   for flip in itertools.product([False,True],repeat=n):
    v=[arms[t][::-1] if f else arms[t] for t,f in zip(order,flip)]
    if any(v[i][1]!=v[(i+1)%n][0] for i in range(n)):continue
    ray=tuple(sorted((''.join(sorted(order[i]+order[(i+1)%n])),v[i][1]) for i in range(n)))
    records.append(ray)
  if records:viable[key]=len(records);raysets[key]=set(records)
assert set(allstars)=={'aad','abg','bbcc','ggr','rrrr','bcrr','ccdr'}
assert set(viable)=={'aad','abg','bbcc','ggr','rrrr'}
assert raysets['ggr']=={(('gg',2),('gr',4),('gr',4))}
assert raysets['abg']=={(('ab',5),('ag',4),('bg',2))}
# Every Q's gg length4 edge must match a P ar length4 edge.
# It has one gr endpoint and one ag endpoint. The checked ray tables give
# exactly 2 gr endpoints at each ggr vertex and 1 ag at each abg vertex.
x,y,z,t,w,p,q=s.symbols('x y z t w p q')
eq=[x+4*w-p,2*y+t-2*p,2*z+t-2*p,2*z-2*q,2*x+t-2*q,y-q,2*x-q,t-q]
M=s.linear_eq_to_matrix(eq,[x,y,z,t,w,p,q])[0]
ker=M.nullspace()
assert len(ker)==1
v=ker[0]*4
assert v==s.Matrix([2,4,4,4,1,6,4])
assert s.simplify(x+y+z+t+w-5*(p+q)/2+p+q).subs(dict(zip([x,y,z,t,w,p,q],v)))==0
print(json.dumps({'angle_only_stars':allstars,'length_compatible_stars':viable,
 'rgg_ray_records':str(raysets['ggr']),'abg_ray_records':str(raysets['abg']),
 'integer_solution_multiple':['2w','4w','4w','4w','w','6w','4w'],
 'scope':'finite full-native-edge flat torus; no partial-contact or infinite-cover conclusion'},indent=2))
