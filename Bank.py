from abc import ABC, abstractclassmethod


class Bank:
    def __init__(self, name, bank_address , registration_no, license) -> None:
        self.name = name
        self.bank_address = bank_address
        self.registration = registration_no
        self.license = license

class Account(ABC):
    accounts = []
    loan_count = 0
    bank_balance = 0

    def __init__(self, name , email, address, account_type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = len(Account.accounts) + 1
        self.balance = 0
        self.loan_taken = 0
        self.transaction_history = []
        Account.accounts.append(self)

    def deposite(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Diposited {amount} rupees and New balance{self.balance}")
        else :
            print("invalid withdrawl amount")

    def check_balance(self):
        print(f"you balance {self.balance}")

    def history_of_transaction(self, transaction):
        self.transaction_history.append(transaction)
    
    def check_transaction_history(self):
        print(f"{self.name} your transaction history is {self.account_number}")
        for transaction in self.transaction_history:
            print(transaction)

    def take_loan(self, amount):
        if Account.loan_count < 2 and self.balance >= amount:
            self.loan_taken += amount
            self.balance -= amount
            Account.bank_balance += amount
            Account.loan_count += 1
            print(f"loan {amount} taken ... new balance {self.balance}")
        
        elif self.balance < amount:
            print("You haven't enough balance")
        else :
            print("Nikal laowre")

    def transfer_amount(self, recipent , amount):
        if recipent in Account.accounts:
            if self.balance >= amount:
                self.balance -= amount
                recipent.deposite(amount)
                print(f"transferred {amount} to {recipent.name}, balance {self.balance}")
            else:
                print("Limit exceed")
        else:
            print("Account doesn't exist ...")

    def show_info(self):
        print(f"Acccount Type: {self.account_type}")
        print(f"Name : {self.name}")
        print(f"Email : {self.email}")
        print(f"Address : {self.address}")
        print(f"Account Number : {self.account_number}")
        print(f"Current Balance: {self.balance}")

class SavingsAccount(Account):
    def __init__(self, name, email, address) -> None:
        super().__init__(name, email, address, "Savings")

    def specific_info(self):
        print("Intrest rate 7.5%")

class CurrentAccount(Account):
    def __init__(self, name, email, address) -> None:
        super().__init__(name, email, address, "Current")

    def specific_info(self):
        print("Intrest rate 8%")

class Admin:
    def create_account(self, name, email, address, account_type):
        if account_type.lower() == "savings":
            account = SavingsAccount(name, email, address)
        elif account_type.lower() == "current":
            account = SavingsAccount(name, email, address)
        else:
            print("Invalid ")

    def delete_account(self,account):
        if account in Account.accounts:
            Account.accounts.remove(account)
            print(f"{account.name} have been removed")
        else:
            print("Account not found")


    def see_all_accounts(self):
        for account in self.accounts:
            account.show_info()
            print("--------- X -------")

    def check_bank_balance(self):
        print(f"avaiable balance {Account.bank_balance}")

    def loan_features(self, status):
        if status:
            Account.loan_count = 0
            print("you can take")
        elif status :
            Account.loan_count = 1
            print("Its last one ")

        else :
            print("Nikal bhikmangge")

    def check_loan_amount(self):
        total_loan_amount = sum(account.loan_taken for account in Account.accounts)
        print(f"loan amount {total_loan_amount}")

admin = Admin()


while True:
    print("1. User")
    print("2. Admin")
    print("3. Exit")
    choice = input("Choose User or Admin or Exit (1/2/3): ")

    if choice == "1":
        name = input("Name: ")
        email = input("Email : ")
        address = input("Address: ")
        account_type = input("Account Type : ")

        user = None

        if account_type.lower() == "savings":
            user = SavingsAccount(name, email, address)
        elif account_type.lower() == "current":
            user = CurrentAccount(name , email, address)
        else:
            print("invalid account type")
            continue

        while user:
            print("\n1. Deposite")
            print("2. withdrawl")
            print("3. Check balance")
            print("4. Check Transaction History")
            print("5. Take Loan")
            print("6. Transfer Amount")
            print("7. Show Info")
            print("8. LOgout")

            option = input("Choose an option number: ")

            if option == "1":
                amount = float(input("Enter deposite amount "))
                user.deposite(amount)
            elif option == "2":
                amount = float(input("Enter withdrawl amount : "))
                user.withdraw(amount)
            elif option == "3":
                print(f"current balance {user.check_balance()}")
            elif option == "4":
                user.check_transaction_history()
            elif option == "5":
                amount = float(input("enter loan amount : "))
                user.take_loan(amount)
            elif option == "6":
                recipient_account_no = int(input("Enter recipient account name : "))
                recipient = next((acc for acc in Account.accounts if acc.account_number == recipient_account_no ), None)
                if recipient:
                    amount = float(input("Enter transfer amount :"))
                    user.transfer_amount(recipient, amount)
                else:
                    print("Doesn't exixts")
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
        print("4. Check bank balance")
        print("5. Total loan amount")
        print("6. Loan Feature")
        print("7. Logout")
        admin_option = int(input("Choose an optiopn number: "))

        if admin_option == "1":
            name = input("name ; ")
            email = input("email : ")
            address = input("address : ")
            account_type = input("Account type (Savings/current)")

    elif choice == "3":
        print("You may leave")