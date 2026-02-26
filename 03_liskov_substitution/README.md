# Phase 3: Liskov Substitution (LSP)

**Goal:** Subclasses must be substitutable for the base class. Callers should not need to know the concrete type.

**Exercise:**
1. **before/** — `Bird` with `fly()`. `Penguin` inherits `Bird` but overrides `fly()` to raise or do nothing → breaks callers that expect "every bird can fly."
2. **after/** — Refactor: e.g. `FlyingBird` and `Bird`, or use composition (e.g. `FlyBehavior`) so `Penguin` doesn’t promise `fly()`.

Implement: `before/main.py` and `after/main.py`.
