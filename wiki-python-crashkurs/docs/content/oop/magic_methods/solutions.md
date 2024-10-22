```python
class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Punkt):
            return Punkt(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Unsupported operand type. Use with another Punkt object.")

    def __eq__(self, other):
        return (isinstance(other, Punkt)
                and self.x == other.x
                and self.y == other.y)

    def __sub__(self, other):
        return Punkt(self.x - other.x, self.y - other.y)

```

```python
from math import isclose

class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Punkt):
            return Punkt(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Unsupported operand type. Use with another Punkt object.")

    def __eq__(self, other):
        return (isinstance(other, Punkt)
                and isclose(self.x, other.x)
                and isclose(self.y, other.y))

    def __sub__(self, other):
        return Punkt(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, int | float):
            return Punkt(self.x * other, self.y * other)
        else:
            raise TypeError("Unsupported operand type. Use int or float")


```