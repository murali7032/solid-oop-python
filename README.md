# SOLID + OOP in Python — Practical Learning Repo

Learn **OOP** and **SOLID principles** in Python by doing: each folder has (or will have) `before` / `after` examples you can run and compare.

## Start here

- **[ROADMAP.md](ROADMAP.md)** — Full learning path: phases, timeline, and how to use this repo.

## Structure

| Folder | Content |
|--------|--------|
| `00_oop_basics/` | Classes, inheritance, polymorphism, composition, ABCs |
| `01_single_responsibility/` | SRP: one class, one job (with before/after) |
| `02_open_closed/` | OCP: extend via new code, not by editing |
| `03_liskov_substitution/` | LSP: subtypes substitutable for base |
| `04_interface_segregation/` | ISP: small, focused interfaces |
| `05_dependency_inversion/` | DIP: depend on abstractions, inject deps |

## Run examples

From the repo root (e.g. `c:\Users\Gajulapalli.Reddy\cursor\solid_principals`):

```bash
python -m 00_oop_basics.shapes
python -m 00_oop_basics.composition_example
python -m 01_single_responsibility.before.main
python -m 01_single_responsibility.after.main
```

## Quick SOLID recap

- **S** — One class, one reason to change.
- **O** — Open for extension (new classes), closed for modification.
- **L** — Subclasses must be drop-in replacements for the base.
- **I** — Prefer many small interfaces over one big one.
- **D** — Depend on abstractions; inject concrete implementations.

Happy learning.
