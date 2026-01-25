# Program to rotate a list by k positions
def rotate_list(lst, k):
    n = len(lst)
    k = k % n  # Handle cases where k > n
    return lst[-k:] + lst[:-k]
my_list = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotated_list = rotate_list(my_list, k)
print(rotated_list)


'''
OUTPUT:
[5, 6, 7, 1, 2, 3, 4]

'''