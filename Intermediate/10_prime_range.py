
# Print all prime numbers in a given range
start, end = 10, 50
 
# Iterate through each number in the range
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")

    '''OUTPUT:
    11 13 17 19 23 29 31 37 41
    43 47 
    '''
