# Function to find the length of the longest consecutive sequence
def longest_consecutive(nums):
    num_set = set(nums)  # Convert list to set for O(1) lookups
    longest = 0

    for num in num_set:
        # Start counting only if num is the start of a sequence
        if num - 1 not in num_set:
            current = num
            length = 1

            # Count consecutive numbers
            while current + 1 in num_set:
                current += 1
                length += 1

            # Update longest sequence found
            longest = max(longest, length)

    return longest


# ---- Taking input from the user ----
nums = list(map(int, input("Enter numbers (space separated): ").split()))

# Find the longest consecutive sequence
print("Length of longest consecutive sequence:", longest_consecutive(nums))



'''
            OUTPUT:
Enter numbers (space separated): 6 1 23 12 14 25 36 74 12
Length of longest consecutive sequence: 1

'''