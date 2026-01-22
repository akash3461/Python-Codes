# Program to find the second largest number in a list
lst = list(map(int, input("Enter numbers separated by spaces: ").split()))

first = second = float('-inf')

for number in lst:
    if number > first:
        second = first
        first = number
    elif first > number > second:
        second = number

print("The second largest number is:", second)


'''
            OUTPUT:
Enter numbers separated by spaces: 12 25 3 6 45 63 25
The second largest number is: 45 
'''