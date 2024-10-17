Sehr häufig möchte man nicht das ganze `DataFrame` lesen, sondern nur bestimmte Teile wie z.B. Spalten, Reihen, die ersten oder letzten fünf Werte und so weiter.

Bei den Beispielen wird eine  Datensammlung über Avocados aus dem Jahre 2018 verwendet, hier findet man die dazugehörige CSV-Datei:
[Avocado Daten](https://github.com/erkansirin78/datasets/blob/master/avocado.csv)






## DataFrame anzeigen/ausgeben

Mit der bereits bekannten Funktion `print()` lässt sich ein `DataFrame` ausgeben:

Beispiel:
```python
import pandas as pd  
  
df = pd.read_csv("avocado_data.csv")  
print(df)
```

Wenn man eine IDE wie Pycharm verwendet, kann es sein dass die gesamten Daten in der Konsole nicht ausgegeben werden. Die Ursache dafür liegt in einem zu großen `DataFrame`, weswegen in der Konsole kein Platz für die Anzeige vorhanden ist. 

Um die Ausgabe zu ermöglichen verwendet man häufig die Methode `to_string()`, um das `DataFrame` in den Datentyp String zu konvertieren.
Dadurch kann man manchmal das gesamte `DataFrame` in der Konsole darstellen:

Beispiel:
```python
import pandas as pd  
  
df = pd.read_csv("avocado_data.csv")  
# Convert DataFrame in string  
df_as_string = df.to_string()  
# Display the converted DataFrame  
print(df_as_string)  
# Display the type of the convertet DataFrame  
print(type(df_as_string))
```

Falls man Jupyter Notebook verwendet, kann man durch die folgenden Einstellungen das gesamte `DataFrame` ausgeben lassen:

```python
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
```

## Die ersten fünf Zeilen ausgeben

Unter der Nutzung der `head()` Methode zusammen mit der `print()` Funktion, lassen sich die ersten fünf Zeilen ausgeben.

Beispiel:
```python
import pandas as pd  
# Import data from csv-file inside a dataframe  
df = pd.read_csv("avocado_data.csv")  
# Read first five rows  
print(df.head())  
# Read first ten rows  
print(df.head(10))
```

## Die letzten fünf Zeilen ausgeben

Genau wie die `head()` Methode funktioniert auch die `tail()` Methode nur eben mit den letzten fünf Zeilen.

Beispiel:
```python
import pandas as pd  
# Import data from csv-file inside a dataframe  
df = pd.read_csv("avocado_data.csv")  
#  bottom five forws  
print(df.tail())
#  bottom ten forws  
print(df.tail(10))
```

## Spaltennamen ausgeben

Häufig sind die `DataFrames` so groß das man nicht alle Spalten sieht wenn man `print()`, `head()` oder `tail()` verwendet.
Deswegen ist es praktisch, wenn man nur die Spaltennamen ausgibt, um sich einen Überblick zu verschaffen.

Dazu benötigt man das Attribut `columns`.

Beispiel:
```python
import pandas as pd  
# Import data from csv-file inside a dataframe  
df = pd.read_csv("avocado_data.csv")  
# Read the column names  
print(df.columns)
```

## Datentyp ausgeben

Man kann auch den Datentyp auslesen lassen, indem man das Attribut `dtypes` verwendet. Dadurch wird eine `Serie` zurückgegeben.

Beispiel:
```python
import pandas as pd  
# Import data from csv-file inside a dataframe  
df = pd.read_csv("avocado_data.csv")  
# Read the datatypes of the dataframe  
print(df.dtypes)
```

In Pandas werden folgende Datentypen unterschieden:

| Pandas dtype  | Python type  | Usage                                        |
| ------------- | ------------ | -------------------------------------------- |
| object        | str or mixed | Text or mixed numeric and non-numeric values |
| int64         | int          | Integer numbers                              |
| float64       | float        | Floating point numbers                       |
| bool          | bool         | True/False values                            |
| datetime64    | NA           | Date and time values                         |
| timedelta[ns] | NA           | Differences between two datetimes            |
| category      | NA           | Finite list of text values                   |

## Spalte/Spalten ausgeben

Man kann sich eine Spalte ausgeben lassen, indem man in eckigen Klammern den Spaltennamen angibt.

Beispiel:
```python
import pandas as pd  
# Import data from csv-file inside a dataframe  
df = pd.read_csv("data_file.csv")  
# Access specific column  
print(df["State"])
```

Eine weitere Möglichkeit bietet der Punktoperator. Den selben Effekt wie im obigen Beispiel können wir erzielen indem wir nach dem Punktoperator der Spaltennamen angeben. Aber Achtung, bei Leerzeilen ist diese Methode nicht möglich.

Beispiel:
```python
import pandas as pd  
# Import data from csv-file inside a dataframe  
df = pd.read_csv("data_file.csv")  
# Access specific column  
print(df.State)
```

Es ist auch möglich mehrere Spalten zu lesen. Dazu wird einfach eine Liste mit den Spaltennamen der rechteckigen Klammer eines `DataFrames` übergeben.

Beispiel:
```python
import pandas as pd  
# Import data from csv-file inside a dataframe  
df = pd.read_csv("data_file.csv")  
# Create a list of column names, which we like to access  
list_of_column_names = ["State", "Area code", "Churn"]  
# Access multiple column  
print(df[list_of_column_names])
```

### Unterschied zwischen einfachen und doppelten eckigen Klammern

Beim Lesen einer Spalte kann man sowohl einfache als auch doppelte eckige Klammern verwendet. Der entscheidende Unterschied liegt im Datentype. Bei den einfachen eckigen Klammern handelt es sich um eine zurückgegebene `Serie` und bei den doppelten eckigen Klammern um ein `DataFrame`.

Beispiel:
```python
import pandas as pd  
# Import data from csv-file inside a dataframe  
df = pd.read_csv("data_file.csv")  
# Create a list of column names, which we like to access  
list_of_column_names = ["State", "Area code", "Churn"]  
# Single square brackets  
single_square_brackets = df["State"]  
# Double square brackets  
double_square_brackets = df[["State"]]  
# Types  
print(type(single_square_brackets))  
print(type(double_square_brackets))
```

## Zeile/Zeilen ausgeben

Durch die Nutzung des Slice Operators (Doppelpunkt), kann man sowohl auf eine als auch auf mehrere Zeilen zugreifen. Als Rückgabe erhält man eine `DataFrame` welches eine oder mehrere Zeilen enthält.

Beispiel:
```python
import pandas as pd  
# Import data from csv-file inside a dataframe  
df = pd.read_csv("avocado_data.csv")  
# Display the 3rd row  
print(df[3:4])  
# Display the 4 until 7 row  
print(df[4:8])
```

Eine weit verbreitete Möglichkeit effektiv auf Zeilen zuzugreifen ist die Nutzung der beiden Methoden `iloc` und `loc` (indexing by integers/keywords).

Diese Methoden ermöglichen durch Indizierung den Zugriff auf Zeilen. 
Dabei unterscheidet man bei den Indizes zwischen numerischen Werten (integers) und Schlüsselwörtern (keywords).

### Zugriff durch iloc (integers)

Die Voraussetzung für die Nutzung der `iloc` Methode ist das vorhanden sein einer nummerischen Indizierung, welche standartmäßig eingestellt ist. Als Rückgabe erhält man eine `Series`, welche alle Informationen zu der jeweiligen Zeile liefert.

Beispiel:
```python
import pandas as pd  
# Import data from csv-file inside a dataframe  
df = pd.read_csv("avocado_data.csv")  
# Display the 3rd row  
print(df.iloc[3])
```

Manchmal möchte man nicht nur eine bestimmte Zeile über den Index ansprechen, sondern auch eine Spalte. Dazu wird ein zweiter Parameter übergeben.

Beispiel:
```python
import pandas as pd  
# Import data from csv-file inside a dataframe  
df = pd.read_csv("avocado_data.csv")  
# Display the value of 3rd row and 1th column  
print(df.iloc[3,1])
```

Man kann auch den `slice` Operator verwenden um einen bestimmten Bereich anzusprechen (Intervalle).

Beispiel:
```python
import pandas as pd  
# Import data from csv-file inside a dataframe  
df = pd.read_csv("avocado_data.csv")  
# Using slice operator to get a range of rows  
print(df.iloc[0:3])
```

### zugriff durch loc (keywords)

Im Vergleich zu der `iloc` Methode verwendet man hier anstelle `int` Indizes bestimmte Schlüsselwörter (keywords) um bestimmte Zeilen auszulesen.

Um Jedoch mit der `loc` Methode arbeiten zu können, muss man zuallererst die standartmäßige Indizierung mit `int` Werten ändern. Erst dann kann man jede einzelne Zeile ansprechen indem man die keywords der `loc` Methode übergibt.

Beispiel:
```python
import pandas as pd  
# Import data from csv-file inside a dataframe  
df = pd.read_csv("avocado_data.csv")  
# Set the column "region" as the new index 
# "inplace" parameter will update current DataFrame "df"  
df.set_index("region", inplace=True)  
print(df)
```

Nachdem die Index Spalte aus keywords besteht, kann man die Spalten ansprechen.

Beispiel:
```python
import pandas as pd  
# Import data from csv-file inside a dataframe  
df = pd.read_csv("avocado_data.csv")  
# Change index of DataFrame  
df.set_index("region", inplace=True)  
# Display Columns with "region" index equal "WestTexNewMexico"  
print(df.loc["WestTexNewMexico"])
```

## Informationen zum DataFrame

Die Methode `info()` gibt eine kurze Zusammenfassung über das jeweilige DataFrame zurück. Bei den Informationen handelt es sich um Anzahl der Spalten, Spaltennamen, Spalten Datentypen, Speichernutzung und noch mehr.

Beispiel:
```python
import pandas as pd  
# Import data from csv-file inside a dataframe  
df = pd.read_csv("avocado_data.csv")  
# Display information about the DataFrame  
print(df.info())
```

## Einzigartige Werte einer Spalte (unique values)

Mithilfe der Methode `unique()` kann man eindeutige Werte einer Spalte finden.
Sie gibt also jeden Wert der in einer spalte vorkommt einmalig aus, egal ob der jeweilige Wert mehrmals in der entsprechenden Spalte vorkommt.
Als Ausgabe erhält man ein Array mit den eindeutigen Werten.

Beispiel:
```python
import pandas as pd  
  
data_finance = {  
   "name": ["William", "Emma", "Sofia", "Markus", "Edward"],  
    "region": ["East", "North", "East", "South", "West"],  
    "sales": [50000, 52000, 90000, 34000, 42000],  
    "expense": [42000, 43000, 400000, 44000, 38000]  
}  
# Create a DataFrame  
df = pd.DataFrame(data=data_finance)  
# Find unique values inside the "region" column  
print(df["region"].unique())
```

## for-Schleife anwenden (loop a DataFrame)

Mit der `iterrows()` Methode ist es möglich jede Zeile eines `DataFrames` anzusprechen. Die Methode gibt den Index der Zeile und die gesamten Daten der Zeile als `Series` zurück.

Beispiel:
```python
import pandas as pd  
  
exam_data = {  
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],  
    'score': [12.5, 9, 16.5, "nan", 9, 20, 14.5, "nan", 8, 19],  
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],  
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}  
  
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']  
  
df = pd.DataFrame(exam_data, index=labels)  
print(df)  
  
for index, row in df.iterrows():  
    print(index)  
    print(row)
```

Wenn Möglich sollte man die Nutzung der for-Schleife vermeiden da bei großen Datenmengen die Laufzeit stark zu leiden hat.

## Anzahl der Spalten und Zeilen

Mit dem Attribut `shape` kann man in einer Tupel-Form `(rows,columns)` die Anzahl der Zeilen und Spalten abfragen

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
print(df.shape)
```

## Anzahl aller Elemente

Mit dem Attribut `size` kann man die Anzahl alles Elemente im `DataFrame` abfragen.

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
print(df.size)
```