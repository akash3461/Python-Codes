# Find the missing number in a list containing numbers from 1 to n with one number missing
lst = [1, 2, 4, 5]
n = 5

total = n * (n + 1) // 2 # Calculate the expected total sum from 1 to n 
print(total - sum(lst)) # Subtract the actual sum of the list from the expected total to find the missing number

'''OUTPUT:
3   
'''