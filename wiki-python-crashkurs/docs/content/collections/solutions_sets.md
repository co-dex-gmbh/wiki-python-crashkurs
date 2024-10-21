# Lösungen

### 1. **Set Erstellung**
```python
mein_set = {1, 2, 3, 4, 5}
print(mein_set)
```

### 2. **Duplikatentfernung**
```python
meine_liste = [1, 2, 2, 3, 4, 5, 5, 6]
mein_set = set(meine_liste)
print(mein_set)
```

### 3. **Elemente Hinzufügen**
```python
mein_set = {1, 2, 3, 4, 5}
mein_set.update([6, 7, 8])
print(mein_set)
```

### 4. **Element Entfernen**
```python
mein_set = {1, 2, 3, 4, 5, 6, 7, 8}
mein_set.remove(5)
print(mein_set)
```

### 5. **Set Durchlaufen**
```python
mein_set = {1, 2, 3, 4, 5}
for element in mein_set:
   print(element)
```

### 6. **Set Union**
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print(union_set)
```

### 7. **Set Schnittmenge**
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
schnittmenge = set1 & set2
print(schnittmenge)
```

### 8. **Set Differenz**
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
differenz = set1 - set2
print(differenz)
```

### 9. **Symmetrische Differenz**
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
sym_differenz = set1 ^ set2
print(sym_differenz)
```

### 10. **Set Länge**
```python
mein_set = {1, 2, 3, 4, 5}
print(len(mein_set))
```

### 11. **Set Mitgliedschaftstest**
```python
mein_set = {1, 2, 3, 4, 5}
print(3 in mein_set)
```

### 12. **Set Leeren**
```python
mein_set = {1, 2, 3, 4, 5}
mein_set.clear()
print(mein_set)
```

### 13. **Subsets**
```python
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print(set1.issubset(set2))
```

### 14. **Supersets**
```python
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print(set2.issuperset(set1))
```

    