#!/usr/bin/env python3
"""640 exact six-piece-wheel boundary matrices; no point/metric search."""
from sage.all import QQ, PolynomialRing, NumberField, matrix
from itertools import combinations, product
from pathlib import Path
import argparse, json

def build():
    R=PolynomialRing(QQ,'t');t=R.gen()
    K=NumberField(t**4-3*t**2-3,'a');a=K.gen()
    records=[]
    for center_large,nlarge in [(False,3),(True,2)]:
        for big in combinations(range(5),nlarge):
            scales=[a if i in big else K(1) for i in range(5)]
            for refl in product([0,1],repeat=5):
                M=matrix(K,5,5)
                for i in range(5):
                    M[i,i]=a*a
                    for corner,native in [(i,(i-1)%5 if refl[i] else i),
                         ((i+1)%5,(i+1)%5 if refl[(i+1)%5] else i)]:
                        M[i,native]-=scales[corner]
                det=M.det()
                assert det!=0
                coeff=[int(c)for c in det.list()]+[0]*4
                records.append({'central_large':center_large,'large_corners':list(big),
                    'reflections':list(refl),'determinant_coefficients':coeff[:4]})
    assert len(records)==640
    return {'minimal_polynomial':'t^4-3*t^2-3','area_multiplier':'(3+sqrt(21))/2',
      'status':'NO DISTINCT-ANGLE SIX-PIECE WHEEL AT ANY REAL POSITIVE SIDE LENGTHS',
      'case_count':640,'zero_determinant_count':0,'records':records}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);ap.add_argument('--check',type=Path)
    args=ap.parse_args();data=build()
    if args.check:assert json.loads(args.check.read_text())==data
    if args.output:args.output.write_text(json.dumps(data,indent=2)+'\n')
    print('PASS: all640 exact six-piece-wheel boundary matrices are nonsingular.')
