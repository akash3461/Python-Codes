# Program to check if two strings are anagrams

s1 = input("Enter first string: ").replace(" ", "").lower()
s2 = input("Enter second string: ").replace(" ", "").lower()

print(sorted(s1) == sorted(s2))



'''OUTPUT:
i/p
Enter first string: Listen
Enter second string: Silent

o/p
True
'''
