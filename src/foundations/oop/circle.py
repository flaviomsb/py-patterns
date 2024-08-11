from math import pi, pow

from shape import Shape


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self):
        return pi * pow(self.radius, 2)
