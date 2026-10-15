"""Declared OFF-NORMAL-M necessary H-only gate for unequal mark-local ray cuts.
16 receiving hexagons; 12 D6 aliases each; exact rational-degree LRA.
No P congruence, cap reconstruction, metric closure, or tiling is inferred.
"""
import z3,json,argparse
from pathlib import Path
s=z3.Solver();s.set(timeout=60000)
H=[z3.Real('H%d'%i) for i in range(6)]
s.add(sum(H)==720,*[z3.And(h>0,h<180) for h in H])
b={(Z,r):z3.Real('b_'+Z+'_'+r) for Z in ['X','Y'] for r in ['tail','head']}
s.add(*[z3.And(x>0,x<90) for x in b.values()])
thetaVar={(Z,r):z3.Real('theta_'+Z+'_'+r) for Z in ['X','Y'] for r in ['tail','head']}
for Z in ['X','Y']:
 s.add(thetaVar[Z,'tail']>0,thetaVar[Z,'head']>0,thetaVar[Z,'tail']+thetaVar[Z,'head']==180-b[Z,'tail']-b[Z,'head'])
E={(Z,r,k):z3.Real('E_'+Z+'_'+r+'_'+str(k)) for Z in ['X','Y'] for r in ['tail','head'] for k in [0,1]}
for Z in ['X','Y']:
 for r in ['tail','head']:
  pair=[E[Z,r,k] for k in [0,1]]
  theta=thetaVar[Z,r]
  s.add(sum(pair)==180+theta,*[z3.And(x>theta,x<180) for x in pair])
ARROWS={'thin':[(0,1,'X'),(2,1,'X'),(2,3,'Y'),(0,3,'Y')],
        'thick':[(0,1,'X'),(1,2,'Y'),(3,2,'Y'),(0,3,'X')]}
records=[]
for species,arrows in ARROWS.items():
 for parity in [0,1]:
  for receiver in range(1-parity,4,2):
   T,J,Z=arrows[receiver]
   for j in [receiver,(receiver+1)%4]:
    incoming='tail' if j==T else 'head'
    donor=(j-1)%4 if receiver==j else j
    assert donor%2==parity
    DT,DH,DZ=arrows[donor]
    outgoing='tail' if j==DT else 'head'
    sigma=(36 if j%2==0 else 144) if species=='thin' else (72 if j%2==0 else 108)
    alpha=sigma+b[Z,incoming]-b[DZ,outgoing]
    theta=thetaVar[Z,incoming]
    choices=[]
    for offset in range(6):
     for direction in [-1,1]:
      angles=[H[(offset+direction*k)%6] for k in range(6)]
      M=angles[3];inner=360-alpha-theta-M
      choices.append(z3.And(angles[0]==alpha,angles[1]==E[Z,incoming,0],angles[2]==E[Z,incoming,1],M>0,inner>0,inner<180,angles[4]>inner,angles[5]>inner))
    s.add(z3.Or(*choices))
    records.append(dict(species=species,parity=parity,receiver=receiver,endpoint=j,alpha=alpha,choices=choices))
status=s.check()
result=dict(status=str(status),domain='OFF-NORMAL-M: 16 receiving H words, all12 D6 aliases, whole donor-apex split identity; necessary angle gate only',timeout_ms=60000)
if status==z3.sat:
 m=s.model();result['H']=[str(m.eval(x)) for x in H];result['base']={str(k):str(m.eval(x)) for k,x in b.items()};result['external']={str(k):str(m.eval(x)) for k,x in E.items()};result['theta']={str(k):str(m.eval(x)) for k,x in thetaVar.items()};result['aliases']=[{key:value for key,value in r.items() if key not in ('alpha','choices')}|dict(alpha=str(m.eval(r['alpha'])),alias=next(j for j,c in enumerate(r['choices']) if z3.is_true(m.eval(c)))) for r in records]
 if any(not z3.is_rational_value(m.eval(x)) for x in H+list(b.values())+list(E.values())+list(thetaVar.values())):raise AssertionError('nonrational unexpected')
elif status==z3.unknown:result['reason']=s.reason_unknown()
print(json.dumps(result,indent=2))
parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args()
if args.output:Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
