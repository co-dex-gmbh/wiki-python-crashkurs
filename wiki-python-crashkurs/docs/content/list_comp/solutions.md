# Lösungen für einfache List Comprehensions

### 1. **Quadrate erstellen**

```python
quadrate = [i ** 2 for i in range(1, 11)]
```

### 2. **Zeichenkettenlängen**

```python
wortlaengen = [len(wort) for wort in ["Hallo", "Welt", "Python"]]
```

### 3. **Absolute Werte**

```python
absolute = [abs(i) for i in [-1, -2, 3, -4, 5]]
```

### 4. **String in Großbuchstaben**

```python
grossbuchstaben = [s.upper() for s in ["hallo", "welt", "python"]]
```

### 5. **Wurzeln ziehen**

```python
wurzeln = [i ** 0.5 for i in [1, 4, 9, 16, 25]]
```

### 6. **Tupel erstellen**

```python
tupel_liste = [(i, i * i) for i in range(1, 11)]
```

### 7. **Teile von Strings**

```python
erste_zeichen = [wort[0] for wort in ["Hallo", "Welt", "Python"]]
```

### 8. **Durchschnittswerte**

```python
durchschnitt = [(liste[i] + liste[i + 1]) / 2 for i in range(len(liste) - 1)]
```


### 9. **Gerade Zahlen**

```python
gerade = [i for i in range(1, 21) if not i % 2]
```

### 10. **Filtern nach Bedingung**

```python
teilbar_durch_3 = [i for i in range(1, 21) if i % 3 == 0]
```

### 11. **Nicht-leere Strings**

```python
nicht_leer = [s for s in ["Hallo", "", "Welt", ""] if s]
```

### 12. **Fizz Buzz**

```python
fizz_buzz = ["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i) for
             i in range(1, 16)]
```

### 13. **Bedingung fehlt**

```python
paare = [(i, j) for i in range(1, 11) for j in range(1, 11) if i + j == 10]
```

### 14. **Liste von Listen abflachen**

```python
abgeflacht = [element for sublist in [[1, 2], [3, 4], [5, 6]] for element in sublist]
```

### 15. Verschachtelung
```python
a = [(i,j) for i in range(2) for j in range(4)]

b = [[i*j for i in range(4)] for j in range(4)]

c = [[i+j for i in "abc"] for j in "ABC"]
```

### 16: Dictionary Comprehensions

```python
a = {i: i * i for i in range(1, 11)}

words = ['Hase', 'Hund']
b = {word: [letter for letter in word] for word in words}

my_dict = {'A': 1, 'B': 2, 'C': 3}
swapped_my_dict = {v: k for k, v in my_dict.items()}
```

### 17. Anzahl der Vokale zählen:

```python
text = "Python ist großartig."
anzahl_vokale = sum(1 for char in text if char.lower() in "aeiou")
print(anzahl_vokale)
```

### 18. Use tuple
```python
my_tuple = tuple(i ** 2 for i in range(11))
```
