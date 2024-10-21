# List Comprehensions

List Comprehensions in Python sind eine elegante und effiziente Möglichkeit um Listen zu erstellen und Operationen auf 
ihren Elementen auszuführen. Sie bieten eine klare und prägnante Alternative zu traditionellen Schleifen
und Funktionsaufrufen. List Comprehensions sind eine typische Struktur, die man in Python-Code häufig findet.

## Problemstellungen

Stellen wir uns vor, wir möchten aus einer vorhandenen Liste eine neue Liste erstellen, in der jedes Element aufgrund
einer Bedingung oder einer Operation verändert wurde. Traditionell würden wir dazu eine for-Schleife verwenden, die
über die alte Liste iteriert, die Operation durchführt und das Ergebnis in einer neuen Liste speichert. Das würde dann
so aussehen:

```python
quadrate = []
for i in range(1, 6):
    quadrate.append(i * i)

print(quadrate)
```


List Comprehensions vereinfachen diesen Code, indem sie die gesamte Logik in eine einzige, lesbare Zeile komprimieren. Sie
können Bedingungen anwenden, Funktionen aufrufen und die resultierende Liste direkt erzeugen, was den Code wesentlich
sauberer und eleganter macht.

```python
quadrate = [i * i for i in range(1, 6)]

print(quadrate)
```

Die einfachste Form der List Comprehension sieht also so aus:

`[ausdruck(item) for item in iterable]`


## Motivation für List Comprehensions

* **Kompakter Code**: List Comprehensions ermöglichen es, Schleifen und bedingte Anweisungen in einer Zeile zu 
schreiben, wodurch der Code kürzer und, wenn man es nicht übertreibt, auch leichter lesbar wird.

* **Performance**: Sie sind oft schneller als traditionelle Schleifen, besonders bei der Erstellung großer Listen.

List Comprehensions sind ein hervorragendes Beispiel für **pythonic** Code, also Code der typisch für Python-Programme
ist und die **jeder kennen und verstehen sollte**.

## Aufgaben zu einfachen List Comprehensions

{{ task(file="tasks/list_comp_quadrate_erstellen.yaml") }}

{{ task(file="tasks/list_comp_zeichenkettenlaengen.yaml") }}

{{ task(file="tasks/list_comp_absolute_werte.yaml") }}

{{ task(file="tasks/list_comp_string_in_grossbuchstaben.yaml") }}

{{ task(file="tasks/list_comp_wurzeln_ziehen.yaml") }}

{{ task(file="tasks/list_comp_tupel_erstellen.yaml") }}

{{ task(file="tasks/list_comp_teile_von_strings.yaml") }}

{{ task(file="tasks/list_comp_durchschnittswerte.yaml") }}

## Elemente filtern

Es ist bei einer List Comprehension einfach möglich bestimmte Elemente
aus der Liste unter einer Bedingung zu entfernen. Der folgende Code:

```python
words = ["Python", "ist", "cool"]

result = []
for word in words:
    if len(word) > 3:
        result.append(word)
        
print(result)
```


lässt sich zu diesem vereinfachen:


```python
words = ["Python", "ist", "cool"]

result = [word for word in words if len(word) > 3]

print(result)
```

## Bedingte Einsetzung

Im letzten Beispiel haben wir gesehen, wie wir Elemente filtern können.
Manchmal möchte man aber auch verschiedene Operationen auf einem
Element durchführen, basierend auf einer Bedingung. Hier lässt sich
der ternäre Operater nutzen. Den folgendne Code

```python
result = []
for i in range(6):
    if i%2:
        result.append(i)
    else:
        result.append(i*i)
        
print(result)
```


vereinfachen wir zunächst zu

```python
result = []
for i in range(6):
    result.append(i if i % 2 else i * i)
        
print(result)
```


und abschließend:


```python
result = [i if i % 2 else i * i for i in range(6)]
print(result)
```

## Aufgaben zu List Comprehensions

{{ task(file='tasks/list_comp_gerade_zahlen.yaml') }}

{{ task(file='tasks/list_comp_filtern_nach_bedingung.yaml') }}

{{ task(file='tasks/list_comp_nicht_leere_strings.yaml') }}

{{ task(file='tasks/list_comp_fizz_buzz.yaml') }}

## Verschachtelte List Comprehension

Es ist auch möglich verschachtelte Schleifen in List Comprehensions
zu übersetzen. 

Ausgangscode:

```python
result = []
for i in range(4):
    for j in range(4):
        result.append(i * j)
print(result)
```

Gekürzt:

```python
result = [i * j for i in range(4) for j in range(4)]

print(result)
```

{{ task(file='tasks/list_comp_bedingung_fehlt.yaml') }}

{{ task(file='tasks/list_comp_liste_von_listen_abflachen.yaml') }}

{{ task(file='tasks/list_comp_verschachtelung.yaml') }}


## List Comprehensions nicht nur für Listen

Tatsächlich lassen sich List Comprehensions nicht nur für Listen
verwenden, man kann sie auch für Dictionaries oder Sets nutzen:

```python
new_set = {abs(x) for x in range(-3, 4)} # {0, 1, 2, 3}

new_dict = {word: len(word) for word in ["Hi", "was", "geht"]} # {"Hi": 2, "was": 3, "geht": 4}
```

{{ task(file='tasks/list_comp_dictionary_comprehension.yaml') }}

## Generator - was dahintersteckt

Vielleicht ist dir aufgefallen, dass die folgende Syntax nicht
zu einem Tupel führt, sondern man einen Generator zurückbekommt:

```python
my_gen = (i * 2 for i in range(4))

print(my_gen) # <generator object <genexpr> at 0x000001F7191D7B50>
print(type(my_gen)) # <class 'generator'>
```

Tatsächlich handelt es sich hier in der ersten Zeile um eine 
[Generator Expression](https://docs.python.org/3/glossary.html#term-generator-expression).

Ein [generator](https://docs.python.org/3/glossary.html#term-generator)
kann mit der Methode `next` um das nächste Element gebeten werden.
Das geht so lange, bis eine `StopIteration` Exception geworfen wird.

```python
my_gen = (i * 2 for i in range(4))

print(next(my_gen)) # 0
print(next(my_gen)) # 2
print(next(my_gen)) # 4
print(next(my_gen)) # 6
print(next(my_gen)) # StopIteration
```

So ein `generator` lässt sich so auch klasse mit einer `for`-Schleife
durchlaufen, da diese intern immer wieder die `next`-Methode aufruft,
bis es zur `StopIteration` Exception kommt.

```python
summe = 0
for i in (i * 2 for i in range(4)):
    summe += i

print(summe)
```

Dieser Code lässt sich tatsächlich noch kürzen zu:

```python
summe = sum(i * 2 for i in range(4))
print(summe)
```

Es gibt diverse eingebaute Pythonmethoden, die so mit Iteratoren
umgehen können. Dazu gehören: `all`, `any`, `map` oder `tuple`. Du findest noch 
weiter [hier in der Dokumentation](https://docs.python.org/3/library/functions.html),
wenn du nach den Funktionen suchst, die `iterable`
als Parameter erwarten.

{{ task(file='tasks/list_comp_anzahl_vokale.yaml') }}

{{ task(file='tasks/list_comp_tuple_comprehension.yaml') }}

