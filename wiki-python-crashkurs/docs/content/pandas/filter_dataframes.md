
Oft möchte man ein `DataFrame` nach bestimmten Bedingungen filtern, dies ist sehr einfach und lässt viel Spielraum. Dazu verwendet man die booleschen Operationen, um seine Aufgaben zum Filtern, zu bewerkstelligen.

Bei den Beispielen wird eine  Datensammlung über Avocados aus dem Jahre 2018 verwendet, hier findet man die dazugehörige CSV-Datei:
[Avocado Daten](../avocado_data.csv)



## Filtern mit isin()

Durch die Methode `isin()` kann man Daten Filtern, indem man der Methode eine Liste übergibt, welche Werte enthält, die gefiltert werden sollen.

Beispiel:
```python
import pandas as pd  
  
df = pd.read_csv("avocado_data.csv")  
print(df.head().to_string())  
filtered = df["type"].isin(["conventional"])  
print(df[filteres].to_string())
```

Das wäre die Alternative ohne die Nutzung von `isin()`:
```python
import pandas as pd  
  
df = pd.read_csv("avocado_data.csv")  
print(df.head().to_string())  
filtered = df["type"] == "conventional"  
print(df[filtered])
```

Als erstes erstellt man eine Variable wo nur `boolsche` Werte drine sind. Anschließend setzt man diese Wahrheitswerte in das `DataFrame` ein um die Werte mit `False` auszublenden.