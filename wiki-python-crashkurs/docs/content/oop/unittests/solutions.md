### Aufgabe: Den Wald vor lauter Bäumen

```python
# suchbaum.py

class Suchbaum:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add(self, new_value):
        if new_value < self.value:
            if self.left is None:
                self.left = Suchbaum(new_value)
            else:
                self.left.add(new_value)
        else:
            if self.right is None:
                self.right = Suchbaum(new_value)
            else:
                self.right.add(new_value)

    def contains(self, value_to_find):
        if self.value == value_to_find:
            return True

        if self.left is not None and value_to_find < self.value:
            return self.left.contains(value_to_find)

        if self.right is not None and self.value < value_to_find:
            return self.right.contains(value_to_find)

        return False

```

