# Was ist eine Bedingung?

{{ youtube_video("https://www.youtube.com/embed/Eq0kgsFAQmY?si=3ffwv8ytB3FKaeii") }}

Eine **Bedingung** ist ein Ausdruck, der schließlich zu einem booleschen Wert `True` oder `False` ausgewertet wird.
Solche Bedingungen können wir leicht verstehen, indem wir sie laut vorlesen.

``` { .python .pytutor_button }
a = int(input("Gebe eine Ganzzahl ein:"))

print("a ist kleiner als 5:")
print(a < 5)

print("a ist größer als 10:")
print(a > 10)

print("a ist größer als 1 und kleiner oder gleich 4:")
print(1 < a <= 4)

print("x in Hallo")
print("x" in "Hallo")

print("a in Hallo")
print("a" in "Hallo")
```

Hier ist eine Liste mit den wichtigsten Operatoren für uns:

| Operator | Name                |
|----------|---------------------|
| `==`     | Gleich              |
| `!=`     | Ungleich            |
| `>`      | (echt) Größer als   |
| `<`      | (echt) Kleiner als  |
| `>=`     | Größer oder gleich  |
| `<=`     | Kleiner oder gleich |
| `in`     | ist enthalten       |

{{ task(file="tasks/bedingungen_voraussagen_1.yaml") }}

{{ task(file="tasks/bedingungen_voraussagen_2.yaml") }}

{{ task(file="tasks/input_korrigieren.yaml") }}

{{ task(file="tasks/verschachtelte_ifs.yaml")}}

