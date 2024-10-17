

In R sind DataFrames ein direkter Bestandteil der Sprache. In Python gibt es keine eingebaute Datenstruktur, die einem DataFrame entspricht. Jedoch gibt es die Bibliothek `pandas`, die eine Datenstruktur namens `DataFrame` bereitstellt, die ähnlich zu einem DataFrame in R ist.

## Was ist Pandas?

Pandas ist eine Open-Source-Bibliothek, die in Python geschrieben wurde und die Datenmanipulation und -analyse erleichtert. Die Bibliothek basiert dabei auf Numpy, welches eine weitere Bibliothek ist, die in Python für numerische Berechnungen verwendet wird.


## Erste Schritte mit Pandas

Wir können Pandas beispielsweise verwenden, um Daten aus einer CSV-Datei zu lesen und in einem DataFrame zu speichern. In Pandas werden zwei neue Datenstrukturen eingeführt: `DataFrames` und `Series`. Am Anfang werden wir uns mit der Datenstruktur `dataframes` auch mit `df` abgekürzt, vertraut machen.

Bevor man mit der Pandas-Bibliothek arbeiten kann, muss man sie importieren. Da es sich nicht um eine eingebaute Bibliothek handelt, muss man sie zunächst installieren. Nicht vergessen die Dokumentation zu dieser Bibliothek zu lesen!

!!! note
    Die nachfolgenden Datensätze können [hier](https://github.com/laxmimerit/All-CSV-ML-Data-Files-Download/tree/master) heruntergeladen werden.
    
Erste Schritte:
```python
import pandas
# Lets read a csv
data = pandas.read_csv("https://github.com/laxmimerit/All-CSV-ML-Data-Files-Download/blob/master/bigmac.csv")
# Display the data inside the csv
print(data)
# Just get the column called Country
countries = data["Country"]
print("# ------------------------------------ #")
# Display only temperatures
print(countries)
```

In Pandas haben wir zwei wichtige Datentypen:

- dataframe, es ist äquivalent zur Tabelle wie im ersten Beispiel.
- series, es ist eine Spalte wie eine Liste

Wenn man diese beiden Datentypen versteht, dann ist man auf einem guten Weg, diese Bibliothek zu verstehen!
Zu Beginn des Lernens von Pandas sollte man sich die zwei Klassen "DataFrame" und "Series" genauer ansehen (Dokumentation).

Berechnen wir als erstes mittel der `pandas` Bibliothek den durchschnittlichen Preis eines Big Macs in den verschiedenen Ländern:

```python
...
average_price = data["Price in US Dollars"].mean()
print(average_price)
```

{{ task(file="tasks/pandas1.yaml") }}

Manchmal möchte man einfach nur eine Zeile der Tabelle erhalten:
```python
row_day = data[data["Country"] == "Germany"]
print(row_day)
```

Oder man möchte die Reihe mit dem höchsten Preis finden:
```python
max_price = data["Price in US Dollars"].max()

row_max_price = data[data["Price in US Dollars"] == max_price]
print(row_max_price)

```

Wir können auch eine neue Spalte erstellen, in der die Preise in € umgerechnet stehen:

```python
...
data["Price in EUR"] = data["Price in US Dollars"] * 1.09
```

Man kann auch einen `dataframe` von Grund auf neu erstellen:
```python
import pandas
# You have given data:
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
# We have to create a data frame from this dictionary
data = pandas.DataFrame(data_dict)
print(data)
# We can even convert our data frame to a csv
data.to_csv("new_data.csv")
    
```

