#!/usr/bin/env python3
"""Eleven forced native B words; exact local/fixed-metric closure gate."""
from itertools import permutations,product
from pathlib import Path
import json
from sage.all import CyclotomicField,QQbar,AA
K=CyclotomicField(360);z=K.gen();emb=K.hom([QQbar.zeta(360)],QQbar)
cross=lambda a,b:(a.conjugate()*b-a*b.conjugate())/(2*z**90)
S=(1+z**67,z**126+z**185,z**239+z**293)
v=(cross(S[1],S[2]),cross(S[2],S[0]),cross(S[0],S[1]))
lengths=tuple(x/v[0] for x in v)
Acol=(0,0,1,1,2,2);Aside=(0,0,1,1,2,2)
Bangles=(134,118,108)
canonical=lambda w:min(t[k:]+t[:k] for t in (w,w[::-1]) for k in range(6))
def main():
    fans=[]
    for colour in range(3):
        corners=[i for i,c in enumerate(Acol) if c==colour];pairs=set();details=[]
        for i,j in product(corners,repeat=2):
            ai=(Aside[(i-1)%6],Aside[i]);aj=(Aside[(j-1)%6],Aside[j])
            for si,sj in product(range(2),repeat=2):
                if ai[si]==aj[sj]:
                    pair=(ai[1-si],aj[1-sj]);pairs.add(pair)
                    details.append(dict(A_corners=(i,j),AA_matching_class=ai[si],B_ordered_arms=pair))
        fans.append(dict(colour=colour,ordered_pairs=sorted(pairs),details=details))
    palette={}
    for i in range(6):
        pair=tuple(sorted((Acol[i],Acol[(i+1)%6])))
        assert pair not in palette or palette[pair]==Aside[i]
        palette[pair]=Aside[i]
    assert len(palette)==6
    words=sorted({canonical(w) for w in permutations(Acol)})
    rows=[]
    for w in words:
        sides=tuple(palette[tuple(sorted((w[i],w[(i+1)%6])))] for i in range(6))
        assert all((sides[(i-1)%6],sides[i]) in fans[w[i]]["ordered_pairs"] for i in range(6))
        dirs=[0]
        for i in range(1,6):dirs.append(dirs[-1]+180-Bangles[w[i]])
        residue=sum((lengths[s]*z**d for s,d in zip(sides,dirs)),K(0))
        row=dict(B_word=w,forced_side_classes=sides,directions=dirs,
                 closes=residue==0,exact_residue_polynomial=str(residue))
        if residue==0:
            vs=[K(0)]
            for s,d in zip(sides,dirs):vs.append(vs[-1]+lengths[s]*z**d)
            val=lambda x:AA(emb(x).real())
            assert all(val(cross(vs[i+1]-vs[i],vs[j]-vs[i]))>0 for i in range(6) for j in range(6) if j not in(i,(i+1)%6))
            assert sides[:3]==sides[3:] and w[:3]==w[3:]
            row["strictly_convex"]=True;row["centrally_symmetric"]=True
        rows.append(row);print(w,sides,"CLOSED" if residue==0 else "NONZERO",flush=True)
    assert [tuple(r["B_word"]) for r in rows if r["closes"]]==[(0,1,2,0,1,2)]
    out=dict(scope="Fixed exact positive A001122 with sidewordaabbcc; all11 B bracelets; unique necessary metric words from samecolour AAB fans and AB endpoint compatibility",fans=fans,palette=[dict(endpoint_pair=k,side_class=v) for k,v in sorted(palette.items())],B_rows=rows,
             conclusion="Any mixed defectfree field with this A forces central B012012, hence a monohedral periodic escape; no mixed extension asserted")
    Path("research/certificates/terra-001122-b-neighbourhood.json").write_text(json.dumps(out,indent=2)+"\n")
if __name__=="__main__":main()
