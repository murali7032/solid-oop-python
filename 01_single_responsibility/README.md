# Phase 1: Single Responsibility (SRP)

- **before/** — One class does user logic, file I/O, and email. Hard to test and change.
- **after/** — Split into `User`, `UserRepository`, `EmailService`. One job per class.

Compare the two and run:
```bash
python -m 01_single_responsibility.before.main
python -m 01_single_responsibility.after.main
```
