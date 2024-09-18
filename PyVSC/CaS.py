class Shape:
    def draw(self):
        pass
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def draw(self):
        print("Drawing a circle")
    def area(self):
        S = 3,14 * self.r * 2
        return S
    def __mul__(self, other):
        self.S = 3,14 * self.r * 2
        self.S * other.S

class Square(Shape):
    def __init__(self, a):
        self.a = a
    
    def draw(self):
        print("Drawing a square")
    
    def area(self):
        S = self.a ** 2
        return S
    
    def __mul__(self, other):
        self.S = self.a ** 2
        self.S * other.S

shapes = [Circle(20.0), Square(6.0)]
c1 = Circle(20.0)
s1 = Square(6.0)
print(c1 * s1)
for shape in shapes:
    shape.draw()