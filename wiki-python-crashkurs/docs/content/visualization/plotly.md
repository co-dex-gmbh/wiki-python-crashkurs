# Plotly 

Neben Matplotlib und SeaBorn ist Plotly die dritte große Bibliothek für die Visualisierung von Daten in Python. Plotly ist eine interaktive Bibliothek, die es ermöglicht, Diagramme zu erstellen, die interaktiv sind. 

Zwar ist Plotly weniger performant als Matplotlib, bietet dafür jedoch optisch ansprechendere Diagramme und interaktive Charts.


**Beispiel:**

```python
import plotly.express as px
import pandas as pd

# Create a DataFrame
data = {
    "Name": ["John", "Anna", "Peter", "Linda"],
    "Age": [23, 34, 45, 56],
    "City": ["New York", "Berlin", "London", "Paris"]
}

df = pd.DataFrame(data)

# Create a scatter plot
fig = px.scatter(df, x="Name", y="Age", color="City")

# Show the plot
fig.show()
```

Plotly hat auch die Möglichkeit, fortgeschrittene Diagramme wie Karten oder auch 3D-Diagramme zu erstellen.

**Beispiel:**

```python
import plotly.express as px
import pandas as pd

# Create a DataFrame
data = {
    "Name": ["John", "Anna", "Peter", "Linda"],
    "Age": [23, 34, 45, 56],
    "City": ["New York", "Berlin", "London", "Paris"]
}

df = pd.DataFrame(data)

# Create a 3D scatter plot
fig = px.scatter_3d(df, x="Name", y="Age", z="City", color="City")

# Show the plot
fig.show()
```



