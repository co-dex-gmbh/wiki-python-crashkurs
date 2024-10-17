Die Berechnung statistischer Größen ist eine häufige Aufgabe bei der Arbeit mit `pandas`. Schließlich wird `pandas` in der Daten Analyse und im Data Science Bereich verwendet. Daher sollte man einige grundlegende statistische Funktionalitäten von `DataFrames` kennen.

Bei den Beispielen wird eine  Datensammlung über Avocados aus dem Jahre 2018 verwendet, hier findet man die dazugehörige CSV-Datei:
[Avocado Daten](../avocado_data.csv)



## Statistik des DataFrames ausgeben

Um die Daten besser zu verstehen, werden einige Funktionalitäten bereitgestellt, um auf statistische Größen zugreifen zu können.
Die Methode `describe()` erstellt eine Zusammenfassung einiger wichtiger statistischer Größen.

Jedoch wird diese Methoden nur auf den Datentyp `int` oder `float` angewendet:
```python
import pandas as pd  
# Import data from csv-file inside a dataframe  
df = pd.read_csv("avocado_data.csv")  
# Summary statistics of data  
print(df.describe())
```

Manchmal möchte man eine Zusammenfassende Statistik nicht nur von `float` 
und `int` Datentypen haben, sondern auch von Objekten. Um `describe()` auf Objekte anzuwenden muss man einen Parameter angeben.
Wenn man den Parameter `include="object"` verwendet werden die Datentypen `int` und `float` ausgeschlossen.

```python
import pandas as pd  
# Import data from csv-file inside a dataframe  
df = pd.read_csv("avocado_data.csv")  
# Summary statistics of data (non int and float values)  
print(df.describe(include="object").to_string())	
```