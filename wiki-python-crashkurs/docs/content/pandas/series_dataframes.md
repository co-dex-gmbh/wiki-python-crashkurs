
## Erstellen von Series

Bei einer `Series` handelt es sich um ein Objekt, welches eine Sequenz aus Werten und einen damit verbundenen Index enthält.

Die Datenstruktur `Series` ist wie eine standartmäßige `Liste` mit dem Unterschied, dass `Series` nur Werte eines einzelnen Datentyps enthalten können.

Das einfachste Beispiel für die Erstellung einer `Series` ist die Nutzung der Klasse `Series`.  Dazu muss man eine `Liste` oder z.B. einen `numpy-array` dem Objekt der Klasse `Series` übergeben:
```python
import pandas as pd  
from pandas import Series  
# A list or array  
my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18]  
# Create a Series(-Objekt) from a list or array  
data_series_list = Series(my_list)  
# Display Series  
print(data_series_list)
```

Man kann auch ein `Dictionary` verwenden um eine `Series` zu erstellen. Dazu muss man einfach das `Dictionary` dem `Series`-Objekt übergeben. Dabei werden die `keys` des `Dictionary` als Indizes verwendet:
```python
import pandas as pd  
from pandas import Series  
# Create a dictionary  
city_population = {  
    "Berlin": 3_669_491,  
                    "Hamburg": 1_847_253,  
                    "München": 1_484_226,  
                    "Köln": 1_087_863,  
                    "Frankfurt am Main": 763_380,  
                    "Stuttgart": 635_911,  
                    "Düsseldorf": 621_877,  
                    "Leipzig": 593_145,  
                    "Dortmund": 588_250,  
                    "Essen": 582_760,  
                    "Bremen": 567_559,  
                    "Dresden": 556_780,  
                    "Hannover": 536_925,  
                    "Nürnberg": 518_370  
                   }  
# Create a Series from a dictionary  
data_series_dict = Series(data=city_population)  
# Display the Series  
print(data_series_dict)
```
## Indexierung ändern

Standartmäßig wird jeder Datenpunkt über einen Index identifiziert. Dabei fängt der Index bei `0` an und endet bei `Anzahl der Elemente - 1`.
Häufig möchte man jedoch eine andere Indexierung der Datenpunkte haben, dazu muss man in das `Series`(-Objekt) den Parameter `index` übergeben:
```python
import pandas as pd  
from pandas import Series  
# A list or array  
my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18]  
my_index = ["d", "e", "f", "g", "h", "i", "j", "k", "l"]  
# Create a Series from a list or array  
data_series_list = Series(data=my_list, index=my_index)  
# Display Series  
print(data_series_list)
```


## Bestimmte Werte ausgeben

Durch die Nutzung eckiger Klammern und der Angabe des Index ist die Ausgabe bestimmter einzelner Werte möglich:
```python
import pandas as pd  
from pandas import Series  
# A list or array  
my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18]  
my_index = ["d", "e", "f", "g", "h", "i", "j", "k", "l"]  
# Create a Series from a list or array  
data_series_list = Series(data=my_list, index=my_index)  
# Display specific value  
print(data_series_list["f"])  
# Other method with same result  
print(data_series_list[2])
```

## Mehrere Werte ausgeben

Möchte man mehrere Werte aus einer `Series` ausgeben, dann muss man die dazugehörigen Indizes in einer Liste übergeben. Dadurch entstehen doppelte eckige Klammern. Als Rückgabe erhält man wieder eine `Series` die man entweder speichern kann, für weitere Verwendungen, oder einfach nur anzeigen:
```python
import pandas as pd  
from pandas import Series  
# A list or array  
my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18]  
my_index = ["d", "e", "f", "g", "h", "i", "j", "k", "l"]  
# Create a Series from a list or array  
data_series_list = Series(data=my_list, index=my_index)  
# Display multiple values, Series will be returned  
print(data_series_list[["l", "j", "d"]])
```

## Mathematische Operatoren anwenden

