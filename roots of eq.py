import math
a= float(input("enter the coefficient of x-squared:"))
b= float(input("enter the coefficient of x:"))
c= float(input("enter the value of the constant:"))
q= (b*b-4*a*c)/2*a
sol1= math.sqrt(q)
sol2= - math.sqrt(q)
print("the roots of the equation are:",sol1,sol2)
