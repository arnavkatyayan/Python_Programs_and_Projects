import sys

class Bank:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount == 0:
            print("The amount can't be zero")
            return
        else:
            self.balance += amount
            print(f"Thanks for the deposit, now the total is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Sorry, insufficient balance.")
        else:
            self.balance -= amount
            print(f"Thanks for the withdrawal, now the total is {self.balance}")

    def exit(self):
        print("Thanks for using the banking system.")
        sys.exit()

    def show(self):
        print(f"The balance in the account is {self.balance}")

    @staticmethod
    def is_name_str(name):
        if name.isdigit():
            return False
        else:
            return True

    def details(self):
        print("\nBank Operations")
        print("1) Deposit")
        print("2) Withdraw")
        print("3) Show")
        print("4) Exit")
        num = int(input("Enter a number from 1 to 4: "))
        return num


# Welcome message and name input
print("Welcome to the bank management system")
while True:
    owner = input("Enter your name, please: ")
    if Bank.is_name_str(owner):
        break
    else:
        print("Invalid name. Name should not contain numbers.")

# Create bank account for the owner
bank_account = Bank(owner)

# Bank operations loop
while True:
    n = bank_account.details()
    if n == 1:
        amount = float(input("Enter amount to deposit: "))
        bank_account.deposit(amount)
    
    elif n == 2:
        amount = float(input("Enter amount to withdraw: "))
        bank_account.withdraw(amount)
    
    elif n == 3:
        bank_account.show()

    elif n==4:
        bank_account.exit()

    else:
        print("Invalid input. Please choose 1, 2, 3, or 4.")
