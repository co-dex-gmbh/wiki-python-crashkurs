 # Codewiederholung

{{ youtube_video("https://www.youtube.com/embed/RVo03eT3U_A?si=I-5BEoTmDDKH1Nyc") }}

<div class="grid" markdown>
<div markdown>

Mit den `if`-Blöcken haben wir kennengelernt, wie man einen Codeblock nur unter bestimmten Bedingungen durchführt.

Wir wollen nun die `while`-Blöcke anschauen. Diese sind so ähnlich wie `if`-Blöcke, den auch sie prüfen eine
Bedingung und führen den eingerückten Code nur aus, wenn die Bedinung `True` ist. ABER: Bei `while` wird
nach jeder Durchführung des eingerückten Codes, ob die Bedingung immernoch erfüllt ist! Und wenn ja, dann
wird der eingerückte Codeblock NOCH MAL durchgeführt. Und das immerwieder!



```python
zahl = 1 # (1)!
while zahl < 100:  # (2)!
    print(zahl)  # (3)!
    zahl = zahl * 2  # (4)!
print(f'Finaler Wert: {zahl}.') # (5)!
```

1. Die Variable `zahl` wird mit dem Wert `#!python 1` angelegt.
2. Es wird geprüft, ob der Wert in `zahl` kleiner als `#!python 100` ist. Wenn ja, werden die nächsten beiden Zeilen ausgeführt. Wenn nein, so wird direkt zu Zeile 5 gesprungen.
3. Auf der Konsole wird der aktuelle Wert von `zahl` ausgegeben.
4. Der Wert von `zahl` wird verdopplt und dies in `zahl` gespeichert.
   **Achtung: Danach geht es in Zeile 2 weiter!**
5. Abschließend wird der finale Wert von `zahl` ausgegeben.

</div>
<div markdown>

``` mermaid
stateDiagram-v2
    classDef yourState font-style:italic,font-weight:bold,fill:white

    B:Bedingung überprüfen
    I:Code *im* eingerückten<br/>Block ausführen
    F:Code *nach* eingerücktem<br/>Block ausführen
    [*] --> B:::yourState
    B --> I : True
    I --> B : Springe zurück
    B --> F : False
```
</div>
</div>

{{ python_tutor("""zahl = 2
while zahl < 100:
    print(zahl)
    zahl = zahl * 2
print(f'Finaler Wert: {zahl}.')
""") }}


!!! bug "Endlosschleifen abbrechen"

    Sollten Sie in eine Endlosschleife geraten, können Sie ins Terminal klicken und die Ausführung mit ++ctrl++ + ++c++ abbrechen.


{{ task(file="tasks/while_lesen_1.yaml") }}

{{ task(file="tasks/while_lesen_2.yaml") }}

{{ task(file="tasks/dauernder_input.yaml") }}

{{ task(file="tasks/schleifen_und_if.yaml") }}

{{ task(file="tasks/immer_wechselnder_output.yaml") }}

## Aufgaben


### 1. Summe von 1 bis 100 
Nutze eine while-Schleife, die die Zahlen 1, 2, 3, ... usw. so lange addiert, bis die Summe größer als 100 ist.
Bis zu welcher Zahl muss addiert werden? Wie groß ist die erste Summe über 100?

### 2. Input erfragen
Schreibe ein Programm, dass den Nutzer immer wieder nach Zahlen fragt. Es soll nach jeder Eingabe 
die Summe aller bisher erfragen Zahlen zurückgeben.

### 3. Fakultät 
Verwende eine While-Schleife, um das kleinste `n` zu finden, sodass `n! > 100_000` ist.

