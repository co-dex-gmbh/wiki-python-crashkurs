
Die [Matplotlib](https://matplotlib.org/contents.html) ist eine umfangreichste Bibliothek, mit deren Hilfe verschiedene Diagrammtypen wie Linien-, Stab- oder Kuchendiagramme, Histogramme, Boxplots, Kontourdiagramme, aber auch dreidimensionale Diagramme und Funktionenplots auf einfache Weise erstellt werden können.

Als erstes muss das Modul importiert werden:
```python
import matplotlib.pyplot as plt
```

# Liniendiagramm

Als Einführungsbeispiel werden wir lernen wie man Liniendiagramme erstellt.
Mit der Methode `plot()` kann man 2D-Grafiken erstellen. Dazu muss man als Parameter eine Liste oder Array mit Werten für die x -und y-Achse übergeben.
Mit der Methode `show()` wird die Grafik sichtbar.

Beispiel:
```python
import matplotlib.pyplot as plt  
# Define the point which have to be connected  
x = [1, 2, 3]  
y = [2, 4, 6]  
# Use the plot method  
plt.plot(x, y)  
# Display the plot  
plt.show()
```

Man kann auch einen Titel zu der Grafik hinzufügen:
```python
import matplotlib.pyplot as plt  
# Define the point which have to be connected  
x = [1, 2, 3]  
y = [2, 4, 6]  
# Set the title  
plt.title("Liniendiagramm")  
# Use the plot method  
plt.plot(x, y)  
# Display the plot  
plt.show()
```

Auch die Beschriftung der beiden Achsen ist möglich:
```python
import matplotlib.pyplot as plt  
# Define the point which have to be connected  
x = [1, 2, 3]  
y = [2, 4, 6]  
# Set the title  
plt.title("Liniendiagramm")  
# Set the title of the axis  
plt.xlabel("x-Werte")  
plt.ylabel("y-Werte")  
# Use the plot method  
plt.plot(x, y)  
# Display the plot  
plt.show()
```

Man kann die Schrittlänge der x -und y-Werte auf den Achsen ändern. 
Dazu verwendet man die Methode `xticks`  und `yticks`.

Zum Beispiel sollen nur Ganzzahlen abgebildet werden:
```python
import matplotlib.pyplot as plt  
# Define the point which have to be connected  
x = [1, 2, 3]  
y = [2, 4, 6]  
# Set the title  
plt.title("Liniendiagramm")  
# Set the title of the axis  
plt.xlabel("x-Werte")  
plt.ylabel("y-Werte")  
# Use the plot method  
plt.plot(x, y)  
# Change the scale of values on the axis  
plt.xticks([0, 1, 2, 3])  # step is set to one unit  
plt.yticks([0, 2, 4, 6, 8, 10])  # step is set to two units  
# Display the plot  
plt.show()
```

Es ist möglich eine Legende für eine bessere Übersicht hinzuzufügen.
Als erstes muss man dem jeweiligen Plot durch den Parameter `label` eine Beschriftung geben. Ich nenne den Plot einfach `2x`. Dann erst kann man die Methode `legend()` verwendet um eine Legende zu erstellen.

Beispiel:
```python
import matplotlib.pyplot as plt  
# Define the point which have to be connected  
x = [1, 2, 3]  
y = [2, 4, 6]  
# Set the title  
plt.title("Liniendiagramm")  
# Set the title of the axis  
plt.xlabel("x-Werte")  
plt.ylabel("y-Werte")  
# Use the plot method  
plt.plot(x, y, label="2x")  
# Change the scale of values on the axis  
plt.xticks([0, 1, 2, 3])  # step is set to one unit  
plt.yticks([0, 2, 4, 6, 8, 10])  # step is set to two units  
# Add a legend  
plt.legend()  
# Display the plot  
plt.show()
```

Das Aussehen der Linie, wie zum Beispiel Farbe, Dicke, Linienart, lässt sich beliebig anpassen. Dazu verwendet man in der `plot()` Methode unterschiedliche Parameter.

Beispiel:
```python
import matplotlib.pyplot as plt  
# Define the point which have to be connected  
x = [1, 2, 3]  
y = [2, 4, 6]  
# Set the title  
plt.title("Liniendiagramm")  
# Set the title of the axis  
plt.xlabel("x-Werte")  
plt.ylabel("y-Werte")  
# Use the plot method  
plt.plot(x, y, label="2x", color="red", linewidth=2, marker=".", markersize=10, markeredgecolor="blue", linestyle="--")  
# Change the scale of values on the axis  
plt.xticks([0, 1, 2, 3])  # step is set to one unit  
plt.yticks([0, 2, 4, 6, 8, 10])  # step is set to two units  
# Add a legend  
plt.legend()  
# Display the plot  
plt.show()
```

Jedoch wird es häufig schnell unübersichtlich wenn man viele Parameter verwendet. Man kann eine sogenannte "shorthand notation" verwenden, welche es uns erlaubt schnell Anpassungen vorzunehmen ohne die Angabe von vielen Parametern.
Die "shorthand notation" sieht folgendermaßen aus: 
`fmt="[color][marker][line]"`

Beispiel:
```python
import matplotlib.pyplot as plt  
# Define the point which have to be connected  
x = [1, 2, 3]  
y = [2, 4, 6]  
# Set the title  
plt.title("Liniendiagramm")  
# Set the title of the axis  
plt.xlabel("x-Werte")  
plt.ylabel("y-Werte")  
# Shorthand notation  
fmt = "r.--"  
# Use the plot method  
plt.plot(x, y, fmt, label="2x",  linewidth=2,  markersize=10, markeredgecolor="blue")  
# Change the scale of values on the axis  
plt.xticks([0, 1, 2, 3])  # step is set to one unit  
plt.yticks([0, 2, 4, 6, 8, 10])  # step is set to two units  
# Add a legend  
plt.legend()  
# Display the plot  
plt.show()
```

Man kann in dem Koordinatensystem selbst Texte platzieren.
Dazu verwendet man die Methode `text()`. Dieser Methode muss man on der folgenden Reihenfolge Parameter übergeben:
- xcoord
- ycoord
- "Your Text"

Beispiel:
```python
import matplotlib.pyplot as plt  
# Define the point which have to be connected  
x = [1, 2, 3]  
y = [2, 4, 6]  
# Set the title  
plt.title("Liniendiagramm")  
# Set the title of the axis  
plt.xlabel("x-Werte")  
plt.ylabel("y-Werte")  
# Shorthand notation  
fmt = "r.--"  
# Use the plot method  
plt.plot(x, y, fmt, label="2x",  linewidth=2,  markersize=10, markeredgecolor="blue")  
# Change the scale of values on the axis  
plt.xticks([0, 1, 2, 3])  # step is set to one unit  
plt.yticks([0, 2, 4, 6, 8, 10])  # step is set to two units  
# Add a legend  
plt.legend()  
# Add Text  
plt.text(1, 6, "Die Funktion ist steigend")  
# Display the plot  
plt.show()
```

Manchmal möchte man das gesamte Aussehen ändern ohne selbstständig jedes Einzelne Element anzupassen. Dazu gibt es sogenannte "style sheets", sie werden durch `plt.style.use('style sheet')` gesetzt. In den Runden Klammern wird dann der Name des jeweiligen "style sheet" gesetzt, die Namen findet man in der Dokumentation.

Beispiel:
```python
import matplotlib.pyplot as plt  
# Define the point which have to be connected  
x = [1, 2, 3]  
y = [2, 4, 6]  
# Styling  
plt.style.use('seaborn-v0_8-dark')  
# print(plt.style.available)  # With this you can check valid style names  
# Set the title  
plt.title("Liniendiagramm")  
# Set the title of the axis  
plt.xlabel("x-Werte")  
plt.ylabel("y-Werte")  
# Shorthand notation  
fmt = "r.--"  
# Use the plot method  
plt.plot(x, y, fmt, label="2x",  linewidth=2,  markersize=10, markeredgecolor="blue")  
# Change the scale of values on the axis  
plt.xticks([0, 1, 2, 3])  # step is set to one unit  
plt.yticks([0, 2, 4, 6, 8, 10])  # step is set to two units  
# Add a legend  
plt.legend()  
# Add Text  
plt.text(1, 6, "Die Funktion ist steigend")  
# Display the plot  
plt.show()
```

# Funktionen plotten 

Die Idee besteht darin, anhand einer Wertetabelle die Funktionen zu plotten.
Bei Funktionen in der Ebene benötigt man die x -und y-Werte.
die x-Werte kann man sich beliebig heraussuchen und die y-Werte werden durch die Funktionsgleichung berechnet.
Am Ende müssen die Werte in separaten Listen vorliegen.

Am Anfang arbeiten wir mit Listen was jedoch sehr unpraktisch ist.
Später werden wir das Modul `numpy` kennen lernen, welche uns optimalere nummerische Berechnungen ermöglichen wird. Dabei wird man einen neuen Datentyp kennen lernen welchen man anstelle der Listen verwendet.

## Normalparabel

```python
import matplotlib.pyplot as plt  
  
# Define x-values  
x = []  
for index in range(-10, 11):  
    x.append(index)  
  
# Define y-values  
y = []  
for index in x:  
    y.append(index ** 2)  
  
# Plot function  
plt.plot(x, y)  
  
plt.show()
```

## Allgemeine Parabel

```python
import matplotlib.pyplot as plt  
# Parameters y=a*x^2 + b*x + c  
a = 0.5  
b = 3  
c = -2  
# Define x-values  
x = []  
for index in range(-20, 22):  
    x.append(index)  
  
# Define y-values  
y = []  
for index in x:  
    y.append(a * (index ** 2) + (b * index) + c)  
  
# Plot function  
plt.plot(x, y)  
  
plt.show()
```

# Größenanpassung 

Es ist möglich die Maße des Bilder anzupassen.
Dazu benötigt man die Methode `figure()`. Innerhalb dieser Methode wird ein Parameter übergeben, womit die Breite und Höhe des Fensters angegeben wird in zoll.

Beispiel:
```python
import matplotlib.pyplot as plt  
  
# Define x-values  
x = []  
for index in range(-10, 11):  
    x.append(index)  
  
# Define y-values  
y = []  
for index in x:  
    y.append(index ** 2)  
# Resize the window  
plt.figure(figsize=(5,3), dpi=300)  # 5x3 inch (5*300=1500px and 3*300=900px)  
  
# Plot function  
plt.plot(x, y)  
  
plt.show()
```


# Plot Speichern

Mit der Methode `savefig()` kann man seinen Plot exportieren.

Beispiel:
```python
import matplotlib.pyplot as plt  
  
# Define x-values  
x = []  
for index in range(-10, 11):  
    x.append(index)  
  
# Define y-values  
y = []  
for index in x:  
    y.append(index ** 2)  
# Resize the window  
plt.figure(figsize=(5,3), dpi=300)  # 5x3 inch (5*300=1500px and 3*300=900px)  
  
# Plot function  
plt.plot(x, y)  
# Export the plot  
plt.savefig("Quadratische_Funktion.png", dpi=300)  
plt.show()
```


## Grundprinzip

Bisher wurden alle Plots einfach in das gerade aktive Plot Fenster gemalt. Für etwas kompliziertere Plots sollte man sich etwas mehr Mühe geben.
Außerdem sollte man sich ein allgemeines Vorgehen zur Anfertigung von Plots aneignen, an welches man sich hält. Ansonsten verliert man schnell die Übersicht weil es sehr viele Wege gibt, die zum Ziel führen.

Die Diagramme in `matplotlib` befinden sich in einem `Figure` Objekt.
Mit `plt.figure()` lässt sich so ein `Figure` Objekt erzeugen. 

Innerhalb des "Figure" befindet sich noch die sogenannte "Axes".
Dies ist das, was man sich unter einem Plot vorstellt, es ist der Bereich des Bildes mit den Daten.  Wenn man ein `Axes` Objekt erstellt, kann man damit dann alle Details des Plots steuern (z.B. Titel, Plot-Typ...).

"Axis" ist die Achse des Diagramms, die mit Achsentitel versehen wird, einen bestimmten Intervall hat und so weiter. Dabei können entweder 2 Achsen oder auch 3 enthalten sein.


![[axes_axis.png]]

## Figure und Axes Objekte

### Figure

Die Methode `plt.figure()` erzeugt ein `Figure` Objekt
```python
fig = plt.figure()
``` 
Durch die `figure()` Methode lassen sich viele Einstellungen vornehmen.
Man kann wichtige Parameter wie `dpi`, `figsize`, `linewidth` und so weiter nutzen, um das Erscheinungsbild zu verändern.

### Axes

Ein "Figure" kann mehrere "Axes" beinhalten, jedoch kann ein "Axes" nur zu einem "Figure" gehören. Mit der Methode `axes()` kann man ein `Axes` Objekt erstellen:
```python
ax = plt.axes()
```

Diese "Axes" gehört dann dem oben zuvor definierten "Figure".
Als Parameter steht normalerweise ein Tupel:  `axes((0.2, 0.2, 0.9, 0.9))`
Die Bedeutung des Tupels ist folgendermaßen zu verstehen:
- Erste Zahl:
  Abstand von der linken Seite des Figure (20%)
- Zweite Zahl:
  Abstand von der unteren Seite des Figure (20%)
- Dritte Zahl:
  Breite des "Axes" von links nach rechts (90%)
- Vierte Zahl:
  Höhe des "Axes" von unten nach oben (90%)

Beispiel:
```python
import matplotlib.pyplot as plt
fig1 = plt.figure()
ax1 = plt.axes((0.2, 0.2, 0.9, 0.9))
ax2 = plt.axes((1.2, 0.2, 0.9, 0.9))
ax3 = plt.axes((0.2, -0.8, 1.9, 0.9))
```


### Die plot() - Methode

Mithilfe der `plot()` kann man "Plots" im Axes-Bereich erstellen.
Dazu muss man die Methode auf einen `Axes` Objekt anwenden.

Beispiel:

```python
import matplotlib.pyplot as plt
import numpy as np 

# Create a figure
fig1 = plt.figure()
# Create axes objects
ax1 = plt.axes((0.2, 0.2, 0.9, 0.9))
ax2 = plt.axes((1.2, 0.2, 0.9, 0.9))
ax3 = plt.axes((0.2, -0.8, 1.9, 0.9))

# Create values for plot
X = np.linspace(-np.pi, np.pi, 25) 
Y1 = np.cos(X) 
Y2 = np.sin(X)
Y3 = X ** 2
Y4 = 2 * X + 1
Y5 = X ** 3 - 1

# Plot in specific axes
p1 = ax1.plot(X, Y1)
p2 = ax2.plot(X, Y2)
p3 = ax3.plot(X, Y3)


# Create one more figure
fig2 = plt.figure()
# Create axes objects
ax4 = plt.axes((0.2, 0.2, 0.5, 0.5))
ax5 = plt.axes((1.2, 0.2, 0.5, 0.5))

# Plot in specific axes
p4 = ax4.plot(X, Y4)
p5 = ax5.plot(X, Y5)

# Zum speichern der beiden Figure Objekte
fig1.savefig("plt1.png", bbox_inches='tight')
fig2.savefig("plt2.png", bbox_inches='tight')
```


### Axis

Mithilfe von `ax.axis()` kann man die Koordinatenachsen eines `Axes` Objekt steuern. Dabei muss es immer unter den jeweiligen Axes-Objekt stehen.
Als Parameter muss man eine Liste übergeben welche wie folgt aussieht:
`[x_min, x_max, y_min, y_max]`

```python
import matplotlib.pyplot as plt
import numpy as np 
# Create a figure
fig1 = plt.figure()

# Create axes objects
ax1 = plt.axes((0.2, 0.2, 0.9, 0.9))
ax2 = plt.axes((1.2, 0.2, 0.9, 0.9))
ax3 = plt.axes((0.2, -0.8, 1.9, 0.9))

# Set axis ticks
ax1.axis([-2, 2, 0, 1])
ax2.axis([-2, 2, -1, 1])
ax3.axis([-5, 5, 0, 5])


# Create values for plot
X = np.linspace(-np.pi, np.pi, 25) 
Y1 = np.cos(X) 
Y2 = np.sin(X)
Y3 = X ** 2

# Plot in specific axes
p1 = ax1.plot(X, Y1)
p2 = ax2.plot(X, Y2)
p3 = ax3.plot(X, Y3)


fig1.savefig("plt1.png", bbox_inches='tight')
```


Man kann sowohl Titel und Achsenbeschriftungen setzen indem man auf das jeweilige `Axes` Objekt zugreift:

```python
import matplotlib.pyplot as plt
import numpy as np 
# Create a figure
fig1 = plt.figure()

# Create axes objects
ax1 = plt.axes((0.2, 0.2, 0.9, 0.9))
ax2 = plt.axes((1.2, 0.2, 0.9, 0.9))
ax3 = plt.axes((0.2, -0.8, 1.9, 0.9))

# Set axis ticks
ax1.axis([-2, 2, 0, 1])
ax2.axis([-2, 2, -1, 1])
ax3.axis([-5, 5, 0, 5])

# Set title
ax1.set_title("Axes1")
ax2.set_title("Axes2")
ax3.set_title("Axes3")

# Set axis labels
ax1.set_xlabel("x-Werte")
ax2.set_xlabel("x-Werte")
ax3.set_xlabel("x-Werte")
ax1.set_ylabel("y-Werte")
ax2.set_ylabel("y-Werte")
ax3.set_ylabel("y-Werte")

# Create values for plot
X = np.linspace(-np.pi, np.pi, 25) 
Y1 = np.cos(X) 
Y2 = np.sin(X)
Y3 = X ** 2

# Plot in specific axes
p1 = ax1.plot(X, Y1)
p2 = ax2.plot(X, Y2)
p3 = ax3.plot(X, Y3)


fig1.savefig("plt1.png", bbox_inches='tight')
```



Jetzt muss man jedoch die Abstände anpassen damit der y-Achsen Titel genug Platz hat. Dazu korrigiert man `ax3 = plt.axes((0.2, -0.8, 1.9, 0.8))`:

### Zusammenfassung

- Vermeide die Nutzung von `plt.plot()`, `plt.title()`, `plt.xlabel()` und so weiter,  ansonsten weiß man später nicht worauf sich die Zeile bezogen hatte
- Verstehe die Terminologie, was ist ein Figure, Axes und Axis
- Lerne nicht alle Parameter auswendig, siehe in der Dokumentation nach

## Aufgaben

{{ task(file="tasks/basic_line_plot.yaml") }}

{{ task(file="tasks/multiple_lines_plot.yaml") }}

{{ task(file="tasks/customizing_plot_appearances.yaml") }}

