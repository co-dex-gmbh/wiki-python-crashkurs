# Listen

{{ youtube_video("https://www.youtube.com/embed/lyhlE_L7Cgg?si=ldzvXK78KMxV3eVY") }}

Derzeit können wir in einer Variablen genau einen Wert speichern.

Wir werden nun Möglichkeiten kennenlernen, wie wir in einer Variable eine große Menge von Daten speichern können.

Die wichtigste Möglichkeit zum Speichern großer Datenmengen in einer Variable sind **Listen**.

Eine Liste kann man sich vorstellen, wie eine Variable mit mehrere Schubladen und diese Schubladen sind
durchnummeriert. Die Nummerierung startet mit `0`, geht dann weiter zu `1`, weiter zu `2` usw.

Wir können eine Liste definieren, indem wir die Elemente, die gespeichert werden sollen in eckige Klammern (`[...]`)
schreiben:

```
trinkgeld = [70, 60, 15, 15, 0, 100, 0]
```

Um nun auf die Elemente zuzugreifen geben wir den schreiben wir nach dem Variablennamen in eckigen Klammern,
welchen Eintrag wir haben möchten.

```python
print(trinkgeld[0]) # (1)!
```

1. Konsolenausgabe: `70`

{{ python_tutor("""trinkgeld = [70, 60, 15, 15, 0, 100, 0]
print(f'Montag: {trinkgeld[0]}')
print(f'Dienstag: {trinkgeld[1]}')
print(f'Mittwoch: {trinkgeld[2]}')
print(f'Donnerstag: {trinkgeld[3]}')
print(f'Freitag: {trinkgeld[4]}')
print(f'Samstag: {trinkgeld[5]}')
print(f'Sonntag: {trinkgeld[6]}')
""") }}

Andererseits können wir über die Notation Werte überschreiben:

```python
trinkgeld[0] = 10 # (2)!
print(trinkgeld[0]) # (1)!
```

1. Konsolenausgabe: `10`
2. Schreibe `10` an die erste Stelle (Index `0`) der Liste.

{{ python_tutor("""supremes = ['Diana', 'Mary', 'Florence']
supremes[2] = 'Cindy'
print(supremes)
""") }}

<!-- Laden der model-viewer Bibliothek -->
<script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>
<script nomodule src="https://unpkg.com/@google/model-viewer/dist/model-viewer-legacy.js"></script>

<div class="grid cards" markdown>

<div markdown>
<p style="text-align:center;" markdown>**Variablen**</p>

---

<model-viewer 
    src="../var.glb" 
    alt="Ein 3D-Modell"
    camera-orbit="-15deg 80deg 2m" 
    disable-zoom 
    camera-controls
    style="width: 100%; height: 300px;">
</model-viewer>
```{ .python }
my_var = 5

print(my_var) # (1)!

my_var = 6 # (2)!
```

1. Zugriff direkt über den Namen der Variablen.
2. Überschreiben der Variablen. 
</div>

<div markdown>
<p style="text-align:center;" markdown>**Listen**</p>

---

<model-viewer 
    src="../list.glb" 
    alt="Ein 3D-Modell"
    camera-orbit="-15deg 80deg 2m" 
    disable-zoom 
    camera-controls
    style="width: 100%; height: 300px;">
</model-viewer>
```{ .python }
my_list = [5, 8, 5, 1, 0,80]

print(my_list[0]) # (1)!

my_list[0] = 10 # (2)!
```

1. Zugriff auf Element über den Index `#!python 0`.
2. Überschreiben des Elements an dem Index `#!python 0`.

</div>
</div>

!!! bug "Listen **niemals** `list` nennen!"

    Der Variablenname einer Liste (oder sonst irgendeines Objektes), darf **niemals** `list` heißen.

    Dies würde zu einer Überschreibung des `list`-Konstruktors führen und ggf. den Rest des Pythonprogramms zerstören :fontawesome-solid-skull:.

    `list` isthier keine Ausnahme. [Hier findest du noch eine Liste aller Build-In-Functions](https://docs.python.org/3/library/functions.html), die man nicht als Variablennamen verwenden soll.


{{ task(file="tasks/listen_lesen_0.yaml") }}

{{ task(file="tasks/listen_definieren_0.yaml") }}

{{ task(file="tasks/listen_definieren_1.yaml") }}

{{ task(file="tasks/listen_manipulieren.yaml") }}

