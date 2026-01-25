# Flatten a Nested List
def flatten(lst):
    result = []
    for i in lst: # Check if the element is a list
        if isinstance(i, list): # If it is, recursively flatten it
            result.extend(flatten(i)) # Extend the result list with the flattened elements
        else:
            result.append(i) # If it's not a list, append the element to the result
    return result

print(flatten([1, [2, [3, 4]], 5]))

'''OUTPUT:
[1, 2, 3, 4, 5]
    '''
