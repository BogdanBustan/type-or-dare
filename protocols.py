from typing import Protocol, List
from abc import ABC, abstractmethod


# Define a Protocol
class Drawable(Protocol):
    def draw(self) -> None:
        ...


# Classes implementing the Drawable protocol
class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def draw(self) -> None:
        print(f"Drawing a circle with radius {self.radius}")


class Square:
    def __init__(self, side_length: float):
        self.side_length = side_length

    def draw(self) -> None:
        print(f"Drawing a square with side length {self.side_length}")


# A class that doesn't explicitly implement the protocol
class Triangle:
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def draw(self) -> None:
        print(f"Drawing a triangle with base {self.base} and height {self.height}")


# Function that uses the Drawable protocol
def draw_shapes(shapes: List[Drawable]) -> None:
    for shape in shapes:
        shape.draw()


# Usage
circle = Circle(5.0)
square = Square(4.0)
triangle = Triangle(3.0, 4.0)

shapes: List[Drawable] = [circle, square, triangle]
draw_shapes(shapes)


# For comparison, here's how you might do this with an abstract base class
class DrawableABC(ABC):
    @abstractmethod
    def draw(self) -> None:
        pass


class CircleABC(DrawableABC):
    def __init__(self, radius: float):
        self.radius = radius

    def draw(self) -> None:
        print(f"Drawing a circle with radius {self.radius}")


# Usage with ABC
circle_abc = CircleABC(5.0)
draw_shapes([circle_abc])  # This works too!
