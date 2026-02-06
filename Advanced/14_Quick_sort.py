# Function to perform quick sort
def quick_sort(arr):
    if len(arr) <= 1:  # Base case: already sorted
        return arr

    pivot = arr[len(arr) // 2]  # Choose the middle element as pivot
    left = [x for x in arr if x < pivot]     # Elements smaller than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]    # Elements greater than pivot

    # Recursively sort left and right, then combine
    return quick_sort(left) + middle + quick_sort(right)


# ---- Taking input from the user ----
arr = list(map(int, input("Enter numbers to sort (space separated): ").split()))

# Sort the array
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)

'''
                        OUTPUT:
Enter numbers to sort (space separated): 12 3 6 15 7 9 18 47
Sorted array: [3, 6, 7, 9, 12, 15, 18, 47]
'''