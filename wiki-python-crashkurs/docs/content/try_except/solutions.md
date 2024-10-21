# Lösung

### Aufgabe: Benutzereingabe und Integer-Konvertierung 

```python
a, b = None, None
while not a or not b:
    try:
        a = int(input("Erste Zahl: "))
        b = int(input("Zweite Zahl: "))
    except ValueError:
        print("Das war keine Zahl. Bitte erneut.")
else:
    print(f"Der Durchschnitt ist: {(a + b) / 2}")
```

### Aufgabe: Benutzerdefinierte Ausnahme 
```python
class NegativeNumberError(Exception):
    pass


for number in [1, 2, 0, -2, 3]:
    if number < 0:
        raise NegativeNumberError(f"Zahl {number} ist negativ")
    print(f"Zahl {number}")
```


### Aufgabe: Welche Fehler kann man so machen? 

Baue für die folgenden Fehler ein Beispiel, in dem sie geworfen werden.
Hier ist die [Liste aller in Python vorimplementierten Exceptions](https://docs.python.org/3/library/exceptions.html).

**IndexError**

```python
my_list = [1,2,3,4]
my_list[10]
```

**OverflowError**

```python
2.0 ** 10000 
```

**StopIteration**

```python
z = zip([1], [1])
next(z)
next(z)
```

**ValueError**

```python
int("Hallo")
```

**ZeroDivisionsError**

```python
10 / 0
```

**KeyboardInterrupt**

Entsteht z. B. wenn ein laufendes Programm abgebrochen wird, dass auf eine Nutzereingabe wartet:

```python
while True:
    print(input("Gib was ein: "))
```

### Aufgabe: Sichere Benutzereingabe 

```python
def get_number(prompt="Gib eine Ganzzahl ein: "):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Das war keine erlaubte Zahl. Erneut bitte:")


def get_operation(prompt="Gebe Operation ein: "):
    while True:
        op = input(prompt)
        if op in operations.keys():
            return op
        print(f"{op} ist keine der Erlaubten Operationen {operations.keys()} Erneut bitte:")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


# Wir speichern eine Referenz auf die jeweilige Operation
# in diesem Dictionary. Wenn wir also eine neue Funktion
# hinzufügen, müssen wir sie hier bloß mit Symbol eintragen
# und alle anderen wissen bescheid.
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

while True:
    num1 = get_number("Gib erste Ganzzahl ein")
    num2 = get_number("Gib zweite Ganzzahl ein")

    op_symbol = get_operation()
    operation = operations.get(op_symbol)

    try:
        result = operation(num1, num2)
    except Exception as e:
        print(f"Operation nicht möglich: {num1} {op_symbol} {num2} ⚡")
        print(e)
    else:
        print(f"{num1} {op_symbol} {num2} = {result}")
```

### Aufgabe: Übertriebene Rekursion 
Die Funktions `fak` ruft sich immer wieder selbst auf (das nennt man eine rekursive Funktion).
Der Callstack wird damit immer größer, bis dieser irgendwann die maximale Größe überschreitet.
Dann wird ein `RekursionError` geworfen.
