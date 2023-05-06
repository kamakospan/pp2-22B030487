# 5. Create a bank account class that has attributes owner, balance and two methods deposit and withdraw.
# Withdrawals may not exceed the available balance. 
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account():
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def balancekansha(self):
        print(f"Balance is {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} has been deposited. Balance is {self.balance}")


    def withdrawal(self, amount):
        if amount > self.balance:
            print("Withdrawal is unavaliable. Balance is low")
        else:
            self.balance -= amount
            print(f"{amount} has been withdrawn from the deposit. Balance is {self.balance}")

ba1 = Account("Angelina Jolie")
ba2 = Account("Eminem")

ba1.balancekansha()
ba1.withdrawal(1000)
ba1.deposit(1000)
ba1.withdrawal(500)