"""Cheap scalar-construction gate: four whole pinwheel triangles, not inflation search.
The rational primitive is the retained three-triangle construction module;
this producer reuses it openly and is not an independent verifier.
"""
import runpy,json
from fractions import Fraction as F
D=runpy.run_path('research/searches/pinwheel-three-triangle-convex-clusters.py')
base=((F(0),F(0)),(F(2),F(0)),(F(0),F(1)))
patches={tuple(sorted((base,)))};counts=[1]
for size in (2,3,4):
    following=set()
    for patch in patches:
        for tri in patch:
            for a,b in D['edges'](tri):
                for candidate in D['placements'](tri,a,b):
                    if all(D['interior_disjoint'](candidate,old) for old in patch):
                        following.add(tuple(sorted(patch+(candidate,))))
    patches=following;counts.append(len(patches))
classes={}
for patch in sorted(patches):
    h=D['hull']([p for tri in patch for p in tri])
    if D['area'](h)!=4:continue
    key=D['canonical'](h)
    if key in classes:continue
    central=len(h)%2==0 and all(D['add'](h[k],h[(k+len(h)//2)%len(h)])==D['add'](h[0],h[len(h)//2]) for k in range(len(h)))
    classes[key]={'boundary':D['encoding'](h),'triangles':[D['encoding'](tri) for tri in patch], 'sides':len(h),'central':central}
assert counts==[1,6,36,221]
assert len(classes)==15
large=[C for C in classes.values() if C['sides']>=6]
assert len(large)==1 and large[0]['sides']==6 and large[0]['central']
assert large[0]['boundary']==[['0','0'],['6/5','-8/5'],['2','-1'],['2','0'],['4/5','8/5'],['0','1']]
pentagons=[C for C in classes.values() if C['sides']==5]
carriers=[]
for C in pentagons:
    P=tuple((F(a),F(b)) for a,b in C['boundary'])
    supp=[]
    for k in range(5):
        e=D['sub'](P[k],P[k-1]);f=D['sub'](P[(k+2)%5],P[(k+1)%5])
        if D['cross'](e,f)==0 and D['dot'](e,f)<0:supp.append(k)
    if not supp:continue
    k=supp[0];centre2=D['add'](P[k],P[(k+1)%5])
    image=tuple(D['sub'](centre2,p) for p in P)
    H=D['hull'](P+image)
    assert D['interior_disjoint'](P,image) and D['area'](H)==8 and len(H)==6
    shifts=[D['mul'](D['sub'](D['add'](H[i+3],H[(i+4)%6]),D['add'](H[i],H[i+1])),F(1,2)) for i in range(3)]
    assert D['sub'](shifts[1],shifts[0])==shifts[2]
    assert abs(D['cross'](shifts[0],shifts[1]))==8
    carriers.append({'P':C['boundary'],'shared_edge':k,'doubled_hexagon':D['encoding'](H),'lattice':D['encoding'](tuple(shifts[:2]))})
assert len(pentagons)==3 and len(carriers)==2
print(json.dumps({'domain':'four unit-area 1-2-sqrt5 triangles, full-native-side connected, extra partial contacts allowed; anchored initial triangle; all isometries', 'raw_counts':counts,'classes':list(classes.values()),'supplementary_pentagon_carriers':carriers,'gate':'sole >=6-sided class mono-periodic; two of three pentagon classes mono-periodic, so every two-distinct-pentagon choice also has an omission escape; no parent-inflation search attempted'},indent=2))
