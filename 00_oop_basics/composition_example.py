"""
Composition vs inheritance: Car HAS-A Engine, not Car IS-A Engine.
Run: python -m 00_oop_basics.composition_example
"""


class Engine:
    def __init__(self, horsepower: int):
        self.horsepower = horsepower

    def start(self) -> str:
        return f"Engine ({self.horsepower} hp) started."


class Car:
    """Car composes an Engine instead of inheriting from it."""

    def __init__(self, brand: str, engine: Engine):
        self.brand = brand
        self.engine = engine  # composition

    def start(self) -> str:
        return f"{self.brand}: {self.engine.start()}"


def main():
    engine = Engine(150)
    car = Car("Toyota", engine)
    print(car.start())


if __name__ == "__main__":
    main()
