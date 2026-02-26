# Phase 3: Liskov Substitution (LSP)
'''
**Goal:** Subclasses must be substitutable for the base class. Callers should not need to know the concrete type.

**Exercise:**
1. **before/** — `Bird` with `fly()`. `Penguin` inherits `Bird` but overrides `fly()` to raise or do nothing → breaks callers that expect "every bird can fly."
2. **after/** — Refactor: e.g. `FlyingBird` and `Bird`, or use composition (e.g. `FlyBehavior`) so `Penguin` doesn’t promise `fly()`.
'''
from abc import ABC, abstractmethod

class Bird(ABC):
    def eat(self):
        print(f"{self.__class__.__name__} is eating.")

class FlyingBird(Bird):
    @abstractmethod
    def fly(self):
        pass

class Sparrow(FlyingBird):
    def fly(self):
        print(f"{self.__class__.__name__} is flying.")

class Penguin(Bird):
    def swim(self):
        print(f"{self.__class__.__name__} is swimming.")

def let_birds_fly(birds):
    for bird in birds:
        if isinstance(bird, FlyingBird):
            bird.fly()
        else:
            print(f"{bird.__class__.__name__} can't fly.")

def main():
    birds = [Sparrow(), Penguin()]
    print("Individual calls:")
    for bird in birds:
        if isinstance(bird, FlyingBird):
            bird.fly()
        else:
            print(f"{bird.__class__.__name__} can't fly.")

    print("\nTesting let_birds_fly with mixed bird types:")
    let_birds_fly(birds)

if __name__ == "__main__":
    main()
