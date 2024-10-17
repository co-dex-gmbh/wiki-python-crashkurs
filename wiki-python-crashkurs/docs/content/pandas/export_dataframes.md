
Es kann vorkommen dass man sein `DataFrame` in einer separaten Datei ausgeben möchte, um sie wo anders weiter zu verwenden. Dazu gibt es einige Möglichkeiten.


## Output to CSV

Mann kann ein DataFrame als eine CSV-Datei exportieren:
```python
import pandas as pd  
# Import data from csv-file inside a dataframe  
df = pd.read_csv("data_file.csv")  
# Replace True with 1 and False with 0 inside the Chrun Binary column  
df["Churn Binary"] = df["Churn"].apply(lambda x: 1 if x==True else 0)  
# Export DataFrame as CSV
df.to_csv("output.csv")
```

## Output to JSON

Mann kann ein DataFrame als eine JSON-Datei exportieren:
```python
import pandas as pd  
# Import data from csv-file inside a dataframe  
df = pd.read_csv("data_file.csv")  
# Replace True with 1 and False with 0 inside the Chrun Binary column  
df["Churn Binary"] = df["Churn"].apply(lambda x: 1 if x==True else 0)  
# Export DataFrame as CSV
df.to_json("output.csv")
```

## Output to HTML

Mann kann ein DataFrame als eine html-Datei exportieren:
```python
import pandas as pd  
# Import data from csv-file inside a dataframe  
df = pd.read_csv("data_file.csv")  
# Replace True with 1 and False with 0 inside the Chrun Binary column  
df["Churn Binary"] = df["Churn"].apply(lambda x: 1 if x==True else 0)  
# Export DataFrame as CSV
df.to_html("output.csv")
```