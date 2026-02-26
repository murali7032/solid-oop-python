"""
OOP basics: inheritance and polymorphism.
Run: python -m 00_oop_basics.shapes
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base: all shapes have area and perimeter."""

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

    def describe(self) -> str:
        return f"{self.__class__.__name__}(area={self.area():.2f}, perimeter={self.perimeter():.2f})"


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height

    def area(self) -> float:
        return self._width * self._height

    def perimeter(self) -> float:
        return 2 * (self._width + self._height)


class Circle(Shape):
    def __init__(self, radius: float):
        self._radius = radius

    def area(self) -> float:
        return math.pi * self._radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self._radius


def main():
    shapes: list[Shape] = [
        Rectangle(3, 4),
        Circle(5),
        Rectangle(1, 1),
    ]
    for s in shapes:
        print(s.describe())  # polymorphism: same call, different behavior


if __name__ == "__main__":
    main()
