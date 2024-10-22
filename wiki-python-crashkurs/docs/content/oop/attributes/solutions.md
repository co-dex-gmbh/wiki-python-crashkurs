
### Aufgabe: Auch Funktionen sind Instanzen

Innerhalb der Funktion, wird ein Attribut `count` von der Funktion (!) angelegt, beschrieben und ausgelesen.
Dann sehen wir immer wechselnden Output:

```python
def say_hello():
    if not hasattr(say_hello, "count"):
        say_hello.count = 0

    say_hello.count += 1

    print(f"Hallo zum {say_hello.count}-ten Mal.")

say_hello() # Hallo zum 1-ten Mal.
say_hello() # Hallo zum 2-ten Mal.
say_hello() # Hallo zum 3-ten Mal.
```
