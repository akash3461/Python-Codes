# Student class to store roll number and name
class Student:
    def __init__(self, roll, name):
        self.roll = roll   # stores student roll number
        self.name = name   # stores student name

    # Method to display student details
    def display(self):
        print(self.roll, self.name)


# List to store all student objects
students = []

# Ask user how many students they want to enter
n = int(input("Enter number of students: "))

# Take input for each student
for i in range(n):
    print(f"\nEnter details of student {i + 1}")
    roll = int(input("Enter roll number: "))  # input roll number
    name = input("Enter name: ")               # input student name

    # Create Student object and add it to the list
    students.append(Student(roll, name))

# Display all stored student details
print("\nStudent Details:")
for s in students:
    s.display()


''' 
=-=-=-=-=-=-=OUTPUT:=-=-=-=-=-=-=
Enter number of students: 2

Enter details of student 1
Enter roll number: 14120
Enter name: Akash Chavan

Enter details of student 2
Enter roll number: 14120
Enter name: Arpit

Student Details:
14120 Akash Chavan
14120 Arpit
'''