import pytest as pt

from polygone import Polygone, Point

def test_perimeter(rectangle, polygone5):
    assert rectangle.perimeter() == 14
    assert polygone5.perimeter() == 18

def test_area(rectangle, polygone5):
    assert rectangle.area() == 12
    assert polygone5.area() == 18