### 4. Fast endlose Schleife 
Erstelle eine Schleife, die so lange Zufallszahlen zwischen 1 und 10 generiert und ausgibt, bis die Zahl 5 erscheint.
Nutze dazu `random.randint(a,b)` ([Doku](https://docs.python.org/3/library/random.html#random.randint))

### 5. Fibonacci 
Nutze eine While-Schleife, um die erste Zahl in der Fibonaccifolge zu finden, die größer als 100 ist.
Die Fibonaccifolge beginnt mit den beiden Zahlen `1` und `1`. Die nächste Zahl der Folge ist die Summe
der beiden vorherigen. Der Anfang der Fibonaccifolge sieht also wie folgt aus:

    1, 1, 2, 3, 5, 8, 13, 21, 34, ...

[Lösungen](solutions.md#while-schleifen)

## Einführung in `for`-Schleifen

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/IZmCkNQb5v8?si=I4rS9cz-B1xrp0_6" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

Hier ist ein einfaches Beispiel für eine `for`-Schleife in Python (drücke auf "Next >" um den Code schrittweise 
durchzuführen):

[💻 Link zum Onlinecompiler](https://pythontutor.com/render.html#code=fruechte%20%3D%20%5B%22Apfel%22,%20%22Banane%22,%20%22Kirsche%22%5D%0Afor%20frucht%20in%20fruechte%3A%0A%20%20%20%20print%28frucht%29%0Aprint%28%22fertig%22%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
fruechte = ["Apfel", "Banane", "Kirsche"]
for frucht in fruechte:
    print(frucht)
print("fertig")
```


Diese Schleife iteriert über die Liste `fruechte` und gibt jede Frucht nacheinander aus. Für jeden Durchlauf der
Schleife nimmt `frucht` ein anderes Element der Liste an und steht im Schleifenkörper zur Verfügung.

## Syntax einer `for`-Schleife

Die grundlegende Syntax einer `for`-Schleife in Python lautet:

```python
for element in sequenz:
# Anweisungen, die für jedes Element ausgeführt werden
```

- `element`: Eine Variable, die den aktuellen Wert aus der Sequenz repräsentiert.
- `sequenz`: Die Sequenz, über die iteriert wird (z. B. eine Liste, ein Tupel, eine Zeichenkette oder eine range, auf die wir gleich eingehen werden).

## Aufgaben

### 1. Zählen 
Schreibe eine `for`-Schleife, die die Zahlen von 1 bis 10 ausgibt.
### 2. Städtetrip 
Erstelle eine Liste von Städten und verwenden Sie eine `for`-Schleife, um jede Stadt auszugeben.
### 3. Summierung 
Schreibe eine `for`-Schleife, die die Summe aller Zahlen von 1 bis 10 berechnet.
### 4. Längster Name 
Erstelle eine Liste von Namen und verwenden Sie eine `for`-Schleife, um den längsten Namen in der Liste zu finden.
### 5. Quadratzahlen 
Schreibe eine `for`-Schleife, die die Quadratzahlen von 1 bis 10 ausgibt.
### 6. Verdreht
Schreibe eine `for`-Schleife, die die Buchstaben eines Wortes in umgekehrter Reihenfolge ausgibt.
### 7. Fakultät 
Schreibe eine `for`-Schleife, die die Fakultät (n!) einer gegebenen Zahl `n` berechnet. Zur Errinnerung:

```commandline
n! := n ⋅ (n-1) ⋅ (n-2) ⋅ ... ⋅ 2 ⋅ 1
6! = 6⋅5⋅4⋅3⋅2⋅1 = 720 
1! = 1
0! = 1
```

### 8. Thermometer für Amerikaner 
Erstelle eine Liste von Temperaturen in Celsius und verwenden Sie eine `for`-Schleife, um jede nacheinander in Fahrenheit
umzuwandeln und auszugeben. Recherchiere die entsprechende Formel.
### 9. Vokale 
Schreibe eine `for`-Schleife, die die Anzahl der Vokale in einem gegebenen Wort zählt.
### 10. Häufigkeit 
Schreibe eine `for`-Schleife, die einen Text durchläuft und zählt, wie oft ein bestimmtes Wort in diesem Text
vorkommt.

[Lösungen](solutions.md#for-schleifen)


## Iteration über feste Zahlenbereiche mit `range`

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/IQhjfZiCOro?si=47NPqX5Fn0SOri8G" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Möchte man über einen bestimmten Zahlenraum iterieren, so verwendet man in Python die `range`-Funktion. Es gibt drei 
Möglichkeiten `range` aufzurufen:

| Anazahl Parameter | Aufruf                         | Bedeutung                                                                                                                | Beispiel          | Entsprechende Liste |
|-------------------|--------------------------------|--------------------------------------------------------------------------------------------------------------------------|-------------------|---------------------|
| 1                 | `range(end)`                   | Die Range enthält die Integer von `0` bis _ausschließlich_ `end`.                                                        | `range(3)`        | `[0,1,2]`           |
| 2                 | `range(start, end)`            | Die Range enthält die Integer von `start` bis _ausschließlich_ `end`.                                                    | `range(12, 15)`   | `[12,13,14]`        |
| 3                 | `range(start, end, step_size)` | Die Range enthält die Integer von `start` bis _ausschließlich_ `end`. und geht dabei in Schritten der Größe `step_size`. | `range(3, 10, 2)` | `[3,5,7,9]`         |

### Aufgabe: Ranges vorhersagen

Welche listen werden in jeder Zeile jeweils erzeugt?

```python
list(range(10)) 
list(range(1, 11))
list(range(0, 30, 5))
list(range(0, 10, 3))
list(range(0, -10, -1))
list(range(0)) 
list(range(1, 0))
```
[Lösung](solutions.md#aufgabe-ranges-vorhersagen)

## Nutzen von Ranges

Ranges wirken auf den ersten Blick sehr ähnlich zu Listen. Schaut man sie sich genauer an, stellt man sogar fest,
dass sie sogar Indizierung und Slicing erlauben. Es gibt zwei wichtige Vorteile:

* Ranges können leicht instanziiert werden (wie würdest du eine Liste aller geraden Zahlen bis 1000 in Python sonst erstellen?),
* Ranges sparen Speicherplatz. Denn die Zahlen, die in der Range sind, werden nicht alle zunächst im Speicher hinlegt, sondern erst bei Bedarf bereitgestellt (indem sie jeweils berechnet werden).

Wir können Ranges so einfach für Schleifeniterationen über einen Integer-Zahlenraum nutzen:

[💻 Link zum Onlinecompiler](https://pythontutor.com/render.html#code=for%20i%20in%20range%285%29%3A%0A%20%20%20%20print%28i%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
for i in range(5):
    print(i)
```

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/nqMMCr3juCE?si=RpI4n9QONgTR_Qz7" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


## Vorzeitiges Abbrechen einer Schleife

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/suZrbAoSmr0?si=hloioyGs7h7phUNw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


[//]: # ([60min])
In vielen Fällen sucht man einfach einen Wert in einem Bereich oder ein bestimmtes Element in einer List. Sobald man
dieses gefunden hat, kann man die Schleife eigentlich abbrechen. Dafür nutzt man das Keyword `break`:

[💻 Link zum Onlinecompiler](https://pythontutor.com/render.html#code=for%20i%20in%20range%280,%2010%29%3A%0A%20%20%20%20print%28i%29%0A%20%20%20%20if%20i%20%3D%3D%205%3A%0A%20%20%20%20%20%20%20%20break%0Aprint%28%22Ende%22%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
for i in range(0, 10):
    print(i)
    if i == 5:
        break
print("Ende")
```


Sobald die Bedingung `i == 5` wahr wird, sorgt `break` dafür, dass wir die Schleifen verlassen. Damit sparen wir uns 5
weitere Durchläufe. Bei komplexen Problemstellungen kann man damit sehr viel Zeit sparen.

Auf der anderen Seite gibt es aber auch Fälle, in denen man nicht die ganze Schleife beenden will, sondern nur den
aktuellen Durchlauf. Dafür nutzt man das Keyword `continue`.

[💻 Link zum Onlinecompiler](https://pythontutor.com/render.html#code=for%20i%20in%20range%280,%2010%29%3A%0A%20%20%20%20if%203%20%3C%3D%20i%20%3C%3D%205%3A%0A%20%20%20%20%20%20%20%20continue%0A%20%20%20%20print%28i%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
for i in range(0, 10):
    if 3 <= i <= 5:
        continue
    print(i)
```


Wieso? Für jeder Zahl zwischen 0 und 10 wird überprüft, ob diese Zahl zwischen 3 und 5 liegt. Ist das der Fall, springt
der Code direkt an den Schleifenanfang (wegen des `continue`), statt die Zeile 4 auszuführen.
direkt zum nächsten Durchlauf. In allen anderen Fällen wird die Zahl auf der Konsole ausgegeben.

Sehr häufig wird break in Kombination mit while-Schleifen verwendet. Wieso? Weil es so einfach möglich ist,
Endlosschleifen zu erzeugen, die unter bestimmten Bedingungen abbrechen, die nicht im Schleifenkopf überprüft werden.  

Zum Beispiel:

```python
while True:
    eingabe = input()
    if eingabe == "C":
        break

    print(f"Deine Eingabe in groß: {eingabe.upper()}")

print("Bye Bye")
```

Durch `while True:` läuft diese Schleife theoretisch endlos lange, weil die Bedingung immer wahr ist. Bei jedem
Schleifendurchlauf wird der Nutzer nach einer Eingabe gefragt. Sobald der Nutzer "C" eingibt, wird die Schleife durch
den Befehl `break` verlassen und das Programm kann normal weiterlaufen.

# Else-Zweig bei While- und For-Schleifen in Python

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/_HQlJUAIuh8?si=N0iBJYNgI4g8MVpT" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


[//]: # ([30min])
In Python können sowohl `while`- als auch `for`-Schleifen mit einem optionalen `else`-Zweig versehen werden. Dieser Teil
der Schleife wird ausgeführt, wenn die Schleife auf normale Weise beendet wird, d.h., **nicht durch ein `break`-Statement
unterbrochen wird**.

[💻 Link zum Onlinecompiler](https://pythontutor.com/render.html#code=summe%20%3D%200%0Afor%20number%20in%20%5B%2243%22,%20%221234%22,%20%2233.4%22,%20%2210%22%5D%3A%0A%20%20%20%20if%20not%20number.isdigit%28%29%3A%0A%20%20%20%20%20%20%20%20print%28f%22%7Bnumber%7D%20is%20no%20integer!%20Abort%22%29%0A%20%20%20%20%20%20%20%20break%0A%20%20%20%20summe%20%2B%3D%20int%28number%29%0Aelse%3A%0A%20%20%20%20print%28f%22Die%20Summe%20aller%20Zahlen%20ist%20%7Bsumme%7D.%22%29%0Aprint%28%22Ende%22%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
summe = 0
for number in ["43", "1234", "33.4", "10"]:
    if not number.isdigit():
        print(f"{number} is no integer! Abort")
        break
    summe += int(number)
else:
    print(f"Die Summe aller Zahlen ist {summe}.")
print("Ende")
```


# Verschachtelte Schleifen

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/eBdI_N7yK8A?si=rr9x0FQ3WyNqqyki" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

Es ist auch möglich Schleifen in Schleifen zu verwenden. Dies sieht man tatsächlich sehr häufig, da es oft
verschachtelte Strukturen gibt, die durchlaufen werden sollen, z.B. Listen von Listen.

[💻 Link zum Onlinecompiler](https://pythontutor.com/render.html#code=list_of_lists%20%3D%20%5B%5B1,2,3%5D,%20%5B40,50,60%5D,%20%5B700,800,900%5D%5D%0A%0Asumme%20%3D%200%0A%0Afor%20sub_list%20in%20list_of_lists%3A%0A%20%20%20%20for%20element%20in%20sub_list%3A%0A%20%20%20%20%20%20%20%20summe%20%2B%3D%20element%0A%20%20%20%20print%28f%22Zwischenergebnis%3A%20%7Bsumme%7D%22%29%20%20%20%20%20%20%20%20%0Aprint%28f%22Endergebnis%3A%20%7Bsumme%7D%22%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
list_of_lists = [[1,2,3], [40,50,60], [700,800,900]]

summe = 0

for sub_list in list_of_lists:
    for element in sub_list:
        summe += element
    print(f"Zwischenergebnis: {summe}")        
print(f"Endergebnis: {summe}")
```



### Aufgabe: Produktsummen

Was ist das Ergebnis des folgenden Codes. Versuche in eigenen Worten zu beschreiben, was der Code tut.
Tipp: Führe den Code mit dem Debugger aus.

```python
result = 1
for sub_list in [[4,3,2], [5,6,7]]:
    subsum = 0
    for element in sub_list:
        subsum += element
    result *= subsum
print(result)
```

### Aufgabe: Summenprodukt

Schreibe Code, der die Liste `[[1,2,3], [-3, 4, 6, 9, 3], [0], [4,4], []]` durchläuft.
Die Elemente jeder inneren Liste sollen multipliziert werden und diese Zwischenergebnisse dann addiert werden.

[Lösung](solutions.md#verschachtelte-schleifen)

# Anspruchsvolle Aufgaben

[//]: # ([60min])

### Aufgabe 1: Finden

Schreibe ien Programm, das in einem Text das erste Wort findet, länger als 8 Buchstaben ist und dieses zurückgibt.
Schreibe eine Antwort mit und eine ohne die Verwendung von `continue`.


### Aufgabe 2: Benutzerdefinierte Passwortüberprüfung 

Schreibe ein Programm, das den Benutzer zur Eingabe eines Passworts auffordert. Das Passwort muss bestimmte Kriterien
erfüllen (z.B. mindestens 8 Zeichen lang, enthält sowohl Zahlen als auch Buchstaben). Das Programm soll dem Benutzer
mitteilen, ob das eingegebene Passwort gültig ist oder nicht. Wenn das Passwort nicht gültig ist, soll das Programm
spezifizieren, welche Kriterien nicht erfüllt wurden.


### Aufgabe 3: Einfacher Zahlenraten 

Erstelle ein Spiel, bei dem der Benutzer versuchen muss, eine zufällig generierte Zahl zwischen 1 und 100 zu erraten.
Nach jeder Eingabe gibt das Programm an, ob die geratene Zahl zu hoch oder zu niedrig ist. Der Benutzer hat eine
begrenzte Anzahl von Versuchen (z.B. 10). Nach dem Spiel gibt das Programm an, ob der Benutzer gewonnen hat und wie
viele Versuche benötigt wurden.

### Aufgabe 4: Bestellung in einem virtuellen Café  

Simuliere ein einfaches Bestellsystem für ein Café. Das Programm listet verschiedene Getränke und Speisen mit ihren
Preisen auf. Der Benutzer kann Artikel auswählen und die gewünschte Menge angeben. Das Programm führt eine laufende
Summe der Bestellung. Nachdem der Benutzer seine Auswahl abgeschlossen hat, zeigt das Programm die Gesamtsumme der
Bestellung an und fragt, ob der Benutzer bar oder mit Karte zahlen möchte.

```python
menu = {"Kaffee": 2.50, "Tee": 2.00, "Kuchen": 3.00}
```

[Lösungen](solutions.md#anspruchsvolle-aufgaben)
