# Lösungen

# for-Schleifen

Natürlich, hier sind die Lösungen zu den Übungsaufgaben zu `for`-Schleifen:

### 1. Zählen
```python
for zahl in [1,2,3,4,5,6,7,8,9,10]:
   print(zahl)
```

### 2. Städtetrip
```python
staedte = ["Berlin", "Paris", "London", "New York"]
for stadt in staedte:
   print(stadt)
```

### 3. Summierung
```python
summe = 0
for zahl in [1,2,3,4,5,6,7,8,9,10]:
   summe += zahl
print(summe)
```

### 4. Längster Name
```python
namen = ["Anna", "Max", "Benjamin", "Alexandra"]
laengster_name = ""
for name in namen:
   if len(name) > len(laengster_name):
       laengster_name = name
print("Längster Name:", laengster_name)
```

### 5. Quadratzahlen
```python
for zahl in range(1, 11):
   quadrat = zahl ** 2
   print(quadrat)
```

### 6. Verdreht
```python
wort = "Python"
for buchstabe in wort[::-1]:
   print(buchstabe)
```

### 7. Fakultät
```python
n = 5
faktor = 1
for zahl in range(1, n + 1):
    faktor *= zahl
print(f"Fakultät von {n} ist {faktor}")
```

### 8. Thermometer für Amerikaner 
```python
temperaturen_celsius = [0, 10, 25, 32, 100]
for celsius in temperaturen_celsius:
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C entspricht {fahrenheit}°F")
```

### 9. Vokale
```python
wort = "Python"
anzahl_vokale = 0
for buchstabe in wort:
    if buchstabe.lower() in "aeiou":
        anzahl_vokale += 1
print(f"Anzahl der Vokale im Wort '{wort}': {anzahl_vokale}")
```

### 10. Häufigkeit
```python
text = "Python ist eine Programmiersprache, und Python ist großartig."
gesuchtes_wort = "Python"
anzahl = 0
woerter = text.split()
for wort in woerter:
    if wort == gesuchtes_wort:
        anzahl += 1
print(f"Anzahl von '{gesuchtes_wort}' im Text: {anzahl}")
```

# Aufgaben Ranges

### Aufgabe: Ranges vorhersagen

```python
list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(1, 11)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(range(0, 30, 5)) # [0, 5, 10, 15, 20, 25]
list(range(0, 10, 3)) # [0, 3, 6, 9]
list(range(0, -10, -1)) # [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
list(range(0)) # []
list(range(1, 0)) # []
```


# while-Schleifen


### 1. Summe von 1 bis 100

```python
summe = 0
i = 1
while i <= 100:
    summe += i
    i += 1
print(f"Die Summe von 1 bis {i} ist {summe}")
```

### 2. Input erfragen

```python
summe = 0
while True:
    next = input("Bitte gib eine Zahl ein: ")
    summe += next
    print(f"In der Summe bisher insgesamt: {summe}")
```

### 3. Fakultät

```python
at_least = 100_000
fakultaet = 1
i = 1
while fakultaet <= at_least:
    fakultaet *= i
    i += 1
    
print(f"Das kleinste n, sodass n! > {at_least} ist {i} und zwar {i}! = {fakultaet}")
```

### 4. Fast endlose Schleife

```python
import random

zahl = 0
while zahl != 5:
    zahl = random.randint(1, 10)
    print(zahl)
print("Das wars!")
```

### 5. Fibonacci

```python
f_1 = 1
f_2 = 1
at_least = 100

while f_2 < at_least:
    # Berechne die nächste Fibonaccizahl
    f_3 = f_1 + f_2

    # Setze die aktuelle und letzte Fibonaccizahl fest.
    f_1 = f_2
    f_2 = f_3

print(f"Die Zahl {f_3} ist die erste Fibonaccizahl, die größer als  {at_least}")
```
# Verschachtelte Schleifen

### Aufgabe: Produktsummen

```python
result = 1
for sub_list in [[4,3,2], [5,6,7]]:
    subsum = 0
    for element in sub_list:
        subsum += element
    result *= subsum
print(result)
```

