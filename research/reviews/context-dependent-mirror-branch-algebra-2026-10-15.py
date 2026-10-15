"""Independent exact algebra for beta18 mirror branch, no producer import."""
from sage.all import QQ,PolynomialRing,NumberField,AA
P=PolynomialRing(QQ,'x');x=P.gen();K=NumberField(4*x*x-2*x-1,'c');c=K.gen()
R=PolynomialRing(K,'v');F=R.fraction_field();v=F(R.gen())
k2=(1-c)/(1+c);kcot=(1-c)/c
L=2*c*v/(c+v)
U=1-((1-v)**2+k2*v*v)/(1-v+kcot*v)
U2=v*((1+c)-2*c*v)/((1+c)*(c+(1-2*c)*v))
D=v*(2*c*v*v-(c+QQ(3)/2)*v+(1+c)/2)/((c+v)*(1+c)*(c+(1-2*c)*v))
assert U==U2 and L-U==D
assert (c+QQ(3)/2)**2-4*c*(1+c)==QQ(3)/2-QQ(5)/2*c
# Direct thick-head coordinates p=(1-a,b), with b=k*B, h=k*v.
# cos72=2c²-1, sin72=2c(1+c)k, sin36*k=1-c.
a=(1-v)*(2*c*c-1)+2*c*(1-c)*v
B=(1-v)*2*c*(1+c)-v*(2*c*c-1)
assert (v*B+v*(1-a))/(B+v)==U
# The actual denominator B+v is positive whenever the internal node lies
# on the required positive side (b>0); v>0. Formula U2 has a globally
# positive denominator for 0<v<1 because its last linear factor ranges
# between c and 1-c.
cp=(1+AA(5).sqrt())/4
assert QQ(3)/5<cp<1
assert QQ(3)/2-QQ(5)/2*cp<0
assert cp>0 and 1-cp>0
print('PASS: exact coordinate upper bound, difference factorization, negative discriminant; mirror branch impossible.')
