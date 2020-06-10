class BankAccount:
    def __init__(self, int_rate = .05, balance =0):
        self.interest_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        print(f"depositing ${amount}")
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance > amount:
            print (f'withdrawling {amount}')
            self.balance -= amount
        else:
            print('insufficient funds, deducting $5')
            self.balance -=5
        return self

    def display_account_info(self):
        print(self.balance)
        return self.balance 
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance = (self.balance * self.interest_rate) + self.balance
            return self
        else:
            print ('man you broke, get a job !!!')

account_01 = BankAccount()
account_02 = BankAccount()

account_01.deposit(100).deposit(100).deposit(100).withdraw(50).yield_interest()
print(account_01.__dict__)

print('*'*80)

account_02.deposit(50).deposit(50).withdraw(50).withdraw(50)
print(account_02.__dict__)

account_01.deposit(100)
account_01.display_account_info()