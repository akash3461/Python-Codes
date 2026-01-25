# Extract unique words from a sentence and sort them alphabetically
sentence = "hello, friends! Welcome to my github and python programmimng repository. Python is easy and interesting."
words = sorted(set(sentence.split())) # Split the sentence into words, convert to a set to get unique words, then sort them
print(words)



'''             OUTPUT:
['Welcome', 'and', 'easy', 'friends!', 'github', 'hello,',
'interesting.', 'is', 'my', 'programmimng', 'python', 'repository.', 'to']
'''