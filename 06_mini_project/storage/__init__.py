"""Order persistence (LSP: any implementation is substitutable)."""
from .file_storage import FileOrderRepository
from .memory_storage import InMemoryOrderRepository

__all__ = ["FileOrderRepository", "InMemoryOrderRepository"]
