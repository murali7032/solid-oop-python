# SOLID + OOP in Python — Practical Roadmap

A step-by-step path to learn **OOP** and **SOLID principles** in Python by building small projects and refactoring code.

---

## Phase 0: Python OOP fundamentals (1–2 weeks)

Before SOLID, you need a solid grasp of Python OOP.

| Topic | What to learn | Practice |
|-------|----------------|----------|
| **Classes & objects** | `class`, `__init__`, `self`, instances | Create a `BankAccount` or `Product` class |
| **Encapsulation** | Private `_attr`, `@property`, getters/setters | Hide internal state, expose clean API |
| **Inheritance** | `class Child(Parent):`, `super()` | `Animal` → `Dog`, `Cat` with overridden methods |
| **Polymorphism** | Same method name, different behavior per class | `speak()` on Dog vs Cat |
| **Composition vs inheritance** | “Has-a” (compose) vs “is-a” (inherit) | Engine inside Car, not Car inheriting Engine |
| **Abstract base classes** | `abc.ABC`, `@abstractmethod` | Define interface; subclasses implement |

**Deliverable:** A small domain (e.g. shapes, vehicles, or a mini library system) using classes, inheritance, and composition.

---

## Phase 1: Single Responsibility Principle (SRP)

**Idea:** One class = one reason to change. One job per class.

| Step | Action |
|------|--------|
| 1 | Write a class that does too much (e.g. User + save to DB + send email + log). |
| 2 | Split into: `User` (data), `UserRepository` (save/load), `EmailService`, `Logger`. |
| 3 | Each class has a single, clear responsibility. |

**Practice folder:** `01_single_responsibility/`

**Question to ask:** “If requirements change in one area (e.g. logging), do I touch only one class?”

---

## Phase 2: Open/Closed Principle (OCP)

**Idea:** Open for extension, closed for modification. Add behavior via new code, not by editing existing classes.

| Step | Action |
|------|--------|
| 1 | Write a function that uses `if/elif` on types (e.g. different shapes, payment methods). |
| 2 | Refactor: define an abstract base (e.g. `Shape`, `PaymentMethod`) and one class per variant. |
| 3 | Add a new variant by adding a new class, not by changing the core logic. |

**Practice folder:** `02_open_closed/`

**Question to ask:** “Can I add a new shape/payment/rule by only adding a new class and not editing existing ones?”

---

## Phase 3: Liskov Substitution Principle (LSP)

**Idea:** Subtypes must be substitutable for their base type. No surprises when you swap implementation.

| Step | Action |
|------|--------|
| 1 | Create a base class and subclasses (e.g. `Bird` → `Penguin`). |
| 2 | Avoid breaking expectations: e.g. if base has `fly()`, don’t make `Penguin.fly()` raise or do something unrelated. Prefer composition or a more precise hierarchy. |
| 3 | Ensure subclasses don’t strengthen preconditions or weaken postconditions. |

**Practice folder:** `03_liskov_substitution/`

**Question to ask:** “Can I pass any subclass where the base type is expected, without callers knowing or breaking?”

---

## Phase 4: Interface Segregation Principle (ISP)

**Idea:** Many small, focused interfaces beat one huge interface. Clients shouldn’t depend on methods they don’t use.

| Step | Action |
|------|--------|
| 1 | Create a “fat” interface (e.g. `Worker` with `work()`, `eat()`, `sleep()`, `get_paid()`). |
| 2 | Split into roles: `Workable`, `Eatable`, `Payable`, etc. |
| 3 | Classes implement only the interfaces they need (e.g. Robot: `Workable` only). |

**Practice folder:** `04_interface_segregation/`

**Question to ask:** “Does each class implement only the methods that make sense for it?”

---

## Phase 5: Dependency Inversion Principle (DIP)

**Idea:** Depend on abstractions (interfaces/ABCs), not concrete classes. High-level logic shouldn’t depend on low-level details.

| Step | Action |
|------|--------|
| 1 | Write a service that directly instantiates a concrete DB or email client. |
| 2 | Introduce an abstract interface (e.g. `Storage`, `NotificationService`) and inject it. |
| 3 | High-level code uses the interface; tests and production inject real or fake implementations. |

**Practice folder:** `05_dependency_inversion/`

**Question to ask:** “Can I swap the database or email provider without changing the core business logic?”

---

## Suggested order and timeline

```
Week 1–2   → Phase 0 (OOP) + Phase 1 (SRP)
Week 3     → Phase 2 (OCP)
Week 4     → Phase 3 (LSP) + Phase 4 (ISP)
Week 5     → Phase 5 (DIP)
Week 6     → Mini project applying all five (e.g. order processing, report generator)
```

---

## How to use this repo

- Each numbered folder (`01_single_responsibility`, …) has:
  - `before/` — code that violates the principle (or is “naive”).
  - `after/` — refactored code that follows the principle.
- Try to refactor `before` yourself, then compare with `after`.
- Run examples: from repo root,  
  `python -m 01_single_responsibility.after.main`  
  (adjust module path as you add `main` or `run` modules).

---

## Quick reference

| Principle | One-line takeaway |
|-----------|-------------------|
| **S**RP | One class, one job. |
| **O**CP | Extend with new code; don’t edit existing. |
| **L**SP | Subclasses must be drop-in replacements. |
| **I**SP | Small, role-based interfaces. |
| **D**IP | Depend on abstractions; inject dependencies. |

---

## Next steps

1. Complete Phase 0 with a small OOP project in Python.
2. Go through each SOLID phase: read the principle, code the `before`, then refactor to `after`.
3. Build one small end-to-end feature (e.g. “place order → persist → notify”) applying all five principles.

Once you’re comfortable, you can add a `06_mini_project/` and implement one feature using SOLID from the start.
