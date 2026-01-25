# Add two matrices element-wise
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
# Perform element-wise addition using nested list comprehensions
result = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
print(result)

'''OUTPUT:
[[6, 8], [10, 12]]
'''