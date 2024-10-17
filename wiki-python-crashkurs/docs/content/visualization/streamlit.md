# Streamlit

Wenn Sie kleine interaktive Dashboards erstellen möchten, kann Streamlit eine gut Wahl sein. Stramlit ist eine Open-Source-Bibliothek, die es ermöglicht, Webanwendungen mit Python zu erstellen. Streamlit ist einfach zu bedienen und erfordert nur wenige Zeilen Code, um eine Webanwendung zu erstellen.

**Beispiel**

```python
import streamlit as st
import pandas as pd
import numpy as np

# Create a simple dataframe
data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=['a', 'b', 'c']
)

# Display the dataframe
st.write(data)

# Create a line chart
st.line_chart(data)
```

Einen Überblick zu den Funktionen von Streamlit finden Sie [hier](https://docs.streamlit.io/library).