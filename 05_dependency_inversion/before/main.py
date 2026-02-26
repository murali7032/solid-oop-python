


# BEFORE Dependency Inversion Principle (DIP) Example

# Low-level database (concrete, hard-coded)
class SqliteDatabase:
    def save_order(self, order):
        print(f"Saving order '{order}' to SQLite database.")

# Low-level notification (concrete, hard-coded)
class SmtpEmail:
    def send_email(self, to, subject, body):
        print(f"Sending email to {to}: {subject}\n{body}\n")

# High-level module, directly depends on concrete classes
class OrderService:
    def __init__(self):
        self.db = SqliteDatabase()
        self.email = SmtpEmail()

    def place_order(self, order, user_email):
        self.db.save_order(order)
        self.email.send_email(
            user_email,
            "Order Confirmation",
            f"Thank you for your order: {order}"
        )

def main():
    service = OrderService()
    service.place_order("Widge'''
High-level modules should not depend on low-level modules.
Both should depend on abstractions.
# Phase 5: Dependency Inversion (DIP)

**Goal:** Depend on abstractions (interfaces/ABCs), not concrete classes. Inject dependencies so you can swap implementations (e.g. for tests or different backends).

**Exercise:**
1. **before/** — `OrderService` that does `db = SqliteDatabase()` and `email = SmtpEmail()` inside. Hard to test or switch to Postgres/Redis.
2. **after/** — Define `Storage` and `NotificationService` (abstract). `OrderService` receives them in `__init__`. Tests inject in-memory/fake implementations.

Implement: `before/main.py` and `after/main.py`.
'''t", "alice@example.com")

if __name__ == "__main__":
    main()
