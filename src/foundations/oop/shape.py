from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def __eq__(self, other) -> bool:
        return self.area() == other.area()

    def __gt__(self, other) -> bool:
        return self.area() > other.area()

    def __repr__(self) -> str:
        return "{0} w/ area {1}".format(self.__class__.__name__, self.area())
