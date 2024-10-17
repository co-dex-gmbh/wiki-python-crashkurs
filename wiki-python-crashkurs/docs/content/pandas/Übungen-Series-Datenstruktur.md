Für einige Aufgaben ist es notwendig selbstständig die nötigen Funktionen, Methoden, Attribute durch Internet Recherche heraus zu finden!


# Aufgaben

## 1. Aufgabe

Write a Pandas program to create and display a one-dimensional array-like object containing an array of data using Pandas module.

## 2. Aufgabe

Write a Pandas program to convert a Panda module Series to Python list and it's type.

## 3. Aufgabe

Write a Pandas program to add, subtract, multiple and divide two Pandas Series. 
Sample Series: `[2, 4, 6, 8, 10], [1, 3, 5, 7, 9]`

## 4. Aufgabe

Write a Pandas program to compare the elements of the two Pandas Series.
Sample Series: `[2, 4, 6, 8, 10], [1, 3, 5, 7, 10]`

## 5. Aufgabe

Write a Pandas program to convert a dictionary to a Pandas series.
```
Original dictionary:  
{'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}  
Converted series:  
a 100  
b 200  
c 300  
d 400  
e 800  
dtype: int64
```

## 6. Aufgabe

Write a Pandas program to convert a NumPy array to a Pandas series. 
```
NumPy array:  
[10 20 30 40 50]  
Converted Pandas series:  
0 10  
1 20  
2 30  
3 40  
4 50  
dtype: int64
```

## 7. Aufgabe

Write a Pandas program to change the data type of given a column or a Series.
```
Original Data Series:  
0 100  
1 200  
2 python  
3 300.12  
4 400  
dtype: object  
Change the said data type to numeric:  
0 100.00  
1 200.00  
2 NaN  
3 300.12  
4 400.00  
dtype: float64
```

## 8. Aufgabe

Write a Pandas program to convert the first column of a DataFrame as a Series.
```
Original DataFrame:  
col1 col2 col3  
0 1 4 7  
1 2 5 5  
2 3 6 8  
3 4 9 12  
4 7 5 1  
5 11 0 11  
1st column as a Series:  
0 1  
1 2  
2 3  
3 4  
4 7  
5 11  
Name: col1, dtype: int64  
<class 'pandas.core.series.Series'>
```

## 9. Aufgabe

Write a Pandas program to convert a given Series to an array.
```
Sample Output:  
Original Data Series:  
0 100  
1 200  
2 python  
3 300.12  
4 400  
dtype: object  
Series to an array  
['100' '200' 'python' '300.12' '400']
```

## 10. Aufgabe

Write a Pandas program to convert Series of lists to one Series.   
```
Sample Output:  
Original Series of list  
0 [Red, Green, White]  
1 [Red, Black]  
2 [Yellow]  
dtype: object  
One Series  
0 Red  
1 Green  
2 White  
3 Red  
4 Black  
5 Yellow  
dtype: object
```

## 11. Aufgabe

Write a Pandas program to sort a given Series.
```
Sample Output:  
Original Data Series: 
0 '100'
1 '200'
2 'python' 
3 '300.12'  
4 '400'  
dtype: object  
0 100  
1 200  
3 300.12  
4 400  
2 python  
dtype: object
```

## 12. Aufgabe

Write a Pandas program to add some data to an existing Series. 
```
Sample Output:  
Original Data Series:  
0 "100"  
1 "200"  
2 "python"  
3 "300.12"  
4 "400"  
dtype: object  
Data Series after adding some data:  
0 "100"  
1 "200"  
2 "python"  
3 "300.12"  
4 "400"   
5 "500"  
6 "php"  
dtype: object
```

## 13. Aufgabe

Write a Pandas program to create a subset of a given series based on value and condition. 
```
Sample Output:  
Original Data Series:  
0 0  
1 1  
2 2  
3 3  
4 4  
5 5  
6 6  
7 7  
8 8  
9 9  
10 10  
dtype: int64  
Subset of the above Data Series:  
0 0  
1 1  
2 2  
3 3  
4 4  
5 5  
dtype: int64
```

## 14. Aufgabe

Write a Pandas program to change the order of index of a given series.
```
Sample Output:  
Original Data Series:  
A 1  
B 2  
C 3  
D 4  
E 5  
dtype: int64  
Data Series after changing the order of index:  
E 2  
D 1  
C 3  
B 4  
A 5  
dtype: int64
```

