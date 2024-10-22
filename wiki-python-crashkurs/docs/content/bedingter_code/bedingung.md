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

## Aufgaben

1. **Einfache if-Abfrage**:
Schreibe ein Programm, das überprüft, ob eine Variable `x` größer als 10 ist. Gib eine 
entsprechende Nachricht aus.
2. **if-else**: 
Überprüfe, ob eine Variable `zahl` gerade ist. Verwende dazu den Modulo-Operator `%`.
3. **Negativ oder Positiv**: 
Schreibe ein Programm, das überprüft, ob eine Zahl positiv, negativ oder 0 ist.
4. **Größer oder kleiner**: 
Überprüfe, ob eine Variable `a` größer, kleiner oder gleich einer anderen Variable `b` ist.
5. **Alter überprüfen**: 
Schreibe ein Programm, das überprüft, ob eine Person anhand ihres Alters volljährig ist.
6. **Passwortüberprüfung**: 
Erstelle ein Programm, das überprüft, ob ein eingegebenes Passwort mit einem gespeicherten 
Passwort übereinstimmt.
7. **Maximalwert**: 
Schreibe ein Programm, das den größeren Wert von zwei Zahlen ausgibt.
8. **Bewertung**: 
Überprüfe anhand einer Variable `note`, ob die Note "sehr gut", "gut", "befriedigend", "ausreichend" 
oder "nicht ausreichend" ist.
9. **Temperaturen**: 
Schreibe ein Programm, das unterschiedliche Meldungen für verschiedene Temperaturbereiche ausgibt 
(z.B. kalt, warm, heiß).
10. **Einfache Rechnung**: 
Schreibe ein Programm, das eine einfache mathematische Operation (Addition, Subtraktion, 
Multiplikation, Division) basierend auf Benutzereingaben ausführt.

11. **Jahreszeiten**: 
Schreibe ein Programm, das den Namen einer Jahreszeit ausgibt, basierend auf einer Monatsnummer (1 bis 12).
12. **Teilbarkeit**: 
Überprüfe, ob eine Zahl durch eine andere Zahl ohne Rest teilbar ist.
13. **Einkaufsliste**: 
Schreibe ein Programm, das überprüft, ob ein Artikel in einer Einkaufsliste vorhanden ist.
14. **Größte von drei Zahlen**: 
Bestimme die größte Zahl aus drei gegebenen Zahlen.
15. **Rabattaktion**: 
Schreibe ein Programm, das basierend auf dem Einkaufswert unterschiedliche Rabatte berechnet.
16. **Lichtschalter**: 
Simuliere einen Lichtschalter, der das Licht ein- und ausschaltet basierend auf der aktuellen 
Zustandsvariable.
17. **Fahrzeugklasse**: 
Schreibe ein Programm, das basierend auf dem Gewicht eines Fahrzeugs eine Kategorie
(Leicht, Mittel, Schwer) zuweist.
18. **Kinotag**: 
Erstelle ein Programm, das unterschiedliche Eintrittspreise basierend auf dem Wochentag berechnet.
19. **Schaltjahr**: 
Schreibe ein Programm, das überprüft, ob ein gegebenes Jahr ein Schaltjahr ist oder nicht.

[Lösungen](solutions.md)