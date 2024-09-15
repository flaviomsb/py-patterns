from math import pi, pow

from shape import Shape


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self):
        return pi * pow(self.radius, 2)

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius: float):
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be an int or float value")
        elif radius < 0:
            raise ValueError("radius must be a positive integer or float")
        else:
            self.__radius = radius
