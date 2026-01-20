# Input a 3-digit number
num = int(input("Enter a 3-digit number: "))

# Extract digits
a = num // 100
b = (num // 10) % 10
c = num % 10

# Calculate sum and product
sum_digits = a + b + c
product_digits = a * b * c

# Display results
print("Sum of digits:", sum_digits)
print("Product of digits:", product_digits)

# Reverse the number
reversed_num = c * 100 + b * 10 + a
print("Reversed number:", reversed_num)
# Calculate number with last digit moved to front
moved_last_to_front = c * 100 + a * 10 + b
print("Number with last digit moved to front:", moved_last_to_front)
# Calculate number with first digit moved to end
moved_first_to_end = b * 100 + c * 10 + a
print("Number with first digit moved to end:", moved_first_to_end)

''' 
       Example Output:
Enter a 3-digit number: 345
Sum of digits: 12
Product of digits: 60
Reversed number: 543
Number with last digit moved to front: 534
Number with first digit moved to end: 453
    '''