# Module und Pakete

In Python ermöglichen Module und Pakete die Organisation von Code in wiederverwendbare Einheiten, um die Lesbarkeit zu verbessern
und die Codeverwaltung zu optimieren.

## Module

{{ youtube_video("https://www.youtube.com/embed/NNJgJ7-EW10?si=vgr49JBc_nwKAQDh") }}


Ein Modul in Python ist im Grunde genommen eine `.py`-Datei mit Python-Code.
In dieser Datei können Funktionen, Variablen und Klassen definiert werden,
die in anderen Python-Dateien wiederverwendet werden können. Es gibt

Angenommen, du erstellst eine Datei/Modul namens `greetings.py`:

```python
# greetings.py

def greet(name):
    return f"Hello, {name}!"
```

Und im selben Ordner eine andere Datei namens `main.py`.
Wir können das Modul `greetings.py` und die darin enthaltene Methode nun wie folgt
verwenden:

```python
# main.py

import greetings

print(greetings.greet("Alice"))
```

Du kannst auch Alias für Module verwenden, um den Code kompakter zu gestalten:

```python
# main.py

import greetings as gr

print(gr.greet("Bob"))
```

Wir können auch nur die einzelne Funktion zu importieren

```python
# main.py

from greetings import greet

print(greet("Bob"))
```

Oder alle Funktionen, die es in einem Modul gibt:

```python
# main.py

from greetings import *

print(greet("Bob"))
```

Es ist jedoch ratsam, selektiv zu importieren, um potenzielle Namenskonflikte zu vermeiden.

{{ task(file="tasks/module_1.yaml") }}

{{ task(file="tasks/module_2.yaml") }}

{{ task(file="tasks/module_3.yaml") }}

{{ task(file="tasks/module_4.yaml") }}