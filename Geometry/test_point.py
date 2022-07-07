import pytest as pt
from pointProperties import Point


@pt.fixture
def point0():
    return Point()


@pt.fixture
def point1():
    return Point(x=3, y=4)


def test_distance(point0, point1):
    assert point0.distance(point1) == 5
    assert point0.distance(point1) != 6


def test_eq(point0, point1):
    assert point0 == point0
    assert not point0 == point1
    point0bis = Point("bis", point0.x, point0.y)
    assert point0 == point0bis
    assert not point0 != point0bis
    assert point0 != point1
    assert not "a" == point0


def test_lt(point0, point1):
    assert point0 < point1
    assert not point1 < point0
    assert point1 > point0
    assert point1 >= point0
    assert point1 >= point1


def test_del(point0):
    with pt.raises(AttributeError) as e:
        del point0.x
    assert "can't delete attribute" in str(e)


def test_addProperty(point0):
    with pt.raises(AttributeError) as e:
        point0.z = 12
    assert "'Point' object has no attribute 'z'" in str(e)


def test_parseInt():
    text = "(12, 155)"
    p = Point.parseInt(text)
    assert p.x == 12
    assert p.y == 155


def test_parseFloat():
    text = "(12.8, -1.55)"
    p = Point.parseFloat(text)
    assert p.x == 12.8
    assert p.y == -1.55

def test_distanceAttributeError(point0):
    with pt.raises(AttributeError) as e:
        point0.distance("a")
    assert "Il n'y a pas x ou y." in str(e)