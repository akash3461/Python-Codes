# Class to represent a point in 2D space
class Point:
    def __init__(self, x, y):
        self.x = x  # x-coordinate
        self.y = y  # y-coordinate

    # Operator overloading for '+'
    # Allows us to add two Point objects using p1 + p2
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # String representation for easy printing
    def __str__(self):
        return f"({self.x}, {self.y})"


# ---- Taking input from the user ----
print("Enter coordinates for first point:")
x1 = int(input("x1: "))
y1 = int(input("y1: "))

print("\nEnter coordinates for second point:")
x2 = int(input("x2: "))
y2 = int(input("y2: "))

# Creating Point objects
p1 = Point(x1, y1)
p2 = Point(x2, y2)

# Adding two points using overloaded '+'
p3 = p1 + p2

# Displaying the result
print(f"\nResult of adding {p1} and {p2} is: {p3}")




'''OUTPUT:
Enter coordinates for first point:
x1: 3
y1: 4

Enter coordinates for second point:
x2: 5
y2: 6

Result of adding (3, 4) and (5, 6) is: (8, 10)
'''
