 
# 1  Assignment

Write a Pandas program to get the the data inside a DataFrame.

Sample data: 
```
{'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
```

Expected Outout:
```
X Y Z  
0 78 84 86  
1 85 94 97  
2 96 89 96  
3 80 83 72  
4 86 86 83
```

## Solution

```python
import pandas as pd  
sample_data = {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}  
df = pd.DataFrame(sample_data)  
print(df)
```

# 2  Assignment

Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels.

Sample Python dictionary data:
```
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],  
'score': [12.5, 9, 16.5, "nan", 9, 20, 14.5, "nan", 8, 19],  
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],  
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
```

Sample Python list labels:
```
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
```

Expected Outout:
```
attempts name qualify score  
a 1 Anastasia yes 12.5  
b 3 Dima no 9.0  
.... i 2 Kevin no 8.0  
j 1 Jonas yes 19.0
```

## Solution

```python
import pandas as pd  
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],  
'score': [12.5, 9, 16.5, "nan", 9, 20, 14.5, "nan", 8, 19],  
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],  
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}  
  
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']  
  
df = pd.DataFrame(exam_data, index=labels)  
print(df)
```

# 3  Assignment

 Write a Pandas program to display a summary of the basic information about a specified DataFrame and its data.

Sample Python dictionary:
```
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],  
'score': [12.5, 9, 16.5, "nan", 9, 20, 14.5, "nan", 8, 19],  
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],  
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
```

Sample list labels:
```
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
```

Expected Output:
```
Summary of the basic information about this DataFrame and its data:
<class 'pandas.core.frame.DataFrame'>
Index: 10 entries, a to j
Data columns (total 4 columns):
attempts    10 non-null int64
name        10 non-null object
qualify     10 non-null object
score       8 non-null float64
dtypes: float64(1), int64(1), object(2)
memory usage: 400.0+ bytes
None
```

## Solution

```python
import pandas as pd  
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],  
'score': [12.5, 9, 16.5, "nan", 9, 20, 14.5, "nan", 8, 19],  
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],  
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}  
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']  
  
df = pd.DataFrame(exam_data, index=labels)  
print("Summary of the basic information about this DataFrame and its data:")  
print(df.info())
```

# 4  Assignment

Write a Pandas program to get the first 3 rows of a given DataFrame.

Sample Python dictionary data:
```
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],  
'score': [12.5, 9, 16.5, "nan", 9, 20, 14.5, "nan", 8, 19],  
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],  
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
```

Sample list labels:
```
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
```

Expected Output:
```
First three rows of the data frame:                                    
   attempts       name qualify  score                                  
a         1  Anastasia     yes   12.5                                  
b         3       Dima      no    9.0                                  
c         2  Katherine     yes   16.5
```

## Solution

```python
import pandas as pd  
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],  
'score': [12.5, 9, 16.5, "nan", 9, 20, 14.5, "nan", 8, 19],  
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],  
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}  
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']  
  
df = pd.DataFrame(exam_data, index=labels)  
print("First three rows of the data frame:")  
print(df.head(3))
```

# 5  Assignment

Write a Pandas program to select the 'name' and 'score' columns from the following DataFrame.

Sample Python dictionary data:
```
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],  
'score': [12.5, 9, 16.5, "nan", 9, 20, 14.5, "nan", 8, 19],  
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],  
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
```

Sample list labels:
```
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
```

Expected Output:
```
Select specific columns:                                               
        name  score                                                    
a  Anastasia   12.5                                                    
b       Dima    9.0                                                    
c  Katherine   16.5                                                    
d      James    NaN                                                    
e      Emily    9.0                                                    
f    Michael   20.0                                                    
g    Matthew   14.5                                                    
h      Laura    NaN                                                    
i      Kevin    8.0                                                    
j      Jonas   19.0
```

## Solution

```python
import pandas as pd  
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],  
'score': [12.5, 9, 16.5, "nan", 9, 20, 14.5, "nan", 8, 19],  
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],  
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}  
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']  
  
df = pd.DataFrame(exam_data, index=labels)  
print("Select specific columns: ")  
print(df[["name", "score"]])
```

# 6  Assignment

Write a Pandas program to select the specified columns and rows from a given data frame. Select 'name' and 'score' columns in rows 1, 3, 5, 6 from the following data frame.

Sample Python dictionary data:
```
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],  
'score': [12.5, 9, 16.5, "nan", 9, 20, 14.5, "nan", 8, 19],  
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],  
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
```

Sample list labels:
```
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
```

Expected Output:
```
Select specific columns and rows:
   score qualify
b    9.0      no
d    NaN      no
f   20.0     yes
g   14.5     yes
```

## Solution

```python
import pandas as pd  
  
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],  
'score': [12.5, 9, 16.5, "nan", 9, 20, 14.5, "nan", 8, 19],  
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],  
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}  
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']  
  
df = pd.DataFrame(exam_data, index=labels)  
print(df.iloc[[1, 3, 5, 6], [1, 3]])
```


# 7  Assignment

Write a Pandas program to select the rows where the number of attempts in the examination is greater than 2.

Sample Python dictionary data:
```
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],  
'score': [12.5, 9, 16.5, "nan", 9, 20, 14.5, "nan", 8, 19],  
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],  
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
```

Sample list labels:
```
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
```

Expected Output:
```
Select specific columns:                                               
Number of attempts in the examination is greater than 2:
      name  score  attempts qualify
b     Dima    9.0         3      no
d    James    NaN         3      no
f  Michael   20.0         3     yes
```

## Solution

```python
import pandas as pd  
  
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],  
'score': [12.5, 9, 16.5, "nan", 9, 20, 14.5, "nan", 8, 19],  
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],  
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}  
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']  
  
df = pd.DataFrame(exam_data, index=labels)  
df = df[df["attempts"] > 2]  
print(df)
```

