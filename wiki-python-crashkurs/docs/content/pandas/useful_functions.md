Hier werden einige häufig verwendeten Funktionalitäten aufgetragen.
Bei der Arbeit mit `DataFrames` kommen sie häufig zum Einsatz um ein gegebenes Problem zu lösen.

## Daten gruppieren

Mit der Methode `groupby()` kann man die Daten anhand einiger Kriterien in gruppen aufgeteilt werden und auch Funktionen auf diese Gruppen angewendet werden

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
# Group DataFrame by "Courses and calculate sum on "Fee" and "Discount" columns  
df = df.groupby(["Courses"]).sum()  
print(df)  
# Display type of grouped DataFrame  
print(type(df))
```

## DataFrame sortieren

Mit der Methode `sort_values()` lässt sich eine DataFrame sortieren.

Zum Beispiel das Sortieren einer Spalte:
```python
import pandas as pd  
  
df = pd.read_csv("avocado_data.csv")  
print(df.head().to_string())  
print(df.head().sort_values("Account length"))
```

Wenn man innerhalb der Methode `sort_values()` das Argument `ascending=False` setzt, werden die Daten in die andere Richtung sortiert:
```python
import pandas as pd  
  
df = pd.read_csv("avocado_data.csv")  
print(df.head().to_string())  
print(df.head().sort_values("Account length", ascending=False))
```

Es ist auch möglich mehrere Spalten auf einmal zu sortieren. Dazu muss man der Methode `sort_values()` eine Liste mit den zu sortierenden Spalten übergeben:
```python
import pandas as pd  
  
df = pd.read_csv("avocado_data.csv")  
print(df.head().to_string())  
print(df.head().sort_values(["Account length", "Customer service calls"], ascending=False))
```

Auch die Übergabe des Arguments `ascending` kann durch eine Liste erfolgen, damit jede Spalte unterschiedlich sortiert wird:
```python
import pandas as pd  
  
df = pd.read_csv("avocado_data.csv")  
print(df.head().to_string())  
print(df.head().sort_values(["Account length", "Customer service calls"], ascending=[False, True]))
```

## Nutzung der "apply" Methode

Man kann anstelle einer "for"-Loop auch die `apply()` Methode verwenden:
```python
import pandas as pd  
  
exam_data = {  
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],  
    'score': [12.5, 9, 16.5, "nan", 9, 20, 14.5, "nan", 8, 19],  
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],  
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}  
  
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']  
  
df = pd.DataFrame(exam_data, index=labels)  
df["Name UpperCase"] = df["name"].apply(str.upper)  
  
print(df)
```

Hier wird als erstes eine neue Spalte mit den Namen `Name UpperCase` erstellt. Anschließend wird in jeder Zeile dieser Spalte der Name aus der "name"-Spalte gespeichert, jedoch unter der Anwendung der `upper` Methode.

## Funktionen auf Spalten/Zeilen anwenden

Mittels der Methode `agg` kann man benutzerdefinierte- oder built-in Funktionen auf Spalten oder Zeilen anwenden. Am häufigsten erstellt man eine eigene Funktion und möchte sie auf eine Zeile anwenden:
```python
import pandas as pd  
  
df = pd.read_csv("data_file.csv")  
print(df.head(50).to_string())  
  
  
def average_account_length(column):  
    return column.sum() / column.count()  
  
  
average_account_length = df["Account length"].agg(average_account_length)  
print(f"The average account legth is: {average_account_length}")
```

Es ist auch möglich die erstellte Funktion auf mehrere Spalten anzuwenden:
```python
import pandas as pd  
  
df = pd.read_csv("data_file.csv")  
print(df.head(50).to_string())  
  
  
def average_calculation(column):  
    return column.sum() / column.count()  
  
  
average_accLength_and_totalDayMinutes = (df[["Account length", "Total day minutes"]].agg(average_calculation))  
print(f"The average account length is: {average_accLength_and_totalDayMinutes[0]} and the average total day minutes are: {average_accLength_and_totalDayMinutes[1]}")
```

Das Anwenden mehrerer Funktion ist auch möglich. Dazu muss man der Methode `agg()` eine Liste mit Funktionen übergeben:
```python
import pandas as pd  
import numpy as np  
  
df = pd.read_csv("data_file.csv")  
print(df.head(50).to_string())  
  
  
def average_calculation(column):  
    return column.sum() / column.count()  
  
  
averageAndmedian_accLength_and_totalDayMinutes = (df[["Account length", "Total day minutes"]].agg([average_calculation, np.median]))  
print(averageAndmedian_accLength_and_totalDayMinutes)
```
