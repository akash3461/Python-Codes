# Quadratic Equation Roots Calculator
# This program calculates the roots of a quadratic equation ax^2 + bx + c =
# based on user-provided coefficients a, b, and c.

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# Calculate discriminant
d = b*b - 4*a*c

# Determine the nature of the roots based on the discriminant
if d > 0:
    r1 = (-b + d**0.5) / (2*a)
    r2 = (-b - d**0.5) / (2*a)
    print("Two real roots:", r1, r2)
elif d == 0:
    r = -b / (2*a)
    print("One real root:", r)
else:
    print("No real roots")

'''
         Example Output:
Enter a: 1
Enter b: -3
Enter c: 2
Two real roots: 2.0 1.0
''' 