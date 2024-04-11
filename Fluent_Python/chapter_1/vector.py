from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        # можно было обойтись без библиотеки math
        # return (self.x ** 2 + self.y ** 2) ** 0.5
        return hypot(self.x, self.y)

    def __bool__(self):
        # более быстрая реализация
        # def __bool__(self):
        #    return bool(self.x or self.y)
        
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)