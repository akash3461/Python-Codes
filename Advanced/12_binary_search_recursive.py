# Function to perform recursive binary search
def binary_search_recursive(arr, low, high, target):
    if low > high:  # Base case: target not found
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:       # Target found
        return mid
    elif arr[mid] < target:      # Search in the right half
        return binary_search_recursive(arr, mid + 1, high, target)
    else:                        # Search in the left half
        return binary_search_recursive(arr, low, mid - 1, target)


# ---- Taking input from the user ----
arr = list(map(int, input("Enter a sorted list of numbers (space separated): ").split()))
target = int(input("Enter the number to search for: "))

# Call the recursive function
result = binary_search_recursive(arr, 0, len(arr) - 1, target)

if result != -1:
    print(f"{target} found at index {result}")
else:
    print(f"{target} not found in the list")

''' 
                        OUTPUT:
Enter a sorted list of numbers (space separated): 2 3 4 5 6 7 8 9 10
Enter the number to search for: 5
5 found at index 3

'''