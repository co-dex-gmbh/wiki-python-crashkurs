# Dictionaries (Schlüssel-Wert-Paare):

Dictionaries sind ein Datentyp in Python, mit dem wir Schlüssel-Wert-Paar beschreiben können. 
Sie ermöglichen uns, Werte mithilfe von Schlüsseln zu speichern und abzurufen, ähnlich wie ein echtes Wörterbuch es 
erlaubt, die Bedeutung eines Wortes zu finden. Wir erinnern uns an Listen oder Tupels, bei denen wir auf die Elemente
durch ihre Position in der Sammlung, also deren Index, auf die Elemente zugreifen können. 

```python
mein_dict = {"Name": "Max", "Alter": 25, "Stadt": "Berlin"}
print(mein_dict)
```


## Eigenschaften von Dictionaries


- **Schlüssel und Werte**: Jeder Eintrag in einem Dictionary besteht aus einem Schlüssel und einem zugehörigen Wert.

- **Einzigartige Schlüssel**: Jeder Schlüssel in einem Dictionary muss einzigartig sein. Sollen mehrere Elemente 
    in einem Schlüssel gespeichert werden, kann man natürlich auch eine Liste für diesen Schlüssel speichern.

- **Veränderbar**: Dictionaries sind veränderbar, was bedeutet, dass Einträge hinzugefügt, entfernt oder geändert
   werden können.

- **Ungeordnet**: Die Elemente in einem Dictionary sind nicht in einer bestimmten Reihenfolge gespeichert. Man greift 
    auf die Elemente über deren Schlüssel zu.

- **Dynamisch**: Die Größe eines Dictionaries kann sich während der Laufzeit des Programms ändern.

## Operationen mit Dictionaries

### Erstellen und Initialisieren eines Dictionaries

Es gibt verschiedene Möglichkeiten ein Dictionary anzulegen:

```python
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict([('two', 2), ('one', 1), ('three', 3)])
d = dict({'three': 3, 'one': 1, 'two': 2})
e = dict({'one': 1, 'three': 3}, two=2)

print(a == b == c == d == e)
```


### Zugriff auf Werte

Der Zugriff auf die Werte erfolgt über den entsprechenden Schlüssel in eckigen Klammern. Das sieht ähnlich aus wie bei
Listen, nur dass wir keinen Index verwenden, sondern den entsprechenden Schlüssel.

```python
mein_dict = {"Name": "Max", "Alter": 25, "Stadt": "Berlin"}
print(mein_dict["Name"])
```

Eine weitere Möglichkeit auf die Values eines Dictionaries zuzugreifen besteht in der Methode `get()`.
Das besondere: Wenn der Key nicht existiert, wird `None` zurückgegeben. Das ist in `if`-Bedingungen nützlich,
bei denen ich Code nur durchführen möchte, wenn der Schlüssel auch tatsächlich existiert. Denn `bool(None)` 
ist immer `False`.

```python
my_dict = dict(one=1, two=2, three=3)

v1 = my_dict.get("one")

if v1:
    print(f"Found value: {v1}")
else:
    print("No Value found")

v2 = my_dict.get("four")

if v2:
    print(f"Found value: {v2}")
else:
    print("No Value found")
```


### Hinzufügen und Ändern von Einträgen

Werte können hinzugefügt werden, in dem wir einem Element, einen Schlüssel hinzufügen und diesem einen Wert zuweisen.
Existiert der Schlüssel bereits wird der vorhandene Wert einfach überschrieben.

Als Schlüssel können dabei nur Objekte genutzt werden, die hashable sind (also z.B. Zahlen, Strings, Tupel)

```python
mein_dict = {"Name": "Max", "Alter": 25, "Stadt": "Berlin"}
# Hinzufügen eines neuen Eintrags
mein_dict["Beruf"] = "Ingenieur"

# Ändern eines vorhandenen Eintrags
mein_dict["Alter"] = 26
```


### Entfernen von Einträgen

Das Entfernen von Einträgen sieht leider nicht wie typischer Python-Code aus. Man greift auf das Element, welches man 
löschen will wie gewohnt zu und löscht das Element mit einem vorangestellten `del`.

```python
mein_dict = {"Name": "Max", "Alter": 25, "Stadt": "Berlin"}

del mein_dict["Stadt"]
```



### Durchlaufen eines Dictionaries

