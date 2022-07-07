from pointcolore import PointColore, Point
from weightedpoint import WeightedPoint

class WeightedPointColore(PointColore, WeightedPoint):

    def __init__(self, name=None, x=0, y=0, weight=1, color="#FFFFFF",**kwargs):
        # WeightedPoint.__init__(self, weight=weight)
        # PointColore.__init__(self, name=name, x=x, y=y, color=color)
        print("WPC")
        super().__init__(name=name, x=x, y=y, weight=weight, color=color, **kwargs)

    def __str__(self) -> str:
        return f"""N : {self.name}
X : {self.x}
Y : {self.y}
W : {self.weight}
C : {self.color}"""
    
if __name__=="__main__":
    print(WeightedPointColore.__mro__)
    a = WeightedPointColore("WPC", 1.1, 2.2, 5.5, "Green")
    print(a)
    
        
