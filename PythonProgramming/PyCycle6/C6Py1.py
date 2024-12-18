class BankAccount:
    def __init__(self, name, account_number, account_type, balance=0):
        # Constructor to initialize the bank account details
        self.name = name
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        # Method to deposit an amount
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        # Method to withdraw an amount (if sufficient balance)
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance is {self.balance}.")
            else:
                print("Insufficient balance for withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def display_details(self):
        # Method to display account details
        print("Account Details:")
        print(f"Name: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance}")


# Getting account details from user input
name = input("Enter your name: ")
account_number = input("Enter your account number: ")
account_type = input("Enter your account type (e.g., Savings, Checking): ")
balance = float(input("Enter your initial balance (default is 0): ") or 0)  # If the user enters nothing, balance is set to 0

# Creating an object of BankAccount with user inputs
account = BankAccount(name=name, account_number=account_number, account_type=account_type, balance=balance)

# Displaying the details of the account
account.display_details()

# Depositing an amount
deposit_amount = float(input("Enter the amount to deposit: "))
account.deposit(deposit_amount)

# Withdrawing an amount
withdraw_amount = float(input("Enter the amount to withdraw: "))
account.withdraw(withdraw_amount)

# Displaying the updated details of the account
account.display_details()
