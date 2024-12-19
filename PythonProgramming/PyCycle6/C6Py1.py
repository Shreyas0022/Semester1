class BankAccount:
    def __init__(self, name, account_number, account_type, balance=0):
        self.name = name
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}\nAvailable Balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Debited: {amount}\nAvailable Balance: {self.balance}")
            else:
                print("Insufficient balance for withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def display_details(self):
        print("\n*** Bank Account Details ***")
        print(f"Name: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance Amount: {self.balance}")

name = input("Enter your Name: ")
account_number = input("Enter your Account number: ")
account_type = input("Enter your Account type [Savings / Current]: ")
balance = float(input("Enter your Initial Balance : ") or 0)

account = BankAccount(name=name, account_number=account_number, account_type=account_type, balance=balance)

while True:
    print("\n*** Menu ***")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Account Details")
    print("4. Exit")

    try:
        choice = int(input("Choose an option :: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        continue

    if choice == 1:
        try:
            deposit_amount = float(input("Enter the amount to deposit: "))
            account.deposit(deposit_amount)
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
    elif choice == 2:
        try:
            withdraw_amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(withdraw_amount)
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
    elif choice == 3:
        account.display_details()
    elif choice == 4:
        print("Thank you for using the Bank Account System. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a number between 1 and 4.")
