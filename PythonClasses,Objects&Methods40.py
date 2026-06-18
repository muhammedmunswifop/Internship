"""40.Create a BankAccount class with account holder name and balance. Add methods to deposit, withdraw, and display the current balance."""
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ₹{self.balance}")
              
account = BankAccount("Muhammed Munswif", 5000)

account.deposit(2000)
account.withdraw(1500)
account.display_balance()