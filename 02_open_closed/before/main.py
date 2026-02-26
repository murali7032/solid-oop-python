'''
# Phase 2: Open/Closed (OCP)

**Goal:** Add new behavior by adding new code (e.g. new classes), not by editing existing code.

**Exercise:**
1. **before/** — Write a function `total_area(shapes)` that uses `if type(s) == Rectangle: ... elif type(s) == Circle: ...`. Adding a new shape forces you to edit this function.
'''
import math

class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

def total_area(shapes):
    total = 0
    for s in shapes:
        if type(s) == Rectangle:
            total += s.width * s.height
        elif type(s) == Circle:
            total += math.pi * s.radius ** 2
        # If you want to add a new shape, you must edit this function!
    return total

def main():
    shapes = [
        Rectangle(3, 4),
        Circle(1),
        Rectangle(5, 2)
    ]
    print("Total area:", total_area(shapes))

if __name__ == "__main__":
    main()
