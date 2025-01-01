class Vector2:
    x=0
    y=0
    pass


class Vector2:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other: Vector2):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector2):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int):
        return Vector2(self.x * other, self.y)

    def __truediv__(self, other: int):
        return Vector2(self.x / other, self.y / other)

    def module(self):
        return (self.x^2+self.y^2)**0.5
