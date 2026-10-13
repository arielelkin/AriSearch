#!/usr/bin/env python3
from itertools import product
from pathlib import Path
import json
placements=list(product(range(6),(1,-1)))
Ac=(0,0,1,1,2,2);As=(0,0,1,1,2,2)
Bc=(0,0,1,2,2,1);Bs=(0,0,1,2,1,0)
def profile(c,l,r,s):
    return dict(native_rotation=r,native_sign=s,
        corners=tuple(c[(r+s*k)%6] for k in range(6)),
        sides=tuple(l[(r+k)%6] if s==1 else l[(r-k-1)%6] for k in range(6)))
def main():
    A=[profile(Ac,As,r,s) for r,s in placements];B=[profile(Bc,Bs,r,s) for r,s in placements]
    rows=[];total=0;seamsurv=0;fullsurv=0
    for bi,b in enumerate(B):
        choices=[]
        for k in range(6):
            choices.append([ai for ai,a in enumerate(A) if a["corners"][(k+2)%6]==b["corners"][k]
                and a["corners"][(k+3)%6]==b["corners"][(k-1)%6]
                and a["sides"][(k+2)%6]==b["sides"][(k-1)%6]])
        states=[]
        for ring in product(*choices):
            total+=1;bad=[];outer=[]
            for k in range(6):
                a=A[ring[k]];d=A[ring[(k+1)%6]]
                matched=(a["sides"][(k+1)%6],d["sides"][(k+4)%6])
                if matched[0]!=matched[1]:bad.append(k)
                colours=(a["corners"][(k+1)%6],d["corners"][(k+5)%6])
                arms=(a["sides"][k],d["sides"][(k+5)%6]);opts=[]
                species="B" if colours[0]==colours[1] else "A"
                colour=colours[0] if species=="B" else 3-colours[0]-colours[1]
                cw,sw=(Bc,Bs) if species=="B" else (Ac,As)
                for slot in range(6):
                    for sign in (1,-1):
                        if cw[slot]==colour and tuple((sw[(slot-1)%6],sw[slot])[::sign])==arms:
                            opts.append(dict(species=species,native_corner=slot,arm_sign=sign))
                outer.append(dict(endpoint_colours=colours,exposed_arms=arms,completions=opts))
            if not bad:seamsurv+=1
            if not bad and all(o["completions"] for o in outer):fullsurv+=1
            states.append(dict(A_native_tuple=ring,AA_bad_seams=bad,outer_endpoints=outer,
                survives=not bad and all(o["completions"] for o in outer)))
        rows.append(dict(B_native_placement=bi,A_choices=choices,states=states))
    result=dict(scope="Genericfive-star language; actualpositiveconvex A001122aabbcc and B001221aabcba with distincta,b,c;12nativeplacements inclreflections; completeAB ring tuples and necessaryAA/outercompletion gates",
        A_placements=A,B_placements=B,rows=rows,counts=dict(AB_rings=total,AA_seam_survivors=seamsurv,outer_complete_survivors=fullsurv))
    Path("research/certificates/terra-001221-native-ring.json").write_text(json.dumps(result,indent=2)+"\n")
    print(result["counts"])
    for row in rows:
        print(row["B_native_placement"],len(row["states"]),[(s["AA_bad_seams"],[i for i,o in enumerate(s["outer_endpoints"]) if not o["completions"]]) for s in row["states"]])
if __name__=="__main__":main()
