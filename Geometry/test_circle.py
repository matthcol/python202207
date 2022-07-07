import pytest as pt
from circle import Circle, Point
from math import pi

@pt.fixture
def circle():
    return Circle("a", Point(8, 2), 2)

def test_perimeter(circle):
    assert abs(circle.perimeter() - 2*pi*circle.radius) < 0.01

def test_area(circle):
    assert abs(circle.area() - pi*circle.radius**2) < 0.01