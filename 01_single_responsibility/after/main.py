"""
AFTER SRP: Each class has one responsibility.
- User: data only (could add validation).
- UserRepository: load/save users.
- EmailService: send emails (here we just print).
- ConsoleLogger: log messages (could be swapped for file logger).
Run: python -m 01_single_responsibility.after.main
"""
from __future__ import annotations

import json
from pathlib import Path
from dataclasses import dataclass


@dataclass
class User:
    """Single responsibility: represent user data."""

    name: str
    email: str


class UserRepository:
    """Single responsibility: persist and load users."""

    def __init__(self, data_file: str = "users.json"):
        self.data_file = Path(data_file)

    def find_all(self) -> list[dict]:
        if not self.data_file.exists():
            return []
        return json.loads(self.data_file.read_text())

    def save_all(self, users: list[dict]) -> None:
        self.data_file.write_text(json.dumps(users, indent=2))


class EmailService:
    """Single responsibility: send emails (stub: prints)."""

    def send_welcome(self, email: str) -> None:
        print(f"[EMAIL] Sent welcome to {email}")


class ConsoleLogger:
    """Single responsibility: log messages."""

    def info(self, message: str) -> None:
        print(f"[LOG] {message}")


def register_user(
    name: str,
    email: str,
    repository: UserRepository,
    email_service: EmailService,
    logger: ConsoleLogger,
) -> User:
    """Orchestrates the flow; each step is delegated to the right class."""
    user = User(name=name, email=email)
    users = repository.find_all()
    users.append({"name": user.name, "email": user.email})
    repository.save_all(users)
    email_service.send_welcome(user.email)
    logger.info(f"Registered user: {user.name}")
    return user


def main():
    repo = UserRepository()
    email_svc = EmailService()
    logger = ConsoleLogger()
    register_user("Alice", "alice@example.com", repo, email_svc, logger)


if __name__ == "__main__":
    main()
