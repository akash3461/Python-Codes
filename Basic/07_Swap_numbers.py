# Swapping two numbers using a temporary variable and without third variable
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Before swapping:")
print("First number:", num1)
print("Second number:", num2)

# Swapping numbers with third variable
'''
temp = num1
num1 = num2 
num2 = temp 
'''
# Swapping numbers without third variable
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

#using multiplication and division
'''
num1 = num1 * num2
num2 = num1 // num2
num1 = num1 // num2
'''

# using XOR bitwise operator
'''
num1 = num1 ^ num2
num2 = num1 ^ num2
num1 = num1 ^ num2
'''
# or using Python's tuple unpacking
'''
num1, num2 = num2, num1
'''

# Displaying swapped values
print("After swapping:")
print("First number:", num1)   
print("Second number:", num2)

"""     OUTPUT
Enter first number: 10
Enter second number: 20
Before swapping:
First number: 10
Second number: 20  
After swapping:
First number: 20
Second number: 10
"""