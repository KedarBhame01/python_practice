class Account:
    def __init__(self,p_acc,p_bal):
        self.acc_no = p_acc
        self.balance = p_bal

    def p_balance(self):
        print("Avaliable balance = ",self.balance,"\n")
    
    def debit(self,amt):
        if amt < self.balance:
            self.balance -= amt
            print(f"{amt} Rs Deducted successfully.")
            self.p_balance()

    def credit(self,amt):
        self.balance += amt
        print(f"{amt} Rs Credited successfully.")
        self.p_balance()
    
a1 = Account(123,1000)
a1.p_balance()
print("Account no. = ",a1.acc_no,"\n")
a1.credit(500)
a1.debit(50)
a1.credit(550)