class Shape:
    def __init__(self, name, color, square):
        self.name = name
        self.color = color
        self.square = square
    def info(self):
        return self.name, self.color, self.square
class Triangle(Shape):
    def set_color(self, x):
        self.color = x
    def set_square(self, y):
        self.square = y
class Rectangle(Shape):
    def set_color(self, x):
        self.color = x
    def set_square(self, y):
        self.square = y
a = Triangle('Triangle', 'x', 'y')
b = Rectangle('Rectangle', 'x', 'y')
a.set_color('red')
a.set_square(10)
b.set_color('blue')
b.set_square(8)
print(a.info(), b.info())
