from pytest import fixture
from pointcolore import PointColore, Point
import pytest as pt

@pt.fixture
def rouge():
    return PointColore("rouge", 1, 3, "#FF0000")
    
@pt.fixture
def rougeSansCouleur(rouge):
    return Point("rouge", rouge.x, rouge.y)

@pt.fixture
def pointPasColore():
    return Point("pc", 4, 7)

def test_pointcoloreConstructor(rouge):
    a = rouge
    assert a.x == 1
    assert a.y == 3
    assert a.color == "#FF0000"

def test_pointcoloreTranslate(rouge):
    rouge.translate(2, -8)
    assert rouge.x == 3
    assert rouge.y == -5

def test_distanceHeritage(rouge, pointPasColore):
    dist = rouge.distance(pointPasColore)
    assert dist == 5

def test_distanceSubstitution(rouge, pointPasColore):
    dist = pointPasColore.distance(rouge)
    assert dist == 5
    
def test_EqHeterogene(rouge, rougeSansCouleur):
    assert rougeSansCouleur == rouge
    assert rouge == rougeSansCouleur

def test_isintance(rouge, rougeSansCouleur):
    assert isinstance(rouge, PointColore)
    assert isinstance(rouge, Point)
    assert isinstance(rouge, object)
    assert not isinstance(rougeSansCouleur, PointColore)