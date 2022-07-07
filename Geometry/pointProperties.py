import math
import functools as ft

from figure import Figure


@ft.total_ordering
class Point(Figure):
    """Ceci est un point."""

    __slots__ = "_x", "_y"

    def __init__(self, name="Point sans nom", x=0, y=0,**kwargs):
        print("P")
        super().__init__(name=name,**kwargs)
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    # @x.deleter
    # def x(self):
    #     del self._x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def distance(self, autrePoint):
        if not (hasattr(autrePoint, "x") and hasattr(autrePoint, "y")):
            raise AttributeError("Il n'y a pas x ou y.")
        return math.hypot(self.x-autrePoint.x, self.y-autrePoint.y)

    def translate(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    def __eq__(self, autrePoint):
        if not isinstance(autrePoint, Point):
            return NotImplemented
        return (self.x, self.y) == (autrePoint.x, autrePoint.y)

    def __lt__(self, autrePoint):
        if not isinstance(autrePoint, Point):
            return NotImplemented
        return (self.x, self.y) < (autrePoint.x, autrePoint.y)

    def __len__(self):
        return 1

    @staticmethod
    def parseInt(string: str):
        x, y = string[1:-1].split(",")
        return Point(x=int(x), y=int(y))

    @classmethod
    def parseFloat(cls, string: str):
        x, y = string[1:-1].split(",")
        # a = cls.parseInt("(1,2+")
        return Point(x=float(x), y=float(y))
