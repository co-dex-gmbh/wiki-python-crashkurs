### Aufgabe: Wir sind hier bei VW

```python

class Car:
    def __init__(self, speed, marke='VW'):
        self.speed = speed
        self.marke = marke

    def change_speed(self, change):
        self.speed += change


a = Car(50)
print(f"Marke: {a.marke}")

print(f"Geschwindigkeit: {a.speed}")
a.change_speed(100)
print(f"Geschwindigkeit: {a.speed}")
```
