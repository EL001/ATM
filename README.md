|class ATM
   ATM(cash=1000)
   
   This class gives a user an account balance of #1000 by default, and contains methods that adds money, withdraws money and checks balance.
   
   Methods defined here:
   
  | __init__(self, cash=1000)
       
       User is given a default account balance of #1000
       
       Parameter
       ----------
       cash : int
   
   |addcash(self, cash_add)
       Adds money to the user's account and returns account balance
      
       Parameter
       ----------
       cash_add : int
           Amount of money to be added to the account
   
   |balance(self)
       Returns account balance
   
   |withdraw(self)
       Colllects an input of amount to be withdrawn and returns account balance

