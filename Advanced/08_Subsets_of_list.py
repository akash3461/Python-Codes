# This function prints all possible subsets of a number (digit by digit)
def subsets(number_str, index=0, current_subset=""):

    # If all digits are processed, print the subset
    if index == len(number_str):
        print(current_subset)
        return

    # Choice 1: Do NOT include the current digit
    subsets(number_str, index + 1, current_subset)

    # Choice 2: Include the current digit
    subsets(number_str, index + 1, current_subset + number_str[index])


# ---- Taking integer input from the user ----
num = int(input("Enter an integer: "))

# Convert integer to string so we can process each digit
num_str = str(num)

print("\nAll possible subsets of the digits are:")
subsets(num_str)


'''

Enter an integer: 1254

All possible subsets of the digits are:

4
5
54
2
24
25
254
1
14
15
154
12
124
125
1254

'''
