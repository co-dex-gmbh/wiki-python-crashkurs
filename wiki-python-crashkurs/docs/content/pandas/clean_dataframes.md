
Um die Qualität eines `DataFrames` sicherzustellen muss man einige Punkte beachten:
- Was macht man mit nicht vorhandenen Werten?
- Sind Duplikate vorhanden?


## Nicht vorhandene Werte in Zeilen entfernen

Häufig hat man innerhalb des `DataFrames` Werte, welche nicht vorhanden sind bzw. Null sind. Das Ziel ist es dann Zeilen welche keinen Wert haben zu 
entfernen (dropp rows).

Die Methode `isnull()` gibt ein `DataFrame` zurück, wo alle Werte welche nicht vorhanden sind mit `True` ersetzt werden und alle Werte die vorhanden 
sind mit `False`.


Beispiel:
```python
import pandas as pd  
  
technologies = {  
  
    'Courses': ["Spark", "PySpark", "Hadoop", "Python", "Pandas", "Hadoop", "Spark", "Python", "NA"],  
    'Fee': [22000, 25000, 23000, 24000, 26000, 25000, 25000, 22000, 1500],  
    'Duration': ['30days', '50days', '55days', '40days', '60days', '35days', '30days', '50days', '40days'],  
    'Discount': [1000, 2300, 1000, 1200, 2500, None, 1400, 1600, 0]  
}  
# Create DataFrame  
df = pd.DataFrame(data=technologies)  
filtered = df.isnull()  
print(filtered)
```

Es wäre jedoch interessanter zu sehen wie viele Werte nicht Vorhanden bzw. Null sind. Man müsste also alle `True` Werte lesen. Dazu verwendet man die Methode `sum()`:
```python
import pandas as pd  
  
technologies = {  
  
    'Courses': ["Spark", "PySpark", "Hadoop", "Python", "Pandas", "Hadoop", "Spark", "Python", "NA"],  
    'Fee': [22000, 25000, 23000, 24000, 26000, 25000, 25000, 22000, 1500],  
    'Duration': ['30days', '50days', '55days', '40days', '60days', '35days', '30days', '50days', '40days'],  
    'Discount': [1000, 2300, 1000, 1200, 2500, None, 1400, 1600, 0]  
}  
# Create DataFrame  
df = pd.DataFrame(data=technologies)  
filtered = df.isnull()  
print(filtered.sum())
```

Um jetzt das `DataFrame` zu updaten, damit die nicht vorhanden Werte entfernt sind (dropp missing values), nutzt man die `dropna()` Methode.
Innerhalb der `dropna()` Methode wird ein Parameter angegeben, welcher Aussagt welche Werte gelöscht werden sollen. In unserem Fall alles was `True` ist, weil die nicht vorhanden Werte mit `True` gekennzeichnet wurden:
```python
import pandas as pd  
  
technologies = {  
  
    'Courses': ["Spark", "PySpark", "Hadoop", "Python", "Pandas", "Hadoop", "Spark", "Python", None],  
    'Fee': [22000, 25000, 23000, 24000, 26000, 25000, 25000, 22000, 1500],  
    'Duration': ['30days', '50days', '55days', '40days', '60days', '35days', '30days', '50days', '40days'],  
    'Discount': [1000, 2300, 1000, 1200, 2500, None, 1400, 1600, 0]  
}  
# Create DataFrame  
df = pd.DataFrame(data=technologies)  
print(df)  
print("----------------")  
df.dropna(inplace=True)  
print(df)
```

## Duplikate entfernen

Häufig möchte man Duplikate innerhalb einer Spalte entfernen:
```python
import pandas as pd  
  
technologies = {  
  
    'Courses': ["Spark", "PySpark", "Hadoop", "Python", "Pandas", "Hadoop", "Spark", "Python", None],  
    'Fee': [22000, 25000, 23000, 24000, 26000, 25000, 25000, 22000, 1500],  
    'Duration': ['30days', '50days', '55days', '40days', '60days', '35days', '30days', '50days', '40days'],  
    'Discount': [1000, 2300, 1000, 1200, 2500, None, 1400, 1600, 0]  
}  
# Create DataFrame  
df = pd.DataFrame(data=technologies)  
print(df)  
df.drop_duplicates(subset="Courses", inplace=True)  
print(df)
```