# Exact complete first metric gate. Run with sage this-file.sage
import itertools, json
from pathlib import Path
K=CyclotomicField(20); z=K.gen()
def cross(a,b): return (a.conjugate()*b-a*b.conjugate())/(2*K.gen()**5)
def positive(x): return QQbar(x).real()>0
def interiors_overlap(p,q):
 for poly,other in ((p,q),(q,p)):
  for i in range(len(poly)):
   a=poly[i]; d=poly[(i+1)%len(poly)]-a
   ps=[QQbar(cross(d,v-a)).real() for v in poly]
   qs=[QQbar(cross(d,v-a)).real() for v in other]
   if max(ps)<=min(qs) or max(qs)<=min(ps):return False
 return True
rows=[]
for bs in itertools.combinations(range(8),4):
 w=''.join('B' if i in bs else 'A' for i in range(8))
 if w!=min(v[i:]+v[:i] for v in (w,w[::-1]) for i in range(8)): continue
 for es in itertools.combinations(range(8),2):
  ends=[j for i in es for j in (i,(i+1)%8)]
  if len(set(ends))!=4 or set(ends)!=set(bs):continue
  # edge i leaves vertex i; exterior turns A=36, B=54 degrees.
  ds=[K(1)]
  for i in range(1,8): ds.append(ds[-1]*z**(2 if w[i]=='A' else 3))
  s=sum(ds[i] for i in range(8) if i not in es)
  u,v=[ds[i] for i in es]; det=cross(u,v)
  row={'word':w,'qq_edges':list(es),'det':str(det)}
  if det==0:
   row['status']='singular'; row['compatible']=cross(u,s)==0; row['unit_sum']=str(s); row['direction_ratio']=str(v/u)
  else:
   x=-cross(s,v)/det; y=-cross(u,s)/det
   ls=[x if i==es[0] else y if i==es[1] else K(1) for i in range(8)]
   assert sum(a*b for a,b in zip(ls,ds))==0
   pts=[K(0)]
   for i in range(7):pts.append(pts[-1]+ls[i]*ds[i])
   pos=positive(x) and positive(y)
   convex=pos and all(positive(cross(ds[i],pts[j]-pts[i])) for i in range(8) for j in range(8) if j not in (i,(i+1)%8))
   neighbors=[]
   for i in range(8):
    if i in es:continue
    p=[pts[i]]; d=ds[i]
    for j in range(4): p.append(p[-1]+d); d*=z**(-4)
    assert p[-1]+d==p[0]
    neighbors.append((i,p))
   collisions=[]
   for (i,p),(j,q) in itertools.combinations(neighbors,2):
    if set(p)==set(q):continue
    if interiors_overlap(p,q):collisions.append([i,j])
   row['forced_p_collisions']=collisions
   pp=[]
   nd=dict(neighbors)
   for i in range(8):
    if w[i]!='A':continue
    p=nd[(i-1)%8];q=nd[i]
    common=set(p).intersection(q)
    assert len(common)==2
    a,b=list(common); assert (a-b)*(a-b).conjugate()==1
    pp.append(i)
   row['verified_pp_at_A']=pp
   seams=[]
   base=[('Q',pts)]+[('P'+str(i),p) for i,p in neighbors]
   for ti in es:
    for si in es:
     for reflected in (False,True):
      a,b=pts[ti],pts[(ti+1)%8];c,d=pts[si],pts[(si+1)%8]
      if reflected:
       scale=(b-a)/(d-c).conjugate()
       def f(v):return a+scale*(v-c).conjugate()
      else:
       scale=(a-b)/(d-c)
       def f(v):return b+scale*(v-c)
      moving=[(name,[f(v) for v in poly]) for name,poly in base]
      bad=[]
      for name,p in base:
       for name2,q in moving:
        if set(p)==set(q):continue
        if interiors_overlap(p,q):bad.append([name,name2])
      seams.append({'target':ti,'source':si,'reflected':reflected,'collisions':bad})
   row['immediate_qq_seams']=seams
   row.update(lengths=[str(x),str(y)],approx=[float(QQbar(x).real()),float(QQbar(y).real())],positive=bool(pos),strict_convex=bool(convex),equal=bool(x==y),status='unique')
  rows.append(row)
out={'field':'Q(zeta_20), zeta_20=exp(2*pi*i/20)','domain':'all 70 labeled 4A4B angle words; dihedral canonical representatives with perfect matching of B vertices by two cycle edges','results':rows}
path=Path('research/searches/regular-pentagon-octagon-144-126-first-gate-2026-10-19.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
