class BankAccount:
    def info(self):
        self.name = input("Enter your name: ")
        self.account_number = input("Enter your account number: ")
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance


# Create account once
account = BankAccount()
account.info()

# Start menu loop
while True:

    print("\nWelcome to the Bank Account System")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        amount = float(input("Enter amount to deposit: "))
        if account.deposit(amount):
            print(f"Deposited: ₹{amount}")
        else:
            print("Deposit failed. Amount must be positive.")

    elif choice == '2':
        amount = float(input("Enter amount to withdraw: "))
        if account.withdraw(amount):
            print(f"Withdrawn: ₹{amount}")
        else:
            print("Withdrawal failed. Check your balance or amount.")

    elif choice == '3':
        print(f"Current Balance: ₹{account.get_balance()}")

    elif choice == '4':
        print("Exiting the system.")
        break

    else:
        print("Invalid choice, please try again.")
