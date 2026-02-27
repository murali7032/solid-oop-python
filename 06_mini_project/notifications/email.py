"""Email notifier — stub that prints (replace with real SMTP later; SRP: only this file changes)."""
from ..interfaces import Notifier


class EmailNotifier(Notifier):
    def notify(self, customer_email: str, message: str) -> None:
        print(f"[EMAIL to {customer_email}] {message}")
