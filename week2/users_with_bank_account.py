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



class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {
            "bankaccount1": BankAccount(int_rate=0.03, balance=0),
            "bankaccount2": BankAccount(int_rate=0.05, balance=0)
        }

    def make_deposit(self, amount, account_name):
        if account_name in self.accounts:
            self.accounts[account_name].deposit(amount)
        else:
            print(f"No account named {account_name}")

    def make_withdrawal(self, amount, account_name):
        if account_name in self.accounts:
            self.accounts[account_name].withdraw(amount)
        else:
            print(f"No account named {account_name}")

    def display_user_balance(self, account_name):
        if account_name in self.accounts:
            print(f"{self.name}'s {account_name} account:")
            self.accounts[account_name].display_account_info()
        else:
            print(f"No account named {account_name}")

    def transfer_money(self, amount, other_user, from_account, to_account):
        if from_account in self.accounts and to_account in other_user.accounts:
            if self.accounts[from_account].balance >= amount:
                self.accounts[from_account].withdraw(amount)
                other_user.accounts[to_account].deposit(amount)
                print(f"Transferred ${amount} from {self.name}'s {from_account} to {other_user.name}'s {to_account}")
            else:
                print(f"Not enough funds to transfer from {self.name}'s {from_account} account")
        else:
            print("Account name error during transfer")


