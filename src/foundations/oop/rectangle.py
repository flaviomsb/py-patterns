from shape import Shape


class Rectangle(Shape):
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
