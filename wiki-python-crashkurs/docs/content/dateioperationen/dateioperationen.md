# Dateioperationen

## Dateien manuell öffnen und schließen

[Lade die Datei `beispiel.txt` herunter🔽](beispiel.txt) und lese sie mit folgendem Code aus:

```python
datei = open("beispiel.txt")
inhalt = datei.read()
print(inhalt)
datei.close()
```

`open` öffnet die Datei, `read` liest sie aus und `close` schließt sie wieder.

Beim Arbeiten mit Dateien ohne `with open` musst du darauf achten,
die Datei manuell zu öffnen und zu schließen. Das kann zu Problemen führen, wenn ein Fehler auftritt,
bevor die Datei geschlossen wird. Daher wird dieser Weg nicht empfohlen, sondern man sollte immer
mit `with` arbeiten.

{{ task(file='tasks/dateinoperationen_1.yaml') }}

{{ task(file='tasks/dateinoperationen_2.yaml') }}


## Dateien mit `with open` nutzen

Um sicherzustellen, dass Dateien immer geschlossen werden (auch bei Fehlern),
sollten Dateien mit `with open` geöffnet und gelesen werden:

```python
with open("beispiel.txt") as datei:
    inhalt = datei.read()

print(inhalt)
```

Die `with open`-Anweisung ist eine sicherere Methode, um mit Dateien umzugehen.
Sie stellt sicher, dass die Datei ordnungsgemäß geschlossen wird, selbst wenn ein Fehler auftritt.

{{ task(file='tasks/dateinoperationen_3.yaml') }}

{{ task(file='tasks/dateinoperationen_4.yaml') }}

## Zugriffsmodi

Es gibt verschiedene Zugriffsmodi auf Dateien, die mit dem zweiten Parameter von `open` ausgewählt werden.

[Link zur Dokumentation von open](https://docs.python.org/3/library/functions.html#open)

| Modus | Beschreibung                    |
|-------|---------------------------------|
| `"r"` | Lesen (default)                 |
| `"w"` | Schreiben                       |
| `"x"` | Exklusives Schreiben            |
| `"a"` | Anhängen                        |
| `"b"` | Binärmodus                      |
| `"t"` | Textmodus (default)             |
| `"+"` | Aktualisieren (Lesen/Schreiben) |

Es können auch mehrere dieser Modi auf ein mal gewählt werden, indem man diese in einem String zusammenstellt.
Z.B. erlaubt `"rw"` das Lesen und Schreiben der Datei.

{{ task(file='tasks/dateinoperationen_5.yaml') }}

## In Dateien schreiben

Mit dem folgenden Code wird in eine Datei geschrieben

```python
with open("save_file", "w") as datei:
    datei.write("Hallo")
```

Beachte, dass die Datei automatisch erstellt wird, wenn sie nicht existiert. Das ist doch nett 😉

{{ task(file='tasks/dateinoperationen_6.yaml') }}

{{ task(file='tasks/dateinoperationen_7.yaml') }}
## Mehrere Dateien öffnen

Wir können natürlich auch den Inhalt der einen Datei in die andere Schreiben und
ggf. auf dem Weg manipulieren. Hier werden alle `"e"` durch `"*"` ersetzt:

```python
with open("beispiel.txt", "rt") as org, open("censored_text.txt", "wt") as censored:
    text = org.read()
    censored.write(text.replace("e", "*"))
```

{{ task(file='tasks/dateinoperationen_8.yaml') }}

{{ task(file='tasks/dateinoperationen_9.yaml') }}

## CSV-Dateien

CSV-Dateien dienen dazu tabulare Daten zu speichern.
In diesen werden Zeilen einer Tabelle gespeichert. Meist sind
Zeilen mit einem Absatz getrennt und Einträge in einer Zeile mit einem `,`.

Fülle eine Exceltabelle mit Inhalt und speichere dann die
Datei als `.csv`. Öffne die Datei dann mit einem Texteditor,
um die Struktur einer CSV zu sehen.

Das `csv`-Modul ermöglicht das Lesen von CSV-Dateien.
Mit der `csv.reader`-Funktion kannst du die Zeilen der CSV-Datei durchgehen.
Der folgende Code zeigt, wie man die CSV-Datei
[persons.csv🔽](persons.csv) öffnen und lesen kann:

```python
import csv

with open("persons.csv", "r") as csv_datei:
    csv_reader = csv.reader(csv_datei)
    for zeile in csv_reader:
        print(zeile)
```

Wenn du Daten in eine CSV-Datei schreiben möchtest,
kannst du auch die `csv`-Bibliothek ebenfalls verwenden.
Hier ist ein Beispiel:

```python
import csv

# Daten, die in die CSV-Datei geschrieben werden sollen
daten = [
    ["Name", "Alter", "Stadt"],
    ["Max", 25, "Berlin"],
    ["Anna", 30, "München"],
    ["Tom", 22, "Hamburg"]
]

# Öffne die CSV-Datei im Schreib-Modus
with open("ausgabe.csv", "w", newline="") as csv_datei:
    # Erstelle einen CSV-Writer
    csv_writer = csv.writer(csv_datei)

    # Schreibe die Daten in die CSV-Datei
    for zeile in daten:
        csv_writer.writerow(zeile)

```

{{ task(file='tasks/dateinoperationen_10.yaml') }}

{{ task(file='tasks/dateinoperationen_11.yaml') }}
