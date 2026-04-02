class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r
    
    def __str__(self):
        return f"Circle(radius={self.r})"

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w
    
    def __str__(self):
        return f"Rectangle(length={self.l}, width={self.w})"


shapes = [Circle(2), Rectangle(4, 5)]

for s in shapes:
    print(f"{s} = {s.area()}")