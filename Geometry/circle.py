from imesurable2D import IMesurable2D
from figure import Figure
from pointProperties import Point
from math import pi


class Circle(Figure, IMesurable2D):
    def __init__(self, name=None, center: Point = None, radius=None) -> None:
        super().__init__(name)
        self.center = center
        self.radius = radius

    def translate(self, dx=0, dy=0):
        self.center.translate(dx, dy)

    def perimeter(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * self.radius**2
