# Vererbung

Die Vererbung ist ein fundamentales Konzept in der objektorientierten Programmierung (OOP),
das die Wiederverwendbarkeit von Code ermöglicht. In Python wird Vererbung durch die Schaffung
von Klassen als Unterklasse einer anderen Klasse realisiert.

## Beispiel 1

{{ youtube_video("https://www.youtube.com/embed/R6udelJEECs?si=w9TCHBiZ6ffc70c5") }}


Wir erzeugen als erstes Beispiel dafür eine Klasse `Rectangle`:

[Link zum Onlinecompiler💻](https://pythontutor.com/render.html#code=class%20Rectangle%3A%0A%20%20%20%20def%20__init__%28self,%20sizeA,%20sizeB%29%3A%0A%20%20%20%20%20%20%20%20self.sizeA%20%3D%20sizeA%0A%20%20%20%20%20%20%20%20self.sizeB%20%3D%20sizeB%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20def%20get_volume%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20self.sizeA%20*%20self.sizeB%0A%0Ar%20%3D%20Rectangle%283,%204%29%0Aprint%28r.get_volume%28%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
class Rectangle:
    def __init__(self, sizeA, sizeB):
        self.sizeA = sizeA
        self.sizeB = sizeB
        
    def get_volume(self):
        return self.sizeA * self.sizeB

r = Rectangle(3, 4)
print(r.get_volume())
```


Nun gibt es aber auch spezielle Rechtecke, wie z.B. Quadrate. Wenn wir diese definieren,
dann wollen wir gerne die Implementierung von `Rectangle` nutzen.
Wir erreichen dies, indem wir eine Klasse `Square` definieren, die von `Rectangle` erbt.
Dies zeigen wir an, indem wir beim Klassenkopf nach dem Klassennamen in runden Klammern notieren,
was die Oberklasse sein soll. Die abgeleitete Klasse `Square` hat zugriff auf alle Attribute und
Funktionen, die in `Rectangle` definiert sind:

[Link zum Onlinecompiler💻](https://pythontutor.com/render.html#code=class%20Rectangle%3A%0A%20%20%20%20def%20__init__%28self,%20sizeA,%20sizeB%29%3A%0A%20%20%20%20%20%20%20%20self.sizeA%20%3D%20sizeA%0A%20%20%20%20%20%20%20%20self.sizeB%20%3D%20sizeB%0A%0A%20%20%20%20def%20get_volume%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20self.sizeA%20*%20self.sizeB%0A%0A%0Aclass%20Square%28Rectangle%29%3A%0A%20%20%20%20def%20__init__%28self,%20size%29%3A%0A%20%20%20%20%20%20%20%20self.sizeA%20%3D%20size%0A%20%20%20%20%20%20%20%20self.sizeB%20%3D%20size%0A%0A%0As%20%3D%20Square%284%29%0Aprint%28s.get_volume%28%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
class Rectangle:
    def __init__(self, sizeA, sizeB):
        self.sizeA = sizeA
        self.sizeB = sizeB

    def get_volume(self):
        return self.sizeA * self.sizeB


class Square(Rectangle):
    def __init__(self, size):
        self.sizeA = size
        self.sizeB = size


s = Square(4)
print(s.get_volume())
```


Wir sehen hier, dass die `Square`-instanz `s` auf die Funktion `get_volume` aus `Rectangle` zugreifen kann.

```mermaid
classDiagram
    Rectangle <| -- Square
    class Rectangle{
        sizeA
        sizeB
        __init__(self, sizeA, sizeB)
        get_volume()
    }
    class Square{
        __init__(self, size)
    }
```

Unser Code erlaubt noch eine Verbesserung. Wir legen im `__init__` von `Square` die Felder `sizeA`
und `sizeB` selbst fest, statt die `__init__` Methode von `Rectangle` auszunutzen. Hier gibt es zwei Varianten,
wie wir vorgehen könnten. Wir könnten `Rectange.__init__(self, size, size)` aufrufen, oder wir nutzen
die `super()` Methode wie folgt:

[Link zum Onlinecompiler💻](https://pythontutor.com/render.html#code=class%20Rectangle%3A%0A%20%20%20%20def%20__init__%28self,%20sizeA,%20sizeB%29%3A%0A%20%20%20%20%20%20%20%20self.sizeA%20%3D%20sizeA%0A%20%20%20%20%20%20%20%20self.sizeB%20%3D%20sizeB%0A%0A%20%20%20%20def%20get_volume%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20self.sizeA%20*%20self.sizeB%0A%0A%0Aclass%20Square%28Rectangle%29%3A%0A%20%20%20%20def%20__init__%28self,%20size%29%3A%0A%20%20%20%20%20%20%20%20super%28%29.__init__%28size,%20size%29%0A%0A%0As%20%3D%20Square%284%29%0Aprint%28s.get_volume%28%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
class Rectangle:
    def __init__(self, sizeA, sizeB):
        self.sizeA = sizeA
        self.sizeB = sizeB

    def get_volume(self):
        return self.sizeA * self.sizeB


class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)


s = Square(4)
print(s.get_volume())
```


{{ task(file="tasks/oop_vererbung_1.yaml") }}

## Beispiel 2

{{ youtube_video("https://www.youtube.com/embed/OlJ2vE6Ri0Y?si=7L7oiKYkfj3QWEEq") }}

Im folgenden Beispiel sehen wir, wie `super()` sowohl dafür verwendet wird, 
wie die `__init__` Methode aufzurufen, als auch die Methdoe `starten`, die in
der Klasse `Elektroauto` überschrieben wird.

[Link zum Onlinecompiler💻](https://pythontutor.com/render.html#code=class%20Auto%3A%0A%20%20%20%20def%20__init__%28self,%20marke,%20modell%29%3A%0A%20%20%20%20%20%20%20%20self.marke%20%3D%20marke%0A%20%20%20%20%20%20%20%20self.modell%20%3D%20modell%0A%0A%20%20%20%20def%20starten%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20f%22%7Bself.marke%7D%20%7Bself.modell%7D%20wird%20gestartet.%22%0A%0Aclass%20Elektroauto%28Auto%29%3A%0A%20%20%20%20def%20__init__%28self,%20marke,%20modell,%20reichweite%29%3A%0A%20%20%20%20%20%20%20%20super%28%29.__init__%28marke,%20modell%29%0A%20%20%20%20%20%20%20%20self.reichweite%20%3D%20reichweite%0A%0A%20%20%20%20def%20starten%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20f%22%7Bsuper%28%29.starten%28%29%7D%20Elektromotor%20wird%20aktiviert.%22%0A%0A%20%20%20%20def%20aufladen%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20f%22%7Bself.marke%7D%20%7Bself.modell%7D%20wird%20aufgeladen.%22%0A%0A%23%20Instanzen%20erstellen%0Amein_auto%20%3D%20Auto%28%22Volkswagen%22,%20%22Golf%22%29%0Amein_elektroauto%20%3D%20Elektroauto%28%22Tesla%22,%20%22Model%20S%22,%20500%29%0A%0A%23%20Methoden%20aufrufen%0Aprint%28mein_auto.starten%28%29%29%20%20%20%20%20%20%20%20%20%20%23%20Ausgabe%3A%20%22Volkswagen%20Golf%20wird%20gestartet.%22%0Aprint%28mein_elektroauto.starten%28%29%29%20%20%20%23%20Ausgabe%3A%20%22Tesla%20Model%20S%20wird%20gestartet.%20Elektromotor%20wird%20aktiviert.%22%0Aprint%28mein_elektroauto.aufladen%28%29%29%20%20%23%20Ausgabe%3A%20%22Tesla%20Model%20S%20wird%20aufgeladen.%22&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
class Auto:
    def __init__(self, marke, modell):
        self.marke = marke
        self.modell = modell

    def starten(self):
        return f"{self.marke} {self.modell} wird gestartet."

class Elektroauto(Auto):
    def __init__(self, marke, modell, reichweite):
        super().__init__(marke, modell)
        self.reichweite = reichweite

    def starten(self):
        return f"{super().starten()} Elektromotor wird aktiviert."

    def aufladen(self):
        return f"{self.marke} {self.modell} wird aufgeladen."

# Instanzen erstellen
mein_auto = Auto("Volkswagen", "Golf")
mein_elektroauto = Elektroauto("Tesla", "Model S", 500)

# Methoden aufrufen
print(mein_auto.starten())          # Ausgabe: "Volkswagen Golf wird gestartet."
print(mein_elektroauto.starten())   # Ausgabe: "Tesla Model S wird gestartet. Elektromotor wird aktiviert."
print(mein_elektroauto.aufladen())  # Ausgabe: "Tesla Model S wird aufgeladen."
```


{{ task(file="tasks/oop_vererbung_2.yaml") }}

{{ task(file="tasks/oop_vererbung_3.yaml") }}

{{ task(file="tasks/oop_vererbung_4.yaml") }}

{{ task(file="tasks/oop_vererbung_5.yaml") }}