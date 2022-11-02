import math
e = 10 ** (-3)

class Point:
    def __init__(self, r = None, phi = None):
        
        if r == None or phi == None:
            raise Exception('Required values')
        
        if not (isinstance(r, int | float) and isinstance(phi, int | float)):
            raise Exception('Required values in types: int or float')
        
        self.r = r
        
        if r < e:
            self.phi = 0        
        elif abs(math.fmod(phi, 360)) > 180:
            self.phi = math.fmod(phi, 360) - math.copysign(1, math.fmod(phi, 360)) * 360
        else:
            self.phi = math.fmod(phi, 360)

    
    @classmethod
    def from_cartesian(cls, x, y):
        
        return cls(math.sqrt(x ** 2 + y ** 2), math.atan2(y, x) / math.pi * 180)
    
    
    def __add__(self, other):
        
        p = Point.from_cartesian(self.r * math.cos(self.phi / 180 * math.pi) + other.r * math.cos(other.phi / 180 * math.pi),
                                 self.r * math.sin(self.phi / 180 * math.pi) + other.r * math.sin(other.phi / 180 * math.pi))
        
        return p
    
    
    def __neg__(self):
        
        return Point(self.r, self.phi - 180)
    
    
    def __sub__(self, other):
        
        if not isinstance(other, Point):
            raise Exception('Second point must be from type Point')
        
        return Point.__add__(self, Point.__neg__(other))
    
    
    def __repr__(self) -> str:
        
        return f'Point({round(self.r, 2)}, {round(self.phi, 2)})'
    
    def __eq__(self, other):
        
        if not isinstance(other, Point):
            raise Exception('Second point must be from type Point')
        
        return (abs(self.r - other.r) < e) and (abs(self.phi - other.phi) < e)