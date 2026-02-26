# Phase 4: Interface Segregation (ISP)

**Goal:** Prefer many small, focused interfaces over one large interface. Clients shouldn’t depend on methods they don’t use.

**Exercise:**
1. **before/** — Interface `Worker` with `work()`, `eat()`, `sleep()`, `get_paid()`. `Robot` must implement `eat()` and `sleep()` even though it doesn’t need them.
2. **after/** — Split into `Workable`, `Eatable`, `Payable`, etc. `Human` implements several; `Robot` implements only `Workable`.

Implement: `before/main.py` and `after/main.py` using ABCs or Protocols.
