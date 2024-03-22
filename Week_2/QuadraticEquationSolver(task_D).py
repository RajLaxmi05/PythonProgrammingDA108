A = float(input("Coefficient a: "))
B = float(input("Coefficient b: "))
C = float(input("Coefficient c: "))

D = B**2 - 4*A*C
r1 = (-B+D**0.5)/2*A
r2 = (-B-D**0.5)/2*A
print("Roots:",r1, 'and', r2)
