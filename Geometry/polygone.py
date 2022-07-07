from figure import Figure
from pointProperties import Point
from imesurable2D import IMesurable2D
from collections.abc import Iterable
import math


class Polygone(Figure, IMesurable2D, Iterable):
    def __init__(self, *summits:Point, name=None) -> None:
        super().__init__(name)
        self.summits = summits

    def perimeter(self):
        return sum(self.summits[i-1].distance(self.summits[i]) 
            for i in range(0, len(self.summits)))

    @staticmethod
    def heron(a, b, c):
        p = sum((a, b, c))/2
        return math.sqrt(p * (p-a) * (p-b) * (p-c))

    @classmethod
    def aideHeron(cls, p1, p2, p3):
        return cls.heron(p1.distance(p2), p2.distance(p3), p1.distance(p3))

    def area(self):
        return sum(Polygone.aideHeron(self.summits[0], self.summits[i], self.summits[i+1]) 
            for i in range(1, len(self.summits)-1))
    
    def translate(self, dx=0, dy=0):
        for s in self.summits:
            s.translate(dx,dy)
