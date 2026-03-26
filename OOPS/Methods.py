class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def Area(self):
        return(self.l * self.b)
    def Parameter(self):
        return 2*(self.l + self.b)
r1=Rectangle(5,8)
print(r1.Area())
print(r1.Parameter())