#!/usr/bin/env python3
"""Exact unit-Robinson partitions of U/V; marked Penrose legality unproved."""
from pathlib import Path
import importlib.util
import json
import argparse
from itertools import combinations
from sage.all import AA, QQ, QQbar
spec=importlib.util.spec_from_file_location("metric",Path(__file__).with_name("pentagrid-golden-metric.py"))
metric=importlib.util.module_from_spec(spec);spec.loader.exec_module(metric)
K,z,phi=metric.K,metric.z,metric.phi
REF={"thin":[K(0),K(1),z],"fat":[K(0),K(1),z**3]}
TEMPLATES={"thin":[("fat",[K(0),K(1),phi*z]),("thin",[K(1),phi,phi*z])],"fat":[("fat",[phi,phi-1,z**2]),("thin",[K(0),phi-1,z**2]),("fat",[K(0),z**2,phi*z**3])]}

def cross(a,b):return (a.conjugate()*b-a*b.conjugate())/(z-z.conjugate())
def real(a):
    q=QQbar(a);assert q.imag()==0
    return AA(q.real())
def area(p):return sum(cross(p[j],p[(j+1)%len(p)])for j in range(len(p)))/2

def isometry(source,target):
    for reflected in(False,True):
        p=[w.conjugate()if reflected else w for w in source]
        for k in range(10):
            r=z**k
            for t in target:
                q=[r*w+t for w in p]
                if set(q)==set(target):return r,t,reflected
    raise AssertionError((source,target))

def dissect(name,level,target):
    if not level:return[(name,list(target))]
    r,t,reflected=isometry([phi**level*w for w in REF[name]],target)
    out=[]
    for child,p in TEMPLATES[name]:
        q=[phi**(level-1)*w for w in p]
        q=[r*(w.conjugate()if reflected else w)+t for w in q]
        out.extend(dissect(child,level-1,q))
    return out

def ccw(p):
    p=list(p)
    if real(area(p))<0:p[1],p[2]=p[2],p[1]
    assert real(area(p))>0
    return p

def separated(p,q):
    for a,b in((p,q),(q,p)):
        for i in range(3):
            e=a[(i+1)%3]-a[i]
            if all(real(cross(e,w-a[i]))<=0 for w in b):return True
    return False

