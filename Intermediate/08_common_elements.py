# Program to find common elements in two lists
# def common_elements(list1, list2):
#     return list(set(list1) & set(list2)) 

l1 = [1, 2, 3, 4, 5]
l2 = [3, 4, 5, 6]
# Using set intersection
# common = list(set(l1) & set(l2))  
# Using loop
common = []
for i in l1:
    if i in l2 and i not in common:
        common.append(i)

print(common)

'''
OUTPUT:
[4, 5]
'''