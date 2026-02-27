"""
Domain model: Order and LineItem.
OOP: encapsulation (private _id), composition (Order has list of LineItems).
"""
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class LineItem:
    """One line in an order: product name, quantity, unit price."""

    product_name: str
    quantity: int
    unit_price: float

    @property
    def subtotal(self) -> float:
        return self.quantity * self.unit_price


@dataclass
class Order:
    """
    Order: customer email + line items.
    Single responsibility: hold order data and compute total.
    """

    customer_email: str
    line_items: list[LineItem] = field(default_factory=list)
    _id: Optional[str] = field(default=None, repr=False)

    @property
    def id(self) -> Optional[str]:
        return self._id

    @id.setter
    def id(self, value: Optional[str]) -> None:
        self._id = value

    @property
    def total(self) -> float:
        return sum(item.subtotal for item in self.line_items)

    def add_item(self, product_name: str, quantity: int, unit_price: float) -> None:
        self.line_items.append(
            LineItem(product_name=product_name, quantity=quantity, unit_price=unit_price)
        )
