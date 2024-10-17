
Eine typische Aufgabe bei der Arbeit mit `DataFrames` ist es neue Daten hinzuzufügen um das `DataFrame` zu erweitern, oder auch bestimmte Daten entfernen.



## Spalten entfernen (dropping columns)

Manchmal möchte man bestimmte Spalten entfernen. Dazu verwendet man die Methode `drop()`. Innerhalb der Muss man durch den Parameter `axis` festlegen ob entweder eine Reihe `axis=0` oder eine Spalte `axis=1` angesprochen werden soll

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
print(df)  
# Drop one column
print(df.drop(labels="Discount", axis=1))
```

Wenn man jetzt jedoch durch `print(df)` das `DataFrame` ausgibt, sieht man keine Änderung. Damit die Änderung auf das aktuelle `DataFrame` vorgenommen wird, muss man den `inplace=True` Parameter verwenden

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
print(df)  
# Drop one column and save the change
df.drop(labels="Discount", axis=1, inplace=True)  
print(df)
```

Häufig möchte man Änderungen am `DataFrame` vornehmen und dabei soll diese Änderung gespeichert werden. Hierzu muss man  den Parameter `inplace` verwenden, er aktualisiert das `DataFrame`.

## Zeilen entfernen (dropping rows)

Ähnlich wie bei der Entfernung von Spalten kann man auch Zeilen entfernen. Mit dem unterschied dass man nun den Parameter `axis` nicht angeben muss, da er standartmäßig auf 0 gesetzt ist. Dem Parameter `labels` muss man den Index, welcher die Zeile repräsentiert, übergeben. Der Index kann dabei ein Integer sein oder auch ein keyword.

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
print(df) 
# Drop two rows
df.drop(labels=[2, 6], axis=0, inplace=True)  
print(df)
```

## Spalte erstellen 

Man kann beliebig viele Spalten zu dem aktuellen `DataFrame` hinzufügen und die Werte aus anderen Spalten ausrechnen.

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
print(df)  
# Create a new column and calculate the values df["Total cost"] = 1250 + df["Fee"]  
print(df)
```

## Zeile erstellen

Durch die Nutzung der `loc` Methode kann man eine Zeile am Ende des `DataFrames` einsetzen.

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
print(df)  
# Create a list with data, which should be appended to df  
row_to_add = ["C++", 21000, "33days", None]  
# Append list to df  
df.loc[len(df)] = row_to_add  
print(df)
```

## Werte ändern mit "at"

Durch die `at` Methode kann man durch Angabe des Index und des Spaltennamens auf einen Wert zugreifen und ihn ändern.

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
print(df)  
df.at[5, "Fee"] = 35000  
print(df)
```

## Werte ändern mit "iat"

Ähnlich wie bei der `at` Methode kann man im `DataFrame` einen Wert ändern mit dem unterschied dann man nur Integer verwendet um die Position des Wertes anzugeben. Die erste Zahl gibt die Zeile an und die zweite Zahl die Spalte.

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
print(df)  
df.iat[3, 2] = "53days"  
print(df)
```