# Phase 4: Interface Segregation (ISP)
'''
**Goal:** Prefer many small, focused interfaces over one large interface. Clients shouldn’t depend on methods they don’t use.

**Exercise:**
1. **before/** — Interface `Worker` with `work()`, `eat()`, `sleep()`, `get_paid()`. `Robot` must implement `eat()` and `sleep()` even though it doesn’t need them.
2. **after/** — Split into `Workable`, `Eatable`, `Payable`, etc. `Human` implements several; `Robot` implements only `Workable`.

Implement: `before/main.py` and `after/main.py` using ABCs or Protocols.
'''
from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

    @abstractmethod
    def get_paid(self):
        pass

class Human(Worker):
    def work(self):
        print("Human is working.")

    def eat(self):
        print("Human is eating.")

    def sleep(self):
        print("Human is sleeping.")

    def get_paid(self):
        print("Human got paid.")

class Robot(Worker):
    def work(self):
        print("Robot is working.")

    def eat(self):
        print("Robot doesn't need to eat, but must implement this method.")

    def sleep(self):
        print("Robot doesn't need to sleep, but must implement this method.")

    def get_paid(self):
        print("Robot doesn't get paid, but must implement this method.")

def main():
    workers = [Human(), Robot()]
    for w in workers:
        print(f"\nTesting {w.__class__.__name__}:")
        w.work()
        w.eat()
        w.sleep()
        w.get_paid()

if __name__ == "__main__":
    main()
