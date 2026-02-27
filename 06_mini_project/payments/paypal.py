"""PayPal payment — another implementation (OCP: no change to existing code)."""
from ..interfaces import PaymentMethod


class PayPalPayment(PaymentMethod):
    def __init__(self, sandbox: bool = True):
        self.sandbox = sandbox

    def charge(self, order_id: str, amount: float, customer_email: str) -> bool:
        env = "sandbox" if self.sandbox else "live"
        print(f"[PayPal {env}] Charged ${amount:.2f} for {customer_email}, order {order_id}")
        return True
