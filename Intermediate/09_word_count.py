# Word Count in a Text File
with open("sample.txt", "r") as file:
    text = file.read() 
    words = text.split() # Split the text into words
    print(len(words))  # Print the number of words 

'''
OUTPUT :
96 '''


'''smple.txt file content :
Python is a versatile programming language that is widely used for various applications,
 including web development, data'''