### Aufgabe: Typen erkennen🌶

| Eingabe                    | Ausgabe                                                                       |
|----------------------------|-------------------------------------------------------------------------------|
| `type(s)`                  | `<class '__main__.Square'>`                                                   |
| `type(s).__mro__`          | `(<class '__main__.Square'>, <class '__main__.Rectangle'>, <class 'object'>)` |
| `Square.__mro__`           | `(<class '__main__.Square'>, <class '__main__.Rectangle'>, <class 'object'>)` |
| `isinstance(s, Square)`    | `True`                                                                        |
| `isinstance(s, Rectangle)` | `True`                                                                        |

Es werden bei `__mro__` also alle Obertypen aufgelistet.

print(type(s)) # <class '__main__.Square'>
print(type(s).__mro__) # <class '__main__.Square'>, <class '__main__.Rectangle'>, <class 'object'>)
print(Square.__mro__) # <class '__main__.Square'>, <class '__main__.Rectangle'>, <class 'object'>)
print(isinstance(s, Square)) # True
print(isinstance(s, Rectangle)) # True

### Aufgabe: Geometry

```python
from math import isclose


class Form:
    def umfang(self):
        raise NotImplementedError("Kann nicht für diese Allgemeine Form bestimmt werden")

    def inhalt(self):
        raise NotImplementedError("Kann nicht für diese Allgemeine Form bestimmt werden")


class Dreieck(Form):
    def __init__(self, size_a, size_b, size_c):
        self.size_a = size_a
        self.size_b = size_b
        self.size_c = size_c

    def umfang(self):
        return self.size_a + self.size_b + self.size_c

    def inhalt(self):
        s = self.umfang() / 2
        result = (s * (s - self.size_a) * (s - self.size_b) * (s - self.size_c)) ** 0.5
        return result

    def hat_90_grad_winkel(self):
        squared_sizes = [s ** 2 for s in (self.size_a, self.size_b, self.size_c)]
        squared_sizes.sort()
        return isclose(squared_sizes[0] + squared_sizes[1], squared_sizes[2])


class Kreis(Form):
    PI = 3.14159265358979323846

    def __init__(self, radius):
        self.radius = radius

    def umfang(self):
        return 2 * self.PI * self.radius

    def inhalt(self):
        return self.PI * self.radius ** 2


class Viereck(Form):
    def __init__(self, size_a, size_b, size_c, size_d):
        self.size_a = size_a
        self.size_b = size_b
        self.size_c = size_c
        self.size_d = size_d

    def umfang(self):
        return self.size_a + self.size_b + self.size_c + self.size_d


class Parallelogramm(Viereck):
    def __init__(self, size_a, size_b):
        super().__init__(size_a, size_b, size_a, size_b)

    def inhalt(self):
        return self.size_a * self.size_b

```