import collections.abc as abc


def test_list():
    a = []
    assert isinstance(a, abc.Sized)
    assert isinstance(a, abc.Iterable)
    assert not isinstance(a, abc.Iterator)
    assert isinstance(a, abc.Reversible)
    assert isinstance(a, abc.Sequence)


def test_iterator():
    a = [1]
    it = iter(a)
    assert isinstance(it, abc.Iterator)
    assert isinstance(it, abc.Iterable)
    assert hasattr(it, "__next__")
    v = next(it)
    assert v == 1
    assert hasattr(a, "__iter__")
    assert iter(it) is it

def test_generator():
    g = (-i for i in range(0,10))
    assert isinstance(g, abc.Generator)
    assert isinstance(g, abc.Iterable)
    assert isinstance(g, abc.Iterator)
        