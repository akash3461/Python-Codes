# Triangle Type Identifier
# This program determines if three given sides can form a triangle
# and identifies the type of triangle (Equilateral, Isosceles, Scalene).
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

# Check for triangle validity
if a + b > c and a + c > b and b + c > a:
    print("Valid triangle")

    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Not a valid triangle")

'''
         Example Output:
Enter side 1: 5
Enter side 2: 5
Enter side 3: 5
Valid triangle
Equilateral
'''
