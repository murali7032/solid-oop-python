# Phase 2: Open/Closed (OCP)

**Goal:** Add new behavior by adding new code (e.g. new classes), not by editing existing code.

**Exercise:**
1. **before/** — Write a function `total_area(shapes)` that uses `if type(s) == Rectangle: ... elif type(s) == Circle: ...`. Adding a new shape forces you to edit this function.
2. **after/** — Use abstract `Shape` with `.area()`. Add `Triangle` by creating a new class only; no change to `total_area`.

You implement: `before/main.py` and `after/main.py` (or reuse `00_oop_basics/shapes.py` and a new `Triangle`).
