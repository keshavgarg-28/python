# Task 1
# Design a class hierarchy for a Payment System.
# Requirements:
# Create a base class Payment:
# Has an instance variable amount
# Has a method pay() that raises NotImplementedError
# Create two child classes:
# CreditCardPayment
# UPIPayment
# Each child class should:
# Override the pay() method
# Return a string describing the payment method and amount
# Add a method process_payment(payment_obj):
# Accepts an object of type Payment
# Calls pay() without checking the object type
# Demonstrates runtime polymorphism
from abc import ABC, abstractmethod
class Payment(ABC):
    def __init__(self,amount):
        self.amount=amount
    @abstractmethod
    def pay(self):
        raise NotImplementedError("Subclass needs to implement this")
class CreditCardPayment(Payment):
    def pay(self):
        return f"{self.amount} paid using credit card"
class UPIPayment(Payment):
    def pay(self):
        return f"{self.amount} paid using UPI"
def process_payment(payment_obj):
    print(payment_obj.pay())
p1=CreditCardPayment(1000)
p2=UPIPayment(500)

process_payment(p1)
process_payment(p2)