"""Notification implementations (OCP: add new notifier = new class)."""
from .console import ConsoleNotifier
from .email import EmailNotifier

__all__ = ["ConsoleNotifier", "EmailNotifier"]
