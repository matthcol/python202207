from pointProperties import Point

class WeightedPoint(Point):

    def __init__(self, name=None, x=0, y=0, weight=1,**kwargs):
        print("WP")
        super().__init__(name=name, x=x, y=y,**kwargs)
        self._weight = weight

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value

    def __str__(self) -> str:
        return f"Point pondere : {self.weight}"
    
