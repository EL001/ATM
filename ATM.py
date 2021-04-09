class ATM:
    def __init__(self, cash = 1000):
        self.cash = cash
        print ("Account balance is", cash)
    
    def addcash(self):
        cash_add = int(input("Amount of cash to be added "))
        self.cash_add = cash_add
        self.cash = cash_add + self.cash
        print ("Total cash is", self.cash)
           
    def withdraw(self):
        withdrawal_amt = int(input("cash to withdraw "))
        self.cash = self.cash - withdrawal_amt
        print ("Total cash after withdrawal is ", self.cash)
        
    def balance(self):
        print ("Total amount in account is ", self.cash)
    
    
    
money = ATM()

money.addcash()

money.withdraw() 

money.balance()
