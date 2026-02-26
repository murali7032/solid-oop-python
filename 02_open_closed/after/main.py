from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass
    @abstractmethod
    def perimeter(self) -> float:
        pass
    def describe(self):
        return f"{self.__class__.__name__}(area={self.area():.2f}, perimeter={self.perimeter():.2f})"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius

def main():
    shapes = [Rectangle(3, 4), Circle(5)]

    for shape in shapes:
        print(shape.describe())

if __name__ == "__main__":
    main()
