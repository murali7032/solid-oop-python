"""
Order service: orchestrates place order → save → pay → notify.
SRP: only orchestration; no payment logic, no storage logic, no notification logic.
DIP: depends on abstractions (PaymentMethod, Notifier, OrderRepository); callers inject implementations.
"""
from typing import Optional

from .domain.order import Order
from .interfaces import Notifier, OrderRepository, PaymentMethod


class OrderService:
    def __init__(
        self,
        repository: OrderRepository,
        payment: PaymentMethod,
        notifier: Notifier,
    ) -> None:
        self._repository = repository
        self._payment = payment
        self._notifier = notifier

    def place_order(self, order: Order) -> Optional[str]:
        """Save order, charge payment, send confirmation. Returns order_id or None on failure."""
        order_id = self._repository.save(order)
        success = self._payment.charge(
            order_id=order_id,
            amount=order.total,
            customer_email=order.customer_email,
        )
        if not success:
            return None
        self._notifier.notify(
            order.customer_email,
            f"Order {order_id} confirmed. Total: ${order.total:.2f}",
        )
        return order_id
