"""Exact positive closure cones for all 60 rooted one-private dimer words.
Run via mise exec -- conda run --no-capture-output -n arisearch python this.py.
No plane tiling or global dimer forcing is inferred by this computation.
"""
from sage.all import QQ, AA, PolynomialRing, NumberField, matrix, vector
from itertools import combinations, permutations
import json, sys
from sage.env import SAGE_VERSION

ring=PolynomialRing(QQ,"z");z=ring.gen()
field=NumberField(8*z**4-8*z**2+1,"c",embedding=((2+AA(2).sqrt())/4).sqrt())
c=field.gen();r=4*c*c-2;t=r/(4*c)
tags=("x","y","u","v","w","H");index={name:i for i,name in enumerate(tags)}
directions=[(1,0),(1/r,1/r),(0,1),(-1/r,1/r),(-1,0),(-1/r,-1/r),(0,-1),(1/r,-1/r)]
middle=sorted(set(permutations(("x","x","y","y","w"))))
words=[("H",first)+p+(last,) for first,last in (("u","v"),("v","u")) for p in middle]
assert len(words)==60
forbidden=[]
for i,j in combinations(range(6),2):
    row=[field(0)]*6;row[i]=1;row[j]=-1
    forbidden.append((tags[i]+"="+tags[j],vector(field,row)))
for host in ("x","y","w"):
    for acute in ("u","v"):
        row=[field(0)]*6;row[index[host]]=1;row[index[acute]]=-2
        forbidden.append((host+"=2"+acute,vector(field,row)))
records=[]
for word in words:
    rows=[[c,-c,1/r,-1/r,0,0],[-t,-t,1/r,1/r,-1,0]]
    for coordinate in (0,1):
        row=[field(0)]*6
        for i,name in enumerate(word):row[index[name]]+=directions[i][coordinate]
        rows.append(row)
    closure=matrix(field,rows)
    normalized=matrix(field,rows+[[1]*6])
    rhs=vector(field,[0,0,0,0,1])
    rank=normalized.rank();dimension=6-rank
    vertices={}
    if rank>closure.rank():
        for zeros in combinations(range(6),dimension):
            equations=list(normalized.rows());targets=list(rhs)
            for i in zeros:
                row=[field(0)]*6;row[i]=1
                equations.append(vector(field,row));targets.append(field(0))
            equations=matrix(field,equations);targets=vector(field,targets)
            if equations.rank()!=6 or equations.augment(matrix(field,len(targets),1,list(targets))).rank()!=6:
                continue
            point=equations.solve_right(targets)
            if all(AA(a)>=0 for a in point):vertices[tuple(point)]=point
    vertices=list(vertices.values())
    record={"word":list(word),"closure_rank":closure.rank(),"normalized_dimension":dimension,
            "vertices":[[str(a) for a in point] for point in vertices]}
    forced_zero=[tags[i] for i in range(6) if not vertices or all(point[i]==0 for point in vertices)]
    forced_equalities=[name for name,row in forbidden if vertices and all(row.dot_product(point)==0 for point in vertices)]
    record["forced_zero_coordinates"]=forced_zero
    record["forced_forbidden_equalities"]=forced_equalities
    if not forced_zero and not forced_equalities:
        limit=len(forbidden)*(len(vertices)-1)+1
        for beta in range(1,limit+1):
            weights=[field(beta)**j for j in range(len(vertices))]
            point=sum((weight*vertex for weight,vertex in zip(weights,vertices)),vector(field,[0]*6))/sum(weights)
            if all(row.dot_product(point)!=0 for _,row in forbidden):
                assert closure*point==vector(field,[0]*4) and sum(point)==1 and all(AA(a)>0 for a in point)
                record["status"]="POSITIVE_GENERIC_CLOSURE"
                record["witness"]={name:str(point[i]) for i,name in enumerate(tags)}
                record["weight_beta"]=beta
                break
        else:raise AssertionError("finite polynomial-root bound violated")
    else:record["status"]="NO_POSITIVE_DISTINCT_NONDOUBLED_CLOSURE"
    records.append(record)
result={"domain":"60 rooted native words H,u,perm(x,x,y,y,w),v and H,v,perm(...),u; all normalized positive closure cones",
        "field":"c root 8c^4-8c^2+1, 9/10<c<1, r=4c^2-2, t=r/(4c)",
        "constraints":"P/Q linear closures; sum six lengths=1; all six lengths positive and pairwise distinct; x,y,w avoid 2u,2v",
        "method":"complete vertices by all active-zero coordinate subsets; exact algebraic positivity; weighted-vertex polynomial hyperplane avoidance",
        "software":{"sage":SAGE_VERSION,"python":sys.version.split()[0]},
        "words_tested":60,"positive_generic_words":sum(rec["status"]=="POSITIVE_GENERIC_CLOSURE" for rec in records),
        "records":records}
if len(sys.argv)==3 and sys.argv[1]=="--output":
    with open(sys.argv[2],"x") as out:json.dump(result,out,indent=2)
elif len(sys.argv)==3 and sys.argv[1]=="--check":
    with open(sys.argv[2]) as inp:assert json.load(inp)==result
elif len(sys.argv)!=1:raise SystemExit("use --output newpath or --check retainedpath")
summary={"status":"COMPLETE","words_tested":60,"positive_generic_words":result["positive_generic_words"],
                  "first_witness":next((rec for rec in records if "witness" in rec),None)}
print(json.dumps(result if len(sys.argv)==1 else summary))
