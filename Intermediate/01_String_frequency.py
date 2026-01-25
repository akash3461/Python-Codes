# Program to count the frequency of each character in a given string

string = input("Enter a string: ")
frequency = {}

# Iterate through each character in the string
for char in string:
    frequency[char] = frequency.get(char, 0) + 1
print("Character frequencies:")

# Print the frequency of each character
for char, count in frequency.items():
    print(f"'{char}': {count}")

    '''OUTPUT:
    Enter a string: My self akash the owner of this repo
Character frequencies:
'M': 1
'y': 1
' ': 7
's': 3
'e': 4
'l': 1
'f': 2
'a': 2
'k': 1
'h': 3
't': 2
'o': 3
'w': 1
'n': 1
'r': 2
'i': 1
'p': 1'''