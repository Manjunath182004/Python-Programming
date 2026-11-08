from abc import ABC, abstractclassmethod

class PaymentProcessor(ABC):

    @abstractclassmethod
    def process_payment(self, amount):
        """This is an abstract method. 
        It has no code implementation here, only the rule that 
        any child class MUST implement it."""

        pass
class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount):
        print("Connecting to secure bank gateway...")
        print("Verifying card digits and CVV...")
        print(f"Successfully charged ₹{amount} via Credit Card.")  


class PayPalPayment(PaymentProcessor):
    def process_payment(self, amount):
        print("Redirecting to PayPal login page...")
        print("Checking PayPal wallet balance...")
        print(f"Successfully transferred ₹{amount} from PayPal account.")



payment_method = CreditCardPayment()

payment_method.process_payment(500)

payment_method2 = PayPalPayment()

payment_method2.process_payment(800)