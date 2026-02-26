"""
BEFORE SRP: One class does everything — user data, file I/O, email, "logging".
Violation: UserManager has multiple reasons to change (storage format, email provider, logging).
Run: python -m 01_single_responsibility.before.main
"""
import json
from pathlib import Path


class UserManager:
    """Does too much: user logic + persistence + email + logging."""

    def __init__(self, data_file: str = "users.json"):
        self.data_file = Path(data_file)

    def register(self, name: str, email: str) -> dict:
        user = {"name": name, "email": email}
        # Responsibility 1: business rule (we could add validation here)
        # Responsibility 2: read file
        data = []
        if self.data_file.exists():
            data = json.loads(self.data_file.read_text())
        data.append(user)
        # Responsibility 3: write file
        self.data_file.write_text(json.dumps(data, indent=2))
        # Responsibility 4: "send email"
        print(f"[EMAIL] Sent welcome to {email}")
        # Responsibility 5: "log"
        print(f"[LOG] Registered user: {name}")
        return user


def main():
    mgr = UserManager()
    mgr.register("Alice", "alice@example.com")


if __name__ == "__main__":
    main()
