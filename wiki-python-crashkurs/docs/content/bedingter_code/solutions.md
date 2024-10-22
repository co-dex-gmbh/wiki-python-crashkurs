
## Lösungen


### 1. **Einfache if-Abfrage**: 
```python
if x > 10: 
    print("x ist größer als 10.")
```
### 2. **if-else**: 
```python
if zahl % 2 == 0: 
    print("Die Zahl ist gerade.") 
else:   
    print("Die Zahl ist ungerade.")
```
### 3. **Negativ oder Positiv**:
```python
if zahl > 0: 
    print("Positiv") 
elif zahl < 0: 
    print("Negativ") 
else: 
    print("Null")
```
### 4. **Größer oder kleiner**: 
```python
if a > b: 
    print("a ist größer als b") 
elif a < b: 
    print("a ist kleiner als b") 
else: 
    print("a ist gleich b")
```
### 5. **Alter überprüfen**:
```python
if alter >= 18: 
    print("Volljährig") 
else: 
    print("Minderjährig")
```
### 6. **Passwortüberprüfung**:
```python
if eingegebenes_passwort == gespeichertes_passwort: 
    print("Passwort korrekt!") 
else: 
    print("Falsches Passwort!")
```
### 7. **Maximalwert**:
```python
if zahl1 > zahl2: 
    print(zahl1) 
else: 
print(zahl2)
```
### 8. **Bewertung**:
```python
if note >= 1.0 and note < 1.5: 
    print("sehr gut") 
elif note < 2.5: 
    print("gut") 
elif note < 3.5: 
    print("befriedigend") 
elif note < 4.0: 
    print("ausreichend") 
else: 
    print("nicht ausreichend")
```
### 9. **Temperaturen**:
```python
if temperatur < 10: 
    print("Kalt") 
elif temperatur < 25:
    print("Warm") 
else: 
    print("Heiß")
```
### 10. **Einfache Rechnung**:
```python
if operation == '+': 
    print(a + b) 
elif operation == '-': 
    print(a - b) 
elif operation == '*': 
    print(a * b) 
elif operation == '/':
    print(a / b)
```

### 11. **Jahreszeiten**:
```python
if monat in [3, 4, 5]: 
    print("Frühling") 
elif monat in [6, 7, 8]: 
    print("Sommer") 
elif monat in [9, 10, 11]: 
    print("Herbst") 
else: 
    print("Winter")
```
### 12. **Teilbarkeit**:
```python
if zahl1 % zahl2 == 0: 
    print("Teilbar") 
else: 
    print("Nicht teilbar")
```
### 13. **Einkaufsliste**:
```python
if artikel in einkaufsliste: 
    print("Artikel vorhanden") 
else: 
    print("Artikel nicht vorhanden")
```
### 14. **Größte von drei Zahlen**:
```python
if a > b and a > c: 
    print(a) 
elif b > a and b > c: 
    print(b) 
else: 
    print(c)
```
### 15. **Rabattaktion**:
```python
if einkaufswert >= 100: 
    print("Rabatt: 20%") 
elif einkaufswert >= 50: 
    print("Rabatt: 10%") 
else: 
    print("Kein Rabatt")
```
### 16. **Lichtschalter**:
```python
if lichtstatus: 
    print("Licht an") 
else: 
    print("Licht aus")
```
### 17. **Fahrzeugklasse**:
```python
if gewicht < 1000: 
    print("Leicht") 
elif gewicht < 3000: 
    print("Mittel") 
else: 
    print("Schwer")
```
### 18. **Kinotag**:
```python
if wochentag == "Montag": 
    print("Preis: 5 Euro") 
else: 
    print("Preis: 10 Euro")
```

### 19. **Schaltjahr**:
```python
if jahr % 4 == 0 and (jahr % 100 != 0 or jahr % 400 == 0): 
    print("Schaltjahr")
else: 
    print("Kein Schaltjahr")
```