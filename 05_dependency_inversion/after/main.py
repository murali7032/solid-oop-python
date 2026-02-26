from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def save_order(self, order):
        pass

class NotificationService(ABC):
    @abstractmethod
    def send(self, message, to):
        pass

class SqliteDatabase(Storage):
    def __init__(self):
        self._orders = []

    def save_order(self, order):
        print(f"[Sqlite] Saving order: {order}")
        self._orders.append(order)

class PostgresSQLDatabase(Storage):
    def __init__(self):
        self._orders = []

    def save_order(self, order):
        print(f"[PostgresSQL] Saving order: {order}")
        self._orders.append(order)

class SmtpEmail(NotificationService):
    def send(self, message, to):
        print(f"[SMTP] Sending email to {to}: {message}")

class OrderService:
    def __init__(self, storage: Storage, notifier: NotificationService):
        self.storage = storage
        self.notifier = notifier

    def place_order(self, order, customer_email):
        self.storage.save_order(order)
        self.notifier.send(f"Your order {order} has been placed!", customer_email)

# Example usage
if __name__ == '__main__':
    # db = SqliteDatabase()
    db = PostgresSQLDatabase()
    email = SmtpEmail()
    service = OrderService(db, email)
    service.place_order(order="Widget", customer_email="alice@example.com")
