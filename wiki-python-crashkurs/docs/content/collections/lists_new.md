# Listen in Python

Listen in Python sind eine der grundlegendsten und nützlichsten Datentypen. Sie ermöglichen es uns, mehrere Elemente in
einer einzigen Struktur zu speichern, auf die wir dann über ihre Indizes zugreifen können.

Listen können nach ihrer Erstellung verändert werden, das heißt, dass sie *mutabel* sind. 

Listen in Python sind eine der vielseitigsten Datenstrukturen und werden verwendet, 
um eine Sammlung von Elementen zu speichern. Hier sind einige Schlüsseleigenschaften:

## Eigenschaften von Listen


1. **Geordnet**:
    - Listen speichern Elemente in einer festgelegten Reihenfolge.
    - Der Zugriff auf Elemente erfolgt über deren Position oder Index.

2. **Veränderlich (Mutable)**:
    - Die Inhalte einer Liste können nach ihrer Erstellung verändert werden.
    - Elemente können hinzugefügt, entfernt oder geändert werden.

3. **Vielseitig**:
    - Listen können verschiedene Datentypen enthalten, einschließlich Zahlen, Strings und andere Listen.
    - Sie sind nicht auf einen einzelnen Datentyp beschränkt.

4. **Dynamisch**:
    - Listen können in ihrer Größe dynamisch wachsen oder schrumpfen.
    - Sie passen sich automatisch der neuen Größe an, wenn Elemente hinzugefügt oder entfernt werden.

5. **Duplikate erlaubt**:
    - Listen können Duplikate von Elementen enthalten, d.h., ein Element kann mehrmals in einer Liste vorkommen.

## Mutabilität und Immunität

- **Mutability** bedeutet, dass ein Objekt nach seiner Erstellung verändert werden kann, ohne dabei ein anderes Objekt 
  zu werden. Listen sind mutable; daher können wir Elemente hinzufügen, entfernen oder ändern.
- **Immunität** bezieht sich darauf, wenn ein Objekt nach seiner Erstellung nicht verändert werden kann. Ein Beispiel
  für einen immutablen Datentyp in Python ist ein Tupel, welches wir auch bald kennenlernen.

## Listenoperationen

Schauen wir uns kurz ein paar Beispiele an wie man mit Listen arbeiten kann. Das wichtigste zuerst, nämlich die
Erstellung von Listen.

1. Erstellung einer Liste: `meine_liste = [1, 2, 3]`
2. Zugriff auf Listenelemente: `meine_liste[1]` (Zugriff auf Element an Index 1). Indices starten bei 0!
2. Hinzufügen eines Elements: `meine_liste.append(4)` - Fügt `4` am Ende der Liste hinzu.
3. Entfernen eines Elements: `meine_liste.remove(2)` - Entfernt das erste Vorkommen von `2` aus der Liste.

Im Folgenden sehen wir weitere Beispiele.

### Tabelle der häufigsten Listenmethoden

| Methode               | Beschreibung                                                 | Beispiel                                                                   |
|-----------------------|--------------------------------------------------------------|----------------------------------------------------------------------------|
| `append(x)`           | Fügt ein Element am Ende der Liste hinzu                     | `lst.append(5)` - Fügt `5` zu `lst` hinzu                                  |
| `extend([x, y, ...])` | Erweitert die Liste um die Elemente in der angegebenen Liste | `lst.extend([6, 7])` - Fügt `6` und `7` zu `lst` hinzu                     |
| `insert(i, x)`        | Fügt an Position `i` das Element `x` ein                     | `lst.insert(2, 'a')` - Fügt `'a'` an der Position 2 in `lst` ein           |
| `remove(x)`           | Entfernt das erste Vorkommen von `x` aus der Liste           | `lst.remove('a')` - Entfernt das erste Vorkommen von `'a'` aus `lst`       |
| `pop(i)`              | Entfernt und gibt das Element an der Position `i` zurück     | `lst.pop(3)` - Entfernt und gibt das Element an Position 3 in `lst` zurück |
| `clear()`             | Entfernt alle Elemente aus der Liste                         | `lst.clear()` - Entfernt alle Elemente aus `lst`                           |
| `index(x)`            | Gibt den Index des ersten Vorkommens von `x` zurück          | `lst.index('a')` - Gibt den Index von `'a'` in `lst` zurück                |
| `count(x)`            | Zählt, wie oft `x` in der Liste vorkommt                     | `lst.count(5)` - Zählt, wie oft `5` in `lst` vorkommt                      |
| `sort()`              | Sortiert die Elemente der Liste                              | `lst.sort()` - Sortiert die Elemente in `lst`                              |
| `reverse()`           | Kehrt die Reihenfolge der Elemente in der Liste um           | `lst.reverse()` - Kehrt die Reihenfolge der Elemente in `lst`              |

