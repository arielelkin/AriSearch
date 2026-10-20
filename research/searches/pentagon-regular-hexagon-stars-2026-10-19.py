"""Complete local-sector gate; geometry and growth proof are in the lemma."""
stars=[(a,b,c,s) for a in range(4) for b in range(4) for c in range(3) for s in range(3)
       if a+b+c>=1 and 5*a+6*b+7*c+9*s==18]
assert stars==[(0,3,0,0),(1,1,1,0)], stars
print({"angle_unit_degrees":20,"complete_local_stars":stars,"status":"complete"})
