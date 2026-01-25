# Program to remove duplicates from a list while preserving order
lst = [1, 2, 2, 3, 1, 4]
result = []

for i in lst:
    if i not in result:
        result.append(i)
# Print the list after removing duplicates
print(result)


'''OUTPUT:
[1, 2, 3, 4]
'''