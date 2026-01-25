# Class to represent a Book
class Book:
    def __init__(self, title):
        self.title = title       # title of the book
        self.available = True    # book is available by default


# Class to represent a Library
class Library:
    def __init__(self):
        self.books = []          # list to store all books

    # Add a new book to the library
    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to library.")

    # Issue a book if available
    def issue_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print(f"Book '{title}' issued successfully.")
                return
        print(f"Book '{title}' not available.")

    # Return a book to the library
    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.available = True
                print(f"Book '{title}' returned successfully.")
                return
        print(f"Book '{title}' does not belong to this library.")


# ---- Main Program with User Input ----
lib = Library()

# Ask how many books to add
n = int(input("How many books do you want to add to the library? "))

for i in range(n):
    title = input(f"Enter title of book {i + 1}: ")
    lib.add_book(Book(title))

# Menu for issuing and returning books
while True:
    print("\nLibrary Menu:")
    print("1. Issue Book")
    print("2. Return Book")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter title of book to issue: ")
        lib.issue_book(title)

    elif choice == "2":
        title = input("Enter title of book to return: ")
        lib.return_book(title)

    elif choice == "3":
        print("Exiting library system. Goodbye!")
        break

    else:
        print("Invalid choice, please try again.")


'''
=-=-=-=-=-=-=OUTPUT:=-=-=-=-=-=-=
How many books do you want to add to the library? 2
Enter title of book 1: the power of subconsious mind 
Book 'the power of subconsious mind' added to library.
Enter title of book 2: atomic habbit
Book 'atomic habbit' added to library.

Library Menu:
1. Issue Book
2. Return Book
3. Exit
Enter your choice: 1
Enter title of book to issue: atomic habbit
Book 'atomic habbit' issued successfully.

Library Menu:
1. Issue Book
2. Return Book
3. Exit
Enter your choice: 2
Enter title of book to return: atomic habbit
Book 'atomic habbit' returned successfully.

Library Menu:
1. Issue Book
2. Return Book
3. Exit
Enter your choice: 3
Exiting library system. Goodbye!

'''