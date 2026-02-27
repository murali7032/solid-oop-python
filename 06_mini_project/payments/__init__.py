"""Payment method implementations (OCP: extend by adding new classes)."""
from .credit_card import CreditCardPayment
from .paypal import PayPalPayment

__all__ = ["CreditCardPayment", "PayPalPayment"]