Listen in Python sind vielseitig und ein wesentlicher Bestandteil der meisten Python-Programme. Durch die
Verwendung dieser Methoden können Listen effektiv zur Verarbeitung von Daten in einer Vielzahl von Anwendungen
genutzt werden.

### Beispiel

Stellen wir uns vor, wir haben eine Aufgabe, bei der wir eine Liste von Zahlen verwalten und verschiedene Operationen
darauf durchführen müssen. Wir werden:

1. Eine Liste erstellen
2. Elemente hinzufügen und entfernen
3. Die Liste sortieren
5. Elemente durchsuchen

```python
# 1. Eine Liste erstellen
zahlen = [3, 1, 4, 1, 5, 9, 2]

# 2. Elemente hinzufügen und entfernen
zahlen.append(6)  # Fügt die Zahl 6 am Ende der Liste hinzu
zahlen.insert(2, 7)  # Fügt die Zahl 7 an der Position 2 ein
zahlen.remove(1)  # Entfernt das erste Vorkommen der Zahl 1

# 3. Die Liste sortieren
zahlen.sort()  # Sortiert die Liste in aufsteigender Reihenfolge

# 4. Elemente durchsuchen
position = zahlen.index(5)  # Findet die Position von 5 in der Liste
anzahl_von_4 = zahlen.count(4)  # Zählt, wie oft die Zahl 4 in der Liste vorkommt

# Ergebnisse ausgeben
print("Sortierte Liste:", zahlen)
print("Position von 5:", position)
print("Anzahl von 4:", anzahl_von_4)
```

In diesem Beispiel:

- Beginnen wir mit einer Liste von Zahlen.
- Fügen dann die Zahl 6 hinzu, fügen die Zahl 7 an der zweiten Position ein und entfernen das erste Vorkommen der Zahl 
"1".
- Danach sortieren wir die Liste.
- Und schließlich suchen wir nach spezifischen Elementen (z.B. der Position von 5 und der Anzahl der 4 in der Liste).

### Slicing

Mit sogenannten Slices kann man auch direkt auf mehrere Elemente zugreifen:

```python
fruechte = ["Apfel", "Banane", "Zitrone", "Birne"]
print(fruechte[0:2]) # gibt ('Apfel', 'Banane') aus
```

Slices werden mit 3 Werten angegeben. Dem Startwert, dem nicht-inklusiven Endwert und der Schrittweite:

```python
[inclusive_start_value:exclusive_stop_value:stepsize]
```

Wenn wir also `[2:6:2]` schreiben, sagen wir, dass wir beim dritten Element starten wollen, dann jedes zweite Element 
nehmen und bei fünf (Stopwert ist _exklusiv_) aufhören. Also erhalten wir das dritte und das fünfte Element. 

### Verkettung von Listen

Wir können Listen außerdem sehr einfach miteinander verketten, wie wir am folgenden Code sehen:

```python
liste1 = [1,2,3,4,5]
liste2 = [4,3,2,1]

finale_liste = liste1 + liste2
print(finale_liste) # gibt [1,2,3,4,5,4,3,2,1] aus
```


# Aufgaben

### 1. **Erstellen einer Liste:** 
Erstelle eine Liste mit den Zahlen 1 bis 5.
### 2. **Hinzufügen von Elementen:** 
Füge die Zahl 6 zur Liste `zahlen` hinzu.
### 3. **Entfernen von Elementen:** 
Entferne die Zahl 3 aus der Liste `zahlen`.
### 4. **Zugreifen auf ein Listenelement:** 
Greife auf das dritte Element in der Liste `zahlen` zu.
### 5. **Listenlänge:** 
Finde heraus, wie lang die Liste `zahlen` ist.
### 6. **Slicing:** 
Erstelle eine neue Liste, die die ersten drei Elemente von `zahlen` enthält.
### 7. **Elemente zählen:** 
Zähle, wie oft die Zahl 2 in der Liste `zahlen` vorkommt.
### 8. **Liste umkehren:** 
Kehre die Reihenfolge der Elemente in der Liste `zahlen` um.
### 9. **Liste sortieren:** 
Sortiere die Liste `zahlen` in absteigender Reihenfolge.
### 10. **Listen verschachteln:** 
Erstelle eine neue Liste `verschachtelt`, die zwei Listen enthält: die ursprüngliche
    Liste `zahlen` und eine Liste mit den Buchstaben ['a', 'b', 'c'].

[Lösungen](solutions.md)


