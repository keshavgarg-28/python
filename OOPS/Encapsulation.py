class Bank:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self, amount):
        self.__balance+=amount
    def get_balance(self):
        return self.__balance
b=Bank(10000)
b.deposit(4000)
print(b.get_balance())