class Bank:
    def __init__(self,balance):
        self.balance=balance
    def credit(self, amount):
        self.balance+=amount
        print("Amount credited:",amount)
        print("Balance Remaining:",self.get_balance())
    def debit(self, amount):
        self.balance-=amount
        print("Amount debited:",amount)
        print("Balance Remaining:",self.get_balance())
    def get_balance(self):
        return self.balance
p1=Bank(10000)
p1.credit(20000)
p1.debit(10000)