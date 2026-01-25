# Validate a password based on specific criteria
password = input("Enter your password : ")

# Check if the password is at least 8 characters long, contains at least one uppercase letter, and at least one digit
if (len(password) >= 8 and
    any(c.isupper() for c in password) and
    any(c.isdigit() for c in password)): 
    print("Valid Password")
else:
    print("Invalid Password")