Um die Keys **und** Values eines Dictionaries zu durchlaufen, muss die Methode `items()` verwendet werden.
Hier erhalten wir dann zwei Werte in unserer `for`-Schleife auf ein Mal:

```python
mein_dict = {"Name": "Max", "Alter": 25, "Stadt": "Berlin"}

for key, value in mein_dict.items():
    print(key, value)

print("fertig")
```


## Häufige Funktionen und Methoden für Dictionaries in Python

Hier haben wir eine Auswahl einiger Methoden auf Dictionaries.
[Hier ist die gesamte Liste.](https://docs.python.org/3/library/stdtypes.html#dict)

| Funktion        | Beschreibung                                                                                                                     | Beispiel                            |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|
| `my_dict[key]`  | Greif auf den Wert mit dem Key `key` zu. Existiert dieser nicht wird er beim Schreiben erstellt. Beim Lesen gibt es einen Fehler | `dict["Key"] = Value`               |
| `get(key)`      | Gibt den Wert für den angegebenen Schlüssel zurück. Gibt `None` zurück, wenn der Schlüssel nicht existiert.                      | `wert = dict.get('schluessel')`     |
| `keys()`        | Gibt ein neues Ansichtsobjekt zurück, das alle Schlüssel des Dictionaries enthält.                                               | `schluessel = dict.keys()`          |
| `values()`      | Gibt ein neues Ansichtsobjekt zurück, das alle Werte des Dictionaries enthält.                                                   | `werte = dict.values()`             |
| `items()`       | Gibt ein neues Ansichtsobjekt zurück, das alle Schlüssel-Wert-Paare des Dictionaries als Tupel enthält.                          | `paare = dict.items()`              |
| `update(dict2)` | Aktualisiert das Dictionary mit Schlüssel-Wert-Paaren aus einem anderen Dictionary oder iterierbaren Schlüssel-Wert-Paaren.      | `dict.update(dict2)`                |
| `pop(key)`      | Entfernt den Eintrag mit dem angegebenen Schlüssel und gibt dessen Wert zurück.                                                  | `wert = dict.pop('schluessel')`     |
| `popitem()`     | Entfernt und gibt ein zufälliges Schlüssel-Wert-Paar als Tupel zurück.                                                           | `schluessel, wert = dict.popitem()` |
| `clear()`       | Entfernt alle Elemente aus dem Dictionary.                                                                                       | `dict.clear()`                      |
| `copy()`        | Erstellt eine flache Kopie des Dictionaries.                                                                                     | `neues_dict = dict.copy()`          |

## Anwendungsbeispiele

Dictionaries sind nützlich für die Speicherung und Manipulation von Schlüssel-Wert-Paaren und bieten schnellen
Zugriff sowie flexible Datenstrukturen.

- **Datenorganisation**: Dictionaries sind ideal für die Speicherung und Organisation komplexer Daten, wie z.B.
  Benutzerinformationen oder Konfigurationseinstellungen.
- **Schneller Zugriff**: Aufgrund ihrer internen Struktur bieten Dictionaries einen schnellen Zugriff auf ihre Elemente.

# Aufgaben

{{ task(file="tasks/dict_grundlegendes_dictionary.yaml") }}

{{ task(file="tasks/dict_zugriff_auf_werte.yaml") }}

{{ task(file="tasks/dict_hinzufuegen_eines_eintrags.yaml") }}

{{ task(file="tasks/dict_aendern_eines_wertes.yaml") }}

{{ task(file="tasks/dict_entfernen_eines_eintrags.yaml") }}

{{ task(file="tasks/dict_durchlaufen_mit_schleifen.yaml") }}

{{ task(file="tasks/dict_nur_schluessel_durchlaufen.yaml") }}

{{ task(file="tasks/dict_nur_werte_durchlaufen.yaml") }}

{{ task(file="tasks/dict_schluessel_existenz_pruefen.yaml") }}

{{ task(file="tasks/dict_nested_dictionary.yaml") }}

# Anspruchsvolle Aufgaben

{{ task(file="tasks/dict_advanced_wort_zaehler.yaml") }}

{{ task(file="tasks/dict_advanced_telefonbuch.yaml") }}

{{ task(file="tasks/dict_advanced_lagerbestandsverwaltung.yaml") }}

{{ task(file="tasks/dict_advanced_verschachtelt.yaml") }}

{{ task(file="tasks/dict_advanced_buchstaben.yaml") }}