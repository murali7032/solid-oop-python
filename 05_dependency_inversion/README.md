# Phase 5: Dependency Inversion (DIP)

**Goal:** Depend on abstractions (interfaces/ABCs), not concrete classes. Inject dependencies so you can swap implementations (e.g. for tests or different backends).

**Exercise:**
1. **before/** — `OrderService` that does `db = SqliteDatabase()` and `email = SmtpEmail()` inside. Hard to test or switch to Postgres/Redis.
2. **after/** — Define `Storage` and `NotificationService` (abstract). `OrderService` receives them in `__init__`. Tests inject in-memory/fake implementations.

Implement: `before/main.py` and `after/main.py`.
