"""
Wire and run: create order, inject implementations, place order.
DIP: we inject concrete PaymentMethod, Notifier, OrderRepository here;
     OrderService only sees the abstractions.
Run from repo root: python -m 06_mini_project.main
"""
from .domain import Order
from .order_service import OrderService
from .payments import CreditCardPayment
from .storage import FileOrderRepository
from .notifications import EmailNotifier


def main() -> None:
    # DIP: inject implementations; OrderService depends on abstractions
    repository = FileOrderRepository("06_mini_project_orders.json")
    payment = CreditCardPayment(last_four_digits="4242")
    notifier = EmailNotifier()

    service = OrderService(repository=repository, payment=payment, notifier=notifier)

    # Build order (OOP: composition — order has line items)
    order = Order(customer_email="customer@example.com")
    order.add_item("Python Book", 2, 29.99)
    order.add_item("SOLID Mug", 1, 14.99)

    order_id = service.place_order(order)
    print(f"Order placed: {order_id}")


if __name__ == "__main__":
    main()
