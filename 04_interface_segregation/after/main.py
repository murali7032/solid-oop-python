# Phase 4: Interface Segregation (ISP)
'''
**Goal:** Prefer many small, focused interfaces over one large interface. Clients shouldn’t depend on methods they don’t use.

**Exercise:**
1. **before/** — Interface `Worker` with `work()`, `eat()`, `sleep()`, `get_paid()`. `Robot` must implement `eat()` and `sleep()` even though it doesn’t need them.
2. **after/** — Split into `Workable`, `Eatable`, `Payable`, etc. `Human` implements several; `Robot` implements only `Workable`.

Implement: `before/main.py` and `after/main.py` using ABCs or Protocols.
'''

from abc import ABC, abstractmethod

# Define small, focused interfaces
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Sleepable(ABC):
    @abstractmethod
    def sleep(self):
        pass

class Payable(ABC):
    @abstractmethod
    def get_paid(self):
        pass

class Chargeable(ABC):
    @abstractmethod
    def get_charged(self):
        pass

# Human implements all relevant interfaces
class Human(Workable, Eatable, Sleepable, Payable):
    def work(self):
        print("Human is working.")

    def eat(self):
        print("Human is eating.")

    def sleep(self):
        print("Human is sleeping.")

    def get_paid(self):
        print("Human got paid.")

# Robot only needs to work
class Robot(Workable, Chargeable):
    def work(self):
        print("Robot is working.")
    def get_charged(self):
        print("Robot is being charged.")

def main():
    workers = [Human(), Robot()]
    for w in workers:
        print(f"\nTesting {w.__class__.__name__}:")
        if isinstance(w, Workable):
            w.work()
        else:
            print(f"{w.__class__.__name__} doesn't work.")

        if isinstance(w, Eatable):
            w.eat()
        else:
            print(f"{w.__class__.__name__} doesn't eat.")

        if isinstance(w, Sleepable):
            w.sleep()
        else:
            print(f"{w.__class__.__name__} doesn't sleep.")

        if isinstance(w, Payable):
            w.get_paid()
        else:
            print(f"{w.__class__.__name__} doesn't get paid.")

        if isinstance(w, Chargeable):
            w.get_charged()
        else:
            print(f"{w.__class__.__name__} doesn't get charged.")
if __name__ == "__main__":
    main()
