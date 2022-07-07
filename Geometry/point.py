import math
import functools as ft

from figure import Figure

@ft.total_ordering
class Point:
    """Ceci est un point."""
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y
        
    def __repr__(self):
        return f"({self.x}, {self.y})"
        
    def distance(self, autrePoint):
        return math.hypot(self.x-autrePoint.x, self.y-autrePoint.y)
    
    def translate(self, dx=0, dy=0):
        self.x+=dx
        self.y+=dy
        
    def __eq__(self, autrePoint):
        if not isinstance(autrePoint, Point):
            return NotImplemented
        return (self.x, self.y)==(autrePoint.x, autrePoint.y)
    
    def __lt__(self, autrePoint):
        if not isinstance(autrePoint, Point):
            return NotImplemented
        return (self.x, self.y)<(autrePoint.x, autrePoint.y)
        
    def __len__(self):
        return 1