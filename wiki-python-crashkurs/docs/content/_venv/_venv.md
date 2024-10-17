# Virtuelle Umgebungen in Pyton

In Python können virtuelle Umgebungen erstellt werden, um die Abhängigkeiten von Projekten zu verwalten. Dies ist besonders nützlich, wenn mehrere Projekte unterschiedliche Versionen von Bibliotheken benötigen. In diesem Kapitel wird gezeigt, wie virtuelle Umgebungen in Python erstellt und verwendet werden.

## Wie funktioniert eine virtuelle Umgebung?

Eine virtuelle Umgebung ist ein Verzeichnis, das alle notwendigen Dateien enthält, um eine isolierte Umgebung für ein Python-Projekt zu erstellen. Dies bedeutet, dass jede virtuelle Umgebung ihre eigene Kopie von Python und Bibliotheken enthält. Wenn eine virtuelle Umgebung aktiviert ist, werden alle Python-Befehle auf die Kopie von Python und die Bibliotheken in der virtuellen Umgebung umgeleitet.

## Erstellen einer virtuellen Umgebung

Eine virtuelle Umgebung kann mit dem Modul `venv` erstellt werden. Das Modul `venv` ist in Python 3.3 und höher standardmäßig enthalten. Um eine virtuelle Umgebung zu erstellen, führen Sie den folgenden Befehl aus:

```bash
python -m venv <name>
```

Der Befehl erstellt ein Verzeichnis mit dem Namen `<name>`, das die virtuelle Umgebung enthält. Der Name kann frei gewählt werden. Um die virtuelle Umgebung zu aktivieren, führen Sie unter Windows den folgenden Befehl aus:

```bash
<name>\Scripts\activate
```

!!! warning "Achtung"
    Unter Linux und macOS lautet der Befehl `source <name>/bin/activate`.

!!! note "Hinweis"
    In VS Code kann die virtuelle Umgebung über das Dropdown-Menü in der unteren rechten Ecke ausgewählt werden. Oftmals wird die virtuelle Umgebung automatisch erkannt.


Um die virtuelle Umgebung zu deaktivieren, führen Sie den folgenden Befehl aus:

```bash
deactivate
```

## Installieren von Bibliotheken

Nachdem die virtuelle Umgebung aktiviert ist, können Bibliotheken mit dem Befehl `pip install` installiert werden. Die Bibliotheken werden in der virtuellen Umgebung installiert und sind nur für das aktuelle Projekt verfügbar.

```bash
pip install <library>
```

Wollen Sie beispielweise die Bibliothek `pandas` installieren, führen Sie den folgenden Befehl aus:

```bash
pip install pandas
```

## Requirements-Datei

Um underen Kollegen oder zukünftigen Selbst zu zeigen, welche Bibliotheken in der virtuellen Umgebung installiert sind, kann eine Requirements-Datei erstellt werden. Die Datei enthält eine Liste der installierten Bibliotheken und deren Versionen. Um eine Requirements-Datei zu erstellen, führen Sie den folgenden Befehl aus:

```bash
pip freeze > requirements.txt
```


