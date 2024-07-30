from math import sqrt
a = float(input("Enter a number A:"))
b = float(input("Enter a number B:"))
c = float(input("Enter a number C:"))

print("Our Equation is : (-b +- root(b**2-4*a*c))/2*a")

r = b**2-4*a*c

if r>0:
    x1 = (-b+sqrt(r))/(2*a)
    x2 = (-b-sqrt(r))/(2*a)
    print("Two results are : ",x1,x2)
elif r==0:
    x3 = -b/2*a
    print("Result is : ",x3)
else:
    print("Discriminent is less than zero")

