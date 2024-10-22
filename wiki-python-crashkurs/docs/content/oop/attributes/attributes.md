# Attribute

{{ youtube_video("https://www.youtube.com/embed/Wa0DjW0Zn4Y?si=KNRedy36pi8kcgsH")}}

Bisher hatten unsere Instanzen noch keine Eigenschaften. Eigenschaften werden auch als **Attribute** bezeichnet.

## Dynamische Attribute

Wir können unseren Instanzen händisch Attribute hinzufügen:

```python
class Roboter:
    pass


x = Roboter()
y = Roboter()

x.baujahr = 1990
x.name = 'Marvin'
y.baujahr = 2005
y.name = 'Justin'

print(f'{x.name} ist {2024 - x.baujahr} Jahre alt')
print(f'{y.name} ist {2024 - y.baujahr} Jahre alt')
```


Beachte, dass jede Instanz ihre eigenen Attribute hat. Da wir den Instanzen erst nach deren Erstellung
Attribute hinzugefügt haben, nennt man diese auch _dynamische Attribute_. Wir werden später sehen, wie man
schon bei der Erzeugung einer Instanz die Attribute festlegen kann.

Wenn wir alle Attribute einer Instanz ansehen wollen, können wir das mit `x.__dict__` tun:

```python
class Roboter:
    pass


x = Roboter()
y = Roboter()

x.baujahr = 1990
x.name = 'Marvin'
y.baujahr = 2005
y.name = 'Justin'

print(x.__dict__)
print(y.__dict__)
```

{{ task(file="tasks/oop_attribute_1.yaml") }}

{{ task(file="tasks/oop_attribute_2.yaml") }}

{{ task(file="tasks/oop_attribute_3.yaml") }}

## Klassenattribute

{{ youtube_video("https://www.youtube.com/embed/_YxyRGvUcpI?si=VqCvQuoxt8ktM3IX")}}

Wir können auch der Klasse Attribute hinzufügen.
Lassen den folgenden Code ausführen, in der das Klassenattribut `marke`
hinzugefügt wird:

```python
class Roboter:
    marke = 'VW'

x = Roboter()
y = Roboter()

x.name = 'Marvin'

print(x.marke)
print(y.marke)
print(Roboter.marke)

print(f'Attribute von x: {x.__dict__}')
print(f'Attribute von y: {y.__dict__}')
```


* Alle Instanzen der Klasse können auf das Klassenattribut zugreifen.
* Man kann über die Klasse auf das Klassenattribut zugreifen.
* Das Klassenattribut ist kein Attribut der Instanz.

Wir können das Klassenattribut auch dynamisch setzen:

```python
class Roboter:
    pass
    
Roboter.marke = 'VW'

...
```

In anderen Programmiersprachen sagt zu Klassenattributen "statische Felder" und zu Attributen der Instanz "Felder".
Die Möglichkeit Attribute oder Klassenattribute dynamisch nach Instanziierung hinzuzufügen, 
gibt es jedoch nicht bei allen Programmiersprachen.


{{ task(file="tasks/oop_attribute_4.yaml") }}

{{ task(file="tasks/oop_attribute_5.yaml") }}

{{ task(file="tasks/oop_attribute_6.yaml") }}
