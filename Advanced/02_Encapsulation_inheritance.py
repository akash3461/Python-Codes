# Encapsulation:
# The Person class hides the name variable so it cannot be accessed directly
class Person:
    def __init__(self, name):
        self.__name = name   # private variable (cannot be accessed outside the class)

    # Public method to safely access the private name
    def get_name(self):
        return self.__name


# Inheritance:
# Student class inherits properties and methods from Person
class Student(Person):
    def __init__(self, name, marks):
        # Calling the constructor of the parent class (Person)
        super().__init__(name)
        self.marks = marks  # marks specific to Student

    # Polymorphism:
    # Same method name 'display' can be used differently in other classes
    def display(self):
        # Accessing the private name using getter method
        return f"Name: {self.get_name()}, Marks: {self.marks}"


# -------- User Input --------
name = input("Enter student name: ")
marks = int(input("Enter marks: "))

# Creating an object of Student class using user input
s = Student(name, marks)

# Displaying student details
print(s.display())


'''OUTPUT:
Enter student name: Akash
Enter marks: 85

Name: Akash, Marks: 85
'''