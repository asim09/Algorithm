class Payment:
    def process_payment(self, amount):
        pass  # To be overridden by subclasses

class CreditCard(Payment):
    def process_payment(self, amount):
        print(f"Paid {amount} using Credit Card.")

class PayPal(Payment):
    def process_payment(self, amount):
        print(f"Paid {amount} using PayPal.")

class UPI(Payment):
    def process_payment(self, amount):
        print(f"Paid {amount} using UPI.")

# Using polymorphism
payments = [CreditCard(), PayPal(), UPI()]

for payment in payments:
    payment.process_payment(1000)
