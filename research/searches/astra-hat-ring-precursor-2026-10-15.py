#!/usr/bin/env python3
"""Numerical precursor only: six-spoke hat ring, no congruence or proof claim."""
import importlib.util,numpy as np,sys
from scipy.optimize import minimize
sp=importlib.util.spec_from_file_location('h','research/searches/source-decoration-hat-patch.py');h=importlib.util.module_from_spec(sp);sp.loader.exec_module(h)
H=np.array([[float(x) for x in p] for p in h.hat_outline])
if '--b2' in sys.argv:
 ds=np.roll(H,-1,axis=0)-H
 ds=[d*(2/np.sqrt(3) if abs(d@d-3)<1e-9 else 1) for d in ds]
 H=np.vstack(([0,0],np.cumsum(ds,axis=0)))[:-1]
leaves=[0,2,4,6,8,11]
if '--edge-spokes' in sys.argv:
 H=np.array([*H[:2],(H[1]+H[2])/2,*H[2:6],(H[5]+H[6])/2,*H[6:]])
 leaves=[0,2,5,7,10,13]
def polygons(x):
 Z=x[:12].reshape(6,2)
 return [Z]+[np.array([*H[leaves[i]:(leaves[i+1] if i<5 else len(H))+1],*([] if i<5 else [H[0]]),Z[(i+1)%6],Z[i]]) for i in range(6)]
def constraints(x):
 vals=[]
 for P in polygons(x):
  for i in range(len(P)):
   v=P[(i+1)%len(P)]-P[i]
   for j in range(len(P)):
    if j in (i,(i+1)%len(P)):continue
    w=P[j]-P[i];vals.append(v[0]*w[1]-v[1]*w[0]-x[-1])
 return np.array(vals)
rng=np.random.default_rng(0)
for k in range(15):
 center=np.array([1.5,0.]);Z=center+.15*(H[leaves]-center)+rng.normal(0,.03,(6,2))
 x=np.r_[Z.ravel(),-.1]
 ans=minimize(lambda x:-x[-1],x,method='SLSQP',constraints=[{'type':'ineq','fun':constraints}],bounds=[(-2,6),(-4,5)]*6+[(-20,2)],options={'maxiter':500,'ftol':1e-10})
 print(k,ans.success,ans.x[-1],np.min(constraints(ans.x)),ans.x[:12].tolist(),flush=True)
 if ans.success and ans.x[-1]>1e-5:break