## 15. Aufgabe

Write a Pandas program to create the mean and standard deviation of the data of a given Series.
```
Sample Output:  
Original Data Series:  
0 1  
1 2  
2 3  
3 4  
4 5  
5 6  
6 7  
7 8  
8 9  
9 5  
10 3  
dtype: int64  
Mean of the said Data Series:  
4.818181818181818  
Standard deviation of the said Data Series:  
2.522624895547565
```

## 16. Aufgabe

Write a Pandas program to get the items of a given series not present in another given series.
```
Sample Output:  
Original Series:  
sr1:  
0 1  
1 2  
2 3  
3 4  
4 5  
dtype: int64  
sr2:  
0 2  
1 4  
2 6  
3 8  
4 10  
dtype: int64  
Items of sr1 not present in sr2:  
0 1  
2 3  
4 5  
dtype: int64
```

## 17. Aufgabe

Write a Pandas program to get the items which are not common of two given series.
```
Sample Output:  
Original Series:  
sr1:  
0 1  
1 2  
2 3  
3 4  
4 5  
dtype: int64  
sr2:  
0 2  
1 4  
2 6  
3 8  
4 10  
dtype: int64  
Items of a given series not present in another given series:  
0 1  
2 3  
4 5  
5 6  
6 8  
7 10  
dtype: int64
```


## 18. Aufgabe

Write a Pandas program to compute the minimum, 25th percentile, median, 75th, and maximum of a given series.
```
Sample Output:  
Original Series:  
0 3.000938  
1 11.370722  
2 14.612143  
3 8.990256  
4 13.925283  
5 12.056875  
.... 
17 14.118931  
18 8.247458  
19 5.526727  
dtype: float64  
Minimum, 25th percentile, median, 75th, and maximum of a given series:  
[3.00093811 8.09463867 10.23353705 12.21537733 14.61214321]
```


# Lösungen

## 1. Aufgabe

```python
import pandas as pd  
  
array = [1, 2, 3, 4, 5, 6, 7]  
serries = pd.Series(array)  
print(serries)
```


## 2. Aufgabe

```python
import pandas as pd  
  
# Create an array or list  
array = [1, 2, 3, 4, 5, 6, 7]  
serries = pd.Series(array)  
# Convert back to a list  
back_to_list = serries.to_list()  
# Check the type  
print(type(back_to_list))
```

## 3. Aufgabe

```python
import pandas as pd  
from pandas import Series  
  
series_1 = Series([2, 4, 6, 8, 10])  
series_2 = Series([1, 3, 5, 7, 9])  
  
def add_series(series_1, series_2):  
    return series_1 + series_2  
  
  
def multiply_series(series_1, series_2):  
    return series_1 * series_2  
  
  
def subtract_series(series_1, series_2):  
    return series_1 - series_2  
  
  
def divide_series(series_1, series_2):  
    return series_1 / series_2  
  
# ---------- MAIN ---------- #  
series_sum = add_series(series_1, series_2)  
print(series_sum)  
series_multiply = multiply_series(series_1, series_2)  
print(series_multiply)  
difference_series = subtract_series(series_1, series_2)  
print(difference_series)  
division_series = divide_series(series_1, series_2)  
print(division_series)
```

## 4. Aufgabe

```python
import pandas as pd  
from pandas import Series  
  
series_1 = Series([2, 4, 6, 8, 10])  
series_2 = Series([1, 3, 5, 7, 9])  
  
print(f"series_1 greater than series_2:\n{series_1 > series_2}")  
print(f"series_1 less than series_2:\n{series_1 < series_2}")  
print(f"series_1 equal series_2:\n{series_1 == series_2}")
```

## 5. Aufgabe

```python
import pandas as pd  
from pandas import Series  
  
dict_data = {  
    'a': 100,  
    'b': 200,  
    'c': 300,  
    'd': 400,  
    'e': 800  
}  
  
series_dict = Series(data=dict_data)  
print(series_dict)
```

## 6. Aufgabe

```python
import pandas as pd  
from pandas import Series  
import numpy as np  
  
np_array = np.array([10, 20, 30, 40, 50])  
  
series_dict = Series(data=np_array)  
print(series_dict)
```

## Aufgabe 7

```python
import pandas as pd  
from pandas import Series  
  
data_Series = Series([100, 200, "python", 300.12, 400])  
  
data_Series_converted = pd.to_numeric(data_Series, errors="coerce")  
print(data_Series_converted)
```

