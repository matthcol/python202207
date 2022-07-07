import pytest as pt
from polygone import Polygone, Point


@pt.fixture
def rectangle():
    return Polygone(Point(x=12, y=2), 
                    Point(x=12, y=5), 
                    Point(x=16, y=5), 
                    Point(x=16, y=2), 
                    )

@pt.fixture
def polygone5():
    return Polygone(Point(x=12, y=2), 
                    Point(x=12, y=5), 
                    Point(x=16, y=5), 
                    Point(x=16, y=2), 
                    Point(x=16, y=-1), 
                    )