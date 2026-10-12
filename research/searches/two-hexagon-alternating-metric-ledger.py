#!/usr/bin/env python3
"""Complete necessary ALT/ALT metric alphabet ledger, before ring search.

203 native A side partitions, exact parity occupancy h, deduplicated integer
B native length multiplicities. Stores multinomial word counts, not native
ring enumeration or sampled geometry.
"""
from collections import Counter
from fractions import Fraction
from math import factorial
import json
import sys

H=[Fraction(0),Fraction(1,6),Fraction(1,4),Fraction(1,3),Fraction(1,2),
   Fraction(2,3),Fraction(3,4),Fraction(5,6),Fraction(1)]

def partitions(n):
    def walk(p):
        if len(p)==n:
            yield tuple(p);return
        for j in range(max(p)+2):yield from walk(p+[j])
    yield from walk([0])

def count_words(mult):
    result=factorial(sum(mult))
    for m in mult:result//=factorial(m)
    return result

def main(path):
    rows=[];hist=Counter();word_total=0;vector_total=0
    for a in partitions(6):
        k=max(a)+1
        even=tuple(sum(a[j]==c for j in (0,2,4)) for c in range(k))
        odd=tuple(sum(a[j]==c for j in (1,3,5)) for c in range(k))
        balanced=even==odd
        vectors={}
        for h in H:
            mult=tuple(2*(h*e+(1-h)*o) for e,o in zip(even,odd))
            if not all(v.denominator==1 for v in mult):continue
            mult=tuple(int(v) for v in mult)
            assert sum(mult)==6 and all(v>=0 for v in mult)
            vectors.setdefault(mult,[]).append(str(h))
        ledgers=[]
        for mult,hs in sorted(vectors.items()):
            n=count_words(mult);word_total+=n;vector_total+=1
            ledgers.append({'B_native_multiplicities':mult,
                            'compatible_AB_even_A_proportions':'ALL_REAL_H_IN_0_1' if balanced else hs,
                            'B_native_word_count':n})
        row={'A_native_side_partition':a,'even_multiplicities':even,'odd_multiplicities':odd,
             'parity_balanced':balanced,'A_has_native_side_period_two':a[0]==a[2]==a[4] and a[1]==a[3]==a[5],
             'distinct_B_multiplicity_ledgers':ledgers,
             'deduplicated_B_native_word_count':sum(x['B_native_word_count'] for x in ledgers)}
        rows.append(row);hist[(k,balanced)]+=1
    assert len(rows)==203
    result={'scope':'Necessary complete metric alphabet for trivalent same-colour AAB with A=ALT,B=ALT; all native A side equality partitions; unmarked metrics and reflections; no geometric extension claim',
            'finite_unbalanced_h_domain':[str(h) for h in H],
            'A_partition_count':len(rows),'parity_balanced_partition_count':sum(r['parity_balanced'] for r in rows),
            'distinct_A_partition_B_multiplicity_count':vector_total,
            'distinct_A_partition_B_native_word_count':word_total,
            'partition_histogram_by_length_classes_and_balance':[
                {'length_classes':k,'balanced':b,'count':n} for (k,b),n in sorted(hist.items())],
            'rows':rows}
    with open(path,'w') as f:json.dump(result,f,indent=2)
    print('partitions',len(rows),'balanced',result['parity_balanced_partition_count'],
          'multiplicity ledgers',vector_total,'native words',word_total,flush=True)
    print('histogram',result['partition_histogram_by_length_classes_and_balance'],flush=True)
    print('distinct A6 case',rows[-1],flush=True)

if __name__=='__main__':main(sys.argv[1])
