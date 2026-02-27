# Mini Project: Order Processing

A small **order processing** flow (create order → save → pay → notify) that uses **OOP** and all **five SOLID principles** in Python.

---

## Architecture

### High-level view

```
┌─────────────────────────────────────────────────────────────────────────┐
│  ENTRY POINT                                                             │
│  main.py / __main__.py  —  builds Order, wires dependencies, runs flow   │
└─────────────────────────────────────┬───────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  APPLICATION LAYER (orchestration)                                      │
│  order_service.OrderService  —  place_order(save → pay → notify)          │
│  Depends only on abstractions (DIP)                                      │
└──────┬──────────────────────────┬──────────────────────────┬────────────┘
       │                          │                          │
       ▼                          ▼                          ▼
┌──────────────┐          ┌──────────────┐          ┌──────────────┐
│  INTERFACES  │          │  INTERFACES  │          │  INTERFACES  │
│  (interfaces.py)        │  (interfaces.py)        │  (interfaces.py)
│  OrderRepository        │  PaymentMethod          │  Notifier    │
└──────┬───────┘          └──────┬───────┘          └──────┬───────┘
       │                          │                          │
       ▼                          ▼                          ▼
┌──────────────┐          ┌──────────────┐          ┌──────────────┐
│  INFRA       │          │  PAYMENTS   │          │ NOTIFICATIONS│
│  storage/    │          │  payments/  │          │ notifications/│
│  • FileOrderRepository  │  • CreditCardPayment   │  • EmailNotifier
│  • InMemoryOrderRepository  • PayPalPayment     │  • ConsoleNotifier
└──────┬───────┘          └─────────────┘          └──────────────┘
       │
       ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  DOMAIN LAYER                                                            │
│  domain/order.py  —  Order, LineItem  (entities, value objects, rules)   │
└─────────────────────────────────────────────────────────────────────────┘
```

### Layers and responsibilities

| Layer | Location | Responsibility | Depends on |
|-------|----------|----------------|------------|
| **Entry** | `main.py`, `__main__.py` | Create domain objects; instantiate concrete implementations; call application service | Application, Domain, all concrete adapters |
| **Application** | `order_service.py` | Orchestrate use case: save order → charge → notify. No persistence/payment/notification logic | Interfaces (abstractions), Domain |
| **Domain** | `domain/` | Core entities and rules: `Order`, `LineItem`; total, line-item subtotal | Nothing (no imports from rest of app) |
| **Interfaces** | `interfaces.py` | Abstract contracts: `OrderRepository`, `PaymentMethod`, `Notifier` (ABCs) | Domain (for `Order` type) |
| **Adapters** | `storage/`, `payments/`, `notifications/` | Concrete implementations of the interfaces (file, memory, credit card, PayPal, email, console) | Interfaces, Domain |

### Dependency direction (DIP)

- **Domain** has no dependency on other layers.
- **Interfaces** depend only on Domain (e.g. `Order` in method signatures).
- **Application** (OrderService) depends on Interfaces and Domain — never on concrete storage/payment/notification classes.
- **Adapters** implement Interfaces and may use Domain types.
- **Entry** (main) knows everything and wires concrete adapters into the service.

```
  main.py  ──►  OrderService  ──►  OrderRepository (interface)
       │              │            PaymentMethod (interface)
       │              │            Notifier (interface)
       │              └──────────► Order, LineItem (domain)
       │
       └──►  FileOrderRepository, CreditCardPayment, EmailNotifier, ...
```

### Data flow: place order

1. **main** builds an `Order` (customer email, line items) and an `OrderService` with injected repository, payment, and notifier.
2. **OrderService.place_order(order)**:
   - Calls **repository.save(order)** → returns `order_id`.
   - Calls **payment.charge(order_id, order.total, order.customer_email)** → success/failure.
   - On success, calls **notifier.notify(customer_email, confirmation_message)**.
3. Returns `order_id` to caller.

### Project layout (with architecture mapping)

```
06_mini_project/
  __init__.py
  __main__.py              # Entry
  main.py                  # Entry (wiring + run)
  interfaces.py            # Interfaces (contracts)
  domain/                  # Domain layer
    __init__.py
    order.py               # Order, LineItem
  order_service.py         # Application layer
  storage/                  # Adapters (persistence)
    __init__.py
    file_storage.py         # FileOrderRepository
    memory_storage.py       # InMemoryOrderRepository
  payments/                 # Adapters (payment)
    __init__.py
    credit_card.py          # CreditCardPayment
    paypal.py               # PayPalPayment
  notifications/           # Adapters (notification)
    __init__.py
    console.py              # ConsoleNotifier
    email.py                # EmailNotifier
```

---

## What it does

1. Create an order with line items (product, quantity, price).
2. Save the order (file or in-memory).
3. Charge via a payment method (credit card or PayPal).
4. Send a confirmation notification (email or console).

## How to run

From the **solid_principals** repo root:

```bash
python -m 06_mini_project.main
```

You should see output like:

```
[CreditCard ****4242] Charged $74.97 for order <uuid>
[EMAIL to customer@example.com] Order <uuid> confirmed. Total: $74.97
Order placed: <uuid>
```

---

## Where SOLID and OOP appear

### OOP

| Concept | Where |
|--------|--------|
| **Encapsulation** | `Order._id` (private), exposed via `id` property; `LineItem.subtotal` as computed property |
| **Composition** | `Order` has a list of `LineItem`; no inheritance between them |
| **Inheritance** | `CreditCardPayment` and `PayPalPayment` extend `PaymentMethod`; same for notifiers and repositories |
| **Polymorphism** | `payment.charge(...)` and `notifier.notify(...)` — same call, different behavior per implementation |
| **Abstraction** | `PaymentMethod`, `Notifier`, `OrderRepository` (ABCs) define the contract |

### SOLID

| Principle | How it’s used |
|-----------|----------------|
| **S — Single Responsibility** | `Order` = data; `OrderRepository` = persistence; `OrderService` = orchestration; `CreditCardPayment` = charge; `EmailNotifier` = send. One clear job per class. |
| **O — Open/Closed** | New payment (e.g. Stripe) = new class `StripePayment(PaymentMethod)`. New notifier (SMS) = new class. No change to `OrderService` or existing code. |
| **L — Liskov Substitution** | Any `PaymentMethod` (or `Notifier`, or `OrderRepository`) can be swapped in. `FileOrderRepository` and `InMemoryOrderRepository` are interchangeable. |
| **I — Interface Segregation** | Small interfaces: `PaymentMethod` (only `charge`), `Notifier` (only `notify`), `OrderRepository` (only `save`, `find_by_id`). No fat interface. |
| **D — Dependency Inversion** | `OrderService` depends on `OrderRepository`, `PaymentMethod`, `Notifier` (abstractions). `main.py` injects concrete implementations (file storage, credit card, email). |

---

## Try this

1. **Add a new payment method** — e.g. `payments/crypto.py` with `class CryptoPayment(PaymentMethod)`. Use it in `main.py` instead of `CreditCardPayment`. No change to `OrderService`.
2. **Use in-memory storage** — In `main.py`, use `InMemoryOrderRepository()` instead of `FileOrderRepository(...)`. Same interface, different implementation (LSP).
3. **Switch notifier** — Use `ConsoleNotifier()` instead of `EmailNotifier()` in `main.py` to “notify” via print.

This mini project is part of the [SOLID + OOP Roadmap](../ROADMAP.md).
