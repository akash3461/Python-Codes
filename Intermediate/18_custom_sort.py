# Sort a list of tuples based on the second element of each tuple
lst = [(1, 3), (4, 1), (2, 2)]
lst.sort(key=lambda x: x[1]) # Use a lambda function to specify sorting by the second element
print(lst)


'''OUTPUT:
[(4, 1), (2, 2), (1, 3)]
'''

