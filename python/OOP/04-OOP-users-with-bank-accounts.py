

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.checking_account = BankAccount(0, 0)	
        self.savings_account = BankAccount(0.5, 0)	

    def make_deposit(self, amount, account_type): 	
        if account_type == "checking":
            print(f"you've made ${amount} deposit, to your {account_type} account")
            self.checking_account.deposit(amount) #method in bank class
        elif account_type == "saving":
            print(f"you've made ${amount} deposit, to your {account_type} account")
            self.savings_account.deposit(amount) #method in bank class
        else: 
            print('account not found')
        return self
    
    def make_withdrawal(self, amount, account_type):
        if account_type == "checking":
            self.checking_account.withdraw(amount) #method in bank class
            print(f"${amount} withdrawal")
        elif account_type == "saving":
            self.savings_account.withdraw(amount) #method in bank class
            print(f"${amount} withdrawal")
        else: 
            print('account not found')
        return self

    def display_user_balance(self, account_type):
        if account_type == "checking":
            print(f"your balance on {account_type} is: ")
            self.checking_account.display_account_info()
        elif account_type == "saving":
            print(f"your balance on {account_type} is: ")
            self.savings_account.display_account_info()
        else: 
            print('account not found')
        return self

    def transfer_money(self, other_user, amount):
        self.account.balance -= amount
        other_user.account.balance += amount
        self.display_user_balance()
        other_user.display_user_balance()
        return self

class BankAccount:
    def __init__(self, int_rate = 0.03, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print("Insufficient funds: Charging a $5 fee" )
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"${self.balance}") 

    def yield_interest(self):
        if self.balance >0:
            self.balance = self.balance + (self.balance * self.int_rate)
        return self

print('=============== BANK ================ OF ================ NAMERZ ================')
user = User("Yurko","Yurko@gmail.com")
user2 = User("Sam", "Sam@gmail.com")

print(f"Welcome back: {user.name}, what account you'll be using today??? checking/saving")
user.make_deposit(10000, 'saving').make_deposit(1250, 'checking').display_user_balance("saving").display_user_balance("checking")
print('Time to get some car:')
user.make_withdrawal(7500, 'saving').display_user_balance("saving")
print('Will try to withdraw $1300 from my checking ')
user.make_withdrawal(1300, 'checking').display_user_balance("checking")




