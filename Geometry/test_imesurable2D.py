import pytest as pt
from figure import Figure
from pointProperties import Point
from circle import Circle, IMesurable2D


@pt.fixture
def point():
    return Point("p", 2, 3)

@pt.fixture
def circle1(point):
    return Circle("c1", point, 5)
    
@pt.fixture
def circle2(point):
    return Circle("c2", point.translate(1, -1), 1)

@pt.fixture
def figures(point, circle1, circle2, rectangle, polygone5):
    return [point, circle1, circle2, rectangle, polygone5]

def test_allfigures(figures):
    assert all(isinstance(f, Figure) for f in figures)

def test_allMesurable(figures):
    cpt=0
    for f in figures:
        if isinstance(f, IMesurable2D):
            area = f.area()
            perim = f.perimeter()
            cpt+=1
    assert cpt==4

