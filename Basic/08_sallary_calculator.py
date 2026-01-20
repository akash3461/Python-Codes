# sallary calculator
# hra = 20% of basic salary
# da = 10% of basic salary


# Input basic salary
basic_salary = float(input("Enter basic salary: "))

# Calculate allowances
hra = basic_salary * 0.20
da = basic_salary * 0.10

# Calculate total salary
total_salary = basic_salary + hra + da

# Display results
print("HRA (20%):", hra)
print("DA (10%):", da)
print("Total Salary:", total_salary)

"""     OUTPUT
Enter basic salary: 50000
HRA (20%): 10000.0
DA (10%): 5000.0
Total Salary: 65000.0
"""