Man kann auf alle Werte einer `Series` mathematische bzw. logische Operatoren anwenden:
```python
import pandas as pd  
from pandas import Series  
# A list or array  
my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18]  
my_index = ["d", "e", "f", "g", "h", "i", "j", "k", "l"]  
# Create a Series from a list or array  
data_series_list = Series(data=my_list, index=my_index)  
# Using mathematical operators  
print(data_series_list * 2)  # Double each value  
print(data_series_list % 2)  # Check if values are even  
print(data_series_list < 10)  # Check which values are less than 10
```

## Series filtern

Oft hat man nur Interesse an einer Teilmenge der `Series`. Manchmal möchte man nur Werte größer als einen bestimmten Wert haben oder nur ganze Werte und so weiter. Dazu muss man logische Operatoren verwenden um eine `Series` mit booleschen Werten zu erhalten. Anschließend werden die booleschen Werte in die `Series` eingesetzt:
```python
import pandas as pd  
from pandas import Series  
# A list or array  
my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18]  
my_index = ["d", "e", "f", "g", "h", "i", "j", "k", "l"]  
# Create a Series from a list or array  
data_series_list = Series(data=my_list, index=my_index)  
# Filtering values  
greater_than_8_bool = data_series_list > 8  # Firstly create boolean values  
print(greater_than_8_bool)  
greater_than_8 = data_series_list[greater_than_8_bool]  # Then insert boolean values inside Series  
print(greater_than_8)
```

Weiteres Beispiel:
```python
import pandas as pd  
from pandas import Series  
# A list or array  
my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18]  
my_index = ["d", "e", "f", "g", "h", "i", "j", "k", "l"]  
# Create a Series from a list or array  
data_series_list = Series(data=my_list, index=my_index)  
# Filtering values  
# We will get a Series with only 4 and 8  
data_series_list_equal = (data_series_list == 4) | (data_series_list == 8)  # Here we get boolean values  
print(data_series_list_equal)  
print(data_series_list[data_series_list_equal])  # Display only 4 and 8
```

Die wohl interessanteste Datenstruktur ist ein `DataFrame`, denn damit wird man am häufigsten arbeiten. Es handelt sich dabei um eine tabellarische Auftragung zugehöriger Daten. Klassischerweise stehen in den Reihen der Tabelle die Einzelmessungen und in den Spalten die festgehaltenen Werte einer Messung.

Die Erstellung eines `DataFrames` kann auf viele Arten erfolgen. Am häufigsten liegt eine Datei wie z.B. eine CSV-Datei vor, welche die zu untersuchenden Daten beinhaltet. Aber auch die Erstellung eines `DataFrames` aus einem `Dictionary` oder einer Datenbank ist möglich.

Bei den Beispielen wird eine  Datensammlung über Avocados aus dem Jahre 2018 verwendet, hier findet man die dazugehörige CSV-Datei:
[Avocado Daten](../avocado_data.csv)


## Erstellen aus einer CSV-Datei

Dazu wird die Methode `read_csv` verwendet.

Beispiel:
```python
import pandas as pd  
# Import data from csv-file inside a dataframe  
df = pd.read_csv("avocado_data.csv")  
print(df)
```

##  Erstellen aus einer Dictionary

Es kann auch mal vorkommen, dass man eine kleine Menge an Daten als ein `DataFrame` haben möchte. Dazu kann man häufig ein eigenes `Dictionary` erstellen und anschließend daraus ein `DataFrame erstellen.

Dabei geht man davon aus dass:
- die `keys` des `Dictionary` die Spaltennamen sind,
- die `values` des `Dictionary` die Daten sind, welche als Liste gespeichert sind.

Beispiel:
```python
import pandas as pd  
# This Dictionary is given  
tempdict = {  
    "col1": [1, 2, 3],  
    "col2": [4, 5, 6],  
    "col3": [7, 8, 9]  
}  
# Create a dataframe from this dictionary  
dictdf = pd.DataFrame.from_dict(tempdict)  
print(dictdf)
```

## Entfernen eines DataFrame

Durch das Schlüsselwort `del` kann man ein DataFrame löschen:
```python
import pandas as pd  
# Import data from csv-file inside a dataframe  
df = pd.read_csv("data_file.csv")  
# Replace True with 1 and False with 0 inside the Chrun Binary column  
df["Churn Binary"] = df["Churn"].apply(lambda x: 1 if x==True else 0)  
# Delete the DataFrame
del df
```