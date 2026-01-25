# Function to generate all permutations of a string
def permutations(s, ans=""):
    # If no characters are left, print one permutation
    if len(s) == 0:
        print(ans)
        return

    # Loop through each character in the string
    for i in range(len(s)):
        # Pick one character and permute the remaining characters
        permutations(s[:i] + s[i+1:], ans + s[i])


# ---- Taking input from the user ----
text = input("Enter a string: ")

print("\nPermutations are:") 
permutations(text) # Generate and print all permutations of the input string




'''
        OUTPUT:
Enter a string: ABC

Permutations are:
ABC
ACB
BAC
BCA
CAB
CBA

'''