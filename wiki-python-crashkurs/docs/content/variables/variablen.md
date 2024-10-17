# Variablen

{{ youtube_video("https://www.youtube.com/embed/Idbd0z0PkIg?si=3jWvVpqaqB5BvJO4", title="Einführung in Variablen") }}

In Python können wir **Informationen in Variablen speichern**.

Man kann sich so eine Variable vorstellen, wie einen beschrifteten Schuhkarton in einem Schrank. 
In so einen Schuhkarton kann man zu einem beliebigen Zeitpunkt:

* etwas hineintun; 
* anschauen, was drin ist;
* durch etwas anderes austauschen.

Genauso ist es auch bei Variablen.

Schauen wir uns dazu den folgenden Code an:

```python
a = 1 # (1)!
print(a) # (4)!

a = 2 # (2)!
print(a) # (5)!

a = a + 3 # (3)!
print(a) # (6)!
```

1. In der neuen Variablen `#!python a` ist initial der Wert `#!python 1` gespeichert.
2. In der Variablen `#!python a` ist nun der Wert `#!python 2` gespeichert. Die `#!python 1` wird vergessen.
3. Der Wert von `#!python a` wird zunächst ausgelesen und dann 3 dazuaddiert. Das Ergebnis (`#!python 5`) wird dann wieder in `#!python a` gespeichert.
4. Der Wert der Variablen `#!python a` wird ausgelesen und in mit der `#!python print`-Funktion auf der Konsole ausgegeben.
5. Der Wert der Variablen `#!python a` wird ausgelesen und in mit der `#!python print`-Funktion auf der Konsole ausgegeben.
6. Der Wert der Variablen `#!python a` wird ausgelesen und in mit der `#!python print`-Funktion auf der Konsole ausgegeben.

Wir können uns das obige Beispiel nun noch einmal im Debugger ansehen:

{{ python_tutor("""a = 1
print(a)

a = 2
print(a)

a = a + 3
print(a)""") }}

!!! danger "'"Das Gleichheitszeichen `#!python =` bedeutet nicht <del>"ist gleich"</del> sondern "ist **nun**"!"
    
    Das Gleichheitszeichen `#!python =` in Python ist der sogenannte **Zuordnungsoperator**.
    Er dient dazu, Inhalte in einer Variablen zuzuordnen.
    Auf der linken Seite des `#!python =` steht immer die Variable, in die wir etwas speichern wollen und auf der 
    rechten Seite, _was_ wir in der Variablen speichern wollen.

    Am besten man ließt man Zeilen wie `#!python a = 2` als: **"`#!python a` hat nun den Wert `#!python 2`."**

    Es ist nicht der Gleichheitsoperator, wie wir in aus der Mathematik kennen.

<p style="text-align:center;" markdown>
:fontawesome-solid-box: :fontawesome-solid-box: :fontawesome-solid-box:
</p>

{{ task(file="tasks/variablen_anlegen_1.yaml") }}

{{ task(file="tasks/variablenbefüllung_voraussagen_1.yaml") }}

{{ task(file="tasks/variablenbefüllung_voraussagen_2.yaml") }}

{{ task(file="tasks/variablenbefüllung_voraussagen_3.yaml") }}

{{ task(file="tasks/variablenbenennung.yaml") }}

{{ task(file="tasks/variablen_vertauschen.yaml") }}

{{ task(file="tasks/marsgewicht.yaml") }}


