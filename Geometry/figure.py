from abc import abstractclassmethod, ABC, abstractmethod

class Figure(ABC):

    __slots__ = "_name",

    def __init__(self, name=None, **kwargs):
        print("F")
        super().__init__()
        self._name=name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @abstractmethod
    def translate(self, dx=0, dy=0):
        pass
