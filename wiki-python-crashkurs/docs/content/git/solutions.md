### Aufgabe: Nutzer korrekt einstellen

```commandline
git config --global user.name "Viktor Reichert"
git config --global user.email "viktor.reichert@qualidy.de"
```

### Aufgabe: Welche Vorteile?

**Kommunikation über E-Mail (Dateien als Anhänge austauschen)**:

* Eignet sich bei einfachen Projekten, bei denen nur eine Partei eine Datei manipuliert.
* Vorteil: An der Mail kann man erkennen, dass die korrekte Person mit Projektversionen vorschlägt.
* Vorteil: Automatische Notifizierung bei Projektversionen.
* Vorteil: Alle Projektversionen sind vorhanden und können wiederhergestellt werden...
* Nachteil: ...außer die Mail wird gelöscht.
* Nachteil: Gerät sehr schnell außer Kontrolle.


**Gemeinsames Laufwerk, auf das alle Projektbeteiligten Zugreifen können**

* Eignet sich bei Projekten mit großen Dateien, die nicht geändert werden, in denen eigentlich nur ein Lagerraum gebraucht wird. (z.B. 100h Videomaterial)
* Vorteil: Alle haben immer auf den aktuellen Status des Projektes Zugriff.
* Nachteil: Aber es gibt auch nur den aktuellen Status des Projektes.
* Nachteil: Alternative Projektversionen müssen erstellt werden, indem die gesamte Ordnerstruktur kopiert wird.
* Nachteil: Änderungen sind schwer bis gar nicht nachvollziehbar.
* Nachteil: Gerät nach kurzer Zeit außer Kontrolle.

**Paralleles Arbeiten an einer Datei, die in der Cloud liegt, wie mit Google Docs oder Microsoft Word**

* Eignet sich für kleine Projekte in kleinen Teams.
* Vorteil: Änderungen anderer sind sofort für alle sichtbar und editierbar.
* Nachteil: Ungestörtes Arbeiten nur mit einer eigenen Kopie der Datei möglich.


### Aufgabe: Was ist mir wichtig?
Das musst du schon selbst wissen😉


### Aufgabe: Metaphorisch gesprochen

| Metapher                  | git                  |
|---------------------------|----------------------|
| Bücherregal               | Repository           |
| Erster Tisch              | Working Tree         |
| Zweiter Tisch mit Kamera  | Index / Staging Area |
| Foto vom zweiten Tisch    | Commit               |
| Zettel auf aktuellem Foto | Branch               |

### Aufgabe: Check Please!

<details>
<summary>
🎦 Video
</summary>

</details>

```mermaid
gitGraph
    commit id: "0f3c214"
    commit id: "0fb8d7"
    branch zeugnisse
    checkout zeugnisse
    commit id: "03ddaff"
    commit id: "a5a60d4"
    checkout main
    merge zeugnisse id: "1842726"
```
Die Commitmessages sagen an, was in den jeweiligen Commits passiert.

### Aufgabe: Hilfe zur Selbsthilfe

```console
$ git help
usage: git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]
...
```

Die ersten drei Befehle rufen die Hilfe für den Befehl `init` auf.

Mit der Option -g können wir auch auf die Liste der internen Anleitungen zugreifen:

```console
$ git help -g
The common Git guides are:
   attributes          Defining attributes per path
   cli                 Git command-line interface and conventions
   core-tutorial       A Git core tutorial for developers
...
$ git help core-tutorial
```

* Die spitzen Klammern `<...>`sind Platzhalter für Inhalte, wie Branchnamen.
* Die eckigen Klammern `[..]` ist ein optionaler Parameter.
* Die eckigen Klammern mit Pipes `[..|..|..]` sind optionale Parameter, von denen nur einer gewält werden kann.
* Die runden Klammern mit Pipes `(..|..)` sind Parameter, von denen einer gewählt werden **muss**.
* Ein Befehl muss mehrfach gelistet werden, weil sich nur so in dieser Syntax alle möglichen Aufrufmöglichkeiten darstellen lassen.

### Aufgabe: cat-file

<details>
<summary>
🎦 Video
</summary>

</details>

```mermaid
flowchart TD
    C0["0f3c214<br>Commit"] -->
    T0["5ef8d03<br>Tree"] --Lebenslauf.txt-->
    B0["168730b<br>Blob<br><br>Alter: 33 Jahre<br>Beruf: Boss<br><br>Vorheriger Arbeitgeber: Geheim"] 

    C1["0fb8da7<br>Commit"] --> C0
    C1 -->
    T1["012b7e8<br>Tree"] --Lebenslauf.txt--> B0
    T1 --Bewerbungsschreiben.txt-->
    B1["7e65d0f<br>Blob<br><br>Sehr geeehrte Damen und Herren,<br><br>warum ich der richtige für euch bin? Hier sind meine 3 besten Gründe:<br><br>1. Ich bin der schönste<br>2. Ich bin der klügste<br>3. Ich bin, ehrlich gesagt, auch der demütigste."]

    C2["03ddaff<br>Commit"] --> C0
    C2 -->
    T2["09cc0f2<br>Tree"] --Lebenslauf.txt--> B0
    T2 --Zeugnis.txt-->
    B2["641eef5<br>Blob<br><br>Mathe: 1<br>Bio: 1<br>Latein: 5<br>Beauty: 1+<br>HSU: 2"]

    C3["a5a60d4<br>Commit"] --> C2
    C3 -->
    T3["c8ba3ee<br>Tree"] --Lebenslauf.txt--> B0
    T3 --Zeugnis.txt-->
    B3["32f54f8<br>Blob<br><br>Mathe: 1<br>Bio: 1<br>Latein: 5<br>Beauty: 1+<br>HSU: 2<br><br><br>Führerschein Klasse A und B"]


    C4["1842726<br/>Commit"] --> C3
    C4 --> C1
    C4 -->
    T4["d276800<br/>Tree"] --Bewerbungsschreiben.txt--> B1
    T4 --Lebenslauf.txt--> B0
    T4 --Zeugnis.txt--> B3

    subgraph Commits
    C0
    C1
    C2
    C3
    C4
    end

    subgraph Trees
    T0
    T1
    T2
    T3
    T4
    end

    subgraph Blobs
    B0
    B1
    B2
    B3
    end

    subgraph Tags
    Tag1["c96c504<br>Tag<br>Anfang"] --> C0
    end
```
