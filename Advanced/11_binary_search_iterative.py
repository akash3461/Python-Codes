# Function to perform iterative binary search
def binary_search_iterative(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:     # Target found
            return mid
        elif arr[mid] < target:    # Search in the right half
            low = mid + 1
        else:                      # Search in the left half
            high = mid - 1

    return -1  # Target not found


# ---- Taking input from the user ----
arr = list(map(int, input("Enter a sorted list of numbers (space separated): ").split()))
target = int(input("Enter the number to search for: "))

result = binary_search_iterative(arr, target)

if result != -1:
    print(f"{target} found at index {result}")
else:
    print(f"{target} not found in the list")


''' OUTPUT:
Enter a sorted list of numbers (space separated): 2 3 4 5 6 7 8 9 10 11
Enter the number to search for: 5
5 found at index 3
'''