## 8. Aufgabe

```python
import pandas as pd  
from pandas import Series, DataFrame  
dict_for_df = {  
    "col1": [1, 2, 3, 4, 7, 11],  
    "col2": [4, 5, 6, 9, 5, 0],  
    "col3": [7, 5, 8, 12, 1, 11]  
}  
df = DataFrame(data=dict_for_df)  
column_as_series = Series(dict_for_df["col1"])  
print(column_as_series)
```

## 9. Aufgabe

```python
import pandas as pd  
from pandas import Series, DataFrame  
import numpy as np  
  
original_data_series = Series([100, 200, "python", 300.12, 400])  
# without ".values.tolist()" you will get only a "str" datatype  
series_as_array = np.array(original_data_series.values.tolist())  
print(series_as_array)  
# For test:  
print(type(series_as_array))  
print(type(series_as_array[2]))
```

## Aufgabe 10

```python
import pandas as pd  
from pandas import Series, DataFrame  
  
series_of_lists = Series(  
    [  
    ["Red", "Green", "White"], ["Red", "Black"], ["Yellow"]  
    ]  
)  
print(series_of_lists)  
# Extract each element to a list  
list_of_elemnts = []  
for list in series_of_lists:  
    list_of_elemnts.extend(list)  
  
print("-----")  
print(list_of_elemnts)  
# Convert list to Series  
final_series = Series(list_of_elemnts)  
print(final_series)
```

## Aufgabe 11

```python
import pandas as pd  
from pandas import Series, DataFrame  
  
series = Series(["100", "200", "python", "300.12", "400"])  
print(series)  
series_sorted = series.sort_values()  
print(series_sorted)
```

## Aufgabe 12

```python
import pandas as pd  
from pandas import Series, DataFrame  
  
series = Series(["100", "200", "python", "300.12", "400"])  
print(series)  
series_added = pd.concat([series, Series(["500", "php"])], ignore_index=True)  
print(series_added)
```

## Aufgabe 13

```python
import pandas as pd  
from pandas import Series, DataFrame  
  
series = Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  
series_condition = series <= 5  
print(series_condition)  
series_filtered = series[series_condition]  
print(series_filtered)
```

## 14. Aufgabe

```python
import pandas as pd  
from pandas import Series, DataFrame  
  
series = Series([1, 2, 3, 4, 5], index=["A", "B", "C", "D", "E"])  
series.sort_index(ascending=False, inplace=True)  
print(series)
```

## 15. Aufgabe

```python
import pandas as pd  
from pandas import Series, DataFrame  
  
series = Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 3])  
print(f"The mean is: {series.mean()}")  
print(f"The standart deviation is: {series.std()}")
```

## 16. Aufgabe

```python
import pandas as pd  
from pandas import Series, DataFrame  
  
series_1 = Series([1, 2, 3, 4, 5])  
series_2 = Series([2, 4, 6, 8, 10])  
print("Items of series_1 not present in series_2:")  
filter_values = series_1.isin(series_2)  
# Change True to False and False to True  
filtered_values = ~filter_values  
print(series_1[filtered_values])
```

## 17. Aufgabe

```python
import pandas as pd  
from pandas import Series, DataFrame  
  
s_1 = Series([1, 2, 3, 4, 5])  
s_2 = Series([2, 4, 6, 8, 10])  
  
s1_not_in_s2 = ~s_1.isin(s_2)  
bool_1 = s1_not_in_s2  
s2_not_in_s1 = ~s_2.isin(s_1)  
bool_2 = s2_not_in_s1  
  
filtered = pd.concat([s_1[bool_1], s_2[bool_2]])  
print(filtered)
```

## 18. Aufgabe

```python
import pandas as pd  
from pandas import Series, DataFrame  
import numpy as np  
# Generate array with float numbers between 1 and 20, 20 times  
random_numbs = np.random.uniform(1, 20, 20)  
given_series = Series(random_numbs)  
min_given_series = given_series.min()  
max_given_series = given_series.max()  
precentile_25 = given_series.quantile(q=0.25)  
median = given_series.quantile(q=0.5)  
precentile_75 = given_series.quantile(q=0.75)  
print(f"max value: {max_given_series}\nmin value: {min_given_series}\n25th percentile: {precentile_25}\n75th percentile: {precentile_75}")
```