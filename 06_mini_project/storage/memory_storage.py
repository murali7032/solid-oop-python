"""In-memory order storage — for tests or demo. LSP: same interface as file storage."""
import uuid
from typing import Optional

from ..domain.order import Order
from ..interfaces import OrderRepository


class InMemoryOrderRepository(OrderRepository):
    def __init__(self) -> None:
        self._orders: dict[str, Order] = {}

    def save(self, order: Order) -> str:
        order_id = str(uuid.uuid4())
        order.id = order_id
        self._orders[order_id] = order
        return order_id

    def find_by_id(self, order_id: str) -> Optional[Order]:
        return self._orders.get(order_id)
