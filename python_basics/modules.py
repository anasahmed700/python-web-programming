# modules
from function import square

# classes
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 4)
print(square(p.x))
print(square(p.y))
