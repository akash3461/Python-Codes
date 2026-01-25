# Run-length encoding of a string
s = "aaabbc"
result = ""
count = 1
# Iterate through the string and count consecutive characters
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        result += s[i-1] + str(count)
        count = 1
# Append the last set of characters
result += s[-1] + str(count)
print(result)

'''OUTPUT:
a3b2c1
'''
