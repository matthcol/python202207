
from figure import Figure
import pytest as pt

def test_figureNonInstanciable():
    with pt.raises(TypeError) as e:
        Figure()
    assert "Can't instantiate abstract class Figure" in str(e)