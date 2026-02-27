"""
Abstractions (protocols) for the mini project.
DIP: high-level code depends on these, not concrete classes.
ISP: small, focused interfaces — no fat interface.
"""
from abc import ABC, abstractmethod
from typing import Optional

from .domain.order import Order


class PaymentMethod(ABC):
    """ISP: only 'charge' — one clear responsibility. OCP: add new payment = new class."""

    @abstractmethod
    def charge(self, order_id: str, amount: float, customer_email: str) -> bool:
        """Process payment. Returns True if successful."""
        pass


class Notifier(ABC):
    """ISP: only 'notify'. OCP: add new channel (SMS, push) = new class."""

    @abstractmethod
    def notify(self, customer_email: str, message: str) -> None:
        """Send notification to customer."""
        pass


class OrderRepository(ABC):
    """ISP: save and find. LSP: any implementation is substitutable (file, DB, memory)."""

    @abstractmethod
    def save(self, order: Order) -> str:
        """Persist order; return assigned id."""
        pass

    @abstractmethod
    def find_by_id(self, order_id: str) -> Optional[Order]:
        """Load order by id; return None if not found."""
        pass
