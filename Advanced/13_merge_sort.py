# Function to perform merge sort
def merge_sort(arr):
    if len(arr) <= 1:  # Base case: already sorted
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])   # Sort left half
    right = merge_sort(arr[mid:])  # Sort right half

    return merge(left, right)      # Merge the sorted halves


# Function to merge two sorted lists
def merge(left, right):
    result = []
    i = j = 0

    # Compare elements from both lists and add the smaller one
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements if any
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ---- Taking input from the user ----
arr = list(map(int, input("Enter numbers to sort (space separated): ").split()))

# Sort the array
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)

'''
OUTPUT:
Enter numbers to sort (space separated): 1 2 6 3 15 9 8
Sorted array: [1, 2, 3, 6, 8, 9, 15]

'''