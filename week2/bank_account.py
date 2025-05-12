class BankAccount:

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('Insufficient funds: Charging a $5 fee')
            self.balance -= 5

    def display_account_info(self):
        print(f"Balance: ${self.balance}")

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (1 + self.int_rate)
        
        

account1 = BankAccount(int_rate= 0.08, balance=1000)
account2 = BankAccount(int_rate=0.05, balance=1500)

account1.deposit(500)
account1.deposit(200)
account1.deposit(700)
account1.withdraw(1200)
account1.yield_interest(0.08)
account1.display_account_info()

account2.deposit(800)
account2.deposit(2400)
account2.withdraw(300)
account2.withdraw(1400)
account2.withdraw(700)
account2.withdraw(1900)
account2.yield_interest(0.05)
account2.display_account_info()
