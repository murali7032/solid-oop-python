# Phase 3: Liskov Substitution (LSP)
'''
**Goal:** Subclasses must be substitutable for the base class. Callers should not need to know the concrete type.

**Exercise:**
1. **before/** — `Bird` with `fly()`. `Penguin` inherits `Bird` but overrides `fly()` to raise or do nothing → breaks callers that expect "every bird can fly."
'''
class Bird:
    def fly(self):
        print(f"{self.__class__.__name__} is flying.")

class Sparrow(Bird):
    pass

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins can't fly!")

def let_birds_fly(birds):
    for bird in birds:
        bird.fly()

def main():
    birds = [Sparrow(), Penguin()]
    for bird in birds:
        try:
            bird.fly()
        except Exception as e:
            print(f"Error: {e}")

    print("\nTesting let_birds_fly with mixed bird types:")
    try:
        let_birds_fly(birds)
    except Exception as e:
        print(f"let_birds_fly error: {e}")

if __name__ == "__main__":
    main()
