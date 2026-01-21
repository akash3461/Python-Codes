# Expression Evaluator
# This program evaluates basic arithmetic expressions (+, -, *, /) with two numbers.

a = float(input("Enter first number: "))
op = input("Enter operator (+ - * /): ")
b = float(input("Enter second number: "))

# Evaluate expression based on the operator

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    if b != 0:
        print(a / b)
    else:
        print("Division by zero not allowed")
else:
    print("Invalid operator")

'''
            Example Output:
Enter first number: 10
Enter operator (+ - * /): *
Enter second number: 5
50.0
''' 
