#!/usr/bin/env python3
"""Exact finite negative-weight chamber; no assertion of universal cell survival."""
import importlib.util,json
from pathlib import Path
from fractions import Fraction as F
sp=importlib.util.spec_from_file_location('gate',Path(__file__).with_name('hat-chiral-weighted-power-gate-2026-10-19.py'))
g=importlib.util.module_from_spec(sp);sp.loader.exec_module(g)
h=g.h
sample=F(-3121,850)
lo,hi=sample-F(1,1000),sample+F(1,1000)
def enc(q):return [str(q.a),str(q.b)]
def ep(p):return [enc(q) for q in p]
def vertex(i,a,b,t):
 d=g.sub(g.s0[a],g.s0[i]);e=g.sub(g.s0[b],g.s0[i])
 A,B=2*d[0],2*d[1];D,E=2*e[0],2*e[1]
 C=g.dot(d,d)+t*(g.chi[i]-g.chi[a]);G=g.dot(e,e)+t*(g.chi[i]-g.chi[b])
 det=A*E-B*D
 assert det.sign()!=0
 return ((C*E-B*G)/det,(A*G-C*D)/det)
def poly(i,t):
 p=[h.pt(-5,-5),h.pt(5,-5),h.pt(5,5),h.pt(-5,5)]
 for j in g.near[i]:
  d=g.sub(g.s0[j],g.s0[i]);p=g.clip(p,2*d[0],2*d[1],g.dot(d,d)+t*(g.chi[i]-g.chi[j]))
 return p
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def coeff(fun):
 a,b,c=fun(0),fun(1),fun(-1)
 return [a,(b-c)/2,(b+c)/2-a]
def evalp(c,t):return c[0]+c[1]*t+c[2]*t*t
rows=[];areas={}
for i,n in ((509,5),(519,5),(516,8)):
 p=poly(i,sample);assert len(p)==n
 # The edge following each vertex is supported by precisely one near-site line.
 oo=[]
 for u,v in zip(p,p[1:]+p[:1]):
  active=[]
  for j in g.near[i]:
   d=g.sub(g.s0[j],g.s0[i]);C=g.dot(d,d)+sample*(g.chi[i]-g.chi[j])
   if all((C-2*g.dot(d,z)).sign()==0 for z in (u,v)):active.append(j)
  assert len(active)==1;oo.append(active[0])
 def verts(t):return [vertex(i,a,b,t) for a,b in zip(oo[-1:]+oo[:-1],oo)]
 minimum_slack=None
 for t in (lo,hi):
  vs=verts(t)
  for k,v in enumerate(vs):
   assert (F(365,16)-g.dot(v,v)).sign()>0
   for j in g.near[i]:
    d=g.sub(g.s0[j],g.s0[i]);s=g.dot(d,d)+t*(g.chi[i]-g.chi[j])-2*g.dot(d,v)
    if j in (oo[k-1],oo[k]):assert s.sign()==0
    else:
     assert s.sign()>0
     if minimum_slack is None or (s-minimum_slack).sign()<0:minimum_slack=s
  for k,j in enumerate(oo):
   d=g.sub(g.s0[j],g.s0[i]);edge=g.sub(vs[(k+1)%n],vs[k]);assert cross(d,edge).sign()>0
 def area(t):
  vs=verts(t);return sum((cross(u,v) for u,v in zip(vs,vs[1:]+vs[:1])),h.ZERO)/2
 ac=coeff(area);areas[i]=ac
 lengths=[]
 for k in range(n):
  def length(t):
   vs=verts(t);e=g.sub(vs[(k+1)%n],vs[k]);return g.dot(e,e)
  lengths.append([enc(q) for q in coeff(length)])
 rows.append({'target':i,'side_count':n,'cyclic_edge_neighbors':oo,'all_radius_10_neighbors':g.near[i],
 'vertices_affine_in_lambda':[{'constant':ep(v),'linear':ep(g.sub(w,v))} for v,w in zip(verts(0),verts(1))],
 'area_coefficients':[enc(q) for q in ac],'squared_side_length_coefficients':lengths,
 'endpoint_minimum_nonincident_slack':enc(minimum_slack),
 'endpoint_vertices':{str(t):[ep(v) for v in verts(t)] for t in (lo,hi)}})
# Convert area difference on [lo,hi] to degree-two Bernstein coefficients.
# Positive coefficients prove strict positivity everywhere including endpoints.
delta=[areas[519][k]-areas[509][k] for k in range(3)]
b0=evalp(delta,lo);b2=evalp(delta,hi)
b1=b0+(hi-lo)*(delta[1]+2*delta[2]*lo)/2
assert all(q.sign()>0 for q in (b0,b1,b2))
assert abs(lo)<4 and abs(hi)<4
assert (100-4)**2>400*F(365,16)
assert all(g.complete.values())
r={'status':'EXACT_NEGATIVE_CHAMBER_NO_SURVIVOR','closed_interval':[str(lo),str(hi)],'sample':str(sample),
 'field_encoding':'[rational a,rational b] means a+b sqrt(3); polynomial coefficients in increasing powers of lambda',
 'source_dependency':'hat-chiral-weighted-power-gate-2026-10-19.py and its reviewed genuine infinite Hat hierarchy',
 'cells':rows,'area_519_minus_area_509_coefficients':[enc(q) for q in delta],
 'area_difference_Bernstein_coefficients_on_interval':[enc(q) for q in (b0,b1,b2)],
 'finite_exclusion':{'radius':10,'weight_spread_bound':4,'vertex_squared_radius_bound':'365/16','strict_cutoff_check':'96^2 > 400*(365/16)','actual_support_disk_complete':g.complete},
 'necessary_congruence_conditions':'equal areas and cyclic squared edge lengths up to rotation/reversal; area equality has no root in chamber',
 'surviving_parameters':[],'scope':'Only these three actual cells; no claim every source site remains nonempty, no global palette or decoder.'}
# Algebraic restart hints only: these fixed-cycle roots do not certify those remote cells.
assert all(q.a==0 for q in delta)
a,b,c=delta[2].b,delta[1].b,delta[0].b
disc=b*b-4*a*c
assert disc>0 and a>0
assert evalp(delta,-32).sign()>0 and evalp(delta,-31).sign()<0
assert evalp(delta,-10).sign()<0 and evalp(delta,-9).sign()>0
r['formal_area_equality_roots']={'formula':'(-b +/- sqrt(b^2-4ac))/(2a)', 'a':str(a),'b':str(b),'c':str(c),'discriminant':str(disc),'isolating_intervals':[['-32','-31'],['-10','-9']],'scope':'formal continuation of fixed-cycle invariants only; remote combinatorics not certified'}
Path('research/certificates/hat-negative-weight-congruence-chamber-2026-10-19.json').write_text(json.dumps(r,indent=2)+'\n')
print(r['status'],r['closed_interval'])
print('area difference',r['area_519_minus_area_509_coefficients'])
print('Bernstein',r['area_difference_Bernstein_coefficients_on_interval'])
