# Lösungen

### 1. **Grundlegendes Dictionary**
```python
mein_dict = {"Name": "Anna", "Alter": 30, "Beruf": "Ingenieurin"}
print(mein_dict)
```

### 2. **Zugriff auf Werte**
```python
print(mein_dict["Name"])  # Gibt "Anna" aus
```

### 3. **Hinzufügen eines Eintrags**
```python
mein_dict["Stadt"] = "Berlin"
print(mein_dict)
```

### 4. **Ändern eines Wertes**
```python
mein_dict["Alter"] = 31
print(mein_dict)
```

### 5. **Entfernen eines Eintrags**
```python
del mein_dict["Beruf"]
print(mein_dict)
```

### 6. **Durchlaufen mit Schleifen**
```python
for key, value in mein_dict.items():
   print(f"{key}: {value}")
```

### 7. **Nur Schlüssel durchlaufen**
```python
for key in mein_dict.keys():
   print(key)
```

### 8. **Nur Werte durchlaufen**
```python
for value in mein_dict.values():
   print(value)
```

### 9. **Schlüssel-Existenz prüfen**
```python
key = "Name"
if key in mein_dict:
   print(f"{key} ist im Dictionary vorhanden.")
else:
   print(f"{key} ist nicht im Dictionary vorhanden.")
```

### 10. **Nested Dictionary**
```python
mein_nested_dict = {
    "person1": {"Name": "Max", "Alter": 25},
    "person2": {"Name": "Lisa", "Alter": 28}
}
print(mein_nested_dict["person1"]["Name"])  # Gibt "Max" aus
```

# Anspruchsvolle Aufgaben

Hier sind die Lösungen für die vorgeschlagenen komplexen Aufgaben mit Python Dictionaries:

### Lösung zu Aufgabe 1: Wortzähler

```python
text = input("Gib einen Text ein: ")
text = text.lower()
wort_haeufigkeit = {}

for wort in text.split():
    if wort in wort_haeufigkeit:
        wort_haeufigkeit[wort] += 1
    else:
        wort_haeufigkeit[wort] = 1

print(wort_haeufigkeit)
```

### Lösung zu Aufgabe 2: Telefonbuch

```python
telefonbuch = {}

while True:
    aktion = input("Wähle eine Aktion: hinzufügen, suchen, ändern, löschen, beenden: ")

    if aktion == "beenden":
        break
    elif aktion == "hinzufügen":
        name = input("Name: ")
        nummer = input("Telefonnummer: ")
        telefonbuch[name] = nummer
    elif aktion == "suchen":
        name = input("Name: ")
        print(telefonbuch.get(name, "Nicht gefunden"))
    elif aktion == "ändern":
        name = input("Name: ")
        if name in telefonbuch:
            nummer = input("Neue Telefonnummer: ")
            telefonbuch[name] = nummer
        else:
            print("Name nicht im Telefonbuch")
    elif aktion == "löschen":
        name = input("Name: ")
        if name in telefonbuch:
            del telefonbuch[name]
        else:
            print("Name nicht im Telefonbuch")

    print("Aktuelles Telefonbuch:", telefonbuch)
```

### Lösung zu Aufgabe 3: Lagerbestandsverwaltung

```python
lager = {}

while True:
    aktion = input("Aktion wählen: hinzufügen, aktualisieren, löschen, anzeigen, beenden: ")

    if aktion == "beenden":
        break
    elif aktion == "hinzufügen":
        produkt = input("Produktname: ")
        menge = int(input("Menge: "))
        lager[produkt] = lager.get(produkt, 0) + menge
    elif aktion == "aktualisieren":
        produkt = input("Produktname: ")
        if produkt in lager:
            menge = int(input("Neue Menge: "))
            lager[produkt] = menge
        else:
            print("Produkt nicht gefunden")
    elif aktion == "löschen":
        produkt = input("Produktname: ")
        if produkt in lager:
            del lager[produkt]
        else:
            print("Produkt nicht gefunden")
    elif aktion == "anzeigen":
        for produkt, menge in lager.items():
            print(f"{produkt}: {menge}")

    print("Aktueller Lagerbestand:", lager)
```

### Lösung zu Aufgabe 4: Verschachteltes Dictionary analysieren

```python
studenten = {"Anna": {"Mathe": 1, "Englisch": 2}, "Max": {"Mathe": 3, "Englisch": 2}}

for name, faecher in studenten.items():
    durchschnitt = sum(faecher.values()) / len(faecher)
    print(f"{name}: Durchschnittsnote = {durchschnitt:.2f}")
```

### Lösung zu Aufgabe 5. Häufigster Buchstabe in einem String finden:
```python
text = "Mississippi"

# Lege Dictionary an
letters = dict()

# Durchlaufe den text Buchstabenweise.
for letter in text:
    # Überprüfe, ob der Buchstabe schon im Dictionary vorhanden ist. Wenn nein, setze den current_count auf 0.
    current_count = letters.get(letter, 0)
    # Speichere den erhöhten Wert für den Buchstaben
    letters[letter] = current_count + 1

# Ermittle, welche Buchstabe der häufigste ist.    
greatest_number = max(letters.values())

# Wähle alle Buchstaben aus, die am häufigsten auftauchen.
result = []
for letter, count in letters:
    if count == greatest_number:
        result.append(letter)

print(f"Im Text '{text}' sind die häufigsten Buchstaben {result}, die jeweils {greatest_number} mal auftauchen.")
```
