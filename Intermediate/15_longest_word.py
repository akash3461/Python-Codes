# Find the longest word in a sentence
sentence = "Python programming is amazing"
words = sentence.split() # Split the sentence into words

# Find the longest word using max with key=len
longest = max(words, key=len)
print(longest)


'''OUTPUT:
programming
'''