def verify(poly,patch):
    out=[];counts={"thin":0,"fat":0}
    for name,p in patch:
        p=ccw(p);r,t,reflection=isometry(REF[name],p);counts[name]+=1
        assert real(area(p))==(real(phi)/2 if name=="fat"else AA(1)/2)
        for j in range(5):
            e=poly[(j+1)%5]-poly[j]
            assert all(real(cross(e,w-poly[j]))>=0 for w in p)
        out.append({"kind":name,"vertices":[metric.coefficients(w)for w in p],"reference_isometry":{"rotation":metric.coefficients(r),"translation":metric.coefficients(t),"reflected":reflection}})
    vertices=[[K([QQ(a)for a in row])for row in d["vertices"]]for d in out]
    for i,j in combinations(range(len(out)),2):assert separated(vertices[i],vertices[j]),(i,j)
    assert sum(area(p)for p in vertices)==area(poly)
    return {"parent_vertices":[metric.coefficients(w)for w in poly],"triangle_counts":counts,"triangles":out,"all_contained":True,"all_interior_disjoint":True,"exact_area_coverage":True,"pair_separation_tests":len(out)*(len(out)-1)//2}

def contacts(out):
    polygons=[[K([QQ(a)for a in row])for row in tri["vertices"]]for tri in out]
    records=[]
    for i,j in combinations(range(len(polygons)),2):
        p,q=polygons[i],polygons[j]
        for e in range(3):
            a,b=p[e],p[(e+1)%3];v=b-a
            for f in range(3):
                c,d=q[f],q[(f+1)%3]
                if cross(v,c-a)!=0 or cross(v,d-a)!=0:continue
                x,y=(c-a)/v,(d-a)/v
                lo=max((K(0),min((x,y),key=real)),key=real)
                hi=min((K(1),max((x,y),key=real)),key=real)
                if real(lo)>=real(hi):continue
                records.append({"first_triangle":i,"first_edge":e,"second_triangle":j,"second_edge":f,"whole_edge_on_both":set((a,b))==set((c,d)),"overlap_start":metric.coefficients(a+lo*v),"overlap_end":metric.coefficients(a+hi*v)})
    return records

def certificate():
    U=[K(0),phi**3,z+z**2+z**3,z**2+z**3,z**3]
    P=z**2
    patch_u=dissect("thin",3,[U[0],U[1],U[2]])
    patch_u += [("fat",[U[2],U[3],P]),("thin",[U[3],U[4],P]),("thin",[U[4],U[0],P])]
    V=[K(0),K(1),1+(1+3*phi)*z**3,2*phi**2*z**3,2*phi*z**4]
    a,b,c=V[4],V[0],V[3]
    ab,bc,ca=(a+b)/2,(b+c)/2,(c+a)/2
    medial=[(a,ab,ca),(b,bc,ab),(c,ca,bc),(ab,bc,ca)]
    patch_v=[]
    for tri in medial:patch_v.extend(dissect("fat",1,tri))
    for j in range(4):
        t=j*z**3
        patch_v += [("fat",[t,t+1,t+z**3]),("fat",[t+1,t+1+z**3,t+z**3])]
    t=4*z**3;s=phi-1
    A=[t+j*s*z**3 for j in range(3)]
    B=[t+1+j*s*z**3 for j in range(4)]
    patch_v += [("thin",[A[0],B[0],B[1]]),("thin",[A[0],A[1],B[1]]),("thin",[A[1],B[1],B[2]]),("thin",[A[1],A[2],B[2]]),("thin",[A[2],B[2],B[3]])]
    u=verify(U,patch_u);v=verify(V,patch_v)
    for record in(u,v):
        record["positive_internal_contacts"]=contacts(record["triangles"])
        record["partial_contact_count"]=sum(not q["whole_edge_on_both"]for q in record["positive_internal_contacts"])
    assert u["triangle_counts"]=={"thin":7,"fat":9}
    assert v["triangle_counts"]=={"thin":9,"fat":16}
    # A mandatory vertex of the chosen medial cap lies strictly inside a
    # whole edge of the chosen rhomb row.  This rejects every refinement
    # respecting these two macro pieces, independently of arrow markings.
    midpoint=phi**2*z**3
    assert real(phi**2)>2 and real(phi**2)<3
    cap_indices=[i for i,(_,p)in enumerate(patch_v[:12])if midpoint in p]
    assert cap_indices
    row_edge=(2*z**3,3*z**3)
    assert set(row_edge).issubset(set(patch_v[16][1]))
    assert cross(row_edge[1]-row_edge[0],midpoint-row_edge[0])==0
    rejection={"scope":"Selected medial fat-cap / four-unit-rhomb-row compiler only",
               "mandatory_cap_vertex":metric.coefficients(midpoint),
               "cap_unit_triangle_indices_with_vertex":cap_indices,
               "row_unit_triangle":16,
               "row_whole_edge":[metric.coefficients(w)for w in row_edge],
               "fraction_of_row_edge":metric.coefficients(phi**2-2),
               "strict_fraction_between_zero_and_one":True,
               "conclusion":"A native triangle vertex in another whole edge's interior is forbidden in an edge-to-edge source patch."}
    return {"field":"Q(z), z^4-z^3+z^2-z+1=0, z=exp(pi*i/5),phi=z+z^(-1)","scope":"Exact geometric partitions into unit Robinson triangles ONLY; these specific partitions fail edge-to-edge source legality; global repartition and shape-only forcing unproved","reference_triangles":{name:[metric.coefficients(w)for w in p]for name,p in REF.items()},"U":u,"V":v,"U_construction":"phi^3 thin triangle plus quad cut at z^2 into two thin and one fat","V_construction":"2phi fat triangle split medially then phi-fat recursion; four unit fat rhombs plus alternating five-thin strip","content_matrix_thin_fat_rows_U_V_columns":[[7,9],[9,16]],"minimal_medial_interface_rejection":rejection,"marked_source_legality":"These exact partitions are not edge-to-edge, so cannot be patches of actual unit Penrose rhomb halves"}

def render(data,path):
    # Floating conversion is for this diagnostic SVG only.
    panels=[]
    for name in("U","V"):
        d=data[name];vertices=[[complex(QQbar(K([QQ(a)for a in row])))for row in tri["vertices"]]for tri in d["triangles"]]
        coords=[w for p in vertices for w in p]
        xmin,xmax=min(w.real for w in coords),max(w.real for w in coords)
        ymin,ymax=min(w.imag for w in coords),max(w.imag for w in coords)
        panels.append((name,d,vertices,xmin,xmax,ymin,ymax))
    svg=["<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"1100\" height=\"750\" viewBox=\"0 0 1100 750\">","<rect width=\"1100\" height=\"750\" fill=\"white\"/>","<text x=\"30\" y=\"32\" font-family=\"sans-serif\" font-size=\"20\">Exact unit Robinson partitions: geometric legality only</text>","<text x=\"30\" y=\"57\" font-family=\"sans-serif\" font-size=\"14\">Blue = fat; amber = thin. Partial contacts exclude these patches from an edge-to-edge source.</text>"]
    for panel,(name,d,vertices,xmin,xmax,ymin,ymax)in enumerate(panels):
        scale=min(470/(xmax-xmin),590/(ymax-ymin));ox=40+550*panel;oy=100
        def point(w):return(ox+scale*(w.real-xmin),oy+scale*(ymax-w.imag))
        svg.append("<text x=\"%d\" y=\"90\" font-family=\"sans-serif\" font-size=\"17\">%s: %s</text>"%(ox,name,d["triangle_counts"]))
        for i,(tri,p)in enumerate(zip(d["triangles"],vertices)):
            pts=" ".join("%.6f,%.6f"%point(w)for w in p)
            color="#a8d5ee"if tri["kind"]=="fat"else"#ffd889"
            svg.append("<polygon points=\"%s\" fill=\"%s\" stroke=\"#404040\" stroke-width=\"1.1\"/>"%(pts,color))
            cx,cy=point(sum(p)/3)
            svg.append("<text x=\"%.6f\" y=\"%.6f\" text-anchor=\"middle\" font-family=\"sans-serif\" font-size=\"10\">%d</text>"%(cx,cy,i))
    svg.append("</svg>");Path(path).write_text("\n".join(svg)+"\n")

if __name__=="__main__":
    if not __debug__:raise RuntimeError("Exact assertions require Python without -O")
    parser=argparse.ArgumentParser();parser.add_argument("--output");parser.add_argument("--svg-output");args=parser.parse_args();data=certificate();payload=json.dumps(data,indent=2)+"\n"
    if args.svg_output:render(data,args.svg_output)
    if args.output:Path(args.output).write_text(payload)
    else:print(payload,end="")
