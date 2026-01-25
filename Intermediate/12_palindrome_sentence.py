# Check if a sentence is a palindrome (ignoring spaces, punctuation, and case)

import re

s = "A man, a plan, a canal: Panama"
clean = re.sub(r'[^a-zA-Z0-9]', '', s).lower() # Remove non-alphanumeric characters and convert to lowercase

print(clean == clean[::-1])

'''OUTPUT:
True
    '''
