from abc import ABC, abstractmethod

class Bank:
    def __init__(self, name, bank_address, registration_no, license):
        self.name = name
        self.bank_address = bank_address
        self.registration = registration_no
        self.license = license


class Account(ABC):
    accounts = []
    loan_count = 0
    bank_balance = 0

    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = len(Account.accounts) + 1
        self.balance = 0
        self.loan_taken = 0
        self.transaction_history = []
        Account.accounts.append(self)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} rupees. New balance: {self.balance}")
        else:
            print("Invalid deposit amount")

    def check_balance(self):
        print(f"Your balance: {self.balance}")

    def history_of_transaction(self, transaction):
        self.transaction_history.append(transaction)

    def check_transaction_history(self):
        print(f"{self.name}, your transaction history for Account {self.account_number}:")
        for transaction in self.transaction_history:
            print(transaction)

    def take_loan(self, amount):
        if Account.loan_count < 2 and self.balance >= amount:
            self.loan_taken += amount
            self.balance -= amount
            Account.bank_balance += amount
            Account.loan_count += 1
            print(f"Loan of {amount} taken. New balance: {self.balance}")
        elif self.balance < amount:
            print("You don't have enough balance for a loan")
        else:
            print("Loan limit exceeded")

    def transfer_amount(self, recipient, amount):
        if recipient in Account.accounts:
            if self.balance >= amount:
                self.balance -= amount
                recipient.deposit(amount)
                print(f"Transferred {amount} to {recipient.name}. New balance: {self.balance}")
            else:
                print("Limit exceeded")
        else:
            print("Recipient account does not exist")

    def show_info(self):
        print(f"Account Type: {self.account_type}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Address: {self.address}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: {self.balance}")


class SavingsAccount(Account):
    def __init__(self, name, email, address):
        super().__init__(name, email, address, "Savings")

    def specific_info(self):
        print("Interest rate: 7.5%")


class CurrentAccount(Account):
    def __init__(self, name, email, address):
        super().__init__(name, email, address, "Current")

    def specific_info(self):
        print("Interest rate: 8%")


class Admin:
    def create_account(self, name, email, address, account_type, bank):
        if account_type.lower() == "savings":
            account = SavingsAccount(name, email, address)
        elif account_type.lower() == "current":
            account = CurrentAccount(name, email, address)
        else:
            print("Invalid account type")

    def delete_account(self, account):
        if account in Account.accounts:
            Account.accounts.remove(account)
            print(f"{account.name} has been removed")
        else:
            print("Account not found")

    def see_all_accounts(self):
        for account in Account.accounts:
            account.show_info()
            print("--------- X -------")

    def check_bank_balance(self):
        print(f"Available balance: {Account.bank_balance}")

    def loan_feature(self, status):
        if status:
            Account.loan_count = 0
            print("Loan feature enabled. You can take loans.")
        else:
            Account.loan_count = 1
            print("Loan feature disabled. You can't take more loans.")

    def check_loan_amount(self):
        total_loan_amount = sum(account.loan_taken for account in Account.accounts)
        print(f"Total loan amount: {total_loan_amount}")


admin = Admin()

while True:
    print("1. User")
    print("2. Admin")
    print("3. Exit")

    choice = input("Choose User or Admin or Exit (1/2/3): ")

    if choice == "1":
        name = input("Name: ")
        email = input("Email: ")
        address = input("Address: ")
        account_type = input("Account Type (Savings/Current): ")

        user = None

        if account_type.lower() == "savings":
            user = SavingsAccount(name, email, address)
        elif account_type.lower() == "current":
            user = CurrentAccount(name, email, address)
        else:
            print("Invalid account type")
            continue

        while user:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Check Transaction History")
            print("5. Take Loan")
            print("6. Transfer Amount")
            print("7. Show Info")
            print("8. Logout")

            option = input("Choose an option number: ")

            if option == "1":
                amount = float(input("Enter deposit amount: "))
                user.deposit(amount)
            elif option == "2":
                amount = float(input("Enter withdrawal amount: "))
                user.withdraw(amount)
            elif option == "3":
                user.check_balance()
            elif option == "4":
                user.check_transaction_history()
            elif option == "5":
                amount = float(input("Enter loan amount: "))
                user.take_loan(amount)
            elif option == "6":
                recipient_account_no = int(input("Enter recipient account number: "))
                recipient = next((acc for acc in Account.accounts if acc.account_number == recipient_account_no), None)
                if recipient:
                    amount = float(input("Enter transfer amount: "))
                    user.transfer_amount(recipient, amount)
                else:
                    print("Recipient account doesn't exist")
            elif option == "7":
                user.show_info()
            elif option == "8":
                user = None
            else:
                print("Invalid option ...")

    elif choice == "2":
        print("Admin Menu:")
        print("1. Create Account")
        print("2. Delete Account")
        print("3. See All Accounts")
        print("4. Check Bank Balance")
        print("5. Total Loan Amount")
        print("6. Loan Feature")
        print("7. Logout")
        admin_option = input("Choose an option number: ")

        if admin_option == "1":
            name = input("Name: ")
            email = input("Email: ")
            address = input("Address: ")
            account_type = input("Account Type (Savings/Current): ")
            admin.create_account(name, email, address, account_type, admin)

        elif admin_option == "2":
            account_number = input("Enter the account number to delete: ")
            account = next((acc for acc in Account.accounts if acc.account_number == account_number), None)

    elif choice == '3':
        print("Loging Out...")
        break
    else:
        print("Invalid option .. Plz press 1/2 or 3")
