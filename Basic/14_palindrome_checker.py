# Palindrome Checker Program
# This program checks whether the given input is a palindrome or not

# Taking input from the user
value = input("Enter a number or word: ")

# Reversing the input using slicing
reversed_value = value[::-1]

# Checking if original value and reversed value are the same
if value == reversed_value:
    print("Yes! It is a Palindrome 😊")
else:
    print("No! It is Not a Palindrome ❌")


# OUTPUT 
"""
Sample Output 1:
Enter a number or word: madam
Yes! It is a Palindrome 😊

Sample Output 2:
Enter a number or word: 123
No! It is Not a Palindrome ❌
"""
