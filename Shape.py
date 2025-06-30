class Shape:
    def __init__(self,l):
        self.l=l
    def getArea(self):
        pass

class Square(Shape):
    def getArea(self):
        return self.l *self.l

s1=Square(8)
print(s1.getArea())