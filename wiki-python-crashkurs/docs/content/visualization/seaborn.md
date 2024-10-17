# Seaborn

Seaborn ist eine Python-Bibliothek, die auf Matplotlib basiert und die Erstellung von ansprechenden und informativen Diagrammen erleichtert. Seaborn bietet eine Vielzahl von Diagrammtypen und Stilen, die es ermöglichen, Daten auf einfache Weise zu visualisieren.

Die Grafiken von Seaborn ähneln denen von ggplot2, einer beliebten Visualisierungsbibliothek in R.

Ein Plot in Seaborn basiert in der Regel auf einem DataFrame, das die Daten enthält, die visualisiert werden sollen. Die Daten werden dann in einem Plot dargestellt, der auf den Daten basiert.

**Beispiel:**

```python
import seaborn as sns
import pandas as pd

# Create a DataFrame
data = {
    "Name": ["John", "Anna", "Peter", "Linda"],
    "Age": [23, 34, 45, 56],
    "City": ["New York", "Berlin", "London", "Paris"]
}

df = pd.DataFrame(data)

# Create a scatter plot
sns.scatterplot(data=df, x="Name", y="Age", hue="City")

# Show the plot
plt.show()
```

In diesem Beispiel haben wir ein Streudiagramm erstellt, das die Namen und das Alter der Personen aus dem DataFrame `df` anzeigt. Die Punktfarben werden basierend auf der Stadt der Person eingefärbt.

Seaborn bietet eine Vielzahl von Diagrammtypen und Stilen, die es ermöglichen, Daten auf einfache und ansprechende Weise zu visualisieren. Es ist eine leistungsstarke Bibliothek für die Datenvisualisierung in Python.

Außerdem gibt es in Seaborn nützlich Funktionen, um sich einen ersten Überblick zu den Daten zu verschaffen. Zum Beispiel können wir in Seaborn die Funktion `pairplot()` verwenden, um Beziehungen zwischen den numerischen Spalten eines DataFrames zu visualisieren.

**Beispiel:**

```python
import seaborn as sns
import pandas as pd

# Load a dataset
df = sns.load_dataset("iris")

# Create a pairplot
sns.pairplot(df)

# Show the plot
plt.show()
```

In diesem Beispiel haben wir ein Paardiagramm erstellt, das Beziehungen zwischen den numerischen Spalten des Iris-Datensatzes visualisiert. Dies kann nützlich sein, um Muster und Beziehungen zwischen den Variablen zu erkennen.