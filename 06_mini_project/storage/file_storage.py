"""File-based order storage (JSON). SRP: only persistence logic here."""
import json
import uuid
from pathlib import Path
from typing import Optional

from ..domain.order import Order, LineItem
from ..interfaces import OrderRepository


class FileOrderRepository(OrderRepository):
    def __init__(self, file_path: str = "orders.json") -> None:
        self._path = Path(file_path)

    def save(self, order: Order) -> str:
        order_id = str(uuid.uuid4())
        order.id = order_id
        data = self._load_all()
        data[order_id] = self._order_to_dict(order)
        self._path.write_text(json.dumps(data, indent=2))
        return order_id

    def find_by_id(self, order_id: str) -> Optional[Order]:
        data = self._load_all()
        raw = data.get(order_id)
        if not raw:
            return None
        return self._dict_to_order(order_id, raw)

    def _load_all(self) -> dict:
        if not self._path.exists():
            return {}
        return json.loads(self._path.read_text())

    def _order_to_dict(self, order: Order) -> dict:
        return {
            "customer_email": order.customer_email,
            "line_items": [
                {
                    "product_name": li.product_name,
                    "quantity": li.quantity,
                    "unit_price": li.unit_price,
                }
                for li in order.line_items
            ],
        }

    def _dict_to_order(self, order_id: str, raw: dict) -> Order:
        order = Order(customer_email=raw["customer_email"])
        order.id = order_id
        for li in raw.get("line_items", []):
            order.add_item(li["product_name"], li["quantity"], li["unit_price"])
        return order
