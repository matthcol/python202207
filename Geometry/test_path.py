import pytest as pt
from pathlib import Path
from pointProperties import Point
import pandas as pd

@pt.fixture
def pointPath(pointList):
    p=Path("points.csv")
    df = pd.DataFrame([ {"name":p.name, "x":p.x, "y":p.y} for p in pointList])
    df.to_csv(p)
    yield p
    p.unlink() # suppression sans corbeille

@pt.fixture
def pointList():
    return [Point("a", 1, 2), Point.parseInt("(11,5)"), Point("b", 59, 612)]

def test_import(pointPath):
    df = pd.read_csv(pointPath)
    assert len(df)==3