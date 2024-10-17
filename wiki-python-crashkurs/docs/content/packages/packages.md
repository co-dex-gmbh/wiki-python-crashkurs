# Module und Pakete

In Python ermöglichen Module und Pakete die Organisation von Code in wiederverwendbare Einheiten, um die Lesbarkeit zu verbessern
und die Codeverwaltung zu optimieren.

## Pakete

Packages (deutsch: "Pakete") sind Verzeichnisse, die Module und möglicherweise Unterpakete enthalten.

### Wofür braucht man Pakete?
Set the stage for [PyPi](https://pypi.org/)!

PyPI ist ein Online-Repository für öffentliche Python-Pakete. Entwickler können Pakete veröffentlichen, die jeder installieren und verwenden kann. Für jedes Paket gibt es hier eine Installationsanleitung, eine Beschreibung, Versionshinweise und Informationen zu Abhängigkeiten.

### Zusatz: Erkunde PyPI
Besuche [PyPi](https://pypi.org/) undschau dich um, suche nach einem beliebten Paket, zum Beispiel `requests`.

### Pakete selber packen
Ein Package enthält **immer** eine `__init__.py`. Diese zeigt an,
dass es sich bei dem Ordner um ein Python Package handelt.

```
my_package/
|-- __init__.py
|-- module1.py
|-- module2.py
|-- subpackage/
|   |-- __init__.py
|   |-- module3.py
```



{{ task(file="tasks/packages_1.yaml") }}


### Zusatz: Noch mal auf Englisch 📺

Das folgende Video von [NeuralNine](https://www.youtube.com/watch?v=GxCXiSkm6no) 
fasst die Inhalte dieses Kapitels zusammen und vertieft sie.
Schau dir das Video an und stell mit deinem Tutor sicher, dass du alle Inhalte verstehst.

{{ youtube_video("https://www.youtube.com/embed/GxCXiSkm6no?si=s0zw6JnWV3lWkjSw") }}

Auch [2MinutesPy](https://www.youtube.com/watch?v=mWaMSGwiSB0) hat ein schönes Video zu `__init__.py`:


{{ youtube_video("https://www.youtube.com/embed/mWaMSGwiSB0?si=i-Qa1KO96IDlFLD_") }}

## Was ist Name == Main?

{{ youtube_video("https://www.youtube.com/embed/57b8gJKZf6o?si=sBKUorE0e-MlfRoK") }}


Wenn wir die folgende Datei `greetings.py` ausführen

```python
# greetings.py

def greet(name):
    return f"Hello, {name}!"

greet("Gustav")
```

so erhalten wir auf der Konsole folgenden Output:

```python
"Hello, Gustav"
```

Wenn wir diese Datei jedoch importieren, so wird die Methode `greet("Gustav")` auch ausgeführt:

```python
from greetings.py import greet

greet("Hanna")
```

Konsolenausgabe

```python
"Hello, Gustav"
"Hello, Hanna"
```

Genau hierfür gibt es die Bedingung `if __name__ == "__main__":`. Sie ermöglicht es, Code in einem Modul auszuführen, wenn es direkt ausgeführt wird, aber nicht, wenn es in einem anderen Skript importiert wird. 

Die Variable `__name__` ist eine besondere Variable in Python, die, je nachdem, wie ein Python-Skript verwendet wird, einen unterschiedlichen Wert annehmen kann. Es gibt zwei Hauptkontexte, in denen ein Python-Skript ausgeführt werden kann: entweder als Hauptprogramm oder als Modul, das in ein anderes Skript importiert wird.

1. Wenn das Skript direkt ausgeführt wird, setzt Python die Variable __name__ auf den Wert "__main__".
2. Wird das Skript jedoch importiert und in einem anderen Skript verwendet, wird __name__ auf den Namen des Skripts (genauer gesagt: auf den Namen des Moduls) gesetzt.

Diese Unterscheidung ist besonders nützlich, um zu bestimmen, welcher Code ausgeführt werden soll, je nachdem, ob das Skript direkt gestartet oder als Modul importiert wird

```python
# greetings.py

def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("Gustav"))
```

Führen wir die Datei `greetings.py` aus, erhalten wir weiterhin:
```python
"Hello, Gustav"
```

Wenn wir `greetings.py` aber nun importieren ...
```python
from greetings.py import greet

greet("Hanna")
```

erhalten wir auch die gewünschte Konsolenausgabe:

```python
"Hello, Hanna"
```
