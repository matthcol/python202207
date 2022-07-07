from turtle import color
from pointProperties import Point

class PointColore(Point):

    def __init__(self, name=None, x=0, y=0, color="#FFFFFF",**kwargs):
        print("PC")
        super().__init__(name=name, x=x, y=y,**kwargs)
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    def __str__(self) -> str:
        return f"Point Colore : {self.color}"
    
