"""Credit card payment — one concrete implementation of PaymentMethod (LSP: substitutable)."""
from ..interfaces import PaymentMethod


class CreditCardPayment(PaymentMethod):
    def __init__(self, last_four_digits: str = "4242"):
        self.last_four_digits = last_four_digits

    def charge(self, order_id: str, amount: float, customer_email: str) -> bool:
        print(f"[CreditCard ****{self.last_four_digits}] Charged ${amount:.2f} for order {order_id}")
        return True

