"""Numeric reconnaissance only: both mixed homogeneous arcs, necessary native covers."""
import math
import numpy as np
from scipy.optimize import root
rad=math.pi/180
def rho(a):return math.atan2(2*math.sin(a*rad),1)/rad
def forms(a,c):
 t=rho(a)-rho(c);u=c+t;v=a-t
 return [u+a,u+360-2*a,u+c,u+360-2*c,v+a,v+360-2*a,v+c,v+360-2*c]
# β indices1,5;ψ3,7, AH/AL require some indexed mixed sums240±δ.
roots=[]
for ib in (1,5):
 for ic in (3,7):
  for sb in (-1,1):
   for sc in (-1,1):
    for ih in range(8):
     for start in ((110,130,15),(130,110,15),(110,140,20),(140,110,20),(150,140,15)):
      def fun(v):
       a,c,d=v;s=forms(a,c)
       return (s[ib]-240-sb*d,s[ic]-240-sc*d,s[ih]-240+sb*d)
      sol=root(fun,start)
      if not sol.success or max(abs(x) for x in fun(sol.x))>1e-7:continue
      a,c,d=sol.x
      if not (90<a<180 and 90<c<180 and 0<d<30 and abs(a-c)>1e-5):continue
      t=rho(a)-rho(c)
      if not(0<c+t<180 and 0<a-t<180):continue
      k=tuple(round(x,6) for x in (a,c,d))
      if k not in roots:roots.append(k)
print('NUMERIC necessary candidate roots; no tilability/absence proof:',sorted(roots))
for a,c,d in sorted(roots):
 if abs(a-120)<1e-3 or abs(c-120)<1e-3: continue
 t=rho(a)-rho(c);u,v=c+t,a-t
 hom=[a,360-2*a,c,360-2*c]
 # Actual noAA star coverage: each native mixed slot requires either1A+1hom
 # or2Bmixed+1hom. Numeric checking only; tolerance below stated.
 def covered(m):
  return any(abs(m+h-(240+sg*d))<2e-5 for h in hom for sg in(-1,1)) or any(abs(m+n+h-360)<2e-5 for n in(u,v) for h in hom)
 if covered(u) and covered(v): print('NUMERIC all-slot candidate',a,c,d,forms(a,c))

