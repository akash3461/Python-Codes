# Count the frequency of each number in a list
lst = [1, 2, 2, 3, 3, 3]
freq = {}
# Iterate through each number in the list and count its occurrences
for num in lst:
    freq[num] = freq.get(num, 0) + 1
# Print the frequency dictionary
print(freq)

'''             OUTPUT:
{1: 1, 2: 2, 3: 3}
'''