# Set

{{ youtube_video("https://www.youtube.com/embed/ypJ-QQQKY2M?si=l69wzgRKPcd69_l0") }}

Sets (deutsch: _Mengen_ ) sind listen sehr ähnlich, sie haben aber zwei für uns wichtige unterschiede:

* Jedes Element in der Liste darf nur ein mal auftauchen.
* Jedes Mengen haben keine Ordnung, das heißt, wir können nicht auf das `x`-te Element zugreifen.
* Sets werden mit geschweifen Klammern definiert, statt mit eckigen.

Ein Anwendungsfall für Sets ist das finden einmaliger Elementen in Listen.

```python
my_list = [1, 1, 2, 1, 2, 3] # (1)!
my_set = set(my_list) # (2)!
print(my_set) # (3)!
```

1. Liste `my_list` wird erstellt. Manche Elemente sind doppelt und dreifach vorhanden.
2. Aus der Liste wird ein Set (Menge) gemacht.
3. In der Liste sind nun alle Elemente einmalig.

{{ python_tutor("""my_list = [1, 1, 2, 1, 2, 3]
my_set = set(my_list)
print(my_set)""") }}

# Tupel

{{ youtube_video("https://www.youtube.com/embed/YAP_SKX6VMA?si=Hajpf0Xb9FCH5hht") }}

Tupel sind fast identisch zu listen. Hier sind die für uns entscheidenden Unterschiede:

* Tupel werden mit runden `()` statt mit eckigen Klammern `[]` definiert.
* Tupel lassen sich im Nachhinein nicht mehr ändern.

```python
my_tuple = (1, 2, 3) # (1)!
print(f"Erstes Element: {my_tuple[0]}") # (2)!

my_tuple[0] = 4 # (3)! 
```

1. Ein Tupel wird hier definiert.
2. Der Zugriff auf die Elemente des Tupels sieht genau so aus, wie bei Listen.
3. Hier kommt es bei der Ausführung zu einem Fehler, denn der Inhalt eines Tupels kann im Nachhinein nicht mehr geändert werden. Auch Methoden wie `append` exitieren nicht bei Tupeln.

# Dictionary

{{ youtube_video("https://www.youtube.com/embed/m2hu4iQwHBY?si=uJIu3hgW7RSkJjcX") }}

Dictionaries sind eine häufig verwendete Datenstruktur, die man als eine Liste mit speziellen Zugriffsmöglichkeiten betrachten kann.
Bei einer Liste greift man auf die Werte immer über Zahlen zu. Bei einem Dictionary werden auf die Werte (Values) über 
vorher definierte Schlüssel (Keys) zugegriffen.

Wir können uns also vorstellen, dass die Schubladen in unseren Schränken nicht durchnummeriert sind, sondern eine Aufschrift haben.

<!-- Laden der model-viewer Bibliothek -->
<script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>
<script nomodule src="https://unpkg.com/@google/model-viewer/dist/model-viewer-legacy.js"></script>

<div class="grid cards" markdown>

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

<div markdown>
<p style="text-align:center;" markdown>**Dictionaries**</p>

---

<model-viewer 
    src="../dict.glb" 
    alt="Ein 3D-Modell"
    camera-orbit="15deg 80deg 2m" 
    disable-zoom 
    camera-controls
    style="width: 100%; height: 300px;">
</model-viewer>
```{ .python }
my_dict = {
    'Hunde': 5,
    'Katzen': 8,
    'Hühner': 5,
    'Hähne': 1,
    'Schweine': 0,
    'Kühe': 80
}

print(my_dict['Hunde']) # (1)!

my_dict['Hunde'] = 6 # (2)!
```

1. Über den Schlüssel `Hunde` wird auf das Value `#!python 5` zugegriffen.
2. Ein neuer Value `#!python 6` wird beim Schlüssel `Hunde` gespeichert. 
</div>
</div>