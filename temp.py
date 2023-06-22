from decimal import Decimal

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x!r}, {self.y})'


print(Vector(Decimal("0"), Decimal("1")))
print(Decimal("1"))