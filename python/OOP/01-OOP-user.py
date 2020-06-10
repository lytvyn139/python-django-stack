class Client:
    def __init__(self, username, email_address):
        self.name = username			
        self.email = email_address		
        self.account_balance = 0		

    def make_deposit(self, amount): 	
        self.account_balance += amount
        return self	

    def make_withdrawal(self, amount): 	
        if self.account_balance < amount:
            print(f"Not enought money for withdrawl ${amount}")
            print(f"I'm charing {self.name} $5 as overdraft fee")
            self.account_balance -= 5
        else:
            self.account_balance -= amount	
        return self

    def display_balance(self):
        #print(f"{self.name} balance is ${self.account_balance}")
        return self.account_balance
        

    def transfter_money(self, other_user, amount):
        print(f"transfering $ {amount} from {self.name} to {other_user.name}")
        self.account_balance -= amount
        other_user.account_balance += amount

#creating instances of class Client
sam = Client('Sam Wise', 'sam-wise@gmail.com')
gendalf = Client('Gendalf the Grey', 'gendalf@gmail.com')
sauron = Client('Sauron', 'sauron@gmail.com')
print('*'*80)
print(f"{sam.name} is making $500 deposit")
sam.make_deposit(500)
print(f"{sam.name} balance now is ${sam.account_balance}")
print(f"{sam.name} is withdrawing -$270 ")
sam.make_withdrawal(270)
print(f"{sam.name} balance now is ${sam.account_balance}")
print(f"{sam.name} is withdrawing -$3000 ")
sam.make_withdrawal(3000)
print(f"{sam.name} balance now is ${sam.account_balance}")
print('*'*80)
print(f"Looks like boys: {gendalf.name}, {sauron.name} did some side hustle")
gendalf.account_balance = 450
sauron.account_balance = 500
print(f"Now {gendalf.name} have ${gendalf.account_balance} & {sauron.name} have ${sauron.account_balance}")
print(f"Unfortunatelly {gendalf.name} lost the card game, and now he have to give $400 to {gendalf.account_balance} ")
gendalf.transfter_money(sauron, 400)
print("in the end of the day they have")
print(f"Sam: ${sam.display_balance()}, Gendalf: ${gendalf.display_balance()}, Sauron: ${sauron.display_balance()}")


