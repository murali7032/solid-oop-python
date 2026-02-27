"""Console notifier — prints to stdout (e.g. for dev/tests)."""
from ..interfaces import Notifier


class ConsoleNotifier(Notifier):
    def notify(self, customer_email: str, message: str) -> None:
        print(f"[Notify → {customer_email}] {message}")

