
# reverse the words
sentence = input("Enter a sentence: ")

result = " ".join(word[::-1] 
for word in sentence.split())
print(result)

'''OUTPUT:
Enter a sentence: Hello World
olleH dlroW'''


