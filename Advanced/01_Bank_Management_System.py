# Bank Management System with Encapsulation
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance   # private variable

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. Balance: {self.__balance}")
        else:
            print("Invalid deposit amount")

    # Withdraw method
    def withdraw(self, amount):
        if amount <= self.__balance and amount > 0:
            self.__balance -= amount
            print(f"Withdrawn {amount}. Balance: {self.__balance}")
        else:
            print("Insufficient balance or invalid amount")

    # Get balance method
    def get_balance(self):
        return self.__balance


# ---- Main Program ----
name = input("Enter account holder name: ")
balance = int(input("Enter initial balance: "))

acc = BankAccount(name, balance)
# Simple menu-driven interface
while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = int(input("Enter deposit amount: "))
        acc.deposit(amount)

    elif choice == "2":
        amount = int(input("Enter withdrawal amount: "))
        acc.withdraw(amount)

    elif choice == "3":
        print("Current Balance:", acc.get_balance())

    elif choice == "4":
        print("Thank you for using the bank system!")
        break

    else:
        print("Invalid choice, try again")


'''
|=-=-=-=-=-=-=-=-=-=-OUTPUT:=-=-=-=-=-=-=-=-=-=-=|
|    Enter account holder name: Akash Chavan     |
|    Enter initial balance: 150000               |
|                                                |
|    1. Deposit                                  |
|    2. Withdraw                                 |
|    3. Check Balance                            | 
|    4. Exit                                     |
|    Enter your choice: 1                        |  
|    Enter deposit amount: 50000                 |
|    Deposited 50000. Balance: 200000            |
|                                                |
|    1. Deposit                                  |                
|    2. Withdraw                                 |
|    3. Check Balance                            |
|    4. Exit                                     |
|    Enter your choice: 2                        |
|    Enter withdrawal amount: 75000              |
|    Withdrawn 75000. Balance: 125000            |
|                                                |
|    1. Deposit                                  |
|    2. Withdraw                                 |
|    3. Check Balance                            |
|    4. Exit                                     |
|    Enter your choice: 3                        |
|    Current Balance: 125000                     |
|                                                |
|    1. Deposit                                  |
|    2. Withdraw                                 |
|    3. Check Balance                            |
|    4. Exit                                     |
|    Enter your choice: 4                        |
|    Thank you for using the bank system!        |
|=-=-=-=-=-=-=-=-=-=-OUTPUT:=-=-=-=-=-=-=-=-=-=-=|
'''