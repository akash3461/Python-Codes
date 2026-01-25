def generate_parentheses(open_brackets, close_brackets, s=""):
    # If no brackets are left, print one valid combination
    if open_brackets == 0 and close_brackets == 0:
        print(s)
        return

    # Add an opening bracket if available
    if open_brackets > 0:
        generate_parentheses(open_brackets - 1, close_brackets, s + "(")

    # Add a closing bracket only if it keeps the string valid
    if close_brackets > open_brackets:
        generate_parentheses(open_brackets, close_brackets - 1, s + ")")


# ---- Taking user input ----
n = int(input("Enter number of pairs of parentheses: "))

print(f"\nAll valid combinations for {n} pairs are:")
generate_parentheses(n, n)



''' 
                OUTPUT:
Enter number of pairs of parentheses: 3

All valid combinations for 3 pairs are:
((()))
(()())
(())()
()(())
()()()
()()()

'''