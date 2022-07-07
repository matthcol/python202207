from abc import ABC, abstractmethod

class IMesurable2D(ABC):

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass