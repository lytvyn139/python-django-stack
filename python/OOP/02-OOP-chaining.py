class Client:
    def __init__(self, username, email_address):
        self.name = username			
        self.email = email_address		
        self.account_balance = 0		

    def make_deposit(self, amount): 	
        self.account_balance += amount
        return self	

average_joe = Client('Joe the Avg', 'email@email.com')
average_joe.make_deposit(300).make_deposit(500).make_deposit(500).make_deposit(1).make_deposit(15)
print(average_joe.account_balance)