$$1 ⋅ (4+3+2) ⋅ (5+6+7) = 1 ⋅ 9 ⋅ 18 = 162$$ 

### Aufgabe: Summenprodukt

```python
super_list = [[1,2,3], [-3, 4, 6, 9, 3], [0], [4,4], []]
result = 0
for sub_list in super_list:
    subprodukt = 1
    for element in sub_list:
        subprodukt *= element
    if len(sub_list) == 0: # Wenn keine Elemente in der Liste sind, soll 0 als Summand genutzt werden, nicht 1.
        subprodukt = 0
    result += subprodukt
print(result)
```

$$0 + (1⋅1⋅2⋅3) + (1⋅(-3)⋅4⋅6⋅9⋅3) + (1⋅0)+ (1⋅4⋅4) + 0 = 0 + 6 + 648 + 0 + 8 + 0 = 662$$

# Anspruchsvolle Aufgaben

### Aufgabe 1: Finden

```python
text = "Schreibe ien Programm, das in einem Text das erste Wort findet, länger als 8 Buchstaben ist und dieses zurückgibt."
for word in text.split():
    if len(word) > 8:
        break
else:
    word = ""
print(f"Erstes Wort mit mehr als 8 Buchstaben: {word}")
```

Code ohne  `continue`
```python
text = "Schreibe ien Programm, das in einem Text das erste Wort findet, länger als 8 Buchstaben ist und dieses zurückgibt."
first_word = ""
for word in text.split():
    if not first_word and len(word) > 8:
        first_word = word

print(f"Erstes Wort mit mehr als 8 Buchstaben: {first_word}")
```

### Aufgabe 2: Benutzerdefinierte Passwortüberprüfung

```python

password = input("Bitte gib ein Passwort ein: ")

# Prüfe, ob String lang genug ist
min_length_ok = len(password) >= 8

# Prüfe, ob wenigstens eine Zahl enthalten ist
digit_found = False
for char in password:
    if char.isdigit():
        digit_found = True
        break

# Prüfe, ob wenigstens ein Buchstabe enthalten ist
char_found = False
for char in password:
    if char.isalpha():
        char_found = True
        break
        
if min_length_ok and digit_found and char_found:
    print("Password ok💚")
else:
    print("Password not ok😰")

if not min_length_ok:
    print("Es ist zu kurz.")
if not digit_found:
    print("Es fehlt mindestens eine Ziffer.")
if not char_found:
    print("Es fehlt mindestens ein Buchstabe.")
```

### Aufgabe 3: Einfacher Zahlenraten

```python
import random

zahl = random.randint(1, 100)

versuch = 1
max_versuche = 10

while versuch < max_versuche:
    raten = int(input("Rate die Zahl: "))

    if raten == zahl:
        print(f"Richtig! Du hast die Zahl in {versuch} Versuchen erraten.")
        break
    elif raten < zahl:
        print("Die gesuchte Zahl ist höher.")
    else:
        print("Die gesuchte Zahl ist niedriger.")
        
    versuch += 1
else:
    print(f"Leider falsch. Die gesuchte Zahl war {zahl}.")
```

### Aufgabe 4: Bestellung in einem virtuellen Café

```python
menu = {"Kaffee": 2.50, "Tee": 2.00, "Kuchen": 3.00}
bestellung = []
summe = 0

print("Menü:")
for artikel, preis in menu.items():
    print(f"{artikel}: {preis} Euro")

while True:
    artikel = input("Wähle einen Artikel (oder 'fertig' zum Abschließen): ")
    if artikel.lower() == "fertig":
        break
    elif artikel in menu:
        menge = int(input(f"Wie viele von {artikel} möchtest du? "))
        summe += menu[artikel] * menge
    else:
        print("Artikel nicht im Menü.")

print(f"Gesamtsumme: {summe} Euro")
zahlung = input("Zahlst du bar oder mit Karte? ")
print(f"Bezahlt mit {zahlung}. Vielen Dank für deine Bestellung!")
```
