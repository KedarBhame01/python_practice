class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
    def debit(self,amt):
        self.balance -= amt
        print("rs",amt," has been debited")
        print("Account balance is ",self.balance)
    def credit(self,amt):
        self.balance += amt
        print("rs",amt," has been credited")
        print("Account balance is ",self.balance) 
    # but this balance method is not working 
    # when we call it
    def balance(self):
        print("Account balance is ",self.balance)   

acc1= Account(10000,12345)
print(acc1.balance)        
print(acc1.account_no)
# del Account.debit
acc1.debit(2000)
acc1.credit(3000)
acc1.balance 
       
