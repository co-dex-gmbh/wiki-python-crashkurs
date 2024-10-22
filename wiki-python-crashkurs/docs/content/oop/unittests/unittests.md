# Unittest

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/hnd6Fs2L0do?si=MfhPW2wgUOiN8qel" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

Wir haben im [Kapitel Docstring](../../docstring/docstring.md#unittests-in-der-dokumentation) gesehen,
wie man Unittests in den Docstring einbauen kann. Das ist nützlich, um sicherzustellen, dass der Nutzer
Codebeispiele besitzt und diese auch immer Funktionieren.

Eine weitere Möglichkeit Unittests zu schreiben ist mittels des Pakets `unittest`.
Der offensichtlichste Unterschied zum Modul `doctest` besteht darin, dass die
Testfälle bei dem Modul `unittest` außerhalb des eigentlichen Programmcodes definiert werden,
d.h. normalerweise in einer eigenen Datei. Der Vorteil besteht unter anderem
darin, dass die Programmdokumentation und die ausführliche Testung voneinander getrennt sind.
Der Preis dafür besteht jedoch in einem erhöhten Aufwand
für die Erstellung der Tests. Doch dieser lohnt sich.

Wir wollen nun für unser Modul `fibonacci.py` einen Test mit `unittest` erstellen.

[Link zum Onlinecompiler💻](https://pythontutor.com/render.html#code=def%20fib%28n%29%3A%0A%20%20%20%20%22%22%22%20%0A%20%20%20%20Die%20Fibonacci-Zahl%20f%C3%BCr%20die%20n-te%20%0A%20%20%20%20Generation%20wird%20iterativ%20berechnet%0A%20%20%20%20%22%22%22%0A%20%20%20%20a,%20b%20%3D%200,%201%0A%20%20%20%20for%20_%20in%20range%28n%29%3A%0A%20%20%20%20%20%20%20%20a,%20b%20%3D%20b,%20a%20%2B%20b%0A%20%20%20%20return%20a%0A%20%20%20%20%0Aprint%28fib%286%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
def fib(n):
    """ 
    Die Fibonacci-Zahl für die n-te 
    Generation wird iterativ berechnet
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
    
print(fib(6))
```


In einer Datei, z.B. `fibonacci_unittest.py`, müssen wir das Modul `unittest` und
das zu testende Modul, also in unserem Fall `fibonacci`, importieren.

__Hinweis:__ Es empfiehlt sich eine einheitliche Konvention innerhalb des Projekts
für die Dateinamen die Tests enthalten zu wählen.
Wird _Visual Studio Code_ verwendet so sollte für die Ausführungserkennung das Wort `test` im Dateinamen vorkommen.
Entweder `fibonacci_test.py` oder `test_fibonacci.py` abhängig davon, ob bevorzugt wird alle Testdateien im Dateibaum
nebeneinandern zu haben, oder alternativ die Testdatei neben der Codedatei, die sie testet, liegen zu haben.

Außerdem müssen wir eine Klasse mit beliebigem Namen - wir wählen in unserem Beispiel `FibonacciTest` - erstellen,
die von `unittest.TestCase` erbt. Wir werden das Konzept von Vererbung später genauer betrachtet; kurz gesagt
sorgen wir so dafür, dass unsere neue Klasse schon jede Menge Funktionen bereithält.

In dieser Klasse werden die nötigen Testfälle in Methoden definiert.
__Der Name dieser Methoden ist nicht beliebig, denn er muss mit **test** beginnen.__
In den Methoden benutzen wir die Methode `assertEqual` der Klasse
`TestCase`. `assertEqual(first, second, msg = None)` prüft, ob der Ausdruck `first` gleich dem Ausdruck `second` ist.
Falls die beiden Ausdrücke ungleich
sind, wird `msg` ausgegeben, wenn `msg` ungleich `None` ist.

```python
import unittest
from fibonacci import fib


class FibonacciTest(unittest.TestCase):

    def test_calculation_0(self):
        self.assertEqual(fib(0), 0)

    def test_calculation_1(self):
        self.assertEqual(fib(1), 1)

    def test_calculation_2(self):
        self.assertEqual(fib(5), 5)

    def test_calculation_3(self):
        self.assertEqual(fib(10), 55)

    def test_calculation_4(self):
        self.assertEqual(fib(20), 6765)


unittest.main()

# Für Jupyter/IPython Sessions:
# unittest.main(argv=[''], verbosity=2, exit=False) 
```

Rufen wir obigen Test auf, erhalten wir folgende Ausgabe:

```bash
Launching pytest with arguments python_programm.py::FibonacciTest --no-header --no-summary -q in C:\Users\Vikto\PycharmProjects\wiki-python

============================= test session starts =============================
collecting ... collected 5 items

python_programm.py::FibonacciTest::test_calculation_0 
python_programm.py::FibonacciTest::test_calculation_1 
python_programm.py::FibonacciTest::test_calculation_2 
python_programm.py::FibonacciTest::test_calculation_3 
python_programm.py::FibonacciTest::test_calculation_4 

============================== 5 passed in 0.03s ==============================
PASSED                   [ 20%]PASSED                   [ 40%]PASSED                   [ 60%]PASSED                   [ 80%]PASSED                   [100%]
Process finished with exit code 0
```

Bei der normalen Programmentwicklung ist dies das von uns gewünschte Ergebnis.

### Methoden der Klasse TestCase

Wir wollen nun näher auf die Klasse TestCase eingehen. Wir stellen dazu einige
wichtige Methoden dieser Klasse vor.

| Methode                                                                     | Bedeutung                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `setUp()`                                                                   | Bei der Methode `setUp` handelt es sich um eine sogenannte Hook-Methode. Sie wird vor jedem Aufruf der implementierten Testmethoden aufgerufen. Wird in der Methode setUp eine Ausnahme generiert, so wird diese auch als Error in der Testausgabe ausgegeben. Selbstverständlich wird auch bei einer Ausnahme im `setUp`-Code der Test abgebrochen.                                                                                                               |
| `tearDown()`                                                                | Die Methode `tearDown` wird nach dem Aufruf einer Testmethode gestartet. Ebenso wie bei setUp gilt, dass im Code von tearDown generierte Ausnahmen auch in der Testausgabe ausgegeben werden.                                                                                                                                                                                                                                                                      |
| `assertAlmostEqual(self, first, second, places=None, msg=None, delta=None)` | Diese Methode schlägt fehl, wenn die Differenz der beiden Parameter `first` und `second` gleich `0` ist, nachdem man sie vor dem Vergleich auf `places` Nachkommastellen gerundet hatte. Der Default-Wert für `places` ist `7`.                                                                                                                                                                                                                                    |
| `assertCountEqual(self, first, second, msg=None)`                           | Die Parameter `first` und `second` müssen hierbei sequentielle Datentypen sein. Es muss folgendes gelten:<br>Alle Elemente müssen genauso oft in `first` wie in `second` vorkommen.<br><br>Beispiel:<br><br>`[0, 1, 1]` und `[1, 0, 1]` gelten in obigem Sinne als gleich, weil die 0 und die 1 jeweils gleich oft vorkommen.<br><br>[0, 0, 1] und [0, 1] sind verschieden, weil die `0` in der ersten Liste zweimal vorkommt und in der zweiten Liste nur einmal. |
| `assertDictEqual(self, d1, d2, msg=None)`                                   | Betrachtet die beiden Argumente als Dictionaries und prüft auf Gleichheit.                                                                                                                                                                                                                                                                                                                                                                                         |
| `assertEqual(self, first, second, msg=None)`                                  | Der Test schlägt fehl, wenn die Parameter "first" und "second" nicht gleich sind. Dabei ist Gleichheit im Sinne von "==" gemeint, also Wertegleichheit und nicht nur reine Objektgleichheit.                                                                                                                                                                                                                                                                       |
| `assertTrue(self, expr, msg=None)`                                          | Prüft, ob der Ausdruck `expr` `True` ist.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `assertGreater(self, a, b, msg=None)`                                       | Prüft, ob a > b gilt.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `assertGreaterEqual(self, a, b, msg=None)`                                  | Prüft, ob a ≥ b gilt.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `assertFalse(self, expr, msg=None)`                                         | Prüft, ob der Ausdruck `expr` `False` ist.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `assertLess(self, a, b, msg=None)`                                          | Prüft, ob a < b gilt.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `assertLessEqual(self, a, b, msg=None)`                                     | Prüft, ob a ≤ b gilt.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `assertIn(self, member, container, msg=None)`                               | Prüft, ob a in b gilt.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `assertIs(self, expr1, expr2, msg=None)`                                    | Prüft, ob "a is b" gilt.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `assertIsInstance(self, obj, cls, msg=None)`                                | Prüft, ob isinstance(obj, cls) gilt.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `assertIsNone(self, obj, msg=None)`                                         | Prüft, ob "obj is None" gilt.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `assertIsNot(self, expr1, expr2, msg=None)`                                 | Prüft, ob "a is not b" gilt.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `assertIsNotNone(self, obj, msg=None)`                                      | Prüft, ob obj nicht None ist.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `assertListEqual(self, list1, list2, msg=None)`                             | Listen werden auf Gleichheit geprüft.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `assertMultiLineEqual(self, first, second, msg=None)`                       | Mehrzeilige Strings werden auf Gleichheit geprüft.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `assertNotRegexpMatches(self, text, unexpected_regexp, msg=None)`           | Schlägt fehl, wenn der Text "text" den regulären Ausdruck unexpected_regexp matched.                                                                                                                                                                                                                                                                                                                                                                               |
| `assertRaises(exception, callable, msg=None)`                               | Prüft, ob die angegebene Exception geworfen wird, wenn das `callable` aufgerufen wird. Wird gerne in einem `with`-Block verwendet.                                                                                                                                                                                                                                                                                                                                 |
| `assertTupleEqual(self, tuple1, tuple2, msg=None)`                          | Analog zu assertListEqual                                                                                                                                                                                                                                                                                                                                                                                                                                          |

Sie dazu [die Dokumentation](https://docs.python.org/3/library/unittest.html).

### Aufgabe: Eigene Test schreiben🌶🌶
Schreibe Tests für die folgende Funktion, die alle positiven Zahlen in einer Liste aufsummiert:

```python
def sum_positives(mylist):
    return sum(i for i in mylist if i > 0)
```
Schreibe dabei Tests für folgende Fälle:

* leere Liste wird übergeben.
* Liste mit einem Element wird übergeben.
* Liste mit mehr als einem Element wird übergeben.
* Eine Liste mit den Zahlen von 1 bis 1000 übergeben wird
* Liste nur aus negativen Zahlen wird übergeben.
* Liste mit nur positiven Zahlen verhält sich genauso wie `sum`.
* Exception wird geworfen, wenn z.B. ein Integer übergeben wird (Recherche nötig).
* Wenn die Liste `float` enthält, ist der Rückgabetyp auch float.
* der Output für `[0.1, 0.2, -0.5]` ist fast `0.3`.

<details>
<summary>Lösung</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/LJ-_kWTeNW0?si=jB99blO-z4ay1KKs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<pre><code>import unittest

def sum_positives(mylist):
    return sum(i for i in mylist if i > 0)

class SumTest(unittest.TestCase):
    # * leere Liste wird übergeben.
    def test_sum_empty(self):
        self.assertEqual(sum_positives([]), 0)

    # * Liste mit einem Element wird übergeben.
    def test_sum_singleton(self):
        self.assertEqual(sum_positives([5]), 5)

    # * Liste mit mehr als einem Element wird übergeben.
    def test_sum_multiple_elements(self):
        self.assertEqual(sum_positives([5, -5, 12]), 17)

    # * Eine Liste mit den Zahlen von 1 bis 1000 übergeben wird
    def test_big_sum(self):
        n = 1000
        big_list = list(range(1, n + 1))
        expected = (n * (n+1)) // 2
        self.assertEqual(sum_positives(big_list), expected)

    # * Liste nur aus negativen Zahlen wird übergeben.
    def test_only_negative_numbers(self):
        self.assertEqual(sum_positives([-1, -3, -4]), 0)

    # * Liste mit nur positiven Zahlen verhält sich genauso wie `sum`.
    def test_sum_equal_to_sum_positive_when_only_positive(self):
        my_list = [3, 5, 29, 4, 2]
        self.assertEqual(sum_positives(my_list), sum(my_list))

    # * Exception wird geworfen, wenn z.B. ein Integer übergeben wird (Recherche nötig).
    def test_exception_when_wrong_type(self):
        with self.assertRaises(TypeError):
            sum_positives(2)

    # * Wenn die Liste `float` enthält, ist der Rückgabetyp auch float.
    def test_return_float_when_input_float(self):
        self.assertIsInstance(sum_positives([0.3]), float)

    # * der Output für `[0.1, 0.2, -0.5]` ist fast `0.3`.
    def test_floaty_example(self):
        self.assertAlmostEqual(sum_positives([0.1, 0.2, -0.5]), 0.3)

unittest.main()</code></pre>
</details>

### Aufgabe: Erst die Tests🌶🌶

Erstelle fünf Tests für die Funktion `get_capital_letters(string)`.
Diese Funktion gibt einem aus einem String alle Großbuchstaben zurück.
Zum Beispiel: 

```python
get_capital_letters("Ich liebe den BVB") # "IBVB" 
```
Überlege dir, dass die Tests verschiedene Szenarien abfragen.
Erst nachdem du die Tests geschrieben hast, implementiere die Funktion!

<details>
<summary>Lösung</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/ZADHeZo9sJo?si=1DOdbMzqSA-td31w" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<pre><code>import unittest


def get_capital_letters(string):
    return "".join(letter for letter in string if letter.isupper())



class TestCapitalLetters(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(get_capital_letters(""), "")

    def test_normalen_satz(self):
        self.assertEqual(get_capital_letters("Hallo. Ich bin in Kiel."), "HIK")

    def test_only_capital_letters(self):
        string = "ABCEDGEFGHDDSE"
        self.assertEqual(get_capital_letters(string), string)

    def test_no_capital_letters(self):
        self.assertEqual(get_capital_letters("abcdefg"), "")

    def test_correct_return_type(self):
        self.assertIsInstance(get_capital_letters("Hallo du"), str)
</code></pre></details>

### Aufgabe: Wie viele Tests
Wie viele Tests sind im folgenden Programmcode notwendig,
um alle Fälle zu testen? Schreibe die dazugehörigen Tests.

```python
def get_price(age, is_weekend):
    if is_weekend:
        if age < 12:
            return 0
        else:
            return 5
    else:
        if age < 12:
            return 2
        else:
            return 7
```

<details>
<summary>Lösung</summary>

<pre><code>import unittest


class PriceTest(unittest.TestCase):
    def test_get_price_0(self):
        self.assertEqual(get_price(11, True), 0)

    def test_get_price_1(self):
        self.assertEqual(get_price(12, True), 5)

    def test_get_price_2(self):
        self.assertEqual(get_price(11, False), 2)

    def test_get_price_3(self):
        self.assertEqual(get_price(12, False), 7)
</code></pre>
</details>

### Aufgabe: Den Wald vor lauter Bäumen🌶🌶🌶🌶
Diese Aufgabe dient den Selbststudium zu Hause.

Wir wollen nun einen Suchbaum implementieren. Erstelle also eine Klasse `Suchbaum`.
Instanzen der Klasse haben drei Attribute:

* `value`, in dem der Wert des Knotens gespeichert wird.
* `left`, in dem ein anderer Suchbaum oder `None` gespeichert ist.
* `right`, in dem ein anderer Suchbaum oder `None` gespeichert ist.

Weiterhin soll es folgende Funktionen geben:

```python
class Suchbaum:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add(self, new_value):
        """Fügt dem Suchbaum ein neues Element hinzu. Wenn *new_value* < *self.value* ist,
        so wird es dem linken Teilbaum hinzugefügt. Andernfalls dem rechten.
        
        Wenn der jeweilige Teilbaum nicht existiert, wird er erstellt."""
        ...

    def contains(self, element):
        """Prüft, ob das *element* im Suchbaum ist und gibt True zurück, wenn ja."""
        ...

```

Füllen die Funktionsrümpfe, sodass die folgenden Unit-Tests grün werden:

```python
import unittest

class SuchbaumTest(unittest.TestCase):
    def setUp(self):
        self.tree = Suchbaum(3)
        self.tree.add(4)
        self.tree.add(2)
        self.tree.add(1)
        self.tree.add(5)

    def test_contains_0(self):
        self.assertTrue(self.tree.contains(3))

    def test_contains_1(self):
        self.assertTrue(self.tree.contains(1))

    def test_contains_2(self):
        self.assertTrue(self.tree.contains(5))

    def test_contains_3(self):
        self.assertFalse(self.tree.contains(7))

    def test_contains_4(self):
        self.assertTrue(Suchbaum(2).contains(2))

    def test_contains_5(self):
        self.assertFalse(Suchbaum(3).contains(2))


unittest.main()
```

<details>
<summary>Lösung</summary>

<pre><code>class Suchbaum:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add(self, new_value):
        if new_value < self.value:
            if self.left is None:
                self.left = Suchbaum(new_value)
            else:
                self.left.add(new_value)
        else:
            if self.right is None:
                self.right = Suchbaum(new_value)
            else:
                self.right.add(new_value)

    def contains(self, value_to_find):
        if self.value == value_to_find:
            return True

        if self.left is not None and value_to_find < self.value:
            return self.left.contains(value_to_find)

        if self.right is not None and self.value < value_to_find:
            return self.right.contains(value_to_find)

        return False</code></pre>
</details>

