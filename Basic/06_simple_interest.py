# Simple Interest Calculator

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time (in years): "))

simple_interest = (principal * rate * time) / 100
amount = principal + simple_interest

print(f"The Simple Interest is: {simple_interest}")
print(f"The Amount is: {amount}")


"""     OUTPUT
Enter the principal amount: 1000
Enter the rate of interest (in %): 5
Enter the time (in years): 3
The Simple Interest is: 150.0
The Amount is: 1150.0
"""
