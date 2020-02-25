import math
class Vec:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def minus(self,vec):
        return Vec(self.x - vec.x, self.y - vec.y)
    
    def plus(self,vec):
        return Vec(self.x + vec.x, self.y + vec.y)
    
    @property
    def length(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    @staticmethod
    def distance(point1,point2):
        dx = point2[0] - point1[0]
        dy = point2[1] - point1[1]
        return math.sqrt(dx ** 2 + dy ** 2)
    
