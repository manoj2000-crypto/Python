# Write a program to create a derived class current_ account from Account class derived class consist two method -
# deposit and withdraw display the deposit and withdraw amount.

class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def display_balance(self):
        print("Account Number : ", self.account_number)
        print("Account Holder : ", self.account_holder)
        print("Balance : ", self.balance)


class CurrentAccount(Account):
    def deposit(self, amount):
        self.balance += amount
        print("Deposit Amount : ", amount)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawal Amount : ", amount)
        else:
            print("Insufficient balance. Cannot withdraw.")


account_number = input("Enter the account number : ")
account_holder = input("Enter the account holder's name : ")

current_account = CurrentAccount(account_number, account_holder)

current_account.display_balance()

amount_to_deposit = float(input("Enter the amount to deposit : "))
current_account.deposit(amount_to_deposit)

amount_to_withdraw = float(input("Enter the amount to withdraw : "))
current_account.withdraw(amount_to_withdraw)

current_account.display_balance()
